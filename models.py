from odoo import models, fields, api

class Acommodation(models.Model):
    _name = 'naturalparks.acommodation'

    name = fields.Char(string="Title", required=True)
    capacity = fields.Integer(required=True)
    category = fields.Selection([('uno', '*'), ('dos','**'), ('tres', '***'), ('cuatro', '****'), ('cinco', '*****')])

class Trip(models.Model):
    _name = 'naturalparks.trip'

    name = fields.Char(string="Definition of the trip")
    trip_type = fields.Selection([('car', 'Car'), ('walking', 'Walking')]) 
    trip_day = fields.Date()
    trip_time = fields.Time()

    acommodation_id = fields.Many2one('naturalparks.acommodation', ondelete='cascade', string="Acommodation Organizer")