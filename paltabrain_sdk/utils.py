from datetime import datetime, timezone
from decimal import Decimal
from google.protobuf.message import Message
from random import getrandbits
from time import time_ns
from uuid import UUID


def set_proto(message: Message, properties: dict):
    for k, v in properties.items():
        if v is None:
            # Always skip NULL values
            continue
        elif isinstance(v, dict):
            # Map field
            for ki, vi in v.items():
                getattr(message, k)[ki] = transform_proto_val(vi)
        elif isinstance(v, list):
            # Repeated field
            for vi in v:
                getattr(message, k).append(transform_proto_val(vi))
        else:
            setattr(message, k, transform_proto_val(v))


def transform_proto_val(v):
    if isinstance(v, Decimal):
        # Decimal is serialized as string to keep precision and preserve maximum compatibility across languages
        return str(v)

    if isinstance(v, datetime):
        # Datetime is serialized as number of milliseconds since epoch
        return int(v.replace(tzinfo=timezone.utc).timestamp() * 1000)

    return v


def time_ms():
    return time_ns() // 1000000


def uuid_v7(time_ms: int):
    """
    UUIDv7 description: https://datatracker.ietf.org/doc/html/draft-peabody-dispatch-new-uuid-format-03#section-5.2
    UUIDv7 example: https://datatracker.ietf.org/doc/html/draft-peabody-dispatch-new-uuid-format-03#appendix-B.2
    """
    ver = 7
    variant = 2

    rand_a = getrandbits(12)
    rand_b = getrandbits(62)

    # Offsets:
    #
    #   unix_ts_ms = 128 - 48 = 80
    #   ver        =  80 -  4 = 76
    #   rand_a     =  76 - 12 = 64
    #   variant    =  64 -  2 = 62
    #   rand_b     =  62 - 62 = 0

    return str(UUID(int=(time_ms << 80) + (ver << 76) + (rand_a << 64) + (variant << 62) + rand_b))
