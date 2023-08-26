# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class TransTemplate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_name': 'str',
        'video': 'Video',
        'audio': 'Audio',
        'common': 'Common'
    }

    attribute_map = {
        'template_name': 'template_name',
        'video': 'video',
        'audio': 'audio',
        'common': 'common'
    }

    def __init__(self, template_name=None, video=None, audio=None, common=None):
        """TransTemplate

        The model defined in g42cloud sdk

        :param template_name: The param of the TransTemplate
        :type template_name: str
        :param video: The param of the TransTemplate
        :type video: :class:`g42cloudsdkmpc.v1.Video`
        :param audio: The param of the TransTemplate
        :type audio: :class:`g42cloudsdkmpc.v1.Audio`
        :param common: The param of the TransTemplate
        :type common: :class:`g42cloudsdkmpc.v1.Common`
        """
        
        

        self._template_name = None
        self._video = None
        self._audio = None
        self._common = None
        self.discriminator = None

        self.template_name = template_name
        if video is not None:
            self.video = video
        if audio is not None:
            self.audio = audio
        self.common = common

    @property
    def template_name(self):
        """Gets the template_name of this TransTemplate.

        :return: The template_name of this TransTemplate.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this TransTemplate.

        :param template_name: The template_name of this TransTemplate.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def video(self):
        """Gets the video of this TransTemplate.

        :return: The video of this TransTemplate.
        :rtype: :class:`g42cloudsdkmpc.v1.Video`
        """
        return self._video

    @video.setter
    def video(self, video):
        """Sets the video of this TransTemplate.

        :param video: The video of this TransTemplate.
        :type video: :class:`g42cloudsdkmpc.v1.Video`
        """
        self._video = video

    @property
    def audio(self):
        """Gets the audio of this TransTemplate.

        :return: The audio of this TransTemplate.
        :rtype: :class:`g42cloudsdkmpc.v1.Audio`
        """
        return self._audio

    @audio.setter
    def audio(self, audio):
        """Sets the audio of this TransTemplate.

        :param audio: The audio of this TransTemplate.
        :type audio: :class:`g42cloudsdkmpc.v1.Audio`
        """
        self._audio = audio

    @property
    def common(self):
        """Gets the common of this TransTemplate.

        :return: The common of this TransTemplate.
        :rtype: :class:`g42cloudsdkmpc.v1.Common`
        """
        return self._common

    @common.setter
    def common(self, common):
        """Sets the common of this TransTemplate.

        :param common: The common of this TransTemplate.
        :type common: :class:`g42cloudsdkmpc.v1.Common`
        """
        self._common = common

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
        if not isinstance(other, TransTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
