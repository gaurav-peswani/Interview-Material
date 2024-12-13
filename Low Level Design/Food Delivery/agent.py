from location import Location

class Agent:

    def __init__(self, id: str, name: str, location: Location) -> None:
        self.id = id
        self.name = name
        self.location = location
        self.is_available = True

    def update_location(self, location: Location) -> None:
        self.location = location