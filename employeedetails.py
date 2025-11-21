class Employee:
    def __init__(self, name, employee_id, department, salary):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.salary = salary

    def display_details(self):
        print(f"Name: {self.name}, ID: {self.employee_id}, Department: {self.department}, Salary: {self.salary}")

    def update_salary(self, new_salary):
        self.salary = new_salary


def update_department_salary(employees, department_name, new_salary):
    for emp in employees:
        if emp.department == department_name:
            emp.update_salary(new_salary)


# Sample usage
employees = [
    Employee("Alice", 101, "HR", 50000),
    Employee("Bob", 102, "IT", 60000),
    Employee("Charlie", 103, "HR", 55000),
    Employee("David", 104, "IT", 65000),
]

print("Before salary update:")
for emp in employees:
    emp.display_details()

# Update salary for HR department
update_department_salary(employees, "HR", 70000)

print("\nAfter salary update:")
for emp in employees:
    emp.display_details()
