class Student:
    """A class to represent a Student."""

    def __init__(self, name: str, marks: float) -> None:
        """
        Initialize the student's name and marks.

        Args:
            name (str): The name of the student.
            marks (float): The marks obtained by the student.
        """
        self.name = name.strip().title()
        self.marks = marks

    def display(self) -> None:
        """Display the student's details."""
        print("\n========== Student Details ==========")
        print(f"Name  : {self.name}")
        print(f"Marks : {self.marks:.2f}")
        print("======================================\n")


def main():
    """Main function to create and display a student object."""
    # Fixed student name as 'Tehreem'
    name = "Tehreem"
    
    while True:
        try:
            marks = float(input(f"Enter marks for student {name}: "))
            break
        except ValueError:
            print("Invalid input! Please enter numeric marks.")

    # Creating a Student object
    student = Student(name, marks)
    
    # Displaying student details
    student.display()


if __name__ == "__main__":
    main()