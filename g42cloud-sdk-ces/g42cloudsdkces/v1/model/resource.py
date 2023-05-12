# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class Resource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'used': 'int',
        'unit': 'str',
        'quota': 'int'
    }

    attribute_map = {
        'type': 'type',
        'used': 'used',
        'unit': 'unit',
        'quota': 'quota'
    }

    def __init__(self, type=None, used=None, unit=None, quota=None):
        """Resource

        The model defined in g42cloud sdk

        :param type: The param of the Resource
        :type type: str
        :param used: The param of the Resource
        :type used: int
        :param unit: The param of the Resource
        :type unit: str
        :param quota: The param of the Resource
        :type quota: int
        """
        
        

        self._type = None
        self._used = None
        self._unit = None
        self._quota = None
        self.discriminator = None

        self.type = type
        self.used = used
        self.unit = unit
        self.quota = quota

    @property
    def type(self):
        """Gets the type of this Resource.

        :return: The type of this Resource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Resource.

        :param type: The type of this Resource.
        :type type: str
        """
        self._type = type

    @property
    def used(self):
        """Gets the used of this Resource.

        :return: The used of this Resource.
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this Resource.

        :param used: The used of this Resource.
        :type used: int
        """
        self._used = used

    @property
    def unit(self):
        """Gets the unit of this Resource.

        :return: The unit of this Resource.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this Resource.

        :param unit: The unit of this Resource.
        :type unit: str
        """
        self._unit = unit

    @property
    def quota(self):
        """Gets the quota of this Resource.

        :return: The quota of this Resource.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        """Sets the quota of this Resource.

        :param quota: The quota of this Resource.
        :type quota: int
        """
        self._quota = quota

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
        if not isinstance(other, Resource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
