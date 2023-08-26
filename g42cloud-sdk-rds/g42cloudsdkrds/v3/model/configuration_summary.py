# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigurationSummary:

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
        'datastore_version_name': 'str',
        'datastore_name': 'str',
        'created': 'str',
        'updated': 'str',
        'user_defined': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'datastore_version_name': 'datastore_version_name',
        'datastore_name': 'datastore_name',
        'created': 'created',
        'updated': 'updated',
        'user_defined': 'user_defined'
    }

    def __init__(self, id=None, name=None, description=None, datastore_version_name=None, datastore_name=None, created=None, updated=None, user_defined=None):
        """ConfigurationSummary

        The model defined in g42cloud sdk

        :param id: The param of the ConfigurationSummary
        :type id: str
        :param name: The param of the ConfigurationSummary
        :type name: str
        :param description: The param of the ConfigurationSummary
        :type description: str
        :param datastore_version_name: The param of the ConfigurationSummary
        :type datastore_version_name: str
        :param datastore_name: The param of the ConfigurationSummary
        :type datastore_name: str
        :param created: The param of the ConfigurationSummary
        :type created: str
        :param updated: The param of the ConfigurationSummary
        :type updated: str
        :param user_defined: The param of the ConfigurationSummary
        :type user_defined: bool
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._datastore_version_name = None
        self._datastore_name = None
        self._created = None
        self._updated = None
        self._user_defined = None
        self.discriminator = None

        self.id = id
        self.name = name
        if description is not None:
            self.description = description
        self.datastore_version_name = datastore_version_name
        self.datastore_name = datastore_name
        self.created = created
        self.updated = updated
        self.user_defined = user_defined

    @property
    def id(self):
        """Gets the id of this ConfigurationSummary.

        :return: The id of this ConfigurationSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConfigurationSummary.

        :param id: The id of this ConfigurationSummary.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ConfigurationSummary.

        :return: The name of this ConfigurationSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConfigurationSummary.

        :param name: The name of this ConfigurationSummary.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ConfigurationSummary.

        :return: The description of this ConfigurationSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ConfigurationSummary.

        :param description: The description of this ConfigurationSummary.
        :type description: str
        """
        self._description = description

    @property
    def datastore_version_name(self):
        """Gets the datastore_version_name of this ConfigurationSummary.

        :return: The datastore_version_name of this ConfigurationSummary.
        :rtype: str
        """
        return self._datastore_version_name

    @datastore_version_name.setter
    def datastore_version_name(self, datastore_version_name):
        """Sets the datastore_version_name of this ConfigurationSummary.

        :param datastore_version_name: The datastore_version_name of this ConfigurationSummary.
        :type datastore_version_name: str
        """
        self._datastore_version_name = datastore_version_name

    @property
    def datastore_name(self):
        """Gets the datastore_name of this ConfigurationSummary.

        :return: The datastore_name of this ConfigurationSummary.
        :rtype: str
        """
        return self._datastore_name

    @datastore_name.setter
    def datastore_name(self, datastore_name):
        """Sets the datastore_name of this ConfigurationSummary.

        :param datastore_name: The datastore_name of this ConfigurationSummary.
        :type datastore_name: str
        """
        self._datastore_name = datastore_name

    @property
    def created(self):
        """Gets the created of this ConfigurationSummary.

        :return: The created of this ConfigurationSummary.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ConfigurationSummary.

        :param created: The created of this ConfigurationSummary.
        :type created: str
        """
        self._created = created

    @property
    def updated(self):
        """Gets the updated of this ConfigurationSummary.

        :return: The updated of this ConfigurationSummary.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this ConfigurationSummary.

        :param updated: The updated of this ConfigurationSummary.
        :type updated: str
        """
        self._updated = updated

    @property
    def user_defined(self):
        """Gets the user_defined of this ConfigurationSummary.

        :return: The user_defined of this ConfigurationSummary.
        :rtype: bool
        """
        return self._user_defined

    @user_defined.setter
    def user_defined(self, user_defined):
        """Sets the user_defined of this ConfigurationSummary.

        :param user_defined: The user_defined of this ConfigurationSummary.
        :type user_defined: bool
        """
        self._user_defined = user_defined

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
        if not isinstance(other, ConfigurationSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
