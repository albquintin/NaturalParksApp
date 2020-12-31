from odoo import models, fields, api

class Area(models.Model):
    _name = 'naturalparks.area'

    name = fields.Char(string="Name", required=True)
    extension = fields.Integer(string="Extension (in km2)", required=True)

    natural_park_id = fields.Many2one('naturalparks.natural_park', string="Natural Park")