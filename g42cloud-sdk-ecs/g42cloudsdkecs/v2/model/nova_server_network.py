# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class NovaServerNetwork:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'port': 'str',
        'uuid': 'str',
        'fixed_ip': 'str'
    }

    attribute_map = {
        'port': 'port',
        'uuid': 'uuid',
        'fixed_ip': 'fixed_ip'
    }

    def __init__(self, port=None, uuid=None, fixed_ip=None):
        """NovaServerNetwork

        The model defined in g42cloud sdk

        :param port: The param of the NovaServerNetwork
        :type port: str
        :param uuid: The param of the NovaServerNetwork
        :type uuid: str
        :param fixed_ip: The param of the NovaServerNetwork
        :type fixed_ip: str
        """
        
        

        self._port = None
        self._uuid = None
        self._fixed_ip = None
        self.discriminator = None

        if port is not None:
            self.port = port
        if uuid is not None:
            self.uuid = uuid
        if fixed_ip is not None:
            self.fixed_ip = fixed_ip

    @property
    def port(self):
        """Gets the port of this NovaServerNetwork.

        :return: The port of this NovaServerNetwork.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this NovaServerNetwork.

        :param port: The port of this NovaServerNetwork.
        :type port: str
        """
        self._port = port

    @property
    def uuid(self):
        """Gets the uuid of this NovaServerNetwork.

        :return: The uuid of this NovaServerNetwork.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this NovaServerNetwork.

        :param uuid: The uuid of this NovaServerNetwork.
        :type uuid: str
        """
        self._uuid = uuid

    @property
    def fixed_ip(self):
        """Gets the fixed_ip of this NovaServerNetwork.

        :return: The fixed_ip of this NovaServerNetwork.
        :rtype: str
        """
        return self._fixed_ip

    @fixed_ip.setter
    def fixed_ip(self, fixed_ip):
        """Sets the fixed_ip of this NovaServerNetwork.

        :param fixed_ip: The fixed_ip of this NovaServerNetwork.
        :type fixed_ip: str
        """
        self._fixed_ip = fixed_ip

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
        if not isinstance(other, NovaServerNetwork):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
