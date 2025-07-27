from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        """Calculate and return the area of the shape."""
        pass

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
        print(f"[Rectangle] Initialized with width={self.width} and height={self.height}")

    def area(self) -> float:
        """Calculate the area of the rectangle."""
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius
        print(f"[Circle] Initialized with radius={self.radius}")

    def area(self) -> float:
        """Calculate the area of the circle."""
        return math.pi * self.radius ** 2

# Example usage
if __name__ == "__main__":
    rectangle = Rectangle(5.0, 3.0)
    circle = Circle(4.0)

    print(f"\nArea of Rectangle: {rectangle.area():.2f} square units")
    print(f"Area of Circle: {circle.area():.2f} square units")