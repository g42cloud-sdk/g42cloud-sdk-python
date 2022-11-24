# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddressGroup:

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
        'description': 'str',
        'ip_set': 'list[str]',
        'ip_version': 'int',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'tenant_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'ip_set': 'ip_set',
        'ip_version': 'ip_version',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'tenant_id': 'tenant_id'
    }

    def __init__(self, id=None, name=None, description=None, ip_set=None, ip_version=None, created_at=None, updated_at=None, tenant_id=None):
        """AddressGroup

        The model defined in g42cloud sdk

        :param id: The param of the AddressGroup
        :type id: str
        :param name: The param of the AddressGroup
        :type name: str
        :param description: The param of the AddressGroup
        :type description: str
        :param ip_set: The param of the AddressGroup
        :type ip_set: list[str]
        :param ip_version: The param of the AddressGroup
        :type ip_version: int
        :param created_at: The param of the AddressGroup
        :type created_at: datetime
        :param updated_at: The param of the AddressGroup
        :type updated_at: datetime
        :param tenant_id: The param of the AddressGroup
        :type tenant_id: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._ip_set = None
        self._ip_version = None
        self._created_at = None
        self._updated_at = None
        self._tenant_id = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.description = description
        self.ip_set = ip_set
        self.ip_version = ip_version
        self.created_at = created_at
        self.updated_at = updated_at
        self.tenant_id = tenant_id

    @property
    def id(self):
        """Gets the id of this AddressGroup.

        :return: The id of this AddressGroup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AddressGroup.

        :param id: The id of this AddressGroup.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this AddressGroup.

        :return: The name of this AddressGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AddressGroup.

        :param name: The name of this AddressGroup.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this AddressGroup.

        :return: The description of this AddressGroup.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AddressGroup.

        :param description: The description of this AddressGroup.
        :type description: str
        """
        self._description = description

    @property
    def ip_set(self):
        """Gets the ip_set of this AddressGroup.

        :return: The ip_set of this AddressGroup.
        :rtype: list[str]
        """
        return self._ip_set

    @ip_set.setter
    def ip_set(self, ip_set):
        """Sets the ip_set of this AddressGroup.

        :param ip_set: The ip_set of this AddressGroup.
        :type ip_set: list[str]
        """
        self._ip_set = ip_set

    @property
    def ip_version(self):
        """Gets the ip_version of this AddressGroup.

        :return: The ip_version of this AddressGroup.
        :rtype: int
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this AddressGroup.

        :param ip_version: The ip_version of this AddressGroup.
        :type ip_version: int
        """
        self._ip_version = ip_version

    @property
    def created_at(self):
        """Gets the created_at of this AddressGroup.

        :return: The created_at of this AddressGroup.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this AddressGroup.

        :param created_at: The created_at of this AddressGroup.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this AddressGroup.

        :return: The updated_at of this AddressGroup.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this AddressGroup.

        :param updated_at: The updated_at of this AddressGroup.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def tenant_id(self):
        """Gets the tenant_id of this AddressGroup.

        :return: The tenant_id of this AddressGroup.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this AddressGroup.

        :param tenant_id: The tenant_id of this AddressGroup.
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
        if not isinstance(other, AddressGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
