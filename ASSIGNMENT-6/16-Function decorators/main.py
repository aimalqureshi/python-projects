def log_function_call(func):
    """Decorator that logs when a function is called."""
    def wrapper(*args, **kwargs):
        print("Function is being called")
        return func(*args, **kwargs)
    return wrapper

@log_function_call
def say_hello():
    """Simple function that prints 'Hello!'."""
    print("Hello!")

# Example usage
if __name__ == "__main__":
    say_hello()  # Calling the decorated function
    # This will print "Function is being called" followed by "Hello!"