import abc

from enums.component_type import ComponentType
from abc import ABC

class BoardComponent(ABC):

    def __init__(self, type: ComponentType, source: int, destination: int) -> None:
        self._type = type
        self._source = source
        self._destination = destination

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value

    @property
    def destination(self):
        return self._destination

    @destination.setter
    def destination(self, value):
        self._destination = value

    @abc.abstractmethod
    def validate(self) -> None:
        pass


