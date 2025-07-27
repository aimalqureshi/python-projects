class Counter:
    """A class to track the number of objects created."""
    
    # Class variable to keep track of the number of objects created
    object_count = 0
    
    def __init__(self) -> None:
        """
        Constructor to increment the object count every time a new instance is created.

        This method automatically increments the class variable `object_count`
        whenever a new instance of the class is initialized.
        """
        Counter.object_count += 1

    @classmethod
    def display_count(cls) -> None:
        """
        Class method to display the current number of objects created.

        This method can be called on the class itself to get the current count
        of how many instances of the class have been created.
        """
        print(f"Total number of objects created: {cls.object_count}")


def main() -> None:
    """Main function to demonstrate the object creation and object count tracking."""
    # Creating multiple Counter objects
    obj1 = Counter()
    obj2 = Counter()
    obj3 = Counter()
    
    # Displaying the total number of objects created
    Counter.display_count()


if __name__ == "__main__":
    main()

# The code defines a class `Counter` that keeps track of how many instances of itself have been created.