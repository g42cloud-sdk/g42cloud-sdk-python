# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class OutputVideoPara:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_id': 'int',
        'size': 'int',
        'pack': 'str',
        'video': 'VideoInfo',
        'audio': 'AudioInfo',
        'file_name': 'str',
        'conver_duration': 'float',
        'error': 'XCodeError'
    }

    attribute_map = {
        'template_id': 'template_id',
        'size': 'size',
        'pack': 'pack',
        'video': 'video',
        'audio': 'audio',
        'file_name': 'file_name',
        'conver_duration': 'conver_duration',
        'error': 'error'
    }

    def __init__(self, template_id=None, size=None, pack=None, video=None, audio=None, file_name=None, conver_duration=None, error=None):
        """OutputVideoPara

        The model defined in g42cloud sdk

        :param template_id: The param of the OutputVideoPara
        :type template_id: int
        :param size: The param of the OutputVideoPara
        :type size: int
        :param pack: The param of the OutputVideoPara
        :type pack: str
        :param video: The param of the OutputVideoPara
        :type video: :class:`g42cloudsdkmpc.v1.VideoInfo`
        :param audio: The param of the OutputVideoPara
        :type audio: :class:`g42cloudsdkmpc.v1.AudioInfo`
        :param file_name: The param of the OutputVideoPara
        :type file_name: str
        :param conver_duration: The param of the OutputVideoPara
        :type conver_duration: float
        :param error: The param of the OutputVideoPara
        :type error: :class:`g42cloudsdkmpc.v1.XCodeError`
        """
        
        

        self._template_id = None
        self._size = None
        self._pack = None
        self._video = None
        self._audio = None
        self._file_name = None
        self._conver_duration = None
        self._error = None
        self.discriminator = None

        if template_id is not None:
            self.template_id = template_id
        if size is not None:
            self.size = size
        if pack is not None:
            self.pack = pack
        if video is not None:
            self.video = video
        if audio is not None:
            self.audio = audio
        if file_name is not None:
            self.file_name = file_name
        if conver_duration is not None:
            self.conver_duration = conver_duration
        if error is not None:
            self.error = error

    @property
    def template_id(self):
        """Gets the template_id of this OutputVideoPara.

        :return: The template_id of this OutputVideoPara.
        :rtype: int
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this OutputVideoPara.

        :param template_id: The template_id of this OutputVideoPara.
        :type template_id: int
        """
        self._template_id = template_id

    @property
    def size(self):
        """Gets the size of this OutputVideoPara.

        :return: The size of this OutputVideoPara.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this OutputVideoPara.

        :param size: The size of this OutputVideoPara.
        :type size: int
        """
        self._size = size

    @property
    def pack(self):
        """Gets the pack of this OutputVideoPara.

        :return: The pack of this OutputVideoPara.
        :rtype: str
        """
        return self._pack

    @pack.setter
    def pack(self, pack):
        """Sets the pack of this OutputVideoPara.

        :param pack: The pack of this OutputVideoPara.
        :type pack: str
        """
        self._pack = pack

    @property
    def video(self):
        """Gets the video of this OutputVideoPara.

        :return: The video of this OutputVideoPara.
        :rtype: :class:`g42cloudsdkmpc.v1.VideoInfo`
        """
        return self._video

    @video.setter
    def video(self, video):
        """Sets the video of this OutputVideoPara.

        :param video: The video of this OutputVideoPara.
        :type video: :class:`g42cloudsdkmpc.v1.VideoInfo`
        """
        self._video = video

    @property
    def audio(self):
        """Gets the audio of this OutputVideoPara.

        :return: The audio of this OutputVideoPara.
        :rtype: :class:`g42cloudsdkmpc.v1.AudioInfo`
        """
        return self._audio

    @audio.setter
    def audio(self, audio):
        """Sets the audio of this OutputVideoPara.

        :param audio: The audio of this OutputVideoPara.
        :type audio: :class:`g42cloudsdkmpc.v1.AudioInfo`
        """
        self._audio = audio

    @property
    def file_name(self):
        """Gets the file_name of this OutputVideoPara.

        :return: The file_name of this OutputVideoPara.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this OutputVideoPara.

        :param file_name: The file_name of this OutputVideoPara.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def conver_duration(self):
        """Gets the conver_duration of this OutputVideoPara.

        :return: The conver_duration of this OutputVideoPara.
        :rtype: float
        """
        return self._conver_duration

    @conver_duration.setter
    def conver_duration(self, conver_duration):
        """Sets the conver_duration of this OutputVideoPara.

        :param conver_duration: The conver_duration of this OutputVideoPara.
        :type conver_duration: float
        """
        self._conver_duration = conver_duration

    @property
    def error(self):
        """Gets the error of this OutputVideoPara.

        :return: The error of this OutputVideoPara.
        :rtype: :class:`g42cloudsdkmpc.v1.XCodeError`
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this OutputVideoPara.

        :param error: The error of this OutputVideoPara.
        :type error: :class:`g42cloudsdkmpc.v1.XCodeError`
        """
        self._error = error

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
        if not isinstance(other, OutputVideoPara):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
