# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListErrorServersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'migproject': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'migproject': 'migproject',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, limit=None, offset=None, migproject=None, enterprise_project_id=None):
        """ListErrorServersRequest

        The model defined in g42cloud sdk

        :param limit: The param of the ListErrorServersRequest
        :type limit: int
        :param offset: The param of the ListErrorServersRequest
        :type offset: int
        :param migproject: The param of the ListErrorServersRequest
        :type migproject: str
        :param enterprise_project_id: The param of the ListErrorServersRequest
        :type enterprise_project_id: str
        """
        
        

        self._limit = None
        self._offset = None
        self._migproject = None
        self._enterprise_project_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        self.offset = offset
        if migproject is not None:
            self.migproject = migproject
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def limit(self):
        """Gets the limit of this ListErrorServersRequest.

        :return: The limit of this ListErrorServersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListErrorServersRequest.

        :param limit: The limit of this ListErrorServersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListErrorServersRequest.

        :return: The offset of this ListErrorServersRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListErrorServersRequest.

        :param offset: The offset of this ListErrorServersRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def migproject(self):
        """Gets the migproject of this ListErrorServersRequest.

        :return: The migproject of this ListErrorServersRequest.
        :rtype: str
        """
        return self._migproject

    @migproject.setter
    def migproject(self, migproject):
        """Sets the migproject of this ListErrorServersRequest.

        :param migproject: The migproject of this ListErrorServersRequest.
        :type migproject: str
        """
        self._migproject = migproject

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListErrorServersRequest.

        :return: The enterprise_project_id of this ListErrorServersRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListErrorServersRequest.

        :param enterprise_project_id: The enterprise_project_id of this ListErrorServersRequest.
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
        if not isinstance(other, ListErrorServersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
