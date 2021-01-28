from odoo import models, fields, api, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    owe_limit = fields.Integer(string='Owe Limit', default=5000, readonly=True)
    no_discount = fields.Boolean(string='No Discount')


