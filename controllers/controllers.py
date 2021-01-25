# -*- coding: utf-8 -*-
# from odoo import http


# class CmCreditLimit(http.Controller):
#     @http.route('/cm_credit_limit/cm_credit_limit/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cm_credit_limit/cm_credit_limit/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cm_credit_limit.listing', {
#             'root': '/cm_credit_limit/cm_credit_limit',
#             'objects': http.request.env['cm_credit_limit.cm_credit_limit'].search([]),
#         })

#     @http.route('/cm_credit_limit/cm_credit_limit/objects/<model("cm_credit_limit.cm_credit_limit"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cm_credit_limit.object', {
#             'object': obj
#         })
