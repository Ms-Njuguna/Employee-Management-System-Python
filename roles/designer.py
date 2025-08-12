from employee import Employee

class Designer(Employee):
    def __init__(self, name, employee_id, employee_email, salary, role = "Designer"):
        super().__init__(name, employee_id, employee_email, role, salary)

    def designer_details(self):
        return super().get_details()