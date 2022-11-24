# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NeutronFirewallRule:

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
        'name': 'str',
        'description': 'str',
        'action': 'str',
        'protocol': 'str',
        'ip_version': 'int',
        'enabled': 'bool',
        'public': 'bool',
        'destination_ip_address': 'str',
        'destination_port': 'str',
        'source_ip_address': 'str',
        'source_port': 'str',
        'tenant_id': 'str',
        'project_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'action': 'action',
        'protocol': 'protocol',
        'ip_version': 'ip_version',
        'enabled': 'enabled',
        'public': 'public',
        'destination_ip_address': 'destination_ip_address',
        'destination_port': 'destination_port',
        'source_ip_address': 'source_ip_address',
        'source_port': 'source_port',
        'tenant_id': 'tenant_id',
        'project_id': 'project_id'
    }

    def __init__(self, id=None, name=None, description=None, action=None, protocol=None, ip_version=None, enabled=None, public=None, destination_ip_address=None, destination_port=None, source_ip_address=None, source_port=None, tenant_id=None, project_id=None):
        """NeutronFirewallRule

        The model defined in g42cloud sdk

        :param id: The param of the NeutronFirewallRule
        :type id: str
        :param name: The param of the NeutronFirewallRule
        :type name: str
        :param description: The param of the NeutronFirewallRule
        :type description: str
        :param action: The param of the NeutronFirewallRule
        :type action: str
        :param protocol: The param of the NeutronFirewallRule
        :type protocol: str
        :param ip_version: The param of the NeutronFirewallRule
        :type ip_version: int
        :param enabled: The param of the NeutronFirewallRule
        :type enabled: bool
        :param public: The param of the NeutronFirewallRule
        :type public: bool
        :param destination_ip_address: The param of the NeutronFirewallRule
        :type destination_ip_address: str
        :param destination_port: The param of the NeutronFirewallRule
        :type destination_port: str
        :param source_ip_address: The param of the NeutronFirewallRule
        :type source_ip_address: str
        :param source_port: The param of the NeutronFirewallRule
        :type source_port: str
        :param tenant_id: The param of the NeutronFirewallRule
        :type tenant_id: str
        :param project_id: The param of the NeutronFirewallRule
        :type project_id: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._action = None
        self._protocol = None
        self._ip_version = None
        self._enabled = None
        self._public = None
        self._destination_ip_address = None
        self._destination_port = None
        self._source_ip_address = None
        self._source_port = None
        self._tenant_id = None
        self._project_id = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.description = description
        self.action = action
        self.protocol = protocol
        self.ip_version = ip_version
        self.enabled = enabled
        self.public = public
        self.destination_ip_address = destination_ip_address
        self.destination_port = destination_port
        self.source_ip_address = source_ip_address
        self.source_port = source_port
        self.tenant_id = tenant_id
        self.project_id = project_id

    @property
    def id(self):
        """Gets the id of this NeutronFirewallRule.

        :return: The id of this NeutronFirewallRule.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NeutronFirewallRule.

        :param id: The id of this NeutronFirewallRule.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this NeutronFirewallRule.

        :return: The name of this NeutronFirewallRule.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NeutronFirewallRule.

        :param name: The name of this NeutronFirewallRule.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this NeutronFirewallRule.

        :return: The description of this NeutronFirewallRule.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NeutronFirewallRule.

        :param description: The description of this NeutronFirewallRule.
        :type description: str
        """
        self._description = description

    @property
    def action(self):
        """Gets the action of this NeutronFirewallRule.

        :return: The action of this NeutronFirewallRule.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this NeutronFirewallRule.

        :param action: The action of this NeutronFirewallRule.
        :type action: str
        """
        self._action = action

    @property
    def protocol(self):
        """Gets the protocol of this NeutronFirewallRule.

        :return: The protocol of this NeutronFirewallRule.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this NeutronFirewallRule.

        :param protocol: The protocol of this NeutronFirewallRule.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def ip_version(self):
        """Gets the ip_version of this NeutronFirewallRule.

        :return: The ip_version of this NeutronFirewallRule.
        :rtype: int
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this NeutronFirewallRule.

        :param ip_version: The ip_version of this NeutronFirewallRule.
        :type ip_version: int
        """
        self._ip_version = ip_version

    @property
    def enabled(self):
        """Gets the enabled of this NeutronFirewallRule.

        :return: The enabled of this NeutronFirewallRule.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this NeutronFirewallRule.

        :param enabled: The enabled of this NeutronFirewallRule.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def public(self):
        """Gets the public of this NeutronFirewallRule.

        :return: The public of this NeutronFirewallRule.
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this NeutronFirewallRule.

        :param public: The public of this NeutronFirewallRule.
        :type public: bool
        """
        self._public = public

    @property
    def destination_ip_address(self):
        """Gets the destination_ip_address of this NeutronFirewallRule.

        :return: The destination_ip_address of this NeutronFirewallRule.
        :rtype: str
        """
        return self._destination_ip_address

    @destination_ip_address.setter
    def destination_ip_address(self, destination_ip_address):
        """Sets the destination_ip_address of this NeutronFirewallRule.

        :param destination_ip_address: The destination_ip_address of this NeutronFirewallRule.
        :type destination_ip_address: str
        """
        self._destination_ip_address = destination_ip_address

    @property
    def destination_port(self):
        """Gets the destination_port of this NeutronFirewallRule.

        :return: The destination_port of this NeutronFirewallRule.
        :rtype: str
        """
        return self._destination_port

    @destination_port.setter
    def destination_port(self, destination_port):
        """Sets the destination_port of this NeutronFirewallRule.

        :param destination_port: The destination_port of this NeutronFirewallRule.
        :type destination_port: str
        """
        self._destination_port = destination_port

    @property
    def source_ip_address(self):
        """Gets the source_ip_address of this NeutronFirewallRule.

        :return: The source_ip_address of this NeutronFirewallRule.
        :rtype: str
        """
        return self._source_ip_address

    @source_ip_address.setter
    def source_ip_address(self, source_ip_address):
        """Sets the source_ip_address of this NeutronFirewallRule.

        :param source_ip_address: The source_ip_address of this NeutronFirewallRule.
        :type source_ip_address: str
        """
        self._source_ip_address = source_ip_address

    @property
    def source_port(self):
        """Gets the source_port of this NeutronFirewallRule.

        :return: The source_port of this NeutronFirewallRule.
        :rtype: str
        """
        return self._source_port

    @source_port.setter
    def source_port(self, source_port):
        """Sets the source_port of this NeutronFirewallRule.

        :param source_port: The source_port of this NeutronFirewallRule.
        :type source_port: str
        """
        self._source_port = source_port

    @property
    def tenant_id(self):
        """Gets the tenant_id of this NeutronFirewallRule.

        :return: The tenant_id of this NeutronFirewallRule.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this NeutronFirewallRule.

        :param tenant_id: The tenant_id of this NeutronFirewallRule.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def project_id(self):
        """Gets the project_id of this NeutronFirewallRule.

        :return: The project_id of this NeutronFirewallRule.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this NeutronFirewallRule.

        :param project_id: The project_id of this NeutronFirewallRule.
        :type project_id: str
        """
        self._project_id = project_id

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
        if not isinstance(other, NeutronFirewallRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
