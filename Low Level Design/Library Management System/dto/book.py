class Book:

    def __init__(self, title: str, author: str, isbn: str, publication: str, year: int) -> None:
        self.title: str = title
        self.author: str = author
        self.isbn: str = isbn
        self.publication: str = publication
        self.year: int = year
