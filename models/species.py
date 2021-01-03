from odoo import models, fields, api

class Species(models.Model):
    _name = 'naturalparks.species'

    name = fields.Char(string="Binomial nomenclature", required=True)
    common_name = fields.Char(required=True)
    number_of_specimens = fields.Integer()

class Plant(models.Model):
    _name = 'naturalparks.plant'
    _inherit = 'naturalparks.species'

    flowering = fields.Selection([('yes', 'Yes'), ('no', 'No')])
    flowering_period = fields.Selection([('spring', 'Spring'), ('summer', 'Summer'), ('autumn', 'Autumn'), ('winter', 'Winter')])

    is_eaten = fields.Selection([('yes', 'Yes'), ('no', 'No')])
    animal_ids = fields.Many2many('naturalparks.animal', string="Herbivores which eat this plant")

class Animal(models.Model):
    _name = 'naturalparks.animal'
    _inherit = 'naturalparks.species'

    alimentation = fields.Selection([('carnivore','Carnivore'), ('herbivore','Herbivore'), ('omnivore','Omnivore')])
    mating_season = fields.Selection([('spring', 'Spring'), ('summer', 'Summer'), ('autumn', 'Autumn'), ('winter', 'Winter')])

    is_eaten = fields.Selection([('yes', 'Yes'), ('no', 'No')])


class Mineral(models.Model):
    _name = 'naturalparks.mineral'
    _inherit = 'naturalparks.species'

    mineral_type = fields.Selection([('crystal', 'Crystal'), ('stone', 'Stone')])