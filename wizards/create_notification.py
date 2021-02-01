from odoo import fields, models


class CreateNotification(models.TransientModel):
    _name = 'notification.wizards'
    _description = 'Wizards: Notification Friendly'

    amount_owed = fields.Many2one('res.partner', string='Amount Owed')
    contend = fields.Text(string='Contend')

    def print_report(self):
        data = {
            'model': 'create.notification',
            'form': self.read()[0]
        }
        return self.env.ref('cm_credit_limit.report_notification').with_context(landscape=True).report_action(self,
                                                                                                              data=data)

    def delete_notification(self):
        for rec in self:
            rec.amount_owed.unlink()

    def create_notification(self):
        vals = {
            'amount_owed': self.amount_owed.id,
            'contend': self.contend,
            'notes': 'Created Form The Wizards/Code'
        }

        self.amount_owed.message_post(body='Test String', subject='Notification Creation')
        new_notification = self.env['res.partner'].create(vals)
        context = dict(self.env.context)
        import logging
        _logger = logging.getLogger(__name__)
