# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NeutronCreateSecurityGroupRuleOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'direction': 'str',
        'ethertype': 'str',
        'port_range_max': 'int',
        'port_range_min': 'int',
        'protocol': 'str',
        'remote_group_id': 'str',
        'remote_ip_prefix': 'str',
        'security_group_id': 'str'
    }

    attribute_map = {
        'description': 'description',
        'direction': 'direction',
        'ethertype': 'ethertype',
        'port_range_max': 'port_range_max',
        'port_range_min': 'port_range_min',
        'protocol': 'protocol',
        'remote_group_id': 'remote_group_id',
        'remote_ip_prefix': 'remote_ip_prefix',
        'security_group_id': 'security_group_id'
    }

    def __init__(self, description=None, direction=None, ethertype=None, port_range_max=None, port_range_min=None, protocol=None, remote_group_id=None, remote_ip_prefix=None, security_group_id=None):
        """NeutronCreateSecurityGroupRuleOption

        The model defined in g42cloud sdk

        :param description: The param of the NeutronCreateSecurityGroupRuleOption
        :type description: str
        :param direction: The param of the NeutronCreateSecurityGroupRuleOption
        :type direction: str
        :param ethertype: The param of the NeutronCreateSecurityGroupRuleOption
        :type ethertype: str
        :param port_range_max: The param of the NeutronCreateSecurityGroupRuleOption
        :type port_range_max: int
        :param port_range_min: The param of the NeutronCreateSecurityGroupRuleOption
        :type port_range_min: int
        :param protocol: The param of the NeutronCreateSecurityGroupRuleOption
        :type protocol: str
        :param remote_group_id: The param of the NeutronCreateSecurityGroupRuleOption
        :type remote_group_id: str
        :param remote_ip_prefix: The param of the NeutronCreateSecurityGroupRuleOption
        :type remote_ip_prefix: str
        :param security_group_id: The param of the NeutronCreateSecurityGroupRuleOption
        :type security_group_id: str
        """
        
        

        self._description = None
        self._direction = None
        self._ethertype = None
        self._port_range_max = None
        self._port_range_min = None
        self._protocol = None
        self._remote_group_id = None
        self._remote_ip_prefix = None
        self._security_group_id = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.direction = direction
        if ethertype is not None:
            self.ethertype = ethertype
        if port_range_max is not None:
            self.port_range_max = port_range_max
        if port_range_min is not None:
            self.port_range_min = port_range_min
        if protocol is not None:
            self.protocol = protocol
        if remote_group_id is not None:
            self.remote_group_id = remote_group_id
        if remote_ip_prefix is not None:
            self.remote_ip_prefix = remote_ip_prefix
        self.security_group_id = security_group_id

    @property
    def description(self):
        """Gets the description of this NeutronCreateSecurityGroupRuleOption.

        :return: The description of this NeutronCreateSecurityGroupRuleOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NeutronCreateSecurityGroupRuleOption.

        :param description: The description of this NeutronCreateSecurityGroupRuleOption.
        :type description: str
        """
        self._description = description

    @property
    def direction(self):
        """Gets the direction of this NeutronCreateSecurityGroupRuleOption.

        :return: The direction of this NeutronCreateSecurityGroupRuleOption.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this NeutronCreateSecurityGroupRuleOption.

        :param direction: The direction of this NeutronCreateSecurityGroupRuleOption.
        :type direction: str
        """
        self._direction = direction

    @property
    def ethertype(self):
        """Gets the ethertype of this NeutronCreateSecurityGroupRuleOption.

        :return: The ethertype of this NeutronCreateSecurityGroupRuleOption.
        :rtype: str
        """
        return self._ethertype

    @ethertype.setter
    def ethertype(self, ethertype):
        """Sets the ethertype of this NeutronCreateSecurityGroupRuleOption.

        :param ethertype: The ethertype of this NeutronCreateSecurityGroupRuleOption.
        :type ethertype: str
        """
        self._ethertype = ethertype

    @property
    def port_range_max(self):
        """Gets the port_range_max of this NeutronCreateSecurityGroupRuleOption.

        :return: The port_range_max of this NeutronCreateSecurityGroupRuleOption.
        :rtype: int
        """
        return self._port_range_max

    @port_range_max.setter
    def port_range_max(self, port_range_max):
        """Sets the port_range_max of this NeutronCreateSecurityGroupRuleOption.

        :param port_range_max: The port_range_max of this NeutronCreateSecurityGroupRuleOption.
        :type port_range_max: int
        """
        self._port_range_max = port_range_max

    @property
    def port_range_min(self):
        """Gets the port_range_min of this NeutronCreateSecurityGroupRuleOption.

        :return: The port_range_min of this NeutronCreateSecurityGroupRuleOption.
        :rtype: int
        """
        return self._port_range_min

    @port_range_min.setter
    def port_range_min(self, port_range_min):
        """Sets the port_range_min of this NeutronCreateSecurityGroupRuleOption.

        :param port_range_min: The port_range_min of this NeutronCreateSecurityGroupRuleOption.
        :type port_range_min: int
        """
        self._port_range_min = port_range_min

    @property
    def protocol(self):
        """Gets the protocol of this NeutronCreateSecurityGroupRuleOption.

        :return: The protocol of this NeutronCreateSecurityGroupRuleOption.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this NeutronCreateSecurityGroupRuleOption.

        :param protocol: The protocol of this NeutronCreateSecurityGroupRuleOption.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def remote_group_id(self):
        """Gets the remote_group_id of this NeutronCreateSecurityGroupRuleOption.

        :return: The remote_group_id of this NeutronCreateSecurityGroupRuleOption.
        :rtype: str
        """
        return self._remote_group_id

    @remote_group_id.setter
    def remote_group_id(self, remote_group_id):
        """Sets the remote_group_id of this NeutronCreateSecurityGroupRuleOption.

        :param remote_group_id: The remote_group_id of this NeutronCreateSecurityGroupRuleOption.
        :type remote_group_id: str
        """
        self._remote_group_id = remote_group_id

    @property
    def remote_ip_prefix(self):
        """Gets the remote_ip_prefix of this NeutronCreateSecurityGroupRuleOption.

        :return: The remote_ip_prefix of this NeutronCreateSecurityGroupRuleOption.
        :rtype: str
        """
        return self._remote_ip_prefix

    @remote_ip_prefix.setter
    def remote_ip_prefix(self, remote_ip_prefix):
        """Sets the remote_ip_prefix of this NeutronCreateSecurityGroupRuleOption.

        :param remote_ip_prefix: The remote_ip_prefix of this NeutronCreateSecurityGroupRuleOption.
        :type remote_ip_prefix: str
        """
        self._remote_ip_prefix = remote_ip_prefix

    @property
    def security_group_id(self):
        """Gets the security_group_id of this NeutronCreateSecurityGroupRuleOption.

        :return: The security_group_id of this NeutronCreateSecurityGroupRuleOption.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this NeutronCreateSecurityGroupRuleOption.

        :param security_group_id: The security_group_id of this NeutronCreateSecurityGroupRuleOption.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

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
        if not isinstance(other, NeutronCreateSecurityGroupRuleOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
