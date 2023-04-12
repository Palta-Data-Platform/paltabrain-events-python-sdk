# Changelog

## [0.7.1] - 2023-04-12

- Update messages generated from `sdk.proto` with `BatchTelemetry`.
- Add explicit error message if SDK failed to download config ZIP.

## [0.7.0] - 2023-03-28

- Implemented entry-point automating download and extraction of Python module.
- Changed SDK_NAME to `PALTABRAIN_PYTHON`, similar naming to iOS.
- Use monotonic timer for all time-related functions in SDK.
- Serialization errors will no longer throw exceptions. Errors will be reported as warnings in `paltabrain_sdk` logger instead. It should help to prevent possible crashes of production scripts.
- Replace `.last_exception` with separate debug properties `.last_request_error` and `.last_serialization_error`.

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
