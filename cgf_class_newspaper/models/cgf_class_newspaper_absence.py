from odoo import models, fields, api

class ClassNewspaperAbsence(models.Model):
    _name = 'cgf.class_newspaper_absence'
    _inherit = 'mail.thread'

    # absent_student_ids = fields.Many2one(str="Absent Student")
    absence_type = fields.Text(str="Absence Type")
    # assigned_teacher = fields.Many2one(str="Assigned Teacher")
    date = fields.Date(str="Date")
    schedule = fields.Selection([
        ('morning', "Morning"),
        ('afternoon', "Afternoon"),
    ], string="Schedule")
    justified = fields.Boolean(str="Justified")
