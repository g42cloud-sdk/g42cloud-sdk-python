# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrePaidServerExtendParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'charging_mode': 'str',
        'region_id': 'str',
        'period_type': 'str',
        'period_num': 'int',
        'is_auto_renew': 'str',
        'is_auto_pay': 'str',
        'enterprise_project_id': 'str',
        'support_auto_recovery': 'bool',
        'market_type': 'str',
        'spot_price': 'str',
        'disk_prior': 'str',
        'spot_duration_hours': 'int',
        'interruption_policy': 'str',
        'spot_duration_count': 'int'
    }

    attribute_map = {
        'charging_mode': 'chargingMode',
        'region_id': 'regionID',
        'period_type': 'periodType',
        'period_num': 'periodNum',
        'is_auto_renew': 'isAutoRenew',
        'is_auto_pay': 'isAutoPay',
        'enterprise_project_id': 'enterprise_project_id',
        'support_auto_recovery': 'support_auto_recovery',
        'market_type': 'marketType',
        'spot_price': 'spotPrice',
        'disk_prior': 'diskPrior',
        'spot_duration_hours': 'spot_duration_hours',
        'interruption_policy': 'interruption_policy',
        'spot_duration_count': 'spot_duration_count'
    }

    def __init__(self, charging_mode=None, region_id=None, period_type=None, period_num=None, is_auto_renew=None, is_auto_pay=None, enterprise_project_id=None, support_auto_recovery=None, market_type=None, spot_price=None, disk_prior=None, spot_duration_hours=None, interruption_policy=None, spot_duration_count=None):
        """PrePaidServerExtendParam

        The model defined in g42cloud sdk

        :param charging_mode: The param of the PrePaidServerExtendParam
        :type charging_mode: str
        :param region_id: The param of the PrePaidServerExtendParam
        :type region_id: str
        :param period_type: The param of the PrePaidServerExtendParam
        :type period_type: str
        :param period_num: The param of the PrePaidServerExtendParam
        :type period_num: int
        :param is_auto_renew: The param of the PrePaidServerExtendParam
        :type is_auto_renew: str
        :param is_auto_pay: The param of the PrePaidServerExtendParam
        :type is_auto_pay: str
        :param enterprise_project_id: The param of the PrePaidServerExtendParam
        :type enterprise_project_id: str
        :param support_auto_recovery: The param of the PrePaidServerExtendParam
        :type support_auto_recovery: bool
        :param market_type: The param of the PrePaidServerExtendParam
        :type market_type: str
        :param spot_price: The param of the PrePaidServerExtendParam
        :type spot_price: str
        :param disk_prior: The param of the PrePaidServerExtendParam
        :type disk_prior: str
        :param spot_duration_hours: The param of the PrePaidServerExtendParam
        :type spot_duration_hours: int
        :param interruption_policy: The param of the PrePaidServerExtendParam
        :type interruption_policy: str
        :param spot_duration_count: The param of the PrePaidServerExtendParam
        :type spot_duration_count: int
        """
        
        

        self._charging_mode = None
        self._region_id = None
        self._period_type = None
        self._period_num = None
        self._is_auto_renew = None
        self._is_auto_pay = None
        self._enterprise_project_id = None
        self._support_auto_recovery = None
        self._market_type = None
        self._spot_price = None
        self._disk_prior = None
        self._spot_duration_hours = None
        self._interruption_policy = None
        self._spot_duration_count = None
        self.discriminator = None

        if charging_mode is not None:
            self.charging_mode = charging_mode
        if region_id is not None:
            self.region_id = region_id
        if period_type is not None:
            self.period_type = period_type
        if period_num is not None:
            self.period_num = period_num
        if is_auto_renew is not None:
            self.is_auto_renew = is_auto_renew
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if support_auto_recovery is not None:
            self.support_auto_recovery = support_auto_recovery
        if market_type is not None:
            self.market_type = market_type
        if spot_price is not None:
            self.spot_price = spot_price
        if disk_prior is not None:
            self.disk_prior = disk_prior
        if spot_duration_hours is not None:
            self.spot_duration_hours = spot_duration_hours
        if interruption_policy is not None:
            self.interruption_policy = interruption_policy
        if spot_duration_count is not None:
            self.spot_duration_count = spot_duration_count

    @property
    def charging_mode(self):
        """Gets the charging_mode of this PrePaidServerExtendParam.

        :return: The charging_mode of this PrePaidServerExtendParam.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        """Sets the charging_mode of this PrePaidServerExtendParam.

        :param charging_mode: The charging_mode of this PrePaidServerExtendParam.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def region_id(self):
        """Gets the region_id of this PrePaidServerExtendParam.

        :return: The region_id of this PrePaidServerExtendParam.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this PrePaidServerExtendParam.

        :param region_id: The region_id of this PrePaidServerExtendParam.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def period_type(self):
        """Gets the period_type of this PrePaidServerExtendParam.

        :return: The period_type of this PrePaidServerExtendParam.
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        """Sets the period_type of this PrePaidServerExtendParam.

        :param period_type: The period_type of this PrePaidServerExtendParam.
        :type period_type: str
        """
        self._period_type = period_type

    @property
    def period_num(self):
        """Gets the period_num of this PrePaidServerExtendParam.

        :return: The period_num of this PrePaidServerExtendParam.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        """Sets the period_num of this PrePaidServerExtendParam.

        :param period_num: The period_num of this PrePaidServerExtendParam.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def is_auto_renew(self):
        """Gets the is_auto_renew of this PrePaidServerExtendParam.

        :return: The is_auto_renew of this PrePaidServerExtendParam.
        :rtype: str
        """
        return self._is_auto_renew

    @is_auto_renew.setter
    def is_auto_renew(self, is_auto_renew):
        """Sets the is_auto_renew of this PrePaidServerExtendParam.

        :param is_auto_renew: The is_auto_renew of this PrePaidServerExtendParam.
        :type is_auto_renew: str
        """
        self._is_auto_renew = is_auto_renew

    @property
    def is_auto_pay(self):
        """Gets the is_auto_pay of this PrePaidServerExtendParam.

        :return: The is_auto_pay of this PrePaidServerExtendParam.
        :rtype: str
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        """Sets the is_auto_pay of this PrePaidServerExtendParam.

        :param is_auto_pay: The is_auto_pay of this PrePaidServerExtendParam.
        :type is_auto_pay: str
        """
        self._is_auto_pay = is_auto_pay

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this PrePaidServerExtendParam.

        :return: The enterprise_project_id of this PrePaidServerExtendParam.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this PrePaidServerExtendParam.

        :param enterprise_project_id: The enterprise_project_id of this PrePaidServerExtendParam.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def support_auto_recovery(self):
        """Gets the support_auto_recovery of this PrePaidServerExtendParam.

        :return: The support_auto_recovery of this PrePaidServerExtendParam.
        :rtype: bool
        """
        return self._support_auto_recovery

    @support_auto_recovery.setter
    def support_auto_recovery(self, support_auto_recovery):
        """Sets the support_auto_recovery of this PrePaidServerExtendParam.

        :param support_auto_recovery: The support_auto_recovery of this PrePaidServerExtendParam.
        :type support_auto_recovery: bool
        """
        self._support_auto_recovery = support_auto_recovery

    @property
    def market_type(self):
        """Gets the market_type of this PrePaidServerExtendParam.

        :return: The market_type of this PrePaidServerExtendParam.
        :rtype: str
        """
        return self._market_type

    @market_type.setter
    def market_type(self, market_type):
        """Sets the market_type of this PrePaidServerExtendParam.

        :param market_type: The market_type of this PrePaidServerExtendParam.
        :type market_type: str
        """
        self._market_type = market_type

    @property
    def spot_price(self):
        """Gets the spot_price of this PrePaidServerExtendParam.

        :return: The spot_price of this PrePaidServerExtendParam.
        :rtype: str
        """
        return self._spot_price

    @spot_price.setter
    def spot_price(self, spot_price):
        """Sets the spot_price of this PrePaidServerExtendParam.

        :param spot_price: The spot_price of this PrePaidServerExtendParam.
        :type spot_price: str
        """
        self._spot_price = spot_price

    @property
    def disk_prior(self):
        """Gets the disk_prior of this PrePaidServerExtendParam.

        :return: The disk_prior of this PrePaidServerExtendParam.
        :rtype: str
        """
        return self._disk_prior

    @disk_prior.setter
    def disk_prior(self, disk_prior):
        """Sets the disk_prior of this PrePaidServerExtendParam.

        :param disk_prior: The disk_prior of this PrePaidServerExtendParam.
        :type disk_prior: str
        """
        self._disk_prior = disk_prior

    @property
    def spot_duration_hours(self):
        """Gets the spot_duration_hours of this PrePaidServerExtendParam.

        :return: The spot_duration_hours of this PrePaidServerExtendParam.
        :rtype: int
        """
        return self._spot_duration_hours

    @spot_duration_hours.setter
    def spot_duration_hours(self, spot_duration_hours):
        """Sets the spot_duration_hours of this PrePaidServerExtendParam.

        :param spot_duration_hours: The spot_duration_hours of this PrePaidServerExtendParam.
        :type spot_duration_hours: int
        """
        self._spot_duration_hours = spot_duration_hours

    @property
    def interruption_policy(self):
        """Gets the interruption_policy of this PrePaidServerExtendParam.

        :return: The interruption_policy of this PrePaidServerExtendParam.
        :rtype: str
        """
        return self._interruption_policy

    @interruption_policy.setter
    def interruption_policy(self, interruption_policy):
        """Sets the interruption_policy of this PrePaidServerExtendParam.

        :param interruption_policy: The interruption_policy of this PrePaidServerExtendParam.
        :type interruption_policy: str
        """
        self._interruption_policy = interruption_policy

    @property
    def spot_duration_count(self):
        """Gets the spot_duration_count of this PrePaidServerExtendParam.

        :return: The spot_duration_count of this PrePaidServerExtendParam.
        :rtype: int
        """
        return self._spot_duration_count

    @spot_duration_count.setter
    def spot_duration_count(self, spot_duration_count):
        """Sets the spot_duration_count of this PrePaidServerExtendParam.

        :param spot_duration_count: The spot_duration_count of this PrePaidServerExtendParam.
        :type spot_duration_count: int
        """
        self._spot_duration_count = spot_duration_count

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
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PrePaidServerExtendParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
