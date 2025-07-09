from odoo import models, fields

class ReportLine(models.Model):
    _name = 'cgf.report_line'
    _description = 'Report line'

    report_id = fields.Many2one('cgf.report', required=True, ondelete='cascade')
    course_name = fields.Char(required=True)
    teacher_name = fields.Char()
    hours = fields.Float(string="Course Hours")
    grade = fields.Float(string="Grade /100")