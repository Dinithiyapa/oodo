{
    'name': 'helpdesk_sla',
    'author': 'WireApps',
    'version': '1.0',
    'category': 'Help Desk',
    'depends': ['base','web' ,'helpdesk_mgmt'],
    "data": [
        "views/helpdesk_ticket_sla_view.xml",
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}