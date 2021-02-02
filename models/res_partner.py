from odoo import models, fields, api, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    owe_limit = fields.Float(string='Owe Limit')

    owe_calculation = fields.Selection(
        selection=[('discount', 'Discount'), ('no discount', 'No Discount'), ('send by email', 'Send By Email')],
        string='Type', default='discount')

    is_receive_email = fields.Boolean(string="Receive Email", default=False)

    def get_remaining_debt(self):
        debt_amount = 0
        for invoice in self.invoice_ids:
            debt_amount += invoice.amount_residual_signed
        return self.owe_limit - debt_amount
