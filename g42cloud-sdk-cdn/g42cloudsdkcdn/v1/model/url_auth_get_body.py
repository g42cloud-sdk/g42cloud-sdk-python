# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UrlAuthGetBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'type': 'str',
        'time_format': 'str',
        'expire_time': 'int'
    }

    attribute_map = {
        'status': 'status',
        'type': 'type',
        'time_format': 'time_format',
        'expire_time': 'expire_time'
    }

    def __init__(self, status=None, type=None, time_format=None, expire_time=None):
        """UrlAuthGetBody

        The model defined in g42cloud sdk

        :param status: The param of the UrlAuthGetBody
        :type status: str
        :param type: The param of the UrlAuthGetBody
        :type type: str
        :param time_format: The param of the UrlAuthGetBody
        :type time_format: str
        :param expire_time: The param of the UrlAuthGetBody
        :type expire_time: int
        """
        
        

        self._status = None
        self._type = None
        self._time_format = None
        self._expire_time = None
        self.discriminator = None

        self.status = status
        if type is not None:
            self.type = type
        if time_format is not None:
            self.time_format = time_format
        if expire_time is not None:
            self.expire_time = expire_time

    @property
    def status(self):
        """Gets the status of this UrlAuthGetBody.

        :return: The status of this UrlAuthGetBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UrlAuthGetBody.

        :param status: The status of this UrlAuthGetBody.
        :type status: str
        """
        self._status = status

    @property
    def type(self):
        """Gets the type of this UrlAuthGetBody.

        :return: The type of this UrlAuthGetBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UrlAuthGetBody.

        :param type: The type of this UrlAuthGetBody.
        :type type: str
        """
        self._type = type

    @property
    def time_format(self):
        """Gets the time_format of this UrlAuthGetBody.

        :return: The time_format of this UrlAuthGetBody.
        :rtype: str
        """
        return self._time_format

    @time_format.setter
    def time_format(self, time_format):
        """Sets the time_format of this UrlAuthGetBody.

        :param time_format: The time_format of this UrlAuthGetBody.
        :type time_format: str
        """
        self._time_format = time_format

    @property
    def expire_time(self):
        """Gets the expire_time of this UrlAuthGetBody.

        :return: The expire_time of this UrlAuthGetBody.
        :rtype: int
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this UrlAuthGetBody.

        :param expire_time: The expire_time of this UrlAuthGetBody.
        :type expire_time: int
        """
        self._expire_time = expire_time

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
        if not isinstance(other, UrlAuthGetBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
