# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerFlavor:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'disk': 'str',
        'vcpus': 'str',
        'ram': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'disk': 'disk',
        'vcpus': 'vcpus',
        'ram': 'ram'
    }

    def __init__(self, id=None, name=None, disk=None, vcpus=None, ram=None):
        """ServerFlavor

        The model defined in g42cloud sdk

        :param id: The param of the ServerFlavor
        :type id: str
        :param name: The param of the ServerFlavor
        :type name: str
        :param disk: The param of the ServerFlavor
        :type disk: str
        :param vcpus: The param of the ServerFlavor
        :type vcpus: str
        :param ram: The param of the ServerFlavor
        :type ram: str
        """
        
        

        self._id = None
        self._name = None
        self._disk = None
        self._vcpus = None
        self._ram = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.disk = disk
        self.vcpus = vcpus
        self.ram = ram

    @property
    def id(self):
        """Gets the id of this ServerFlavor.

        :return: The id of this ServerFlavor.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ServerFlavor.

        :param id: The id of this ServerFlavor.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ServerFlavor.

        :return: The name of this ServerFlavor.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ServerFlavor.

        :param name: The name of this ServerFlavor.
        :type name: str
        """
        self._name = name

    @property
    def disk(self):
        """Gets the disk of this ServerFlavor.

        :return: The disk of this ServerFlavor.
        :rtype: str
        """
        return self._disk

    @disk.setter
    def disk(self, disk):
        """Sets the disk of this ServerFlavor.

        :param disk: The disk of this ServerFlavor.
        :type disk: str
        """
        self._disk = disk

    @property
    def vcpus(self):
        """Gets the vcpus of this ServerFlavor.

        :return: The vcpus of this ServerFlavor.
        :rtype: str
        """
        return self._vcpus

    @vcpus.setter
    def vcpus(self, vcpus):
        """Sets the vcpus of this ServerFlavor.

        :param vcpus: The vcpus of this ServerFlavor.
        :type vcpus: str
        """
        self._vcpus = vcpus

    @property
    def ram(self):
        """Gets the ram of this ServerFlavor.

        :return: The ram of this ServerFlavor.
        :rtype: str
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this ServerFlavor.

        :param ram: The ram of this ServerFlavor.
        :type ram: str
        """
        self._ram = ram

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
        if not isinstance(other, ServerFlavor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
