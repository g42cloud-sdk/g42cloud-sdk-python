# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class TargetDisk:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'device_use': 'str',
        'disk_id': 'str',
        'name': 'str',
        'physical_volumes': 'list[TargetPhysicalVolumes]',
        'size': 'int',
        'used_size': 'int',
        'disk_index': 'str',
        'os_disk': 'bool',
        'partition_style': 'str',
        'relation_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'device_use': 'device_use',
        'disk_id': 'disk_id',
        'name': 'name',
        'physical_volumes': 'physical_volumes',
        'size': 'size',
        'used_size': 'used_size',
        'disk_index': 'disk_index',
        'os_disk': 'os_disk',
        'partition_style': 'partition_style',
        'relation_name': 'relation_name'
    }

    def __init__(self, id=None, device_use=None, disk_id=None, name=None, physical_volumes=None, size=None, used_size=None, disk_index=None, os_disk=None, partition_style=None, relation_name=None):
        """TargetDisk

        The model defined in g42cloud sdk

        :param id: The param of the TargetDisk
        :type id: int
        :param device_use: The param of the TargetDisk
        :type device_use: str
        :param disk_id: The param of the TargetDisk
        :type disk_id: str
        :param name: The param of the TargetDisk
        :type name: str
        :param physical_volumes: The param of the TargetDisk
        :type physical_volumes: list[:class:`g42cloudsdksms.v3.TargetPhysicalVolumes`]
        :param size: The param of the TargetDisk
        :type size: int
        :param used_size: The param of the TargetDisk
        :type used_size: int
        :param disk_index: The param of the TargetDisk
        :type disk_index: str
        :param os_disk: The param of the TargetDisk
        :type os_disk: bool
        :param partition_style: The param of the TargetDisk
        :type partition_style: str
        :param relation_name: The param of the TargetDisk
        :type relation_name: str
        """
        
        

        self._id = None
        self._device_use = None
        self._disk_id = None
        self._name = None
        self._physical_volumes = None
        self._size = None
        self._used_size = None
        self._disk_index = None
        self._os_disk = None
        self._partition_style = None
        self._relation_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if device_use is not None:
            self.device_use = device_use
        if disk_id is not None:
            self.disk_id = disk_id
        if name is not None:
            self.name = name
        if physical_volumes is not None:
            self.physical_volumes = physical_volumes
        if size is not None:
            self.size = size
        if used_size is not None:
            self.used_size = used_size
        if disk_index is not None:
            self.disk_index = disk_index
        if os_disk is not None:
            self.os_disk = os_disk
        if partition_style is not None:
            self.partition_style = partition_style
        if relation_name is not None:
            self.relation_name = relation_name

    @property
    def id(self):
        """Gets the id of this TargetDisk.

        :return: The id of this TargetDisk.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TargetDisk.

        :param id: The id of this TargetDisk.
        :type id: int
        """
        self._id = id

    @property
    def device_use(self):
        """Gets the device_use of this TargetDisk.

        :return: The device_use of this TargetDisk.
        :rtype: str
        """
        return self._device_use

    @device_use.setter
    def device_use(self, device_use):
        """Sets the device_use of this TargetDisk.

        :param device_use: The device_use of this TargetDisk.
        :type device_use: str
        """
        self._device_use = device_use

    @property
    def disk_id(self):
        """Gets the disk_id of this TargetDisk.

        :return: The disk_id of this TargetDisk.
        :rtype: str
        """
        return self._disk_id

    @disk_id.setter
    def disk_id(self, disk_id):
        """Sets the disk_id of this TargetDisk.

        :param disk_id: The disk_id of this TargetDisk.
        :type disk_id: str
        """
        self._disk_id = disk_id

    @property
    def name(self):
        """Gets the name of this TargetDisk.

        :return: The name of this TargetDisk.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TargetDisk.

        :param name: The name of this TargetDisk.
        :type name: str
        """
        self._name = name

    @property
    def physical_volumes(self):
        """Gets the physical_volumes of this TargetDisk.

        :return: The physical_volumes of this TargetDisk.
        :rtype: list[:class:`g42cloudsdksms.v3.TargetPhysicalVolumes`]
        """
        return self._physical_volumes

    @physical_volumes.setter
    def physical_volumes(self, physical_volumes):
        """Sets the physical_volumes of this TargetDisk.

        :param physical_volumes: The physical_volumes of this TargetDisk.
        :type physical_volumes: list[:class:`g42cloudsdksms.v3.TargetPhysicalVolumes`]
        """
        self._physical_volumes = physical_volumes

    @property
    def size(self):
        """Gets the size of this TargetDisk.

        :return: The size of this TargetDisk.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this TargetDisk.

        :param size: The size of this TargetDisk.
        :type size: int
        """
        self._size = size

    @property
    def used_size(self):
        """Gets the used_size of this TargetDisk.

        :return: The used_size of this TargetDisk.
        :rtype: int
        """
        return self._used_size

    @used_size.setter
    def used_size(self, used_size):
        """Sets the used_size of this TargetDisk.

        :param used_size: The used_size of this TargetDisk.
        :type used_size: int
        """
        self._used_size = used_size

    @property
    def disk_index(self):
        """Gets the disk_index of this TargetDisk.

        :return: The disk_index of this TargetDisk.
        :rtype: str
        """
        return self._disk_index

    @disk_index.setter
    def disk_index(self, disk_index):
        """Sets the disk_index of this TargetDisk.

        :param disk_index: The disk_index of this TargetDisk.
        :type disk_index: str
        """
        self._disk_index = disk_index

    @property
    def os_disk(self):
        """Gets the os_disk of this TargetDisk.

        :return: The os_disk of this TargetDisk.
        :rtype: bool
        """
        return self._os_disk

    @os_disk.setter
    def os_disk(self, os_disk):
        """Sets the os_disk of this TargetDisk.

        :param os_disk: The os_disk of this TargetDisk.
        :type os_disk: bool
        """
        self._os_disk = os_disk

    @property
    def partition_style(self):
        """Gets the partition_style of this TargetDisk.

        :return: The partition_style of this TargetDisk.
        :rtype: str
        """
        return self._partition_style

    @partition_style.setter
    def partition_style(self, partition_style):
        """Sets the partition_style of this TargetDisk.

        :param partition_style: The partition_style of this TargetDisk.
        :type partition_style: str
        """
        self._partition_style = partition_style

    @property
    def relation_name(self):
        """Gets the relation_name of this TargetDisk.

        :return: The relation_name of this TargetDisk.
        :rtype: str
        """
        return self._relation_name

    @relation_name.setter
    def relation_name(self, relation_name):
        """Sets the relation_name of this TargetDisk.

        :param relation_name: The relation_name of this TargetDisk.
        :type relation_name: str
        """
        self._relation_name = relation_name

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
        if not isinstance(other, TargetDisk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
