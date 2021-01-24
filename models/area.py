from odoo import models, fields, api, exceptions

class Area(models.Model):
    _name = 'naturalparks.area'
    _order = 'natural_park_id'

    name = fields.Char(string="Name", required=True)
    extension = fields.Integer(string="Extension (in km2)", required=True)

    natural_park_id = fields.Many2one('naturalparks.natural_park', string="Natural Park", ondelete='cascade', required=True)
    community_id = fields.Many2one('naturalparks.community', string="Community", required=True)

    @api.constrains('extension')
    def _check_park_has_extension(self):
        for r in self:
            if r.extension <= 0:
                raise exceptions.ValidationError("The area must have extension")

    @api.constrains('natural_park_id', 'community_id')
    def _check_community_is_of_the_park(self):
        for r in self:
            if r.community_id not in r.natural_park_id.community_ids:
                raise exceptions.ValidationError("The park isn't in this community")
            