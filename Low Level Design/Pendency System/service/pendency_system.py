from typing import List

from entities.tracked_entity import TrackedEntity
from entities.entity import Entity

from service.entity_service import EntityService
from service.tracked_entity_service import TrackedEntityService

class PendencySystem:

    _instance = None

    def __new__(cls, *args, **kwargs) -> None:
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance.entity_service = EntityService.get_instance()
            cls._instance.tracked_entity_service = TrackedEntityService.get_instance()
        return cls._instance

    @staticmethod
    def get_instance() -> 'PendencySystem':
        if PendencySystem._instance is None:
            PendencySystem()
        return PendencySystem._instance

    def start_tracking(self, tracked_entity: TrackedEntity) -> None:
        self.tracked_entity_service.add_tracked_entity(tracked_entity)
        for entity in tracked_entity.hierarchy:
            self.entity_service.add_entity(entity)
        print(f"Entity {tracked_entity.id} with entity tags: {[ent.tag for ent in tracked_entity.hierarchy]} "
              f"has been added to the DB for tracking.")

    def stop_tracking(self, tracking_entity_id: int) -> None:
        self.tracked_entity_service.remove_tracked_entity(tracking_entity_id)
        print(f"Entity {tracking_entity_id} has been removed from the DB and will no longer be tracked.")

    def get_counts(self, tags: List[str]) -> int:
        print(f"Input: getCounts({tags})")
        prefixed_entities = self.tracked_entity_service.get_tracked_entities_starting_with(tags)
        return len(prefixed_entities)
