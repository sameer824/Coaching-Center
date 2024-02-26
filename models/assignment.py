from odoo import models, fields, api , _

class CoachingAssignment(models.Model):
    """
    Model for MR Developer Coaching Dashboard
    """
    _name = "coaching.assignment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Coaching Assignment"


    name = fields.Char(string='Assignment Name', required=True)
    deadline = fields.Datetime(string='Deadline', required=True)
    course_id = fields.Many2one('coaching.courses', string='Course', required=True)
    description = fields.Text(string='Description')
    class_id = fields.Many2one('classes', string='Class Name', store=True)
    student_lines = fields.One2many('coaching.students', 'assignment_id', string='Students')
    passing_marks = fields.Float(string= 'Total Marks')  # 
    assignment_file = fields.Binary(string='Assignment File', attachment=True, help='Upload your Assignment')
    @api.onchange('class_id')
    def _onchange_class_id(self):
        for rec in self:
            lines = [(5, 0, 0)]  # Initialize with delete operation
            for student in rec.class_id.student_ids:
                vals = {
                    'student_id': student.name
                }
                lines.append((0, 0, vals))
        rec.student_lines = lines
    @api.onchange('passing_marks')
    def _onchange_passing_marks(self):
        for record in self:
            # Update related coaching.students records
            if record.student_lines:
                for student_line in record.student_lines:
                    student_line.max_marks = record.passing_marks
    # @api.model
    # def write(self, values):
    #     if 'passing_marks' in values:
    #         passing_marks = values['passing_marks']
    #     return super(CoachingAssignment, self).write(values)
    # @api.model
    # def write(self, values):
    #     if 'passing_marks' in values:
    #         passing_marks = values['passing_marks']
    #     for rec in self:
    #         if rec.student_lines:
    #             rec.student_lines.write({'max_marks': passing_marks})
    #     return super(CoachingAssignment, self).write(values)


class CoachingStudents(models.Model):
    _name = "coaching.students"
    _description = "Coaching Students"
    assignment_id = fields.Many2one('coaching.assignment', string='Assignment')
    student_id = fields.Char(string='Student Name', required=True)
    max_marks = fields.Float(string='Total Marks')
    passing_marks = fields.Float(string=' Marks')
    is_published = fields.Boolean(string='Published', default=False)
    solve_file = fields.Binary(string='Solution File', attachment=True, help='Upload you Solution ')

# class AssignmentResult(models.Model):
#     _name = "coaching.assignment.result"
#     _description = "Assignment Results"

#     student_id = fields.Many2one('coaching.student', string='Student', required=True)
#     assignment_id = fields.Many2one('coaching.assignment', string='Assignment', required=True)
#     obtained_marks = fields.Float(string='Obtained Marks')
#     is_pass = fields.Boolean(string='Pass', compute='_compute_is_pass', store=True)

#     @api.depends('obtained_marks', 'assignment_id.passing_marks')
#     def _compute_is_pass(self):
#         for rec in self:
#             rec.is_pass = rec.obtained_marks >= rec.assignment_id.passing_marks















    # result_ids = fields.One2many('coaching.assignment.result', 'assignment_id', string='Results')
    # class_id = fields.Many2one('classes', string='Class Name', required=True)
    # @api.onchange('class_id')
    # def _onchange_class_id(self):
    #     for rec in self:
    #         lines = [(5, 0, 0)]  # Initialize with delete operation
    #         for student in rec.class_id.student_ids:
    #             vals = {
    #                 'student_id': student.name
    #             }
    #             lines.append((0, 0, vals))
    #     rec.student_lines = lines
    
# class StudentsLine(models.Model):
#     _name = "coaching.students.line"
#     _description = "Students Lines"

#     line_id = fields.Many2one('coaching.assignment', string='Student')
#     student_id = fields.Char(string='Students')

    # class Course(models.Model):
    #     _name = "coaching.course"
    #     _description = "Courses"

    #     name = fields.Char(string='Course Name', required=True)
    #     # Other course-related fields

    # class Student(models.Model):
    #     _name = "coaching.student"
    #     _description = "Students"

    #     name = fields.Char(string='Student Name', required=True)
        # Other student-related fields
        
    # @api.onchange('course_id')
    # def _onchange_course_id(self):
        # Update student_ids based on the selected course (if needed)
        # Example: You may want to automatically assign students based on the course.
        # Implement your logic here.

    # Additional fields or methods as needed @api.onchange('course_id')
        # def _onchange_course_id(self):
        # Update student_ids based on the selected course (if needed)
        # Example: You may want to automatically assign students based on the course.
        # Implement your logic here.

    # Additional fields or methods as needed