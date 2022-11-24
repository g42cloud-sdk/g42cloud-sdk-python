# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NeutronListSecurityGroupRulesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'marker': 'str',
        'id': 'str',
        'direction': 'str',
        'protocol': 'str',
        'ethertype': 'str',
        'description': 'str',
        'remote_ip_prefix': 'str',
        'remote_group_id': 'str',
        'security_group_id': 'str',
        'port_range_max': 'str',
        'port_range_min': 'str',
        'tenant_id': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'id': 'id',
        'direction': 'direction',
        'protocol': 'protocol',
        'ethertype': 'ethertype',
        'description': 'description',
        'remote_ip_prefix': 'remote_ip_prefix',
        'remote_group_id': 'remote_group_id',
        'security_group_id': 'security_group_id',
        'port_range_max': 'port_range_max',
        'port_range_min': 'port_range_min',
        'tenant_id': 'tenant_id'
    }

    def __init__(self, limit=None, marker=None, id=None, direction=None, protocol=None, ethertype=None, description=None, remote_ip_prefix=None, remote_group_id=None, security_group_id=None, port_range_max=None, port_range_min=None, tenant_id=None):
        """NeutronListSecurityGroupRulesRequest

        The model defined in g42cloud sdk

        :param limit: The param of the NeutronListSecurityGroupRulesRequest
        :type limit: int
        :param marker: The param of the NeutronListSecurityGroupRulesRequest
        :type marker: str
        :param id: The param of the NeutronListSecurityGroupRulesRequest
        :type id: str
        :param direction: The param of the NeutronListSecurityGroupRulesRequest
        :type direction: str
        :param protocol: The param of the NeutronListSecurityGroupRulesRequest
        :type protocol: str
        :param ethertype: The param of the NeutronListSecurityGroupRulesRequest
        :type ethertype: str
        :param description: The param of the NeutronListSecurityGroupRulesRequest
        :type description: str
        :param remote_ip_prefix: The param of the NeutronListSecurityGroupRulesRequest
        :type remote_ip_prefix: str
        :param remote_group_id: The param of the NeutronListSecurityGroupRulesRequest
        :type remote_group_id: str
        :param security_group_id: The param of the NeutronListSecurityGroupRulesRequest
        :type security_group_id: str
        :param port_range_max: The param of the NeutronListSecurityGroupRulesRequest
        :type port_range_max: str
        :param port_range_min: The param of the NeutronListSecurityGroupRulesRequest
        :type port_range_min: str
        :param tenant_id: The param of the NeutronListSecurityGroupRulesRequest
        :type tenant_id: str
        """
        
        

        self._limit = None
        self._marker = None
        self._id = None
        self._direction = None
        self._protocol = None
        self._ethertype = None
        self._description = None
        self._remote_ip_prefix = None
        self._remote_group_id = None
        self._security_group_id = None
        self._port_range_max = None
        self._port_range_min = None
        self._tenant_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if id is not None:
            self.id = id
        if direction is not None:
            self.direction = direction
        if protocol is not None:
            self.protocol = protocol
        if ethertype is not None:
            self.ethertype = ethertype
        if description is not None:
            self.description = description
        if remote_ip_prefix is not None:
            self.remote_ip_prefix = remote_ip_prefix
        if remote_group_id is not None:
            self.remote_group_id = remote_group_id
        if security_group_id is not None:
            self.security_group_id = security_group_id
        if port_range_max is not None:
            self.port_range_max = port_range_max
        if port_range_min is not None:
            self.port_range_min = port_range_min
        if tenant_id is not None:
            self.tenant_id = tenant_id

    @property
    def limit(self):
        """Gets the limit of this NeutronListSecurityGroupRulesRequest.

        :return: The limit of this NeutronListSecurityGroupRulesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this NeutronListSecurityGroupRulesRequest.

        :param limit: The limit of this NeutronListSecurityGroupRulesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this NeutronListSecurityGroupRulesRequest.

        :return: The marker of this NeutronListSecurityGroupRulesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this NeutronListSecurityGroupRulesRequest.

        :param marker: The marker of this NeutronListSecurityGroupRulesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def id(self):
        """Gets the id of this NeutronListSecurityGroupRulesRequest.

        :return: The id of this NeutronListSecurityGroupRulesRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NeutronListSecurityGroupRulesRequest.

        :param id: The id of this NeutronListSecurityGroupRulesRequest.
        :type id: str
        """
        self._id = id

    @property
    def direction(self):
        """Gets the direction of this NeutronListSecurityGroupRulesRequest.

        :return: The direction of this NeutronListSecurityGroupRulesRequest.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this NeutronListSecurityGroupRulesRequest.

        :param direction: The direction of this NeutronListSecurityGroupRulesRequest.
        :type direction: str
        """
        self._direction = direction

    @property
    def protocol(self):
        """Gets the protocol of this NeutronListSecurityGroupRulesRequest.

        :return: The protocol of this NeutronListSecurityGroupRulesRequest.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this NeutronListSecurityGroupRulesRequest.

        :param protocol: The protocol of this NeutronListSecurityGroupRulesRequest.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def ethertype(self):
        """Gets the ethertype of this NeutronListSecurityGroupRulesRequest.

        :return: The ethertype of this NeutronListSecurityGroupRulesRequest.
        :rtype: str
        """
        return self._ethertype

    @ethertype.setter
    def ethertype(self, ethertype):
        """Sets the ethertype of this NeutronListSecurityGroupRulesRequest.

        :param ethertype: The ethertype of this NeutronListSecurityGroupRulesRequest.
        :type ethertype: str
        """
        self._ethertype = ethertype

    @property
    def description(self):
        """Gets the description of this NeutronListSecurityGroupRulesRequest.

        :return: The description of this NeutronListSecurityGroupRulesRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NeutronListSecurityGroupRulesRequest.

        :param description: The description of this NeutronListSecurityGroupRulesRequest.
        :type description: str
        """
        self._description = description

    @property
    def remote_ip_prefix(self):
        """Gets the remote_ip_prefix of this NeutronListSecurityGroupRulesRequest.

        :return: The remote_ip_prefix of this NeutronListSecurityGroupRulesRequest.
        :rtype: str
        """
        return self._remote_ip_prefix

    @remote_ip_prefix.setter
    def remote_ip_prefix(self, remote_ip_prefix):
        """Sets the remote_ip_prefix of this NeutronListSecurityGroupRulesRequest.

        :param remote_ip_prefix: The remote_ip_prefix of this NeutronListSecurityGroupRulesRequest.
        :type remote_ip_prefix: str
        """
        self._remote_ip_prefix = remote_ip_prefix

    @property
    def remote_group_id(self):
        """Gets the remote_group_id of this NeutronListSecurityGroupRulesRequest.

        :return: The remote_group_id of this NeutronListSecurityGroupRulesRequest.
        :rtype: str
        """
        return self._remote_group_id

    @remote_group_id.setter
    def remote_group_id(self, remote_group_id):
        """Sets the remote_group_id of this NeutronListSecurityGroupRulesRequest.

        :param remote_group_id: The remote_group_id of this NeutronListSecurityGroupRulesRequest.
        :type remote_group_id: str
        """
        self._remote_group_id = remote_group_id

    @property
    def security_group_id(self):
        """Gets the security_group_id of this NeutronListSecurityGroupRulesRequest.

        :return: The security_group_id of this NeutronListSecurityGroupRulesRequest.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this NeutronListSecurityGroupRulesRequest.

        :param security_group_id: The security_group_id of this NeutronListSecurityGroupRulesRequest.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def port_range_max(self):
        """Gets the port_range_max of this NeutronListSecurityGroupRulesRequest.

        :return: The port_range_max of this NeutronListSecurityGroupRulesRequest.
        :rtype: str
        """
        return self._port_range_max

    @port_range_max.setter
    def port_range_max(self, port_range_max):
        """Sets the port_range_max of this NeutronListSecurityGroupRulesRequest.

        :param port_range_max: The port_range_max of this NeutronListSecurityGroupRulesRequest.
        :type port_range_max: str
        """
        self._port_range_max = port_range_max

    @property
    def port_range_min(self):
        """Gets the port_range_min of this NeutronListSecurityGroupRulesRequest.

        :return: The port_range_min of this NeutronListSecurityGroupRulesRequest.
        :rtype: str
        """
        return self._port_range_min

    @port_range_min.setter
    def port_range_min(self, port_range_min):
        """Sets the port_range_min of this NeutronListSecurityGroupRulesRequest.

        :param port_range_min: The port_range_min of this NeutronListSecurityGroupRulesRequest.
        :type port_range_min: str
        """
        self._port_range_min = port_range_min

    @property
    def tenant_id(self):
        """Gets the tenant_id of this NeutronListSecurityGroupRulesRequest.

        :return: The tenant_id of this NeutronListSecurityGroupRulesRequest.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this NeutronListSecurityGroupRulesRequest.

        :param tenant_id: The tenant_id of this NeutronListSecurityGroupRulesRequest.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

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
        if not isinstance(other, NeutronListSecurityGroupRulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
