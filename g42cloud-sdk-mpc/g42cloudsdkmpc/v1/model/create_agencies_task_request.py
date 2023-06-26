# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAgenciesTaskRequest:

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
        'body': 'AgenciesTaskReq'
    }

    attribute_map = {
        'authorization': 'Authorization',
        'x_project_id': 'X-Project_Id',
        'x_sdk_date': 'X-Sdk-Date',
        'body': 'body'
    }

    def __init__(self, authorization=None, x_project_id=None, x_sdk_date=None, body=None):
        """CreateAgenciesTaskRequest

        The model defined in g42cloud sdk

        :param authorization: The param of the CreateAgenciesTaskRequest
        :type authorization: str
        :param x_project_id: The param of the CreateAgenciesTaskRequest
        :type x_project_id: str
        :param x_sdk_date: The param of the CreateAgenciesTaskRequest
        :type x_sdk_date: str
        :param body: The param of the CreateAgenciesTaskRequest
        :type body: :class:`g42cloudsdkmpc.v1.AgenciesTaskReq`
        """
        
        

        self._authorization = None
        self._x_project_id = None
        self._x_sdk_date = None
        self._body = None
        self.discriminator = None

        if authorization is not None:
            self.authorization = authorization
        if x_project_id is not None:
            self.x_project_id = x_project_id
        if x_sdk_date is not None:
            self.x_sdk_date = x_sdk_date
        if body is not None:
            self.body = body

    @property
    def authorization(self):
        """Gets the authorization of this CreateAgenciesTaskRequest.

        :return: The authorization of this CreateAgenciesTaskRequest.
        :rtype: str
        """
        return self._authorization

    @authorization.setter
    def authorization(self, authorization):
        """Sets the authorization of this CreateAgenciesTaskRequest.

        :param authorization: The authorization of this CreateAgenciesTaskRequest.
        :type authorization: str
        """
        self._authorization = authorization

    @property
    def x_project_id(self):
        """Gets the x_project_id of this CreateAgenciesTaskRequest.

        :return: The x_project_id of this CreateAgenciesTaskRequest.
        :rtype: str
        """
        return self._x_project_id

    @x_project_id.setter
    def x_project_id(self, x_project_id):
        """Sets the x_project_id of this CreateAgenciesTaskRequest.

        :param x_project_id: The x_project_id of this CreateAgenciesTaskRequest.
        :type x_project_id: str
        """
        self._x_project_id = x_project_id

    @property
    def x_sdk_date(self):
        """Gets the x_sdk_date of this CreateAgenciesTaskRequest.

        :return: The x_sdk_date of this CreateAgenciesTaskRequest.
        :rtype: str
        """
        return self._x_sdk_date

    @x_sdk_date.setter
    def x_sdk_date(self, x_sdk_date):
        """Sets the x_sdk_date of this CreateAgenciesTaskRequest.

        :param x_sdk_date: The x_sdk_date of this CreateAgenciesTaskRequest.
        :type x_sdk_date: str
        """
        self._x_sdk_date = x_sdk_date

    @property
    def body(self):
        """Gets the body of this CreateAgenciesTaskRequest.

        :return: The body of this CreateAgenciesTaskRequest.
        :rtype: :class:`g42cloudsdkmpc.v1.AgenciesTaskReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateAgenciesTaskRequest.

        :param body: The body of this CreateAgenciesTaskRequest.
        :type body: :class:`g42cloudsdkmpc.v1.AgenciesTaskReq`
        """
        self._body = body

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
        if not isinstance(other, CreateAgenciesTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other