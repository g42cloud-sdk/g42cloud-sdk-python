# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSubnetOption:

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
        'ipv6_enable': 'bool',
        'dhcp_enable': 'bool',
        'primary_dns': 'str',
        'secondary_dns': 'str',
        'dns_list': 'list[str]',
        'extra_dhcp_opts': 'list[ExtraDhcpOption]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'ipv6_enable': 'ipv6_enable',
        'dhcp_enable': 'dhcp_enable',
        'primary_dns': 'primary_dns',
        'secondary_dns': 'secondary_dns',
        'dns_list': 'dnsList',
        'extra_dhcp_opts': 'extra_dhcp_opts'
    }

    def __init__(self, name=None, description=None, ipv6_enable=None, dhcp_enable=None, primary_dns=None, secondary_dns=None, dns_list=None, extra_dhcp_opts=None):
        """UpdateSubnetOption

        The model defined in g42cloud sdk

        :param name: The param of the UpdateSubnetOption
        :type name: str
        :param description: The param of the UpdateSubnetOption
        :type description: str
        :param ipv6_enable: The param of the UpdateSubnetOption
        :type ipv6_enable: bool
        :param dhcp_enable: The param of the UpdateSubnetOption
        :type dhcp_enable: bool
        :param primary_dns: The param of the UpdateSubnetOption
        :type primary_dns: str
        :param secondary_dns: The param of the UpdateSubnetOption
        :type secondary_dns: str
        :param dns_list: The param of the UpdateSubnetOption
        :type dns_list: list[str]
        :param extra_dhcp_opts: The param of the UpdateSubnetOption
        :type extra_dhcp_opts: list[:class:`g42cloudsdkvpc.v2.ExtraDhcpOption`]
        """
        
        

        self._name = None
        self._description = None
        self._ipv6_enable = None
        self._dhcp_enable = None
        self._primary_dns = None
        self._secondary_dns = None
        self._dns_list = None
        self._extra_dhcp_opts = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
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
        if extra_dhcp_opts is not None:
            self.extra_dhcp_opts = extra_dhcp_opts

    @property
    def name(self):
        """Gets the name of this UpdateSubnetOption.

        :return: The name of this UpdateSubnetOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateSubnetOption.

        :param name: The name of this UpdateSubnetOption.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateSubnetOption.

        :return: The description of this UpdateSubnetOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateSubnetOption.

        :param description: The description of this UpdateSubnetOption.
        :type description: str
        """
        self._description = description

    @property
    def ipv6_enable(self):
        """Gets the ipv6_enable of this UpdateSubnetOption.

        :return: The ipv6_enable of this UpdateSubnetOption.
        :rtype: bool
        """
        return self._ipv6_enable

    @ipv6_enable.setter
    def ipv6_enable(self, ipv6_enable):
        """Sets the ipv6_enable of this UpdateSubnetOption.

        :param ipv6_enable: The ipv6_enable of this UpdateSubnetOption.
        :type ipv6_enable: bool
        """
        self._ipv6_enable = ipv6_enable

    @property
    def dhcp_enable(self):
        """Gets the dhcp_enable of this UpdateSubnetOption.

        :return: The dhcp_enable of this UpdateSubnetOption.
        :rtype: bool
        """
        return self._dhcp_enable

    @dhcp_enable.setter
    def dhcp_enable(self, dhcp_enable):
        """Sets the dhcp_enable of this UpdateSubnetOption.

        :param dhcp_enable: The dhcp_enable of this UpdateSubnetOption.
        :type dhcp_enable: bool
        """
        self._dhcp_enable = dhcp_enable

    @property
    def primary_dns(self):
        """Gets the primary_dns of this UpdateSubnetOption.

        :return: The primary_dns of this UpdateSubnetOption.
        :rtype: str
        """
        return self._primary_dns

    @primary_dns.setter
    def primary_dns(self, primary_dns):
        """Sets the primary_dns of this UpdateSubnetOption.

        :param primary_dns: The primary_dns of this UpdateSubnetOption.
        :type primary_dns: str
        """
        self._primary_dns = primary_dns

    @property
    def secondary_dns(self):
        """Gets the secondary_dns of this UpdateSubnetOption.

        :return: The secondary_dns of this UpdateSubnetOption.
        :rtype: str
        """
        return self._secondary_dns

    @secondary_dns.setter
    def secondary_dns(self, secondary_dns):
        """Sets the secondary_dns of this UpdateSubnetOption.

        :param secondary_dns: The secondary_dns of this UpdateSubnetOption.
        :type secondary_dns: str
        """
        self._secondary_dns = secondary_dns

    @property
    def dns_list(self):
        """Gets the dns_list of this UpdateSubnetOption.

        :return: The dns_list of this UpdateSubnetOption.
        :rtype: list[str]
        """
        return self._dns_list

    @dns_list.setter
    def dns_list(self, dns_list):
        """Sets the dns_list of this UpdateSubnetOption.

        :param dns_list: The dns_list of this UpdateSubnetOption.
        :type dns_list: list[str]
        """
        self._dns_list = dns_list

    @property
    def extra_dhcp_opts(self):
        """Gets the extra_dhcp_opts of this UpdateSubnetOption.

        :return: The extra_dhcp_opts of this UpdateSubnetOption.
        :rtype: list[:class:`g42cloudsdkvpc.v2.ExtraDhcpOption`]
        """
        return self._extra_dhcp_opts

    @extra_dhcp_opts.setter
    def extra_dhcp_opts(self, extra_dhcp_opts):
        """Sets the extra_dhcp_opts of this UpdateSubnetOption.

        :param extra_dhcp_opts: The extra_dhcp_opts of this UpdateSubnetOption.
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
        if not isinstance(other, UpdateSubnetOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
