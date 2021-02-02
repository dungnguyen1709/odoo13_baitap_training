from odoo import fields, models


class CreateNotification(models.TransientModel):
    _name = 'notification.wizards'
    _description = 'Wizards: Notification Friendly'

    amount_owed = fields.Many2one('sale.order', string='Amount Owed')
    partner_id = fields.Many2one('res.partner', string='Partner', related='amount_owed.partner_id')
    content = fields.Text(string='Content')
    is_email_receive = fields.Boolean('Receive Email', related='partner_id.is_receive_email')

    def send_email(self):
        if self.is_email_receive:
            print('123')

        return {
            'type': 'ir.actions.act_window_close'
        }