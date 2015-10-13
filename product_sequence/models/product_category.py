# -*- coding: utf-8 -*-
# (c) 2015 Oihane Crucelaegui - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp import api, fields, models


class ProductCategory(models.Model):
    _inherit = 'product.category'

    @api.model
    def _get_domain_sequence_id(self):
        seq_type = self.env.ref('product_sequence.seq_product_auto_type')
        domain = [('code', '=', seq_type.code)]
        return domain

    sequence_id = fields.Many2one(
        comodel_name='ir.sequence', string='Sequence', copy=False,
        domain=_get_domain_sequence_id)
