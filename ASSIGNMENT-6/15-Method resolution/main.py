class A:
    def show(self):
        """Method in class A."""
        print("A's show() method")

class B(A):
    def show(self):
        """Override show() in class B."""
        print("B's show() method")

class C(A):
    def show(self):
        """Override show() in class C."""
        print("C's show() method")

class D(B, C):
    """Class D inherits from B and C, demonstrating diamond inheritance."""
    pass

# Example usage
if __name__ == "__main__":
    obj = D()  # Create an instance of class D
    obj.show()  # Call the show() method, which will demonstrate MRO

    # Displaying the MRO for class D
    print("\nMethod Resolution Order (MRO) of class D:", D.__mro__)
    # This will show the order in which Python looks for methods in the inheritance hierarchy