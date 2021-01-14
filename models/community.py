from odoo import models, fields, api, exceptions

class Community(models.Model):
    _name = 'naturalparks.community'

    name = fields.Char(string="Name")
    extension = fields.Integer(string="Extension (in km2)")
    administrative_authority = fields.Char()

    @api.constrains('extension')
    def _check_park_has_extension(self):
        for r in self:
            if r.extension <= 0:
                raise exceptions.ValidationError("The community must have extension")
