# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDataImageRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cmk_id': 'str',
        'description': 'str',
        'enterprise_project_id': 'str',
        'image_tags': 'list[ImageTag]',
        'image_url': 'str',
        'min_disk': 'int',
        'name': 'str',
        'os_type': 'str',
        'tags': 'list[str]'
    }

    attribute_map = {
        'cmk_id': 'cmk_id',
        'description': 'description',
        'enterprise_project_id': 'enterprise_project_id',
        'image_tags': 'image_tags',
        'image_url': 'image_url',
        'min_disk': 'min_disk',
        'name': 'name',
        'os_type': 'os_type',
        'tags': 'tags'
    }

    def __init__(self, cmk_id=None, description=None, enterprise_project_id=None, image_tags=None, image_url=None, min_disk=None, name=None, os_type=None, tags=None):
        """CreateDataImageRequestBody

        The model defined in g42cloud sdk

        :param cmk_id: The param of the CreateDataImageRequestBody
        :type cmk_id: str
        :param description: The param of the CreateDataImageRequestBody
        :type description: str
        :param enterprise_project_id: The param of the CreateDataImageRequestBody
        :type enterprise_project_id: str
        :param image_tags: The param of the CreateDataImageRequestBody
        :type image_tags: list[:class:`g42cloudsdkims.v2.ImageTag`]
        :param image_url: The param of the CreateDataImageRequestBody
        :type image_url: str
        :param min_disk: The param of the CreateDataImageRequestBody
        :type min_disk: int
        :param name: The param of the CreateDataImageRequestBody
        :type name: str
        :param os_type: The param of the CreateDataImageRequestBody
        :type os_type: str
        :param tags: The param of the CreateDataImageRequestBody
        :type tags: list[str]
        """
        
        

        self._cmk_id = None
        self._description = None
        self._enterprise_project_id = None
        self._image_tags = None
        self._image_url = None
        self._min_disk = None
        self._name = None
        self._os_type = None
        self._tags = None
        self.discriminator = None

        if cmk_id is not None:
            self.cmk_id = cmk_id
        if description is not None:
            self.description = description
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if image_tags is not None:
            self.image_tags = image_tags
        self.image_url = image_url
        self.min_disk = min_disk
        self.name = name
        if os_type is not None:
            self.os_type = os_type
        if tags is not None:
            self.tags = tags

    @property
    def cmk_id(self):
        """Gets the cmk_id of this CreateDataImageRequestBody.

        :return: The cmk_id of this CreateDataImageRequestBody.
        :rtype: str
        """
        return self._cmk_id

    @cmk_id.setter
    def cmk_id(self, cmk_id):
        """Sets the cmk_id of this CreateDataImageRequestBody.

        :param cmk_id: The cmk_id of this CreateDataImageRequestBody.
        :type cmk_id: str
        """
        self._cmk_id = cmk_id

    @property
    def description(self):
        """Gets the description of this CreateDataImageRequestBody.

        :return: The description of this CreateDataImageRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateDataImageRequestBody.

        :param description: The description of this CreateDataImageRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateDataImageRequestBody.

        :return: The enterprise_project_id of this CreateDataImageRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateDataImageRequestBody.

        :param enterprise_project_id: The enterprise_project_id of this CreateDataImageRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def image_tags(self):
        """Gets the image_tags of this CreateDataImageRequestBody.

        :return: The image_tags of this CreateDataImageRequestBody.
        :rtype: list[:class:`g42cloudsdkims.v2.ImageTag`]
        """
        return self._image_tags

    @image_tags.setter
    def image_tags(self, image_tags):
        """Sets the image_tags of this CreateDataImageRequestBody.

        :param image_tags: The image_tags of this CreateDataImageRequestBody.
        :type image_tags: list[:class:`g42cloudsdkims.v2.ImageTag`]
        """
        self._image_tags = image_tags

    @property
    def image_url(self):
        """Gets the image_url of this CreateDataImageRequestBody.

        :return: The image_url of this CreateDataImageRequestBody.
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this CreateDataImageRequestBody.

        :param image_url: The image_url of this CreateDataImageRequestBody.
        :type image_url: str
        """
        self._image_url = image_url

    @property
    def min_disk(self):
        """Gets the min_disk of this CreateDataImageRequestBody.

        :return: The min_disk of this CreateDataImageRequestBody.
        :rtype: int
        """
        return self._min_disk

    @min_disk.setter
    def min_disk(self, min_disk):
        """Sets the min_disk of this CreateDataImageRequestBody.

        :param min_disk: The min_disk of this CreateDataImageRequestBody.
        :type min_disk: int
        """
        self._min_disk = min_disk

    @property
    def name(self):
        """Gets the name of this CreateDataImageRequestBody.

        :return: The name of this CreateDataImageRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateDataImageRequestBody.

        :param name: The name of this CreateDataImageRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def os_type(self):
        """Gets the os_type of this CreateDataImageRequestBody.

        :return: The os_type of this CreateDataImageRequestBody.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this CreateDataImageRequestBody.

        :param os_type: The os_type of this CreateDataImageRequestBody.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def tags(self):
        """Gets the tags of this CreateDataImageRequestBody.

        :return: The tags of this CreateDataImageRequestBody.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateDataImageRequestBody.

        :param tags: The tags of this CreateDataImageRequestBody.
        :type tags: list[str]
        """
        self._tags = tags

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
        if not isinstance(other, CreateDataImageRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
