from odoo import models, fields

class EmployeeBenefitReport(models.Model):
    _name = 'employee.benefit.report'
    _description = 'Employee Benefit Report'
    _auto = False 

    # Employee Information
    employee_id = fields.Many2one('hr.employee', string='Employee', readonly=True)
    employee_name = fields.Char(string='Employee Name', readonly=True)
    department_id = fields.Many2one('hr.department', string='Department', readonly=True)
    job_id = fields.Many2one('hr.job', string='Job Title', readonly=True)
    manager_id = fields.Many2one('hr.employee', string='Manager', readonly=True)

    # Benefit Information
    benefit_type = fields.Selection([
        ('health', 'Health Insurance'),
        ('transport', 'Transportation'),
        ('bonus', 'Bonus'),
    ], string='Benefit Type', readonly=True)
    total_benefit_value = fields.Float(string='Total Benefit Value', readonly=True)


    def init(self):
        self._cr.execute("""
            CREATE OR REPLACE VIEW employee_benefit_report AS (
                SELECT
                    eb.id AS id,
                    e.id AS employee_id,
                    e.name AS employee_name,
                    e.department_id AS department_id,
                    e.job_id AS job_id,
                    e.parent_id AS manager_id,
                    eb.benefit_type AS benefit_type,
                    eb.amount AS total_benefit_value
                FROM hr_employee_benefits eb
                JOIN hr_employee e ON e.id = eb.employee_id
                GROUP BY eb.id, e.id
            )
        """)
