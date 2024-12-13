from service.library_management_system import LibraryManagementSystem
from uuid import uuid4

from dto.book import Book
from dto.member import Member

class Demo:

    @staticmethod
    def run() -> None:
        system = LibraryManagementSystem.get_instance()

        book1 = Book("Mathematics for Class XII", "RD Sharma", "0000-1234", "Penguin", 2014)
        book2 = Book("English for Class X", "AK Singh", "0000-4234", "US Publication", 2023)
        book3 = Book("Science for Class XII", "Reena Saxena", "0000-1214", "CBSE Extras", 2011)

        member1 = Member(str(uuid4()), "Gaurav", "9953903405")
        member2 = Member(str(uuid4()), "Saurav", "9953902205")

        system.add_book(book1, 2)
        system.add_book(book2, 1)
        system.add_book(book3, 1)

        system.add_member(member1)
        system.add_member(member2)

        # List all books
        print("\nCase I: List all books")
        system.get_books()

        # Search a book
        print("\nCase II: Search a book")
        system.search_books(title="XII")

        # Borrow Success
        print("\nCase III: Borrow Successful")
        system.borrow_book(book1, member1, "07-12-2024", "08-12-2024")
        system.get_member_records(member1)

        # Borrow exceeds capacity
        print("\nCase IV: Borrow Fails")
        system.borrow_book(book2, member1, "07-12-2024", "08-12-2024")
        # system.get_member_records(member1)

        # Returning a book that was not borrowed - Exception
        print("\nCase V: Return Fails")
        system.return_book(book2, member1)
        # system.get_member_records(member1)

        # Return Success
        print("\nCase VI: Return Successful")
        system.return_book(book1, member1)
        system.get_member_records(member1)

if __name__ == "__main__":
    Demo.run()