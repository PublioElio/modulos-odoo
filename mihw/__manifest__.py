# -*- coding: utf-8 -*-
{
    'name': "MIHW",

    'summary': """
        Este módulo es para gestionar una tienda de equipos informáticos""",

    'description': """
        Este módulo es para gestionar una tienda de equipos informáticos
    """,

    'author': "Adriano Díaz",
    'website': "https://github.com/PublioElio",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/equipo.xml',
        'views/comprador.xml',
        'views/componente.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
