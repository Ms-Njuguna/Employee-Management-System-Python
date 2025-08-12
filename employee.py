class Employee():
    def __init__(self, name, employee_id, employee_email, role):
        self.name = name
        self.employee_id = employee_id
        self.employee_email = employee_email
        self.role = role

    def get_details(self):
        return (f"Employee name: {self.name}\n"
                f"Employee ID: {self.employee_id}\n"
                f"Employee Email: {self.employee_email}\n"
                f"Role: {self.role}\n")
    
    def responsibilities(self):
        if self.role.lower() == "manager":
            return f"{self.name} is responsible for supervising the team."
        elif self.role.lower() == "developer":
            return f"{self.name} is responsible for writing and reviewing code."
        elif self.role.lower() == "designer":
            return f"{self.name} is responsible for creating UI/UX designs."
        else:
            return f"{self.name} has general employee responsibilities."