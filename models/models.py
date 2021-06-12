# -*- coding: utf-8 -*-

from odoo import models, fields


class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'Open Academy course'

    name = fields.Char(string="Title", required = True, help="Course name")
    description = fields.Text(string="Description course")

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
