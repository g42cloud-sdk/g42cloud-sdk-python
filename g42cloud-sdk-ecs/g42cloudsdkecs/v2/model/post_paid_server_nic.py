# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostPaidServerNic:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'subnet_id': 'str',
        'ip_address': 'str',
        'ipv6_enable': 'bool',
        'ipv6_bandwidth': 'PostPaidServerIpv6Bandwidth'
    }

    attribute_map = {
        'subnet_id': 'subnet_id',
        'ip_address': 'ip_address',
        'ipv6_enable': 'ipv6_enable',
        'ipv6_bandwidth': 'ipv6_bandwidth'
    }

    def __init__(self, subnet_id=None, ip_address=None, ipv6_enable=None, ipv6_bandwidth=None):
        """PostPaidServerNic

        The model defined in g42cloud sdk

        :param subnet_id: The param of the PostPaidServerNic
        :type subnet_id: str
        :param ip_address: The param of the PostPaidServerNic
        :type ip_address: str
        :param ipv6_enable: The param of the PostPaidServerNic
        :type ipv6_enable: bool
        :param ipv6_bandwidth: The param of the PostPaidServerNic
        :type ipv6_bandwidth: :class:`g42cloudsdkecs.v2.PostPaidServerIpv6Bandwidth`
        """
        
        

        self._subnet_id = None
        self._ip_address = None
        self._ipv6_enable = None
        self._ipv6_bandwidth = None
        self.discriminator = None

        self.subnet_id = subnet_id
        if ip_address is not None:
            self.ip_address = ip_address
        if ipv6_enable is not None:
            self.ipv6_enable = ipv6_enable
        if ipv6_bandwidth is not None:
            self.ipv6_bandwidth = ipv6_bandwidth

    @property
    def subnet_id(self):
        """Gets the subnet_id of this PostPaidServerNic.

        :return: The subnet_id of this PostPaidServerNic.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this PostPaidServerNic.

        :param subnet_id: The subnet_id of this PostPaidServerNic.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def ip_address(self):
        """Gets the ip_address of this PostPaidServerNic.

        :return: The ip_address of this PostPaidServerNic.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this PostPaidServerNic.

        :param ip_address: The ip_address of this PostPaidServerNic.
        :type ip_address: str
        """
        self._ip_address = ip_address

    @property
    def ipv6_enable(self):
        """Gets the ipv6_enable of this PostPaidServerNic.

        :return: The ipv6_enable of this PostPaidServerNic.
        :rtype: bool
        """
        return self._ipv6_enable

    @ipv6_enable.setter
    def ipv6_enable(self, ipv6_enable):
        """Sets the ipv6_enable of this PostPaidServerNic.

        :param ipv6_enable: The ipv6_enable of this PostPaidServerNic.
        :type ipv6_enable: bool
        """
        self._ipv6_enable = ipv6_enable

    @property
    def ipv6_bandwidth(self):
        """Gets the ipv6_bandwidth of this PostPaidServerNic.

        :return: The ipv6_bandwidth of this PostPaidServerNic.
        :rtype: :class:`g42cloudsdkecs.v2.PostPaidServerIpv6Bandwidth`
        """
        return self._ipv6_bandwidth

    @ipv6_bandwidth.setter
    def ipv6_bandwidth(self, ipv6_bandwidth):
        """Sets the ipv6_bandwidth of this PostPaidServerNic.

        :param ipv6_bandwidth: The ipv6_bandwidth of this PostPaidServerNic.
        :type ipv6_bandwidth: :class:`g42cloudsdkecs.v2.PostPaidServerIpv6Bandwidth`
        """
        self._ipv6_bandwidth = ipv6_bandwidth

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
        if not isinstance(other, PostPaidServerNic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
