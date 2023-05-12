# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmActions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'notification_list': 'list[str]'
    }

    attribute_map = {
        'type': 'type',
        'notification_list': 'notificationList'
    }

    def __init__(self, type=None, notification_list=None):
        """AlarmActions

        The model defined in g42cloud sdk

        :param type: The param of the AlarmActions
        :type type: str
        :param notification_list: The param of the AlarmActions
        :type notification_list: list[str]
        """
        
        

        self._type = None
        self._notification_list = None
        self.discriminator = None

        self.type = type
        self.notification_list = notification_list

    @property
    def type(self):
        """Gets the type of this AlarmActions.

        :return: The type of this AlarmActions.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AlarmActions.

        :param type: The type of this AlarmActions.
        :type type: str
        """
        self._type = type

    @property
    def notification_list(self):
        """Gets the notification_list of this AlarmActions.

        :return: The notification_list of this AlarmActions.
        :rtype: list[str]
        """
        return self._notification_list

    @notification_list.setter
    def notification_list(self, notification_list):
        """Sets the notification_list of this AlarmActions.

        :param notification_list: The notification_list of this AlarmActions.
        :type notification_list: list[str]
        """
        self._notification_list = notification_list

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
        if not isinstance(other, AlarmActions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
