# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EniNetwork:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'eni_subnet_id': 'str',
        'eni_subnet_cidr': 'str',
        'subnets': 'list[NetworkSubnet]'
    }

    attribute_map = {
        'eni_subnet_id': 'eniSubnetId',
        'eni_subnet_cidr': 'eniSubnetCIDR',
        'subnets': 'subnets'
    }

    def __init__(self, eni_subnet_id=None, eni_subnet_cidr=None, subnets=None):
        """EniNetwork

        The model defined in g42cloud sdk

        :param eni_subnet_id: The param of the EniNetwork
        :type eni_subnet_id: str
        :param eni_subnet_cidr: The param of the EniNetwork
        :type eni_subnet_cidr: str
        :param subnets: The param of the EniNetwork
        :type subnets: list[:class:`g42cloudsdkcce.v3.NetworkSubnet`]
        """
        
        

        self._eni_subnet_id = None
        self._eni_subnet_cidr = None
        self._subnets = None
        self.discriminator = None

        self.eni_subnet_id = eni_subnet_id
        self.eni_subnet_cidr = eni_subnet_cidr
        self.subnets = subnets

    @property
    def eni_subnet_id(self):
        """Gets the eni_subnet_id of this EniNetwork.

        :return: The eni_subnet_id of this EniNetwork.
        :rtype: str
        """
        return self._eni_subnet_id

    @eni_subnet_id.setter
    def eni_subnet_id(self, eni_subnet_id):
        """Sets the eni_subnet_id of this EniNetwork.

        :param eni_subnet_id: The eni_subnet_id of this EniNetwork.
        :type eni_subnet_id: str
        """
        self._eni_subnet_id = eni_subnet_id

    @property
    def eni_subnet_cidr(self):
        """Gets the eni_subnet_cidr of this EniNetwork.

        :return: The eni_subnet_cidr of this EniNetwork.
        :rtype: str
        """
        return self._eni_subnet_cidr

    @eni_subnet_cidr.setter
    def eni_subnet_cidr(self, eni_subnet_cidr):
        """Sets the eni_subnet_cidr of this EniNetwork.

        :param eni_subnet_cidr: The eni_subnet_cidr of this EniNetwork.
        :type eni_subnet_cidr: str
        """
        self._eni_subnet_cidr = eni_subnet_cidr

    @property
    def subnets(self):
        """Gets the subnets of this EniNetwork.

        :return: The subnets of this EniNetwork.
        :rtype: list[:class:`g42cloudsdkcce.v3.NetworkSubnet`]
        """
        return self._subnets

    @subnets.setter
    def subnets(self, subnets):
        """Sets the subnets of this EniNetwork.

        :param subnets: The subnets of this EniNetwork.
        :type subnets: list[:class:`g42cloudsdkcce.v3.NetworkSubnet`]
        """
        self._subnets = subnets

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
        if not isinstance(other, EniNetwork):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
