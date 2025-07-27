class Car:
    """A class to represent a Car."""

    def __init__(self, brand: str) -> None:
        """
        Initialize the Car with a brand name.

        Args:
            brand (str): The brand of the car.
        """
        self.brand = brand  # Public variable

    def start(self) -> None:
        """
        Public method to start the car.

        Prints a message indicating that the car has started.
        """
        print(f"The {self.brand} car has started successfully.")


def main() -> None:
    """Main function to demonstrate accessing public variables and methods."""
    # Taking user input for car brand
    brand_name = input("Enter the brand of the car: ").strip().title()

    # Creating a Car object
    my_car = Car(brand_name)

    # Accessing the public variable
    print(f"\nCar Brand: {my_car.brand}")

    # Calling the public method
    my_car.start()


if __name__ == "__main__":
    main()

# This code demonstrates the use of public variables and methods in a class.