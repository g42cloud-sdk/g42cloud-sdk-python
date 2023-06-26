# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListStatSummaryRequest:

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
        'start_time': 'str',
        'end_time': 'str',
        'stat_type': 'str'
    }

    attribute_map = {
        'authorization': 'Authorization',
        'x_project_id': 'X-Project_Id',
        'x_sdk_date': 'X-Sdk-Date',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'stat_type': 'stat_type'
    }

    def __init__(self, authorization=None, x_project_id=None, x_sdk_date=None, start_time=None, end_time=None, stat_type=None):
        """ListStatSummaryRequest

        The model defined in g42cloud sdk

        :param authorization: The param of the ListStatSummaryRequest
        :type authorization: str
        :param x_project_id: The param of the ListStatSummaryRequest
        :type x_project_id: str
        :param x_sdk_date: The param of the ListStatSummaryRequest
        :type x_sdk_date: str
        :param start_time: The param of the ListStatSummaryRequest
        :type start_time: str
        :param end_time: The param of the ListStatSummaryRequest
        :type end_time: str
        :param stat_type: The param of the ListStatSummaryRequest
        :type stat_type: str
        """
        
        

        self._authorization = None
        self._x_project_id = None
        self._x_sdk_date = None
        self._start_time = None
        self._end_time = None
        self._stat_type = None
        self.discriminator = None

        if authorization is not None:
            self.authorization = authorization
        if x_project_id is not None:
            self.x_project_id = x_project_id
        if x_sdk_date is not None:
            self.x_sdk_date = x_sdk_date
        self.start_time = start_time
        self.end_time = end_time
        self.stat_type = stat_type

    @property
    def authorization(self):
        """Gets the authorization of this ListStatSummaryRequest.

        :return: The authorization of this ListStatSummaryRequest.
        :rtype: str
        """
        return self._authorization

    @authorization.setter
    def authorization(self, authorization):
        """Sets the authorization of this ListStatSummaryRequest.

        :param authorization: The authorization of this ListStatSummaryRequest.
        :type authorization: str
        """
        self._authorization = authorization

    @property
    def x_project_id(self):
        """Gets the x_project_id of this ListStatSummaryRequest.

        :return: The x_project_id of this ListStatSummaryRequest.
        :rtype: str
        """
        return self._x_project_id

    @x_project_id.setter
    def x_project_id(self, x_project_id):
        """Sets the x_project_id of this ListStatSummaryRequest.

        :param x_project_id: The x_project_id of this ListStatSummaryRequest.
        :type x_project_id: str
        """
        self._x_project_id = x_project_id

    @property
    def x_sdk_date(self):
        """Gets the x_sdk_date of this ListStatSummaryRequest.

        :return: The x_sdk_date of this ListStatSummaryRequest.
        :rtype: str
        """
        return self._x_sdk_date

    @x_sdk_date.setter
    def x_sdk_date(self, x_sdk_date):
        """Sets the x_sdk_date of this ListStatSummaryRequest.

        :param x_sdk_date: The x_sdk_date of this ListStatSummaryRequest.
        :type x_sdk_date: str
        """
        self._x_sdk_date = x_sdk_date

    @property
    def start_time(self):
        """Gets the start_time of this ListStatSummaryRequest.

        :return: The start_time of this ListStatSummaryRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListStatSummaryRequest.

        :param start_time: The start_time of this ListStatSummaryRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListStatSummaryRequest.

        :return: The end_time of this ListStatSummaryRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListStatSummaryRequest.

        :param end_time: The end_time of this ListStatSummaryRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def stat_type(self):
        """Gets the stat_type of this ListStatSummaryRequest.

        :return: The stat_type of this ListStatSummaryRequest.
        :rtype: str
        """
        return self._stat_type

    @stat_type.setter
    def stat_type(self, stat_type):
        """Sets the stat_type of this ListStatSummaryRequest.

        :param stat_type: The stat_type of this ListStatSummaryRequest.
        :type stat_type: str
        """
        self._stat_type = stat_type

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
        if not isinstance(other, ListStatSummaryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
