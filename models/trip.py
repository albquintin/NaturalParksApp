from odoo import models, fields, api

class Trip(models.Model):
    _name = 'naturalparks.trip'

    name = fields.Char(string="Definition of the trip", required=True)
    trip_type = fields.Selection([('car', 'Car'), ('walking', 'Walking')]) 
    trip_time = fields.Datetime()

    acommodation_id = fields.Many2one('naturalparks.acommodation', ondelete='cascade', string="Acommodation Organizer")