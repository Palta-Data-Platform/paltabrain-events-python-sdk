# PaltaBrain Events Python SDK

This SDK helps to organize events in batches and to send batches to PaltaBrain API endpoint.

## Getting started

1. Install package from GitHub:
   ```
   pip install --upgrade git+https://github.com/Palta-Data-Platform/paltabrain-events-python-sdk.git
   ```
2. Get `hostname` and `api_key` from PaltaBrain team.
3. Download pre-generated Python config module for your startup.
   ```
   paltabrain-sdk-download-config --hostname=<hostname> --api-key=<api_key> <path_to_module_dir>
   ```
   You may use ENV variables `PALTABRAIN_SDK_HOSTNAME` and `PALTABRAIN_SDK_API_KEY` to pass credentials in CI/CD instead of `--hostname` and `--api-key` options.
4. Import `paltabrain_sdk` module and config module in your code. Init SDK and start sending events.


## How to use SDK

1. Import classes:
   ```python
   from paltabrain_sdk import PaltabrainSdk
   from <config_module> import *
   ```

2. Initialize SDK instance using provided credentials and `Context` object from Python module:
   ```python
   with PaltabrainSdk[Context](
       hostname='<hostname>',
       api_key='<api_key>', 
       context=Context(),
   ) as sdk:
   ```

3. Set context properties, for example:
   ```python
   sdk.context.set_application(
       app_id='<app_id>',
       app_platform='<app_platform>',
       app_version='<app_version>',
   )

   sdk.context.set_os(
       os_name='<os_name>',
       os_version='<os_version>',
   )

   ...
   ```

4. Create & track event objects:
   ```python
   # Event without properties
   sdk.track(EventSessionStart())
   
   # Event with event properties
   sdk.track(
       EventPermissionsRequest(
           is_granted=True,
           type="CAMERA"
       )
   )
   
   # Event with event properties and header properties
   sdk.track(
       EventPageOpen(
           page_id='abc'
       ).set_parent(
           parent_elements=['main_screen', 'first_block']
       )
   )
   ...
   ```

5. When finished tracking, shutdown SDK by exiting context manager (recommended!) or by calling `.shutdown()` method explicitly. This step is mandatory to stop the background control thread.
   ```python
   sdk.shutdown()
   ```

## Examples

- Complete example: [example1.py](/test/example1.py)
- Python config module: [init.py](/test/_config/__init__.py)


## Options

| Option              | Example                                | Default  | Description                                                                                       |
|---------------------|----------------------------------------|----------|---------------------------------------------------------------------------------------------------|
| `hostname`          | `telemetry.mobilesdk.paltabrain.com`   | Required | Base hostname for API-calls. Each startup has its own dedicated hostname.                         |
| `api_key`           | `1237c694a824422a88e2a3c5a90510e3`     | Required | API-key for authentication.                                                                       |
| `context`           | `Context()`                            | Required | Context object from Python module.                                                                |
| `instance_id`       | `f1a1d6ae-0369-496a-8de9-2afcc964207b` | `None`   | Enforce specific Instance ID. If not set, generate UUIDv7 random value.                           |
| `session_id`        | `f1a1d6ae-0369-496a-8de9-2afcc964207b` | `None`   | Enforce Session ID. If not set, generate UUIDv7 random value if `start_session` is enabled.       |
| `start_session`     | `False`                                | `False`  | Start a new session automatically during SDK init.                                                |
| `flush_buffer_size` | `150`                                  | `100`    | Flush event buffer when the amount of events in queue reaches this limit.                         |
| `flush_interval_ms` | `10000`                                | `5000`   | Flush event buffer when the amount of time since the last flush exceeds interval in milliseconds. |
| `flush_max_retries` | `5`                                    | `5`      | Make this number of attempts to send event batch before SDK will give up and discard it.          |


## Properties

| Name                       | Description                                                                                                                                                             |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `context`                  | `Context` object passed during initialization of SDK. It can be accessed directly and altered via `set_` functions.                                                     |
| `instance_id`              | Instance ID passed of generated during initialization of SDK.                                                                                                           |
| `session_id`               | Session ID passed of generated during initialization of SDK.                                                                                                            |
| `batch_counters`           | Dictionary with counters of number of batches which were successfully sent (SUCCESS), discarded due to network issues (REJECT) or failed due to exceptions (EXCEPTION). |
| `last_request_error`       | If at least one batch request has failed, this property will hold last exception object. It might be useful for debugging.                                              |
| `last_serialization_error` | If at least one event serialization attempt has failed, this property will last exception object. It might be useful for debugging.                                     |

## Usage notes

- SDK uses `threading` and `ThreadPoolExecutor` internally. Please make sure to use Context Manager (`with` keyword) to prevent potential issues with exception handling and background threads.
- Events are serialized in the main thread when you call `.track()`. If something goes wrong during serialization of event, you'll see warning emitted in the main thread. Event will be discarded, and your code will not be interrupted.
- Events are combined into batches in the background thread and sent to API Gateway using `ThreadPoolExecutor`, 1 extra thread per request, up to 20 threads running in parallel.
- Retries are implemented using [HTTPAdapter and Retry policy](https://www.peterbe.com/plog/best-practice-with-retries-with-requests) with very small `backoff_factor` of `0.1`. If batch reaches maximum number of retries, it will be discarded. Currently, events can be lost due to network problems.
- SDK is thread-safe. Events can be tracked from multiple threads simultaneously. Internally `deque` object is used to store events.

## Incremental updates of Context and Header properties

Context is NOT persistent. It should be fully constructed on each initialization of SDK.

Context and Headers properties are updated incrementally with arguments you explicitly pass to setter function. To unset the property pass `None` value explicitly. If you do not mention property, it will not change.

Example:

```python
   sdk.context.set_user(
       user_id="123",
       country_code="GB",
       is_trial=True,
   )

   # Context is {"user_id": "123", "country_code": "GB", "is_trial": true}

   sdk.context.set_user(
       is_paying=True,
   )

   # Context is {"user_id": "123", "country_code": "GB", "is_trial": true, "is_paying": true}

   sdk.context.set_user(
      user_id=None,
      country_code=None,
      is_trial=False,
      is_paying=False,
   )

   # Context is {"is_trial": false, "is_paying": false}
```

## Data types mapping

| Logical type    | Protobuf type   | Python type     | Snowflake type     | Snowflake default |
|-----------------|-----------------|-----------------|--------------------|-------------------|
| `boolean`       | `bool`          | `bool`          | `BOOLEAN`          | `NULL`            |
| `decimal(x,y)`  | `string`        | `Decimal`       | `NUMBER(x,y)`      | `NULL`            |
| `enum`          | `sint64`        | `IntEnum`       | `VARCHAR(65536)`   | `NULL`            |
| `integer`       | `sint64`        | `int`           | `NUMBER(20,0)`     | `NULL`            |
| `string`        | `string`        | `str`           | `VARCHAR(65536)`   | `NULL`            |
| `timestamp`     | `sint64`        | `datetime`      | `TIMESTAMP_NTZ(3)` | `NULL`            |
| ---             | ---             | ---             | ---                | ---               |
| `array<T>`      | `repeated<T>`   | `List[<T>]`     | `ARRAY`            | `NULL`            |
| `map<T>`        | `map<String,T>` | `Dict[str,<T>]` | `OBJECT`           | `NULL`            |

- Native `float` type is not provided on purpose. Please use `decimal` with specific precision and scale instead to prevent inaccuracy and rounding errors.
- Native `date` type is not provided on purpose. Please use `timestamp` instead.
- `timestamp` values are converted to and stored in UTC timezone. Timezone information is not preserved.


## Debugging

You may enable debug logging by adding log handler for `paltabrain_sdk` logger:

```python
logger = getLogger('paltabrain_sdk')
logger.addHandler(StreamHandler())
logger.setLevel(DEBUG)
```

Logging provides information about success of failure to send each event batch.

It is also possible to verify the contents of Event and Context objects by calling `.asdict()` method before calling `.track()`.
