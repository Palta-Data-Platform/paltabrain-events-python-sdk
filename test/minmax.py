from datetime import datetime, timedelta
from decimal import Decimal
from logging import getLogger, StreamHandler, DEBUG
from os import getenv

# Import SDK and pre-generated Python classes
from paltabrain_sdk import PaltabrainSdk
from _config import Context, EventEdgeCase, EnumResult


logger = getLogger('paltabrain_sdk')
logger.addHandler(StreamHandler())
logger.setLevel(DEBUG)


with PaltabrainSdk[Context](
        hostname=getenv('TEST_SDK_HOSTNAME'),
        api_key=getenv('TEST_SDK_API_KEY'),
        context=Context(),
) as sdk:

    # All minimums
    sdk.track(
        EventEdgeCase(
            prop_boolean=False,
            prop_decimal_3=Decimal(f"-{'9' * 38}"),
            prop_decimal_4=Decimal(f"-0.{'9' * 37}"),
            prop_enum=EnumResult.UNKNOWN,
            prop_integer=-9_223_372_036_854_775_808,
            prop_string="",
            prop_timestamp=datetime.min,
        )
    )

    # All maximums
    sdk.track(
        EventEdgeCase(
            prop_boolean=True,
            prop_decimal_3=Decimal(f"{'9' * 38}"),
            prop_decimal_4=Decimal(f"0.{'9' * 37}"),
            prop_enum=EnumResult.RESULT_ERROR,
            prop_integer=9_223_372_036_854_775_807,
            prop_string="あ" * 65536,
            prop_timestamp=datetime.max - timedelta(days=1),
        )
    )
