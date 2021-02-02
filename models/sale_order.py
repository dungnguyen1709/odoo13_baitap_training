from odoo import fields, api, models, _
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    owe_limit = fields.Float(string='Owe Limit', related='partner_id.owe_limit')
    remaining_debt = fields.Float(string='Remaining Debt', readonly=True)

    @api.onchange('partner_id')
    def get_remaining_debt(self):
        for rec in self:
            rec.remaining_debt = rec.partner_id.get_remaining_debt()
            print(rec.remaining_debt)

    def action_confirm(self):
        for rec in self:
            super(SaleOrder, rec).action_confirm()

            cart_total = 0
            for product in rec.order_line:
                cart_total += product.price_subtotal

            if cart_total > rec.partner_id.get_remaining_debt():
                print(cart_total)
                print(rec.partner_id.get_remaining_debt())
                content = 'dit me may'
                return {
                    'name': _('Thong bao'),
                    'res_model': 'notification.wizards',
                    'view_mode': 'form',
                    'type': 'ir.actions.act_window',
                    'target': 'new',
                    'context': {
                        'default_amount_owed': self.id,
                        'default_content': content,
                    }
                }


    def test_name(self):
        view_id = self.env.ref('cm_credit_limit.create_notification_wizard').id
        print(view_id)
        return {
            'name': _('Thong bao'),
            'res_model': 'notification.wizards',
            'view_mode': 'form',
            'type': 'ir.actions.act_window',
            'target': 'new',
            'context': {
                'default_amount_owed': self.id
            }
        }

    # @api.onchange('order_line')
    # def check_can_buy(self):
    #     for rec in self:
    #         if rec.partner_id:
    #             cart_total = 0
    #             for product in rec.order_line:
    #                 cart_total += product.price_subtotal
    #                 if cart_total > rec.remaining_debt:
    #                     raise ValidationError('DMM')
