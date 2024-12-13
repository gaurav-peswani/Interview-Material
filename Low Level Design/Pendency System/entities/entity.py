class Entity:

    def __init__(self, id: int, tag: str) -> None:
        self._id = id
        self._tag = tag

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def tag(self):
        return self._tag

    @tag.setter
    def tag(self, value):
        self._tag = value