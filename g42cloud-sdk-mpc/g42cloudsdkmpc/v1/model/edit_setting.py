# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class EditSetting:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'timeline_start': 'str',
        'timeline_end': 'str',
        'trans_template_id': 'int',
        'av_parameter': 'AvParameters',
        'mosaics': 'list[MosaicInfo]',
        'image_watermarks': 'list[ImageWatermarkSetting]',
        'heads': 'list[ObsObjInfo]',
        'tails': 'list[ObsObjInfo]',
        'output': 'ObsObjInfo'
    }

    attribute_map = {
        'timeline_start': 'timeline_start',
        'timeline_end': 'timeline_end',
        'trans_template_id': 'trans_template_id',
        'av_parameter': 'av_parameter',
        'mosaics': 'mosaics',
        'image_watermarks': 'image_watermarks',
        'heads': 'heads',
        'tails': 'tails',
        'output': 'output'
    }

    def __init__(self, timeline_start=None, timeline_end=None, trans_template_id=None, av_parameter=None, mosaics=None, image_watermarks=None, heads=None, tails=None, output=None):
        """EditSetting

        The model defined in g42cloud sdk

        :param timeline_start: The param of the EditSetting
        :type timeline_start: str
        :param timeline_end: The param of the EditSetting
        :type timeline_end: str
        :param trans_template_id: The param of the EditSetting
        :type trans_template_id: int
        :param av_parameter: The param of the EditSetting
        :type av_parameter: :class:`g42cloudsdkmpc.v1.AvParameters`
        :param mosaics: The param of the EditSetting
        :type mosaics: list[:class:`g42cloudsdkmpc.v1.MosaicInfo`]
        :param image_watermarks: The param of the EditSetting
        :type image_watermarks: list[:class:`g42cloudsdkmpc.v1.ImageWatermarkSetting`]
        :param heads: The param of the EditSetting
        :type heads: list[:class:`g42cloudsdkmpc.v1.ObsObjInfo`]
        :param tails: The param of the EditSetting
        :type tails: list[:class:`g42cloudsdkmpc.v1.ObsObjInfo`]
        :param output: The param of the EditSetting
        :type output: :class:`g42cloudsdkmpc.v1.ObsObjInfo`
        """
        
        

        self._timeline_start = None
        self._timeline_end = None
        self._trans_template_id = None
        self._av_parameter = None
        self._mosaics = None
        self._image_watermarks = None
        self._heads = None
        self._tails = None
        self._output = None
        self.discriminator = None

        if timeline_start is not None:
            self.timeline_start = timeline_start
        if timeline_end is not None:
            self.timeline_end = timeline_end
        if trans_template_id is not None:
            self.trans_template_id = trans_template_id
        if av_parameter is not None:
            self.av_parameter = av_parameter
        if mosaics is not None:
            self.mosaics = mosaics
        if image_watermarks is not None:
            self.image_watermarks = image_watermarks
        if heads is not None:
            self.heads = heads
        if tails is not None:
            self.tails = tails
        self.output = output

    @property
    def timeline_start(self):
        """Gets the timeline_start of this EditSetting.

        :return: The timeline_start of this EditSetting.
        :rtype: str
        """
        return self._timeline_start

    @timeline_start.setter
    def timeline_start(self, timeline_start):
        """Sets the timeline_start of this EditSetting.

        :param timeline_start: The timeline_start of this EditSetting.
        :type timeline_start: str
        """
        self._timeline_start = timeline_start

    @property
    def timeline_end(self):
        """Gets the timeline_end of this EditSetting.

        :return: The timeline_end of this EditSetting.
        :rtype: str
        """
        return self._timeline_end

    @timeline_end.setter
    def timeline_end(self, timeline_end):
        """Sets the timeline_end of this EditSetting.

        :param timeline_end: The timeline_end of this EditSetting.
        :type timeline_end: str
        """
        self._timeline_end = timeline_end

    @property
    def trans_template_id(self):
        """Gets the trans_template_id of this EditSetting.

        :return: The trans_template_id of this EditSetting.
        :rtype: int
        """
        return self._trans_template_id

    @trans_template_id.setter
    def trans_template_id(self, trans_template_id):
        """Sets the trans_template_id of this EditSetting.

        :param trans_template_id: The trans_template_id of this EditSetting.
        :type trans_template_id: int
        """
        self._trans_template_id = trans_template_id

    @property
    def av_parameter(self):
        """Gets the av_parameter of this EditSetting.

        :return: The av_parameter of this EditSetting.
        :rtype: :class:`g42cloudsdkmpc.v1.AvParameters`
        """
        return self._av_parameter

    @av_parameter.setter
    def av_parameter(self, av_parameter):
        """Sets the av_parameter of this EditSetting.

        :param av_parameter: The av_parameter of this EditSetting.
        :type av_parameter: :class:`g42cloudsdkmpc.v1.AvParameters`
        """
        self._av_parameter = av_parameter

    @property
    def mosaics(self):
        """Gets the mosaics of this EditSetting.

        :return: The mosaics of this EditSetting.
        :rtype: list[:class:`g42cloudsdkmpc.v1.MosaicInfo`]
        """
        return self._mosaics

    @mosaics.setter
    def mosaics(self, mosaics):
        """Sets the mosaics of this EditSetting.

        :param mosaics: The mosaics of this EditSetting.
        :type mosaics: list[:class:`g42cloudsdkmpc.v1.MosaicInfo`]
        """
        self._mosaics = mosaics

    @property
    def image_watermarks(self):
        """Gets the image_watermarks of this EditSetting.

        :return: The image_watermarks of this EditSetting.
        :rtype: list[:class:`g42cloudsdkmpc.v1.ImageWatermarkSetting`]
        """
        return self._image_watermarks

    @image_watermarks.setter
    def image_watermarks(self, image_watermarks):
        """Sets the image_watermarks of this EditSetting.

        :param image_watermarks: The image_watermarks of this EditSetting.
        :type image_watermarks: list[:class:`g42cloudsdkmpc.v1.ImageWatermarkSetting`]
        """
        self._image_watermarks = image_watermarks

    @property
    def heads(self):
        """Gets the heads of this EditSetting.

        :return: The heads of this EditSetting.
        :rtype: list[:class:`g42cloudsdkmpc.v1.ObsObjInfo`]
        """
        return self._heads

    @heads.setter
    def heads(self, heads):
        """Sets the heads of this EditSetting.

        :param heads: The heads of this EditSetting.
        :type heads: list[:class:`g42cloudsdkmpc.v1.ObsObjInfo`]
        """
        self._heads = heads

    @property
    def tails(self):
        """Gets the tails of this EditSetting.

        :return: The tails of this EditSetting.
        :rtype: list[:class:`g42cloudsdkmpc.v1.ObsObjInfo`]
        """
        return self._tails

    @tails.setter
    def tails(self, tails):
        """Sets the tails of this EditSetting.

        :param tails: The tails of this EditSetting.
        :type tails: list[:class:`g42cloudsdkmpc.v1.ObsObjInfo`]
        """
        self._tails = tails

    @property
    def output(self):
        """Gets the output of this EditSetting.

        :return: The output of this EditSetting.
        :rtype: :class:`g42cloudsdkmpc.v1.ObsObjInfo`
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this EditSetting.

        :param output: The output of this EditSetting.
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
        if not isinstance(other, EditSetting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
