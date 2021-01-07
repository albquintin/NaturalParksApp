from odoo import models, fields, api

class Species(models.Model):
    _name = 'naturalparks.species'

    name = fields.Char(string="Binomial nomenclature", required=True)
    common_name = fields.Char(required=True)
    number_of_specimens = fields.Integer()

class Plant(models.Model):
    _name = 'naturalparks.plant'
    _inherit = 'naturalparks.species'

    blooming = fields.Boolean(string="Does the plant have blooming?")
    blooming_period = fields.Selection([('spring', 'Spring'), ('summer', 'Summer'), ('autumn', 'Autumn'), ('winter', 'Winter')])

    is_eaten = fields.Boolean(string="Is the plant eaten?")
    animal_ids = fields.Many2many('naturalparks.animal', string="Herbivores which eat this plant")

class Animal(models.Model):
    _name = 'naturalparks.animal'
    _inherit = 'naturalparks.species'

    alimentation = fields.Selection([('carnivore','Carnivore'), ('herbivore','Herbivore'), ('omnivore','Omnivore')])
    mating_season = fields.Selection([('spring', 'Spring'), ('summer', 'Summer'), ('autumn', 'Autumn'), ('winter', 'Winter')])

    is_eaten = fields.Boolean(string="Is the animal eaten?")
    animal_ids = fields.Many2many(comodel_name='naturalparks.animal', relation='animals_eaten', column1='prey', column2='carnivores', string="Carnivores which eat this animal")


class Mineral(models.Model):
    _name = 'naturalparks.mineral'
    _inherit = 'naturalparks.species'

    mineral_type = fields.Selection([('crystal', 'Crystal'), ('stone', 'Stone')])