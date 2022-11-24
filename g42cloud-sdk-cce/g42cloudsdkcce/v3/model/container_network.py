# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ContainerNetwork:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'mode': 'str',
        'cidr': 'str',
        'cidrs': 'list[ContainerCIDR]'
    }

    attribute_map = {
        'mode': 'mode',
        'cidr': 'cidr',
        'cidrs': 'cidrs'
    }

    def __init__(self, mode=None, cidr=None, cidrs=None):
        """ContainerNetwork

        The model defined in g42cloud sdk

        :param mode: The param of the ContainerNetwork
        :type mode: str
        :param cidr: The param of the ContainerNetwork
        :type cidr: str
        :param cidrs: The param of the ContainerNetwork
        :type cidrs: list[:class:`g42cloudsdkcce.v3.ContainerCIDR`]
        """
        
        

        self._mode = None
        self._cidr = None
        self._cidrs = None
        self.discriminator = None

        self.mode = mode
        if cidr is not None:
            self.cidr = cidr
        if cidrs is not None:
            self.cidrs = cidrs

    @property
    def mode(self):
        """Gets the mode of this ContainerNetwork.

        :return: The mode of this ContainerNetwork.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this ContainerNetwork.

        :param mode: The mode of this ContainerNetwork.
        :type mode: str
        """
        self._mode = mode

    @property
    def cidr(self):
        """Gets the cidr of this ContainerNetwork.

        :return: The cidr of this ContainerNetwork.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this ContainerNetwork.

        :param cidr: The cidr of this ContainerNetwork.
        :type cidr: str
        """
        self._cidr = cidr

    @property
    def cidrs(self):
        """Gets the cidrs of this ContainerNetwork.

        :return: The cidrs of this ContainerNetwork.
        :rtype: list[:class:`g42cloudsdkcce.v3.ContainerCIDR`]
        """
        return self._cidrs

    @cidrs.setter
    def cidrs(self, cidrs):
        """Sets the cidrs of this ContainerNetwork.

        :param cidrs: The cidrs of this ContainerNetwork.
        :type cidrs: list[:class:`g42cloudsdkcce.v3.ContainerCIDR`]
        """
        self._cidrs = cidrs

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
        if not isinstance(other, ContainerNetwork):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
