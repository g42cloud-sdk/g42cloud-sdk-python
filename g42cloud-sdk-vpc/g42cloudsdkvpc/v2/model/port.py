# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Port:

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
        'network_id': 'str',
        'admin_state_up': 'bool',
        'mac_address': 'str',
        'fixed_ips': 'list[FixedIp]',
        'device_id': 'str',
        'device_owner': 'str',
        'tenant_id': 'str',
        'status': 'str',
        'security_groups': 'list[str]',
        'allowed_address_pairs': 'list[AllowedAddressPair]',
        'extra_dhcp_opts': 'list[ExtraDhcpOpt]',
        'bindingvnic_type': 'str',
        'dns_assignment': 'list[DnsAssignMent]',
        'dns_name': 'str',
        'bindingvif_details': 'BindingVifDetails',
        'bindingprofile': 'object',
        'instance_id': 'str',
        'instance_type': 'str',
        'port_security_enabled': 'bool',
        'zone_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'network_id': 'network_id',
        'admin_state_up': 'admin_state_up',
        'mac_address': 'mac_address',
        'fixed_ips': 'fixed_ips',
        'device_id': 'device_id',
        'device_owner': 'device_owner',
        'tenant_id': 'tenant_id',
        'status': 'status',
        'security_groups': 'security_groups',
        'allowed_address_pairs': 'allowed_address_pairs',
        'extra_dhcp_opts': 'extra_dhcp_opts',
        'bindingvnic_type': 'binding:vnic_type',
        'dns_assignment': 'dns_assignment',
        'dns_name': 'dns_name',
        'bindingvif_details': 'binding:vif_details',
        'bindingprofile': 'binding:profile',
        'instance_id': 'instance_id',
        'instance_type': 'instance_type',
        'port_security_enabled': 'port_security_enabled',
        'zone_id': 'zone_id'
    }

    def __init__(self, id=None, name=None, network_id=None, admin_state_up=None, mac_address=None, fixed_ips=None, device_id=None, device_owner=None, tenant_id=None, status=None, security_groups=None, allowed_address_pairs=None, extra_dhcp_opts=None, bindingvnic_type=None, dns_assignment=None, dns_name=None, bindingvif_details=None, bindingprofile=None, instance_id=None, instance_type=None, port_security_enabled=None, zone_id=None):
        """Port

        The model defined in g42cloud sdk

        :param id: The param of the Port
        :type id: str
        :param name: The param of the Port
        :type name: str
        :param network_id: The param of the Port
        :type network_id: str
        :param admin_state_up: The param of the Port
        :type admin_state_up: bool
        :param mac_address: The param of the Port
        :type mac_address: str
        :param fixed_ips: The param of the Port
        :type fixed_ips: list[:class:`g42cloudsdkvpc.v2.FixedIp`]
        :param device_id: The param of the Port
        :type device_id: str
        :param device_owner: The param of the Port
        :type device_owner: str
        :param tenant_id: The param of the Port
        :type tenant_id: str
        :param status: The param of the Port
        :type status: str
        :param security_groups: The param of the Port
        :type security_groups: list[str]
        :param allowed_address_pairs: The param of the Port
        :type allowed_address_pairs: list[:class:`g42cloudsdkvpc.v2.AllowedAddressPair`]
        :param extra_dhcp_opts: The param of the Port
        :type extra_dhcp_opts: list[:class:`g42cloudsdkvpc.v2.ExtraDhcpOpt`]
        :param bindingvnic_type: The param of the Port
        :type bindingvnic_type: str
        :param dns_assignment: The param of the Port
        :type dns_assignment: list[:class:`g42cloudsdkvpc.v2.DnsAssignMent`]
        :param dns_name: The param of the Port
        :type dns_name: str
        :param bindingvif_details: The param of the Port
        :type bindingvif_details: :class:`g42cloudsdkvpc.v2.BindingVifDetails`
        :param bindingprofile: The param of the Port
        :type bindingprofile: object
        :param instance_id: The param of the Port
        :type instance_id: str
        :param instance_type: The param of the Port
        :type instance_type: str
        :param port_security_enabled: The param of the Port
        :type port_security_enabled: bool
        :param zone_id: The param of the Port
        :type zone_id: str
        """
        
        

        self._id = None
        self._name = None
        self._network_id = None
        self._admin_state_up = None
        self._mac_address = None
        self._fixed_ips = None
        self._device_id = None
        self._device_owner = None
        self._tenant_id = None
        self._status = None
        self._security_groups = None
        self._allowed_address_pairs = None
        self._extra_dhcp_opts = None
        self._bindingvnic_type = None
        self._dns_assignment = None
        self._dns_name = None
        self._bindingvif_details = None
        self._bindingprofile = None
        self._instance_id = None
        self._instance_type = None
        self._port_security_enabled = None
        self._zone_id = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.network_id = network_id
        self.admin_state_up = admin_state_up
        self.mac_address = mac_address
        self.fixed_ips = fixed_ips
        self.device_id = device_id
        self.device_owner = device_owner
        self.tenant_id = tenant_id
        self.status = status
        self.security_groups = security_groups
        self.allowed_address_pairs = allowed_address_pairs
        self.extra_dhcp_opts = extra_dhcp_opts
        self.bindingvnic_type = bindingvnic_type
        self.dns_assignment = dns_assignment
        self.dns_name = dns_name
        self.bindingvif_details = bindingvif_details
        self.bindingprofile = bindingprofile
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.port_security_enabled = port_security_enabled
        self.zone_id = zone_id

    @property
    def id(self):
        """Gets the id of this Port.

        :return: The id of this Port.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Port.

        :param id: The id of this Port.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this Port.

        :return: The name of this Port.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Port.

        :param name: The name of this Port.
        :type name: str
        """
        self._name = name

    @property
    def network_id(self):
        """Gets the network_id of this Port.

        :return: The network_id of this Port.
        :rtype: str
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id):
        """Sets the network_id of this Port.

        :param network_id: The network_id of this Port.
        :type network_id: str
        """
        self._network_id = network_id

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this Port.

        :return: The admin_state_up of this Port.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this Port.

        :param admin_state_up: The admin_state_up of this Port.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def mac_address(self):
        """Gets the mac_address of this Port.

        :return: The mac_address of this Port.
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this Port.

        :param mac_address: The mac_address of this Port.
        :type mac_address: str
        """
        self._mac_address = mac_address

    @property
    def fixed_ips(self):
        """Gets the fixed_ips of this Port.

        :return: The fixed_ips of this Port.
        :rtype: list[:class:`g42cloudsdkvpc.v2.FixedIp`]
        """
        return self._fixed_ips

    @fixed_ips.setter
    def fixed_ips(self, fixed_ips):
        """Sets the fixed_ips of this Port.

        :param fixed_ips: The fixed_ips of this Port.
        :type fixed_ips: list[:class:`g42cloudsdkvpc.v2.FixedIp`]
        """
        self._fixed_ips = fixed_ips

    @property
    def device_id(self):
        """Gets the device_id of this Port.

        :return: The device_id of this Port.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this Port.

        :param device_id: The device_id of this Port.
        :type device_id: str
        """
        self._device_id = device_id

    @property
    def device_owner(self):
        """Gets the device_owner of this Port.

        :return: The device_owner of this Port.
        :rtype: str
        """
        return self._device_owner

    @device_owner.setter
    def device_owner(self, device_owner):
        """Sets the device_owner of this Port.

        :param device_owner: The device_owner of this Port.
        :type device_owner: str
        """
        self._device_owner = device_owner

    @property
    def tenant_id(self):
        """Gets the tenant_id of this Port.

        :return: The tenant_id of this Port.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this Port.

        :param tenant_id: The tenant_id of this Port.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def status(self):
        """Gets the status of this Port.

        :return: The status of this Port.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Port.

        :param status: The status of this Port.
        :type status: str
        """
        self._status = status

    @property
    def security_groups(self):
        """Gets the security_groups of this Port.

        :return: The security_groups of this Port.
        :rtype: list[str]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this Port.

        :param security_groups: The security_groups of this Port.
        :type security_groups: list[str]
        """
        self._security_groups = security_groups

    @property
    def allowed_address_pairs(self):
        """Gets the allowed_address_pairs of this Port.

        :return: The allowed_address_pairs of this Port.
        :rtype: list[:class:`g42cloudsdkvpc.v2.AllowedAddressPair`]
        """
        return self._allowed_address_pairs

    @allowed_address_pairs.setter
    def allowed_address_pairs(self, allowed_address_pairs):
        """Sets the allowed_address_pairs of this Port.

        :param allowed_address_pairs: The allowed_address_pairs of this Port.
        :type allowed_address_pairs: list[:class:`g42cloudsdkvpc.v2.AllowedAddressPair`]
        """
        self._allowed_address_pairs = allowed_address_pairs

    @property
    def extra_dhcp_opts(self):
        """Gets the extra_dhcp_opts of this Port.

        :return: The extra_dhcp_opts of this Port.
        :rtype: list[:class:`g42cloudsdkvpc.v2.ExtraDhcpOpt`]
        """
        return self._extra_dhcp_opts

    @extra_dhcp_opts.setter
    def extra_dhcp_opts(self, extra_dhcp_opts):
        """Sets the extra_dhcp_opts of this Port.

        :param extra_dhcp_opts: The extra_dhcp_opts of this Port.
        :type extra_dhcp_opts: list[:class:`g42cloudsdkvpc.v2.ExtraDhcpOpt`]
        """
        self._extra_dhcp_opts = extra_dhcp_opts

    @property
    def bindingvnic_type(self):
        """Gets the bindingvnic_type of this Port.

        :return: The bindingvnic_type of this Port.
        :rtype: str
        """
        return self._bindingvnic_type

    @bindingvnic_type.setter
    def bindingvnic_type(self, bindingvnic_type):
        """Sets the bindingvnic_type of this Port.

        :param bindingvnic_type: The bindingvnic_type of this Port.
        :type bindingvnic_type: str
        """
        self._bindingvnic_type = bindingvnic_type

    @property
    def dns_assignment(self):
        """Gets the dns_assignment of this Port.

        :return: The dns_assignment of this Port.
        :rtype: list[:class:`g42cloudsdkvpc.v2.DnsAssignMent`]
        """
        return self._dns_assignment

    @dns_assignment.setter
    def dns_assignment(self, dns_assignment):
        """Sets the dns_assignment of this Port.

        :param dns_assignment: The dns_assignment of this Port.
        :type dns_assignment: list[:class:`g42cloudsdkvpc.v2.DnsAssignMent`]
        """
        self._dns_assignment = dns_assignment

    @property
    def dns_name(self):
        """Gets the dns_name of this Port.

        :return: The dns_name of this Port.
        :rtype: str
        """
        return self._dns_name

    @dns_name.setter
    def dns_name(self, dns_name):
        """Sets the dns_name of this Port.

        :param dns_name: The dns_name of this Port.
        :type dns_name: str
        """
        self._dns_name = dns_name

    @property
    def bindingvif_details(self):
        """Gets the bindingvif_details of this Port.

        :return: The bindingvif_details of this Port.
        :rtype: :class:`g42cloudsdkvpc.v2.BindingVifDetails`
        """
        return self._bindingvif_details

    @bindingvif_details.setter
    def bindingvif_details(self, bindingvif_details):
        """Sets the bindingvif_details of this Port.

        :param bindingvif_details: The bindingvif_details of this Port.
        :type bindingvif_details: :class:`g42cloudsdkvpc.v2.BindingVifDetails`
        """
        self._bindingvif_details = bindingvif_details

    @property
    def bindingprofile(self):
        """Gets the bindingprofile of this Port.

        :return: The bindingprofile of this Port.
        :rtype: object
        """
        return self._bindingprofile

    @bindingprofile.setter
    def bindingprofile(self, bindingprofile):
        """Sets the bindingprofile of this Port.

        :param bindingprofile: The bindingprofile of this Port.
        :type bindingprofile: object
        """
        self._bindingprofile = bindingprofile

    @property
    def instance_id(self):
        """Gets the instance_id of this Port.

        :return: The instance_id of this Port.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this Port.

        :param instance_id: The instance_id of this Port.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_type(self):
        """Gets the instance_type of this Port.

        :return: The instance_type of this Port.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this Port.

        :param instance_type: The instance_type of this Port.
        :type instance_type: str
        """
        self._instance_type = instance_type

    @property
    def port_security_enabled(self):
        """Gets the port_security_enabled of this Port.

        :return: The port_security_enabled of this Port.
        :rtype: bool
        """
        return self._port_security_enabled

    @port_security_enabled.setter
    def port_security_enabled(self, port_security_enabled):
        """Sets the port_security_enabled of this Port.

        :param port_security_enabled: The port_security_enabled of this Port.
        :type port_security_enabled: bool
        """
        self._port_security_enabled = port_security_enabled

    @property
    def zone_id(self):
        """Gets the zone_id of this Port.

        :return: The zone_id of this Port.
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this Port.

        :param zone_id: The zone_id of this Port.
        :type zone_id: str
        """
        self._zone_id = zone_id

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
        if not isinstance(other, Port):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
