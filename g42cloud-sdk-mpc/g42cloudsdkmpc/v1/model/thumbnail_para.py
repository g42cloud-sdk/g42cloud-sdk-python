# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class ThumbnailPara:

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
        'time': 'int',
        'start_time': 'int',
        'duration': 'int',
        'dots': 'list[int]',
        'output_filename': 'str',
        'format': 'int',
        'width': 'int',
        'height': 'int',
        'max_length': 'int'
    }

    attribute_map = {
        'type': 'type',
        'time': 'time',
        'start_time': 'start_time',
        'duration': 'duration',
        'dots': 'dots',
        'output_filename': 'output_filename',
        'format': 'format',
        'width': 'width',
        'height': 'height',
        'max_length': 'max_length'
    }

    def __init__(self, type=None, time=None, start_time=None, duration=None, dots=None, output_filename=None, format=None, width=None, height=None, max_length=None):
        """ThumbnailPara

        The model defined in g42cloud sdk

        :param type: The param of the ThumbnailPara
        :type type: str
        :param time: The param of the ThumbnailPara
        :type time: int
        :param start_time: The param of the ThumbnailPara
        :type start_time: int
        :param duration: The param of the ThumbnailPara
        :type duration: int
        :param dots: The param of the ThumbnailPara
        :type dots: list[int]
        :param output_filename: The param of the ThumbnailPara
        :type output_filename: str
        :param format: The param of the ThumbnailPara
        :type format: int
        :param width: The param of the ThumbnailPara
        :type width: int
        :param height: The param of the ThumbnailPara
        :type height: int
        :param max_length: The param of the ThumbnailPara
        :type max_length: int
        """
        
        

        self._type = None
        self._time = None
        self._start_time = None
        self._duration = None
        self._dots = None
        self._output_filename = None
        self._format = None
        self._width = None
        self._height = None
        self._max_length = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if time is not None:
            self.time = time
        if start_time is not None:
            self.start_time = start_time
        if duration is not None:
            self.duration = duration
        if dots is not None:
            self.dots = dots
        if output_filename is not None:
            self.output_filename = output_filename
        if format is not None:
            self.format = format
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if max_length is not None:
            self.max_length = max_length

    @property
    def type(self):
        """Gets the type of this ThumbnailPara.

        :return: The type of this ThumbnailPara.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ThumbnailPara.

        :param type: The type of this ThumbnailPara.
        :type type: str
        """
        self._type = type

    @property
    def time(self):
        """Gets the time of this ThumbnailPara.

        :return: The time of this ThumbnailPara.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this ThumbnailPara.

        :param time: The time of this ThumbnailPara.
        :type time: int
        """
        self._time = time

    @property
    def start_time(self):
        """Gets the start_time of this ThumbnailPara.

        :return: The start_time of this ThumbnailPara.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ThumbnailPara.

        :param start_time: The start_time of this ThumbnailPara.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def duration(self):
        """Gets the duration of this ThumbnailPara.

        :return: The duration of this ThumbnailPara.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this ThumbnailPara.

        :param duration: The duration of this ThumbnailPara.
        :type duration: int
        """
        self._duration = duration

    @property
    def dots(self):
        """Gets the dots of this ThumbnailPara.

        :return: The dots of this ThumbnailPara.
        :rtype: list[int]
        """
        return self._dots

    @dots.setter
    def dots(self, dots):
        """Sets the dots of this ThumbnailPara.

        :param dots: The dots of this ThumbnailPara.
        :type dots: list[int]
        """
        self._dots = dots

    @property
    def output_filename(self):
        """Gets the output_filename of this ThumbnailPara.

        :return: The output_filename of this ThumbnailPara.
        :rtype: str
        """
        return self._output_filename

    @output_filename.setter
    def output_filename(self, output_filename):
        """Sets the output_filename of this ThumbnailPara.

        :param output_filename: The output_filename of this ThumbnailPara.
        :type output_filename: str
        """
        self._output_filename = output_filename

    @property
    def format(self):
        """Gets the format of this ThumbnailPara.

        :return: The format of this ThumbnailPara.
        :rtype: int
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this ThumbnailPara.

        :param format: The format of this ThumbnailPara.
        :type format: int
        """
        self._format = format

    @property
    def width(self):
        """Gets the width of this ThumbnailPara.

        :return: The width of this ThumbnailPara.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this ThumbnailPara.

        :param width: The width of this ThumbnailPara.
        :type width: int
        """
        self._width = width

    @property
    def height(self):
        """Gets the height of this ThumbnailPara.

        :return: The height of this ThumbnailPara.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this ThumbnailPara.

        :param height: The height of this ThumbnailPara.
        :type height: int
        """
        self._height = height

    @property
    def max_length(self):
        """Gets the max_length of this ThumbnailPara.

        :return: The max_length of this ThumbnailPara.
        :rtype: int
        """
        return self._max_length

    @max_length.setter
    def max_length(self, max_length):
        """Sets the max_length of this ThumbnailPara.

        :param max_length: The max_length of this ThumbnailPara.
        :type max_length: int
        """
        self._max_length = max_length

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
        if not isinstance(other, ThumbnailPara):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
