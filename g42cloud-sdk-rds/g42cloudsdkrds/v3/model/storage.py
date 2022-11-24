# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Storage:

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
        'az_status': 'dict(str, str)',
        'support_compute_group_type': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'az_status': 'az_status',
        'support_compute_group_type': 'support_compute_group_type'
    }

    def __init__(self, name=None, az_status=None, support_compute_group_type=None):
        """Storage

        The model defined in g42cloud sdk

        :param name: The param of the Storage
        :type name: str
        :param az_status: The param of the Storage
        :type az_status: dict(str, str)
        :param support_compute_group_type: The param of the Storage
        :type support_compute_group_type: list[str]
        """
        
        

        self._name = None
        self._az_status = None
        self._support_compute_group_type = None
        self.discriminator = None

        self.name = name
        self.az_status = az_status
        if support_compute_group_type is not None:
            self.support_compute_group_type = support_compute_group_type

    @property
    def name(self):
        """Gets the name of this Storage.

        :return: The name of this Storage.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Storage.

        :param name: The name of this Storage.
        :type name: str
        """
        self._name = name

    @property
    def az_status(self):
        """Gets the az_status of this Storage.

        :return: The az_status of this Storage.
        :rtype: dict(str, str)
        """
        return self._az_status

    @az_status.setter
    def az_status(self, az_status):
        """Sets the az_status of this Storage.

        :param az_status: The az_status of this Storage.
        :type az_status: dict(str, str)
        """
        self._az_status = az_status

    @property
    def support_compute_group_type(self):
        """Gets the support_compute_group_type of this Storage.

        :return: The support_compute_group_type of this Storage.
        :rtype: list[str]
        """
        return self._support_compute_group_type

    @support_compute_group_type.setter
    def support_compute_group_type(self, support_compute_group_type):
        """Sets the support_compute_group_type of this Storage.

        :param support_compute_group_type: The support_compute_group_type of this Storage.
        :type support_compute_group_type: list[str]
        """
        self._support_compute_group_type = support_compute_group_type

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
        if not isinstance(other, Storage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
