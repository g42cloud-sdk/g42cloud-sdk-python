# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttachServerVolumeOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'device': 'str',
        'volume_id': 'str',
        'volume_type': 'str',
        'count': 'int',
        'hwpassthrough': 'str'
    }

    attribute_map = {
        'device': 'device',
        'volume_id': 'volumeId',
        'volume_type': 'volume_type',
        'count': 'count',
        'hwpassthrough': 'hw:passthrough'
    }

    def __init__(self, device=None, volume_id=None, volume_type=None, count=None, hwpassthrough=None):
        """AttachServerVolumeOption

        The model defined in g42cloud sdk

        :param device: The param of the AttachServerVolumeOption
        :type device: str
        :param volume_id: The param of the AttachServerVolumeOption
        :type volume_id: str
        :param volume_type: The param of the AttachServerVolumeOption
        :type volume_type: str
        :param count: The param of the AttachServerVolumeOption
        :type count: int
        :param hwpassthrough: The param of the AttachServerVolumeOption
        :type hwpassthrough: str
        """
        
        

        self._device = None
        self._volume_id = None
        self._volume_type = None
        self._count = None
        self._hwpassthrough = None
        self.discriminator = None

        if device is not None:
            self.device = device
        self.volume_id = volume_id
        if volume_type is not None:
            self.volume_type = volume_type
        if count is not None:
            self.count = count
        if hwpassthrough is not None:
            self.hwpassthrough = hwpassthrough

    @property
    def device(self):
        """Gets the device of this AttachServerVolumeOption.

        :return: The device of this AttachServerVolumeOption.
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this AttachServerVolumeOption.

        :param device: The device of this AttachServerVolumeOption.
        :type device: str
        """
        self._device = device

    @property
    def volume_id(self):
        """Gets the volume_id of this AttachServerVolumeOption.

        :return: The volume_id of this AttachServerVolumeOption.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """Sets the volume_id of this AttachServerVolumeOption.

        :param volume_id: The volume_id of this AttachServerVolumeOption.
        :type volume_id: str
        """
        self._volume_id = volume_id

    @property
    def volume_type(self):
        """Gets the volume_type of this AttachServerVolumeOption.

        :return: The volume_type of this AttachServerVolumeOption.
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        """Sets the volume_type of this AttachServerVolumeOption.

        :param volume_type: The volume_type of this AttachServerVolumeOption.
        :type volume_type: str
        """
        self._volume_type = volume_type

    @property
    def count(self):
        """Gets the count of this AttachServerVolumeOption.

        :return: The count of this AttachServerVolumeOption.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this AttachServerVolumeOption.

        :param count: The count of this AttachServerVolumeOption.
        :type count: int
        """
        self._count = count

    @property
    def hwpassthrough(self):
        """Gets the hwpassthrough of this AttachServerVolumeOption.

        :return: The hwpassthrough of this AttachServerVolumeOption.
        :rtype: str
        """
        return self._hwpassthrough

    @hwpassthrough.setter
    def hwpassthrough(self, hwpassthrough):
        """Sets the hwpassthrough of this AttachServerVolumeOption.

        :param hwpassthrough: The hwpassthrough of this AttachServerVolumeOption.
        :type hwpassthrough: str
        """
        self._hwpassthrough = hwpassthrough

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
        if not isinstance(other, AttachServerVolumeOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
