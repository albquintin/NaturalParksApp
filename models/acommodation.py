from odoo import models, fields, api, exceptions

class Acommodation(models.Model):
    _name = 'naturalparks.acommodation'

    name = fields.Char(string="Name", required=True)
    capacity = fields.Integer(required=True)
    category = fields.Selection([('one', '*'), ('two','**'), ('three', '***'), ('four', '****'), ('five', '*****')])
    color = fields.Integer()
    
    natural_park_id = fields.Many2one('naturalparks.natural_park', string="Natural Park", required=True)

    @api.constrains('capacity')
    def _check_capacity_is_higher_than_zero(self):
        for r in self:
            if r.capacity <= 0:
                raise exceptions.ValidationError("The capacity must be positive")
    
    
