# -*- coding: utf-8 -*-
{
    'name': "Odoo Training Bootcamp",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "Rimba",
    'website': "https://www.rimbashr.my.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'mail',
        'stock',
        'sale_management',
        ],

    # always loaded
    'data': [
        'report/report_action.xml',
        'report/report_training_session.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/training_views.xml',
        'views/partner_views.xml',
        'wizard/training_wizard_views.xml',
        'views/menuitem_views.xml',
        'data/scheduler_data.xml',
        'data/sequence_data.xml',
        'data/data.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}

