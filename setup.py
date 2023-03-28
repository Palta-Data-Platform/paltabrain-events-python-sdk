from pathlib import Path
from setuptools import setup, find_packages

__version__ = '0.0.0'
version_path = Path(__file__).parent / 'paltabrain_sdk' / 'version.py'
exec(version_path.read_text())

setup(
    name='paltabrain_sdk',
    version=__version__,
    url='https://github.com/Palta-Data-Platform/paltabrain-events-python-sdk',
    author='Vitaly Markov',
    author_email='vitaly.markov@palta.com',
    description='',
    packages=find_packages(),
    install_requires=[
        'protobuf',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'paltabrain-sdk-download-config = paltabrain_sdk.__main__:download_config_entry_point',
        ],
    },
)
