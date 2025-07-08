from odoo import models, fields, api


class Partner(models.Model):
    _inherit = 'res.partner'

    type_contact=fields.Selection(selection=[("student", "Student"), ("professor", "Professor"), ("holder", "Holder"),("secretariat/direction","Secretariat/Direction"), ("other", "Other")])