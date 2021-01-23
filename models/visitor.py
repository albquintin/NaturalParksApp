from odoo import models, fields, api

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

    acommodation_id = fields.Many2one('naturalparks.acommodation', ondelete='cascade', string="Acommodation", required=True)
    management_id = fields.Many2one('naturalparks.management', string="Person who registered this visitor")

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
