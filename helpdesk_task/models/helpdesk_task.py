# Copyright 2019 Oscar Soto
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models, _


class HelpdeskTask(models.Model):
   
    _inherit = 'helpdesk.ticket'

    project_id = fields.Many2one(comodel_name='project.project',
                                 string='Project',
                                 required=False)
    task_id = fields.Many2one(comodel_name='project.task',
                              string='Task',
                              required=True)
    planned_hours = fields.Float(string='Planned hours',
                                 related='task_id.planned_hours',
                                 readonly=True)

    effective_hours = fields.Float(string='Effective hours',
                                   related='task_id.effective_hours',
                                   readonly=True)

    timesheet_ids = fields.One2many(comodel_name='project.task',
                                    inverse_name='task_id',
                                    string='Timesheet',
                                    related='task_id.timesheet_ids',
                                    required=True)
