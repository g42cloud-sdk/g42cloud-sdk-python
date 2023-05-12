# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyTriggerPropertiesResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pattern': 'list[str]',
        'start_time': 'str'
    }

    attribute_map = {
        'pattern': 'pattern',
        'start_time': 'start_time'
    }

    def __init__(self, pattern=None, start_time=None):
        """PolicyTriggerPropertiesResp

        The model defined in g42cloud sdk

        :param pattern: The param of the PolicyTriggerPropertiesResp
        :type pattern: list[str]
        :param start_time: The param of the PolicyTriggerPropertiesResp
        :type start_time: str
        """
        
        

        self._pattern = None
        self._start_time = None
        self.discriminator = None

        self.pattern = pattern
        if start_time is not None:
            self.start_time = start_time

    @property
    def pattern(self):
        """Gets the pattern of this PolicyTriggerPropertiesResp.

        :return: The pattern of this PolicyTriggerPropertiesResp.
        :rtype: list[str]
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        """Sets the pattern of this PolicyTriggerPropertiesResp.

        :param pattern: The pattern of this PolicyTriggerPropertiesResp.
        :type pattern: list[str]
        """
        self._pattern = pattern

    @property
    def start_time(self):
        """Gets the start_time of this PolicyTriggerPropertiesResp.

        :return: The start_time of this PolicyTriggerPropertiesResp.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this PolicyTriggerPropertiesResp.

        :param start_time: The start_time of this PolicyTriggerPropertiesResp.
        :type start_time: str
        """
        self._start_time = start_time

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
        if not isinstance(other, PolicyTriggerPropertiesResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
