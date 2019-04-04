# Copyright 2017 Dario Lodeiros - Dario Lodeiros <dariodafoz@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "HelpDesk",
    "summary":
        "Module to Support Teams",
    "version": "12.0.1.0.0",
    "category": "Customer Relationship Management",
    "website": "",
    "author": "Dario Lodeiros Vazquez <dariodafoz@gmail.com>",
    "license": "AGPL-3",
    "data": [
        "views/helpdesk_ticket_views.xml",
        "views/helpdesk_team_views.xml",
        "security/helpdesk_security.xml",
        "security/ir.model.access.csv",
        ],
    "application": True,
    "installable": True,
    "depends": ["base","mail"],
}
