from employee import Employee

class Developer(Employee):
    def __init__(self, name, employee_id, employee_email, salary, role = "Developer"):
        super().__init__(name, employee_id, employee_email, role, salary)

    def developer_details(self):
        return super().get_details()