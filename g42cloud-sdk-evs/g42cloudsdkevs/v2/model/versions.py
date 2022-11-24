# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Versions:

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
        'links': 'list[Link]',
        'media_types': 'list[MediaTypes]',
        'min_version': 'str',
        'status': 'str',
        'updated': 'str',
        'version': 'str'
    }

    attribute_map = {
        'id': 'id',
        'links': 'links',
        'media_types': 'media-types',
        'min_version': 'min_version',
        'status': 'status',
        'updated': 'updated',
        'version': 'version'
    }

    def __init__(self, id=None, links=None, media_types=None, min_version=None, status=None, updated=None, version=None):
        """Versions

        The model defined in g42cloud sdk

        :param id: The param of the Versions
        :type id: str
        :param links: The param of the Versions
        :type links: list[:class:`g42cloudsdkevs.v2.Link`]
        :param media_types: The param of the Versions
        :type media_types: list[:class:`g42cloudsdkevs.v2.MediaTypes`]
        :param min_version: The param of the Versions
        :type min_version: str
        :param status: The param of the Versions
        :type status: str
        :param updated: The param of the Versions
        :type updated: str
        :param version: The param of the Versions
        :type version: str
        """
        
        

        self._id = None
        self._links = None
        self._media_types = None
        self._min_version = None
        self._status = None
        self._updated = None
        self._version = None
        self.discriminator = None

        self.id = id
        self.links = links
        self.media_types = media_types
        if min_version is not None:
            self.min_version = min_version
        self.status = status
        self.updated = updated
        self.version = version

    @property
    def id(self):
        """Gets the id of this Versions.

        :return: The id of this Versions.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Versions.

        :param id: The id of this Versions.
        :type id: str
        """
        self._id = id

    @property
    def links(self):
        """Gets the links of this Versions.

        :return: The links of this Versions.
        :rtype: list[:class:`g42cloudsdkevs.v2.Link`]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Versions.

        :param links: The links of this Versions.
        :type links: list[:class:`g42cloudsdkevs.v2.Link`]
        """
        self._links = links

    @property
    def media_types(self):
        """Gets the media_types of this Versions.

        :return: The media_types of this Versions.
        :rtype: list[:class:`g42cloudsdkevs.v2.MediaTypes`]
        """
        return self._media_types

    @media_types.setter
    def media_types(self, media_types):
        """Sets the media_types of this Versions.

        :param media_types: The media_types of this Versions.
        :type media_types: list[:class:`g42cloudsdkevs.v2.MediaTypes`]
        """
        self._media_types = media_types

    @property
    def min_version(self):
        """Gets the min_version of this Versions.

        :return: The min_version of this Versions.
        :rtype: str
        """
        return self._min_version

    @min_version.setter
    def min_version(self, min_version):
        """Sets the min_version of this Versions.

        :param min_version: The min_version of this Versions.
        :type min_version: str
        """
        self._min_version = min_version

    @property
    def status(self):
        """Gets the status of this Versions.

        :return: The status of this Versions.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Versions.

        :param status: The status of this Versions.
        :type status: str
        """
        self._status = status

    @property
    def updated(self):
        """Gets the updated of this Versions.

        :return: The updated of this Versions.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this Versions.

        :param updated: The updated of this Versions.
        :type updated: str
        """
        self._updated = updated

    @property
    def version(self):
        """Gets the version of this Versions.

        :return: The version of this Versions.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Versions.

        :param version: The version of this Versions.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, Versions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
