# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RouteTableListResp:

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
        'name': 'str',
        'default': 'bool',
        'subnets': 'list[SubnetList]',
        'tenant_id': 'str',
        'vpc_id': 'str',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'default': 'default',
        'subnets': 'subnets',
        'tenant_id': 'tenant_id',
        'vpc_id': 'vpc_id',
        'description': 'description'
    }

    def __init__(self, id=None, name=None, default=None, subnets=None, tenant_id=None, vpc_id=None, description=None):
        """RouteTableListResp

        The model defined in g42cloud sdk

        :param id: The param of the RouteTableListResp
        :type id: str
        :param name: The param of the RouteTableListResp
        :type name: str
        :param default: The param of the RouteTableListResp
        :type default: bool
        :param subnets: The param of the RouteTableListResp
        :type subnets: list[:class:`g42cloudsdkvpc.v2.SubnetList`]
        :param tenant_id: The param of the RouteTableListResp
        :type tenant_id: str
        :param vpc_id: The param of the RouteTableListResp
        :type vpc_id: str
        :param description: The param of the RouteTableListResp
        :type description: str
        """
        
        

        self._id = None
        self._name = None
        self._default = None
        self._subnets = None
        self._tenant_id = None
        self._vpc_id = None
        self._description = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.default = default
        self.subnets = subnets
        self.tenant_id = tenant_id
        self.vpc_id = vpc_id
        self.description = description

    @property
    def id(self):
        """Gets the id of this RouteTableListResp.

        :return: The id of this RouteTableListResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RouteTableListResp.

        :param id: The id of this RouteTableListResp.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this RouteTableListResp.

        :return: The name of this RouteTableListResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RouteTableListResp.

        :param name: The name of this RouteTableListResp.
        :type name: str
        """
        self._name = name

    @property
    def default(self):
        """Gets the default of this RouteTableListResp.

        :return: The default of this RouteTableListResp.
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this RouteTableListResp.

        :param default: The default of this RouteTableListResp.
        :type default: bool
        """
        self._default = default

    @property
    def subnets(self):
        """Gets the subnets of this RouteTableListResp.

        :return: The subnets of this RouteTableListResp.
        :rtype: list[:class:`g42cloudsdkvpc.v2.SubnetList`]
        """
        return self._subnets

    @subnets.setter
    def subnets(self, subnets):
        """Sets the subnets of this RouteTableListResp.

        :param subnets: The subnets of this RouteTableListResp.
        :type subnets: list[:class:`g42cloudsdkvpc.v2.SubnetList`]
        """
        self._subnets = subnets

    @property
    def tenant_id(self):
        """Gets the tenant_id of this RouteTableListResp.

        :return: The tenant_id of this RouteTableListResp.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this RouteTableListResp.

        :param tenant_id: The tenant_id of this RouteTableListResp.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def vpc_id(self):
        """Gets the vpc_id of this RouteTableListResp.

        :return: The vpc_id of this RouteTableListResp.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this RouteTableListResp.

        :param vpc_id: The vpc_id of this RouteTableListResp.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def description(self):
        """Gets the description of this RouteTableListResp.

        :return: The description of this RouteTableListResp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RouteTableListResp.

        :param description: The description of this RouteTableListResp.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, RouteTableListResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
