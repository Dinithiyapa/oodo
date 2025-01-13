from odoo import fields, models


class HelpdeskSLA(models.Model):
    """Helpdesk tags"""
    _name = 'helpdesk.sla'
    _description = 'Helpdesk SLA'

    name = fields.Char(string='SLA', help='SLA name of the helpdesk.')
