# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class GlanceCreateImageMetadataRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'os_version': 'str',
        'container_format': 'str',
        'disk_format': 'str',
        'min_disk': 'int',
        'min_ram': 'int',
        'name': 'str',
        'protected': 'bool',
        'tags': 'list[str]',
        'visibility': 'str'
    }

    attribute_map = {
        'os_version': '__os_version',
        'container_format': 'container_format',
        'disk_format': 'disk_format',
        'min_disk': 'min_disk',
        'min_ram': 'min_ram',
        'name': 'name',
        'protected': 'protected',
        'tags': 'tags',
        'visibility': 'visibility'
    }

    def __init__(self, os_version=None, container_format=None, disk_format=None, min_disk=None, min_ram=None, name=None, protected=None, tags=None, visibility=None):
        """GlanceCreateImageMetadataRequestBody

        The model defined in g42cloud sdk

        :param os_version: The param of the GlanceCreateImageMetadataRequestBody
        :type os_version: str
        :param container_format: The param of the GlanceCreateImageMetadataRequestBody
        :type container_format: str
        :param disk_format: The param of the GlanceCreateImageMetadataRequestBody
        :type disk_format: str
        :param min_disk: The param of the GlanceCreateImageMetadataRequestBody
        :type min_disk: int
        :param min_ram: The param of the GlanceCreateImageMetadataRequestBody
        :type min_ram: int
        :param name: The param of the GlanceCreateImageMetadataRequestBody
        :type name: str
        :param protected: The param of the GlanceCreateImageMetadataRequestBody
        :type protected: bool
        :param tags: The param of the GlanceCreateImageMetadataRequestBody
        :type tags: list[str]
        :param visibility: The param of the GlanceCreateImageMetadataRequestBody
        :type visibility: str
        """
        
        

        self._os_version = None
        self._container_format = None
        self._disk_format = None
        self._min_disk = None
        self._min_ram = None
        self._name = None
        self._protected = None
        self._tags = None
        self._visibility = None
        self.discriminator = None

        if os_version is not None:
            self.os_version = os_version
        if container_format is not None:
            self.container_format = container_format
        if disk_format is not None:
            self.disk_format = disk_format
        if min_disk is not None:
            self.min_disk = min_disk
        if min_ram is not None:
            self.min_ram = min_ram
        if name is not None:
            self.name = name
        if protected is not None:
            self.protected = protected
        if tags is not None:
            self.tags = tags
        if visibility is not None:
            self.visibility = visibility

    @property
    def os_version(self):
        """Gets the os_version of this GlanceCreateImageMetadataRequestBody.

        :return: The os_version of this GlanceCreateImageMetadataRequestBody.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """Sets the os_version of this GlanceCreateImageMetadataRequestBody.

        :param os_version: The os_version of this GlanceCreateImageMetadataRequestBody.
        :type os_version: str
        """
        self._os_version = os_version

    @property
    def container_format(self):
        """Gets the container_format of this GlanceCreateImageMetadataRequestBody.

        :return: The container_format of this GlanceCreateImageMetadataRequestBody.
        :rtype: str
        """
        return self._container_format

    @container_format.setter
    def container_format(self, container_format):
        """Sets the container_format of this GlanceCreateImageMetadataRequestBody.

        :param container_format: The container_format of this GlanceCreateImageMetadataRequestBody.
        :type container_format: str
        """
        self._container_format = container_format

    @property
    def disk_format(self):
        """Gets the disk_format of this GlanceCreateImageMetadataRequestBody.

        :return: The disk_format of this GlanceCreateImageMetadataRequestBody.
        :rtype: str
        """
        return self._disk_format

    @disk_format.setter
    def disk_format(self, disk_format):
        """Sets the disk_format of this GlanceCreateImageMetadataRequestBody.

        :param disk_format: The disk_format of this GlanceCreateImageMetadataRequestBody.
        :type disk_format: str
        """
        self._disk_format = disk_format

    @property
    def min_disk(self):
        """Gets the min_disk of this GlanceCreateImageMetadataRequestBody.

        :return: The min_disk of this GlanceCreateImageMetadataRequestBody.
        :rtype: int
        """
        return self._min_disk

    @min_disk.setter
    def min_disk(self, min_disk):
        """Sets the min_disk of this GlanceCreateImageMetadataRequestBody.

        :param min_disk: The min_disk of this GlanceCreateImageMetadataRequestBody.
        :type min_disk: int
        """
        self._min_disk = min_disk

    @property
    def min_ram(self):
        """Gets the min_ram of this GlanceCreateImageMetadataRequestBody.

        :return: The min_ram of this GlanceCreateImageMetadataRequestBody.
        :rtype: int
        """
        return self._min_ram

    @min_ram.setter
    def min_ram(self, min_ram):
        """Sets the min_ram of this GlanceCreateImageMetadataRequestBody.

        :param min_ram: The min_ram of this GlanceCreateImageMetadataRequestBody.
        :type min_ram: int
        """
        self._min_ram = min_ram

    @property
    def name(self):
        """Gets the name of this GlanceCreateImageMetadataRequestBody.

        :return: The name of this GlanceCreateImageMetadataRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GlanceCreateImageMetadataRequestBody.

        :param name: The name of this GlanceCreateImageMetadataRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def protected(self):
        """Gets the protected of this GlanceCreateImageMetadataRequestBody.

        :return: The protected of this GlanceCreateImageMetadataRequestBody.
        :rtype: bool
        """
        return self._protected

    @protected.setter
    def protected(self, protected):
        """Sets the protected of this GlanceCreateImageMetadataRequestBody.

        :param protected: The protected of this GlanceCreateImageMetadataRequestBody.
        :type protected: bool
        """
        self._protected = protected

    @property
    def tags(self):
        """Gets the tags of this GlanceCreateImageMetadataRequestBody.

        :return: The tags of this GlanceCreateImageMetadataRequestBody.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this GlanceCreateImageMetadataRequestBody.

        :param tags: The tags of this GlanceCreateImageMetadataRequestBody.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def visibility(self):
        """Gets the visibility of this GlanceCreateImageMetadataRequestBody.

        :return: The visibility of this GlanceCreateImageMetadataRequestBody.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this GlanceCreateImageMetadataRequestBody.

        :param visibility: The visibility of this GlanceCreateImageMetadataRequestBody.
        :type visibility: str
        """
        self._visibility = visibility

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
        if not isinstance(other, GlanceCreateImageMetadataRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
