# Copyright (C) 2016-Today: La Louve (<http://www.lalouve.net/>)
# Copyright (C) 2022-Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class ProductProduct(models.Model):
    _name = "product.product"
    _inherit = ["product.product", "product.print.category.mixin"]

    # Columns Section
    print_category_id = fields.Many2one(
        string="Print Category",
        comodel_name="product.print.category",
        default=lambda s: s._default_print_category_id(),
    )

    to_print = fields.Boolean()

    @api.onchange("print_category_id")
    def onchange_print_category_id(self):
        self.to_print = bool(self.print_category_id)

    # Default Section
    def _default_print_category_id(self):
        return self.env.user.company_id.print_category_id

    @api.model_create_multi
    def create(self, vals_list):
        if not self.env.context.get("to_print_ok", False):
            for vals in vals_list:
                # if not explicitely defined, we guess "to_print" value,
                # based on the print_category_id value.
                if "to_print" not in vals:
                    vals["to_print"] = bool(vals.get("print_category_id", False))
        return super(ProductProduct, self.with_context(to_print_ok=True)).create(
            vals_list
        )
