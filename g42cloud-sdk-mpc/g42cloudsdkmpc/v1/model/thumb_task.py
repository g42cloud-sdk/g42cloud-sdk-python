# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class ThumbTask:

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
        'input': 'ObsObjInfo',
        'output': 'ObsObjInfo',
        'output_file_name': 'str',
        'user_data': 'str',
        'description': 'str',
        'thumbnail_info': 'list[PicInfo]'
    }

    attribute_map = {
        'task_id': 'task_id',
        'status': 'status',
        'create_time': 'create_time',
        'end_time': 'end_time',
        'input': 'input',
        'output': 'output',
        'output_file_name': 'output_file_name',
        'user_data': 'user_data',
        'description': 'description',
        'thumbnail_info': 'thumbnail_info'
    }

    def __init__(self, task_id=None, status=None, create_time=None, end_time=None, input=None, output=None, output_file_name=None, user_data=None, description=None, thumbnail_info=None):
        """ThumbTask

        The model defined in g42cloud sdk

        :param task_id: The param of the ThumbTask
        :type task_id: str
        :param status: The param of the ThumbTask
        :type status: str
        :param create_time: The param of the ThumbTask
        :type create_time: str
        :param end_time: The param of the ThumbTask
        :type end_time: str
        :param input: The param of the ThumbTask
        :type input: :class:`g42cloudsdkmpc.v1.ObsObjInfo`
        :param output: The param of the ThumbTask
        :type output: :class:`g42cloudsdkmpc.v1.ObsObjInfo`
        :param output_file_name: The param of the ThumbTask
        :type output_file_name: str
        :param user_data: The param of the ThumbTask
        :type user_data: str
        :param description: The param of the ThumbTask
        :type description: str
        :param thumbnail_info: The param of the ThumbTask
        :type thumbnail_info: list[:class:`g42cloudsdkmpc.v1.PicInfo`]
        """
        
        

        self._task_id = None
        self._status = None
        self._create_time = None
        self._end_time = None
        self._input = None
        self._output = None
        self._output_file_name = None
        self._user_data = None
        self._description = None
        self._thumbnail_info = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time
        if end_time is not None:
            self.end_time = end_time
        if input is not None:
            self.input = input
        if output is not None:
            self.output = output
        if output_file_name is not None:
            self.output_file_name = output_file_name
        if user_data is not None:
            self.user_data = user_data
        if description is not None:
            self.description = description
        if thumbnail_info is not None:
            self.thumbnail_info = thumbnail_info

    @property
    def task_id(self):
        """Gets the task_id of this ThumbTask.

        :return: The task_id of this ThumbTask.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this ThumbTask.

        :param task_id: The task_id of this ThumbTask.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def status(self):
        """Gets the status of this ThumbTask.

        :return: The status of this ThumbTask.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ThumbTask.

        :param status: The status of this ThumbTask.
        :type status: str
        """
        self._status = status

    @property
    def create_time(self):
        """Gets the create_time of this ThumbTask.

        :return: The create_time of this ThumbTask.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ThumbTask.

        :param create_time: The create_time of this ThumbTask.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def end_time(self):
        """Gets the end_time of this ThumbTask.

        :return: The end_time of this ThumbTask.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ThumbTask.

        :param end_time: The end_time of this ThumbTask.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def input(self):
        """Gets the input of this ThumbTask.

        :return: The input of this ThumbTask.
        :rtype: :class:`g42cloudsdkmpc.v1.ObsObjInfo`
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this ThumbTask.

        :param input: The input of this ThumbTask.
        :type input: :class:`g42cloudsdkmpc.v1.ObsObjInfo`
        """
        self._input = input

    @property
    def output(self):
        """Gets the output of this ThumbTask.

        :return: The output of this ThumbTask.
        :rtype: :class:`g42cloudsdkmpc.v1.ObsObjInfo`
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this ThumbTask.

        :param output: The output of this ThumbTask.
        :type output: :class:`g42cloudsdkmpc.v1.ObsObjInfo`
        """
        self._output = output

    @property
    def output_file_name(self):
        """Gets the output_file_name of this ThumbTask.

        :return: The output_file_name of this ThumbTask.
        :rtype: str
        """
        return self._output_file_name

    @output_file_name.setter
    def output_file_name(self, output_file_name):
        """Sets the output_file_name of this ThumbTask.

        :param output_file_name: The output_file_name of this ThumbTask.
        :type output_file_name: str
        """
        self._output_file_name = output_file_name

    @property
    def user_data(self):
        """Gets the user_data of this ThumbTask.

        :return: The user_data of this ThumbTask.
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this ThumbTask.

        :param user_data: The user_data of this ThumbTask.
        :type user_data: str
        """
        self._user_data = user_data

    @property
    def description(self):
        """Gets the description of this ThumbTask.

        :return: The description of this ThumbTask.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ThumbTask.

        :param description: The description of this ThumbTask.
        :type description: str
        """
        self._description = description

    @property
    def thumbnail_info(self):
        """Gets the thumbnail_info of this ThumbTask.

        :return: The thumbnail_info of this ThumbTask.
        :rtype: list[:class:`g42cloudsdkmpc.v1.PicInfo`]
        """
        return self._thumbnail_info

    @thumbnail_info.setter
    def thumbnail_info(self, thumbnail_info):
        """Sets the thumbnail_info of this ThumbTask.

        :param thumbnail_info: The thumbnail_info of this ThumbTask.
        :type thumbnail_info: list[:class:`g42cloudsdkmpc.v1.PicInfo`]
        """
        self._thumbnail_info = thumbnail_info

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
        if not isinstance(other, ThumbTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
