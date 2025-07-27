def add_greeting(cls):
    """Class decorator that adds a greet() method to a class."""
    def greet(self):
        return "Hello from Decorator!"
    
    # Add the greet method to the class
    cls.greet = greet
    return cls

@add_greeting
class Person:
    def __init__(self, name: str):
        self.name = name

# Example usage
if __name__ == "__main__":
    person = Person("Tehreem")
    print(person.greet())  # Calling the greet() method added by the decorator