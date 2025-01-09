from odoo import http
from odoo.http import request

class HrLeaveReportController(http.Controller):

    @http.route('/leaves/upcoming', type='http', auth='user', website=True)
    def upcoming_leaves(self):
        leave_model = request.env['hr.leave.report']
        upcoming_leaves = leave_model.get_upcoming_leaves()
        return request.render('employee_leave_email.upcoming_leaves_template', {'docs': upcoming_leaves})
