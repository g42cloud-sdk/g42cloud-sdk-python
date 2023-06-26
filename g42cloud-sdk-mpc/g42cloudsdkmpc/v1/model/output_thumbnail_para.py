# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class OutputThumbnailPara:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_pictures': 'int',
        'width': 'int',
        'height': 'int',
        'file_name': 'str',
        'output': 'ObsObjInfo'
    }

    attribute_map = {
        'total_pictures': 'total_pictures',
        'width': 'width',
        'height': 'height',
        'file_name': 'file_name',
        'output': 'output'
    }

    def __init__(self, total_pictures=None, width=None, height=None, file_name=None, output=None):
        """OutputThumbnailPara

        The model defined in g42cloud sdk

        :param total_pictures: The param of the OutputThumbnailPara
        :type total_pictures: int
        :param width: The param of the OutputThumbnailPara
        :type width: int
        :param height: The param of the OutputThumbnailPara
        :type height: int
        :param file_name: The param of the OutputThumbnailPara
        :type file_name: str
        :param output: The param of the OutputThumbnailPara
        :type output: :class:`g42cloudsdkmpc.v1.ObsObjInfo`
        """
        
        

        self._total_pictures = None
        self._width = None
        self._height = None
        self._file_name = None
        self._output = None
        self.discriminator = None

        if total_pictures is not None:
            self.total_pictures = total_pictures
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if file_name is not None:
            self.file_name = file_name
        if output is not None:
            self.output = output

    @property
    def total_pictures(self):
        """Gets the total_pictures of this OutputThumbnailPara.

        :return: The total_pictures of this OutputThumbnailPara.
        :rtype: int
        """
        return self._total_pictures

    @total_pictures.setter
    def total_pictures(self, total_pictures):
        """Sets the total_pictures of this OutputThumbnailPara.

        :param total_pictures: The total_pictures of this OutputThumbnailPara.
        :type total_pictures: int
        """
        self._total_pictures = total_pictures

    @property
    def width(self):
        """Gets the width of this OutputThumbnailPara.

        :return: The width of this OutputThumbnailPara.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this OutputThumbnailPara.

        :param width: The width of this OutputThumbnailPara.
        :type width: int
        """
        self._width = width

    @property
    def height(self):
        """Gets the height of this OutputThumbnailPara.

        :return: The height of this OutputThumbnailPara.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this OutputThumbnailPara.

        :param height: The height of this OutputThumbnailPara.
        :type height: int
        """
        self._height = height

    @property
    def file_name(self):
        """Gets the file_name of this OutputThumbnailPara.

        :return: The file_name of this OutputThumbnailPara.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this OutputThumbnailPara.

        :param file_name: The file_name of this OutputThumbnailPara.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def output(self):
        """Gets the output of this OutputThumbnailPara.

        :return: The output of this OutputThumbnailPara.
        :rtype: :class:`g42cloudsdkmpc.v1.ObsObjInfo`
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this OutputThumbnailPara.

        :param output: The output of this OutputThumbnailPara.
        :type output: :class:`g42cloudsdkmpc.v1.ObsObjInfo`
        """
        self._output = output

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
        if not isinstance(other, OutputThumbnailPara):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
