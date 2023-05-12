# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityPolicy:

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
        'project_id': 'str',
        'name': 'str',
        'description': 'str',
        'listeners': 'list[ListenerRef]',
        'protocols': 'list[str]',
        'ciphers': 'list[str]',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'name': 'name',
        'description': 'description',
        'listeners': 'listeners',
        'protocols': 'protocols',
        'ciphers': 'ciphers',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, project_id=None, name=None, description=None, listeners=None, protocols=None, ciphers=None, created_at=None, updated_at=None):
        """SecurityPolicy

        The model defined in g42cloud sdk

        :param id: The param of the SecurityPolicy
        :type id: str
        :param project_id: The param of the SecurityPolicy
        :type project_id: str
        :param name: The param of the SecurityPolicy
        :type name: str
        :param description: The param of the SecurityPolicy
        :type description: str
        :param listeners: The param of the SecurityPolicy
        :type listeners: list[:class:`g42cloudsdkelb.v3.ListenerRef`]
        :param protocols: The param of the SecurityPolicy
        :type protocols: list[str]
        :param ciphers: The param of the SecurityPolicy
        :type ciphers: list[str]
        :param created_at: The param of the SecurityPolicy
        :type created_at: str
        :param updated_at: The param of the SecurityPolicy
        :type updated_at: str
        """
        
        

        self._id = None
        self._project_id = None
        self._name = None
        self._description = None
        self._listeners = None
        self._protocols = None
        self._ciphers = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.id = id
        self.project_id = project_id
        self.name = name
        self.description = description
        self.listeners = listeners
        self.protocols = protocols
        self.ciphers = ciphers
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this SecurityPolicy.

        :return: The id of this SecurityPolicy.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SecurityPolicy.

        :param id: The id of this SecurityPolicy.
        :type id: str
        """
        self._id = id

    @property
    def project_id(self):
        """Gets the project_id of this SecurityPolicy.

        :return: The project_id of this SecurityPolicy.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this SecurityPolicy.

        :param project_id: The project_id of this SecurityPolicy.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def name(self):
        """Gets the name of this SecurityPolicy.

        :return: The name of this SecurityPolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SecurityPolicy.

        :param name: The name of this SecurityPolicy.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this SecurityPolicy.

        :return: The description of this SecurityPolicy.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SecurityPolicy.

        :param description: The description of this SecurityPolicy.
        :type description: str
        """
        self._description = description

    @property
    def listeners(self):
        """Gets the listeners of this SecurityPolicy.

        :return: The listeners of this SecurityPolicy.
        :rtype: list[:class:`g42cloudsdkelb.v3.ListenerRef`]
        """
        return self._listeners

    @listeners.setter
    def listeners(self, listeners):
        """Sets the listeners of this SecurityPolicy.

        :param listeners: The listeners of this SecurityPolicy.
        :type listeners: list[:class:`g42cloudsdkelb.v3.ListenerRef`]
        """
        self._listeners = listeners

    @property
    def protocols(self):
        """Gets the protocols of this SecurityPolicy.

        :return: The protocols of this SecurityPolicy.
        :rtype: list[str]
        """
        return self._protocols

    @protocols.setter
    def protocols(self, protocols):
        """Sets the protocols of this SecurityPolicy.

        :param protocols: The protocols of this SecurityPolicy.
        :type protocols: list[str]
        """
        self._protocols = protocols

    @property
    def ciphers(self):
        """Gets the ciphers of this SecurityPolicy.

        :return: The ciphers of this SecurityPolicy.
        :rtype: list[str]
        """
        return self._ciphers

    @ciphers.setter
    def ciphers(self, ciphers):
        """Sets the ciphers of this SecurityPolicy.

        :param ciphers: The ciphers of this SecurityPolicy.
        :type ciphers: list[str]
        """
        self._ciphers = ciphers

    @property
    def created_at(self):
        """Gets the created_at of this SecurityPolicy.

        :return: The created_at of this SecurityPolicy.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this SecurityPolicy.

        :param created_at: The created_at of this SecurityPolicy.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this SecurityPolicy.

        :return: The updated_at of this SecurityPolicy.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this SecurityPolicy.

        :param updated_at: The updated_at of this SecurityPolicy.
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
        if not isinstance(other, SecurityPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
