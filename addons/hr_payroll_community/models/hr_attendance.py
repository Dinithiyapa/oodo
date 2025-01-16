from odoo import fields, models, api

class HrAttendance(models.Model):
    _name = 'payslip.employee.attendance'
    _description = 'Employee Attendance'

    worked_days = fields.Float(string='Worked Days', help="Number of days worked")

    def _compute_working_days(self, employee_id=None):
        print("Computing worked days for employees")
        print(f"Employee ID: {employee_id}")

        if not employee_id:
            print("No employee ID provided")
            return 0  # Return a default value if no employee_id is provided

        # Search for attendance records related to the given employee_id
        attendance_records = self.env['hr.attendance'].search([('employee_id', '=', employee_id)])
        print(f"Attendance Records: {attendance_records}")

        # Count the unique attendance records (or simply their IDs)
        worked_days = len(attendance_records.ids)

        print(f"Computed worked_days for Employee ID {employee_id}: {worked_days}")
        return worked_days


