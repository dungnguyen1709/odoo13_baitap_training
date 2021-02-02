from odoo import fields, models, _


class CreateNotification(models.TransientModel):
    _name = 'notification.wizards'
    _description = 'Wizards: Notification Friendly'

    amount_owed = fields.Many2one('sale.order', string='Amount Owed')
    partner_id = fields.Many2one('res.partner', string='Partner', related='amount_owed.partner_id')
    content = fields.Text(string='Content')
    is_email_receive = fields.Boolean('Receive Email', related='partner_id.is_receive_email')
    # mail_id = fields.Char(string='Email')
    # user_id = fields.Many2one('res.users', string='PRO')
    # name_seq = fields.Char(string='Partner ID', required=True, copy=False, readonly=True,
    #                        index=True, default=lambda self: _('New'))

    def action_send_email(self):
        if self.is_email_receive:
            print('17O91997')
            template_id = self.env.ref('cm_credit_limit.sale_order_limit_email_template').id
            template = self.env['mail.template'].browse(template_id)
            template.send_mail(self.amount_owed.id, force_send=True)
        return {
            'type': 'ir.actions.act_window_close'
        }
