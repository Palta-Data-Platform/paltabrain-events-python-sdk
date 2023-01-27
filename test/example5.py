from datetime import datetime, timedelta
from decimal import Decimal
from logging import getLogger, StreamHandler, DEBUG
from os import getenv

# Import SDK and pre-generated Python classes
from paltabrain_sdk import PaltabrainSdk
from _config import Context, EventSessionStart, EventEdgeCase, EnumResult


logger = getLogger('paltabrain_sdk')
logger.addHandler(StreamHandler())
logger.setLevel(DEBUG)


with PaltabrainSdk[Context](
    hostname=getenv('TEST_SDK_HOSTNAME'),
    api_key=getenv('TEST_SDK_API_KEY'),
    context=Context(),
) as sdk:

    sdk.context.set_application(
        app_id="com.pora",
        app_version="0.1.0",
        app_platform="iOS",
    )

    sdk.context.set_device(
        device_brand="Apple",
        device_model="iPhone 13",
        device_carrier="Orange ES"
    )

    sdk.context.set_identify(
        idfa="ace9be38-8265-4f95-a536-21938b4360b8",
        idfv="0ddc9ac6-6b82-4e90-9fac-6ba305e24c82",
    )

    sdk.context.set_os(
        os_name="iOS",
        os_version="15.3.1",
    )

    sdk.context.set_appsflyer(
        appsflyer_id="9e471207-58d3-43b9-88e5-12344d803650",
        appsflyer_media_source="Facebook Ads",
    )

    ##########
    # Send some valid events
    ##########

    sdk.track(EventSessionStart())

    sdk.track(
        EventEdgeCase(
            prop_boolean=False,
            prop_decimal_1=Decimal('-100.15'),
            prop_decimal_2=Decimal('-100'),
            prop_enum=EnumResult.RESULT_SUCCESS,
            prop_integer=-100,
            prop_string="abc",
            prop_timestamp=datetime.utcnow(),
            prop_boolean_array=[False, True],
            prop_decimal_array=[Decimal('100.25'), Decimal('99.15')],
            prop_enum_array=[EnumResult.RESULT_ERROR, EnumResult.RESULT_SKIP, EnumResult.RESULT_SUCCESS],
            prop_integer_array=[10, 15, 20],
            prop_string_array=["abc", "cde", "ghj"],
            prop_timestamp_array=[datetime.utcnow(), datetime.utcnow() + timedelta(seconds=10)]
        )
    )

    ##########
    # Send some invalid events
    ##########

    sdk.track(
        EventEdgeCase(
            prop_boolean=False,
            prop_decimal_1=Decimal('1111111111111111111111111'),  # 25 precision vs allowed 25
            prop_decimal_2=Decimal('-100.15'),                    # 2 scale vs allowed 0
            prop_enum=EnumResult.RESULT_SUCCESS,
            prop_integer=-100,
            prop_string="a" * 10000,                              # 10,000 chars vs allowed 8,192
            prop_timestamp=-72135596725000,                       # below min value
            prop_boolean_array=[False, True],
            prop_decimal_array=[Decimal('100.25'), Decimal('99.15')],
            prop_enum_array=[EnumResult.RESULT_ERROR, EnumResult.RESULT_SKIP, EnumResult.RESULT_SUCCESS],
            prop_integer_array=[10, 15, 20],
            prop_string_array=["abc", "cde", "g" * 10000],        # Only one value is broken
        )
    )
