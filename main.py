from roles.manager import Manager
from roles.developer import Developer
from roles.designer import Designer


general_manager = Manager("Susan", "NCLK1370", "susan@employee.nclk", "Manager")
senior_developer = Developer("John", "NCLK2901", "john@employee.nclk", "Developer")
lead_designer = Designer("Amani", "NCLK61037", "amani@employee.nclk", "Designer")


print(general_manager.manager_details())
print(general_manager.responsibilities())
print()
print(general_manager.monthly_salary())
print()
print("-" * 40)
print()

print(senior_developer.developer_details())
print(senior_developer.responsibilities())
print()
print(senior_developer.monthly_salary())
print()
print("-" * 40)
print()

print(lead_designer.designer_details())
print(lead_designer.responsibilities())
print()
print(lead_designer.monthly_salary())
print()
print("-" * 40)
print()