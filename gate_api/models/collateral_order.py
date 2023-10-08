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


class CollateralOrder(object):
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
        'order_id': 'int',
        'collateral_currency': 'str',
        'collateral_amount': 'str',
        'borrow_currency': 'str',
        'borrow_amount': 'str',
        'repaid_amount': 'str',
        'repaid_principal': 'str',
        'repaid_interest': 'str',
        'init_ltv': 'str',
        'current_ltv': 'str',
        'liquidate_ltv': 'str',
        'status': 'str',
        'borrow_time': 'int',
        'left_repay_total': 'str',
        'left_repay_principal': 'str',
        'left_repay_interest': 'str',
    }

    attribute_map = {
        'order_id': 'order_id',
        'collateral_currency': 'collateral_currency',
        'collateral_amount': 'collateral_amount',
        'borrow_currency': 'borrow_currency',
        'borrow_amount': 'borrow_amount',
        'repaid_amount': 'repaid_amount',
        'repaid_principal': 'repaid_principal',
        'repaid_interest': 'repaid_interest',
        'init_ltv': 'init_ltv',
        'current_ltv': 'current_ltv',
        'liquidate_ltv': 'liquidate_ltv',
        'status': 'status',
        'borrow_time': 'borrow_time',
        'left_repay_total': 'left_repay_total',
        'left_repay_principal': 'left_repay_principal',
        'left_repay_interest': 'left_repay_interest',
    }

    def __init__(
        self,
        order_id=None,
        collateral_currency=None,
        collateral_amount=None,
        borrow_currency=None,
        borrow_amount=None,
        repaid_amount=None,
        repaid_principal=None,
        repaid_interest=None,
        init_ltv=None,
        current_ltv=None,
        liquidate_ltv=None,
        status=None,
        borrow_time=None,
        left_repay_total=None,
        left_repay_principal=None,
        left_repay_interest=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        # type: (int, str, str, str, str, str, str, str, str, str, str, str, int, str, str, str, Configuration) -> None
        """CollateralOrder - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._order_id = None
        self._collateral_currency = None
        self._collateral_amount = None
        self._borrow_currency = None
        self._borrow_amount = None
        self._repaid_amount = None
        self._repaid_principal = None
        self._repaid_interest = None
        self._init_ltv = None
        self._current_ltv = None
        self._liquidate_ltv = None
        self._status = None
        self._borrow_time = None
        self._left_repay_total = None
        self._left_repay_principal = None
        self._left_repay_interest = None
        self.discriminator = None

        if order_id is not None:
            self.order_id = order_id
        if collateral_currency is not None:
            self.collateral_currency = collateral_currency
        if collateral_amount is not None:
            self.collateral_amount = collateral_amount
        if borrow_currency is not None:
            self.borrow_currency = borrow_currency
        if borrow_amount is not None:
            self.borrow_amount = borrow_amount
        if repaid_amount is not None:
            self.repaid_amount = repaid_amount
        if repaid_principal is not None:
            self.repaid_principal = repaid_principal
        if repaid_interest is not None:
            self.repaid_interest = repaid_interest
        if init_ltv is not None:
            self.init_ltv = init_ltv
        if current_ltv is not None:
            self.current_ltv = current_ltv
        if liquidate_ltv is not None:
            self.liquidate_ltv = liquidate_ltv
        if status is not None:
            self.status = status
        if borrow_time is not None:
            self.borrow_time = borrow_time
        if left_repay_total is not None:
            self.left_repay_total = left_repay_total
        if left_repay_principal is not None:
            self.left_repay_principal = left_repay_principal
        if left_repay_interest is not None:
            self.left_repay_interest = left_repay_interest

    @property
    def order_id(self):
        """Gets the order_id of this CollateralOrder.  # noqa: E501

        订单id  # noqa: E501

        :return: The order_id of this CollateralOrder.  # noqa: E501
        :rtype: int
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this CollateralOrder.

        订单id  # noqa: E501

        :param order_id: The order_id of this CollateralOrder.  # noqa: E501
        :type: int
        """

        self._order_id = order_id

    @property
    def collateral_currency(self):
        """Gets the collateral_currency of this CollateralOrder.  # noqa: E501

        质押币种  # noqa: E501

        :return: The collateral_currency of this CollateralOrder.  # noqa: E501
        :rtype: str
        """
        return self._collateral_currency

    @collateral_currency.setter
    def collateral_currency(self, collateral_currency):
        """Sets the collateral_currency of this CollateralOrder.

        质押币种  # noqa: E501

        :param collateral_currency: The collateral_currency of this CollateralOrder.  # noqa: E501
        :type: str
        """

        self._collateral_currency = collateral_currency

    @property
    def collateral_amount(self):
        """Gets the collateral_amount of this CollateralOrder.  # noqa: E501

        质押数量  # noqa: E501

        :return: The collateral_amount of this CollateralOrder.  # noqa: E501
        :rtype: str
        """
        return self._collateral_amount

    @collateral_amount.setter
    def collateral_amount(self, collateral_amount):
        """Sets the collateral_amount of this CollateralOrder.

        质押数量  # noqa: E501

        :param collateral_amount: The collateral_amount of this CollateralOrder.  # noqa: E501
        :type: str
        """

        self._collateral_amount = collateral_amount

    @property
    def borrow_currency(self):
        """Gets the borrow_currency of this CollateralOrder.  # noqa: E501

        借款币种  # noqa: E501

        :return: The borrow_currency of this CollateralOrder.  # noqa: E501
        :rtype: str
        """
        return self._borrow_currency

    @borrow_currency.setter
    def borrow_currency(self, borrow_currency):
        """Sets the borrow_currency of this CollateralOrder.

        借款币种  # noqa: E501

        :param borrow_currency: The borrow_currency of this CollateralOrder.  # noqa: E501
        :type: str
        """

        self._borrow_currency = borrow_currency

    @property
    def borrow_amount(self):
        """Gets the borrow_amount of this CollateralOrder.  # noqa: E501

        借款数量  # noqa: E501

        :return: The borrow_amount of this CollateralOrder.  # noqa: E501
        :rtype: str
        """
        return self._borrow_amount

    @borrow_amount.setter
    def borrow_amount(self, borrow_amount):
        """Sets the borrow_amount of this CollateralOrder.

        借款数量  # noqa: E501

        :param borrow_amount: The borrow_amount of this CollateralOrder.  # noqa: E501
        :type: str
        """

        self._borrow_amount = borrow_amount

    @property
    def repaid_amount(self):
        """Gets the repaid_amount of this CollateralOrder.  # noqa: E501

        已还款数量  # noqa: E501

        :return: The repaid_amount of this CollateralOrder.  # noqa: E501
        :rtype: str
        """
        return self._repaid_amount

    @repaid_amount.setter
    def repaid_amount(self, repaid_amount):
        """Sets the repaid_amount of this CollateralOrder.

        已还款数量  # noqa: E501

        :param repaid_amount: The repaid_amount of this CollateralOrder.  # noqa: E501
        :type: str
        """

        self._repaid_amount = repaid_amount

    @property
    def repaid_principal(self):
        """Gets the repaid_principal of this CollateralOrder.  # noqa: E501

        已还本金  # noqa: E501

        :return: The repaid_principal of this CollateralOrder.  # noqa: E501
        :rtype: str
        """
        return self._repaid_principal

    @repaid_principal.setter
    def repaid_principal(self, repaid_principal):
        """Sets the repaid_principal of this CollateralOrder.

        已还本金  # noqa: E501

        :param repaid_principal: The repaid_principal of this CollateralOrder.  # noqa: E501
        :type: str
        """

        self._repaid_principal = repaid_principal

    @property
    def repaid_interest(self):
        """Gets the repaid_interest of this CollateralOrder.  # noqa: E501

        已还利息  # noqa: E501

        :return: The repaid_interest of this CollateralOrder.  # noqa: E501
        :rtype: str
        """
        return self._repaid_interest

    @repaid_interest.setter
    def repaid_interest(self, repaid_interest):
        """Sets the repaid_interest of this CollateralOrder.

        已还利息  # noqa: E501

        :param repaid_interest: The repaid_interest of this CollateralOrder.  # noqa: E501
        :type: str
        """

        self._repaid_interest = repaid_interest

    @property
    def init_ltv(self):
        """Gets the init_ltv of this CollateralOrder.  # noqa: E501

        初始质押率  # noqa: E501

        :return: The init_ltv of this CollateralOrder.  # noqa: E501
        :rtype: str
        """
        return self._init_ltv

    @init_ltv.setter
    def init_ltv(self, init_ltv):
        """Sets the init_ltv of this CollateralOrder.

        初始质押率  # noqa: E501

        :param init_ltv: The init_ltv of this CollateralOrder.  # noqa: E501
        :type: str
        """

        self._init_ltv = init_ltv

    @property
    def current_ltv(self):
        """Gets the current_ltv of this CollateralOrder.  # noqa: E501

        当前质押率  # noqa: E501

        :return: The current_ltv of this CollateralOrder.  # noqa: E501
        :rtype: str
        """
        return self._current_ltv

    @current_ltv.setter
    def current_ltv(self, current_ltv):
        """Sets the current_ltv of this CollateralOrder.

        当前质押率  # noqa: E501

        :param current_ltv: The current_ltv of this CollateralOrder.  # noqa: E501
        :type: str
        """

        self._current_ltv = current_ltv

    @property
    def liquidate_ltv(self):
        """Gets the liquidate_ltv of this CollateralOrder.  # noqa: E501

        平仓质押率  # noqa: E501

        :return: The liquidate_ltv of this CollateralOrder.  # noqa: E501
        :rtype: str
        """
        return self._liquidate_ltv

    @liquidate_ltv.setter
    def liquidate_ltv(self, liquidate_ltv):
        """Sets the liquidate_ltv of this CollateralOrder.

        平仓质押率  # noqa: E501

        :param liquidate_ltv: The liquidate_ltv of this CollateralOrder.  # noqa: E501
        :type: str
        """

        self._liquidate_ltv = liquidate_ltv

    @property
    def status(self):
        """Gets the status of this CollateralOrder.  # noqa: E501

        订单状态: - initial: 下单初始状态 - collateral_deducted: 扣除质押物成功 - collateral_returning: 放款失败-待退回质押物 - lent: 放款成功 - repaying: 还款中 - liquidating: 平仓中 - finished: 已完成 - closed_liquidated: 已结束-平仓还款结束  # noqa: E501

        :return: The status of this CollateralOrder.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CollateralOrder.

        订单状态: - initial: 下单初始状态 - collateral_deducted: 扣除质押物成功 - collateral_returning: 放款失败-待退回质押物 - lent: 放款成功 - repaying: 还款中 - liquidating: 平仓中 - finished: 已完成 - closed_liquidated: 已结束-平仓还款结束  # noqa: E501

        :param status: The status of this CollateralOrder.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def borrow_time(self):
        """Gets the borrow_time of this CollateralOrder.  # noqa: E501

        借款时间，时间戳，单位秒  # noqa: E501

        :return: The borrow_time of this CollateralOrder.  # noqa: E501
        :rtype: int
        """
        return self._borrow_time

    @borrow_time.setter
    def borrow_time(self, borrow_time):
        """Sets the borrow_time of this CollateralOrder.

        借款时间，时间戳，单位秒  # noqa: E501

        :param borrow_time: The borrow_time of this CollateralOrder.  # noqa: E501
        :type: int
        """

        self._borrow_time = borrow_time

    @property
    def left_repay_total(self):
        """Gets the left_repay_total of this CollateralOrder.  # noqa: E501

        待还本息（待还本金+待还利息）  # noqa: E501

        :return: The left_repay_total of this CollateralOrder.  # noqa: E501
        :rtype: str
        """
        return self._left_repay_total

    @left_repay_total.setter
    def left_repay_total(self, left_repay_total):
        """Sets the left_repay_total of this CollateralOrder.

        待还本息（待还本金+待还利息）  # noqa: E501

        :param left_repay_total: The left_repay_total of this CollateralOrder.  # noqa: E501
        :type: str
        """

        self._left_repay_total = left_repay_total

    @property
    def left_repay_principal(self):
        """Gets the left_repay_principal of this CollateralOrder.  # noqa: E501

        待还本金  # noqa: E501

        :return: The left_repay_principal of this CollateralOrder.  # noqa: E501
        :rtype: str
        """
        return self._left_repay_principal

    @left_repay_principal.setter
    def left_repay_principal(self, left_repay_principal):
        """Sets the left_repay_principal of this CollateralOrder.

        待还本金  # noqa: E501

        :param left_repay_principal: The left_repay_principal of this CollateralOrder.  # noqa: E501
        :type: str
        """

        self._left_repay_principal = left_repay_principal

    @property
    def left_repay_interest(self):
        """Gets the left_repay_interest of this CollateralOrder.  # noqa: E501

        待还利息  # noqa: E501

        :return: The left_repay_interest of this CollateralOrder.  # noqa: E501
        :rtype: str
        """
        return self._left_repay_interest

    @left_repay_interest.setter
    def left_repay_interest(self, left_repay_interest):
        """Sets the left_repay_interest of this CollateralOrder.

        待还利息  # noqa: E501

        :param left_repay_interest: The left_repay_interest of this CollateralOrder.  # noqa: E501
        :type: str
        """

        self._left_repay_interest = left_repay_interest

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
        if not isinstance(other, CollateralOrder):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CollateralOrder):
            return True

        return self.to_dict() != other.to_dict()
