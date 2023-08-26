# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class MergeChannelsTaskInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'status': 'str',
        'create_time': 'str',
        'end_time': 'str',
        'output': 'ObsObjInfo',
        'description': 'str',
        'audio_files': 'list[AudioFile]',
        'output_filename': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'status': 'status',
        'create_time': 'create_time',
        'end_time': 'end_time',
        'output': 'output',
        'description': 'description',
        'audio_files': 'audio_files',
        'output_filename': 'output_filename'
    }

    def __init__(self, task_id=None, status=None, create_time=None, end_time=None, output=None, description=None, audio_files=None, output_filename=None):
        """MergeChannelsTaskInfo

        The model defined in g42cloud sdk

        :param task_id: The param of the MergeChannelsTaskInfo
        :type task_id: str
        :param status: The param of the MergeChannelsTaskInfo
        :type status: str
        :param create_time: The param of the MergeChannelsTaskInfo
        :type create_time: str
        :param end_time: The param of the MergeChannelsTaskInfo
        :type end_time: str
        :param output: The param of the MergeChannelsTaskInfo
        :type output: :class:`g42cloudsdkmpc.v1.ObsObjInfo`
        :param description: The param of the MergeChannelsTaskInfo
        :type description: str
        :param audio_files: The param of the MergeChannelsTaskInfo
        :type audio_files: list[:class:`g42cloudsdkmpc.v1.AudioFile`]
        :param output_filename: The param of the MergeChannelsTaskInfo
        :type output_filename: str
        """
        
        

        self._task_id = None
        self._status = None
        self._create_time = None
        self._end_time = None
        self._output = None
        self._description = None
        self._audio_files = None
        self._output_filename = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time
        if end_time is not None:
            self.end_time = end_time
        if output is not None:
            self.output = output
        if description is not None:
            self.description = description
        if audio_files is not None:
            self.audio_files = audio_files
        if output_filename is not None:
            self.output_filename = output_filename

    @property
    def task_id(self):
        """Gets the task_id of this MergeChannelsTaskInfo.

        :return: The task_id of this MergeChannelsTaskInfo.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this MergeChannelsTaskInfo.

        :param task_id: The task_id of this MergeChannelsTaskInfo.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def status(self):
        """Gets the status of this MergeChannelsTaskInfo.

        :return: The status of this MergeChannelsTaskInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MergeChannelsTaskInfo.

        :param status: The status of this MergeChannelsTaskInfo.
        :type status: str
        """
        self._status = status

    @property
    def create_time(self):
        """Gets the create_time of this MergeChannelsTaskInfo.

        :return: The create_time of this MergeChannelsTaskInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this MergeChannelsTaskInfo.

        :param create_time: The create_time of this MergeChannelsTaskInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def end_time(self):
        """Gets the end_time of this MergeChannelsTaskInfo.

        :return: The end_time of this MergeChannelsTaskInfo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this MergeChannelsTaskInfo.

        :param end_time: The end_time of this MergeChannelsTaskInfo.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def output(self):
        """Gets the output of this MergeChannelsTaskInfo.

        :return: The output of this MergeChannelsTaskInfo.
        :rtype: :class:`g42cloudsdkmpc.v1.ObsObjInfo`
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this MergeChannelsTaskInfo.

        :param output: The output of this MergeChannelsTaskInfo.
        :type output: :class:`g42cloudsdkmpc.v1.ObsObjInfo`
        """
        self._output = output

    @property
    def description(self):
        """Gets the description of this MergeChannelsTaskInfo.

        :return: The description of this MergeChannelsTaskInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MergeChannelsTaskInfo.

        :param description: The description of this MergeChannelsTaskInfo.
        :type description: str
        """
        self._description = description

    @property
    def audio_files(self):
        """Gets the audio_files of this MergeChannelsTaskInfo.

        :return: The audio_files of this MergeChannelsTaskInfo.
        :rtype: list[:class:`g42cloudsdkmpc.v1.AudioFile`]
        """
        return self._audio_files

    @audio_files.setter
    def audio_files(self, audio_files):
        """Sets the audio_files of this MergeChannelsTaskInfo.

        :param audio_files: The audio_files of this MergeChannelsTaskInfo.
        :type audio_files: list[:class:`g42cloudsdkmpc.v1.AudioFile`]
        """
        self._audio_files = audio_files

    @property
    def output_filename(self):
        """Gets the output_filename of this MergeChannelsTaskInfo.

        :return: The output_filename of this MergeChannelsTaskInfo.
        :rtype: str
        """
        return self._output_filename

    @output_filename.setter
    def output_filename(self, output_filename):
        """Sets the output_filename of this MergeChannelsTaskInfo.

        :param output_filename: The output_filename of this MergeChannelsTaskInfo.
        :type output_filename: str
        """
        self._output_filename = output_filename

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
        if not isinstance(other, MergeChannelsTaskInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
