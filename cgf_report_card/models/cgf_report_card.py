from odoo import models, fields, api
from datetime import datetime

class Report(models.Model):
    _name = 'cgf.report'
    _description = "Student's report"
    _order = 'sequence'

    sequence = fields.Char(string='Report ID', required=True, copy=False, readonly=True, default='New')
    date = fields.Date(required=True)
    student_id = fields.Many2one('res.partner', domain=[('type_contact', '=', "student")], required=True)
    homeroom_teacher = fields.Many2one('res.partner', domain=[('type_contact', '=', "professor")], required=True)
    classroom = fields.Char(string="Class")
    period_id = fields.Many2one('cgf.report_period', required=True)
    line_ids = fields.One2many('cgf.report_line', 'report_id', string="Courses")
    average = fields.Float(compute='_compute_averages', store=True)
    weighted_average = fields.Float(compute='_compute_averages', store=True)

    @api.model_create_multi
    def create(self, vals_list):

        records = super().create(vals_list)
        for rec in records:
            period_name = rec.period_id.name
            student_name=rec.student_id.name
            date= rec.date or fields.Date.today()
            year = datetime.strptime(date, '%Y-%m-%d').year if isinstance(date, str) else date.year

            rec.sequence= f"{year}/{period_name}/{student_name}"
        return records

    @api.depends('line_ids.grade', 'line_ids.hours')
    def _compute_averages(self):
        for rec in self:
            grades = [line.grade for line in rec.line_ids if line.grade is not None]
            total_hours = sum(line.hours for line in rec.line_ids if line.hours)

            rec.average = sum(grades) / len(grades) if grades else 0.0
            rec.weighted_average = (
                sum(line.grade * line.hours for line in rec.line_ids if line.grade and line.hours) / total_hours
                if total_hours else 0.0
            )
