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


class OrderBook(object):
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
    openapi_types = {'id': 'int', 'asks': 'list[list[str]]', 'bids': 'list[list[str]]'}

    attribute_map = {'id': 'id', 'asks': 'asks', 'bids': 'bids'}

    def __init__(self, id=None, asks=None, bids=None, local_vars_configuration=None):  # noqa: E501
        # type: (int, list[list[str]], list[list[str]], Configuration) -> None
        """OrderBook - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._asks = None
        self._bids = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.asks = asks
        self.bids = bids

    @property
    def id(self):
        """Gets the id of this OrderBook.  # noqa: E501

        Order book ID, which is updated whenever the order book is changed. Valid only when `with_id` is set to `true`  # noqa: E501

        :return: The id of this OrderBook.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrderBook.

        Order book ID, which is updated whenever the order book is changed. Valid only when `with_id` is set to `true`  # noqa: E501

        :param id: The id of this OrderBook.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def asks(self):
        """Gets the asks of this OrderBook.  # noqa: E501

        Asks order depth  # noqa: E501

        :return: The asks of this OrderBook.  # noqa: E501
        :rtype: list[list[str]]
        """
        return self._asks

    @asks.setter
    def asks(self, asks):
        """Sets the asks of this OrderBook.

        Asks order depth  # noqa: E501

        :param asks: The asks of this OrderBook.  # noqa: E501
        :type: list[list[str]]
        """
        if self.local_vars_configuration.client_side_validation and asks is None:  # noqa: E501
            raise ValueError("Invalid value for `asks`, must not be `None`")  # noqa: E501

        self._asks = asks

    @property
    def bids(self):
        """Gets the bids of this OrderBook.  # noqa: E501

        Bids order depth  # noqa: E501

        :return: The bids of this OrderBook.  # noqa: E501
        :rtype: list[list[str]]
        """
        return self._bids

    @bids.setter
    def bids(self, bids):
        """Sets the bids of this OrderBook.

        Bids order depth  # noqa: E501

        :param bids: The bids of this OrderBook.  # noqa: E501
        :type: list[list[str]]
        """
        if self.local_vars_configuration.client_side_validation and bids is None:  # noqa: E501
            raise ValueError("Invalid value for `bids`, must not be `None`")  # noqa: E501

        self._bids = bids

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
        if not isinstance(other, OrderBook):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrderBook):
            return True

        return self.to_dict() != other.to_dict()
