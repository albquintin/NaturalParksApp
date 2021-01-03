from odoo import models, fields, api

class Community(models.Model):
    _name = 'naturalparks.community'

    name = fields.Char(string="Name", required=True)
    extension = fields.Integer(string="Extension (in km2)", required=True)
    administrative_authority = fields.Char(required=True)