# Changelog

## [0.6.0] - 2023-01-27

- Added `Generic` for `PaltabrainSdk` class. It accepts `Context` class, which helps to improve code auto-completion in IDE.
- Reworked code generation for Python. Implemented proper formatting for `description`, `is_deprecated`.
- Added sentinel `UNDEFINED` object to setters of Context and Header properties. Now these properties are updated incrementally instead of being fully replaced.
- Output of `serialise_context()` is now deterministic to avoid possible context comparison issues for payloads with MAP collections.
- Implemented `session_event_seq_num`. It is protected with `Lock` to handle potential multi-threading scenarios.
- `enum` logical type is now translated into `Enum` of specific type only (previously also included raw `int`).
- `timestamp` logical type is now translated into `datetime` only (previously also included raw `int` as number of milliseconds).

## [0.5.0] - 2022-12-12

- Prepared Python SDK package for public release. Add license, manifest and changelog.
- Implemented `map` collection type, in addition to existing `array`.
- Switched all instances of `int64` to `sint64`.
- Added explicit `optional` for SDK proto fields which can be skipped.
