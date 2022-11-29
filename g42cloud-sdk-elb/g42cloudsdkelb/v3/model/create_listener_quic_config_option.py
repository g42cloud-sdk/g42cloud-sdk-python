# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateListenerQuicConfigOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'quic_listener_id': 'str',
        'enable_quic_upgrade': 'bool'
    }

    attribute_map = {
        'quic_listener_id': 'quic_listener_id',
        'enable_quic_upgrade': 'enable_quic_upgrade'
    }

    def __init__(self, quic_listener_id=None, enable_quic_upgrade=None):
        """CreateListenerQuicConfigOption

        The model defined in g42cloud sdk

        :param quic_listener_id: The param of the CreateListenerQuicConfigOption
        :type quic_listener_id: str
        :param enable_quic_upgrade: The param of the CreateListenerQuicConfigOption
        :type enable_quic_upgrade: bool
        """
        
        

        self._quic_listener_id = None
        self._enable_quic_upgrade = None
        self.discriminator = None

        self.quic_listener_id = quic_listener_id
        if enable_quic_upgrade is not None:
            self.enable_quic_upgrade = enable_quic_upgrade

    @property
    def quic_listener_id(self):
        """Gets the quic_listener_id of this CreateListenerQuicConfigOption.

        :return: The quic_listener_id of this CreateListenerQuicConfigOption.
        :rtype: str
        """
        return self._quic_listener_id

    @quic_listener_id.setter
    def quic_listener_id(self, quic_listener_id):
        """Sets the quic_listener_id of this CreateListenerQuicConfigOption.

        :param quic_listener_id: The quic_listener_id of this CreateListenerQuicConfigOption.
        :type quic_listener_id: str
        """
        self._quic_listener_id = quic_listener_id

    @property
    def enable_quic_upgrade(self):
        """Gets the enable_quic_upgrade of this CreateListenerQuicConfigOption.

        :return: The enable_quic_upgrade of this CreateListenerQuicConfigOption.
        :rtype: bool
        """
        return self._enable_quic_upgrade

    @enable_quic_upgrade.setter
    def enable_quic_upgrade(self, enable_quic_upgrade):
        """Sets the enable_quic_upgrade of this CreateListenerQuicConfigOption.

        :param enable_quic_upgrade: The enable_quic_upgrade of this CreateListenerQuicConfigOption.
        :type enable_quic_upgrade: bool
        """
        self._enable_quic_upgrade = enable_quic_upgrade

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
        if not isinstance(other, CreateListenerQuicConfigOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
