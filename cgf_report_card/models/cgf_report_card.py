from odoo import models, fields, api
from odoo.odoo.exceptions import ValidationError


class ReportCard(models.Model):
    _name = 'cgf.report_card'


    card_id=fields.Char("Card id")


