from typing import Dict, List

from entities.tracked_entity import TrackedEntity
from entities.entity import Entity

class Database:

    _instance = None

    def __new__(cls, *args, **kwargs) -> None:
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance.entities: Dict[int, Entity] = {}
            cls._instance.tracked_entities: Dict[int, TrackedEntity] = {}
        return cls._instance

    @staticmethod
    def get_instance() -> 'Database':
        if Database._instance is None:
            Database()
        return Database._instance

    def get_entity(self, entity_id: int) -> Entity:
        if entity_id not in self.entities:
            raise KeyError(f"Entity with id {entity_id} does not exist.")
        return self.entities[entity_id]

    def add_entity(self, entity: Entity) -> None:
        # if entity.id not in self.entities:
            # raise ValueError(f"Tracked Entity with id {entity.id} already exists.")
        self.entities[entity.id] = entity

    def remove_entity(self, entity_id: int) -> None:
        if entity_id not in self.entities:
            raise KeyError(f"Entity with id {entity_id} does not exist.")
        del self.entities[entity_id]

    def get_tracked_entity(self, tracked_entity_id: int) -> TrackedEntity:
        if tracked_entity_id not in self.entities:
            raise KeyError(f"Tracked Entity with id {tracked_entity_id} does not exist.")
        return self.tracked_entities[tracked_entity_id]

    def add_tracked_entity(self, tracked_entity: TrackedEntity) -> None:
        if tracked_entity.id in self.tracked_entities:
            raise ValueError(f"Tracked Entity with id {tracked_entity.id} already exists.")
        self.tracked_entities[tracked_entity.id] = tracked_entity

    def remove_tracked_entity(self, tracked_entity_id: int) -> None:
        if tracked_entity_id not in self.tracked_entities:
            raise KeyError(f"Tracked Entity with id {tracked_entity_id} does not exist.")
        del self.tracked_entities[tracked_entity_id]

    def get_all_tracked_entities(self) -> List[TrackedEntity]:
        return list(self.tracked_entities.values())
