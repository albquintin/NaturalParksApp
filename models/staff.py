from datetime import timedelta
from odoo import models, fields, api, exceptions

class Staff(models.Model):
    _name = 'naturalparks.staff'

    name = fields.Char(string="Name", required=True)
    dni = fields.Char(required=True)
    social_security = fields.Char(required=True)
    natural_park_id = fields.Many2one('naturalparks.natural_park', ondelete='cascade', string="Natural Park", required=True)
    address = fields.Char()
    mobile_phone = fields.Char()
    landline = fields.Char()
    salary = fields.Integer(string="Salary (in €, annual)")

    @api.constrains('salary')
    def _check_park_has_extension(self):
        for r in self:
            if r.salary <= 0:
                raise exceptions.ValidationError("The salary must be positive")

class Management(models.Model):
    _name = 'naturalparks.management'
    _inherit = 'naturalparks.staff'

    number_entrance = fields.Integer()

class Vigilance(models.Model):
    _name = 'naturalparks.vigilance'
    _inherit = 'naturalparks.staff'

    area_id = fields.Many2one('naturalparks.area', string="Area", required=True)
    car_id = fields.Many2one('naturalparks.car', string="Car", required=True)

    @api.constrains('natural_park_id', 'area_id')
    def _check_area_is_in_the_park(self):
        for r in self:
            if r.area_id.natural_park_id != r.natural_park_id:
                raise exceptions.ValidationError("The area must be in the park")


class Car(models.Model):
    _name = 'naturalparks.car'

    name = fields.Char(string="Car Type", required=True)
    car_enrollment = fields.Char()

class Research(models.Model):
    _name = 'naturalparks.research'
    _inherit = 'naturalparks.staff'

    title = fields.Char(required=True)

class Project(models.Model):
    _name = 'naturalparks.project'

    name = fields.Char(string="Project Name", required=True)
    species_id = fields.Many2one('naturalparks.species', string="Species", required=True)
    research_ids = fields.Many2many('naturalparks.research', string="Researchers", required=True)
    budget = fields.Float(string="Budget (in €)", digits=(8, 2))
    starting_date = fields.Date()
    ending_date = fields.Date()

    @api.constrains('budget')
    def _check_park_has_extension(self):
        for r in self:
            if r.budget <= 0:
                raise exceptions.ValidationError("The budget must be positive")

class Conservation(models.Model):
    _name = 'naturalparks.conservation'
    _inherit = 'naturalparks.staff'

    area_id = fields.Many2one('naturalparks.area', string="Area", required=True)
    specialty = fields.Selection([('cleaning', 'Cleaning'), ('roads', 'Roads'), ('others', 'Others')]) 

    @api.constrains('natural_park_id', 'area_id')
    def _check_area_is_in_the_park(self):
        for r in self:
            if r.area_id.natural_park_id != r.natural_park_id:
                raise exceptions.ValidationError("The area must be in the park")
