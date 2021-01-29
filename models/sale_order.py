from odoo import fields, api, models, _
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    owe_limit = fields.Integer(string='Owe Limit', related='partner_id.owe_limit')
    remaining_debt = fields.Float(string='Remaining Debt', readonly=True)

    @api.onchange('partner_id')
    def get_remaining_debt(self):
        for rec in self:
            rec.remaining_debt = rec.partner_id.get_remaining_debt()
            print(rec.remaining_debt)

    def action_confirm(self):
        for rec in self:
            cart_total = 0
            for product in rec.order_line:
                cart_total += product.price_subtotal

            if cart_total > rec.partner_id.get_remaining_debt():
                print(cart_total)
                print(rec.partner_id.get_remaining_debt())
                return {
                    'name': _('Sale'),
                    'view_type': 'form',
                    'res_model': 'sale.order',
                    'view_id': False,
                    'view_mode': 'tree,form',
                    'type': 'ir.actions.act_window',
                    'type': 'ir.actions.act_window',
                }
            else:
                super(SaleOrder, self).action_confirm()

    # @api.onchange('order_line')
    # def check_can_buy(self):
    #     for rec in self:
    #         if rec.partner_id:
    #             cart_total = 0
    #             for product in rec.order_line:
    #                 cart_total += product.price_subtotal
    #                 if cart_total > rec.remaining_debt:
    #                     raise ValidationError('DMM')
