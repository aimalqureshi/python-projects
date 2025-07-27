class InvalidAgeError(Exception):
    """Custom exception for invalid age."""
    def __init__(self, message="Age must be 18 or older."):
        self.message = message
        super().__init__(self.message)

def check_age(age: int):
    """Function to check if the age is 18 or older."""
    if age < 18:
        raise InvalidAgeError(f"Provided age {age} is less than 18.")
    return f"Age {age} is valid."

# Example usage
if __name__ == "__main__":
    try:
        age = int(input("Enter your age: "))
        result = check_age(age)
        print(result)
    except InvalidAgeError as e:
        print(f"Error: {e}")
    except ValueError:
        print("Invalid input! Please enter a valid number.")