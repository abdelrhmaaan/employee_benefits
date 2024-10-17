import io
import xlsxwriter
from odoo import http
from odoo.http import request

class EmployeeBenefitExcelReportController(http.Controller):

    @http.route('/employee_benefit/excel_report', type='http', auth='user')
    def generate_employee_benefit_report(self):
        
        employees = request.env['hr.employee'].search([])
        benefits = request.env['hr.employee.benefits'].search([])

        
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        worksheet = workbook.add_worksheet('Employee Benefit Report')

        
        bold = workbook.add_format({'bold': True})
        currency_format = workbook.add_format({'num_format': '$#,##0.00'})

        
        worksheet.write(0, 0, 'Employee Name', bold)
        worksheet.write(0, 1, 'Department', bold)
        worksheet.write(0, 2, 'Job Title', bold)
        worksheet.write(0, 3, 'Total Benefit Value', bold)
        worksheet.write(0, 4, 'Health Insurance', bold)
        worksheet.write(0, 5, 'Transportation', bold)
        worksheet.write(0, 6, 'Bonus', bold)
        worksheet.write(0, 7, 'Other', bold)

    
        row = 1
        for employee in employees:
            benefits = request.env['hr.employee.benefits'].search([('employee_id', '=', employee.id)])
            total_benefits = sum(benefits.mapped('amount'))
            health_insurance = sum(benefits.filtered(lambda b: b.benefit_type == 'health_insurance').mapped('amount'))
            transportation = sum(benefits.filtered(lambda b: b.benefit_type == 'transportation').mapped('amount'))
            bonus = sum(benefits.filtered(lambda b: b.benefit_type == 'bonus').mapped('amount'))
            other = sum(benefits.filtered(lambda b: b.benefit_type == 'other').mapped('amount'))

            worksheet.write(row, 0, employee.name)
            worksheet.write(row, 1, employee.department_id.name)
            worksheet.write(row, 2, employee.job_id.name)
            worksheet.write(row, 3, total_benefits, currency_format)
            worksheet.write(row, 4, health_insurance, currency_format)
            worksheet.write(row, 5, transportation, currency_format)
            worksheet.write(row, 6, bonus, currency_format)
            worksheet.write(row, 7, other, currency_format)

            row += 1

        # Summarize total benefit costs by department
        worksheet.write(row + 1, 0, 'Department Summary', bold)
        row += 2
        departments = request.env['hr.department'].search([])
        for department in departments:
            dept_benefits = request.env['hr.employee.benefits'].search([('employee_id.department_id', '=', department.id)])
            total_dept_benefits = sum(dept_benefits.mapped('amount'))

            worksheet.write(row, 0, department.name)
            worksheet.write(row, 1, total_dept_benefits, currency_format)

            row += 1

        # Close the workbook and return the response
        workbook.close()
        output.seek(0)


        response = request.make_response(
            output.read(),
            headers=[
                ('Content-Type', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'),
                ('Content-Disposition', 'attachment; filename=Employee_Benefit_Report.xlsx;')
            ]
        )
        return response
