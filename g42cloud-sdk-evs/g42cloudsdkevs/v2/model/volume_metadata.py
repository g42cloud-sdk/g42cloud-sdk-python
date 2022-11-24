# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VolumeMetadata:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'system__cmkid': 'str',
        'system__encrypted': 'str',
        'full_clone': 'str',
        'hwpassthrough': 'str',
        'order_id': 'str'
    }

    attribute_map = {
        'system__cmkid': '__system__cmkid',
        'system__encrypted': '__system__encrypted',
        'full_clone': 'full_clone',
        'hwpassthrough': 'hw:passthrough',
        'order_id': 'orderID'
    }

    def __init__(self, system__cmkid=None, system__encrypted=None, full_clone=None, hwpassthrough=None, order_id=None):
        """VolumeMetadata

        The model defined in g42cloud sdk

        :param system__cmkid: The param of the VolumeMetadata
        :type system__cmkid: str
        :param system__encrypted: The param of the VolumeMetadata
        :type system__encrypted: str
        :param full_clone: The param of the VolumeMetadata
        :type full_clone: str
        :param hwpassthrough: The param of the VolumeMetadata
        :type hwpassthrough: str
        :param order_id: The param of the VolumeMetadata
        :type order_id: str
        """
        
        

        self._system__cmkid = None
        self._system__encrypted = None
        self._full_clone = None
        self._hwpassthrough = None
        self._order_id = None
        self.discriminator = None

        if system__cmkid is not None:
            self.system__cmkid = system__cmkid
        if system__encrypted is not None:
            self.system__encrypted = system__encrypted
        if full_clone is not None:
            self.full_clone = full_clone
        if hwpassthrough is not None:
            self.hwpassthrough = hwpassthrough
        if order_id is not None:
            self.order_id = order_id

    @property
    def system__cmkid(self):
        """Gets the system__cmkid of this VolumeMetadata.

        :return: The system__cmkid of this VolumeMetadata.
        :rtype: str
        """
        return self._system__cmkid

    @system__cmkid.setter
    def system__cmkid(self, system__cmkid):
        """Sets the system__cmkid of this VolumeMetadata.

        :param system__cmkid: The system__cmkid of this VolumeMetadata.
        :type system__cmkid: str
        """
        self._system__cmkid = system__cmkid

    @property
    def system__encrypted(self):
        """Gets the system__encrypted of this VolumeMetadata.

        :return: The system__encrypted of this VolumeMetadata.
        :rtype: str
        """
        return self._system__encrypted

    @system__encrypted.setter
    def system__encrypted(self, system__encrypted):
        """Sets the system__encrypted of this VolumeMetadata.

        :param system__encrypted: The system__encrypted of this VolumeMetadata.
        :type system__encrypted: str
        """
        self._system__encrypted = system__encrypted

    @property
    def full_clone(self):
        """Gets the full_clone of this VolumeMetadata.

        :return: The full_clone of this VolumeMetadata.
        :rtype: str
        """
        return self._full_clone

    @full_clone.setter
    def full_clone(self, full_clone):
        """Sets the full_clone of this VolumeMetadata.

        :param full_clone: The full_clone of this VolumeMetadata.
        :type full_clone: str
        """
        self._full_clone = full_clone

    @property
    def hwpassthrough(self):
        """Gets the hwpassthrough of this VolumeMetadata.

        :return: The hwpassthrough of this VolumeMetadata.
        :rtype: str
        """
        return self._hwpassthrough

    @hwpassthrough.setter
    def hwpassthrough(self, hwpassthrough):
        """Sets the hwpassthrough of this VolumeMetadata.

        :param hwpassthrough: The hwpassthrough of this VolumeMetadata.
        :type hwpassthrough: str
        """
        self._hwpassthrough = hwpassthrough

    @property
    def order_id(self):
        """Gets the order_id of this VolumeMetadata.

        :return: The order_id of this VolumeMetadata.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this VolumeMetadata.

        :param order_id: The order_id of this VolumeMetadata.
        :type order_id: str
        """
        self._order_id = order_id

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
        if not isinstance(other, VolumeMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
