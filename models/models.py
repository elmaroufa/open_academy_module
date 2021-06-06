# -*- coding: utf-8 -*-

from odoo import models, fields


class course(models.Model):
    name = 'openacademy.course'
    description = 'Open Academy course'

    name = fields.Char(string="Title", required = True, help="Course name")
    description = fields.Text(string="Description course")

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
