# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class VideoProcess:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'hls_init_count': 'int',
        'hls_init_interval': 'int',
        'rotate': 'int',
        'adaptation': 'str',
        'upsample': 'int'
    }

    attribute_map = {
        'hls_init_count': 'hls_init_count',
        'hls_init_interval': 'hls_init_interval',
        'rotate': 'rotate',
        'adaptation': 'adaptation',
        'upsample': 'upsample'
    }

    def __init__(self, hls_init_count=None, hls_init_interval=None, rotate=None, adaptation=None, upsample=None):
        """VideoProcess

        The model defined in g42cloud sdk

        :param hls_init_count: The param of the VideoProcess
        :type hls_init_count: int
        :param hls_init_interval: The param of the VideoProcess
        :type hls_init_interval: int
        :param rotate: The param of the VideoProcess
        :type rotate: int
        :param adaptation: The param of the VideoProcess
        :type adaptation: str
        :param upsample: The param of the VideoProcess
        :type upsample: int
        """
        
        

        self._hls_init_count = None
        self._hls_init_interval = None
        self._rotate = None
        self._adaptation = None
        self._upsample = None
        self.discriminator = None

        if hls_init_count is not None:
            self.hls_init_count = hls_init_count
        if hls_init_interval is not None:
            self.hls_init_interval = hls_init_interval
        if rotate is not None:
            self.rotate = rotate
        if adaptation is not None:
            self.adaptation = adaptation
        if upsample is not None:
            self.upsample = upsample

    @property
    def hls_init_count(self):
        """Gets the hls_init_count of this VideoProcess.

        :return: The hls_init_count of this VideoProcess.
        :rtype: int
        """
        return self._hls_init_count

    @hls_init_count.setter
    def hls_init_count(self, hls_init_count):
        """Sets the hls_init_count of this VideoProcess.

        :param hls_init_count: The hls_init_count of this VideoProcess.
        :type hls_init_count: int
        """
        self._hls_init_count = hls_init_count

    @property
    def hls_init_interval(self):
        """Gets the hls_init_interval of this VideoProcess.

        :return: The hls_init_interval of this VideoProcess.
        :rtype: int
        """
        return self._hls_init_interval

    @hls_init_interval.setter
    def hls_init_interval(self, hls_init_interval):
        """Sets the hls_init_interval of this VideoProcess.

        :param hls_init_interval: The hls_init_interval of this VideoProcess.
        :type hls_init_interval: int
        """
        self._hls_init_interval = hls_init_interval

    @property
    def rotate(self):
        """Gets the rotate of this VideoProcess.

        :return: The rotate of this VideoProcess.
        :rtype: int
        """
        return self._rotate

    @rotate.setter
    def rotate(self, rotate):
        """Sets the rotate of this VideoProcess.

        :param rotate: The rotate of this VideoProcess.
        :type rotate: int
        """
        self._rotate = rotate

    @property
    def adaptation(self):
        """Gets the adaptation of this VideoProcess.

        :return: The adaptation of this VideoProcess.
        :rtype: str
        """
        return self._adaptation

    @adaptation.setter
    def adaptation(self, adaptation):
        """Sets the adaptation of this VideoProcess.

        :param adaptation: The adaptation of this VideoProcess.
        :type adaptation: str
        """
        self._adaptation = adaptation

    @property
    def upsample(self):
        """Gets the upsample of this VideoProcess.

        :return: The upsample of this VideoProcess.
        :rtype: int
        """
        return self._upsample

    @upsample.setter
    def upsample(self, upsample):
        """Sets the upsample of this VideoProcess.

        :param upsample: The upsample of this VideoProcess.
        :type upsample: int
        """
        self._upsample = upsample

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
        if not isinstance(other, VideoProcess):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
