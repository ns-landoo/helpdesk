# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockPickingReturn(models.TransientModel):

    _description = 'Stock Picking Return '
    _inherit = 'stock.return.picking'

    name = fields.Char()
    ticket_id = fields.Many2one(comodel_name="stock.return.picking",
                                string="Ticket")

    def create_returns(self):
        self.picking_id.write({
            'ticket_id': self.ticket_id,
        })
        return super(StockPickingReturn, self).create_returns()
