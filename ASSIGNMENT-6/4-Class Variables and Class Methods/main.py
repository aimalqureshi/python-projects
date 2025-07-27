class Bank:
    """A class to represent a Bank with a shared bank name."""

    # Class variable
    bank_name = "Default Bank"

    def __init__(self, account_holder: str) -> None:
        """
        Initialize the Bank object with an account holder's name.

        Args:
            account_holder (str): The name of the account holder.
        """
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name: str) -> None:
        """
        Class method to change the bank's name.

        Args:
            name (str): The new name for the bank.
        """
        cls.bank_name = name.strip().title()

    def display_details(self) -> None:
        """Display the account holder's details along with the bank name."""
        print(f"Account Holder: {self.account_holder}")
        print(f"Bank Name     : {self.bank_name}")
        print("-" * 30)


def main() -> None:
    """Main function to demonstrate class variable and dynamic name change."""
    # Creating Bank instances
    customer1 = Bank("Tehreem")
    customer2 = Bank("Ayesha")

    print("\n--- Before Changing Bank Name ---")
    customer1.display_details()
    customer2.display_details()

    # Asking user to enter a new bank name
    new_bank_name = input("\nEnter a new Bank Name: ")
    Bank.change_bank_name(new_bank_name)

    print("\n--- After Changing Bank Name ---")
    customer1.display_details()
    customer2.display_details()


if __name__ == "__main__":
    main()

# This code defines a Bank class with a class variable for the bank name.