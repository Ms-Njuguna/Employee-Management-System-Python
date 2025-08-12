class Employee():
    def __init__(self, name, employee_id, employee_email, role, salary):
        self.name = name
        self.employee_id = employee_id
        self.employee_email = employee_email
        self.role = role
        self.salary = salary

    def get_details(self):
        return (f"Employee name: {self.name}\n"
                f"Employee ID: {self.employee_id}\n"
                f"Employee Email: {self.employee_email}\n"
                f"Role: {self.role}\n")
    
    def responsibilities(self):
        if self.role.lower() == "manager":
            return f"{self.name} is responsible for supervising the team.\n"
        elif self.role.lower() == "developer":
            return f"{self.name} is responsible for writing and reviewing code.\n"
        elif self.role.lower() == "designer":
            return f"{self.name} is responsible for creating UI/UX designs.\n"
        else:
            return f"{self.name} has general employee responsibilities.\n"
        
    def monthly_salary(self):
        if self.role.lower() == "manager":
            base_salary = 150000
            bonus = base_salary * 0.4
            monthly_income = base_salary + bonus
            return f"Base Salary: ${base_salary}\nBonus: ${bonus}\nMonthly Income: ${monthly_income}"
        elif self.role.lower() == "developer":
            base_salary = 100000
            bonus = base_salary * 0.3
            monthly_income = base_salary + bonus
            return f"Base Salary: ${base_salary}\nBonus: ${bonus}\nMonthly Income: ${monthly_income}"
        elif self.role.lower() == "designer":
            base_salary = 50000
            bonus = base_salary * 0.2
            monthly_income = base_salary + bonus
            return f"Base Salary: ${base_salary}\nBonus: ${bonus}\nMonthly Income: ${monthly_income}"
        else:
            base_salary = 25000
            bonus = base_salary * 0.1
            monthly_income = base_salary + bonus
            return f"Base Salary: ${base_salary}\nBonus: ${bonus}\nMonthly Income: ${monthly_income}"