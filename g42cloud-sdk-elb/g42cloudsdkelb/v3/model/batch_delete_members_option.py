# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteMembersOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'address': 'str',
        'protocol_port': 'int'
    }

    attribute_map = {
        'id': 'id',
        'address': 'address',
        'protocol_port': 'protocol_port'
    }

    def __init__(self, id=None, address=None, protocol_port=None):
        """BatchDeleteMembersOption

        The model defined in g42cloud sdk

        :param id: The param of the BatchDeleteMembersOption
        :type id: str
        :param address: The param of the BatchDeleteMembersOption
        :type address: str
        :param protocol_port: The param of the BatchDeleteMembersOption
        :type protocol_port: int
        """
        
        

        self._id = None
        self._address = None
        self._protocol_port = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if address is not None:
            self.address = address
        if protocol_port is not None:
            self.protocol_port = protocol_port

    @property
    def id(self):
        """Gets the id of this BatchDeleteMembersOption.

        :return: The id of this BatchDeleteMembersOption.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BatchDeleteMembersOption.

        :param id: The id of this BatchDeleteMembersOption.
        :type id: str
        """
        self._id = id

    @property
    def address(self):
        """Gets the address of this BatchDeleteMembersOption.

        :return: The address of this BatchDeleteMembersOption.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this BatchDeleteMembersOption.

        :param address: The address of this BatchDeleteMembersOption.
        :type address: str
        """
        self._address = address

    @property
    def protocol_port(self):
        """Gets the protocol_port of this BatchDeleteMembersOption.

        :return: The protocol_port of this BatchDeleteMembersOption.
        :rtype: int
        """
        return self._protocol_port

    @protocol_port.setter
    def protocol_port(self, protocol_port):
        """Sets the protocol_port of this BatchDeleteMembersOption.

        :param protocol_port: The protocol_port of this BatchDeleteMembersOption.
        :type protocol_port: int
        """
        self._protocol_port = protocol_port

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
        if not isinstance(other, BatchDeleteMembersOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
