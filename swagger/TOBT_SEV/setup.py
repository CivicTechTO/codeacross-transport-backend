# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "swagger_server"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="Toronto Traffic Travel Times Sensor Data API",
    author_email="",
    url="",
    keywords=["Swagger", "Toronto Traffic Travel Times Sensor Data API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    long_description="""\
    The City of Toronto collects travel time data from Bluetooth and WiFi sensors on streets and highways across the City. Travel times are derived from individual point (i.e. single location) observations, generated when a vehicle or mobile device passes by a Bluetooth/WiFi sensor. Historical data (refreshed monthly) and a real-time feed are both available to the public.  Data is averaged into 5-minute snapshots based on a sample of detected vehicles. Availability of historical and real-time data are contingent on the installation date and on-going functionality of sensors on individual segments. 
    """
)

