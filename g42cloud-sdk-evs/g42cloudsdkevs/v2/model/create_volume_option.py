# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateVolumeOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'availability_zone': 'str',
        'backup_id': 'str',
        'count': 'int',
        'description': 'str',
        'enterprise_project_id': 'str',
        'image_ref': 'str',
        'metadata': 'dict(str, str)',
        'multiattach': 'bool',
        'name': 'str',
        'size': 'int',
        'snapshot_id': 'str',
        'volume_type': 'str',
        'tags': 'dict(str, str)'
    }

    attribute_map = {
        'availability_zone': 'availability_zone',
        'backup_id': 'backup_id',
        'count': 'count',
        'description': 'description',
        'enterprise_project_id': 'enterprise_project_id',
        'image_ref': 'imageRef',
        'metadata': 'metadata',
        'multiattach': 'multiattach',
        'name': 'name',
        'size': 'size',
        'snapshot_id': 'snapshot_id',
        'volume_type': 'volume_type',
        'tags': 'tags'
    }

    def __init__(self, availability_zone=None, backup_id=None, count=None, description=None, enterprise_project_id=None, image_ref=None, metadata=None, multiattach=None, name=None, size=None, snapshot_id=None, volume_type=None, tags=None):
        """CreateVolumeOption

        The model defined in g42cloud sdk

        :param availability_zone: The param of the CreateVolumeOption
        :type availability_zone: str
        :param backup_id: The param of the CreateVolumeOption
        :type backup_id: str
        :param count: The param of the CreateVolumeOption
        :type count: int
        :param description: The param of the CreateVolumeOption
        :type description: str
        :param enterprise_project_id: The param of the CreateVolumeOption
        :type enterprise_project_id: str
        :param image_ref: The param of the CreateVolumeOption
        :type image_ref: str
        :param metadata: The param of the CreateVolumeOption
        :type metadata: dict(str, str)
        :param multiattach: The param of the CreateVolumeOption
        :type multiattach: bool
        :param name: The param of the CreateVolumeOption
        :type name: str
        :param size: The param of the CreateVolumeOption
        :type size: int
        :param snapshot_id: The param of the CreateVolumeOption
        :type snapshot_id: str
        :param volume_type: The param of the CreateVolumeOption
        :type volume_type: str
        :param tags: The param of the CreateVolumeOption
        :type tags: dict(str, str)
        """
        
        

        self._availability_zone = None
        self._backup_id = None
        self._count = None
        self._description = None
        self._enterprise_project_id = None
        self._image_ref = None
        self._metadata = None
        self._multiattach = None
        self._name = None
        self._size = None
        self._snapshot_id = None
        self._volume_type = None
        self._tags = None
        self.discriminator = None

        self.availability_zone = availability_zone
        if backup_id is not None:
            self.backup_id = backup_id
        if count is not None:
            self.count = count
        if description is not None:
            self.description = description
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if image_ref is not None:
            self.image_ref = image_ref
        if metadata is not None:
            self.metadata = metadata
        if multiattach is not None:
            self.multiattach = multiattach
        if name is not None:
            self.name = name
        self.size = size
        if snapshot_id is not None:
            self.snapshot_id = snapshot_id
        self.volume_type = volume_type
        if tags is not None:
            self.tags = tags

    @property
    def availability_zone(self):
        """Gets the availability_zone of this CreateVolumeOption.

        :return: The availability_zone of this CreateVolumeOption.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this CreateVolumeOption.

        :param availability_zone: The availability_zone of this CreateVolumeOption.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def backup_id(self):
        """Gets the backup_id of this CreateVolumeOption.

        :return: The backup_id of this CreateVolumeOption.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        """Sets the backup_id of this CreateVolumeOption.

        :param backup_id: The backup_id of this CreateVolumeOption.
        :type backup_id: str
        """
        self._backup_id = backup_id

    @property
    def count(self):
        """Gets the count of this CreateVolumeOption.

        :return: The count of this CreateVolumeOption.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this CreateVolumeOption.

        :param count: The count of this CreateVolumeOption.
        :type count: int
        """
        self._count = count

    @property
    def description(self):
        """Gets the description of this CreateVolumeOption.

        :return: The description of this CreateVolumeOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateVolumeOption.

        :param description: The description of this CreateVolumeOption.
        :type description: str
        """
        self._description = description

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateVolumeOption.

        :return: The enterprise_project_id of this CreateVolumeOption.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateVolumeOption.

        :param enterprise_project_id: The enterprise_project_id of this CreateVolumeOption.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def image_ref(self):
        """Gets the image_ref of this CreateVolumeOption.

        :return: The image_ref of this CreateVolumeOption.
        :rtype: str
        """
        return self._image_ref

    @image_ref.setter
    def image_ref(self, image_ref):
        """Sets the image_ref of this CreateVolumeOption.

        :param image_ref: The image_ref of this CreateVolumeOption.
        :type image_ref: str
        """
        self._image_ref = image_ref

    @property
    def metadata(self):
        """Gets the metadata of this CreateVolumeOption.

        :return: The metadata of this CreateVolumeOption.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this CreateVolumeOption.

        :param metadata: The metadata of this CreateVolumeOption.
        :type metadata: dict(str, str)
        """
        self._metadata = metadata

    @property
    def multiattach(self):
        """Gets the multiattach of this CreateVolumeOption.

        :return: The multiattach of this CreateVolumeOption.
        :rtype: bool
        """
        return self._multiattach

    @multiattach.setter
    def multiattach(self, multiattach):
        """Sets the multiattach of this CreateVolumeOption.

        :param multiattach: The multiattach of this CreateVolumeOption.
        :type multiattach: bool
        """
        self._multiattach = multiattach

    @property
    def name(self):
        """Gets the name of this CreateVolumeOption.

        :return: The name of this CreateVolumeOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateVolumeOption.

        :param name: The name of this CreateVolumeOption.
        :type name: str
        """
        self._name = name

    @property
    def size(self):
        """Gets the size of this CreateVolumeOption.

        :return: The size of this CreateVolumeOption.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this CreateVolumeOption.

        :param size: The size of this CreateVolumeOption.
        :type size: int
        """
        self._size = size

    @property
    def snapshot_id(self):
        """Gets the snapshot_id of this CreateVolumeOption.

        :return: The snapshot_id of this CreateVolumeOption.
        :rtype: str
        """
        return self._snapshot_id

    @snapshot_id.setter
    def snapshot_id(self, snapshot_id):
        """Sets the snapshot_id of this CreateVolumeOption.

        :param snapshot_id: The snapshot_id of this CreateVolumeOption.
        :type snapshot_id: str
        """
        self._snapshot_id = snapshot_id

    @property
    def volume_type(self):
        """Gets the volume_type of this CreateVolumeOption.

        :return: The volume_type of this CreateVolumeOption.
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        """Sets the volume_type of this CreateVolumeOption.

        :param volume_type: The volume_type of this CreateVolumeOption.
        :type volume_type: str
        """
        self._volume_type = volume_type

    @property
    def tags(self):
        """Gets the tags of this CreateVolumeOption.

        :return: The tags of this CreateVolumeOption.
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateVolumeOption.

        :param tags: The tags of this CreateVolumeOption.
        :type tags: dict(str, str)
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
        if not isinstance(other, CreateVolumeOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
