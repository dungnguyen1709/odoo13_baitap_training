from odoo import models, fields, api, _


class ResPartners(models.Model):
    _inherit = 'res.partner'

    debt_limit = fields.Integer(string='Debt Limit')
    debt_calculation = fields.Selection(selection_add=['type1', 'type2','type3'], string='Type')







