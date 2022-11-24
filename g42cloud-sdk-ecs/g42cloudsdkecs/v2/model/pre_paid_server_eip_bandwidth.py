# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrePaidServerEipBandwidth:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'size': 'int',
        'sharetype': 'str',
        'chargemode': 'str',
        'id': 'str'
    }

    attribute_map = {
        'size': 'size',
        'sharetype': 'sharetype',
        'chargemode': 'chargemode',
        'id': 'id'
    }

    def __init__(self, size=None, sharetype=None, chargemode=None, id=None):
        """PrePaidServerEipBandwidth

        The model defined in g42cloud sdk

        :param size: The param of the PrePaidServerEipBandwidth
        :type size: int
        :param sharetype: The param of the PrePaidServerEipBandwidth
        :type sharetype: str
        :param chargemode: The param of the PrePaidServerEipBandwidth
        :type chargemode: str
        :param id: The param of the PrePaidServerEipBandwidth
        :type id: str
        """
        
        

        self._size = None
        self._sharetype = None
        self._chargemode = None
        self._id = None
        self.discriminator = None

        if size is not None:
            self.size = size
        self.sharetype = sharetype
        if chargemode is not None:
            self.chargemode = chargemode
        if id is not None:
            self.id = id

    @property
    def size(self):
        """Gets the size of this PrePaidServerEipBandwidth.

        :return: The size of this PrePaidServerEipBandwidth.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this PrePaidServerEipBandwidth.

        :param size: The size of this PrePaidServerEipBandwidth.
        :type size: int
        """
        self._size = size

    @property
    def sharetype(self):
        """Gets the sharetype of this PrePaidServerEipBandwidth.

        :return: The sharetype of this PrePaidServerEipBandwidth.
        :rtype: str
        """
        return self._sharetype

    @sharetype.setter
    def sharetype(self, sharetype):
        """Sets the sharetype of this PrePaidServerEipBandwidth.

        :param sharetype: The sharetype of this PrePaidServerEipBandwidth.
        :type sharetype: str
        """
        self._sharetype = sharetype

    @property
    def chargemode(self):
        """Gets the chargemode of this PrePaidServerEipBandwidth.

        :return: The chargemode of this PrePaidServerEipBandwidth.
        :rtype: str
        """
        return self._chargemode

    @chargemode.setter
    def chargemode(self, chargemode):
        """Sets the chargemode of this PrePaidServerEipBandwidth.

        :param chargemode: The chargemode of this PrePaidServerEipBandwidth.
        :type chargemode: str
        """
        self._chargemode = chargemode

    @property
    def id(self):
        """Gets the id of this PrePaidServerEipBandwidth.

        :return: The id of this PrePaidServerEipBandwidth.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PrePaidServerEipBandwidth.

        :param id: The id of this PrePaidServerEipBandwidth.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, PrePaidServerEipBandwidth):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
