from odoo import models, fields, api

class CgfLessons(models.Model):
    _name = 'cgf.lessons'

    cover = fields.Binary(string='cover')
    name= fields.Char(string="Name")
    lessons_type = fields.Char(string="type")
    nb_hour=fields.Float(string="number of hour")
    degree=fields.Integer(string="degree")
    select_professor_id= fields.Many2one(comodel_name="res.partner",string="professor",domain=[("type_contact","=","professor")])


