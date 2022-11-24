# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchRebootSeversOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'servers': 'list[ServerId]',
        'type': 'str'
    }

    attribute_map = {
        'servers': 'servers',
        'type': 'type'
    }

    def __init__(self, servers=None, type=None):
        """BatchRebootSeversOption

        The model defined in g42cloud sdk

        :param servers: The param of the BatchRebootSeversOption
        :type servers: list[:class:`g42cloudsdkecs.v2.ServerId`]
        :param type: The param of the BatchRebootSeversOption
        :type type: str
        """
        
        

        self._servers = None
        self._type = None
        self.discriminator = None

        self.servers = servers
        self.type = type

    @property
    def servers(self):
        """Gets the servers of this BatchRebootSeversOption.

        :return: The servers of this BatchRebootSeversOption.
        :rtype: list[:class:`g42cloudsdkecs.v2.ServerId`]
        """
        return self._servers

    @servers.setter
    def servers(self, servers):
        """Sets the servers of this BatchRebootSeversOption.

        :param servers: The servers of this BatchRebootSeversOption.
        :type servers: list[:class:`g42cloudsdkecs.v2.ServerId`]
        """
        self._servers = servers

    @property
    def type(self):
        """Gets the type of this BatchRebootSeversOption.

        :return: The type of this BatchRebootSeversOption.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BatchRebootSeversOption.

        :param type: The type of this BatchRebootSeversOption.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, BatchRebootSeversOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
