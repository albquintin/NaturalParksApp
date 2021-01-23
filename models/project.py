from datetime import timedelta
from odoo import models, fields, api, exceptions

class Project(models.Model):
    _name = 'naturalparks.project'

    name = fields.Char(string="Project Name", required=True)
    species_id = fields.Many2one('naturalparks.species', string="Species", required=True)
    research_ids = fields.Many2many('naturalparks.research', string="Researchers", required=True)
    budget = fields.Float(string="Budget (in €)", digits=(8, 2))
    starting_date = fields.Date(required=True)
    ending_date = fields.Date(required=True)
    color = fields.Integer()
    state = fields.Selection([
            ('draft', 'Draft'),
            ('confirm', 'Confirm'),
            ('done', 'Done'),
        ], string='Status', readonly=True, default='draft')

    @api.constrains('budget')
    def _check_park_has_extension(self):
        for r in self:
            if r.budget <= 0:
                raise exceptions.ValidationError("The budget must be positive")

    @api.constrains('starting_date', 'ending_date')
    def _check_ending_date_is_after_starting_date(self):
        for r in self:
            if r.starting_date > r.ending_date:
                raise exceptions.ValidationError("Ending date must be before the starting date")

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