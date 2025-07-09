from odoo import models, fields, api

class CgfStudent(models.Model):
    _name = 'cgf.students'


    name_students_ids=fields.Many2one(comodel_name="res.partner",string="Name",domain=[("type_contact","=","student")])

    student_avatar = fields.Image(related='name_students_ids.avatar_128', string="Avatar Étudiant")




