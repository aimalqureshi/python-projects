class Logger:
    def __init__(self):
        # Constructor: called when an object is created
        print("Logger object created.")

    def __del__(self):
        # Destructor: called when an object is destroyed
        print("Logger object destroyed.")

# Example usage
if __name__ == "__main__":
    log = Logger()  # Creates a Logger object
    print("Working with the logger...")
    # When the script ends or 'log' is deleted, __del__() is called automatically
    del log  # Explicitly delete the object to trigger __del__()
    print("Logger object deleted.")

    # Note: In Python, __del__() is not guaranteed to be called immediately when the object goes out of scope.