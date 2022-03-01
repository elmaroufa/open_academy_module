# -*- coding: utf-8 -*-
from odoo import models, fields 


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library book'

    name = fields.Char(string="Title", required = True, help="Book name")
    description = fields.Text(string="Description course")
    responsible_id = fields.Many2one('res.users', string="Responsible", ondelete="set null", index=True)
    session_ids = fields.One2many('openacademy.session', \
        'course_id', string='Session')
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


class Session(models.Model):
    _name = 'openacademy.session'
    _description = 'Session open academy'

    name = fields.Char(required = True)
    start_date = fields.Date()
    duration = fields.Float(digits = (6,3), help="duration in day")
    seats = fields.Integer(string="number of seats")
    instructor_id = fields.Many2one("res.partner", string="Instructor")
    course_id = fields.Many2one("openacademy.course", ondelete="cascade", required=True)
