from odoo import models, fields

class ReportPeriod(models.Model):
    _name = 'cgf.report_period'
    _description = 'Reports Period'

    name = fields.Char(required=True)
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)
    period_type = fields.Selection([('certif', 'Certificative'), ('formatif', 'Formative')], required=True)
    percentage = fields.Float(string="Weight for the year (%)")
