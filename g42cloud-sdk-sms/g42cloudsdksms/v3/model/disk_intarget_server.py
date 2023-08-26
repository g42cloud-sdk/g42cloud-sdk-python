# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class DiskIntargetServer:

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
        'size': 'int',
        'device_use': 'str',
        'used_size': 'int',
        'physical_volumes': 'list[PhysicalVolumes]'
    }

    attribute_map = {
        'name': 'name',
        'size': 'size',
        'device_use': 'device_use',
        'used_size': 'used_size',
        'physical_volumes': 'physical_volumes'
    }

    def __init__(self, name=None, size=None, device_use=None, used_size=None, physical_volumes=None):
        """DiskIntargetServer

        The model defined in g42cloud sdk

        :param name: The param of the DiskIntargetServer
        :type name: str
        :param size: The param of the DiskIntargetServer
        :type size: int
        :param device_use: The param of the DiskIntargetServer
        :type device_use: str
        :param used_size: The param of the DiskIntargetServer
        :type used_size: int
        :param physical_volumes: The param of the DiskIntargetServer
        :type physical_volumes: list[:class:`g42cloudsdksms.v3.PhysicalVolumes`]
        """
        
        

        self._name = None
        self._size = None
        self._device_use = None
        self._used_size = None
        self._physical_volumes = None
        self.discriminator = None

        self.name = name
        self.size = size
        if device_use is not None:
            self.device_use = device_use
        if used_size is not None:
            self.used_size = used_size
        if physical_volumes is not None:
            self.physical_volumes = physical_volumes

    @property
    def name(self):
        """Gets the name of this DiskIntargetServer.

        :return: The name of this DiskIntargetServer.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DiskIntargetServer.

        :param name: The name of this DiskIntargetServer.
        :type name: str
        """
        self._name = name

    @property
    def size(self):
        """Gets the size of this DiskIntargetServer.

        :return: The size of this DiskIntargetServer.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this DiskIntargetServer.

        :param size: The size of this DiskIntargetServer.
        :type size: int
        """
        self._size = size

    @property
    def device_use(self):
        """Gets the device_use of this DiskIntargetServer.

        :return: The device_use of this DiskIntargetServer.
        :rtype: str
        """
        return self._device_use

    @device_use.setter
    def device_use(self, device_use):
        """Sets the device_use of this DiskIntargetServer.

        :param device_use: The device_use of this DiskIntargetServer.
        :type device_use: str
        """
        self._device_use = device_use

    @property
    def used_size(self):
        """Gets the used_size of this DiskIntargetServer.

        :return: The used_size of this DiskIntargetServer.
        :rtype: int
        """
        return self._used_size

    @used_size.setter
    def used_size(self, used_size):
        """Sets the used_size of this DiskIntargetServer.

        :param used_size: The used_size of this DiskIntargetServer.
        :type used_size: int
        """
        self._used_size = used_size

    @property
    def physical_volumes(self):
        """Gets the physical_volumes of this DiskIntargetServer.

        :return: The physical_volumes of this DiskIntargetServer.
        :rtype: list[:class:`g42cloudsdksms.v3.PhysicalVolumes`]
        """
        return self._physical_volumes

    @physical_volumes.setter
    def physical_volumes(self, physical_volumes):
        """Sets the physical_volumes of this DiskIntargetServer.

        :param physical_volumes: The physical_volumes of this DiskIntargetServer.
        :type physical_volumes: list[:class:`g42cloudsdksms.v3.PhysicalVolumes`]
        """
        self._physical_volumes = physical_volumes

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
        if not isinstance(other, DiskIntargetServer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
