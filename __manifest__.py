# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'MR Developer Coaching',
    'version' : '1.1',
    'summary': 'Tech coaching centers Educational hubs specializing in technology skills of programming to cybersecurity.',
    'sequence': -100,
    'description': """ This module manages coaching center activities such as courses, students, and instructors.""",
    'category': 'Technology Education and Training',
    'website': 'https://www.mrdevelopercoaching.com',
    'license': 'LGPL-3',
    'depends' : [
        'mail'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/dashboard.view.xml',
        'views/assignment.view.xml',
        'views/student.view.xml',
        'views/courses.view.xml',
        'views/teachers.view.xml',
        'views/salary.view.xml',
        'views/classes.view.xml',
        'views/attendance.view.xml',
        'views/quizes.view.xml'

    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,

}
