class Book:
    total_books = 0  # Class variable shared among all instances

    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        Book.increment_book_count()
        print(f"[Book] Created '{self.title}' by {self.author}")

    @classmethod
    def increment_book_count(cls) -> None:
        """Increment the total number of books."""
        cls.total_books += 1
        print(f"[Book] Total books updated: {cls.total_books}")

# Example usage
if __name__ == "__main__":
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")

    print(f"\nFinal Total Books: {Book.total_books}")
    # Output: Final Total Books: 2