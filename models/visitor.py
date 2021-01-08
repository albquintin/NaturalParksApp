from odoo import models, fields, api

class Visitor(models.Model):
    _name = 'naturalparks.visitor'

    dni = fields.Char(required=True)
    name = fields.Char(required=True)
    address = fields.Char()
    job = fields.Char()

    acommodation_id = fields.Many2one('naturalparks.acommodation', ondelete='cascade', string="Acommodation", required=True)
    management_id = fields.Many2one('naturalparks.management', string="Person who registered this visitor")
