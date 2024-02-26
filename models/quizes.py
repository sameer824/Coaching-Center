from odoo import models, fields, api

class CoachingQuiz(models.Model):
    _name = 'coaching.quiz'
    _description = 'Coaching Center Quiz'

    name = fields.Char(string='Quiz Name', required=True)
    topic = fields.Char(string='Quiz Topic', required=True)
    duration = fields.Float(string='Duration (in minutes)', help='Duration of the quiz in minutes')
    description = fields.Text(string='Description')
    quiz_file = fields.Binary(string='Quiz File', attachment=True, help='Upload any relevant files for the entire quiz')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('started', 'Started'),
        ('finished', 'Finished'),
    ], string='State', default='draft', copy=False, index=True, track_visibility='onchange')
    q_date=fields.Datetime(string='Quiz Date')

    quiz_marks = fields.Float(string= 'Total Marks')  # 

    student_lines = fields.One2many('coaching.quiz.line', 'quiz_id', string='Students')
    class_id = fields.Many2one('classes', string='Class Name', store=True)
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
    @api.onchange('quiz_marks')
    def _onchange_quiz_marks(self):
        for record in self:
            # Update related coaching.students records
            if record.student_lines:
                for student_line in record.student_lines:
                    student_line.max_marks = record.quiz_marks


class QuizOrderline(models.Model):
    _name = "coaching.quiz.line"
    _description = "Coaching Quiz Orderline"
    quiz_id = fields.Many2one('coaching.quiz', string='Quiz')
    student_id = fields.Char(string='Student Name', required=True)
    max_marks = fields.Float(string='Total Marks')
    passing_marks = fields.Float(string=' Marks')
    is_published = fields.Boolean(string='Published', default=False)
    solve_file = fields.Binary(string='Solution File', attachment=True, help='Upload you Solution ')
