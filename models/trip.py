from odoo import models, fields, api, exceptions

class Trip(models.Model):
    _name = 'naturalparks.trip'

    name = fields.Char(string="Definition of the trip", required=True)
    trip_type = fields.Selection([('car', 'Car'), ('walking', 'Walking')]) 
    starting_date = fields.Datetime()
    ending_date = fields.Datetime()

    natural_park_id = fields.Many2one('naturalparks.natural_park', string="Natural Park", required=True)
    acommodation_id = fields.Many2one('naturalparks.acommodation', ondelete='cascade', string="Acommodation Organizer", required=True)
    visitor_ids = fields.Many2many('naturalparks.visitor', string="Visitors")

    @api.constrains('natural_park_id', 'acommodation_id')
    def _check_acommodation_is_in_the_park(self):
        for r in self:
            if r.acommodation_id.natural_park_id != r.natural_park_id:
                raise exceptions.ValidationError("The acommodation must be in the park")