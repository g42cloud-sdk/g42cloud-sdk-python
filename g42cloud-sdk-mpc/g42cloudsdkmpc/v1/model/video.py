# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class Video:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'output_policy': 'str',
        'codec': 'int',
        'bitrate': 'int',
        'profile': 'int',
        'level': 'int',
        'preset': 'int',
        'max_iframes_interval': 'int',
        'bframes_count': 'int',
        'frame_rate': 'int',
        'width': 'int',
        'height': 'int',
        'black_cut': 'int'
    }

    attribute_map = {
        'output_policy': 'output_policy',
        'codec': 'codec',
        'bitrate': 'bitrate',
        'profile': 'profile',
        'level': 'level',
        'preset': 'preset',
        'max_iframes_interval': 'max_iframes_interval',
        'bframes_count': 'bframes_count',
        'frame_rate': 'frame_rate',
        'width': 'width',
        'height': 'height',
        'black_cut': 'black_cut'
    }

    def __init__(self, output_policy=None, codec=None, bitrate=None, profile=None, level=None, preset=None, max_iframes_interval=None, bframes_count=None, frame_rate=None, width=None, height=None, black_cut=None):
        """Video

        The model defined in g42cloud sdk

        :param output_policy: The param of the Video
        :type output_policy: str
        :param codec: The param of the Video
        :type codec: int
        :param bitrate: The param of the Video
        :type bitrate: int
        :param profile: The param of the Video
        :type profile: int
        :param level: The param of the Video
        :type level: int
        :param preset: The param of the Video
        :type preset: int
        :param max_iframes_interval: The param of the Video
        :type max_iframes_interval: int
        :param bframes_count: The param of the Video
        :type bframes_count: int
        :param frame_rate: The param of the Video
        :type frame_rate: int
        :param width: The param of the Video
        :type width: int
        :param height: The param of the Video
        :type height: int
        :param black_cut: The param of the Video
        :type black_cut: int
        """
        
        

        self._output_policy = None
        self._codec = None
        self._bitrate = None
        self._profile = None
        self._level = None
        self._preset = None
        self._max_iframes_interval = None
        self._bframes_count = None
        self._frame_rate = None
        self._width = None
        self._height = None
        self._black_cut = None
        self.discriminator = None

        if output_policy is not None:
            self.output_policy = output_policy
        if codec is not None:
            self.codec = codec
        if bitrate is not None:
            self.bitrate = bitrate
        if profile is not None:
            self.profile = profile
        if level is not None:
            self.level = level
        if preset is not None:
            self.preset = preset
        if max_iframes_interval is not None:
            self.max_iframes_interval = max_iframes_interval
        if bframes_count is not None:
            self.bframes_count = bframes_count
        if frame_rate is not None:
            self.frame_rate = frame_rate
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if black_cut is not None:
            self.black_cut = black_cut

    @property
    def output_policy(self):
        """Gets the output_policy of this Video.

        :return: The output_policy of this Video.
        :rtype: str
        """
        return self._output_policy

    @output_policy.setter
    def output_policy(self, output_policy):
        """Sets the output_policy of this Video.

        :param output_policy: The output_policy of this Video.
        :type output_policy: str
        """
        self._output_policy = output_policy

    @property
    def codec(self):
        """Gets the codec of this Video.

        :return: The codec of this Video.
        :rtype: int
        """
        return self._codec

    @codec.setter
    def codec(self, codec):
        """Sets the codec of this Video.

        :param codec: The codec of this Video.
        :type codec: int
        """
        self._codec = codec

    @property
    def bitrate(self):
        """Gets the bitrate of this Video.

        :return: The bitrate of this Video.
        :rtype: int
        """
        return self._bitrate

    @bitrate.setter
    def bitrate(self, bitrate):
        """Sets the bitrate of this Video.

        :param bitrate: The bitrate of this Video.
        :type bitrate: int
        """
        self._bitrate = bitrate

    @property
    def profile(self):
        """Gets the profile of this Video.

        :return: The profile of this Video.
        :rtype: int
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this Video.

        :param profile: The profile of this Video.
        :type profile: int
        """
        self._profile = profile

    @property
    def level(self):
        """Gets the level of this Video.

        :return: The level of this Video.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this Video.

        :param level: The level of this Video.
        :type level: int
        """
        self._level = level

    @property
    def preset(self):
        """Gets the preset of this Video.

        :return: The preset of this Video.
        :rtype: int
        """
        return self._preset

    @preset.setter
    def preset(self, preset):
        """Sets the preset of this Video.

        :param preset: The preset of this Video.
        :type preset: int
        """
        self._preset = preset

    @property
    def max_iframes_interval(self):
        """Gets the max_iframes_interval of this Video.

        :return: The max_iframes_interval of this Video.
        :rtype: int
        """
        return self._max_iframes_interval

    @max_iframes_interval.setter
    def max_iframes_interval(self, max_iframes_interval):
        """Sets the max_iframes_interval of this Video.

        :param max_iframes_interval: The max_iframes_interval of this Video.
        :type max_iframes_interval: int
        """
        self._max_iframes_interval = max_iframes_interval

    @property
    def bframes_count(self):
        """Gets the bframes_count of this Video.

        :return: The bframes_count of this Video.
        :rtype: int
        """
        return self._bframes_count

    @bframes_count.setter
    def bframes_count(self, bframes_count):
        """Sets the bframes_count of this Video.

        :param bframes_count: The bframes_count of this Video.
        :type bframes_count: int
        """
        self._bframes_count = bframes_count

    @property
    def frame_rate(self):
        """Gets the frame_rate of this Video.

        :return: The frame_rate of this Video.
        :rtype: int
        """
        return self._frame_rate

    @frame_rate.setter
    def frame_rate(self, frame_rate):
        """Sets the frame_rate of this Video.

        :param frame_rate: The frame_rate of this Video.
        :type frame_rate: int
        """
        self._frame_rate = frame_rate

    @property
    def width(self):
        """Gets the width of this Video.

        :return: The width of this Video.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this Video.

        :param width: The width of this Video.
        :type width: int
        """
        self._width = width

    @property
    def height(self):
        """Gets the height of this Video.

        :return: The height of this Video.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this Video.

        :param height: The height of this Video.
        :type height: int
        """
        self._height = height

    @property
    def black_cut(self):
        """Gets the black_cut of this Video.

        :return: The black_cut of this Video.
        :rtype: int
        """
        return self._black_cut

    @black_cut.setter
    def black_cut(self, black_cut):
        """Sets the black_cut of this Video.

        :param black_cut: The black_cut of this Video.
        :type black_cut: int
        """
        self._black_cut = black_cut

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
        if not isinstance(other, Video):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
