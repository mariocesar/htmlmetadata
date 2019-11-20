import sys

from setuptools import find_packages, setup

if sys.version_info < (3, 6):
    raise Exception(f"Unsupported python version {sys.version}. Use Python 3.6 or Superior")

setup()
