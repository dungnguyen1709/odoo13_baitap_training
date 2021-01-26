from odoo import models, fields, api, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    debt_limit = fields.Integer(string='Debt Limit')
    debt_calculation = fields.Selection(
        selection_add=[('discount', 'Discount'), ('no_discount', 'No Discount'), ('send_by_email', 'Send By Email')],
        string='Type')

    @api.depends('price')
    def yes_discount(self):
        for rec in self:
            if rec.price * 0.9:
                rec.discount = '10%'
            elif rec.price * 0.7:
                rec.discount = '30%'
            else:
                rec.discount = rec.price * 0.5
                rec.discount = '50%'

    discount = fields.Selection(selection=[('10%', 'Discount 10%'), ('30%', 'Discount 30%'), ('50%', 'Discount 50%')],
                                compute='yes_discount')

    @api.model
    def create(self, vals_list):
        res = super(ResPartner, self).create(vals_list)
        return res
