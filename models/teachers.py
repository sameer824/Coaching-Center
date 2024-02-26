from odoo import models, fields, api, _
class CoachingCenterTeachers(models.Model):
    _name = "coaching.center.teachers"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Teachers Information"
    _rec_name='name'
    
    teachers_id =fields.Char(string='Teacher_Seq',required=True,Copy=False,readonly=True,
                        default=lambda self: _('New Teacher'))
    name = fields.Char(string='Name', required=True ,tracking=True)
    email = fields.Char(string='Email',required=True ,tracking=True)
    phone = fields.Char(string='Phone' ,required=True,tracking=True)
    address = fields.Text(string='Address',tracking=True)
    date_of_birth = fields.Date(string='Date of Birth' ,required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender',default='male',required=True)
    qualification = fields.Char(string='Qualification',required=True)
    experience_years = fields.Integer(string='Years of Experience',required=True ,tracking=True)
    subjects_taught = fields.Many2many('coaching.center.subject', string='Subjects Taught')
    hourly_rate = fields.Float(string='Hourly Rate' ,required=True)
    basic_salary = fields.Float(string='Basic Salary', required=True,tracking=True)

    availability = fields.Selection([
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('contract', 'Contract')
    ], string='Availability',required=True)
    teaching_days = fields.Many2many('coaching.center.day', string='Teaching Days' )
    t_image = fields.Binary(string="Teacher Image", attachment=True, resize=(200, 200))
    state = fields.Selection([
        ('draft', 'Draft'),
        ('open', 'Open'),
        ('confirm', 'Confirm'),
        ('deleted', 'Deleted'),
    ], string='Status', default='draft', readonly=True)

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
    @api.model
    def create(self, vals):
        if not  vals.get('teachers_id',('_New'))==_('New'):
            vals['teachers_id']=self.env['ir.sequence'].next_by_code('coaching.center.teachers') or _('New')
        res = super(CoachingCenterTeachers, self).create(vals)
        return res




class CoachingCenterSubject(models.Model):
    _name = 'coaching.center.subject'
    _description = 'Subjects Offered'

    name = fields.Char(string='Subject Name')

class CoachingCenterDay(models.Model):
    _name = 'coaching.center.day'
    _description = 'Days of the Week'

    name = fields.Char(string='Day Name')

    

    #classes  attendances /quiz/fee structure fee submissions
