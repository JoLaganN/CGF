from odoo import models, fields, api

class CgfClass(models.Model):
    _name = 'cgf.class'


    name=fields.Char(string="name")
    name_holder_ids = fields.Many2one(comodel_name="res.partner", string="holder",domain=[("type_contact", "=", "holder")])
    name_students_ids = fields.Many2many(comodel_name="res.partner", string="students",domain=[("type_contact", "=", "student")])
    degree_ids = fields.Many2one(comodel_name="cgf.config.degree", string="degree")
    prog_ids=fields.Many2many(comodel_name="cgf.program",string="program")
