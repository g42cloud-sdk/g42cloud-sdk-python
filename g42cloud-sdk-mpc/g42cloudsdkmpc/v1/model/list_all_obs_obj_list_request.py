# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAllObsObjListRequest:

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
        'bucket': 'str',
        'prefix': 'str',
        'type': 'str'
    }

    attribute_map = {
        'authorization': 'Authorization',
        'x_project_id': 'X-Project_Id',
        'x_sdk_date': 'X-Sdk-Date',
        'bucket': 'bucket',
        'prefix': 'prefix',
        'type': 'type'
    }

    def __init__(self, authorization=None, x_project_id=None, x_sdk_date=None, bucket=None, prefix=None, type=None):
        """ListAllObsObjListRequest

        The model defined in g42cloud sdk

        :param authorization: The param of the ListAllObsObjListRequest
        :type authorization: str
        :param x_project_id: The param of the ListAllObsObjListRequest
        :type x_project_id: str
        :param x_sdk_date: The param of the ListAllObsObjListRequest
        :type x_sdk_date: str
        :param bucket: The param of the ListAllObsObjListRequest
        :type bucket: str
        :param prefix: The param of the ListAllObsObjListRequest
        :type prefix: str
        :param type: The param of the ListAllObsObjListRequest
        :type type: str
        """
        
        

        self._authorization = None
        self._x_project_id = None
        self._x_sdk_date = None
        self._bucket = None
        self._prefix = None
        self._type = None
        self.discriminator = None

        if authorization is not None:
            self.authorization = authorization
        if x_project_id is not None:
            self.x_project_id = x_project_id
        if x_sdk_date is not None:
            self.x_sdk_date = x_sdk_date
        self.bucket = bucket
        if prefix is not None:
            self.prefix = prefix
        if type is not None:
            self.type = type

    @property
    def authorization(self):
        """Gets the authorization of this ListAllObsObjListRequest.

        :return: The authorization of this ListAllObsObjListRequest.
        :rtype: str
        """
        return self._authorization

    @authorization.setter
    def authorization(self, authorization):
        """Sets the authorization of this ListAllObsObjListRequest.

        :param authorization: The authorization of this ListAllObsObjListRequest.
        :type authorization: str
        """
        self._authorization = authorization

    @property
    def x_project_id(self):
        """Gets the x_project_id of this ListAllObsObjListRequest.

        :return: The x_project_id of this ListAllObsObjListRequest.
        :rtype: str
        """
        return self._x_project_id

    @x_project_id.setter
    def x_project_id(self, x_project_id):
        """Sets the x_project_id of this ListAllObsObjListRequest.

        :param x_project_id: The x_project_id of this ListAllObsObjListRequest.
        :type x_project_id: str
        """
        self._x_project_id = x_project_id

    @property
    def x_sdk_date(self):
        """Gets the x_sdk_date of this ListAllObsObjListRequest.

        :return: The x_sdk_date of this ListAllObsObjListRequest.
        :rtype: str
        """
        return self._x_sdk_date

    @x_sdk_date.setter
    def x_sdk_date(self, x_sdk_date):
        """Sets the x_sdk_date of this ListAllObsObjListRequest.

        :param x_sdk_date: The x_sdk_date of this ListAllObsObjListRequest.
        :type x_sdk_date: str
        """
        self._x_sdk_date = x_sdk_date

    @property
    def bucket(self):
        """Gets the bucket of this ListAllObsObjListRequest.

        :return: The bucket of this ListAllObsObjListRequest.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this ListAllObsObjListRequest.

        :param bucket: The bucket of this ListAllObsObjListRequest.
        :type bucket: str
        """
        self._bucket = bucket

    @property
    def prefix(self):
        """Gets the prefix of this ListAllObsObjListRequest.

        :return: The prefix of this ListAllObsObjListRequest.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this ListAllObsObjListRequest.

        :param prefix: The prefix of this ListAllObsObjListRequest.
        :type prefix: str
        """
        self._prefix = prefix

    @property
    def type(self):
        """Gets the type of this ListAllObsObjListRequest.

        :return: The type of this ListAllObsObjListRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListAllObsObjListRequest.

        :param type: The type of this ListAllObsObjListRequest.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ListAllObsObjListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
