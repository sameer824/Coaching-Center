# coaching_module/models.py

from odoo import models, fields, api

class Attendance(models.Model):
    _name = "coaching.attendance"
    _description = "Attendance Records"
    _rec_name = "class_id"

    date = fields.Date(string='Date', required=True, default=fields.Date.today())
    class_id = fields.Many2one('classes', string='Class Name', required=True)
    teacher_id = fields.Char(string='Teacher Name')
    
    # attendance_lines = fields.One2many(
    #     'coaching.attendance.line', 'attendance_id', 
    #     string='Attendance Lines'
    #     domain="[('class_id', '=', class_id)]"
    # )   
    attendance_lines = fields.One2many('coaching.attendance.line', 'attendance_id', string='Attendance Lines')

    # status bar and its buttons
    state = fields.Selection(selection=[
        ('draft', 'Draft'), ('open', 'In Progress'),
        ('confirm', 'Confirmed'), ('delete', 'Deleted')
    ], default='draft', string="Admission Status", tracking=True)

    @api.onchange('class_id')
    def _onchange_class_id(self):
        if self.class_id:
            self.teacher_id = self.class_id.teachers
        for rec in self:
            lines = [(5, 0, 0)]  # Initialize with delete operation
            for student in rec.class_id.student_ids:
                vals = {
                    'student_id': student.name
                }
                lines.append((0, 0, vals))
        rec.attendance_lines = lines
        # Set the teacher_id field based on the selected class
        

    # Define status bar methods
    def action_confirm(self):
        self.state = 'confirm'

    def action_open(self):
        self.state = 'open'

    def action_draft(self):
        self.state = 'draft'

    def action_close(self):
        self.state = 'closed'

    def action_delete(self):
        # Delete the record
        if self.state in ['draft', 'open']:
            self.unlink()

class AttendanceLine(models.Model):
    _name = "coaching.attendance.line"
    _description = "Attendance Lines"

    attendance_id = fields.Many2one('coaching.attendance', string='Attendance')
    class_id = fields.Many2one('classes', string='Class Name', related='attendance_id.class_id', store=True)
    student_id = fields.Char( string='Student')

    is_present = fields.Boolean(string='Present', default=True)
    is_absent = fields.Boolean(string='Absent')
    is_late = fields.Boolean(string='Late')
    
    @api.onchange('is_present', 'is_absent', 'is_late')
    def _onchange_attendance_status(self):
        for rec in self:
            if rec.is_present:
                rec.is_absent = False
                rec.is_late = False
            elif rec.is_absent:
                rec.is_present = False
                rec.is_late = False
            elif rec.is_late:
                rec.is_present = False
                rec.is_absent = False
            else:
            # If none of the options is selected, you might want to set a default behavior or leave it as is.
                pass
            