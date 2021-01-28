from odoo import models, fields, api, _


class ResPartner(models.Model):
    _inherit = 'res.partner'
    _name = 'partner.model'

    owe_limit = fields.Integer(string='Owe Limit', default=5000, readonly=True)

    owe_calculation = fields.Selection(
        selection=[('discount', 'Discount'), ('no discount', 'No Discount'), ('send by email', 'Send By Email')],
        string='Type', default='discount')

    # debts = fields.One2many(string='Debts', 'account.model', 'account_id')


class AccountMove(models.Model):
    _name = 'account.model'

    account_id = fields.Many2one('partner.model', string='Account ID')
