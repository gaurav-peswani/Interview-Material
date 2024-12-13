from typing import List

from entities.entity import Entity

class TrackedEntity:

    def __init__(self, id: int) -> None:
        self._id = id
        self._hierarchy: List[Entity] = []

    @property
    def hierarchy(self):
        return self._hierarchy

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    def add_to_hierarchy(self, entity: Entity) -> None:
        print(f"Added entity with id: {entity.id}, tag: {entity.tag} into tracked entity heirarchy {self._id}.")
        self._hierarchy.append(entity)

    def remove_from_hierarchy(self, entity_id: int) -> None:
        entity_index = None
        for index, entity in enumerate(self._hierarchy):
            if entity.id == entity_id:
                entity_index = index
        if entity_index is not None:
            self._hierarchy.pop(entity_index)
        else:
            raise IndexError(f"Entity with id {entity_id} is not present in the heirarchy.")



