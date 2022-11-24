# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HostNetwork:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vpc': 'str',
        'subnet': 'str',
        'security_group': 'str'
    }

    attribute_map = {
        'vpc': 'vpc',
        'subnet': 'subnet',
        'security_group': 'SecurityGroup'
    }

    def __init__(self, vpc=None, subnet=None, security_group=None):
        """HostNetwork

        The model defined in g42cloud sdk

        :param vpc: The param of the HostNetwork
        :type vpc: str
        :param subnet: The param of the HostNetwork
        :type subnet: str
        :param security_group: The param of the HostNetwork
        :type security_group: str
        """
        
        

        self._vpc = None
        self._subnet = None
        self._security_group = None
        self.discriminator = None

        self.vpc = vpc
        self.subnet = subnet
        if security_group is not None:
            self.security_group = security_group

    @property
    def vpc(self):
        """Gets the vpc of this HostNetwork.

        :return: The vpc of this HostNetwork.
        :rtype: str
        """
        return self._vpc

    @vpc.setter
    def vpc(self, vpc):
        """Sets the vpc of this HostNetwork.

        :param vpc: The vpc of this HostNetwork.
        :type vpc: str
        """
        self._vpc = vpc

    @property
    def subnet(self):
        """Gets the subnet of this HostNetwork.

        :return: The subnet of this HostNetwork.
        :rtype: str
        """
        return self._subnet

    @subnet.setter
    def subnet(self, subnet):
        """Sets the subnet of this HostNetwork.

        :param subnet: The subnet of this HostNetwork.
        :type subnet: str
        """
        self._subnet = subnet

    @property
    def security_group(self):
        """Gets the security_group of this HostNetwork.

        :return: The security_group of this HostNetwork.
        :rtype: str
        """
        return self._security_group

    @security_group.setter
    def security_group(self, security_group):
        """Sets the security_group of this HostNetwork.

        :param security_group: The security_group of this HostNetwork.
        :type security_group: str
        """
        self._security_group = security_group

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
        if not isinstance(other, HostNetwork):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
