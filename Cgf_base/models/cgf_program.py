from odoo import models, fields, api


class CgfProgram(models.Model):
    _name = 'cgf.program'
    _rec_name = 'name'

    name = fields.Char(string="Name")
    lessons_ids = fields.Many2many(comodel_name="cgf.lessons", string="lessons")
    nb_hour_prog = fields.Float(string="nb hour", compute="_compute_nb_hour_lessons", store=True)

    @api.depends('lessons_ids')
    def _compute_nb_hour_lessons(self):
        for record in self:
            total = 0.0
            for lesson in record.lessons_ids:
                total += lesson.nb_hour or 0.0
            record.nb_hour_prog = total
