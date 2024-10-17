from odoo import api, models, fields

class HREmployeeBenefits(models.Model):
    _name = 'hr.employee.benefits'
    _description = 'Employee Benefits'

    name = fields.Char(string="Benefit Name", required=True)
    benefit_type = fields.Selection([
        ('health_insurance', 'Health Insurance'),
        ('transportation', 'Transportation'),
        ('bonus', 'Bonus'),
        ('other', 'Other'),
    ], string="Benefit Type", required=True)
    description = fields.Text(string="Description")
    employee_id = fields.Many2one('hr.employee', string="Employee", required=True)
    amount = fields.Float(string="Benefit Amount")
    date_awarded = fields.Date(string="Date Awarded")
    total_amount = fields.Float(string="Total Amount",default=0.0, compute="_compute_total_amount",store=True)


    @api.depends('employee_id','amount')
    def _compute_total_amount(self):
        for record in self:  
            if record.employee_id:
                benefits = self.env['hr.employee.benefits'].search([('employee_id', '=', record.employee_id.id)]).mapped('amount')
                record.total_amount = sum(benefits) if benefits else 0.0


class HREmployee(models.Model):
    _inherit = 'hr.employee'

    benefit_ids = fields.One2many('hr.employee.benefits', 'employee_id', string="Benefits")


    def print_xls_benefits_report(self):
        return {
                "type": "ir.actions.act_url",
                "url": "/employee_benefit/excel_report",
                "target":"new",
                }
    