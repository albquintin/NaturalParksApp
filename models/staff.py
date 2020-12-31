from odoo import models, fields, api

class Staff(models.Model):
    _name = 'naturalparks.staff'

    name = fields.Char(string="Name", required=True)
    dni = fields.Char(required=True)
    social_security = fields.Char(required=True)
    address = fields.Char()
    mobile_phone = fields.Integer()
    landline = fields.Integer()
    salary = fields.Integer(string="Salary (in €)")