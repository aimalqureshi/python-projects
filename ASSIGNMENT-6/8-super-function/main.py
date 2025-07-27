class Person:
    def __init__(self, name: str):
        self.name = name
        print(f"[Person] Initialized with name: {self.name}")

class Teacher(Person):
    def __init__(self, name: str, subject: str):
        super().__init__(name)
        self.subject = subject
        print(f"[Teacher] Initialized with subject: {self.subject}")

    def display_info(self):
        print(f"Teacher Name: {self.name}")
        print(f"Subject: {self.subject}")

# Example usage
if __name__ == "__main__":
    teacher = Teacher("Tehreem", "Mathematics")
    print("\nDisplaying Teacher Information:")
    teacher.display_info()