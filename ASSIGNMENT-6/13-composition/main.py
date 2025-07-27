class Engine:
    def __init__(self, horsepower: int):
        self.horsepower = horsepower
        print(f"[Engine] Created with {self.horsepower} horsepower.")

    def start(self) -> str:
        """Simulate starting the engine."""
        return "Engine started!"

class Car:
    def __init__(self, make: str, model: str, engine: Engine):
        self.make = make
        self.model = model
        self.engine = engine  # Composition: Car "has" an Engine
        print(f"[Car] Created {self.make} {self.model}.")

    def start_engine(self) -> str:
        """Access Engine's method via Car."""
        return self.engine.start()

# Example usage
if __name__ == "__main__":
    engine = Engine(200)  # Create an Engine object
    car = Car("Toyota", "Camry", engine)  # Pass Engine to Car
    print(car.start_engine())  # Accessing Engine's method via Car