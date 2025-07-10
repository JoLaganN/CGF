# -*- coding: utf-8 -*-
{
    'name': "CGF",

    'summary': "CGF.base",

    'description': """
School Base
    """,

    'author': "joachim henry",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'views/base_views.xml',
        'views/res_partner_views.xml',
        'views/cgf_student_views.xml',
        'views/cgf_lessons_views.xml',
        'views/cgf_config_type_views.xml',
        'views/cgf_config_degree_views.xml',
        'views/cgf_program_views.xml',
        'views/cgf_class_views.xml',
    ],
    'sequence': -100,
}
