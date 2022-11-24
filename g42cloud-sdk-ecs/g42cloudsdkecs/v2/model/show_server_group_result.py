# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowServerGroupResult:

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
        'members': 'list[str]',
        'metadata': 'dict(str, str)',
        'name': 'str',
        'policies': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'members': 'members',
        'metadata': 'metadata',
        'name': 'name',
        'policies': 'policies'
    }

    def __init__(self, id=None, members=None, metadata=None, name=None, policies=None):
        """ShowServerGroupResult

        The model defined in g42cloud sdk

        :param id: The param of the ShowServerGroupResult
        :type id: str
        :param members: The param of the ShowServerGroupResult
        :type members: list[str]
        :param metadata: The param of the ShowServerGroupResult
        :type metadata: dict(str, str)
        :param name: The param of the ShowServerGroupResult
        :type name: str
        :param policies: The param of the ShowServerGroupResult
        :type policies: list[str]
        """
        
        

        self._id = None
        self._members = None
        self._metadata = None
        self._name = None
        self._policies = None
        self.discriminator = None

        self.id = id
        self.members = members
        self.metadata = metadata
        self.name = name
        self.policies = policies

    @property
    def id(self):
        """Gets the id of this ShowServerGroupResult.

        :return: The id of this ShowServerGroupResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowServerGroupResult.

        :param id: The id of this ShowServerGroupResult.
        :type id: str
        """
        self._id = id

    @property
    def members(self):
        """Gets the members of this ShowServerGroupResult.

        :return: The members of this ShowServerGroupResult.
        :rtype: list[str]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this ShowServerGroupResult.

        :param members: The members of this ShowServerGroupResult.
        :type members: list[str]
        """
        self._members = members

    @property
    def metadata(self):
        """Gets the metadata of this ShowServerGroupResult.

        :return: The metadata of this ShowServerGroupResult.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ShowServerGroupResult.

        :param metadata: The metadata of this ShowServerGroupResult.
        :type metadata: dict(str, str)
        """
        self._metadata = metadata

    @property
    def name(self):
        """Gets the name of this ShowServerGroupResult.

        :return: The name of this ShowServerGroupResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowServerGroupResult.

        :param name: The name of this ShowServerGroupResult.
        :type name: str
        """
        self._name = name

    @property
    def policies(self):
        """Gets the policies of this ShowServerGroupResult.

        :return: The policies of this ShowServerGroupResult.
        :rtype: list[str]
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        """Sets the policies of this ShowServerGroupResult.

        :param policies: The policies of this ShowServerGroupResult.
        :type policies: list[str]
        """
        self._policies = policies

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
        if not isinstance(other, ShowServerGroupResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
