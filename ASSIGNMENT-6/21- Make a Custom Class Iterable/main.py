class Countdown:
    def __init__(self, start: int):
        """Initialize with a starting number."""
        self.start = start
        self.current = start

    def __iter__(self):
        """Return the iterator object itself."""
        return self

    def __next__(self):
        """Return the next value in the countdown."""
        if self.current < 0:
            raise StopIteration  # Stop the iteration once we reach 0
        value = self.current
        self.current -= 1
        return value

# Example usage
if __name__ == "__main__":
    countdown = Countdown(5)  # Starting from 5
    
    for number in countdown:
        print(number)
    