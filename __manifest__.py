# -*- coding: utf-8 -*-
{
    'name': "NaturalParks",

    'summary': """Manage Natural Parks""",

    'description': """
        Module for CA to manage natural parks:
            - visitors
            - own staff
            - acommodation
    """,

    'author': "Alberto Quintin",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/acommodation.xml',
        'views/trip.xml',
        'views/visitor.xml',
        'views/species.xml',
        'views/community.xml',
        'views/natural_park.xml',
        'views/area.xml',
        'views/staff.xml',
        'reports/report_trip.xml',
        'reports/report_project.xml',
    ],
    # only loaded in demonstration mode
    #'demo': [
    #    'demo.xml',
    #],
}