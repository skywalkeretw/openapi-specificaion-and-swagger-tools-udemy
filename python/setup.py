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

REQUIRES = [
    "connexion",
    "swagger-ui-bundle>=0.0.2"
]

setup(
    name=NAME,
    version=VERSION,
    description="EazyShop Products APIs Definition",
    author_email="support@eazyshop.com",
    url="",
    keywords=["Swagger", "EazyShop Products APIs Definition"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
    # About Us **EazyShop** is a open market product selling company. Any website can list our products by  using our _APIs_. Shipping &amp; other logistics will be taken care by us. You will get an &#x60;Affiliate commision&#x60; for selling our products. # Categories suported   - Mobiles     - Apple     - Samsung     - OnePlus   - Laptops   - Televisions   - Headphones 
    """
)
