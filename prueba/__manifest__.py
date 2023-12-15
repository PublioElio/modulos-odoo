# -*- coding: utf-8 -*-
{
    'name': "prueba",

    'summary': """
        PRIMER MÓDULO DE PRUEBA """,

    'description': """
        Descripción de mi módulo
    """,

    'author': "Adriano Díaz",
    'website': "https://www.google.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
