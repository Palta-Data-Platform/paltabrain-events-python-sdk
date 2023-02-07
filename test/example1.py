from datetime import datetime, timedelta
from decimal import Decimal
from logging import getLogger, StreamHandler, DEBUG
from os import getenv

# Import SDK and pre-generated Python classes
from paltabrain_sdk import PaltabrainSdk
from _config import Context, EventSessionStart, EventPageOpen, EventEdgeCase, EventPermissionsRequest, EnumResult


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
    # Send some events
    ##########

    sdk.track(EventSessionStart())

    sdk.track(
        EventPageOpen(
            page_id='abc'
        ).set_parent(
            parent_elements=['main_screen', 'first_block']
        )
    )

    ##########
    # Change context
    ##########

    sdk.context.set_user(
        user_id="123",
    )

    ##########
    # Send more events
    ##########

    sdk.track(
        EventPermissionsRequest(
            is_granted=True,
            type="CAMERA"
        )
    )

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
            prop_timestamp_array=[datetime.utcnow(), datetime.utcnow() + timedelta(seconds=10)],
            prop_boolean_map={"foo": False, "bar": True},
            prop_decimal_map={"foo": Decimal('100.25'), "123": Decimal('99.15')},
            prop_enum_map={"foo": EnumResult.RESULT_ERROR, "bar": EnumResult.RESULT_SUCCESS},
            prop_integer_map={"foo": 10, "bar": -20},
            prop_string_map={"foo": "abc", "bar": "cde"},
            prop_timestamp_map={"foo": datetime.utcnow(), "bar": datetime.utcnow() + timedelta(seconds=10)},
        ).set_edge_case(
            prop_boolean=False,
            prop_decimal_1=Decimal('100500'),
            prop_decimal_2=Decimal('0.15'),
            prop_enum=EnumResult.RESULT_SKIP,
            prop_integer=5550,
            prop_string="cde",
            prop_timestamp=datetime.utcnow(),
            prop_integer_array=[5, 6, 7],
            prop_integer_map={"yes": 1, "no": 2}
        )
    )
