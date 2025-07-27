class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self._price = price

    @property
    def price(self):
        """Getter for the price."""
        return self._price

    @price.setter
    def price(self, new_price: float):
        """Setter for the price with validation."""
        if new_price < 0:
            print("Price cannot be negative!")
        else:
            self._price = new_price

    @price.deleter
    def price(self):
        """Deleter for the price."""
        print(f"Deleting the price of {self.name}")
        del self._price

# Example usage
if __name__ == "__main__":
    product = Product("Laptop", 1000)
    
    # Getting the price
    print(f"Initial price: ${product.price}")
    
    # Setting the price
    product.price = 1200
    print(f"Updated price: ${product.price}")
    
    # Trying to set a negative price (validation)
    product.price = -500  # This should print a warning
    
    # Deleting the price
    del product.price
    # Trying to access the price after deletion (will raise an AttributeError)
    try:
        print(product.price)
    except AttributeError:
        print("Price has been deleted.")
        