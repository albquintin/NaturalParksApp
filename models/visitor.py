from odoo import models, fields, api, exceptions

class Visitor(models.Model):
    _name = 'naturalparks.visitor'
    _order = 'name'

    name = fields.Char(required=True)    
    dni = fields.Char(required=True)
    address = fields.Char()
    job = fields.Char()
    color = fields.Integer()
    state = fields.Selection([
            ('1.draft', 'Draft'),
            ('2.confirm', 'Confirm'),
            ('3.done', 'Done'),
        ], string='Status', default='1.draft')

    natural_park_id = fields.Many2one('naturalparks.natural_park', string="Natural Park", ondelete='cascade', required=True)
    acommodation_id = fields.Many2one('naturalparks.acommodation', string="Acommodation", required=True)
    management_id = fields.Many2one('naturalparks.management', string="Person who registered this visitor")

    @api.onchange('natural_park_id')
    def filter_acommodation(self):
        for r in self:
            return {'domain': {'acommodation_id': [('natural_park_id', '=', r.natural_park_id.id)]}}

    @api.onchange('natural_park_id')
    def filter_management_employee(self):
        for r in self:
            return {'domain': {'management_id': [('natural_park_id', '=', r.natural_park_id.id)]}}


    def action_confirm(self):
        for r in self:
            r.state = '2.confirm'
            return {
                'effect': {
                    'fadeout': 'slow',
                    'message': 'Visitor Confirmed',
                    'type': 'rainbow_man',
                }
            }
            
    def action_done(self):
        for r in self:
            r.state = '3.done'

    def action_draft(self):
        for r in self:
            r.state = '1.draft'