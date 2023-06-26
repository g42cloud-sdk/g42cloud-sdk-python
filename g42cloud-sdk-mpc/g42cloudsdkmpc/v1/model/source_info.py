# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class SourceInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'duration': 'int',
        'duration_ms': 'int',
        'format': 'str',
        'size': 'int',
        'video_info': 'VideoInfo',
        'audio_info': 'list[AudioInfo]'
    }

    attribute_map = {
        'duration': 'duration',
        'duration_ms': 'duration_ms',
        'format': 'format',
        'size': 'size',
        'video_info': 'video_info',
        'audio_info': 'audio_info'
    }

    def __init__(self, duration=None, duration_ms=None, format=None, size=None, video_info=None, audio_info=None):
        """SourceInfo

        The model defined in g42cloud sdk

        :param duration: The param of the SourceInfo
        :type duration: int
        :param duration_ms: The param of the SourceInfo
        :type duration_ms: int
        :param format: The param of the SourceInfo
        :type format: str
        :param size: The param of the SourceInfo
        :type size: int
        :param video_info: The param of the SourceInfo
        :type video_info: :class:`g42cloudsdkmpc.v1.VideoInfo`
        :param audio_info: The param of the SourceInfo
        :type audio_info: list[:class:`g42cloudsdkmpc.v1.AudioInfo`]
        """
        
        

        self._duration = None
        self._duration_ms = None
        self._format = None
        self._size = None
        self._video_info = None
        self._audio_info = None
        self.discriminator = None

        if duration is not None:
            self.duration = duration
        if duration_ms is not None:
            self.duration_ms = duration_ms
        if format is not None:
            self.format = format
        if size is not None:
            self.size = size
        if video_info is not None:
            self.video_info = video_info
        if audio_info is not None:
            self.audio_info = audio_info

    @property
    def duration(self):
        """Gets the duration of this SourceInfo.

        :return: The duration of this SourceInfo.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this SourceInfo.

        :param duration: The duration of this SourceInfo.
        :type duration: int
        """
        self._duration = duration

    @property
    def duration_ms(self):
        """Gets the duration_ms of this SourceInfo.

        :return: The duration_ms of this SourceInfo.
        :rtype: int
        """
        return self._duration_ms

    @duration_ms.setter
    def duration_ms(self, duration_ms):
        """Sets the duration_ms of this SourceInfo.

        :param duration_ms: The duration_ms of this SourceInfo.
        :type duration_ms: int
        """
        self._duration_ms = duration_ms

    @property
    def format(self):
        """Gets the format of this SourceInfo.

        :return: The format of this SourceInfo.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this SourceInfo.

        :param format: The format of this SourceInfo.
        :type format: str
        """
        self._format = format

    @property
    def size(self):
        """Gets the size of this SourceInfo.

        :return: The size of this SourceInfo.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this SourceInfo.

        :param size: The size of this SourceInfo.
        :type size: int
        """
        self._size = size

    @property
    def video_info(self):
        """Gets the video_info of this SourceInfo.

        :return: The video_info of this SourceInfo.
        :rtype: :class:`g42cloudsdkmpc.v1.VideoInfo`
        """
        return self._video_info

    @video_info.setter
    def video_info(self, video_info):
        """Sets the video_info of this SourceInfo.

        :param video_info: The video_info of this SourceInfo.
        :type video_info: :class:`g42cloudsdkmpc.v1.VideoInfo`
        """
        self._video_info = video_info

    @property
    def audio_info(self):
        """Gets the audio_info of this SourceInfo.

        :return: The audio_info of this SourceInfo.
        :rtype: list[:class:`g42cloudsdkmpc.v1.AudioInfo`]
        """
        return self._audio_info

    @audio_info.setter
    def audio_info(self, audio_info):
        """Sets the audio_info of this SourceInfo.

        :param audio_info: The audio_info of this SourceInfo.
        :type audio_info: list[:class:`g42cloudsdkmpc.v1.AudioInfo`]
        """
        self._audio_info = audio_info

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
        if not isinstance(other, SourceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
