{
    'name': 'Equipment Maintenance',
    'version': '1.0',
    'summary': 'Управління обладнанням та заявками на обслуговування',
    'category': 'Maintenance',
    'depends': ['base', 'mail'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/equipment_views.xml',
        'views/request_views.xml',
        'views/history_views.xml', 
        'views/report_views.xml',
    ],
    'installable': True,
    'application': True,
}