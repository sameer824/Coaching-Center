from odoo import models, fields, api , _

class CoachingDashboard(models.Model):
    """
    Model for MR Developer Coaching Dashboard
    """
    _name = "coaching.dashboard"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Coaching Dashboard"
    
    total_students = fields.Integer(string='Total Students', compute='_compute_total_students')
    total_classes = fields.Integer(string='Total Classes', compute='_compute_total_classes')
    total_teachers = fields.Integer(string='Total Teachers', compute='_compute_total_teachers')
    # Add more fields as needed for other statistics

    @api.depends('total_students')
    def _compute_total_students(self):
        self.total_students = self.env['student.coaching'].search_count([])

    @api.depends('total_classes')
    def _compute_total_classes(self):
        self.total_classes = self.env['classes'].search_count([])

    @api.depends('total_teachers')
    def _compute_total_teachers(self):
        self.total_teachers = self.env['coaching.center.teachers'].search_count([])