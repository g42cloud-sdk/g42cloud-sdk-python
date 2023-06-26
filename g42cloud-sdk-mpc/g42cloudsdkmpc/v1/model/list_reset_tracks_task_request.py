# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResetTracksTaskRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'authorization': 'str',
        'x_project_id': 'str',
        'x_sdk_date': 'str',
        'task_id': 'list[str]',
        'status': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'page': 'int',
        'size': 'int'
    }

    attribute_map = {
        'authorization': 'Authorization',
        'x_project_id': 'X-Project_Id',
        'x_sdk_date': 'X-Sdk-Date',
        'task_id': 'task_id',
        'status': 'status',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'page': 'page',
        'size': 'size'
    }

    def __init__(self, authorization=None, x_project_id=None, x_sdk_date=None, task_id=None, status=None, start_time=None, end_time=None, page=None, size=None):
        """ListResetTracksTaskRequest

        The model defined in g42cloud sdk

        :param authorization: The param of the ListResetTracksTaskRequest
        :type authorization: str
        :param x_project_id: The param of the ListResetTracksTaskRequest
        :type x_project_id: str
        :param x_sdk_date: The param of the ListResetTracksTaskRequest
        :type x_sdk_date: str
        :param task_id: The param of the ListResetTracksTaskRequest
        :type task_id: list[str]
        :param status: The param of the ListResetTracksTaskRequest
        :type status: str
        :param start_time: The param of the ListResetTracksTaskRequest
        :type start_time: str
        :param end_time: The param of the ListResetTracksTaskRequest
        :type end_time: str
        :param page: The param of the ListResetTracksTaskRequest
        :type page: int
        :param size: The param of the ListResetTracksTaskRequest
        :type size: int
        """
        
        

        self._authorization = None
        self._x_project_id = None
        self._x_sdk_date = None
        self._task_id = None
        self._status = None
        self._start_time = None
        self._end_time = None
        self._page = None
        self._size = None
        self.discriminator = None

        if authorization is not None:
            self.authorization = authorization
        if x_project_id is not None:
            self.x_project_id = x_project_id
        if x_sdk_date is not None:
            self.x_sdk_date = x_sdk_date
        if task_id is not None:
            self.task_id = task_id
        if status is not None:
            self.status = status
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if page is not None:
            self.page = page
        if size is not None:
            self.size = size

    @property
    def authorization(self):
        """Gets the authorization of this ListResetTracksTaskRequest.

        :return: The authorization of this ListResetTracksTaskRequest.
        :rtype: str
        """
        return self._authorization

    @authorization.setter
    def authorization(self, authorization):
        """Sets the authorization of this ListResetTracksTaskRequest.

        :param authorization: The authorization of this ListResetTracksTaskRequest.
        :type authorization: str
        """
        self._authorization = authorization

    @property
    def x_project_id(self):
        """Gets the x_project_id of this ListResetTracksTaskRequest.

        :return: The x_project_id of this ListResetTracksTaskRequest.
        :rtype: str
        """
        return self._x_project_id

    @x_project_id.setter
    def x_project_id(self, x_project_id):
        """Sets the x_project_id of this ListResetTracksTaskRequest.

        :param x_project_id: The x_project_id of this ListResetTracksTaskRequest.
        :type x_project_id: str
        """
        self._x_project_id = x_project_id

    @property
    def x_sdk_date(self):
        """Gets the x_sdk_date of this ListResetTracksTaskRequest.

        :return: The x_sdk_date of this ListResetTracksTaskRequest.
        :rtype: str
        """
        return self._x_sdk_date

    @x_sdk_date.setter
    def x_sdk_date(self, x_sdk_date):
        """Sets the x_sdk_date of this ListResetTracksTaskRequest.

        :param x_sdk_date: The x_sdk_date of this ListResetTracksTaskRequest.
        :type x_sdk_date: str
        """
        self._x_sdk_date = x_sdk_date

    @property
    def task_id(self):
        """Gets the task_id of this ListResetTracksTaskRequest.

        :return: The task_id of this ListResetTracksTaskRequest.
        :rtype: list[str]
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this ListResetTracksTaskRequest.

        :param task_id: The task_id of this ListResetTracksTaskRequest.
        :type task_id: list[str]
        """
        self._task_id = task_id

    @property
    def status(self):
        """Gets the status of this ListResetTracksTaskRequest.

        :return: The status of this ListResetTracksTaskRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListResetTracksTaskRequest.

        :param status: The status of this ListResetTracksTaskRequest.
        :type status: str
        """
        self._status = status

    @property
    def start_time(self):
        """Gets the start_time of this ListResetTracksTaskRequest.

        :return: The start_time of this ListResetTracksTaskRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListResetTracksTaskRequest.

        :param start_time: The start_time of this ListResetTracksTaskRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListResetTracksTaskRequest.

        :return: The end_time of this ListResetTracksTaskRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListResetTracksTaskRequest.

        :param end_time: The end_time of this ListResetTracksTaskRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def page(self):
        """Gets the page of this ListResetTracksTaskRequest.

        :return: The page of this ListResetTracksTaskRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListResetTracksTaskRequest.

        :param page: The page of this ListResetTracksTaskRequest.
        :type page: int
        """
        self._page = page

    @property
    def size(self):
        """Gets the size of this ListResetTracksTaskRequest.

        :return: The size of this ListResetTracksTaskRequest.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ListResetTracksTaskRequest.

        :param size: The size of this ListResetTracksTaskRequest.
        :type size: int
        """
        self._size = size

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
        if not isinstance(other, ListResetTracksTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
