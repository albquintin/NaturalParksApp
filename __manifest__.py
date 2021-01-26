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

    'category': 'Test',
    'version': '0.1',

    'depends': ['base', 'board'],

    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/acommodation.xml',
        'views/trip.xml',
        'views/visitor.xml',
        'views/species.xml',
        'views/community.xml',
        'views/natural_park.xml',
        'views/area.xml',        
        'views/staff.xml',
        'views/project.xml',
        'views/animal_board.xml',
        'views/plant_board.xml',
        'views/trip_board.xml',
        'views/project_board.xml',
        'reports/report_trip.xml',
        'reports/report_project.xml',
        'reports/report_visitor.xml',
        'reports/report_research.xml',
        'reports/report_management.xml',
        'reports/report_conservation.xml',
        'reports/report_vigilance.xml',
    ],
}