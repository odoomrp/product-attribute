# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields, api
from openerp.tools.translate import _


def update_null_and_slash_codes(cr):  # pragma: no cover
    """
    Updates existing codes matching the default '/' or
    empty. Primarily this ensures installation does not
    fail for demo data.
    :param cr: database cursor
    :return: void
    """
    cr.execute("""UPDATE product_product
                     SET default_code = '!!mig!!' || id
                   WHERE default_code IS NULL OR default_code = '/';""")


class ProductProduct(models.Model):
    _inherit = 'product.product'

    default_code = fields.Char(
        string='Reference', select=True, required=True, default='/')

    _sql_constraints = [
        ('uniq_default_code', 'unique(default_code)',
         'The reference must be unique'),
    ]

    @api.model
    def create(self, vals):
        if vals.get('default_code', '/') == '/'and vals.get('categ_id'):
            categ = self.env['product.category'].browse(vals['categ_id'])
            sequence = (categ.sequence_id or
                        self.env.ref('product_sequence.seq_product_auto'))
            vals['default_code'] = (
                sequence and
                self.env['ir.sequence'].next_by_id(sequence.id))
        return super(ProductProduct, self).create(vals)

    @api.multi
    def write(self, vals):
        for product in self:
            if product.default_code in [False, '/']:
                vals['default_code'] = self.env['ir.sequence'].get(
                    'product.product')
            super(ProductProduct, product).write(vals)
        return True

    @api.one
    def copy(self, default=None):
        if default is None:
            default = {}
        if self.default_code:
            default.update({
                'default_code': self.default_code + _('-copy'),
            })
        return super(ProductProduct, self).copy(default)
