# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class LoadBalancerStatusL7Rule:

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
        'type': 'str',
        'provisioning_status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'provisioning_status': 'provisioning_status'
    }

    def __init__(self, id=None, type=None, provisioning_status=None):
        """LoadBalancerStatusL7Rule

        The model defined in g42cloud sdk

        :param id: The param of the LoadBalancerStatusL7Rule
        :type id: str
        :param type: The param of the LoadBalancerStatusL7Rule
        :type type: str
        :param provisioning_status: The param of the LoadBalancerStatusL7Rule
        :type provisioning_status: str
        """
        
        

        self._id = None
        self._type = None
        self._provisioning_status = None
        self.discriminator = None

        self.id = id
        self.type = type
        self.provisioning_status = provisioning_status

    @property
    def id(self):
        """Gets the id of this LoadBalancerStatusL7Rule.

        :return: The id of this LoadBalancerStatusL7Rule.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LoadBalancerStatusL7Rule.

        :param id: The id of this LoadBalancerStatusL7Rule.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        """Gets the type of this LoadBalancerStatusL7Rule.

        :return: The type of this LoadBalancerStatusL7Rule.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LoadBalancerStatusL7Rule.

        :param type: The type of this LoadBalancerStatusL7Rule.
        :type type: str
        """
        self._type = type

    @property
    def provisioning_status(self):
        """Gets the provisioning_status of this LoadBalancerStatusL7Rule.

        :return: The provisioning_status of this LoadBalancerStatusL7Rule.
        :rtype: str
        """
        return self._provisioning_status

    @provisioning_status.setter
    def provisioning_status(self, provisioning_status):
        """Sets the provisioning_status of this LoadBalancerStatusL7Rule.

        :param provisioning_status: The provisioning_status of this LoadBalancerStatusL7Rule.
        :type provisioning_status: str
        """
        self._provisioning_status = provisioning_status

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
        if not isinstance(other, LoadBalancerStatusL7Rule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
