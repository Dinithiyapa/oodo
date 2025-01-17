from odoo import fields, models


class HelpdeskTicketSla(models.Model):
    _name = "helpdesk.ticket.sla"
    _description = "Helpdesk Ticket SLA"

    sla_id = fields.Many2one(string='ID', comodel_name="helpdesk.ticket.sla")
    name = fields.Char(string="Name", required=True)
    sequence = fields.Integer(default=10, string="Sequence")
    active = fields.Boolean(default=True, string="Active")

    # New fields added
    sla_type = fields.Selection([
        ('response', 'Response Time'),
        ('resolution', 'Resolution Time'),
    ], string="SLA Type", default='response', required=True)

    priority = fields.Selection([
        ("0", "Not set"),
        ("1", "Low"),
        ("2", "Medium"),
        ("3", "High"),
        ("4", "Critical"),
    ], string="Priority", required=True)

    description = fields.Text(string="Description")

    start_date = fields.Datetime(string="SLA Start Date")
    end_date = fields.Datetime(string="SLA End Date")

    time_to_resolve = fields.Integer(string="Time to Resolve (in hours)", required=True)
    time_to_respond = fields.Integer(string="Time to Respond (in hours)", required=True)

    sla_status = fields.Selection([
        ('active', 'Active'),
        ('archived', 'Archived'),
    ], string="SLA Status", default='active')

    company_id = fields.Many2one(
        comodel_name="res.company",
        string="Company",
        default=lambda self: self.env.company,
    )
