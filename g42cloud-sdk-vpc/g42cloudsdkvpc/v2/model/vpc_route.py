# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VpcRoute:

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
        'destination': 'str',
        'nexthop': 'str',
        'type': 'str',
        'vpc_id': 'str',
        'tenant_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'destination': 'destination',
        'nexthop': 'nexthop',
        'type': 'type',
        'vpc_id': 'vpc_id',
        'tenant_id': 'tenant_id'
    }

    def __init__(self, id=None, destination=None, nexthop=None, type=None, vpc_id=None, tenant_id=None):
        """VpcRoute

        The model defined in g42cloud sdk

        :param id: The param of the VpcRoute
        :type id: str
        :param destination: The param of the VpcRoute
        :type destination: str
        :param nexthop: The param of the VpcRoute
        :type nexthop: str
        :param type: The param of the VpcRoute
        :type type: str
        :param vpc_id: The param of the VpcRoute
        :type vpc_id: str
        :param tenant_id: The param of the VpcRoute
        :type tenant_id: str
        """
        
        

        self._id = None
        self._destination = None
        self._nexthop = None
        self._type = None
        self._vpc_id = None
        self._tenant_id = None
        self.discriminator = None

        self.id = id
        self.destination = destination
        self.nexthop = nexthop
        self.type = type
        self.vpc_id = vpc_id
        self.tenant_id = tenant_id

    @property
    def id(self):
        """Gets the id of this VpcRoute.

        :return: The id of this VpcRoute.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VpcRoute.

        :param id: The id of this VpcRoute.
        :type id: str
        """
        self._id = id

    @property
    def destination(self):
        """Gets the destination of this VpcRoute.

        :return: The destination of this VpcRoute.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this VpcRoute.

        :param destination: The destination of this VpcRoute.
        :type destination: str
        """
        self._destination = destination

    @property
    def nexthop(self):
        """Gets the nexthop of this VpcRoute.

        :return: The nexthop of this VpcRoute.
        :rtype: str
        """
        return self._nexthop

    @nexthop.setter
    def nexthop(self, nexthop):
        """Sets the nexthop of this VpcRoute.

        :param nexthop: The nexthop of this VpcRoute.
        :type nexthop: str
        """
        self._nexthop = nexthop

    @property
    def type(self):
        """Gets the type of this VpcRoute.

        :return: The type of this VpcRoute.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VpcRoute.

        :param type: The type of this VpcRoute.
        :type type: str
        """
        self._type = type

    @property
    def vpc_id(self):
        """Gets the vpc_id of this VpcRoute.

        :return: The vpc_id of this VpcRoute.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this VpcRoute.

        :param vpc_id: The vpc_id of this VpcRoute.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this VpcRoute.

        :return: The tenant_id of this VpcRoute.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this VpcRoute.

        :param tenant_id: The tenant_id of this VpcRoute.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

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
        if not isinstance(other, VpcRoute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
