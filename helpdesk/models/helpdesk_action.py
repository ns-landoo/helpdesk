# Copyright 2018 Dario Lodeiros
# Copyright 2018 Angel Moya
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models, _


class HelpdeskAction(models.Model):

    _name = 'helpdesk.action'
    _description = 'Helpdesk Action'

    name = fields.Char()
    ticket_id = fields.Many2one(
        comodel_name='helpdesk.ticket',
        string='Ticket')
