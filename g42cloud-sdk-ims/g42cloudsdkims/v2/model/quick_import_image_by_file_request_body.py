# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class QuickImportImageByFileRequestBody:

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
        'os_version': 'str',
        'image_url': 'str',
        'min_disk': 'int',
        'tags': 'list[str]',
        'type': 'str',
        'enterprise_project_id': 'str',
        'architecture': 'str',
        'os_type': 'str',
        'image_tags': 'list[ResourceTag]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'os_version': 'os_version',
        'image_url': 'image_url',
        'min_disk': 'min_disk',
        'tags': 'tags',
        'type': 'type',
        'enterprise_project_id': 'enterprise_project_id',
        'architecture': 'architecture',
        'os_type': 'os_type',
        'image_tags': 'image_tags'
    }

    def __init__(self, name=None, description=None, os_version=None, image_url=None, min_disk=None, tags=None, type=None, enterprise_project_id=None, architecture=None, os_type=None, image_tags=None):
        """QuickImportImageByFileRequestBody

        The model defined in g42cloud sdk

        :param name: The param of the QuickImportImageByFileRequestBody
        :type name: str
        :param description: The param of the QuickImportImageByFileRequestBody
        :type description: str
        :param os_version: The param of the QuickImportImageByFileRequestBody
        :type os_version: str
        :param image_url: The param of the QuickImportImageByFileRequestBody
        :type image_url: str
        :param min_disk: The param of the QuickImportImageByFileRequestBody
        :type min_disk: int
        :param tags: The param of the QuickImportImageByFileRequestBody
        :type tags: list[str]
        :param type: The param of the QuickImportImageByFileRequestBody
        :type type: str
        :param enterprise_project_id: The param of the QuickImportImageByFileRequestBody
        :type enterprise_project_id: str
        :param architecture: The param of the QuickImportImageByFileRequestBody
        :type architecture: str
        :param os_type: The param of the QuickImportImageByFileRequestBody
        :type os_type: str
        :param image_tags: The param of the QuickImportImageByFileRequestBody
        :type image_tags: list[:class:`g42cloudsdkims.v2.ResourceTag`]
        """
        
        

        self._name = None
        self._description = None
        self._os_version = None
        self._image_url = None
        self._min_disk = None
        self._tags = None
        self._type = None
        self._enterprise_project_id = None
        self._architecture = None
        self._os_type = None
        self._image_tags = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.os_version = os_version
        self.image_url = image_url
        self.min_disk = min_disk
        if tags is not None:
            self.tags = tags
        if type is not None:
            self.type = type
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if architecture is not None:
            self.architecture = architecture
        if os_type is not None:
            self.os_type = os_type
        if image_tags is not None:
            self.image_tags = image_tags

    @property
    def name(self):
        """Gets the name of this QuickImportImageByFileRequestBody.

        :return: The name of this QuickImportImageByFileRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this QuickImportImageByFileRequestBody.

        :param name: The name of this QuickImportImageByFileRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this QuickImportImageByFileRequestBody.

        :return: The description of this QuickImportImageByFileRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this QuickImportImageByFileRequestBody.

        :param description: The description of this QuickImportImageByFileRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def os_version(self):
        """Gets the os_version of this QuickImportImageByFileRequestBody.

        :return: The os_version of this QuickImportImageByFileRequestBody.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """Sets the os_version of this QuickImportImageByFileRequestBody.

        :param os_version: The os_version of this QuickImportImageByFileRequestBody.
        :type os_version: str
        """
        self._os_version = os_version

    @property
    def image_url(self):
        """Gets the image_url of this QuickImportImageByFileRequestBody.

        :return: The image_url of this QuickImportImageByFileRequestBody.
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this QuickImportImageByFileRequestBody.

        :param image_url: The image_url of this QuickImportImageByFileRequestBody.
        :type image_url: str
        """
        self._image_url = image_url

    @property
    def min_disk(self):
        """Gets the min_disk of this QuickImportImageByFileRequestBody.

        :return: The min_disk of this QuickImportImageByFileRequestBody.
        :rtype: int
        """
        return self._min_disk

    @min_disk.setter
    def min_disk(self, min_disk):
        """Sets the min_disk of this QuickImportImageByFileRequestBody.

        :param min_disk: The min_disk of this QuickImportImageByFileRequestBody.
        :type min_disk: int
        """
        self._min_disk = min_disk

    @property
    def tags(self):
        """Gets the tags of this QuickImportImageByFileRequestBody.

        :return: The tags of this QuickImportImageByFileRequestBody.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this QuickImportImageByFileRequestBody.

        :param tags: The tags of this QuickImportImageByFileRequestBody.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def type(self):
        """Gets the type of this QuickImportImageByFileRequestBody.

        :return: The type of this QuickImportImageByFileRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this QuickImportImageByFileRequestBody.

        :param type: The type of this QuickImportImageByFileRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this QuickImportImageByFileRequestBody.

        :return: The enterprise_project_id of this QuickImportImageByFileRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this QuickImportImageByFileRequestBody.

        :param enterprise_project_id: The enterprise_project_id of this QuickImportImageByFileRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def architecture(self):
        """Gets the architecture of this QuickImportImageByFileRequestBody.

        :return: The architecture of this QuickImportImageByFileRequestBody.
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        """Sets the architecture of this QuickImportImageByFileRequestBody.

        :param architecture: The architecture of this QuickImportImageByFileRequestBody.
        :type architecture: str
        """
        self._architecture = architecture

    @property
    def os_type(self):
        """Gets the os_type of this QuickImportImageByFileRequestBody.

        :return: The os_type of this QuickImportImageByFileRequestBody.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this QuickImportImageByFileRequestBody.

        :param os_type: The os_type of this QuickImportImageByFileRequestBody.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def image_tags(self):
        """Gets the image_tags of this QuickImportImageByFileRequestBody.

        :return: The image_tags of this QuickImportImageByFileRequestBody.
        :rtype: list[:class:`g42cloudsdkims.v2.ResourceTag`]
        """
        return self._image_tags

    @image_tags.setter
    def image_tags(self, image_tags):
        """Sets the image_tags of this QuickImportImageByFileRequestBody.

        :param image_tags: The image_tags of this QuickImportImageByFileRequestBody.
        :type image_tags: list[:class:`g42cloudsdkims.v2.ResourceTag`]
        """
        self._image_tags = image_tags

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
        if not isinstance(other, QuickImportImageByFileRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
