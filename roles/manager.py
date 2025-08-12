from employee import Employee

class Manager(Employee):
    def __init__(self, name, employee_id, employee_email, role = "Manager"):
        super().__init__(name, employee_id, employee_email, role)

    def manager_details(self):
        return super().get_details()