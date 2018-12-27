# coding: utf-8

"""
    Gate API v4

    APIv4 合约接口提供了与合约交易相关的操作，包括公共接口查询合约市场行情，以及需要认证的私有接口， 实现基于 API 的自动交易。 API 文档按照 OpenAPI v3 标准制定 API 文档， 方便 API 使用者能够轻松生成需要的客户端代码，快速接入新的功能   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@mail.gate.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class InsuranceRecordInner(object):
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
    openapi_types = {
        't': 'int',
        'b': 'str'
    }

    attribute_map = {
        't': 't',
        'b': 'b'
    }

    def __init__(self, t=None, b=None):  # noqa: E501
        """InsuranceRecordInner - a model defined in OpenAPI"""  # noqa: E501

        self._t = None
        self._b = None
        self.discriminator = None

        if t is not None:
            self.t = t
        if b is not None:
            self.b = b

    @property
    def t(self):
        """Gets the t of this InsuranceRecordInner.  # noqa: E501

        秒 s 精度的 Unix 时间戳  # noqa: E501

        :return: The t of this InsuranceRecordInner.  # noqa: E501
        :rtype: int
        """
        return self._t

    @t.setter
    def t(self, t):
        """Sets the t of this InsuranceRecordInner.

        秒 s 精度的 Unix 时间戳  # noqa: E501

        :param t: The t of this InsuranceRecordInner.  # noqa: E501
        :type: int
        """

        self._t = t

    @property
    def b(self):
        """Gets the b of this InsuranceRecordInner.  # noqa: E501

        保险基金余额  # noqa: E501

        :return: The b of this InsuranceRecordInner.  # noqa: E501
        :rtype: str
        """
        return self._b

    @b.setter
    def b(self, b):
        """Sets the b of this InsuranceRecordInner.

        保险基金余额  # noqa: E501

        :param b: The b of this InsuranceRecordInner.  # noqa: E501
        :type: str
        """

        self._b = b

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
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
        if not isinstance(other, InsuranceRecordInner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
