# -*- coding: utf-8 -*-
from odoo import http

# class Hpcuser(http.Controller):
#     @http.route('/hpcuser/hpcuser/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hpcuser/hpcuser/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hpcuser.listing', {
#             'root': '/hpcuser/hpcuser',
#             'objects': http.request.env['hpcuser.hpcuser'].search([]),
#         })

#     @http.route('/hpcuser/hpcuser/objects/<model("hpcuser.hpcuser"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hpcuser.object', {
#             'object': obj
#         })