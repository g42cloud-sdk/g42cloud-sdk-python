# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class TextWatermark:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dx': 'str',
        'dy': 'str',
        'referpos': 'str',
        'timeline_start': 'str',
        'timeline_duration': 'str',
        'font_name': 'str',
        'font_size': 'int',
        'font_color': 'str',
        'base': 'str'
    }

    attribute_map = {
        'dx': 'dx',
        'dy': 'dy',
        'referpos': 'referpos',
        'timeline_start': 'timeline_start',
        'timeline_duration': 'timeline_duration',
        'font_name': 'font_name',
        'font_size': 'font_size',
        'font_color': 'font_color',
        'base': 'base'
    }

    def __init__(self, dx=None, dy=None, referpos=None, timeline_start=None, timeline_duration=None, font_name=None, font_size=None, font_color=None, base=None):
        """TextWatermark

        The model defined in g42cloud sdk

        :param dx: The param of the TextWatermark
        :type dx: str
        :param dy: The param of the TextWatermark
        :type dy: str
        :param referpos: The param of the TextWatermark
        :type referpos: str
        :param timeline_start: The param of the TextWatermark
        :type timeline_start: str
        :param timeline_duration: The param of the TextWatermark
        :type timeline_duration: str
        :param font_name: The param of the TextWatermark
        :type font_name: str
        :param font_size: The param of the TextWatermark
        :type font_size: int
        :param font_color: The param of the TextWatermark
        :type font_color: str
        :param base: The param of the TextWatermark
        :type base: str
        """
        
        

        self._dx = None
        self._dy = None
        self._referpos = None
        self._timeline_start = None
        self._timeline_duration = None
        self._font_name = None
        self._font_size = None
        self._font_color = None
        self._base = None
        self.discriminator = None

        if dx is not None:
            self.dx = dx
        if dy is not None:
            self.dy = dy
        if referpos is not None:
            self.referpos = referpos
        if timeline_start is not None:
            self.timeline_start = timeline_start
        if timeline_duration is not None:
            self.timeline_duration = timeline_duration
        if font_name is not None:
            self.font_name = font_name
        if font_size is not None:
            self.font_size = font_size
        if font_color is not None:
            self.font_color = font_color
        if base is not None:
            self.base = base

    @property
    def dx(self):
        """Gets the dx of this TextWatermark.

        :return: The dx of this TextWatermark.
        :rtype: str
        """
        return self._dx

    @dx.setter
    def dx(self, dx):
        """Sets the dx of this TextWatermark.

        :param dx: The dx of this TextWatermark.
        :type dx: str
        """
        self._dx = dx

    @property
    def dy(self):
        """Gets the dy of this TextWatermark.

        :return: The dy of this TextWatermark.
        :rtype: str
        """
        return self._dy

    @dy.setter
    def dy(self, dy):
        """Sets the dy of this TextWatermark.

        :param dy: The dy of this TextWatermark.
        :type dy: str
        """
        self._dy = dy

    @property
    def referpos(self):
        """Gets the referpos of this TextWatermark.

        :return: The referpos of this TextWatermark.
        :rtype: str
        """
        return self._referpos

    @referpos.setter
    def referpos(self, referpos):
        """Sets the referpos of this TextWatermark.

        :param referpos: The referpos of this TextWatermark.
        :type referpos: str
        """
        self._referpos = referpos

    @property
    def timeline_start(self):
        """Gets the timeline_start of this TextWatermark.

        :return: The timeline_start of this TextWatermark.
        :rtype: str
        """
        return self._timeline_start

    @timeline_start.setter
    def timeline_start(self, timeline_start):
        """Sets the timeline_start of this TextWatermark.

        :param timeline_start: The timeline_start of this TextWatermark.
        :type timeline_start: str
        """
        self._timeline_start = timeline_start

    @property
    def timeline_duration(self):
        """Gets the timeline_duration of this TextWatermark.

        :return: The timeline_duration of this TextWatermark.
        :rtype: str
        """
        return self._timeline_duration

    @timeline_duration.setter
    def timeline_duration(self, timeline_duration):
        """Sets the timeline_duration of this TextWatermark.

        :param timeline_duration: The timeline_duration of this TextWatermark.
        :type timeline_duration: str
        """
        self._timeline_duration = timeline_duration

    @property
    def font_name(self):
        """Gets the font_name of this TextWatermark.

        :return: The font_name of this TextWatermark.
        :rtype: str
        """
        return self._font_name

    @font_name.setter
    def font_name(self, font_name):
        """Sets the font_name of this TextWatermark.

        :param font_name: The font_name of this TextWatermark.
        :type font_name: str
        """
        self._font_name = font_name

    @property
    def font_size(self):
        """Gets the font_size of this TextWatermark.

        :return: The font_size of this TextWatermark.
        :rtype: int
        """
        return self._font_size

    @font_size.setter
    def font_size(self, font_size):
        """Sets the font_size of this TextWatermark.

        :param font_size: The font_size of this TextWatermark.
        :type font_size: int
        """
        self._font_size = font_size

    @property
    def font_color(self):
        """Gets the font_color of this TextWatermark.

        :return: The font_color of this TextWatermark.
        :rtype: str
        """
        return self._font_color

    @font_color.setter
    def font_color(self, font_color):
        """Sets the font_color of this TextWatermark.

        :param font_color: The font_color of this TextWatermark.
        :type font_color: str
        """
        self._font_color = font_color

    @property
    def base(self):
        """Gets the base of this TextWatermark.

        :return: The base of this TextWatermark.
        :rtype: str
        """
        return self._base

    @base.setter
    def base(self, base):
        """Sets the base of this TextWatermark.

        :param base: The base of this TextWatermark.
        :type base: str
        """
        self._base = base

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
        if not isinstance(other, TextWatermark):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
