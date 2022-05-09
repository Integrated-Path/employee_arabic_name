# -*- coding: utf-8 -*-
# from odoo import http


# class EmployeeArabicName(http.Controller):
#     @http.route('/employee_arabic_name/employee_arabic_name', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/employee_arabic_name/employee_arabic_name/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('employee_arabic_name.listing', {
#             'root': '/employee_arabic_name/employee_arabic_name',
#             'objects': http.request.env['employee_arabic_name.employee_arabic_name'].search([]),
#         })

#     @http.route('/employee_arabic_name/employee_arabic_name/objects/<model("employee_arabic_name.employee_arabic_name"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('employee_arabic_name.object', {
#             'object': obj
#         })
