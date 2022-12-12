from abc import ABC, abstractmethod
from enum import IntEnum


class BaseEnum(IntEnum):
    pass


class BaseContext(ABC):
    def __init__(self):
        self._context = {}

    @abstractmethod
    def serialize_context(self) -> bytes:
        pass

    def asdict(self):
        return self._context


class BaseEvent(ABC):
    event_type_id = 0

    def __init__(self):
        self._header = {}
        self._payload = {}

    @abstractmethod
    def serialize_header(self) -> bytes:
        pass

    @abstractmethod
    def serialize_payload(self) -> bytes:
        pass

    def asdict(self):
        return {
            "header": self._header,
            "payload": self._payload,
        }
