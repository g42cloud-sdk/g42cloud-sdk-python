# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Vpc:

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
        'cidr': 'str',
        'description': 'str',
        'routes': 'list[Route]',
        'status': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'cidr': 'cidr',
        'description': 'description',
        'routes': 'routes',
        'status': 'status',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, id=None, name=None, cidr=None, description=None, routes=None, status=None, enterprise_project_id=None):
        """Vpc

        The model defined in g42cloud sdk

        :param id: The param of the Vpc
        :type id: str
        :param name: The param of the Vpc
        :type name: str
        :param cidr: The param of the Vpc
        :type cidr: str
        :param description: The param of the Vpc
        :type description: str
        :param routes: The param of the Vpc
        :type routes: list[:class:`g42cloudsdkvpc.v2.Route`]
        :param status: The param of the Vpc
        :type status: str
        :param enterprise_project_id: The param of the Vpc
        :type enterprise_project_id: str
        """
        
        

        self._id = None
        self._name = None
        self._cidr = None
        self._description = None
        self._routes = None
        self._status = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.cidr = cidr
        self.description = description
        self.routes = routes
        self.status = status
        self.enterprise_project_id = enterprise_project_id

    @property
    def id(self):
        """Gets the id of this Vpc.

        :return: The id of this Vpc.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Vpc.

        :param id: The id of this Vpc.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this Vpc.

        :return: The name of this Vpc.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Vpc.

        :param name: The name of this Vpc.
        :type name: str
        """
        self._name = name

    @property
    def cidr(self):
        """Gets the cidr of this Vpc.

        :return: The cidr of this Vpc.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this Vpc.

        :param cidr: The cidr of this Vpc.
        :type cidr: str
        """
        self._cidr = cidr

    @property
    def description(self):
        """Gets the description of this Vpc.

        :return: The description of this Vpc.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Vpc.

        :param description: The description of this Vpc.
        :type description: str
        """
        self._description = description

    @property
    def routes(self):
        """Gets the routes of this Vpc.

        :return: The routes of this Vpc.
        :rtype: list[:class:`g42cloudsdkvpc.v2.Route`]
        """
        return self._routes

    @routes.setter
    def routes(self, routes):
        """Sets the routes of this Vpc.

        :param routes: The routes of this Vpc.
        :type routes: list[:class:`g42cloudsdkvpc.v2.Route`]
        """
        self._routes = routes

    @property
    def status(self):
        """Gets the status of this Vpc.

        :return: The status of this Vpc.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Vpc.

        :param status: The status of this Vpc.
        :type status: str
        """
        self._status = status

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this Vpc.

        :return: The enterprise_project_id of this Vpc.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this Vpc.

        :param enterprise_project_id: The enterprise_project_id of this Vpc.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, Vpc):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
