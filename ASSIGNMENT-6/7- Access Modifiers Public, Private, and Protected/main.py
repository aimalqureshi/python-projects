class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # Public attribute
        self._salary = salary      # Protected attribute (single underscore by convention)
        self.__ssn = ssn           # Private attribute (double underscore triggers name mangling)

# Example usage
if __name__ == "__main__":
    employee = Employee("Tehreem", 75000, "123-45-6789")

    # Accessing public attribute
    print(f"Employee Name (Public): {employee.name}")

    # Accessing protected attribute
    print(f"Employee Salary (Protected): {employee._salary}")

    # Attempting to access private attribute directly (will raise an AttributeError)
    try:
        print(f"Employee SSN (Private): {employee.__ssn}")
    except AttributeError as error:
        print(f"Error accessing private attribute: {error}")

    # Accessing private attribute using name mangling
    print(f"Employee SSN (Private, via name mangling): {employee._Employee__ssn}")

    # Attempting to access protected attribute from outside the class (not recommended but possible)