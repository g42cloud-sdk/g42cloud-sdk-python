# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostPaidServerExtendParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'charging_mode': 'int',
        'region_id': 'str',
        'support_auto_recovery': 'bool',
        'enterprise_project_id': 'str',
        'market_type': 'str',
        'spot_price': 'str',
        'disk_prior': 'str',
        'spot_duration_hours': 'int',
        'interruption_policy': 'str',
        'spot_duration_count': 'int',
        'cb_csbs_backup': 'str'
    }

    attribute_map = {
        'charging_mode': 'chargingMode',
        'region_id': 'regionID',
        'support_auto_recovery': 'support_auto_recovery',
        'enterprise_project_id': 'enterprise_project_id',
        'market_type': 'marketType',
        'spot_price': 'spotPrice',
        'disk_prior': 'diskPrior',
        'spot_duration_hours': 'spot_duration_hours',
        'interruption_policy': 'interruption_policy',
        'spot_duration_count': 'spot_duration_count',
        'cb_csbs_backup': 'CB_CSBS_BACKUP'
    }

    def __init__(self, charging_mode=None, region_id=None, support_auto_recovery=None, enterprise_project_id=None, market_type=None, spot_price=None, disk_prior=None, spot_duration_hours=None, interruption_policy=None, spot_duration_count=None, cb_csbs_backup=None):
        """PostPaidServerExtendParam

        The model defined in g42cloud sdk

        :param charging_mode: The param of the PostPaidServerExtendParam
        :type charging_mode: int
        :param region_id: The param of the PostPaidServerExtendParam
        :type region_id: str
        :param support_auto_recovery: The param of the PostPaidServerExtendParam
        :type support_auto_recovery: bool
        :param enterprise_project_id: The param of the PostPaidServerExtendParam
        :type enterprise_project_id: str
        :param market_type: The param of the PostPaidServerExtendParam
        :type market_type: str
        :param spot_price: The param of the PostPaidServerExtendParam
        :type spot_price: str
        :param disk_prior: The param of the PostPaidServerExtendParam
        :type disk_prior: str
        :param spot_duration_hours: The param of the PostPaidServerExtendParam
        :type spot_duration_hours: int
        :param interruption_policy: The param of the PostPaidServerExtendParam
        :type interruption_policy: str
        :param spot_duration_count: The param of the PostPaidServerExtendParam
        :type spot_duration_count: int
        :param cb_csbs_backup: The param of the PostPaidServerExtendParam
        :type cb_csbs_backup: str
        """
        
        

        self._charging_mode = None
        self._region_id = None
        self._support_auto_recovery = None
        self._enterprise_project_id = None
        self._market_type = None
        self._spot_price = None
        self._disk_prior = None
        self._spot_duration_hours = None
        self._interruption_policy = None
        self._spot_duration_count = None
        self._cb_csbs_backup = None
        self.discriminator = None

        if charging_mode is not None:
            self.charging_mode = charging_mode
        if region_id is not None:
            self.region_id = region_id
        if support_auto_recovery is not None:
            self.support_auto_recovery = support_auto_recovery
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
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
        if cb_csbs_backup is not None:
            self.cb_csbs_backup = cb_csbs_backup

    @property
    def charging_mode(self):
        """Gets the charging_mode of this PostPaidServerExtendParam.

        :return: The charging_mode of this PostPaidServerExtendParam.
        :rtype: int
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        """Sets the charging_mode of this PostPaidServerExtendParam.

        :param charging_mode: The charging_mode of this PostPaidServerExtendParam.
        :type charging_mode: int
        """
        self._charging_mode = charging_mode

    @property
    def region_id(self):
        """Gets the region_id of this PostPaidServerExtendParam.

        :return: The region_id of this PostPaidServerExtendParam.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this PostPaidServerExtendParam.

        :param region_id: The region_id of this PostPaidServerExtendParam.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def support_auto_recovery(self):
        """Gets the support_auto_recovery of this PostPaidServerExtendParam.

        :return: The support_auto_recovery of this PostPaidServerExtendParam.
        :rtype: bool
        """
        return self._support_auto_recovery

    @support_auto_recovery.setter
    def support_auto_recovery(self, support_auto_recovery):
        """Sets the support_auto_recovery of this PostPaidServerExtendParam.

        :param support_auto_recovery: The support_auto_recovery of this PostPaidServerExtendParam.
        :type support_auto_recovery: bool
        """
        self._support_auto_recovery = support_auto_recovery

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this PostPaidServerExtendParam.

        :return: The enterprise_project_id of this PostPaidServerExtendParam.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this PostPaidServerExtendParam.

        :param enterprise_project_id: The enterprise_project_id of this PostPaidServerExtendParam.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def market_type(self):
        """Gets the market_type of this PostPaidServerExtendParam.

        :return: The market_type of this PostPaidServerExtendParam.
        :rtype: str
        """
        return self._market_type

    @market_type.setter
    def market_type(self, market_type):
        """Sets the market_type of this PostPaidServerExtendParam.

        :param market_type: The market_type of this PostPaidServerExtendParam.
        :type market_type: str
        """
        self._market_type = market_type

    @property
    def spot_price(self):
        """Gets the spot_price of this PostPaidServerExtendParam.

        :return: The spot_price of this PostPaidServerExtendParam.
        :rtype: str
        """
        return self._spot_price

    @spot_price.setter
    def spot_price(self, spot_price):
        """Sets the spot_price of this PostPaidServerExtendParam.

        :param spot_price: The spot_price of this PostPaidServerExtendParam.
        :type spot_price: str
        """
        self._spot_price = spot_price

    @property
    def disk_prior(self):
        """Gets the disk_prior of this PostPaidServerExtendParam.

        :return: The disk_prior of this PostPaidServerExtendParam.
        :rtype: str
        """
        return self._disk_prior

    @disk_prior.setter
    def disk_prior(self, disk_prior):
        """Sets the disk_prior of this PostPaidServerExtendParam.

        :param disk_prior: The disk_prior of this PostPaidServerExtendParam.
        :type disk_prior: str
        """
        self._disk_prior = disk_prior

    @property
    def spot_duration_hours(self):
        """Gets the spot_duration_hours of this PostPaidServerExtendParam.

        :return: The spot_duration_hours of this PostPaidServerExtendParam.
        :rtype: int
        """
        return self._spot_duration_hours

    @spot_duration_hours.setter
    def spot_duration_hours(self, spot_duration_hours):
        """Sets the spot_duration_hours of this PostPaidServerExtendParam.

        :param spot_duration_hours: The spot_duration_hours of this PostPaidServerExtendParam.
        :type spot_duration_hours: int
        """
        self._spot_duration_hours = spot_duration_hours

    @property
    def interruption_policy(self):
        """Gets the interruption_policy of this PostPaidServerExtendParam.

        :return: The interruption_policy of this PostPaidServerExtendParam.
        :rtype: str
        """
        return self._interruption_policy

    @interruption_policy.setter
    def interruption_policy(self, interruption_policy):
        """Sets the interruption_policy of this PostPaidServerExtendParam.

        :param interruption_policy: The interruption_policy of this PostPaidServerExtendParam.
        :type interruption_policy: str
        """
        self._interruption_policy = interruption_policy

    @property
    def spot_duration_count(self):
        """Gets the spot_duration_count of this PostPaidServerExtendParam.

        :return: The spot_duration_count of this PostPaidServerExtendParam.
        :rtype: int
        """
        return self._spot_duration_count

    @spot_duration_count.setter
    def spot_duration_count(self, spot_duration_count):
        """Sets the spot_duration_count of this PostPaidServerExtendParam.

        :param spot_duration_count: The spot_duration_count of this PostPaidServerExtendParam.
        :type spot_duration_count: int
        """
        self._spot_duration_count = spot_duration_count

    @property
    def cb_csbs_backup(self):
        """Gets the cb_csbs_backup of this PostPaidServerExtendParam.

        :return: The cb_csbs_backup of this PostPaidServerExtendParam.
        :rtype: str
        """
        return self._cb_csbs_backup

    @cb_csbs_backup.setter
    def cb_csbs_backup(self, cb_csbs_backup):
        """Sets the cb_csbs_backup of this PostPaidServerExtendParam.

        :param cb_csbs_backup: The cb_csbs_backup of this PostPaidServerExtendParam.
        :type cb_csbs_backup: str
        """
        self._cb_csbs_backup = cb_csbs_backup

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
        if not isinstance(other, PostPaidServerExtendParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
