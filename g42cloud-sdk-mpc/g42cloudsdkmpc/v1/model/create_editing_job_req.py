# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateEditingJobReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'edit_type': 'list[str]',
        'clips': 'list[ClipInfo]',
        'concats': 'list[MultiConcatInfo]',
        'concat': 'ConcatInfo',
        'mix': 'MixInfo',
        'input': 'ObsObjInfo',
        'output_setting': 'OutputSetting',
        'image_watermark_settings': 'list[ImageWatermarkSetting]',
        'edit_settings': 'list[EditSetting]',
        'user_data': 'str'
    }

    attribute_map = {
        'edit_type': 'edit_type',
        'clips': 'clips',
        'concats': 'concats',
        'concat': 'concat',
        'mix': 'mix',
        'input': 'input',
        'output_setting': 'output_setting',
        'image_watermark_settings': 'image_watermark_settings',
        'edit_settings': 'edit_settings',
        'user_data': 'user_data'
    }

    def __init__(self, edit_type=None, clips=None, concats=None, concat=None, mix=None, input=None, output_setting=None, image_watermark_settings=None, edit_settings=None, user_data=None):
        """CreateEditingJobReq

        The model defined in g42cloud sdk

        :param edit_type: The param of the CreateEditingJobReq
        :type edit_type: list[str]
        :param clips: The param of the CreateEditingJobReq
        :type clips: list[:class:`g42cloudsdkmpc.v1.ClipInfo`]
        :param concats: The param of the CreateEditingJobReq
        :type concats: list[:class:`g42cloudsdkmpc.v1.MultiConcatInfo`]
        :param concat: The param of the CreateEditingJobReq
        :type concat: :class:`g42cloudsdkmpc.v1.ConcatInfo`
        :param mix: The param of the CreateEditingJobReq
        :type mix: :class:`g42cloudsdkmpc.v1.MixInfo`
        :param input: The param of the CreateEditingJobReq
        :type input: :class:`g42cloudsdkmpc.v1.ObsObjInfo`
        :param output_setting: The param of the CreateEditingJobReq
        :type output_setting: :class:`g42cloudsdkmpc.v1.OutputSetting`
        :param image_watermark_settings: The param of the CreateEditingJobReq
        :type image_watermark_settings: list[:class:`g42cloudsdkmpc.v1.ImageWatermarkSetting`]
        :param edit_settings: The param of the CreateEditingJobReq
        :type edit_settings: list[:class:`g42cloudsdkmpc.v1.EditSetting`]
        :param user_data: The param of the CreateEditingJobReq
        :type user_data: str
        """
        
        

        self._edit_type = None
        self._clips = None
        self._concats = None
        self._concat = None
        self._mix = None
        self._input = None
        self._output_setting = None
        self._image_watermark_settings = None
        self._edit_settings = None
        self._user_data = None
        self.discriminator = None

        if edit_type is not None:
            self.edit_type = edit_type
        if clips is not None:
            self.clips = clips
        if concats is not None:
            self.concats = concats
        if concat is not None:
            self.concat = concat
        if mix is not None:
            self.mix = mix
        if input is not None:
            self.input = input
        if output_setting is not None:
            self.output_setting = output_setting
        if image_watermark_settings is not None:
            self.image_watermark_settings = image_watermark_settings
        if edit_settings is not None:
            self.edit_settings = edit_settings
        if user_data is not None:
            self.user_data = user_data

    @property
    def edit_type(self):
        """Gets the edit_type of this CreateEditingJobReq.

        :return: The edit_type of this CreateEditingJobReq.
        :rtype: list[str]
        """
        return self._edit_type

    @edit_type.setter
    def edit_type(self, edit_type):
        """Sets the edit_type of this CreateEditingJobReq.

        :param edit_type: The edit_type of this CreateEditingJobReq.
        :type edit_type: list[str]
        """
        self._edit_type = edit_type

    @property
    def clips(self):
        """Gets the clips of this CreateEditingJobReq.

        :return: The clips of this CreateEditingJobReq.
        :rtype: list[:class:`g42cloudsdkmpc.v1.ClipInfo`]
        """
        return self._clips

    @clips.setter
    def clips(self, clips):
        """Sets the clips of this CreateEditingJobReq.

        :param clips: The clips of this CreateEditingJobReq.
        :type clips: list[:class:`g42cloudsdkmpc.v1.ClipInfo`]
        """
        self._clips = clips

    @property
    def concats(self):
        """Gets the concats of this CreateEditingJobReq.

        :return: The concats of this CreateEditingJobReq.
        :rtype: list[:class:`g42cloudsdkmpc.v1.MultiConcatInfo`]
        """
        return self._concats

    @concats.setter
    def concats(self, concats):
        """Sets the concats of this CreateEditingJobReq.

        :param concats: The concats of this CreateEditingJobReq.
        :type concats: list[:class:`g42cloudsdkmpc.v1.MultiConcatInfo`]
        """
        self._concats = concats

    @property
    def concat(self):
        """Gets the concat of this CreateEditingJobReq.

        :return: The concat of this CreateEditingJobReq.
        :rtype: :class:`g42cloudsdkmpc.v1.ConcatInfo`
        """
        return self._concat

    @concat.setter
    def concat(self, concat):
        """Sets the concat of this CreateEditingJobReq.

        :param concat: The concat of this CreateEditingJobReq.
        :type concat: :class:`g42cloudsdkmpc.v1.ConcatInfo`
        """
        self._concat = concat

    @property
    def mix(self):
        """Gets the mix of this CreateEditingJobReq.

        :return: The mix of this CreateEditingJobReq.
        :rtype: :class:`g42cloudsdkmpc.v1.MixInfo`
        """
        return self._mix

    @mix.setter
    def mix(self, mix):
        """Sets the mix of this CreateEditingJobReq.

        :param mix: The mix of this CreateEditingJobReq.
        :type mix: :class:`g42cloudsdkmpc.v1.MixInfo`
        """
        self._mix = mix

    @property
    def input(self):
        """Gets the input of this CreateEditingJobReq.

        :return: The input of this CreateEditingJobReq.
        :rtype: :class:`g42cloudsdkmpc.v1.ObsObjInfo`
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this CreateEditingJobReq.

        :param input: The input of this CreateEditingJobReq.
        :type input: :class:`g42cloudsdkmpc.v1.ObsObjInfo`
        """
        self._input = input

    @property
    def output_setting(self):
        """Gets the output_setting of this CreateEditingJobReq.

        :return: The output_setting of this CreateEditingJobReq.
        :rtype: :class:`g42cloudsdkmpc.v1.OutputSetting`
        """
        return self._output_setting

    @output_setting.setter
    def output_setting(self, output_setting):
        """Sets the output_setting of this CreateEditingJobReq.

        :param output_setting: The output_setting of this CreateEditingJobReq.
        :type output_setting: :class:`g42cloudsdkmpc.v1.OutputSetting`
        """
        self._output_setting = output_setting

    @property
    def image_watermark_settings(self):
        """Gets the image_watermark_settings of this CreateEditingJobReq.

        :return: The image_watermark_settings of this CreateEditingJobReq.
        :rtype: list[:class:`g42cloudsdkmpc.v1.ImageWatermarkSetting`]
        """
        return self._image_watermark_settings

    @image_watermark_settings.setter
    def image_watermark_settings(self, image_watermark_settings):
        """Sets the image_watermark_settings of this CreateEditingJobReq.

        :param image_watermark_settings: The image_watermark_settings of this CreateEditingJobReq.
        :type image_watermark_settings: list[:class:`g42cloudsdkmpc.v1.ImageWatermarkSetting`]
        """
        self._image_watermark_settings = image_watermark_settings

    @property
    def edit_settings(self):
        """Gets the edit_settings of this CreateEditingJobReq.

        :return: The edit_settings of this CreateEditingJobReq.
        :rtype: list[:class:`g42cloudsdkmpc.v1.EditSetting`]
        """
        return self._edit_settings

    @edit_settings.setter
    def edit_settings(self, edit_settings):
        """Sets the edit_settings of this CreateEditingJobReq.

        :param edit_settings: The edit_settings of this CreateEditingJobReq.
        :type edit_settings: list[:class:`g42cloudsdkmpc.v1.EditSetting`]
        """
        self._edit_settings = edit_settings

    @property
    def user_data(self):
        """Gets the user_data of this CreateEditingJobReq.

        :return: The user_data of this CreateEditingJobReq.
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this CreateEditingJobReq.

        :param user_data: The user_data of this CreateEditingJobReq.
        :type user_data: str
        """
        self._user_data = user_data

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
        if not isinstance(other, CreateEditingJobReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
