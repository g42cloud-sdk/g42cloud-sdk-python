# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class VersionItem:

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
        'min_version': 'str',
        'status': 'str',
        'updated': 'str',
        'version': 'str',
        'links': 'list[LinksItem]'
    }

    attribute_map = {
        'id': 'id',
        'min_version': 'min_version',
        'status': 'status',
        'updated': 'updated',
        'version': 'version',
        'links': 'links'
    }

    def __init__(self, id=None, min_version=None, status=None, updated=None, version=None, links=None):
        """VersionItem

        The model defined in g42cloud sdk

        :param id: The param of the VersionItem
        :type id: str
        :param min_version: The param of the VersionItem
        :type min_version: str
        :param status: The param of the VersionItem
        :type status: str
        :param updated: The param of the VersionItem
        :type updated: str
        :param version: The param of the VersionItem
        :type version: str
        :param links: The param of the VersionItem
        :type links: list[:class:`g42cloudsdksmn.v2.LinksItem`]
        """
        
        

        self._id = None
        self._min_version = None
        self._status = None
        self._updated = None
        self._version = None
        self._links = None
        self.discriminator = None

        self.id = id
        self.min_version = min_version
        self.status = status
        self.updated = updated
        self.version = version
        self.links = links

    @property
    def id(self):
        """Gets the id of this VersionItem.

        :return: The id of this VersionItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VersionItem.

        :param id: The id of this VersionItem.
        :type id: str
        """
        self._id = id

    @property
    def min_version(self):
        """Gets the min_version of this VersionItem.

        :return: The min_version of this VersionItem.
        :rtype: str
        """
        return self._min_version

    @min_version.setter
    def min_version(self, min_version):
        """Sets the min_version of this VersionItem.

        :param min_version: The min_version of this VersionItem.
        :type min_version: str
        """
        self._min_version = min_version

    @property
    def status(self):
        """Gets the status of this VersionItem.

        :return: The status of this VersionItem.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this VersionItem.

        :param status: The status of this VersionItem.
        :type status: str
        """
        self._status = status

    @property
    def updated(self):
        """Gets the updated of this VersionItem.

        :return: The updated of this VersionItem.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this VersionItem.

        :param updated: The updated of this VersionItem.
        :type updated: str
        """
        self._updated = updated

    @property
    def version(self):
        """Gets the version of this VersionItem.

        :return: The version of this VersionItem.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this VersionItem.

        :param version: The version of this VersionItem.
        :type version: str
        """
        self._version = version

    @property
    def links(self):
        """Gets the links of this VersionItem.

        :return: The links of this VersionItem.
        :rtype: list[:class:`g42cloudsdksmn.v2.LinksItem`]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this VersionItem.

        :param links: The links of this VersionItem.
        :type links: list[:class:`g42cloudsdksmn.v2.LinksItem`]
        """
        self._links = links

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
        if not isinstance(other, VersionItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
