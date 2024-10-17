{
    'name': 'Employee Benefits',
    'version': '17.0',
    'description': 'Manage Your Employee Benefits',
    'summary': '',
    'author': 'Abdelrhman Gouda',
    'website': '',
    'license': 'LGPL-3',
    'category': '',
    'depends': [
        'base',
        'hr',
    ],
    'data': [
        # data
        'data/lead_group.xml',
        # security
        'security/ir.model.access.csv',
        'security/employee_benefits_security.xml',
        #views
        'views/benefits_view.xml',
        # menus
        'views/menu_items.xml',
        # reports
        'report/employee_benefit_pivot_report.xml',
        'report/employees_view.xml',

    ],
    'auto_install': False,
    'application': True,
}
