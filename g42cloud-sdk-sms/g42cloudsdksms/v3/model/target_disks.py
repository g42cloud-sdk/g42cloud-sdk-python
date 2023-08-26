# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class TargetDisks:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'device_use': 'str',
        'disk_id': 'str',
        'name': 'str',
        'physical_volumes': 'list[PhysicalVolumes]',
        'size': 'int',
        'used_size': 'int'
    }

    attribute_map = {
        'device_use': 'device_use',
        'disk_id': 'disk_id',
        'name': 'name',
        'physical_volumes': 'physical_volumes',
        'size': 'size',
        'used_size': 'used_size'
    }

    def __init__(self, device_use=None, disk_id=None, name=None, physical_volumes=None, size=None, used_size=None):
        """TargetDisks

        The model defined in g42cloud sdk

        :param device_use: The param of the TargetDisks
        :type device_use: str
        :param disk_id: The param of the TargetDisks
        :type disk_id: str
        :param name: The param of the TargetDisks
        :type name: str
        :param physical_volumes: The param of the TargetDisks
        :type physical_volumes: list[:class:`g42cloudsdksms.v3.PhysicalVolumes`]
        :param size: The param of the TargetDisks
        :type size: int
        :param used_size: The param of the TargetDisks
        :type used_size: int
        """
        
        

        self._device_use = None
        self._disk_id = None
        self._name = None
        self._physical_volumes = None
        self._size = None
        self._used_size = None
        self.discriminator = None

        if device_use is not None:
            self.device_use = device_use
        if disk_id is not None:
            self.disk_id = disk_id
        self.name = name
        self.physical_volumes = physical_volumes
        self.size = size
        self.used_size = used_size

    @property
    def device_use(self):
        """Gets the device_use of this TargetDisks.

        :return: The device_use of this TargetDisks.
        :rtype: str
        """
        return self._device_use

    @device_use.setter
    def device_use(self, device_use):
        """Sets the device_use of this TargetDisks.

        :param device_use: The device_use of this TargetDisks.
        :type device_use: str
        """
        self._device_use = device_use

    @property
    def disk_id(self):
        """Gets the disk_id of this TargetDisks.

        :return: The disk_id of this TargetDisks.
        :rtype: str
        """
        return self._disk_id

    @disk_id.setter
    def disk_id(self, disk_id):
        """Sets the disk_id of this TargetDisks.

        :param disk_id: The disk_id of this TargetDisks.
        :type disk_id: str
        """
        self._disk_id = disk_id

    @property
    def name(self):
        """Gets the name of this TargetDisks.

        :return: The name of this TargetDisks.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TargetDisks.

        :param name: The name of this TargetDisks.
        :type name: str
        """
        self._name = name

    @property
    def physical_volumes(self):
        """Gets the physical_volumes of this TargetDisks.

        :return: The physical_volumes of this TargetDisks.
        :rtype: list[:class:`g42cloudsdksms.v3.PhysicalVolumes`]
        """
        return self._physical_volumes

    @physical_volumes.setter
    def physical_volumes(self, physical_volumes):
        """Sets the physical_volumes of this TargetDisks.

        :param physical_volumes: The physical_volumes of this TargetDisks.
        :type physical_volumes: list[:class:`g42cloudsdksms.v3.PhysicalVolumes`]
        """
        self._physical_volumes = physical_volumes

    @property
    def size(self):
        """Gets the size of this TargetDisks.

        :return: The size of this TargetDisks.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this TargetDisks.

        :param size: The size of this TargetDisks.
        :type size: int
        """
        self._size = size

    @property
    def used_size(self):
        """Gets the used_size of this TargetDisks.

        :return: The used_size of this TargetDisks.
        :rtype: int
        """
        return self._used_size

    @used_size.setter
    def used_size(self, used_size):
        """Sets the used_size of this TargetDisks.

        :param used_size: The used_size of this TargetDisks.
        :type used_size: int
        """
        self._used_size = used_size

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
        if not isinstance(other, TargetDisks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
