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


class StpGroup(object):
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
    openapi_types = {'id': 'int', 'name': 'str', 'creator_id': 'int', 'create_time': 'int'}

    attribute_map = {'id': 'id', 'name': 'name', 'creator_id': 'creator_id', 'create_time': 'create_time'}

    def __init__(
        self, id=None, name=None, creator_id=None, create_time=None, local_vars_configuration=None
    ):  # noqa: E501
        # type: (int, str, int, int, Configuration) -> None
        """StpGroup - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._creator_id = None
        self._create_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if creator_id is not None:
            self.creator_id = creator_id
        if create_time is not None:
            self.create_time = create_time

    @property
    def id(self):
        """Gets the id of this StpGroup.  # noqa: E501

        STP Group ID  # noqa: E501

        :return: The id of this StpGroup.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StpGroup.

        STP Group ID  # noqa: E501

        :param id: The id of this StpGroup.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this StpGroup.  # noqa: E501

        STP Group name  # noqa: E501

        :return: The name of this StpGroup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StpGroup.

        STP Group name  # noqa: E501

        :param name: The name of this StpGroup.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def creator_id(self):
        """Gets the creator_id of this StpGroup.  # noqa: E501

        Creator ID  # noqa: E501

        :return: The creator_id of this StpGroup.  # noqa: E501
        :rtype: int
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this StpGroup.

        Creator ID  # noqa: E501

        :param creator_id: The creator_id of this StpGroup.  # noqa: E501
        :type: int
        """

        self._creator_id = creator_id

    @property
    def create_time(self):
        """Gets the create_time of this StpGroup.  # noqa: E501

        Creation time  # noqa: E501

        :return: The create_time of this StpGroup.  # noqa: E501
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this StpGroup.

        Creation time  # noqa: E501

        :param create_time: The create_time of this StpGroup.  # noqa: E501
        :type: int
        """

        self._create_time = create_time

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
        if not isinstance(other, StpGroup):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StpGroup):
            return True

        return self.to_dict() != other.to_dict()