from typing import Dict, List
from uuid import uuid4

from dto.book import Book
from dto.member import Member
from dto.borrow_record import BorrowRecord
from dto.catalog import Catalog
from enums.borrow_status import BorrowStatus

MAX_BORROW_COUNT_PER_MEMBER = 1

class LibraryManagementSystem:

    _instance = None

    def __new__(cls, *args, **kwargs) -> None:
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance.books: Dict[str, Book] = {}
            cls._instance.members: Dict[str, Member] = {}
            cls._instance.catalog: Catalog = Catalog()
            cls._instance.borrow_records: Dict[str, BorrowRecord] = {}
        return cls._instance

    @staticmethod
    def get_instance() -> 'LibraryManagementSystem':
        if LibraryManagementSystem._instance is None:
            LibraryManagementSystem()
        return LibraryManagementSystem._instance

    # Helper methods
    def __generate_uuid(self) -> str:
        return str(uuid4())

    def __is_borrow_allowed(self, member: Member) -> bool:
        return member.get_active_borrow_count() < MAX_BORROW_COUNT_PER_MEMBER

    # Book Methods
    def add_book(self, book: Book, quantity: int) -> None:
        self.catalog.add_book(book, quantity)

    def search_books(self, title: str=None, author: str=None, isbn: str=None, publication: str=None, year: int=None):
        books_available = self.catalog.search_books(title, author, isbn, publication, year)
        for book in books_available:
            print(f"{book.title} \t {book.author} \t {book.isbn} \t {book.publication} \t {book.year}")

    def get_books(self):
        books_available = self.catalog.get_all_books()
        for book in books_available:
            print(f"{book.title} \t {book.author} \t {book.isbn} \t {book.publication} \t {book.year}")

    def borrow_book(self, book: Book, member: Member, from_date: str, to_date: str) -> None:
        if not self.catalog.is_book_available(book):
            print(f"Book {book.title} is not available.")

        if not self.__is_borrow_allowed(member):
            print(f"Member {member.name} has exceeded the maximum borrowing count. "
                            f"Return some books in order to borrrow more.")
            return

        record_id = self.__generate_uuid()
        record = BorrowRecord(record_id, book, member, from_date, to_date)
        self.borrow_records[record_id] = record

        self.catalog.borrow_book(book)
        member.add_borrow_record(record)

        print(f"Member {member.name} has borrowed {book.title} from {from_date} to {to_date}.")

    def return_book(self, book: Book, member: Member) -> None:
        record_id = member.get_borrow_record_id(book)
        if record_id is None:
            print(f"Member {member.name} has not borrowed the book {book.title}")
            return

        record = self.borrow_records[record_id]

        record.set_status(BorrowStatus.RETURNED)
        self.catalog.return_book(book)

        self.borrow_records[record_id] = record
        member.update_borrow_record(record)

        print(f"Member {member.name} has returned the {book.title}.")


    # Member Methods
    def add_member(self, member: Member) -> None:
        self.members[member.id] = member

    def get_member_records(self, member: Member) -> List[BorrowRecord]:
        member_borrow_records = member.get_borrow_records()
        print(f"Borrow Record for {member.name}:")
        for br in member_borrow_records:
            print(f"{br.id} \t {br.book.title} \t {br.status} \t {br.from_date} \t {br.to_date}")
        return member_borrow_records

