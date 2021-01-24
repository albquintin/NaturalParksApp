from odoo import models, fields, api, exceptions

class Species(models.Model):
    _name = 'naturalparks.species'

    name = fields.Char(string="Binomial nomenclature", required=True)
    common_name = fields.Char(required=True)
    area_ids = fields.Many2many('naturalparks.area', string="Area", required=True)
    number_of_specimens = fields.Integer()

    @api.constrains('number_of_specimens')
    def _check_number_is_positive(self):
        for r in self:
            if r.number_of_specimens <= 0:
                raise exceptions.ValidationError("The number must be positive")

class Plant(models.Model):
    _name = 'naturalparks.plant'
    _inherit = 'naturalparks.species'

    blooming = fields.Boolean(string="Does the plant have blooming?")
    blooming_period = fields.Selection([('spring', 'Spring'), ('summer', 'Summer'), ('autumn', 'Autumn'), ('winter', 'Winter')])

    is_eaten = fields.Boolean(string="Is this plant eaten?")
    animal_ids = fields.Many2many('naturalparks.animal', string="Herbivores which eat this plant", 
        domain=[('alimentation', '!=', 'carnivore')])

    @api.constrains('blooming', 'blooming_period')
    def _check_plant_has_blooming(self):
        for r in self:
            if not r.blooming and r.blooming_period:
                raise exceptions.ValidationError("Mark if the plant has blooming before adding the period")

    @api.constrains('is_eaten', 'animal_ids')
    def _check_animals_are_herbivores_or_omnivores(self):
        for r in self:
            if not r.is_eaten and r.animal_ids:
                raise exceptions.ValidationError("Mark if the plant is eaten before adding the herbivores which eat this plant")


class Animal(models.Model):
    _name = 'naturalparks.animal'
    _inherit = 'naturalparks.species'

    alimentation = fields.Selection([('carnivore','Carnivore'), ('herbivore','Herbivore'), ('omnivore','Omnivore')], required=True)
    mating_season = fields.Selection([('spring', 'Spring'), ('summer', 'Summer'), ('autumn', 'Autumn'), ('winter', 'Winter')])
    color = fields.Integer()

    is_eaten = fields.Boolean(string="Is this animal eaten?")
    animal_ids = fields.Many2many(comodel_name='naturalparks.animal', relation='animals_eaten', column1='prey', column2='carnivores', string="Carnivores which eat this animal",
        domain=[('alimentation', '!=', 'herbivore')])

    @api.constrains('is_eaten', 'animal_ids')
    def _check_animals_are_carnivores_or_omnivores(self):
        for r in self:
            if not r.is_eaten and r.animal_ids:
                raise exceptions.ValidationError("Mark is_eaten before the herbivores which eat this plant")


class Mineral(models.Model):
    _name = 'naturalparks.mineral'
    _inherit = 'naturalparks.species'

    mineral_type = fields.Selection([('crystal', 'Crystal'), ('stone', 'Stone')], required=True)
    color = fields.Integer()