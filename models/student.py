from odoo import models, fields, api , _

class StudentCoaching(models.Model):
    """
    Model for MR Developer Coaching
    """
    _name = "student.coaching"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Student Coaching"
    # all created  students fields
    student_id =fields.Char(string='Student_Seq',required=True,Copy=False,readonly=True,
                        default=lambda self: _('New Student Details'))
    course_id = fields.Many2many("coaching.courses", string='Course Name')

    name = fields.Char(string='Student Name', required=True, tracking=True)
    s_cnic=fields.Char(string="CNIC NO",required=True ,tracking=True)
    s_gender =  fields.Selection([
    ('male', 'Male'),
    ('female', 'Female')
], string='Gender',default="male")
    dob = fields.Date(string="DOB", required=True)

    
    country= fields.Char(string="Country",required=True)
    city=fields.Char(string="City")
    address = fields.Text(string='Address')
    s_bloodgroup=fields.Char(string="Blood Group")
    f_name = fields.Char(string='Father Name', required=True, tracking=True)
    s_phone = fields.Char(string='Phone', required=True, tracking=True)
    s_email = fields.Char(string='Email', required=True, tracking=True)
    duration= fields.Char(string='Course Duration', required=True, tracking=True)
    # course = fields.Char(string='Course Name', required=True, tracking=True)
    student_image = fields.Binary(string="Student Image", attachment=True, resize=(200, 200))
    admission_date = fields.Date(string="Admission Date", required=True, tracking=True)
    emergency_contact_name = fields.Char(string='Emergency Contact Name')
    emergency_contact_phone = fields.Char(string='Emergency Contact Phone')
    
    educational_background = fields.Text(string='Educational Background')
    
    payment_method = fields.Selection([
        ('online', 'Online'),
        ('offline', 'Offline'),
    ], string='Payment Method',default="offline", tracking=True)
    payment_status = fields.Selection([
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ], string='Payment Status',default="pending", tracking=True)
    fee_details = fields.Char(string='Fee Details',tracking=True)

    medical_information = fields.Text(string='Medical Information')
    
    additional_notes = fields.Text(string='Additional Notes or Comments')

    # Corrected field definition for Batch
    # batch = fields.Many2one('your.batch.model', string='Batch', required=True, tracking=True)
    #guardian form fields code 

    guardian_image =fields.Binary(string="Guardian  Image" , resize=(200, 200))
    g_name = fields.Char(string='Guardian Name')
    g_cnic =fields.Char(string="Guardian CNIC")
    g_dob = fields.Date("Birth Date")
    g_gender =  fields.Selection([
    ('male', 'Male'),
    ('female', 'Female')
], string='Gender',default="male")
    g_relation = fields.Selection([
    ('father', 'Father'),
    ('mother', 'Mother'),
    ('sister', 'Sister'),
    ('brother', 'Brother'),
    ('son', 'Son'),
    ('daughter', 'Daughter'),
    ('husband','Husband'),
    ('wife','Wife')
], string='Guardian Relation ',default="father")
    g_contact = fields.Char(string='Contact Number')
    g_email=fields.Char(string="Guardian Email")
    g_address = fields.Char(string='Guardian Address')
    g_blood = fields.Char(string ="Blood Group")
    terms_and_conditions_accepted = fields.Boolean(string='Terms and Conditions Accepted')



    # status bar and its button 
    state = fields.Selection(selection=[
    ('draft', 'Draft'), ('open', 'In Progress'),
    ('confirm', 'Confirmed'),('delete', 'Deleted')
        ], default='draft', string=" Addmission Status", tracking=True)
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
    # create event to give the sequence number to the now student
    @api.model
    def create(self, values):
        # Your create logic here
        return super(StudentCoaching, self).create(values)

    def write(self, values):
        # Your write logic here
        return super(StudentCoaching, self).write(values)


    def action_submit(self):
        # Additional logic on submit if needed
        return True

    def action_reset(self):
        # Reset all fields to their default values
        self.write(self.default_get(self.fields_get()))
        return True
    @api.model
    def create(self, vals):
        if not  vals.get('student_id',('_New'))==_('New'):
            vals['student_id']=self.env['ir.sequence'].next_by_code('student.coaching') or _('New')
        res = super(StudentCoaching, self).create(vals)
        return res
    # @api.onchange('course_id')
    # def _onchange_course_id(self):
    #     # Set the basic_salary field based on the selected teacher
    #     if self.course_id:
    #         self.course = self.course_id.course
