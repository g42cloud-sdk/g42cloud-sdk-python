# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class AnimatedGraphicsOutputParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'format': 'str',
        'width': 'int',
        'height': 'int',
        'start': 'int',
        'end': 'int',
        'frame_rate': 'int'
    }

    attribute_map = {
        'format': 'format',
        'width': 'width',
        'height': 'height',
        'start': 'start',
        'end': 'end',
        'frame_rate': 'frame_rate'
    }

    def __init__(self, format=None, width=None, height=None, start=None, end=None, frame_rate=None):
        """AnimatedGraphicsOutputParam

        The model defined in g42cloud sdk

        :param format: The param of the AnimatedGraphicsOutputParam
        :type format: str
        :param width: The param of the AnimatedGraphicsOutputParam
        :type width: int
        :param height: The param of the AnimatedGraphicsOutputParam
        :type height: int
        :param start: The param of the AnimatedGraphicsOutputParam
        :type start: int
        :param end: The param of the AnimatedGraphicsOutputParam
        :type end: int
        :param frame_rate: The param of the AnimatedGraphicsOutputParam
        :type frame_rate: int
        """
        
        

        self._format = None
        self._width = None
        self._height = None
        self._start = None
        self._end = None
        self._frame_rate = None
        self.discriminator = None

        if format is not None:
            self.format = format
        self.width = width
        self.height = height
        self.start = start
        self.end = end
        if frame_rate is not None:
            self.frame_rate = frame_rate

    @property
    def format(self):
        """Gets the format of this AnimatedGraphicsOutputParam.

        :return: The format of this AnimatedGraphicsOutputParam.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this AnimatedGraphicsOutputParam.

        :param format: The format of this AnimatedGraphicsOutputParam.
        :type format: str
        """
        self._format = format

    @property
    def width(self):
        """Gets the width of this AnimatedGraphicsOutputParam.

        :return: The width of this AnimatedGraphicsOutputParam.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this AnimatedGraphicsOutputParam.

        :param width: The width of this AnimatedGraphicsOutputParam.
        :type width: int
        """
        self._width = width

    @property
    def height(self):
        """Gets the height of this AnimatedGraphicsOutputParam.

        :return: The height of this AnimatedGraphicsOutputParam.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this AnimatedGraphicsOutputParam.

        :param height: The height of this AnimatedGraphicsOutputParam.
        :type height: int
        """
        self._height = height

    @property
    def start(self):
        """Gets the start of this AnimatedGraphicsOutputParam.

        :return: The start of this AnimatedGraphicsOutputParam.
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this AnimatedGraphicsOutputParam.

        :param start: The start of this AnimatedGraphicsOutputParam.
        :type start: int
        """
        self._start = start

    @property
    def end(self):
        """Gets the end of this AnimatedGraphicsOutputParam.

        :return: The end of this AnimatedGraphicsOutputParam.
        :rtype: int
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this AnimatedGraphicsOutputParam.

        :param end: The end of this AnimatedGraphicsOutputParam.
        :type end: int
        """
        self._end = end

    @property
    def frame_rate(self):
        """Gets the frame_rate of this AnimatedGraphicsOutputParam.

        :return: The frame_rate of this AnimatedGraphicsOutputParam.
        :rtype: int
        """
        return self._frame_rate

    @frame_rate.setter
    def frame_rate(self, frame_rate):
        """Sets the frame_rate of this AnimatedGraphicsOutputParam.

        :param frame_rate: The frame_rate of this AnimatedGraphicsOutputParam.
        :type frame_rate: int
        """
        self._frame_rate = frame_rate

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
        if not isinstance(other, AnimatedGraphicsOutputParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
