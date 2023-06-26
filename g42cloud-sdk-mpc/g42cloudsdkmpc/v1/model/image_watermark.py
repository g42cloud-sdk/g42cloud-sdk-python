# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageWatermark:

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
        'image_process': 'str',
        'width': 'str',
        'height': 'str',
        'base': 'str'
    }

    attribute_map = {
        'dx': 'dx',
        'dy': 'dy',
        'referpos': 'referpos',
        'timeline_start': 'timeline_start',
        'timeline_duration': 'timeline_duration',
        'image_process': 'image_process',
        'width': 'width',
        'height': 'height',
        'base': 'base'
    }

    def __init__(self, dx=None, dy=None, referpos=None, timeline_start=None, timeline_duration=None, image_process=None, width=None, height=None, base=None):
        """ImageWatermark

        The model defined in g42cloud sdk

        :param dx: The param of the ImageWatermark
        :type dx: str
        :param dy: The param of the ImageWatermark
        :type dy: str
        :param referpos: The param of the ImageWatermark
        :type referpos: str
        :param timeline_start: The param of the ImageWatermark
        :type timeline_start: str
        :param timeline_duration: The param of the ImageWatermark
        :type timeline_duration: str
        :param image_process: The param of the ImageWatermark
        :type image_process: str
        :param width: The param of the ImageWatermark
        :type width: str
        :param height: The param of the ImageWatermark
        :type height: str
        :param base: The param of the ImageWatermark
        :type base: str
        """
        
        

        self._dx = None
        self._dy = None
        self._referpos = None
        self._timeline_start = None
        self._timeline_duration = None
        self._image_process = None
        self._width = None
        self._height = None
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
        if image_process is not None:
            self.image_process = image_process
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if base is not None:
            self.base = base

    @property
    def dx(self):
        """Gets the dx of this ImageWatermark.

        :return: The dx of this ImageWatermark.
        :rtype: str
        """
        return self._dx

    @dx.setter
    def dx(self, dx):
        """Sets the dx of this ImageWatermark.

        :param dx: The dx of this ImageWatermark.
        :type dx: str
        """
        self._dx = dx

    @property
    def dy(self):
        """Gets the dy of this ImageWatermark.

        :return: The dy of this ImageWatermark.
        :rtype: str
        """
        return self._dy

    @dy.setter
    def dy(self, dy):
        """Sets the dy of this ImageWatermark.

        :param dy: The dy of this ImageWatermark.
        :type dy: str
        """
        self._dy = dy

    @property
    def referpos(self):
        """Gets the referpos of this ImageWatermark.

        :return: The referpos of this ImageWatermark.
        :rtype: str
        """
        return self._referpos

    @referpos.setter
    def referpos(self, referpos):
        """Sets the referpos of this ImageWatermark.

        :param referpos: The referpos of this ImageWatermark.
        :type referpos: str
        """
        self._referpos = referpos

    @property
    def timeline_start(self):
        """Gets the timeline_start of this ImageWatermark.

        :return: The timeline_start of this ImageWatermark.
        :rtype: str
        """
        return self._timeline_start

    @timeline_start.setter
    def timeline_start(self, timeline_start):
        """Sets the timeline_start of this ImageWatermark.

        :param timeline_start: The timeline_start of this ImageWatermark.
        :type timeline_start: str
        """
        self._timeline_start = timeline_start

    @property
    def timeline_duration(self):
        """Gets the timeline_duration of this ImageWatermark.

        :return: The timeline_duration of this ImageWatermark.
        :rtype: str
        """
        return self._timeline_duration

    @timeline_duration.setter
    def timeline_duration(self, timeline_duration):
        """Sets the timeline_duration of this ImageWatermark.

        :param timeline_duration: The timeline_duration of this ImageWatermark.
        :type timeline_duration: str
        """
        self._timeline_duration = timeline_duration

    @property
    def image_process(self):
        """Gets the image_process of this ImageWatermark.

        :return: The image_process of this ImageWatermark.
        :rtype: str
        """
        return self._image_process

    @image_process.setter
    def image_process(self, image_process):
        """Sets the image_process of this ImageWatermark.

        :param image_process: The image_process of this ImageWatermark.
        :type image_process: str
        """
        self._image_process = image_process

    @property
    def width(self):
        """Gets the width of this ImageWatermark.

        :return: The width of this ImageWatermark.
        :rtype: str
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this ImageWatermark.

        :param width: The width of this ImageWatermark.
        :type width: str
        """
        self._width = width

    @property
    def height(self):
        """Gets the height of this ImageWatermark.

        :return: The height of this ImageWatermark.
        :rtype: str
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this ImageWatermark.

        :param height: The height of this ImageWatermark.
        :type height: str
        """
        self._height = height

    @property
    def base(self):
        """Gets the base of this ImageWatermark.

        :return: The base of this ImageWatermark.
        :rtype: str
        """
        return self._base

    @base.setter
    def base(self, base):
        """Sets the base of this ImageWatermark.

        :param base: The base of this ImageWatermark.
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
        if not isinstance(other, ImageWatermark):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
