# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateLoadBalancerBandwidthOption:

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
        'size': 'int',
        'charge_mode': 'str',
        'share_type': 'str',
        'billing_info': 'str',
        'id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'size': 'size',
        'charge_mode': 'charge_mode',
        'share_type': 'share_type',
        'billing_info': 'billing_info',
        'id': 'id'
    }

    def __init__(self, name=None, size=None, charge_mode=None, share_type=None, billing_info=None, id=None):
        """CreateLoadBalancerBandwidthOption

        The model defined in g42cloud sdk

        :param name: The param of the CreateLoadBalancerBandwidthOption
        :type name: str
        :param size: The param of the CreateLoadBalancerBandwidthOption
        :type size: int
        :param charge_mode: The param of the CreateLoadBalancerBandwidthOption
        :type charge_mode: str
        :param share_type: The param of the CreateLoadBalancerBandwidthOption
        :type share_type: str
        :param billing_info: The param of the CreateLoadBalancerBandwidthOption
        :type billing_info: str
        :param id: The param of the CreateLoadBalancerBandwidthOption
        :type id: str
        """
        
        

        self._name = None
        self._size = None
        self._charge_mode = None
        self._share_type = None
        self._billing_info = None
        self._id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if size is not None:
            self.size = size
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if share_type is not None:
            self.share_type = share_type
        if billing_info is not None:
            self.billing_info = billing_info
        if id is not None:
            self.id = id

    @property
    def name(self):
        """Gets the name of this CreateLoadBalancerBandwidthOption.

        :return: The name of this CreateLoadBalancerBandwidthOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateLoadBalancerBandwidthOption.

        :param name: The name of this CreateLoadBalancerBandwidthOption.
        :type name: str
        """
        self._name = name

    @property
    def size(self):
        """Gets the size of this CreateLoadBalancerBandwidthOption.

        :return: The size of this CreateLoadBalancerBandwidthOption.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this CreateLoadBalancerBandwidthOption.

        :param size: The size of this CreateLoadBalancerBandwidthOption.
        :type size: int
        """
        self._size = size

    @property
    def charge_mode(self):
        """Gets the charge_mode of this CreateLoadBalancerBandwidthOption.

        :return: The charge_mode of this CreateLoadBalancerBandwidthOption.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this CreateLoadBalancerBandwidthOption.

        :param charge_mode: The charge_mode of this CreateLoadBalancerBandwidthOption.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def share_type(self):
        """Gets the share_type of this CreateLoadBalancerBandwidthOption.

        :return: The share_type of this CreateLoadBalancerBandwidthOption.
        :rtype: str
        """
        return self._share_type

    @share_type.setter
    def share_type(self, share_type):
        """Sets the share_type of this CreateLoadBalancerBandwidthOption.

        :param share_type: The share_type of this CreateLoadBalancerBandwidthOption.
        :type share_type: str
        """
        self._share_type = share_type

    @property
    def billing_info(self):
        """Gets the billing_info of this CreateLoadBalancerBandwidthOption.

        :return: The billing_info of this CreateLoadBalancerBandwidthOption.
        :rtype: str
        """
        return self._billing_info

    @billing_info.setter
    def billing_info(self, billing_info):
        """Sets the billing_info of this CreateLoadBalancerBandwidthOption.

        :param billing_info: The billing_info of this CreateLoadBalancerBandwidthOption.
        :type billing_info: str
        """
        self._billing_info = billing_info

    @property
    def id(self):
        """Gets the id of this CreateLoadBalancerBandwidthOption.

        :return: The id of this CreateLoadBalancerBandwidthOption.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateLoadBalancerBandwidthOption.

        :param id: The id of this CreateLoadBalancerBandwidthOption.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, CreateLoadBalancerBandwidthOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
