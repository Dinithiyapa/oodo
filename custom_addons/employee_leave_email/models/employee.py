import logging
from datetime import timedelta
from odoo import fields, models, api

# Set up a logger for the model
_logger = logging.getLogger(__name__)

class HrLeaveReportCalendar(models.Model):
    _inherit = 'hr.leave.report'

    @api.model
    def get_upcoming_leaves(self):
        today = fields.Datetime.now()
        two_weeks_later = today + timedelta(weeks=2)

        # Search for approved leaves within the next two weeks
        leaves = self.search([
            ('date_from', '>=', today),
            ('date_to', '<=', two_weeks_later),
            ('state', '=', 'validate')  # Approved leaves
        ])

        # Log the number of leaves found
        _logger.info(f"Found {len(leaves)} leaves between {today} and {two_weeks_later}.")

        leave_data = []
        for leave in leaves:
            _logger.info(f"Processing leave for employee: {leave.employee_id.name}")
            leave_data.append({
                'employee_name': leave.employee_id.name,
                'leave_days': (leave.date_to - leave.date_from).days + 1,
                'start_date': leave.date_from,
                'end_date': leave.date_to,
            })

        # Log the final leave data
        _logger.info(f"Leave data: {leave_data}")
        return leave_data
