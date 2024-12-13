from dto.book import Book
from enums.borrow_status import BorrowStatus

class BorrowRecord:

    def __init__(self, id: str, book: Book, member, from_date: str, to_date: str) -> None:
        self.id: str = id
        self.book: Book = book
        self.member = member
        self.from_date: str = from_date
        self.to_date: str = to_date
        self.status = BorrowStatus.BORROWED

    def set_status(self, status: BorrowStatus) -> None:
        self.status = status