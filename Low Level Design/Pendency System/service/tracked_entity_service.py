from typing import List

from database.database import Database

from entities.entity import Entity
from entities.tracked_entity import TrackedEntity


class TrackedEntityService:
    _instance = None

    def __new__(cls, *args, **kwargs) -> None:
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._database: Database = Database.get_instance()
        return cls._instance

    @staticmethod
    def get_instance() -> 'TrackedEntityService':
        if TrackedEntityService._instance is None:
            TrackedEntityService()
        return TrackedEntityService._instance

    def get_tracked_entity(self, tracked_entity_id: int) -> TrackedEntity:
        return self._database.get_tracked_entity(tracked_entity_id)

    def add_tracked_entity(self, tracked_entity: TrackedEntity) -> None:
        self._database.add_tracked_entity(tracked_entity)

    def remove_tracked_entity(self, tracked_entity_id: int) -> None:
        self._database.remove_tracked_entity(tracked_entity_id)

    def get_tracked_entities_starting_with(self, tags: List[str]) -> List[TrackedEntity]:
        prefix_entities = []
        all_tracked_entities = self._database.get_all_tracked_entities()

        for tracked_entity in all_tracked_entities:
            heirarchy = tracked_entity.hierarchy
            if self.__is_matching_tags(tags, heirarchy):
                prefix_entities.append(heirarchy)

        return prefix_entities

    def __is_matching_tags(self, tags: List[str], heirarchy: List[Entity]) -> bool:
        tag_index = 0
        for entity in heirarchy:
            if tag_index < len(tags) and entity.tag == tags[tag_index]:
                tag_index += 1
            else:
                break
        return tag_index == len(tags)