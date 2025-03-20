# Copyright 2025 Fernando Plaza - ENZO
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    brand = fields.Char(
        string='Brand')
    
    eye_size = fields.Selection(
        selection=[
            ("40-43", "40-43"),
            ("44-46", "44-46"),
            ("47-49", "47-49"),
            ("50-53", "50-53"),
            ("54-56", "54-56"),
            ("57-UP", "57-UP"),
            ],
        string="Eye Size",
    )

    features = fields.Selection(
        selection=[
            ("limited-edition", "Limited-Edition"),
            ("mirrored", "Mirrored"),
            ("polarize", "Polarized"),
            ],
        string="Features",
    )

    material = fields.Selection(
        selection=[
            ("acetate", "Acetate"),
            ("combination", "Combination"),
            ("metal", "Metal"),
            ],
        string="Materials",
    ) 

    shape = fields.Selection(
        selection=[
            ("aviator", "Aviator"),
            ("cateye", "Cateye"),
            ("rectangle", "Rectangle"),
            ("round", "Round"),
            ("square", "Square"),
            ],
        string="Shape",
    ) 

    style = fields.Selection(
        selection=[
            ("men", "Men's"),
            ("women", "Women's"),
            ("unisex", "Unisex"),
            ],
        string="Style",
    ) 

    size = fields.Char(
        string='Size')
    