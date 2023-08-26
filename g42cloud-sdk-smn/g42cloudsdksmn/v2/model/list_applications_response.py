# coding: utf-8

import six

from g42cloudsdkcore.sdk_response import SdkResponse
from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListApplicationsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'application_count': 'int',
        'applications': 'list[ApplicationItem]'
    }

    attribute_map = {
        'request_id': 'request_id',
        'application_count': 'application_count',
        'applications': 'applications'
    }

    def __init__(self, request_id=None, application_count=None, applications=None):
        """ListApplicationsResponse

        The model defined in g42cloud sdk

        :param request_id: The param of the ListApplicationsResponse
        :type request_id: str
        :param application_count: The param of the ListApplicationsResponse
        :type application_count: int
        :param applications: The param of the ListApplicationsResponse
        :type applications: list[:class:`g42cloudsdksmn.v2.ApplicationItem`]
        """
        
        super(ListApplicationsResponse, self).__init__()

        self._request_id = None
        self._application_count = None
        self._applications = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if application_count is not None:
            self.application_count = application_count
        if applications is not None:
            self.applications = applications

    @property
    def request_id(self):
        """Gets the request_id of this ListApplicationsResponse.

        :return: The request_id of this ListApplicationsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListApplicationsResponse.

        :param request_id: The request_id of this ListApplicationsResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def application_count(self):
        """Gets the application_count of this ListApplicationsResponse.

        :return: The application_count of this ListApplicationsResponse.
        :rtype: int
        """
        return self._application_count

    @application_count.setter
    def application_count(self, application_count):
        """Sets the application_count of this ListApplicationsResponse.

        :param application_count: The application_count of this ListApplicationsResponse.
        :type application_count: int
        """
        self._application_count = application_count

    @property
    def applications(self):
        """Gets the applications of this ListApplicationsResponse.

        :return: The applications of this ListApplicationsResponse.
        :rtype: list[:class:`g42cloudsdksmn.v2.ApplicationItem`]
        """
        return self._applications

    @applications.setter
    def applications(self, applications):
        """Sets the applications of this ListApplicationsResponse.

        :param applications: The applications of this ListApplicationsResponse.
        :type applications: list[:class:`g42cloudsdksmn.v2.ApplicationItem`]
        """
        self._applications = applications

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
        if not isinstance(other, ListApplicationsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
