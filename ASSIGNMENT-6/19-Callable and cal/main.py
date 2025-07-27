class Multiplier:
    def __init__(self, factor: int):
        """Initialize with a factor to multiply."""
        self.factor = factor

    def __call__(self, number: int):
        """Allow the object to be called like a function to multiply."""
        return number * self.factor

# Example usage
if __name__ == "__main__":
    # Creating a Multiplier object with a factor of 5
    multiplier = Multiplier(5)
    
    # Test with callable()
    print(f"Is multiplier callable? {callable(multiplier)}")
    
    # Using the object like a function
    result = multiplier(10)  # Should multiply 10 by the factor 5
    print(f"Result of calling multiplier(10): {result}")
    # Test with isinstance()
    print(f"Is multiplier an instance of Multiplier? {isinstance(multiplier, Multiplier)}")
    # Test with type()
    print(f"Type of multiplier: {type(multiplier)}")
    # Test with dir()
    print(f"Attributes and methods of multiplier: {dir(multiplier)}")
    # Test with help()
    print("Help on Multiplier object:")
    help(multiplier)
    