from odoo import models, fields, api, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    owe_limit = fields.Integer(string='Owe Limit', default=5000, readonly=True)

    owe_calculation = fields.Selection(
        selection=[('discount', 'Discount'), ('no discount', 'No Discount'), ('send by email', 'Send By Email')],
        string='Type', default='discount')
