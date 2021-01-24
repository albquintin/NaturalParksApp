from odoo import models, fields, api, exceptions
from odoo.exceptions import ValidationError

class Trip(models.Model):
    _name = 'naturalparks.trip'

    name = fields.Char(string="Definition of the trip", required=True)
    trip_type = fields.Selection([('car', 'Car'), ('walking', 'Walking')]) 
    starting_date = fields.Datetime(required=True)
    ending_date = fields.Datetime(required=True)
    color = fields.Integer()

    natural_park_id = fields.Many2one('naturalparks.natural_park', string="Natural Park", required=True)
    acommodation_id = fields.Many2one('naturalparks.acommodation', ondelete='cascade', string="Acommodation Organizer", required=True)
    visitor_ids = fields.Many2many('naturalparks.visitor', string="Visitors")
    total_visitors = fields.Integer(compute='_calculate_visitors')
    state = fields.Selection([
            ('draft', 'Draft'),
            ('confirm', 'Confirm'),
            ('done', 'Done'),
        ], string='Status', readonly=True, default='draft')

    @api.onchange('natural_park_id')
    def onchange_natural_park_id_check_acommodation(self):
        for r in self:
            return {'domain': {'acommodation_id': [('natural_park_id', '=', r.natural_park_id.id)]}}

    @api.onchange('natural_park_id')
    def onchange_natural_park_id_check_visitors(self):
        for r in self:
            return {'domain': {'visitor_ids': [('natural_park_id', '=', r.natural_park_id.id)]}}

    @api.constrains('natural_park_id', 'visitor_ids')
    def _check_visitors(self):
        for r in self:
            if r.visitor_ids.natural_park_id != r.natural_park_id:
                raise exceptions.ValidationError("Visitors must be in the park")

    @api.constrains('starting_date', 'ending_date')
    def _check_ending_date_is_after_starting_date(self):
        for r in self:
            if r.starting_date > r.ending_date:
                raise exceptions.ValidationError("Ending date must be before the starting date")

    @api.depends('visitor_ids')
    def _calculate_visitors(self):
        for r in self:
            r.total_visitors = len(r.visitor_ids)   
                
    def action_confirm(self):
        for r in self:
            r.state = 'confirm'
            return {
                'effect': {
                    'fadeout': 'slow',
                    'message': 'Trip Confirmed',
                    'type': 'rainbow_man',
                }
            }
            
    def action_done(self):
        for r in self:
            r.state = 'done'

    def action_draft(self):
        for r in self:
            r.state = 'draft'

    