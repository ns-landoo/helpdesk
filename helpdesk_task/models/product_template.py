from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    detour_included = fields.Boolean(string='Detour Included')


