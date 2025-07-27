class Employee:
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role
        print(f"[Employee] Created {self.name}, Role: {self.role}")

    def get_details(self) -> str:
        """Return employee details."""
        return f"Employee: {self.name}, Role: {self.role}"

class Department:
    def __init__(self, department_name: str):
        self.department_name = department_name
        self.employees = []  # List to store Employee objects
        print(f"[Department] Created department: {self.department_name}")

    def add_employee(self, employee: Employee) -> None:
        """Add an Employee to the department."""
        self.employees.append(employee)
        print(f"[Department] Added {employee.name} to {self.department_name} department.")

    def show_employees(self) -> None:
        """Display all employees in the department."""
        print(f"\nEmployees in {self.department_name} Department:")
        for emp in self.employees:
            print(emp.get_details())

# Example usage
if __name__ == "__main__":
    emp1 = Employee("Tehreem", "Software Engineer")
    emp2 = Employee("Jaweriya", "Data Scientist")

    department = Department("Engineering")
    department.add_employee(emp1)
    department.add_employee(emp2)

    department.show_employees()