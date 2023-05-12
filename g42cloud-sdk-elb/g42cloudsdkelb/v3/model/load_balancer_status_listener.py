# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class LoadBalancerStatusListener:

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
        'provisioning_status': 'str',
        'pools': 'list[LoadBalancerStatusPool]',
        'l7policies': 'list[LoadBalancerStatusPolicy]',
        'id': 'str',
        'operating_status': 'str'
    }

    attribute_map = {
        'name': 'name',
        'provisioning_status': 'provisioning_status',
        'pools': 'pools',
        'l7policies': 'l7policies',
        'id': 'id',
        'operating_status': 'operating_status'
    }

    def __init__(self, name=None, provisioning_status=None, pools=None, l7policies=None, id=None, operating_status=None):
        """LoadBalancerStatusListener

        The model defined in g42cloud sdk

        :param name: The param of the LoadBalancerStatusListener
        :type name: str
        :param provisioning_status: The param of the LoadBalancerStatusListener
        :type provisioning_status: str
        :param pools: The param of the LoadBalancerStatusListener
        :type pools: list[:class:`g42cloudsdkelb.v3.LoadBalancerStatusPool`]
        :param l7policies: The param of the LoadBalancerStatusListener
        :type l7policies: list[:class:`g42cloudsdkelb.v3.LoadBalancerStatusPolicy`]
        :param id: The param of the LoadBalancerStatusListener
        :type id: str
        :param operating_status: The param of the LoadBalancerStatusListener
        :type operating_status: str
        """
        
        

        self._name = None
        self._provisioning_status = None
        self._pools = None
        self._l7policies = None
        self._id = None
        self._operating_status = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if provisioning_status is not None:
            self.provisioning_status = provisioning_status
        if pools is not None:
            self.pools = pools
        if l7policies is not None:
            self.l7policies = l7policies
        if id is not None:
            self.id = id
        if operating_status is not None:
            self.operating_status = operating_status

    @property
    def name(self):
        """Gets the name of this LoadBalancerStatusListener.

        :return: The name of this LoadBalancerStatusListener.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LoadBalancerStatusListener.

        :param name: The name of this LoadBalancerStatusListener.
        :type name: str
        """
        self._name = name

    @property
    def provisioning_status(self):
        """Gets the provisioning_status of this LoadBalancerStatusListener.

        :return: The provisioning_status of this LoadBalancerStatusListener.
        :rtype: str
        """
        return self._provisioning_status

    @provisioning_status.setter
    def provisioning_status(self, provisioning_status):
        """Sets the provisioning_status of this LoadBalancerStatusListener.

        :param provisioning_status: The provisioning_status of this LoadBalancerStatusListener.
        :type provisioning_status: str
        """
        self._provisioning_status = provisioning_status

    @property
    def pools(self):
        """Gets the pools of this LoadBalancerStatusListener.

        :return: The pools of this LoadBalancerStatusListener.
        :rtype: list[:class:`g42cloudsdkelb.v3.LoadBalancerStatusPool`]
        """
        return self._pools

    @pools.setter
    def pools(self, pools):
        """Sets the pools of this LoadBalancerStatusListener.

        :param pools: The pools of this LoadBalancerStatusListener.
        :type pools: list[:class:`g42cloudsdkelb.v3.LoadBalancerStatusPool`]
        """
        self._pools = pools

    @property
    def l7policies(self):
        """Gets the l7policies of this LoadBalancerStatusListener.

        :return: The l7policies of this LoadBalancerStatusListener.
        :rtype: list[:class:`g42cloudsdkelb.v3.LoadBalancerStatusPolicy`]
        """
        return self._l7policies

    @l7policies.setter
    def l7policies(self, l7policies):
        """Sets the l7policies of this LoadBalancerStatusListener.

        :param l7policies: The l7policies of this LoadBalancerStatusListener.
        :type l7policies: list[:class:`g42cloudsdkelb.v3.LoadBalancerStatusPolicy`]
        """
        self._l7policies = l7policies

    @property
    def id(self):
        """Gets the id of this LoadBalancerStatusListener.

        :return: The id of this LoadBalancerStatusListener.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LoadBalancerStatusListener.

        :param id: The id of this LoadBalancerStatusListener.
        :type id: str
        """
        self._id = id

    @property
    def operating_status(self):
        """Gets the operating_status of this LoadBalancerStatusListener.

        :return: The operating_status of this LoadBalancerStatusListener.
        :rtype: str
        """
        return self._operating_status

    @operating_status.setter
    def operating_status(self, operating_status):
        """Sets the operating_status of this LoadBalancerStatusListener.

        :param operating_status: The operating_status of this LoadBalancerStatusListener.
        :type operating_status: str
        """
        self._operating_status = operating_status

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
        if not isinstance(other, LoadBalancerStatusListener):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
