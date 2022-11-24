# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackupStrategyForResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_time': 'str',
        'keep_days': 'int'
    }

    attribute_map = {
        'start_time': 'start_time',
        'keep_days': 'keep_days'
    }

    def __init__(self, start_time=None, keep_days=None):
        """BackupStrategyForResponse

        The model defined in g42cloud sdk

        :param start_time: The param of the BackupStrategyForResponse
        :type start_time: str
        :param keep_days: The param of the BackupStrategyForResponse
        :type keep_days: int
        """
        
        

        self._start_time = None
        self._keep_days = None
        self.discriminator = None

        self.start_time = start_time
        self.keep_days = keep_days

    @property
    def start_time(self):
        """Gets the start_time of this BackupStrategyForResponse.

        :return: The start_time of this BackupStrategyForResponse.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this BackupStrategyForResponse.

        :param start_time: The start_time of this BackupStrategyForResponse.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def keep_days(self):
        """Gets the keep_days of this BackupStrategyForResponse.

        :return: The keep_days of this BackupStrategyForResponse.
        :rtype: int
        """
        return self._keep_days

    @keep_days.setter
    def keep_days(self, keep_days):
        """Sets the keep_days of this BackupStrategyForResponse.

        :param keep_days: The keep_days of this BackupStrategyForResponse.
        :type keep_days: int
        """
        self._keep_days = keep_days

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
        if not isinstance(other, BackupStrategyForResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
