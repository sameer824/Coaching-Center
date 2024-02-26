from odoo import models, fields, api, _
class TeachersSalary(models.Model):
    _name = "teachers.salary"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Teachers Salary Information"
    _rec_name="teacher_id" #this rec name field is use to show the name of the selected items
    teacher_id = fields.Many2one("coaching.center.teachers", string='Teacher')
    subjects_id = fields.Many2many('coaching.center.subject', string='Subjects Taught')
    salary_month = fields.Date(string='Salary Month', required=True, default=fields.Date.today())
    basic_salary = fields.Float(string='Basic Salary', required=True)
    bonuses = fields.Float(string='Bonuses')
    deductions = fields.Float(string='Deductions')
    net_salary = fields.Float(string='Net Salary', compute='_compute_net_salary', store=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('open', 'Open'),
        ('confirm', 'Confirm'),
        ('deleted', 'Deleted'),
    ], string='Status', default='draft', readonly=True)
    
    @api.depends('basic_salary', 'bonuses', 'deductions')
    def _compute_net_salary(self):
        for record in self:
            record.net_salary = record.basic_salary + record.bonuses - record.deductions
    def action_draft(self):
        self.state = 'draft'

    def action_open(self):
        self.state = 'open'

    def action_confirm(self):
        self.state = 'confirm'

    def action_delete(self):
        # Delete the record
        if self.state in ['draft', 'open']:
            self.unlink()
    @api.onchange('teacher_id')
    def _onchange_teacher_id(self):
        # Set the basic_salary field based on the selected teacher
        if self.teacher_id:
            self.basic_salary = self.teacher_id.basic_salary

            
    