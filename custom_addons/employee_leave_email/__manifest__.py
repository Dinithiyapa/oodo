{
    'name': 'employee_leave_email',
    'author': 'WireApps',
    'version': '1.0',
    'category': 'Human Resources',
    'depends': ['base', 'hr' , 'hr_payroll_community', 'base_setup', 'web'],
    "data": [
        "views/email_template.xml"
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}