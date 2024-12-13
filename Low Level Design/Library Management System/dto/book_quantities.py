from dto.book import Book

class BookQuantity:

    def __init__(self, book: Book, quantity: int) -> None:
        self.book: Book = book
        self.quantity: int = quantity

    def increment_quantity(self):
        self.quantity += 1

    def decrement_quantity(self):
        if self.quantity == 0:
            raise Exception("Quantity cannot be reduced to less than 0.")
        self.quantity -= 1

    def is_available(self) -> bool:
        return self.quantity > 0