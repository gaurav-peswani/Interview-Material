from os import name


class User:

    def __init__(self, id: str, name: str, phone: str, address: str) -> None:
        self.id = id
        self.name = name
        self.phone = phone
        self.address = address