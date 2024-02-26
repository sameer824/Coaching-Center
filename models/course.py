from odoo import models, fields, api, _
class CoachingCourses(models.Model):
    _name = "coaching.courses"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Coaching Courses"
    _rec_name="course_name" #this rec name field is use to show the name of the selected items

    course_name=fields.Char(string="Course Name",required=True,tracking=True)
    # avaiable_teachers= fields.Char(string=" Teacher Name " , required=True,tracking=True)
    course_start_date = fields.Date(string="Start Date")
    course_end_date = fields.Date(string="End Date")
    teacher_id = fields.Many2one("coaching.center.teachers", string='Teacher Name')

    note = fields.Text(string='Description')
    free=fields.Integer(string=" Total Fee")

    state = fields.Selection(selection=[
    ('draft', 'Draft'), ('open', 'In Progress'),
    ('confirm', 'Confirmed'),('delete', 'Deleted')
        ], default='draft', string=" Course Status", tracking=True)
    # define and method of status bar
    def action_confirm(self):
        self.state='confirm'
    def action_open(self):
        self.state='open'
    def action_draft(self):
        self.state='draft'
    def action_close(self):
        self.state='closed'
    def action_delete(self):  
        # Delete the record
        if self.state in ['draft', 'open']:
            # Delete the record
            self.unlink()
    # @api.onchange('teacher_id')
    # def _onchange_teacher_id(self):
    #     # Set the basic_salary field based on the selected teacher
    #     if self.teacher_id:
    #         self.avaiable_teachers = self.teacher_id.avaiable_teachers



