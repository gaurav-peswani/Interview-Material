from typing import Dict, List

from dto.borrow_record import BorrowRecord
from dto.book import Book
from enums.borrow_status import BorrowStatus

class Member:

    def __init__(self, id: str, name: str, contact: str) -> None:
        self.id: str = id
        self.name: str = name
        self.contact: str = contact

        self.borrow_records: Dict[str, BorrowRecord] = {}

    def add_borrow_record(self, borrow_record: BorrowRecord) -> None:
        self.borrow_records[borrow_record.id] = borrow_record

    def update_borrow_record(self, borrow_record: BorrowRecord) -> None:
        self.borrow_records[borrow_record.id] = borrow_record

    def get_borrow_records(self) -> List[BorrowRecord]:
        return list(self.borrow_records.values())

    def get_borrow_record_id(self, book: Book) -> str:
        for record_id, record in self.borrow_records.items():
            if record.status == BorrowStatus.BORROWED and record.book.title == book.title:
                return record_id
        return None

    def get_active_borrow_count(self) -> int:
        borrowed_count = 0
        for record in self.borrow_records.values():
            if record.status == BorrowStatus.BORROWED:
                borrowed_count += 1
        return borrowed_count