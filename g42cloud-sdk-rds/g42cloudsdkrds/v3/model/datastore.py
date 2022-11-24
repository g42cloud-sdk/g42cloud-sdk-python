# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Datastore:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'version': 'str',
        'complete_version': 'str'
    }

    attribute_map = {
        'type': 'type',
        'version': 'version',
        'complete_version': 'complete_version'
    }

    def __init__(self, type=None, version=None, complete_version=None):
        """Datastore

        The model defined in g42cloud sdk

        :param type: The param of the Datastore
        :type type: str
        :param version: The param of the Datastore
        :type version: str
        :param complete_version: The param of the Datastore
        :type complete_version: str
        """
        
        

        self._type = None
        self._version = None
        self._complete_version = None
        self.discriminator = None

        self.type = type
        self.version = version
        if complete_version is not None:
            self.complete_version = complete_version

    @property
    def type(self):
        """Gets the type of this Datastore.

        :return: The type of this Datastore.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Datastore.

        :param type: The type of this Datastore.
        :type type: str
        """
        self._type = type

    @property
    def version(self):
        """Gets the version of this Datastore.

        :return: The version of this Datastore.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Datastore.

        :param version: The version of this Datastore.
        :type version: str
        """
        self._version = version

    @property
    def complete_version(self):
        """Gets the complete_version of this Datastore.

        :return: The complete_version of this Datastore.
        :rtype: str
        """
        return self._complete_version

    @complete_version.setter
    def complete_version(self, complete_version):
        """Sets the complete_version of this Datastore.

        :param complete_version: The complete_version of this Datastore.
        :type complete_version: str
        """
        self._complete_version = complete_version

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
        if not isinstance(other, Datastore):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
