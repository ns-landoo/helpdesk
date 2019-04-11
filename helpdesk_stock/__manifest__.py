# Copyright 2019 Nagore Salaberria <ns@landoo.es>
# Copyright 2019 Oscar Soto <osoto@sdi.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
# -*- coding: utf-8 -*-
{
    'name': "Helpdesk Stock",
    'summary': "Module Helpdesk join to stock",
    'author': "Nagore Salaberria <ns@landoo.es>,Oscar Soto",
    'license': "AGPL-3",
    'category': 'Uncategorized',
    'version': "12.0.1.0.0",
    "application": False,
    "installable": True,
    'depends': [
        'stock',
        'helpdesk'
    ],
    'data': [
        'views/helpdesk_ticket.xml',
        'views/stock_picking.xml',
        'wizards/stock_picking_return_wizard.xml',
        'report/inherit_report_picking.xml',
    ],

}
