# -*- coding: utf-8 -*-
from odoo import http

# class TestOdoo(http.Controller):
#     @http.route('/test_odoo/test_odoo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test_odoo/test_odoo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('test_odoo.listing', {
#             'root': '/test_odoo/test_odoo',
#             'objects': http.request.env['test_odoo.test_odoo'].search([]),
#         })

#     @http.route('/test_odoo/test_odoo/objects/<model("test_odoo.test_odoo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test_odoo.object', {
#             'object': obj
#         })