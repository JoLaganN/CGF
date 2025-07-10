from odoo import models, fields, api

class CgfConfigDegree(models.Model):
    _name = 'cgf.config.degree'
    _rec_name = 'degree'

    degree=fields.Integer(string="degree")


