from odoo import models, fields, api

class Staff(models.Model):
    _name = 'naturalparks.staff'

    name = fields.Char(string="Name", required=True)
    dni = fields.Char(required=True)
    social_security = fields.Char(required=True)
    natural_park_id = fields.Many2one('naturalparks.natural_park', ondelete='cascade', string="Natural Park", required=True)
    address = fields.Char()
    mobile_phone = fields.Integer()
    landline = fields.Integer()
    salary = fields.Integer(string="Salary (in €)")

class Management(models.Model):
    _name = 'naturalparks.management'
    _inherit = 'naturalparks.staff'

    number_entrance = fields.Integer()

class Vigilance(models.Model):
    _name = 'naturalparks.vigilance'
    _inherit = 'naturalparks.staff'

    area_id = fields.Many2one('naturalparks.area', string="Area", required=True)
    car_id = fields.Many2one('naturalparks.car', string="Car", required=True)

class Car(models.Model):
    _name = 'naturalparks.car'

    name = fields.Char(string="Car Type")
    car_enrollment = fields.Char()

class Research(models.Model):
    _name = 'naturalparks.research'
    _inherit = 'naturalparks.staff'

    title = fields.Char()

class Project(models.Model):
    _name = 'naturalparks.project'

    name = fields.Char(string="Project Name", required=True)
    species_id = fields.Many2one('naturalparks.specie', string="Species", required=True)
    research_ids = fields.Many2many('naturalparks.research', string="Researchers", required=True)
    budget = fields.Float(string="Budget (in €)", digits=(8, 2))
    project_time = fields.Integer(string="Project Time (in months)")

class Conservation(models.Model):
    _name = 'naturalparks.conservation'
    _inherit = 'naturalparks.staff'

    area_id = fields.Many2one('naturalparks.area', string="Area", required=True)
    specialty = fields.Selection([('cleaning', 'Cleaning'), ('roads', 'Roads'), ('others', 'Others')]) 
