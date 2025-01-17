from odoo import fields, models


class HelpdeskTicketTag(models.Model):
    _name = "helpdesk.ticket.sla"
    _description = "Helpdesk Ticket SLA"
    sla_id = fields.Many2one(string='ID')
    name = fields.Char()
    sequence = fields.Integer(default=10)
    color = fields.Integer(string="Color Index")
    active = fields.Boolean(default=True)
    company_id = fields.Many2one(
        comodel_name="res.company",
        string="Company",
        default=lambda self: self.env.company,
    )
