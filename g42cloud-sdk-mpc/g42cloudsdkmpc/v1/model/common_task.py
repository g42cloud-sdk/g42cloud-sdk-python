# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class CommonTask:

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
        'start_time': 'str',
        'end_time': 'str',
        'error_code': 'str',
        'description': 'str',
        'user_data': 'str',
        'input': 'ObsObjInfo',
        'output': 'ObsObjInfo'
    }

    attribute_map = {
        'task_id': 'task_id',
        'status': 'status',
        'create_time': 'create_time',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'error_code': 'error_code',
        'description': 'description',
        'user_data': 'user_data',
        'input': 'input',
        'output': 'output'
    }

    def __init__(self, task_id=None, status=None, create_time=None, start_time=None, end_time=None, error_code=None, description=None, user_data=None, input=None, output=None):
        """CommonTask

        The model defined in g42cloud sdk

        :param task_id: The param of the CommonTask
        :type task_id: str
        :param status: The param of the CommonTask
        :type status: str
        :param create_time: The param of the CommonTask
        :type create_time: str
        :param start_time: The param of the CommonTask
        :type start_time: str
        :param end_time: The param of the CommonTask
        :type end_time: str
        :param error_code: The param of the CommonTask
        :type error_code: str
        :param description: The param of the CommonTask
        :type description: str
        :param user_data: The param of the CommonTask
        :type user_data: str
        :param input: The param of the CommonTask
        :type input: :class:`g42cloudsdkmpc.v1.ObsObjInfo`
        :param output: The param of the CommonTask
        :type output: :class:`g42cloudsdkmpc.v1.ObsObjInfo`
        """
        
        

        self._task_id = None
        self._status = None
        self._create_time = None
        self._start_time = None
        self._end_time = None
        self._error_code = None
        self._description = None
        self._user_data = None
        self._input = None
        self._output = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if error_code is not None:
            self.error_code = error_code
        if description is not None:
            self.description = description
        if user_data is not None:
            self.user_data = user_data
        if input is not None:
            self.input = input
        if output is not None:
            self.output = output

    @property
    def task_id(self):
        """Gets the task_id of this CommonTask.

        :return: The task_id of this CommonTask.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this CommonTask.

        :param task_id: The task_id of this CommonTask.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def status(self):
        """Gets the status of this CommonTask.

        :return: The status of this CommonTask.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CommonTask.

        :param status: The status of this CommonTask.
        :type status: str
        """
        self._status = status

    @property
    def create_time(self):
        """Gets the create_time of this CommonTask.

        :return: The create_time of this CommonTask.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CommonTask.

        :param create_time: The create_time of this CommonTask.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def start_time(self):
        """Gets the start_time of this CommonTask.

        :return: The start_time of this CommonTask.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this CommonTask.

        :param start_time: The start_time of this CommonTask.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this CommonTask.

        :return: The end_time of this CommonTask.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this CommonTask.

        :param end_time: The end_time of this CommonTask.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def error_code(self):
        """Gets the error_code of this CommonTask.

        :return: The error_code of this CommonTask.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this CommonTask.

        :param error_code: The error_code of this CommonTask.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def description(self):
        """Gets the description of this CommonTask.

        :return: The description of this CommonTask.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CommonTask.

        :param description: The description of this CommonTask.
        :type description: str
        """
        self._description = description

    @property
    def user_data(self):
        """Gets the user_data of this CommonTask.

        :return: The user_data of this CommonTask.
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this CommonTask.

        :param user_data: The user_data of this CommonTask.
        :type user_data: str
        """
        self._user_data = user_data

    @property
    def input(self):
        """Gets the input of this CommonTask.

        :return: The input of this CommonTask.
        :rtype: :class:`g42cloudsdkmpc.v1.ObsObjInfo`
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this CommonTask.

        :param input: The input of this CommonTask.
        :type input: :class:`g42cloudsdkmpc.v1.ObsObjInfo`
        """
        self._input = input

    @property
    def output(self):
        """Gets the output of this CommonTask.

        :return: The output of this CommonTask.
        :rtype: :class:`g42cloudsdkmpc.v1.ObsObjInfo`
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this CommonTask.

        :param output: The output of this CommonTask.
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
        if not isinstance(other, CommonTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
