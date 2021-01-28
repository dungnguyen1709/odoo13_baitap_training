from odoo import fields, models, _, api


class SaleOrder(models.Model):
    _inherit = "sale.order.line"

    no_discount = fields.Boolean(string='No Discount')


class SaleOrders(models.Model):
    _inherit = "sale.order"

    owe_limit = fields.Integer(string='Owe Limit', default=5000, readonly=True)

    # product_id = fields.Many2one('product.product', string='Product', readonly=True)
    #
    # price = fields.Float('Total Price', compute='check_total_price_product', readonly=True, store=True)
    #
    # @api.onchange('order_line')
    # def check_total_price_product(self):
    #
