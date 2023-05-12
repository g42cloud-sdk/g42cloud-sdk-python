# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class IpGroup:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'created_at': 'str',
        'description': 'str',
        'id': 'str',
        'ip_list': 'list[IpInfo]',
        'listeners': 'list[ListenerRef]',
        'name': 'str',
        'project_id': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'created_at': 'created_at',
        'description': 'description',
        'id': 'id',
        'ip_list': 'ip_list',
        'listeners': 'listeners',
        'name': 'name',
        'project_id': 'project_id',
        'updated_at': 'updated_at'
    }

    def __init__(self, created_at=None, description=None, id=None, ip_list=None, listeners=None, name=None, project_id=None, updated_at=None):
        """IpGroup

        The model defined in g42cloud sdk

        :param created_at: The param of the IpGroup
        :type created_at: str
        :param description: The param of the IpGroup
        :type description: str
        :param id: The param of the IpGroup
        :type id: str
        :param ip_list: The param of the IpGroup
        :type ip_list: list[:class:`g42cloudsdkelb.v3.IpInfo`]
        :param listeners: The param of the IpGroup
        :type listeners: list[:class:`g42cloudsdkelb.v3.ListenerRef`]
        :param name: The param of the IpGroup
        :type name: str
        :param project_id: The param of the IpGroup
        :type project_id: str
        :param updated_at: The param of the IpGroup
        :type updated_at: str
        """
        
        

        self._created_at = None
        self._description = None
        self._id = None
        self._ip_list = None
        self._listeners = None
        self._name = None
        self._project_id = None
        self._updated_at = None
        self.discriminator = None

        self.created_at = created_at
        self.description = description
        self.id = id
        self.ip_list = ip_list
        self.listeners = listeners
        self.name = name
        self.project_id = project_id
        self.updated_at = updated_at

    @property
    def created_at(self):
        """Gets the created_at of this IpGroup.

        :return: The created_at of this IpGroup.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this IpGroup.

        :param created_at: The created_at of this IpGroup.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def description(self):
        """Gets the description of this IpGroup.

        :return: The description of this IpGroup.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IpGroup.

        :param description: The description of this IpGroup.
        :type description: str
        """
        self._description = description

    @property
    def id(self):
        """Gets the id of this IpGroup.

        :return: The id of this IpGroup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IpGroup.

        :param id: The id of this IpGroup.
        :type id: str
        """
        self._id = id

    @property
    def ip_list(self):
        """Gets the ip_list of this IpGroup.

        :return: The ip_list of this IpGroup.
        :rtype: list[:class:`g42cloudsdkelb.v3.IpInfo`]
        """
        return self._ip_list

    @ip_list.setter
    def ip_list(self, ip_list):
        """Sets the ip_list of this IpGroup.

        :param ip_list: The ip_list of this IpGroup.
        :type ip_list: list[:class:`g42cloudsdkelb.v3.IpInfo`]
        """
        self._ip_list = ip_list

    @property
    def listeners(self):
        """Gets the listeners of this IpGroup.

        :return: The listeners of this IpGroup.
        :rtype: list[:class:`g42cloudsdkelb.v3.ListenerRef`]
        """
        return self._listeners

    @listeners.setter
    def listeners(self, listeners):
        """Sets the listeners of this IpGroup.

        :param listeners: The listeners of this IpGroup.
        :type listeners: list[:class:`g42cloudsdkelb.v3.ListenerRef`]
        """
        self._listeners = listeners

    @property
    def name(self):
        """Gets the name of this IpGroup.

        :return: The name of this IpGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IpGroup.

        :param name: The name of this IpGroup.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        """Gets the project_id of this IpGroup.

        :return: The project_id of this IpGroup.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this IpGroup.

        :param project_id: The project_id of this IpGroup.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def updated_at(self):
        """Gets the updated_at of this IpGroup.

        :return: The updated_at of this IpGroup.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this IpGroup.

        :param updated_at: The updated_at of this IpGroup.
        :type updated_at: str
        """
        self._updated_at = updated_at

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
        if not isinstance(other, IpGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
