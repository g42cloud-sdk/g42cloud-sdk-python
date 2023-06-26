# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class EachEncryptRsp:

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
        'output_file_name': 'list[str]',
        'user_data': 'str',
        'description': 'str'
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
        'description': 'description'
    }

    def __init__(self, task_id=None, status=None, create_time=None, end_time=None, input=None, output=None, output_file_name=None, user_data=None, description=None):
        """EachEncryptRsp

        The model defined in g42cloud sdk

        :param task_id: The param of the EachEncryptRsp
        :type task_id: str
        :param status: The param of the EachEncryptRsp
        :type status: str
        :param create_time: The param of the EachEncryptRsp
        :type create_time: str
        :param end_time: The param of the EachEncryptRsp
        :type end_time: str
        :param input: The param of the EachEncryptRsp
        :type input: :class:`g42cloudsdkmpc.v1.ObsObjInfo`
        :param output: The param of the EachEncryptRsp
        :type output: :class:`g42cloudsdkmpc.v1.ObsObjInfo`
        :param output_file_name: The param of the EachEncryptRsp
        :type output_file_name: list[str]
        :param user_data: The param of the EachEncryptRsp
        :type user_data: str
        :param description: The param of the EachEncryptRsp
        :type description: str
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

    @property
    def task_id(self):
        """Gets the task_id of this EachEncryptRsp.

        :return: The task_id of this EachEncryptRsp.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this EachEncryptRsp.

        :param task_id: The task_id of this EachEncryptRsp.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def status(self):
        """Gets the status of this EachEncryptRsp.

        :return: The status of this EachEncryptRsp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this EachEncryptRsp.

        :param status: The status of this EachEncryptRsp.
        :type status: str
        """
        self._status = status

    @property
    def create_time(self):
        """Gets the create_time of this EachEncryptRsp.

        :return: The create_time of this EachEncryptRsp.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this EachEncryptRsp.

        :param create_time: The create_time of this EachEncryptRsp.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def end_time(self):
        """Gets the end_time of this EachEncryptRsp.

        :return: The end_time of this EachEncryptRsp.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this EachEncryptRsp.

        :param end_time: The end_time of this EachEncryptRsp.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def input(self):
        """Gets the input of this EachEncryptRsp.

        :return: The input of this EachEncryptRsp.
        :rtype: :class:`g42cloudsdkmpc.v1.ObsObjInfo`
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this EachEncryptRsp.

        :param input: The input of this EachEncryptRsp.
        :type input: :class:`g42cloudsdkmpc.v1.ObsObjInfo`
        """
        self._input = input

    @property
    def output(self):
        """Gets the output of this EachEncryptRsp.

        :return: The output of this EachEncryptRsp.
        :rtype: :class:`g42cloudsdkmpc.v1.ObsObjInfo`
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this EachEncryptRsp.

        :param output: The output of this EachEncryptRsp.
        :type output: :class:`g42cloudsdkmpc.v1.ObsObjInfo`
        """
        self._output = output

    @property
    def output_file_name(self):
        """Gets the output_file_name of this EachEncryptRsp.

        :return: The output_file_name of this EachEncryptRsp.
        :rtype: list[str]
        """
        return self._output_file_name

    @output_file_name.setter
    def output_file_name(self, output_file_name):
        """Sets the output_file_name of this EachEncryptRsp.

        :param output_file_name: The output_file_name of this EachEncryptRsp.
        :type output_file_name: list[str]
        """
        self._output_file_name = output_file_name

    @property
    def user_data(self):
        """Gets the user_data of this EachEncryptRsp.

        :return: The user_data of this EachEncryptRsp.
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this EachEncryptRsp.

        :param user_data: The user_data of this EachEncryptRsp.
        :type user_data: str
        """
        self._user_data = user_data

    @property
    def description(self):
        """Gets the description of this EachEncryptRsp.

        :return: The description of this EachEncryptRsp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EachEncryptRsp.

        :param description: The description of this EachEncryptRsp.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, EachEncryptRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
