# Copyright 2018 Dario Lodeiros
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models

class HelpdeskTeam(models.Model):

    _name = 'helpdesk.team'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True)
    user_ids = fields.Many2many('res.users', string='Members')
