from odoo import models, fields, api

class ClassNewspaperComments(models.Model):
    _name = 'cgf.class_newspaper_comments'

    # student_ids = fields.Many2one(str="Student")
    # professor_ids = fields.Many2one(str="Professor")
    comments = fields.Text(str="Comments")
    severity = fields.Integer(str="Severity")
    is_confirmed_by_parent = fields.Boolean(str="Confirmed By Parents")

    # def open_action_send_email(self):
    #     template = self.env.ref(module_name.absence_mail_template)
    #     email_values = {'email_from': self.env.user.email}
    #     template.send_mail(self.id, force_send=True, email_values=email_values)

    # def open_loan_wizard(self):
    #     action = {
    #         'name': 'Make A Loan',
    #         'type': 'ir.actions.act_window',
    #         'res_model': 'library.loan.wizard',
    #         'view_mode': 'form',
    #         'target': 'new',
    #         'context': {
    #             'default_member_id': self.member_id.id,
    #             'default_return_date_due': self.return_date_due,
    #         # 'domain': [('member_id', '=', self.id)]
    #     }}
    #
    #     return action