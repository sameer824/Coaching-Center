from odoo import models, fields, api, _
class Classes(models.Model):
    _name = "classes"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Classes Information"
    name = fields.Char(string='Class Name', required=True)
    teachers= fields.Char(string='Teacher  Name',tracking=True)

    # You can add more fields as needed

    # Example: Adding a Many2many field for students in the class
    student_ids = fields.Many2many('student.coaching', string='Students', help='Students in the class')
    class_code = fields.Char(string='Class Code' , required=True, tracking=True)
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    duration = fields.Float(string='Duration (in hours)')
    location = fields.Char(string='Location')
    max_capacity = fields.Integer(string='Maximum Capacity')
    course_id = fields.Many2one("coaching.courses", string='Course Name')      
    class_level = fields.Selection([
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        # Add more choices as needed
    ], string='Class Level',default='beginner')
    notes = fields.Text(string='Notes')
    active = fields.Boolean(string='Active', default=True)
    syllabus_link = fields.Many2many('syllabus.link', string='Syllabus Link')
    # @api.depends('course_id')
    # def _compute_dates(self):
    #     for record in self:
    #         if record.course_id:
    #             # Assuming each course has a start_date and end_date field
    #             start_dates = record.course_id.mapped('start_date')
    #             end_dates = record.course_id.mapped('end_date')
                
    #             # Update the start_date and end_date fields of the current record
    #             record.start_date = min(start_dates)
    #             record.end_date = max(end_dates)

    @api.onchange('course_id')
    def _onchange_course_id(self):
        # Set the basic_salary field based on the selected teacher
        if self.course_id:
            self.start_date = self.course_id.course_start_date
        if self.course_id:
            self.end_date = self.course_id.course_end_date
        if  self.course_id:
            self.teachers = self.course_id.teacher_id.name
    

    class SyllabusLink(models.Model):
        _name = 'syllabus.link'
        _description = 'Syllabus Link'

        name = fields.Char(string='Link', required=True)
        description = fields.Text(string='Description')
        tags = fields.Many2many('syllabus.tag', string='Tags')
        date_added = fields.Date(string='Date Added')
        rating = fields.Float(string='Rating', digits=(5, 2))
        is_active = fields.Boolean(string='Active', default=True)

        _sql_constraints = [
            ('name_unique', 'unique(name)', 'Link must be unique!'),
        ]


