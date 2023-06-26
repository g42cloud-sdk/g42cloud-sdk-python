# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class WatermarkTemplate:

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
        'base': 'str',
        'template_id': 'int',
        'template_name': 'str',
        'type': 'str'
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
        'base': 'base',
        'template_id': 'template_id',
        'template_name': 'template_name',
        'type': 'type'
    }

    def __init__(self, dx=None, dy=None, referpos=None, timeline_start=None, timeline_duration=None, image_process=None, width=None, height=None, base=None, template_id=None, template_name=None, type=None):
        """WatermarkTemplate

        The model defined in g42cloud sdk

        :param dx: The param of the WatermarkTemplate
        :type dx: str
        :param dy: The param of the WatermarkTemplate
        :type dy: str
        :param referpos: The param of the WatermarkTemplate
        :type referpos: str
        :param timeline_start: The param of the WatermarkTemplate
        :type timeline_start: str
        :param timeline_duration: The param of the WatermarkTemplate
        :type timeline_duration: str
        :param image_process: The param of the WatermarkTemplate
        :type image_process: str
        :param width: The param of the WatermarkTemplate
        :type width: str
        :param height: The param of the WatermarkTemplate
        :type height: str
        :param base: The param of the WatermarkTemplate
        :type base: str
        :param template_id: The param of the WatermarkTemplate
        :type template_id: int
        :param template_name: The param of the WatermarkTemplate
        :type template_name: str
        :param type: The param of the WatermarkTemplate
        :type type: str
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
        self._template_id = None
        self._template_name = None
        self._type = None
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
        if template_id is not None:
            self.template_id = template_id
        if template_name is not None:
            self.template_name = template_name
        if type is not None:
            self.type = type

    @property
    def dx(self):
        """Gets the dx of this WatermarkTemplate.

        :return: The dx of this WatermarkTemplate.
        :rtype: str
        """
        return self._dx

    @dx.setter
    def dx(self, dx):
        """Sets the dx of this WatermarkTemplate.

        :param dx: The dx of this WatermarkTemplate.
        :type dx: str
        """
        self._dx = dx

    @property
    def dy(self):
        """Gets the dy of this WatermarkTemplate.

        :return: The dy of this WatermarkTemplate.
        :rtype: str
        """
        return self._dy

    @dy.setter
    def dy(self, dy):
        """Sets the dy of this WatermarkTemplate.

        :param dy: The dy of this WatermarkTemplate.
        :type dy: str
        """
        self._dy = dy

    @property
    def referpos(self):
        """Gets the referpos of this WatermarkTemplate.

        :return: The referpos of this WatermarkTemplate.
        :rtype: str
        """
        return self._referpos

    @referpos.setter
    def referpos(self, referpos):
        """Sets the referpos of this WatermarkTemplate.

        :param referpos: The referpos of this WatermarkTemplate.
        :type referpos: str
        """
        self._referpos = referpos

    @property
    def timeline_start(self):
        """Gets the timeline_start of this WatermarkTemplate.

        :return: The timeline_start of this WatermarkTemplate.
        :rtype: str
        """
        return self._timeline_start

    @timeline_start.setter
    def timeline_start(self, timeline_start):
        """Sets the timeline_start of this WatermarkTemplate.

        :param timeline_start: The timeline_start of this WatermarkTemplate.
        :type timeline_start: str
        """
        self._timeline_start = timeline_start

    @property
    def timeline_duration(self):
        """Gets the timeline_duration of this WatermarkTemplate.

        :return: The timeline_duration of this WatermarkTemplate.
        :rtype: str
        """
        return self._timeline_duration

    @timeline_duration.setter
    def timeline_duration(self, timeline_duration):
        """Sets the timeline_duration of this WatermarkTemplate.

        :param timeline_duration: The timeline_duration of this WatermarkTemplate.
        :type timeline_duration: str
        """
        self._timeline_duration = timeline_duration

    @property
    def image_process(self):
        """Gets the image_process of this WatermarkTemplate.

        :return: The image_process of this WatermarkTemplate.
        :rtype: str
        """
        return self._image_process

    @image_process.setter
    def image_process(self, image_process):
        """Sets the image_process of this WatermarkTemplate.

        :param image_process: The image_process of this WatermarkTemplate.
        :type image_process: str
        """
        self._image_process = image_process

    @property
    def width(self):
        """Gets the width of this WatermarkTemplate.

        :return: The width of this WatermarkTemplate.
        :rtype: str
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this WatermarkTemplate.

        :param width: The width of this WatermarkTemplate.
        :type width: str
        """
        self._width = width

    @property
    def height(self):
        """Gets the height of this WatermarkTemplate.

        :return: The height of this WatermarkTemplate.
        :rtype: str
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this WatermarkTemplate.

        :param height: The height of this WatermarkTemplate.
        :type height: str
        """
        self._height = height

    @property
    def base(self):
        """Gets the base of this WatermarkTemplate.

        :return: The base of this WatermarkTemplate.
        :rtype: str
        """
        return self._base

    @base.setter
    def base(self, base):
        """Sets the base of this WatermarkTemplate.

        :param base: The base of this WatermarkTemplate.
        :type base: str
        """
        self._base = base

    @property
    def template_id(self):
        """Gets the template_id of this WatermarkTemplate.

        :return: The template_id of this WatermarkTemplate.
        :rtype: int
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this WatermarkTemplate.

        :param template_id: The template_id of this WatermarkTemplate.
        :type template_id: int
        """
        self._template_id = template_id

    @property
    def template_name(self):
        """Gets the template_name of this WatermarkTemplate.

        :return: The template_name of this WatermarkTemplate.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this WatermarkTemplate.

        :param template_name: The template_name of this WatermarkTemplate.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def type(self):
        """Gets the type of this WatermarkTemplate.

        :return: The type of this WatermarkTemplate.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WatermarkTemplate.

        :param type: The type of this WatermarkTemplate.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, WatermarkTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
