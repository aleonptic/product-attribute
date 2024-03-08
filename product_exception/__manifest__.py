{
    "name": "Product Exception",
    "summary": "Ensure products are valid against a set of rules",
    "version": "13.0.1.0.1",
    "development_status": "Beta",
    "category": "Quality",
    "website": "https://github.com/OCA/product-attribute",
    "author": "Akretion, Odoo Community Association (OCA)",
    "maintainers": ["hparfr"],
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["stock", "base_exception"],
    "demo": ["demo/product_exception.xml"],
    "data": [
        "data/data.xml",
        "views/exception_rule_views.xml",
        "views/product_template_views.xml",
    ],
}
