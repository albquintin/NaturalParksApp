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
    _order = 'name'
    _inherit = 'naturalparks.staff'

    number_entrance = fields.Integer()

class Vigilance(models.Model):
    _name = 'naturalparks.vigilance'
    _order = 'name'
    _inherit = 'naturalparks.staff'

    area_id = fields.Many2one('naturalparks.area', string="Area", required=True)
    car_id = fields.Many2one('naturalparks.car', string="Car", required=True)

    @api.onchange('natural_park_id')
    def onchange_acommodation_id(self):
        for r in self:
            return {'domain': {'area_id': [('natural_park_id', '=', r.natural_park_id.id)]}}


class Car(models.Model):
    _name = 'naturalparks.car'
    _order = 'name'

    name = fields.Char(string="Car Type", required=True)
    number_plate = fields.Char(string="Number Plate")
    color = fields.Integer()
    car_image = fields.Binary(string="Car Image", max_width=100, max_height=100, 
                            verify_resolution=False)

class Research(models.Model):
    _name = 'naturalparks.research'
    _order = 'name'
    _inherit = 'naturalparks.staff'

    title = fields.Char(required=True)

class Conservation(models.Model):
    _name = 'naturalparks.conservation'
    _order = 'name'
    _inherit = 'naturalparks.staff'

    area_id = fields.Many2one('naturalparks.area', string="Area", required=True)
    specialty = fields.Selection([('cleaning', 'Cleaning'), ('roads', 'Roads'), ('others', 'Others')]) 

    @api.onchange('natural_park_id')
    def onchange_acommodation_id(self):
        for r in self:
            return {'domain': {'area_id': [('natural_park_id', '=', r.natural_park_id.id)]}}
