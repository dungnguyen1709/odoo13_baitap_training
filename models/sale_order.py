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

            remaining_debt = rec.partner_id.get_remaining_debt()

            if rec.amount_total > remaining_debt:
                print(rec.amount_total)
                print(rec.partner_id.get_remaining_debt())

                content = f'Has exceeded the limit amount:  {remaining_debt - rec.amount_total}',
                return {
                    'name': _('Notification'),
                    'res_model': 'notification.wizards',
                    'view_mode': 'form',
                    'type': 'ir.actions.act_window',
                    'target': 'new',
                    'context': {
                        'default_amount_owed': self.id,
                        'default_content': content[0],
                    }
                }


