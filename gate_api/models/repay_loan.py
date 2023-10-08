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


class RepayLoan(object):
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
    openapi_types = {'order_id': 'int', 'repay_amount': 'str', 'repaid_all': 'bool'}

    attribute_map = {'order_id': 'order_id', 'repay_amount': 'repay_amount', 'repaid_all': 'repaid_all'}

    def __init__(self, order_id=None, repay_amount=None, repaid_all=None, local_vars_configuration=None):  # noqa: E501
        # type: (int, str, bool, Configuration) -> None
        """RepayLoan - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._order_id = None
        self._repay_amount = None
        self._repaid_all = None
        self.discriminator = None

        self.order_id = order_id
        self.repay_amount = repay_amount
        self.repaid_all = repaid_all

    @property
    def order_id(self):
        """Gets the order_id of this RepayLoan.  # noqa: E501

        订单id  # noqa: E501

        :return: The order_id of this RepayLoan.  # noqa: E501
        :rtype: int
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this RepayLoan.

        订单id  # noqa: E501

        :param order_id: The order_id of this RepayLoan.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and order_id is None:  # noqa: E501
            raise ValueError("Invalid value for `order_id`, must not be `None`")  # noqa: E501

        self._order_id = order_id

    @property
    def repay_amount(self):
        """Gets the repay_amount of this RepayLoan.  # noqa: E501

        还款数量，部分还款时候是必须  # noqa: E501

        :return: The repay_amount of this RepayLoan.  # noqa: E501
        :rtype: str
        """
        return self._repay_amount

    @repay_amount.setter
    def repay_amount(self, repay_amount):
        """Sets the repay_amount of this RepayLoan.

        还款数量，部分还款时候是必须  # noqa: E501

        :param repay_amount: The repay_amount of this RepayLoan.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and repay_amount is None:  # noqa: E501
            raise ValueError("Invalid value for `repay_amount`, must not be `None`")  # noqa: E501

        self._repay_amount = repay_amount

    @property
    def repaid_all(self):
        """Gets the repaid_all of this RepayLoan.  # noqa: E501

        还款方式, 为`true`时全部还款, 为`false`时部分还款; 当为`false`部分还款时，不允许repay_amount参数大于用户剩余待还  # noqa: E501

        :return: The repaid_all of this RepayLoan.  # noqa: E501
        :rtype: bool
        """
        return self._repaid_all

    @repaid_all.setter
    def repaid_all(self, repaid_all):
        """Sets the repaid_all of this RepayLoan.

        还款方式, 为`true`时全部还款, 为`false`时部分还款; 当为`false`部分还款时，不允许repay_amount参数大于用户剩余待还  # noqa: E501

        :param repaid_all: The repaid_all of this RepayLoan.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and repaid_all is None:  # noqa: E501
            raise ValueError("Invalid value for `repaid_all`, must not be `None`")  # noqa: E501

        self._repaid_all = repaid_all

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
        if not isinstance(other, RepayLoan):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RepayLoan):
            return True

        return self.to_dict() != other.to_dict()
