# -*- coding: utf-8 -*-
{
    'name': "test_odoo",

    'summary': """
        Prueba Tarea 27 Enero 2021, ENTRENAMIENTO ODOO""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Fernando Alvarez Villalvazo",
    'website': "http://www.SYSTEG.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/secuencias.xml',
        'views/res_partner.xml',
        'views/cabecera_cliente.xml',
        'report/report.xml',
        'report/tamplate.xml',
        'report/modify_report.xml',
        'report/modify_template.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}