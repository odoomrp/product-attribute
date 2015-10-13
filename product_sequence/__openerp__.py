# -*- coding: utf-8 -*-
# (c) 2011 Zikzakmedia S.L. (http://zikzakmedia.com)
# (c) 2015 Oihane Crucelaegui - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name": "Product Sequence",
    "version": "8.0.0.1.0",
    "author": "Zikzakmedia SL, Odoo Community Association (OCA)",
    "website": "http://www.zikzakmedia.com",
    "license": "AGPL-3",
    "category": "Generic Modules/Inventory Control",
    "depends": [
        "product",
    ],
    "data": [
        "data/product_sequence.xml",
        "views/product_category_view.xml",
    ],
    "demo": [
        "demo/product_product.xml"
    ],
    "pre_init_hook": "update_null_and_slash_codes",
    "auto_install": False,
    "installable": True,
}
