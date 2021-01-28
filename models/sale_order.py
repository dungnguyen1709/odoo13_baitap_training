from odoo import fields, models, _


class ResPartner(models.Model):
    _inherit = "sale.order.line"

    owe_limit = fields.Integer(string='Owe Limit', default=5000)


class ResPartner(models.Model):
    _inherit = "sale.order"

    owe_limit = fields.Integer(string='Owe Limit', related="order_line.owe_limit")
