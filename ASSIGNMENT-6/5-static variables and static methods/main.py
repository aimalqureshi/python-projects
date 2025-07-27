class MathUtils:
    """A utility class for mathematical operations."""

    @staticmethod
    def add(a: float, b: float) -> float:
        """
        Static method to add two numbers.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The sum of a and b.
        """
        return a + b


def main() -> None:
    """Main function to demonstrate the static method usage."""
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Calling the static method without creating an object
        result = MathUtils.add(num1, num2)

        print(f"\nThe sum of {num1} and {num2} is: {result:.2f}")
    except ValueError:
        print("\nInvalid input! Please enter numeric values only.")


if __name__ == "__main__":
    main()

# This code defines a utility class with a static method for addition and demonstrates its usage in the main function.