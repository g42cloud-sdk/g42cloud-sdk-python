# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePortOption:

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
        'security_groups': 'list[str]',
        'allowed_address_pairs': 'list[AllowedAddressPair]',
        'extra_dhcp_opts': 'list[ExtraDhcpOpt]'
    }

    attribute_map = {
        'name': 'name',
        'security_groups': 'security_groups',
        'allowed_address_pairs': 'allowed_address_pairs',
        'extra_dhcp_opts': 'extra_dhcp_opts'
    }

    def __init__(self, name=None, security_groups=None, allowed_address_pairs=None, extra_dhcp_opts=None):
        """UpdatePortOption

        The model defined in g42cloud sdk

        :param name: The param of the UpdatePortOption
        :type name: str
        :param security_groups: The param of the UpdatePortOption
        :type security_groups: list[str]
        :param allowed_address_pairs: The param of the UpdatePortOption
        :type allowed_address_pairs: list[:class:`g42cloudsdkvpc.v2.AllowedAddressPair`]
        :param extra_dhcp_opts: The param of the UpdatePortOption
        :type extra_dhcp_opts: list[:class:`g42cloudsdkvpc.v2.ExtraDhcpOpt`]
        """
        
        

        self._name = None
        self._security_groups = None
        self._allowed_address_pairs = None
        self._extra_dhcp_opts = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if security_groups is not None:
            self.security_groups = security_groups
        if allowed_address_pairs is not None:
            self.allowed_address_pairs = allowed_address_pairs
        if extra_dhcp_opts is not None:
            self.extra_dhcp_opts = extra_dhcp_opts

    @property
    def name(self):
        """Gets the name of this UpdatePortOption.

        :return: The name of this UpdatePortOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdatePortOption.

        :param name: The name of this UpdatePortOption.
        :type name: str
        """
        self._name = name

    @property
    def security_groups(self):
        """Gets the security_groups of this UpdatePortOption.

        :return: The security_groups of this UpdatePortOption.
        :rtype: list[str]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this UpdatePortOption.

        :param security_groups: The security_groups of this UpdatePortOption.
        :type security_groups: list[str]
        """
        self._security_groups = security_groups

    @property
    def allowed_address_pairs(self):
        """Gets the allowed_address_pairs of this UpdatePortOption.

        :return: The allowed_address_pairs of this UpdatePortOption.
        :rtype: list[:class:`g42cloudsdkvpc.v2.AllowedAddressPair`]
        """
        return self._allowed_address_pairs

    @allowed_address_pairs.setter
    def allowed_address_pairs(self, allowed_address_pairs):
        """Sets the allowed_address_pairs of this UpdatePortOption.

        :param allowed_address_pairs: The allowed_address_pairs of this UpdatePortOption.
        :type allowed_address_pairs: list[:class:`g42cloudsdkvpc.v2.AllowedAddressPair`]
        """
        self._allowed_address_pairs = allowed_address_pairs

    @property
    def extra_dhcp_opts(self):
        """Gets the extra_dhcp_opts of this UpdatePortOption.

        :return: The extra_dhcp_opts of this UpdatePortOption.
        :rtype: list[:class:`g42cloudsdkvpc.v2.ExtraDhcpOpt`]
        """
        return self._extra_dhcp_opts

    @extra_dhcp_opts.setter
    def extra_dhcp_opts(self, extra_dhcp_opts):
        """Sets the extra_dhcp_opts of this UpdatePortOption.

        :param extra_dhcp_opts: The extra_dhcp_opts of this UpdatePortOption.
        :type extra_dhcp_opts: list[:class:`g42cloudsdkvpc.v2.ExtraDhcpOpt`]
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
        if not isinstance(other, UpdatePortOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
