from argparse import ArgumentParser
from io import BytesIO
from pathlib import Path
from requests import get
from os import getenv
from shutil import rmtree
from zipfile import ZipFile

from .constant import *
from .version import __version__


def download_config_entry_point():
    parser = ArgumentParser(
        prog="paltabrain-sdk-download-config",
        description="Download and extract config module for Paltabrain Python SDK"
    )

    parser.add_argument("module_path", help="Path to config module directory")

    parser.add_argument("--hostname", help="Hostname", default=getenv("PALTABRAIN_SDK_HOSTNAME"))
    parser.add_argument("--api-key", help="API Key", default=getenv("PALTABRAIN_SDK_API_KEY"))
    parser.add_argument("--overwrite", help="Overwrite existing config module", default=False, action="store_true")

    args = parser.parse_args()

    # Download ZIP into memory
    zfile = download_config_zip(args.hostname, args.api_key)

    # Prepare directory
    module_path = Path(args.module_path)

    if module_path.exists():
        if module_path.is_dir():
            if any(module_path.iterdir()):
                if args.overwrite:
                    rmtree(module_path)
                else:
                    raise RuntimeError(f"Module path directory [{module_path}] is not empty, please use --overwrite option to clean it up")
        else:
            raise RuntimeError(f"Module path directory [{module_path}] exists, but it is not a directory")

    module_path.mkdir(mode=0o755, exist_ok=True)

    # Extract files from ZIP
    zfile.extractall(module_path)


def download_config_zip(hostname, api_key):
    url = f"https://{hostname}{ENDPOINT_CONFIG_MODULE}"

    headers = {
        'Content-Type': CONTENT_TYPE,
        'X-API-Key': api_key,
        'X-SDK-Name': SDK_NAME,
        'X-SDK-Version': __version__,
    }

    get_response = get(url, headers=headers)

    if not get_response.ok:
        raise RuntimeError(f"Failed to download config module from [{url}], please verify hostname and API key")

    return ZipFile(BytesIO(get_response.content), "r")
