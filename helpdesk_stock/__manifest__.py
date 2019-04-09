# Copyright 2019 Nagore Salaberria <ns@landoo.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
# -*- coding: utf-8 -*-
{
    'name': "Helpdesk Stock",
    'summary': "Module Helpdesk join to stock",
    'author': "Nagore Salaberria <ns@landoo.es>",
    'license': "AGPL-3",
    'category': 'Uncategorized',
    'version': "12.0.1.0.0",
    "application": True,
    "installable": True,
    'depends': ['stock'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/stock_picking_return_view.xml',
        'views/templates.xml',
    ],

}