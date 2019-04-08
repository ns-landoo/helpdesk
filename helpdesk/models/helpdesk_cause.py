# Copyright 2018 Dario Lodeiros
# Copyright 2018 Angel Moya
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models, _


class HelpdeskCause(models.Model):

    _name = 'helpdesk.cause'
    _description = 'Helpdesk Cause'

    name = fields.Char()