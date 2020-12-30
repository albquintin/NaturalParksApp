from odoo import models, fields, api

class Acommodation(models.Model):
    _name = 'naturalparks.acommodation'

    name = fields.Char(string="Name", required=True)
    capacity = fields.Integer(required=True)
    category = fields.Selection([('uno', '*'), ('dos','**'), ('tres', '***'), ('cuatro', '****'), ('cinco', '*****')])