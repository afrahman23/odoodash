# -*- coding: utf-8 -*-
# from odoo import http


# class Dash(http.Controller):
#     @http.route('/dash/dash', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dash/dash/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('dash.listing', {
#             'root': '/dash/dash',
#             'objects': http.request.env['dash.dash'].search([]),
#         })

#     @http.route('/dash/dash/objects/<model("dash.dash"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dash.object', {
#             'object': obj
#         })
