# Copyright 2019 Nagore Salaberria <ns@landoo.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
# -*- coding: utf-8 -*-
{
    'name': "Helpdesk Task",
    'summary': "Module Helpdesk join to Projects Task",
    'author': "Nagore Salaberria <ns@landoo.es>",
    'license': "AGPL-3",
    'category': 'Uncategorized',
    'version': "12.0.1.0.0",
    'application': False,
    'installable': True,
    'depends': [
        'sale_timesheet',
        'project',
        'helpdesk',
        'helpdesk_stock'
    ],
    'data': [
        'views/helpdesk_task_view.xml',
        'security/ir.model.access.csv',
    ],
}
