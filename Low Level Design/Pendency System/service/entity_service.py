from database.database import Database

from entities.entity import Entity

class EntityService:

    _instance = None

    def __new__(cls, *args, **kwargs) -> None:
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._database: Database = Database.get_instance()
        return cls._instance

    @staticmethod
    def get_instance() -> 'EntityService':
        if EntityService._instance is None:
            EntityService()
        return EntityService._instance

    def get_entity(self, entity_id: int) -> Entity:
        return self._database.get_entity(entity_id)

    def add_entity(self, entity: Entity) -> None:
        self._database.add_entity(entity)

    def remove_entity(self, entity_id: int) -> None:
        self._database.remove_entity(entity_id)
