class User:

    def __init__(self, id: str, username: str, password: str) -> None:
        self._id = id
        self._username = username
        self._password = password

    @property
    def password(self):
        return self._password

    @property
    def id(self):
        return self._id

    @property
    def username(self):
        return self._username