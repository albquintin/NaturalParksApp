from odoo import models, fields, api, exceptions

class Visitor(models.Model):
    _name = 'naturalparks.visitor'

    dni = fields.Char(required=True)
    name = fields.Char(required=True)
    address = fields.Char()
    job = fields.Char()
    state = fields.Selection([
            ('draft', 'Draft'),
            ('confirm', 'Confirm'),
            ('done', 'Done'),
        ], string='Status', readonly=True, default='draft')

    natural_park_id = fields.Many2one('naturalparks.natural_park', string="Natural Park", required=True)
    acommodation_id = fields.Many2one('naturalparks.acommodation', ondelete='cascade', string="Acommodation", required=True)
    management_id = fields.Many2one('naturalparks.management', string="Person who registered this visitor")

    @api.constrains('natural_park_id', 'acommodation_id')
    def _check_acommodation_is_in_the_park(self):
        for r in self:
            if r.acommodation_id.natural_park_id != r.natural_park_id:
                raise exceptions.ValidationError("The acommodation must be in the park")

    def action_confirm(self):
        for r in self:
            r.state = 'confirm'
            return {
                'effect': {
                    'fadeout': 'slow',
                    'message': 'Visitor Confirmed',
                    'type': 'rainbow_man',
                }
            }
            
    def action_done(self):
        for r in self:
            r.state = 'done'

    def action_draft(self):
        for r in self:
            r.state = 'draft'

    