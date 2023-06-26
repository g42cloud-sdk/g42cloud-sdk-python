# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class MbTasksReportReq:

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
        'task_name': 'str',
        'retry': 'bool',
        'parameter': 'MbTaskParameter'
    }

    attribute_map = {
        'task_id': 'task_id',
        'status': 'status',
        'task_name': 'task_name',
        'retry': 'retry',
        'parameter': 'parameter'
    }

    def __init__(self, task_id=None, status=None, task_name=None, retry=None, parameter=None):
        """MbTasksReportReq

        The model defined in g42cloud sdk

        :param task_id: The param of the MbTasksReportReq
        :type task_id: str
        :param status: The param of the MbTasksReportReq
        :type status: str
        :param task_name: The param of the MbTasksReportReq
        :type task_name: str
        :param retry: The param of the MbTasksReportReq
        :type retry: bool
        :param parameter: The param of the MbTasksReportReq
        :type parameter: :class:`g42cloudsdkmpc.v1.MbTaskParameter`
        """
        
        

        self._task_id = None
        self._status = None
        self._task_name = None
        self._retry = None
        self._parameter = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if status is not None:
            self.status = status
        if task_name is not None:
            self.task_name = task_name
        if retry is not None:
            self.retry = retry
        if parameter is not None:
            self.parameter = parameter

    @property
    def task_id(self):
        """Gets the task_id of this MbTasksReportReq.

        :return: The task_id of this MbTasksReportReq.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this MbTasksReportReq.

        :param task_id: The task_id of this MbTasksReportReq.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def status(self):
        """Gets the status of this MbTasksReportReq.

        :return: The status of this MbTasksReportReq.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MbTasksReportReq.

        :param status: The status of this MbTasksReportReq.
        :type status: str
        """
        self._status = status

    @property
    def task_name(self):
        """Gets the task_name of this MbTasksReportReq.

        :return: The task_name of this MbTasksReportReq.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this MbTasksReportReq.

        :param task_name: The task_name of this MbTasksReportReq.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def retry(self):
        """Gets the retry of this MbTasksReportReq.

        :return: The retry of this MbTasksReportReq.
        :rtype: bool
        """
        return self._retry

    @retry.setter
    def retry(self, retry):
        """Sets the retry of this MbTasksReportReq.

        :param retry: The retry of this MbTasksReportReq.
        :type retry: bool
        """
        self._retry = retry

    @property
    def parameter(self):
        """Gets the parameter of this MbTasksReportReq.

        :return: The parameter of this MbTasksReportReq.
        :rtype: :class:`g42cloudsdkmpc.v1.MbTaskParameter`
        """
        return self._parameter

    @parameter.setter
    def parameter(self, parameter):
        """Sets the parameter of this MbTasksReportReq.

        :param parameter: The parameter of this MbTasksReportReq.
        :type parameter: :class:`g42cloudsdkmpc.v1.MbTaskParameter`
        """
        self._parameter = parameter

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
        if not isinstance(other, MbTasksReportReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
