# coding: utf-8

"""
    Gate API v4

    Welcome to Gate.io API  APIv4 provides spot, margin and futures trading operations. There are public APIs to retrieve the real-time market statistics, and private APIs which needs authentication to trade on user's behalf.  # noqa: E501

    Contact: support@mail.gate.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from gate_api.configuration import Configuration


class UnifiedBorrowable(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {'currency': 'str', 'amount': 'str'}

    attribute_map = {'currency': 'currency', 'amount': 'amount'}

    def __init__(self, currency=None, amount=None, local_vars_configuration=None):  # noqa: E501
        # type: (str, str, Configuration) -> None
        """UnifiedBorrowable - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._currency = None
        self._amount = None
        self.discriminator = None

        if currency is not None:
            self.currency = currency
        if amount is not None:
            self.amount = amount

    @property
    def currency(self):
        """Gets the currency of this UnifiedBorrowable.  # noqa: E501

        Currency detail  # noqa: E501

        :return: The currency of this UnifiedBorrowable.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this UnifiedBorrowable.

        Currency detail  # noqa: E501

        :param currency: The currency of this UnifiedBorrowable.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def amount(self):
        """Gets the amount of this UnifiedBorrowable.  # noqa: E501

        Max borrowable amount  # noqa: E501

        :return: The amount of this UnifiedBorrowable.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this UnifiedBorrowable.

        Max borrowable amount  # noqa: E501

        :param amount: The amount of this UnifiedBorrowable.  # noqa: E501
        :type: str
        """

        self._amount = amount

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict()) if hasattr(item[1], "to_dict") else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UnifiedBorrowable):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UnifiedBorrowable):
            return True

        return self.to_dict() != other.to_dict()
