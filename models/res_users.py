# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResUser(models.Model):
    _inherit = 'res.users'
#     _description = 'dash.dash'

    ip = fields.Char(string="IP")
    mac = fields.Char(string="MAC Address")
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
