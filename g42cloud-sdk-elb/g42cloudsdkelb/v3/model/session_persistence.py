# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class SessionPersistence:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cookie_name': 'str',
        'type': 'str',
        'persistence_timeout': 'int'
    }

    attribute_map = {
        'cookie_name': 'cookie_name',
        'type': 'type',
        'persistence_timeout': 'persistence_timeout'
    }

    def __init__(self, cookie_name=None, type=None, persistence_timeout=None):
        """SessionPersistence

        The model defined in g42cloud sdk

        :param cookie_name: The param of the SessionPersistence
        :type cookie_name: str
        :param type: The param of the SessionPersistence
        :type type: str
        :param persistence_timeout: The param of the SessionPersistence
        :type persistence_timeout: int
        """
        
        

        self._cookie_name = None
        self._type = None
        self._persistence_timeout = None
        self.discriminator = None

        if cookie_name is not None:
            self.cookie_name = cookie_name
        self.type = type
        if persistence_timeout is not None:
            self.persistence_timeout = persistence_timeout

    @property
    def cookie_name(self):
        """Gets the cookie_name of this SessionPersistence.

        :return: The cookie_name of this SessionPersistence.
        :rtype: str
        """
        return self._cookie_name

    @cookie_name.setter
    def cookie_name(self, cookie_name):
        """Sets the cookie_name of this SessionPersistence.

        :param cookie_name: The cookie_name of this SessionPersistence.
        :type cookie_name: str
        """
        self._cookie_name = cookie_name

    @property
    def type(self):
        """Gets the type of this SessionPersistence.

        :return: The type of this SessionPersistence.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SessionPersistence.

        :param type: The type of this SessionPersistence.
        :type type: str
        """
        self._type = type

    @property
    def persistence_timeout(self):
        """Gets the persistence_timeout of this SessionPersistence.

        :return: The persistence_timeout of this SessionPersistence.
        :rtype: int
        """
        return self._persistence_timeout

    @persistence_timeout.setter
    def persistence_timeout(self, persistence_timeout):
        """Sets the persistence_timeout of this SessionPersistence.

        :param persistence_timeout: The persistence_timeout of this SessionPersistence.
        :type persistence_timeout: int
        """
        self._persistence_timeout = persistence_timeout

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
        if not isinstance(other, SessionPersistence):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
