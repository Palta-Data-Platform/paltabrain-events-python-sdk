from datetime import datetime, timezone
from decimal import Decimal
from enum import IntEnum
from google.protobuf.message import Message
from random import getrandbits
from time import time_ns, monotonic_ns
from uuid import UUID


init_time_ns = time_ns()
init_monotonic_ns = monotonic_ns()


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
    # Transformation for Protobuf and Event Schema

    if isinstance(v, Decimal):
        # Decimal is serialized as string to keep precision and preserve maximum compatibility across languages
        return str(v)

    if isinstance(v, IntEnum):
        # Enum is serialized as int value
        return v.value

    if isinstance(v, datetime):
        # Timestamp is serialized as number of milliseconds since epoch
        return int(v.replace(tzinfo=timezone.utc).timestamp() * 1000)

    return v


def build_amplitude_dict(properties: dict):
    result = {}

    for k, v in properties.items():
        if v in (None, {}, []):
            # Always skip NULL values, empty dict and empty list
            continue
        elif isinstance(v, dict):
            # Map field
            result[k] = {ki: transform_amplitude_val(vi) for ki, vi in v.items()}
        elif isinstance(v, list):
            # Repeated field
            result[k] = [transform_amplitude_val(vi) for vi in v]
        else:
            result[k] = transform_amplitude_val(v)

    return result


def transform_amplitude_val(v):
    # Transformation for Amplitude

    if isinstance(v, Decimal):
        # Decimal is serialized as string to keep precision
        return str(v)

    if isinstance(v, IntEnum):
        # Enum is serialized as string label
        return v.name

    if isinstance(v, datetime):
        # Timestamp is serialised as ISO format for databases "YYYY-MM-DD HH:mm:ss.fff"
        return v.replace(tzinfo=timezone.utc).isoformat(sep=' ', timespec='milliseconds')

    return v


def monotonic_time_ms():
    return (init_time_ns + monotonic_ns() - init_monotonic_ns) // 1_000_000


def uuid_v7():
    """
    UUIDv7 description: https://datatracker.ietf.org/doc/html/draft-peabody-dispatch-new-uuid-format-03#section-5.2
    UUIDv7 example: https://datatracker.ietf.org/doc/html/draft-peabody-dispatch-new-uuid-format-03#appendix-B.2
    """
    time_ms = monotonic_time_ms()

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
