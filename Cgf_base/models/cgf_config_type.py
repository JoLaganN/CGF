from odoo import models, fields, api

class CgfConfigType(models.Model):
    _name = 'cgf.config.type'
    _rec_name = 'lessons_type'


    lessons_type = fields.Char(string="type")



    #select_professor_id= fields.Many2one(comodel_name="res.partner",string="professor",domain=[("type_contact","=","professor")])

