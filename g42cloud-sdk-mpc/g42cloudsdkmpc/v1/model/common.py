# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class Common:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pvc': 'bool',
        'hls_interval': 'int',
        'dash_interval': 'int',
        'pack_type': 'int'
    }

    attribute_map = {
        'pvc': 'PVC',
        'hls_interval': 'hls_interval',
        'dash_interval': 'dash_interval',
        'pack_type': 'pack_type'
    }

    def __init__(self, pvc=None, hls_interval=None, dash_interval=None, pack_type=None):
        """Common

        The model defined in g42cloud sdk

        :param pvc: The param of the Common
        :type pvc: bool
        :param hls_interval: The param of the Common
        :type hls_interval: int
        :param dash_interval: The param of the Common
        :type dash_interval: int
        :param pack_type: The param of the Common
        :type pack_type: int
        """
        
        

        self._pvc = None
        self._hls_interval = None
        self._dash_interval = None
        self._pack_type = None
        self.discriminator = None

        if pvc is not None:
            self.pvc = pvc
        if hls_interval is not None:
            self.hls_interval = hls_interval
        if dash_interval is not None:
            self.dash_interval = dash_interval
        self.pack_type = pack_type

    @property
    def pvc(self):
        """Gets the pvc of this Common.

        :return: The pvc of this Common.
        :rtype: bool
        """
        return self._pvc

    @pvc.setter
    def pvc(self, pvc):
        """Sets the pvc of this Common.

        :param pvc: The pvc of this Common.
        :type pvc: bool
        """
        self._pvc = pvc

    @property
    def hls_interval(self):
        """Gets the hls_interval of this Common.

        :return: The hls_interval of this Common.
        :rtype: int
        """
        return self._hls_interval

    @hls_interval.setter
    def hls_interval(self, hls_interval):
        """Sets the hls_interval of this Common.

        :param hls_interval: The hls_interval of this Common.
        :type hls_interval: int
        """
        self._hls_interval = hls_interval

    @property
    def dash_interval(self):
        """Gets the dash_interval of this Common.

        :return: The dash_interval of this Common.
        :rtype: int
        """
        return self._dash_interval

    @dash_interval.setter
    def dash_interval(self, dash_interval):
        """Sets the dash_interval of this Common.

        :param dash_interval: The dash_interval of this Common.
        :type dash_interval: int
        """
        self._dash_interval = dash_interval

    @property
    def pack_type(self):
        """Gets the pack_type of this Common.

        :return: The pack_type of this Common.
        :rtype: int
        """
        return self._pack_type

    @pack_type.setter
    def pack_type(self, pack_type):
        """Sets the pack_type of this Common.

        :param pack_type: The pack_type of this Common.
        :type pack_type: int
        """
        self._pack_type = pack_type

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
        if not isinstance(other, Common):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
