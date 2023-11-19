# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Address(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, address_line: str=None, city: str=None, state: str=None, zipcode: str=None, is_office_address: bool=None):  # noqa: E501
        """Address - a model defined in Swagger

        :param address_line: The address_line of this Address.  # noqa: E501
        :type address_line: str
        :param city: The city of this Address.  # noqa: E501
        :type city: str
        :param state: The state of this Address.  # noqa: E501
        :type state: str
        :param zipcode: The zipcode of this Address.  # noqa: E501
        :type zipcode: str
        :param is_office_address: The is_office_address of this Address.  # noqa: E501
        :type is_office_address: bool
        """
        self.swagger_types = {
            'address_line': str,
            'city': str,
            'state': str,
            'zipcode': str,
            'is_office_address': bool
        }

        self.attribute_map = {
            'address_line': 'addressLine',
            'city': 'city',
            'state': 'state',
            'zipcode': 'zipcode',
            'is_office_address': 'isOfficeAddress'
        }
        self._address_line = address_line
        self._city = city
        self._state = state
        self._zipcode = zipcode
        self._is_office_address = is_office_address

    @classmethod
    def from_dict(cls, dikt) -> 'Address':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Address of this Address.  # noqa: E501
        :rtype: Address
        """
        return util.deserialize_model(dikt, cls)

    @property
    def address_line(self) -> str:
        """Gets the address_line of this Address.


        :return: The address_line of this Address.
        :rtype: str
        """
        return self._address_line

    @address_line.setter
    def address_line(self, address_line: str):
        """Sets the address_line of this Address.


        :param address_line: The address_line of this Address.
        :type address_line: str
        """
        if address_line is None:
            raise ValueError("Invalid value for `address_line`, must not be `None`")  # noqa: E501

        self._address_line = address_line

    @property
    def city(self) -> str:
        """Gets the city of this Address.


        :return: The city of this Address.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city: str):
        """Sets the city of this Address.


        :param city: The city of this Address.
        :type city: str
        """
        if city is None:
            raise ValueError("Invalid value for `city`, must not be `None`")  # noqa: E501

        self._city = city

    @property
    def state(self) -> str:
        """Gets the state of this Address.


        :return: The state of this Address.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state: str):
        """Sets the state of this Address.


        :param state: The state of this Address.
        :type state: str
        """
        allowed_values = ["California", "Texas", "Indiana", "New York"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def zipcode(self) -> str:
        """Gets the zipcode of this Address.


        :return: The zipcode of this Address.
        :rtype: str
        """
        return self._zipcode

    @zipcode.setter
    def zipcode(self, zipcode: str):
        """Sets the zipcode of this Address.


        :param zipcode: The zipcode of this Address.
        :type zipcode: str
        """
        if zipcode is None:
            raise ValueError("Invalid value for `zipcode`, must not be `None`")  # noqa: E501

        self._zipcode = zipcode

    @property
    def is_office_address(self) -> bool:
        """Gets the is_office_address of this Address.


        :return: The is_office_address of this Address.
        :rtype: bool
        """
        return self._is_office_address

    @is_office_address.setter
    def is_office_address(self, is_office_address: bool):
        """Sets the is_office_address of this Address.


        :param is_office_address: The is_office_address of this Address.
        :type is_office_address: bool
        """

        self._is_office_address = is_office_address
