# -*- coding: utf-8 -*-
# from odoo import http


# class Redom(http.Controller):
#     @http.route('/redom/redom', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/redom/redom/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('redom.listing', {
#             'root': '/redom/redom',
#             'objects': http.request.env['redom.redom'].search([]),
#         })

#     @http.route('/redom/redom/objects/<model("redom.redom"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('redom.object', {
#             'object': obj
#         })
