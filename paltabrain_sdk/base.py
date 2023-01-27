from abc import ABC, abstractmethod
from collections import defaultdict
from enum import IntEnum


class BaseEnum(IntEnum):
    pass


class BaseContext(ABC):
    def __init__(self):
        self._context = defaultdict(dict)

    @abstractmethod
    def serialize_context(self) -> bytes:
        pass

    def asdict(self):
        return self._context


class BaseEvent(ABC):
    event_type_id = 0

    def __init__(self):
        self._header = defaultdict(dict)
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


class BaseSentinel:
    def __bool__(self):
        return False

    @classmethod
    def filter(cls, params: dict):
        return {k: v for k, v in params.items() if not isinstance(v, cls)}
