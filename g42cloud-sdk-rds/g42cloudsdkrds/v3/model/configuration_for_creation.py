# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigurationForCreation:

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
        'description': 'str',
        'datastore': 'ParaGroupDatastore',
        'values': 'dict(str, str)'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'datastore': 'datastore',
        'values': 'values'
    }

    def __init__(self, name=None, description=None, datastore=None, values=None):
        """ConfigurationForCreation

        The model defined in g42cloud sdk

        :param name: The param of the ConfigurationForCreation
        :type name: str
        :param description: The param of the ConfigurationForCreation
        :type description: str
        :param datastore: The param of the ConfigurationForCreation
        :type datastore: :class:`g42cloudsdkrds.v3.ParaGroupDatastore`
        :param values: The param of the ConfigurationForCreation
        :type values: dict(str, str)
        """
        
        

        self._name = None
        self._description = None
        self._datastore = None
        self._values = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.datastore = datastore
        if values is not None:
            self.values = values

    @property
    def name(self):
        """Gets the name of this ConfigurationForCreation.

        :return: The name of this ConfigurationForCreation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConfigurationForCreation.

        :param name: The name of this ConfigurationForCreation.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ConfigurationForCreation.

        :return: The description of this ConfigurationForCreation.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ConfigurationForCreation.

        :param description: The description of this ConfigurationForCreation.
        :type description: str
        """
        self._description = description

    @property
    def datastore(self):
        """Gets the datastore of this ConfigurationForCreation.

        :return: The datastore of this ConfigurationForCreation.
        :rtype: :class:`g42cloudsdkrds.v3.ParaGroupDatastore`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        """Sets the datastore of this ConfigurationForCreation.

        :param datastore: The datastore of this ConfigurationForCreation.
        :type datastore: :class:`g42cloudsdkrds.v3.ParaGroupDatastore`
        """
        self._datastore = datastore

    @property
    def values(self):
        """Gets the values of this ConfigurationForCreation.

        :return: The values of this ConfigurationForCreation.
        :rtype: dict(str, str)
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this ConfigurationForCreation.

        :param values: The values of this ConfigurationForCreation.
        :type values: dict(str, str)
        """
        self._values = values

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
        if not isinstance(other, ConfigurationForCreation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
