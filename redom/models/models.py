# -*- coding: utf-8 -*-

from odoo import models, fields, api


class redomModel(models.Model):
    _name = 'redom.model'
    _description = 'DB de RedOM8'

    name = fields.Char(required=True,string="Name")
    value = fields.Integer(required=True,string="Value")
    phone = fields.Text(required=True,string="Phone")
    date = fields.Date(required=True,string="Date")
    gender = fields.Selection([('male','Male'),('female','Female')],string="Gender")
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
