from employee import Employee

class Developer(Employee):
    def __init__(self, name, employee_id, employee_email, role = "Developer"):
        super().__init__(name, employee_id, employee_email, role)

    def developer_details(self):
        return super().get_details()