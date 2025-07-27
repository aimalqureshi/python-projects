class Dog:
    def __init__(self, name: str, breed: str):
        self.name = name
        self.breed = breed
        print(f"[Dog] Initialized with name: {self.name}, breed: {self.breed}")

    def bark(self) -> None:
        """Print a barking message including the dog's name."""
        print(f"{self.name} says: Woof! Woof!")

# Example usage
if __name__ == "__main__":
    dog = Dog("Buddy", "Golden Retriever")
    dog.bark()
    # Output: Buddy says: Woof! Woof!
    