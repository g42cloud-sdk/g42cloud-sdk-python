# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrepaidChangeChargeModeOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'include_publicip': 'bool',
        'period_type': 'str',
        'period_num': 'int',
        'auto_renew': 'bool',
        'auto_pay': 'bool'
    }

    attribute_map = {
        'include_publicip': 'include_publicip',
        'period_type': 'period_type',
        'period_num': 'period_num',
        'auto_renew': 'auto_renew',
        'auto_pay': 'auto_pay'
    }

    def __init__(self, include_publicip=None, period_type=None, period_num=None, auto_renew=None, auto_pay=None):
        """PrepaidChangeChargeModeOption

        The model defined in g42cloud sdk

        :param include_publicip: The param of the PrepaidChangeChargeModeOption
        :type include_publicip: bool
        :param period_type: The param of the PrepaidChangeChargeModeOption
        :type period_type: str
        :param period_num: The param of the PrepaidChangeChargeModeOption
        :type period_num: int
        :param auto_renew: The param of the PrepaidChangeChargeModeOption
        :type auto_renew: bool
        :param auto_pay: The param of the PrepaidChangeChargeModeOption
        :type auto_pay: bool
        """
        
        

        self._include_publicip = None
        self._period_type = None
        self._period_num = None
        self._auto_renew = None
        self._auto_pay = None
        self.discriminator = None

        if include_publicip is not None:
            self.include_publicip = include_publicip
        self.period_type = period_type
        if period_num is not None:
            self.period_num = period_num
        if auto_renew is not None:
            self.auto_renew = auto_renew
        if auto_pay is not None:
            self.auto_pay = auto_pay

    @property
    def include_publicip(self):
        """Gets the include_publicip of this PrepaidChangeChargeModeOption.

        :return: The include_publicip of this PrepaidChangeChargeModeOption.
        :rtype: bool
        """
        return self._include_publicip

    @include_publicip.setter
    def include_publicip(self, include_publicip):
        """Sets the include_publicip of this PrepaidChangeChargeModeOption.

        :param include_publicip: The include_publicip of this PrepaidChangeChargeModeOption.
        :type include_publicip: bool
        """
        self._include_publicip = include_publicip

    @property
    def period_type(self):
        """Gets the period_type of this PrepaidChangeChargeModeOption.

        :return: The period_type of this PrepaidChangeChargeModeOption.
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        """Sets the period_type of this PrepaidChangeChargeModeOption.

        :param period_type: The period_type of this PrepaidChangeChargeModeOption.
        :type period_type: str
        """
        self._period_type = period_type

    @property
    def period_num(self):
        """Gets the period_num of this PrepaidChangeChargeModeOption.

        :return: The period_num of this PrepaidChangeChargeModeOption.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        """Sets the period_num of this PrepaidChangeChargeModeOption.

        :param period_num: The period_num of this PrepaidChangeChargeModeOption.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def auto_renew(self):
        """Gets the auto_renew of this PrepaidChangeChargeModeOption.

        :return: The auto_renew of this PrepaidChangeChargeModeOption.
        :rtype: bool
        """
        return self._auto_renew

    @auto_renew.setter
    def auto_renew(self, auto_renew):
        """Sets the auto_renew of this PrepaidChangeChargeModeOption.

        :param auto_renew: The auto_renew of this PrepaidChangeChargeModeOption.
        :type auto_renew: bool
        """
        self._auto_renew = auto_renew

    @property
    def auto_pay(self):
        """Gets the auto_pay of this PrepaidChangeChargeModeOption.

        :return: The auto_pay of this PrepaidChangeChargeModeOption.
        :rtype: bool
        """
        return self._auto_pay

    @auto_pay.setter
    def auto_pay(self, auto_pay):
        """Sets the auto_pay of this PrepaidChangeChargeModeOption.

        :param auto_pay: The auto_pay of this PrepaidChangeChargeModeOption.
        :type auto_pay: bool
        """
        self._auto_pay = auto_pay

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
        if not isinstance(other, PrepaidChangeChargeModeOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
