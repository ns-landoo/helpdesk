# -*- coding: utf-8 -*-

from odoo import models, fields, api

class helpdeskStockPickingReturn(models.TransientModel):

    _description = 'Helpdesk Stock Picking Return '
    _inherit = 'stock.return.picking'

    name = fields.Char()
    ticket_id = fields.Many2one(comodel_name="stock.return.picking",
                                string="Ticket")