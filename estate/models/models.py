# -*- coding: utf-8 -*-

from odoo import models, fields, api


class estate(models.Model):
    _name = 'estate.property'
    _description = 'Real State Advertisement'

    name = fields.Char(required=True)
    description = fields.Integer()
    postcode = fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float(required=True)
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([('north','North'),('south','South'),('east','East'),('west','West')])
