# -*- coding: utf-8 -*-
# from odoo import http


# class Adriano(http.Controller):
#     @http.route('/adriano/adriano', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/adriano/adriano/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('adriano.listing', {
#             'root': '/adriano/adriano',
#             'objects': http.request.env['adriano.adriano'].search([]),
#         })

#     @http.route('/adriano/adriano/objects/<model("adriano.adriano"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('adriano.object', {
#             'object': obj
#         })
