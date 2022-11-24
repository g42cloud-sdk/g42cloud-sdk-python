# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResetServerPasswordOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'new_password': 'str',
        'is_check_password': 'bool'
    }

    attribute_map = {
        'new_password': 'new_password',
        'is_check_password': 'is_check_password'
    }

    def __init__(self, new_password=None, is_check_password=None):
        """ResetServerPasswordOption

        The model defined in g42cloud sdk

        :param new_password: The param of the ResetServerPasswordOption
        :type new_password: str
        :param is_check_password: The param of the ResetServerPasswordOption
        :type is_check_password: bool
        """
        
        

        self._new_password = None
        self._is_check_password = None
        self.discriminator = None

        self.new_password = new_password
        if is_check_password is not None:
            self.is_check_password = is_check_password

    @property
    def new_password(self):
        """Gets the new_password of this ResetServerPasswordOption.

        :return: The new_password of this ResetServerPasswordOption.
        :rtype: str
        """
        return self._new_password

    @new_password.setter
    def new_password(self, new_password):
        """Sets the new_password of this ResetServerPasswordOption.

        :param new_password: The new_password of this ResetServerPasswordOption.
        :type new_password: str
        """
        self._new_password = new_password

    @property
    def is_check_password(self):
        """Gets the is_check_password of this ResetServerPasswordOption.

        :return: The is_check_password of this ResetServerPasswordOption.
        :rtype: bool
        """
        return self._is_check_password

    @is_check_password.setter
    def is_check_password(self, is_check_password):
        """Sets the is_check_password of this ResetServerPasswordOption.

        :param is_check_password: The is_check_password of this ResetServerPasswordOption.
        :type is_check_password: bool
        """
        self._is_check_password = is_check_password

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
        if not isinstance(other, ResetServerPasswordOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
