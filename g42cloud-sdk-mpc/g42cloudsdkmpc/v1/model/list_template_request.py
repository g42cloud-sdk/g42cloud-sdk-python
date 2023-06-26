# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTemplateRequest:

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
        'x_vod_project_id': 'str',
        'template_id': 'list[int]',
        'page': 'int',
        'size': 'int'
    }

    attribute_map = {
        'authorization': 'Authorization',
        'x_project_id': 'X-Project_Id',
        'x_sdk_date': 'X-Sdk-Date',
        'x_vod_project_id': 'x-vod-projectId',
        'template_id': 'template_id',
        'page': 'page',
        'size': 'size'
    }

    def __init__(self, authorization=None, x_project_id=None, x_sdk_date=None, x_vod_project_id=None, template_id=None, page=None, size=None):
        """ListTemplateRequest

        The model defined in g42cloud sdk

        :param authorization: The param of the ListTemplateRequest
        :type authorization: str
        :param x_project_id: The param of the ListTemplateRequest
        :type x_project_id: str
        :param x_sdk_date: The param of the ListTemplateRequest
        :type x_sdk_date: str
        :param x_vod_project_id: The param of the ListTemplateRequest
        :type x_vod_project_id: str
        :param template_id: The param of the ListTemplateRequest
        :type template_id: list[int]
        :param page: The param of the ListTemplateRequest
        :type page: int
        :param size: The param of the ListTemplateRequest
        :type size: int
        """
        
        

        self._authorization = None
        self._x_project_id = None
        self._x_sdk_date = None
        self._x_vod_project_id = None
        self._template_id = None
        self._page = None
        self._size = None
        self.discriminator = None

        if authorization is not None:
            self.authorization = authorization
        if x_project_id is not None:
            self.x_project_id = x_project_id
        if x_sdk_date is not None:
            self.x_sdk_date = x_sdk_date
        if x_vod_project_id is not None:
            self.x_vod_project_id = x_vod_project_id
        if template_id is not None:
            self.template_id = template_id
        if page is not None:
            self.page = page
        if size is not None:
            self.size = size

    @property
    def authorization(self):
        """Gets the authorization of this ListTemplateRequest.

        :return: The authorization of this ListTemplateRequest.
        :rtype: str
        """
        return self._authorization

    @authorization.setter
    def authorization(self, authorization):
        """Sets the authorization of this ListTemplateRequest.

        :param authorization: The authorization of this ListTemplateRequest.
        :type authorization: str
        """
        self._authorization = authorization

    @property
    def x_project_id(self):
        """Gets the x_project_id of this ListTemplateRequest.

        :return: The x_project_id of this ListTemplateRequest.
        :rtype: str
        """
        return self._x_project_id

    @x_project_id.setter
    def x_project_id(self, x_project_id):
        """Sets the x_project_id of this ListTemplateRequest.

        :param x_project_id: The x_project_id of this ListTemplateRequest.
        :type x_project_id: str
        """
        self._x_project_id = x_project_id

    @property
    def x_sdk_date(self):
        """Gets the x_sdk_date of this ListTemplateRequest.

        :return: The x_sdk_date of this ListTemplateRequest.
        :rtype: str
        """
        return self._x_sdk_date

    @x_sdk_date.setter
    def x_sdk_date(self, x_sdk_date):
        """Sets the x_sdk_date of this ListTemplateRequest.

        :param x_sdk_date: The x_sdk_date of this ListTemplateRequest.
        :type x_sdk_date: str
        """
        self._x_sdk_date = x_sdk_date

    @property
    def x_vod_project_id(self):
        """Gets the x_vod_project_id of this ListTemplateRequest.

        :return: The x_vod_project_id of this ListTemplateRequest.
        :rtype: str
        """
        return self._x_vod_project_id

    @x_vod_project_id.setter
    def x_vod_project_id(self, x_vod_project_id):
        """Sets the x_vod_project_id of this ListTemplateRequest.

        :param x_vod_project_id: The x_vod_project_id of this ListTemplateRequest.
        :type x_vod_project_id: str
        """
        self._x_vod_project_id = x_vod_project_id

    @property
    def template_id(self):
        """Gets the template_id of this ListTemplateRequest.

        :return: The template_id of this ListTemplateRequest.
        :rtype: list[int]
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this ListTemplateRequest.

        :param template_id: The template_id of this ListTemplateRequest.
        :type template_id: list[int]
        """
        self._template_id = template_id

    @property
    def page(self):
        """Gets the page of this ListTemplateRequest.

        :return: The page of this ListTemplateRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListTemplateRequest.

        :param page: The page of this ListTemplateRequest.
        :type page: int
        """
        self._page = page

    @property
    def size(self):
        """Gets the size of this ListTemplateRequest.

        :return: The size of this ListTemplateRequest.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ListTemplateRequest.

        :param size: The size of this ListTemplateRequest.
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
        if not isinstance(other, ListTemplateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
