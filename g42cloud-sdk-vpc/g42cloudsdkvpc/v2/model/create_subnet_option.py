# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSubnetOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'cidr': 'str',
        'vpc_id': 'str',
        'gateway_ip': 'str',
        'ipv6_enable': 'bool',
        'dhcp_enable': 'bool',
        'primary_dns': 'str',
        'secondary_dns': 'str',
        'dns_list': 'list[str]',
        'availability_zone': 'str',
        'extra_dhcp_opts': 'list[ExtraDhcpOption]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'cidr': 'cidr',
        'vpc_id': 'vpc_id',
        'gateway_ip': 'gateway_ip',
        'ipv6_enable': 'ipv6_enable',
        'dhcp_enable': 'dhcp_enable',
        'primary_dns': 'primary_dns',
        'secondary_dns': 'secondary_dns',
        'dns_list': 'dnsList',
        'availability_zone': 'availability_zone',
        'extra_dhcp_opts': 'extra_dhcp_opts'
    }

    def __init__(self, name=None, description=None, cidr=None, vpc_id=None, gateway_ip=None, ipv6_enable=None, dhcp_enable=None, primary_dns=None, secondary_dns=None, dns_list=None, availability_zone=None, extra_dhcp_opts=None):
        """CreateSubnetOption

        The model defined in g42cloud sdk

        :param name: The param of the CreateSubnetOption
        :type name: str
        :param description: The param of the CreateSubnetOption
        :type description: str
        :param cidr: The param of the CreateSubnetOption
        :type cidr: str
        :param vpc_id: The param of the CreateSubnetOption
        :type vpc_id: str
        :param gateway_ip: The param of the CreateSubnetOption
        :type gateway_ip: str
        :param ipv6_enable: The param of the CreateSubnetOption
        :type ipv6_enable: bool
        :param dhcp_enable: The param of the CreateSubnetOption
        :type dhcp_enable: bool
        :param primary_dns: The param of the CreateSubnetOption
        :type primary_dns: str
        :param secondary_dns: The param of the CreateSubnetOption
        :type secondary_dns: str
        :param dns_list: The param of the CreateSubnetOption
        :type dns_list: list[str]
        :param availability_zone: The param of the CreateSubnetOption
        :type availability_zone: str
        :param extra_dhcp_opts: The param of the CreateSubnetOption
        :type extra_dhcp_opts: list[:class:`g42cloudsdkvpc.v2.ExtraDhcpOption`]
        """
        
        

        self._name = None
        self._description = None
        self._cidr = None
        self._vpc_id = None
        self._gateway_ip = None
        self._ipv6_enable = None
        self._dhcp_enable = None
        self._primary_dns = None
        self._secondary_dns = None
        self._dns_list = None
        self._availability_zone = None
        self._extra_dhcp_opts = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.cidr = cidr
        self.vpc_id = vpc_id
        self.gateway_ip = gateway_ip
        if ipv6_enable is not None:
            self.ipv6_enable = ipv6_enable
        if dhcp_enable is not None:
            self.dhcp_enable = dhcp_enable
        if primary_dns is not None:
            self.primary_dns = primary_dns
        if secondary_dns is not None:
            self.secondary_dns = secondary_dns
        if dns_list is not None:
            self.dns_list = dns_list
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if extra_dhcp_opts is not None:
            self.extra_dhcp_opts = extra_dhcp_opts

    @property
    def name(self):
        """Gets the name of this CreateSubnetOption.

        :return: The name of this CreateSubnetOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateSubnetOption.

        :param name: The name of this CreateSubnetOption.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateSubnetOption.

        :return: The description of this CreateSubnetOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateSubnetOption.

        :param description: The description of this CreateSubnetOption.
        :type description: str
        """
        self._description = description

    @property
    def cidr(self):
        """Gets the cidr of this CreateSubnetOption.

        :return: The cidr of this CreateSubnetOption.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this CreateSubnetOption.

        :param cidr: The cidr of this CreateSubnetOption.
        :type cidr: str
        """
        self._cidr = cidr

    @property
    def vpc_id(self):
        """Gets the vpc_id of this CreateSubnetOption.

        :return: The vpc_id of this CreateSubnetOption.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this CreateSubnetOption.

        :param vpc_id: The vpc_id of this CreateSubnetOption.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def gateway_ip(self):
        """Gets the gateway_ip of this CreateSubnetOption.

        :return: The gateway_ip of this CreateSubnetOption.
        :rtype: str
        """
        return self._gateway_ip

    @gateway_ip.setter
    def gateway_ip(self, gateway_ip):
        """Sets the gateway_ip of this CreateSubnetOption.

        :param gateway_ip: The gateway_ip of this CreateSubnetOption.
        :type gateway_ip: str
        """
        self._gateway_ip = gateway_ip

    @property
    def ipv6_enable(self):
        """Gets the ipv6_enable of this CreateSubnetOption.

        :return: The ipv6_enable of this CreateSubnetOption.
        :rtype: bool
        """
        return self._ipv6_enable

    @ipv6_enable.setter
    def ipv6_enable(self, ipv6_enable):
        """Sets the ipv6_enable of this CreateSubnetOption.

        :param ipv6_enable: The ipv6_enable of this CreateSubnetOption.
        :type ipv6_enable: bool
        """
        self._ipv6_enable = ipv6_enable

    @property
    def dhcp_enable(self):
        """Gets the dhcp_enable of this CreateSubnetOption.

        :return: The dhcp_enable of this CreateSubnetOption.
        :rtype: bool
        """
        return self._dhcp_enable

    @dhcp_enable.setter
    def dhcp_enable(self, dhcp_enable):
        """Sets the dhcp_enable of this CreateSubnetOption.

        :param dhcp_enable: The dhcp_enable of this CreateSubnetOption.
        :type dhcp_enable: bool
        """
        self._dhcp_enable = dhcp_enable

    @property
    def primary_dns(self):
        """Gets the primary_dns of this CreateSubnetOption.

        :return: The primary_dns of this CreateSubnetOption.
        :rtype: str
        """
        return self._primary_dns

    @primary_dns.setter
    def primary_dns(self, primary_dns):
        """Sets the primary_dns of this CreateSubnetOption.

        :param primary_dns: The primary_dns of this CreateSubnetOption.
        :type primary_dns: str
        """
        self._primary_dns = primary_dns

    @property
    def secondary_dns(self):
        """Gets the secondary_dns of this CreateSubnetOption.

        :return: The secondary_dns of this CreateSubnetOption.
        :rtype: str
        """
        return self._secondary_dns

    @secondary_dns.setter
    def secondary_dns(self, secondary_dns):
        """Sets the secondary_dns of this CreateSubnetOption.

        :param secondary_dns: The secondary_dns of this CreateSubnetOption.
        :type secondary_dns: str
        """
        self._secondary_dns = secondary_dns

    @property
    def dns_list(self):
        """Gets the dns_list of this CreateSubnetOption.

        :return: The dns_list of this CreateSubnetOption.
        :rtype: list[str]
        """
        return self._dns_list

    @dns_list.setter
    def dns_list(self, dns_list):
        """Sets the dns_list of this CreateSubnetOption.

        :param dns_list: The dns_list of this CreateSubnetOption.
        :type dns_list: list[str]
        """
        self._dns_list = dns_list

    @property
    def availability_zone(self):
        """Gets the availability_zone of this CreateSubnetOption.

        :return: The availability_zone of this CreateSubnetOption.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this CreateSubnetOption.

        :param availability_zone: The availability_zone of this CreateSubnetOption.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def extra_dhcp_opts(self):
        """Gets the extra_dhcp_opts of this CreateSubnetOption.

        :return: The extra_dhcp_opts of this CreateSubnetOption.
        :rtype: list[:class:`g42cloudsdkvpc.v2.ExtraDhcpOption`]
        """
        return self._extra_dhcp_opts

    @extra_dhcp_opts.setter
    def extra_dhcp_opts(self, extra_dhcp_opts):
        """Sets the extra_dhcp_opts of this CreateSubnetOption.

        :param extra_dhcp_opts: The extra_dhcp_opts of this CreateSubnetOption.
        :type extra_dhcp_opts: list[:class:`g42cloudsdkvpc.v2.ExtraDhcpOption`]
        """
        self._extra_dhcp_opts = extra_dhcp_opts

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
        if not isinstance(other, CreateSubnetOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
