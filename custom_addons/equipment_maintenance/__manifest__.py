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
        'views/dashboard_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'equipment_maintenance/static/src/components/dashboard/dashboard.js',
            'equipment_maintenance/static/src/components/dashboard/dashboard.xml',
        ],
    },
    'installable': True,
    'application': True,
}