# -*- coding: utf-8 -*-
# from odoo import http


# class Mihw(http.Controller):
#     @http.route('/mihw/mihw', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mihw/mihw/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mihw.listing', {
#             'root': '/mihw/mihw',
#             'objects': http.request.env['mihw.mihw'].search([]),
#         })

#     @http.route('/mihw/mihw/objects/<model("mihw.mihw"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mihw.object', {
#             'object': obj
#         })
