# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateImageRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_images': 'list[CreateDataImage]',
        'description': 'str',
        'enterprise_project_id': 'str',
        'image_tags': 'list[TagKeyValue]',
        'instance_id': 'str',
        'name': 'str',
        'tags': 'list[str]',
        'max_ram': 'int',
        'min_ram': 'int',
        'os_version': 'str',
        'image_url': 'str',
        'min_disk': 'int',
        'is_config': 'bool',
        'cmk_id': 'str',
        'type': 'str',
        'is_quick_import': 'bool',
        'architecture': 'str',
        'volume_id': 'str'
    }

    attribute_map = {
        'data_images': 'data_images',
        'description': 'description',
        'enterprise_project_id': 'enterprise_project_id',
        'image_tags': 'image_tags',
        'instance_id': 'instance_id',
        'name': 'name',
        'tags': 'tags',
        'max_ram': 'max_ram',
        'min_ram': 'min_ram',
        'os_version': 'os_version',
        'image_url': 'image_url',
        'min_disk': 'min_disk',
        'is_config': 'is_config',
        'cmk_id': 'cmk_id',
        'type': 'type',
        'is_quick_import': 'is_quick_import',
        'architecture': 'architecture',
        'volume_id': 'volume_id'
    }

    def __init__(self, data_images=None, description=None, enterprise_project_id=None, image_tags=None, instance_id=None, name=None, tags=None, max_ram=None, min_ram=None, os_version=None, image_url=None, min_disk=None, is_config=None, cmk_id=None, type=None, is_quick_import=None, architecture=None, volume_id=None):
        """CreateImageRequestBody

        The model defined in g42cloud sdk

        :param data_images: The param of the CreateImageRequestBody
        :type data_images: list[:class:`g42cloudsdkims.v2.CreateDataImage`]
        :param description: The param of the CreateImageRequestBody
        :type description: str
        :param enterprise_project_id: The param of the CreateImageRequestBody
        :type enterprise_project_id: str
        :param image_tags: The param of the CreateImageRequestBody
        :type image_tags: list[:class:`g42cloudsdkims.v2.TagKeyValue`]
        :param instance_id: The param of the CreateImageRequestBody
        :type instance_id: str
        :param name: The param of the CreateImageRequestBody
        :type name: str
        :param tags: The param of the CreateImageRequestBody
        :type tags: list[str]
        :param max_ram: The param of the CreateImageRequestBody
        :type max_ram: int
        :param min_ram: The param of the CreateImageRequestBody
        :type min_ram: int
        :param os_version: The param of the CreateImageRequestBody
        :type os_version: str
        :param image_url: The param of the CreateImageRequestBody
        :type image_url: str
        :param min_disk: The param of the CreateImageRequestBody
        :type min_disk: int
        :param is_config: The param of the CreateImageRequestBody
        :type is_config: bool
        :param cmk_id: The param of the CreateImageRequestBody
        :type cmk_id: str
        :param type: The param of the CreateImageRequestBody
        :type type: str
        :param is_quick_import: The param of the CreateImageRequestBody
        :type is_quick_import: bool
        :param architecture: The param of the CreateImageRequestBody
        :type architecture: str
        :param volume_id: The param of the CreateImageRequestBody
        :type volume_id: str
        """
        
        

        self._data_images = None
        self._description = None
        self._enterprise_project_id = None
        self._image_tags = None
        self._instance_id = None
        self._name = None
        self._tags = None
        self._max_ram = None
        self._min_ram = None
        self._os_version = None
        self._image_url = None
        self._min_disk = None
        self._is_config = None
        self._cmk_id = None
        self._type = None
        self._is_quick_import = None
        self._architecture = None
        self._volume_id = None
        self.discriminator = None

        if data_images is not None:
            self.data_images = data_images
        if description is not None:
            self.description = description
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if image_tags is not None:
            self.image_tags = image_tags
        if instance_id is not None:
            self.instance_id = instance_id
        self.name = name
        if tags is not None:
            self.tags = tags
        if max_ram is not None:
            self.max_ram = max_ram
        if min_ram is not None:
            self.min_ram = min_ram
        if os_version is not None:
            self.os_version = os_version
        if image_url is not None:
            self.image_url = image_url
        if min_disk is not None:
            self.min_disk = min_disk
        if is_config is not None:
            self.is_config = is_config
        if cmk_id is not None:
            self.cmk_id = cmk_id
        if type is not None:
            self.type = type
        if is_quick_import is not None:
            self.is_quick_import = is_quick_import
        if architecture is not None:
            self.architecture = architecture
        if volume_id is not None:
            self.volume_id = volume_id

    @property
    def data_images(self):
        """Gets the data_images of this CreateImageRequestBody.

        :return: The data_images of this CreateImageRequestBody.
        :rtype: list[:class:`g42cloudsdkims.v2.CreateDataImage`]
        """
        return self._data_images

    @data_images.setter
    def data_images(self, data_images):
        """Sets the data_images of this CreateImageRequestBody.

        :param data_images: The data_images of this CreateImageRequestBody.
        :type data_images: list[:class:`g42cloudsdkims.v2.CreateDataImage`]
        """
        self._data_images = data_images

    @property
    def description(self):
        """Gets the description of this CreateImageRequestBody.

        :return: The description of this CreateImageRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateImageRequestBody.

        :param description: The description of this CreateImageRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateImageRequestBody.

        :return: The enterprise_project_id of this CreateImageRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateImageRequestBody.

        :param enterprise_project_id: The enterprise_project_id of this CreateImageRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def image_tags(self):
        """Gets the image_tags of this CreateImageRequestBody.

        :return: The image_tags of this CreateImageRequestBody.
        :rtype: list[:class:`g42cloudsdkims.v2.TagKeyValue`]
        """
        return self._image_tags

    @image_tags.setter
    def image_tags(self, image_tags):
        """Sets the image_tags of this CreateImageRequestBody.

        :param image_tags: The image_tags of this CreateImageRequestBody.
        :type image_tags: list[:class:`g42cloudsdkims.v2.TagKeyValue`]
        """
        self._image_tags = image_tags

    @property
    def instance_id(self):
        """Gets the instance_id of this CreateImageRequestBody.

        :return: The instance_id of this CreateImageRequestBody.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this CreateImageRequestBody.

        :param instance_id: The instance_id of this CreateImageRequestBody.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def name(self):
        """Gets the name of this CreateImageRequestBody.

        :return: The name of this CreateImageRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateImageRequestBody.

        :param name: The name of this CreateImageRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def tags(self):
        """Gets the tags of this CreateImageRequestBody.

        :return: The tags of this CreateImageRequestBody.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateImageRequestBody.

        :param tags: The tags of this CreateImageRequestBody.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def max_ram(self):
        """Gets the max_ram of this CreateImageRequestBody.

        :return: The max_ram of this CreateImageRequestBody.
        :rtype: int
        """
        return self._max_ram

    @max_ram.setter
    def max_ram(self, max_ram):
        """Sets the max_ram of this CreateImageRequestBody.

        :param max_ram: The max_ram of this CreateImageRequestBody.
        :type max_ram: int
        """
        self._max_ram = max_ram

    @property
    def min_ram(self):
        """Gets the min_ram of this CreateImageRequestBody.

        :return: The min_ram of this CreateImageRequestBody.
        :rtype: int
        """
        return self._min_ram

    @min_ram.setter
    def min_ram(self, min_ram):
        """Sets the min_ram of this CreateImageRequestBody.

        :param min_ram: The min_ram of this CreateImageRequestBody.
        :type min_ram: int
        """
        self._min_ram = min_ram

    @property
    def os_version(self):
        """Gets the os_version of this CreateImageRequestBody.

        :return: The os_version of this CreateImageRequestBody.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """Sets the os_version of this CreateImageRequestBody.

        :param os_version: The os_version of this CreateImageRequestBody.
        :type os_version: str
        """
        self._os_version = os_version

    @property
    def image_url(self):
        """Gets the image_url of this CreateImageRequestBody.

        :return: The image_url of this CreateImageRequestBody.
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this CreateImageRequestBody.

        :param image_url: The image_url of this CreateImageRequestBody.
        :type image_url: str
        """
        self._image_url = image_url

    @property
    def min_disk(self):
        """Gets the min_disk of this CreateImageRequestBody.

        :return: The min_disk of this CreateImageRequestBody.
        :rtype: int
        """
        return self._min_disk

    @min_disk.setter
    def min_disk(self, min_disk):
        """Sets the min_disk of this CreateImageRequestBody.

        :param min_disk: The min_disk of this CreateImageRequestBody.
        :type min_disk: int
        """
        self._min_disk = min_disk

    @property
    def is_config(self):
        """Gets the is_config of this CreateImageRequestBody.

        :return: The is_config of this CreateImageRequestBody.
        :rtype: bool
        """
        return self._is_config

    @is_config.setter
    def is_config(self, is_config):
        """Sets the is_config of this CreateImageRequestBody.

        :param is_config: The is_config of this CreateImageRequestBody.
        :type is_config: bool
        """
        self._is_config = is_config

    @property
    def cmk_id(self):
        """Gets the cmk_id of this CreateImageRequestBody.

        :return: The cmk_id of this CreateImageRequestBody.
        :rtype: str
        """
        return self._cmk_id

    @cmk_id.setter
    def cmk_id(self, cmk_id):
        """Sets the cmk_id of this CreateImageRequestBody.

        :param cmk_id: The cmk_id of this CreateImageRequestBody.
        :type cmk_id: str
        """
        self._cmk_id = cmk_id

    @property
    def type(self):
        """Gets the type of this CreateImageRequestBody.

        :return: The type of this CreateImageRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateImageRequestBody.

        :param type: The type of this CreateImageRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def is_quick_import(self):
        """Gets the is_quick_import of this CreateImageRequestBody.

        :return: The is_quick_import of this CreateImageRequestBody.
        :rtype: bool
        """
        return self._is_quick_import

    @is_quick_import.setter
    def is_quick_import(self, is_quick_import):
        """Sets the is_quick_import of this CreateImageRequestBody.

        :param is_quick_import: The is_quick_import of this CreateImageRequestBody.
        :type is_quick_import: bool
        """
        self._is_quick_import = is_quick_import

    @property
    def architecture(self):
        """Gets the architecture of this CreateImageRequestBody.

        :return: The architecture of this CreateImageRequestBody.
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        """Sets the architecture of this CreateImageRequestBody.

        :param architecture: The architecture of this CreateImageRequestBody.
        :type architecture: str
        """
        self._architecture = architecture

    @property
    def volume_id(self):
        """Gets the volume_id of this CreateImageRequestBody.

        :return: The volume_id of this CreateImageRequestBody.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """Sets the volume_id of this CreateImageRequestBody.

        :param volume_id: The volume_id of this CreateImageRequestBody.
        :type volume_id: str
        """
        self._volume_id = volume_id

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
        if not isinstance(other, CreateImageRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
