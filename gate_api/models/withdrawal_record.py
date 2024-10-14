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


class WithdrawalRecord(object):
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
        'id': 'str',
        'txid': 'str',
        'block_number': 'str',
        'withdraw_order_id': 'str',
        'timestamp': 'str',
        'amount': 'str',
        'fee': 'str',
        'currency': 'str',
        'address': 'str',
        'memo': 'str',
        'status': 'str',
        'chain': 'str',
    }

    attribute_map = {
        'id': 'id',
        'txid': 'txid',
        'block_number': 'block_number',
        'withdraw_order_id': 'withdraw_order_id',
        'timestamp': 'timestamp',
        'amount': 'amount',
        'fee': 'fee',
        'currency': 'currency',
        'address': 'address',
        'memo': 'memo',
        'status': 'status',
        'chain': 'chain',
    }

    def __init__(
        self,
        id=None,
        txid=None,
        block_number=None,
        withdraw_order_id=None,
        timestamp=None,
        amount=None,
        fee=None,
        currency=None,
        address=None,
        memo=None,
        status=None,
        chain=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        # type: (str, str, str, str, str, str, str, str, str, str, str, str, Configuration) -> None
        """WithdrawalRecord - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._txid = None
        self._block_number = None
        self._withdraw_order_id = None
        self._timestamp = None
        self._amount = None
        self._fee = None
        self._currency = None
        self._address = None
        self._memo = None
        self._status = None
        self._chain = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if txid is not None:
            self.txid = txid
        if block_number is not None:
            self.block_number = block_number
        if withdraw_order_id is not None:
            self.withdraw_order_id = withdraw_order_id
        if timestamp is not None:
            self.timestamp = timestamp
        self.amount = amount
        if fee is not None:
            self.fee = fee
        self.currency = currency
        if address is not None:
            self.address = address
        if memo is not None:
            self.memo = memo
        if status is not None:
            self.status = status
        self.chain = chain

    @property
    def id(self):
        """Gets the id of this WithdrawalRecord.  # noqa: E501

        Record ID  # noqa: E501

        :return: The id of this WithdrawalRecord.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WithdrawalRecord.

        Record ID  # noqa: E501

        :param id: The id of this WithdrawalRecord.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def txid(self):
        """Gets the txid of this WithdrawalRecord.  # noqa: E501

        Hash record of the withdrawal  # noqa: E501

        :return: The txid of this WithdrawalRecord.  # noqa: E501
        :rtype: str
        """
        return self._txid

    @txid.setter
    def txid(self, txid):
        """Sets the txid of this WithdrawalRecord.

        Hash record of the withdrawal  # noqa: E501

        :param txid: The txid of this WithdrawalRecord.  # noqa: E501
        :type: str
        """

        self._txid = txid

    @property
    def block_number(self):
        """Gets the block_number of this WithdrawalRecord.  # noqa: E501

        区块编号  # noqa: E501

        :return: The block_number of this WithdrawalRecord.  # noqa: E501
        :rtype: str
        """
        return self._block_number

    @block_number.setter
    def block_number(self, block_number):
        """Sets the block_number of this WithdrawalRecord.

        区块编号  # noqa: E501

        :param block_number: The block_number of this WithdrawalRecord.  # noqa: E501
        :type: str
        """

        self._block_number = block_number

    @property
    def withdraw_order_id(self):
        """Gets the withdraw_order_id of this WithdrawalRecord.  # noqa: E501

        Client order id, up to 32 length and can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.)   # noqa: E501

        :return: The withdraw_order_id of this WithdrawalRecord.  # noqa: E501
        :rtype: str
        """
        return self._withdraw_order_id

    @withdraw_order_id.setter
    def withdraw_order_id(self, withdraw_order_id):
        """Sets the withdraw_order_id of this WithdrawalRecord.

        Client order id, up to 32 length and can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.)   # noqa: E501

        :param withdraw_order_id: The withdraw_order_id of this WithdrawalRecord.  # noqa: E501
        :type: str
        """

        self._withdraw_order_id = withdraw_order_id

    @property
    def timestamp(self):
        """Gets the timestamp of this WithdrawalRecord.  # noqa: E501

        Operation time  # noqa: E501

        :return: The timestamp of this WithdrawalRecord.  # noqa: E501
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this WithdrawalRecord.

        Operation time  # noqa: E501

        :param timestamp: The timestamp of this WithdrawalRecord.  # noqa: E501
        :type: str
        """

        self._timestamp = timestamp

    @property
    def amount(self):
        """Gets the amount of this WithdrawalRecord.  # noqa: E501

        Currency amount  # noqa: E501

        :return: The amount of this WithdrawalRecord.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this WithdrawalRecord.

        Currency amount  # noqa: E501

        :param amount: The amount of this WithdrawalRecord.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and amount is None:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def fee(self):
        """Gets the fee of this WithdrawalRecord.  # noqa: E501

        fee  # noqa: E501

        :return: The fee of this WithdrawalRecord.  # noqa: E501
        :rtype: str
        """
        return self._fee

    @fee.setter
    def fee(self, fee):
        """Sets the fee of this WithdrawalRecord.

        fee  # noqa: E501

        :param fee: The fee of this WithdrawalRecord.  # noqa: E501
        :type: str
        """

        self._fee = fee

    @property
    def currency(self):
        """Gets the currency of this WithdrawalRecord.  # noqa: E501

        Currency name  # noqa: E501

        :return: The currency of this WithdrawalRecord.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this WithdrawalRecord.

        Currency name  # noqa: E501

        :param currency: The currency of this WithdrawalRecord.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and currency is None:  # noqa: E501
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def address(self):
        """Gets the address of this WithdrawalRecord.  # noqa: E501

        Withdrawal address. Required for withdrawals  # noqa: E501

        :return: The address of this WithdrawalRecord.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this WithdrawalRecord.

        Withdrawal address. Required for withdrawals  # noqa: E501

        :param address: The address of this WithdrawalRecord.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def memo(self):
        """Gets the memo of this WithdrawalRecord.  # noqa: E501

        Additional remarks with regards to the withdrawal  # noqa: E501

        :return: The memo of this WithdrawalRecord.  # noqa: E501
        :rtype: str
        """
        return self._memo

    @memo.setter
    def memo(self, memo):
        """Sets the memo of this WithdrawalRecord.

        Additional remarks with regards to the withdrawal  # noqa: E501

        :param memo: The memo of this WithdrawalRecord.  # noqa: E501
        :type: str
        """

        self._memo = memo

    @property
    def status(self):
        """Gets the status of this WithdrawalRecord.  # noqa: E501

        交易状态  - DONE: 完成 (block_number > 0 才算真的上链完成) - CANCEL: 已取消 - REQUEST: 请求中 - MANUAL: 待人工审核 - BCODE: 充值码操作 - EXTPEND: 已经发送等待确认 - FAIL: 链上失败等待确认 - INVALID: 无效订单 - VERIFY: 验证中 - PROCES: 处理中 - PEND: 处理中 - DMOVE: 待人工审核 - SPLITPEND: cny提现大于5w,自动分单  # noqa: E501

        :return: The status of this WithdrawalRecord.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this WithdrawalRecord.

        交易状态  - DONE: 完成 (block_number > 0 才算真的上链完成) - CANCEL: 已取消 - REQUEST: 请求中 - MANUAL: 待人工审核 - BCODE: 充值码操作 - EXTPEND: 已经发送等待确认 - FAIL: 链上失败等待确认 - INVALID: 无效订单 - VERIFY: 验证中 - PROCES: 处理中 - PEND: 处理中 - DMOVE: 待人工审核 - SPLITPEND: cny提现大于5w,自动分单  # noqa: E501

        :param status: The status of this WithdrawalRecord.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "DONE",
            "CANCEL",
            "REQUEST",
            "MANUAL",
            "BCODE",
            "EXTPEND",
            "FAIL",
            "INVALID",
            "VERIFY",
            "PROCES",
            "PEND",
            "DMOVE",
            "SPLITPEND",
        ]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}".format(status, allowed_values)  # noqa: E501
            )

        self._status = status

    @property
    def chain(self):
        """Gets the chain of this WithdrawalRecord.  # noqa: E501

        Name of the chain used in withdrawals  # noqa: E501

        :return: The chain of this WithdrawalRecord.  # noqa: E501
        :rtype: str
        """
        return self._chain

    @chain.setter
    def chain(self, chain):
        """Sets the chain of this WithdrawalRecord.

        Name of the chain used in withdrawals  # noqa: E501

        :param chain: The chain of this WithdrawalRecord.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and chain is None:  # noqa: E501
            raise ValueError("Invalid value for `chain`, must not be `None`")  # noqa: E501

        self._chain = chain

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
        if not isinstance(other, WithdrawalRecord):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WithdrawalRecord):
            return True

        return self.to_dict() != other.to_dict()