# Copyright 2018 Dario Lodeiros
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models

class HelpdeskTicket(models.Model):

    _name = 'helpdesk.ticket'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True)
    description = fields.Text('Description')
    date_deadline = fields.Datetime('Date limit')
    priority = fields.Selection([
        ('0','Low'),
        ('1','Medium'),
        ('2','Hight'),
        ('3','Very Hight')], default='0')
    partner_id = fields.Many2one('res.partner', 'Customer')
    team_id = fields.Many2one('helpdesk.team', 'Team')
