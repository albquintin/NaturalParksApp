from odoo import models, fields, api, exceptions

class Natural_Park(models.Model):
    _name = 'naturalparks.natural_park'

    name = fields.Char(string="Name", required=True)
    starting_date = fields.Date()
    extension = fields.Integer(string="Extension (in km2)", required=True)

    community_ids = fields.Many2many('naturalparks.community', string="Autonomous Communities", required=True)

    @api.constrains('extension')
    def _check_park_has_extension(self):
        for r in self:
            if r.extension <= 0:
                raise exceptions.ValidationError("The park must have extension")