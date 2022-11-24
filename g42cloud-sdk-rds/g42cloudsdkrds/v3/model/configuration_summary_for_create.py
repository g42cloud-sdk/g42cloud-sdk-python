# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigurationSummaryForCreate:

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
        'updated': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'datastore_version_name': 'datastore_version_name',
        'datastore_name': 'datastore_name',
        'created': 'created',
        'updated': 'updated'
    }

    def __init__(self, id=None, name=None, description=None, datastore_version_name=None, datastore_name=None, created=None, updated=None):
        """ConfigurationSummaryForCreate

        The model defined in g42cloud sdk

        :param id: The param of the ConfigurationSummaryForCreate
        :type id: str
        :param name: The param of the ConfigurationSummaryForCreate
        :type name: str
        :param description: The param of the ConfigurationSummaryForCreate
        :type description: str
        :param datastore_version_name: The param of the ConfigurationSummaryForCreate
        :type datastore_version_name: str
        :param datastore_name: The param of the ConfigurationSummaryForCreate
        :type datastore_name: str
        :param created: The param of the ConfigurationSummaryForCreate
        :type created: str
        :param updated: The param of the ConfigurationSummaryForCreate
        :type updated: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._datastore_version_name = None
        self._datastore_name = None
        self._created = None
        self._updated = None
        self.discriminator = None

        self.id = id
        self.name = name
        if description is not None:
            self.description = description
        self.datastore_version_name = datastore_version_name
        self.datastore_name = datastore_name
        self.created = created
        self.updated = updated

    @property
    def id(self):
        """Gets the id of this ConfigurationSummaryForCreate.

        :return: The id of this ConfigurationSummaryForCreate.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConfigurationSummaryForCreate.

        :param id: The id of this ConfigurationSummaryForCreate.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ConfigurationSummaryForCreate.

        :return: The name of this ConfigurationSummaryForCreate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConfigurationSummaryForCreate.

        :param name: The name of this ConfigurationSummaryForCreate.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ConfigurationSummaryForCreate.

        :return: The description of this ConfigurationSummaryForCreate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ConfigurationSummaryForCreate.

        :param description: The description of this ConfigurationSummaryForCreate.
        :type description: str
        """
        self._description = description

    @property
    def datastore_version_name(self):
        """Gets the datastore_version_name of this ConfigurationSummaryForCreate.

        :return: The datastore_version_name of this ConfigurationSummaryForCreate.
        :rtype: str
        """
        return self._datastore_version_name

    @datastore_version_name.setter
    def datastore_version_name(self, datastore_version_name):
        """Sets the datastore_version_name of this ConfigurationSummaryForCreate.

        :param datastore_version_name: The datastore_version_name of this ConfigurationSummaryForCreate.
        :type datastore_version_name: str
        """
        self._datastore_version_name = datastore_version_name

    @property
    def datastore_name(self):
        """Gets the datastore_name of this ConfigurationSummaryForCreate.

        :return: The datastore_name of this ConfigurationSummaryForCreate.
        :rtype: str
        """
        return self._datastore_name

    @datastore_name.setter
    def datastore_name(self, datastore_name):
        """Sets the datastore_name of this ConfigurationSummaryForCreate.

        :param datastore_name: The datastore_name of this ConfigurationSummaryForCreate.
        :type datastore_name: str
        """
        self._datastore_name = datastore_name

    @property
    def created(self):
        """Gets the created of this ConfigurationSummaryForCreate.

        :return: The created of this ConfigurationSummaryForCreate.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ConfigurationSummaryForCreate.

        :param created: The created of this ConfigurationSummaryForCreate.
        :type created: str
        """
        self._created = created

    @property
    def updated(self):
        """Gets the updated of this ConfigurationSummaryForCreate.

        :return: The updated of this ConfigurationSummaryForCreate.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this ConfigurationSummaryForCreate.

        :param updated: The updated of this ConfigurationSummaryForCreate.
        :type updated: str
        """
        self._updated = updated

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
        if not isinstance(other, ConfigurationSummaryForCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other