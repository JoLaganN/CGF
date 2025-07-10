from odoo import models, fields, api

class CgfLessons(models.Model):
    _name = 'cgf.lessons'
    _rec_name = "name"

    cover = fields.Binary(string='cover')
    name= fields.Char(string="Name")
    lessons_type_ids = fields.Many2one(comodel_name="cgf.config.type",string="type")
    nb_hour=fields.Float(string="number of hour")
    degree_ids=fields.Many2one(comodel_name="cgf.config.degree",string="degree")
    select_professor_id= fields.Many2one(comodel_name="res.partner",string="professor",domain=[("type_contact","=","professor")])


