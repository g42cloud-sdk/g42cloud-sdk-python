# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SourceWithPort:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ip_or_domain': 'str',
        'origin_type': 'str',
        'active_standby': 'int',
        'enable_obs_web_hosting': 'int',
        'http_port': 'int',
        'https_port': 'int'
    }

    attribute_map = {
        'ip_or_domain': 'ip_or_domain',
        'origin_type': 'origin_type',
        'active_standby': 'active_standby',
        'enable_obs_web_hosting': 'enable_obs_web_hosting',
        'http_port': 'http_port',
        'https_port': 'https_port'
    }

    def __init__(self, ip_or_domain=None, origin_type=None, active_standby=None, enable_obs_web_hosting=None, http_port=None, https_port=None):
        """SourceWithPort

        The model defined in g42cloud sdk

        :param ip_or_domain: The param of the SourceWithPort
        :type ip_or_domain: str
        :param origin_type: The param of the SourceWithPort
        :type origin_type: str
        :param active_standby: The param of the SourceWithPort
        :type active_standby: int
        :param enable_obs_web_hosting: The param of the SourceWithPort
        :type enable_obs_web_hosting: int
        :param http_port: The param of the SourceWithPort
        :type http_port: int
        :param https_port: The param of the SourceWithPort
        :type https_port: int
        """
        
        

        self._ip_or_domain = None
        self._origin_type = None
        self._active_standby = None
        self._enable_obs_web_hosting = None
        self._http_port = None
        self._https_port = None
        self.discriminator = None

        self.ip_or_domain = ip_or_domain
        self.origin_type = origin_type
        self.active_standby = active_standby
        if enable_obs_web_hosting is not None:
            self.enable_obs_web_hosting = enable_obs_web_hosting
        if http_port is not None:
            self.http_port = http_port
        if https_port is not None:
            self.https_port = https_port

    @property
    def ip_or_domain(self):
        """Gets the ip_or_domain of this SourceWithPort.

        :return: The ip_or_domain of this SourceWithPort.
        :rtype: str
        """
        return self._ip_or_domain

    @ip_or_domain.setter
    def ip_or_domain(self, ip_or_domain):
        """Sets the ip_or_domain of this SourceWithPort.

        :param ip_or_domain: The ip_or_domain of this SourceWithPort.
        :type ip_or_domain: str
        """
        self._ip_or_domain = ip_or_domain

    @property
    def origin_type(self):
        """Gets the origin_type of this SourceWithPort.

        :return: The origin_type of this SourceWithPort.
        :rtype: str
        """
        return self._origin_type

    @origin_type.setter
    def origin_type(self, origin_type):
        """Sets the origin_type of this SourceWithPort.

        :param origin_type: The origin_type of this SourceWithPort.
        :type origin_type: str
        """
        self._origin_type = origin_type

    @property
    def active_standby(self):
        """Gets the active_standby of this SourceWithPort.

        :return: The active_standby of this SourceWithPort.
        :rtype: int
        """
        return self._active_standby

    @active_standby.setter
    def active_standby(self, active_standby):
        """Sets the active_standby of this SourceWithPort.

        :param active_standby: The active_standby of this SourceWithPort.
        :type active_standby: int
        """
        self._active_standby = active_standby

    @property
    def enable_obs_web_hosting(self):
        """Gets the enable_obs_web_hosting of this SourceWithPort.

        :return: The enable_obs_web_hosting of this SourceWithPort.
        :rtype: int
        """
        return self._enable_obs_web_hosting

    @enable_obs_web_hosting.setter
    def enable_obs_web_hosting(self, enable_obs_web_hosting):
        """Sets the enable_obs_web_hosting of this SourceWithPort.

        :param enable_obs_web_hosting: The enable_obs_web_hosting of this SourceWithPort.
        :type enable_obs_web_hosting: int
        """
        self._enable_obs_web_hosting = enable_obs_web_hosting

    @property
    def http_port(self):
        """Gets the http_port of this SourceWithPort.

        :return: The http_port of this SourceWithPort.
        :rtype: int
        """
        return self._http_port

    @http_port.setter
    def http_port(self, http_port):
        """Sets the http_port of this SourceWithPort.

        :param http_port: The http_port of this SourceWithPort.
        :type http_port: int
        """
        self._http_port = http_port

    @property
    def https_port(self):
        """Gets the https_port of this SourceWithPort.

        :return: The https_port of this SourceWithPort.
        :rtype: int
        """
        return self._https_port

    @https_port.setter
    def https_port(self, https_port):
        """Sets the https_port of this SourceWithPort.

        :param https_port: The https_port of this SourceWithPort.
        :type https_port: int
        """
        self._https_port = https_port

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
        if not isinstance(other, SourceWithPort):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
