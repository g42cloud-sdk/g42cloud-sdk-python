# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NovaSecurityGroupCommonRule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'from_port': 'int',
        'group': 'NovaSecurityGroupCommonGroup',
        'id': 'str',
        'ip_protocol': 'str',
        'ip_range': 'NovaSecurityGroupCommonIpRange',
        'parent_group_id': 'str',
        'to_port': 'int'
    }

    attribute_map = {
        'from_port': 'from_port',
        'group': 'group',
        'id': 'id',
        'ip_protocol': 'ip_protocol',
        'ip_range': 'ip_range',
        'parent_group_id': 'parent_group_id',
        'to_port': 'to_port'
    }

    def __init__(self, from_port=None, group=None, id=None, ip_protocol=None, ip_range=None, parent_group_id=None, to_port=None):
        """NovaSecurityGroupCommonRule

        The model defined in g42cloud sdk

        :param from_port: The param of the NovaSecurityGroupCommonRule
        :type from_port: int
        :param group: The param of the NovaSecurityGroupCommonRule
        :type group: :class:`g42cloudsdkecs.v2.NovaSecurityGroupCommonGroup`
        :param id: The param of the NovaSecurityGroupCommonRule
        :type id: str
        :param ip_protocol: The param of the NovaSecurityGroupCommonRule
        :type ip_protocol: str
        :param ip_range: The param of the NovaSecurityGroupCommonRule
        :type ip_range: :class:`g42cloudsdkecs.v2.NovaSecurityGroupCommonIpRange`
        :param parent_group_id: The param of the NovaSecurityGroupCommonRule
        :type parent_group_id: str
        :param to_port: The param of the NovaSecurityGroupCommonRule
        :type to_port: int
        """
        
        

        self._from_port = None
        self._group = None
        self._id = None
        self._ip_protocol = None
        self._ip_range = None
        self._parent_group_id = None
        self._to_port = None
        self.discriminator = None

        self.from_port = from_port
        self.group = group
        self.id = id
        self.ip_protocol = ip_protocol
        self.ip_range = ip_range
        self.parent_group_id = parent_group_id
        self.to_port = to_port

    @property
    def from_port(self):
        """Gets the from_port of this NovaSecurityGroupCommonRule.

        :return: The from_port of this NovaSecurityGroupCommonRule.
        :rtype: int
        """
        return self._from_port

    @from_port.setter
    def from_port(self, from_port):
        """Sets the from_port of this NovaSecurityGroupCommonRule.

        :param from_port: The from_port of this NovaSecurityGroupCommonRule.
        :type from_port: int
        """
        self._from_port = from_port

    @property
    def group(self):
        """Gets the group of this NovaSecurityGroupCommonRule.

        :return: The group of this NovaSecurityGroupCommonRule.
        :rtype: :class:`g42cloudsdkecs.v2.NovaSecurityGroupCommonGroup`
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this NovaSecurityGroupCommonRule.

        :param group: The group of this NovaSecurityGroupCommonRule.
        :type group: :class:`g42cloudsdkecs.v2.NovaSecurityGroupCommonGroup`
        """
        self._group = group

    @property
    def id(self):
        """Gets the id of this NovaSecurityGroupCommonRule.

        :return: The id of this NovaSecurityGroupCommonRule.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NovaSecurityGroupCommonRule.

        :param id: The id of this NovaSecurityGroupCommonRule.
        :type id: str
        """
        self._id = id

    @property
    def ip_protocol(self):
        """Gets the ip_protocol of this NovaSecurityGroupCommonRule.

        :return: The ip_protocol of this NovaSecurityGroupCommonRule.
        :rtype: str
        """
        return self._ip_protocol

    @ip_protocol.setter
    def ip_protocol(self, ip_protocol):
        """Sets the ip_protocol of this NovaSecurityGroupCommonRule.

        :param ip_protocol: The ip_protocol of this NovaSecurityGroupCommonRule.
        :type ip_protocol: str
        """
        self._ip_protocol = ip_protocol

    @property
    def ip_range(self):
        """Gets the ip_range of this NovaSecurityGroupCommonRule.

        :return: The ip_range of this NovaSecurityGroupCommonRule.
        :rtype: :class:`g42cloudsdkecs.v2.NovaSecurityGroupCommonIpRange`
        """
        return self._ip_range

    @ip_range.setter
    def ip_range(self, ip_range):
        """Sets the ip_range of this NovaSecurityGroupCommonRule.

        :param ip_range: The ip_range of this NovaSecurityGroupCommonRule.
        :type ip_range: :class:`g42cloudsdkecs.v2.NovaSecurityGroupCommonIpRange`
        """
        self._ip_range = ip_range

    @property
    def parent_group_id(self):
        """Gets the parent_group_id of this NovaSecurityGroupCommonRule.

        :return: The parent_group_id of this NovaSecurityGroupCommonRule.
        :rtype: str
        """
        return self._parent_group_id

    @parent_group_id.setter
    def parent_group_id(self, parent_group_id):
        """Sets the parent_group_id of this NovaSecurityGroupCommonRule.

        :param parent_group_id: The parent_group_id of this NovaSecurityGroupCommonRule.
        :type parent_group_id: str
        """
        self._parent_group_id = parent_group_id

    @property
    def to_port(self):
        """Gets the to_port of this NovaSecurityGroupCommonRule.

        :return: The to_port of this NovaSecurityGroupCommonRule.
        :rtype: int
        """
        return self._to_port

    @to_port.setter
    def to_port(self, to_port):
        """Sets the to_port of this NovaSecurityGroupCommonRule.

        :param to_port: The to_port of this NovaSecurityGroupCommonRule.
        :type to_port: int
        """
        self._to_port = to_port

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
        if not isinstance(other, NovaSecurityGroupCommonRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
