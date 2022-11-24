# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLogsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_name': 'str',
        'query_date': 'int',
        'page_size': 'int',
        'page_number': 'int',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'domain_name': 'domain_name',
        'query_date': 'query_date',
        'page_size': 'page_size',
        'page_number': 'page_number',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, domain_name=None, query_date=None, page_size=None, page_number=None, enterprise_project_id=None):
        """ShowLogsRequest

        The model defined in g42cloud sdk

        :param domain_name: The param of the ShowLogsRequest
        :type domain_name: str
        :param query_date: The param of the ShowLogsRequest
        :type query_date: int
        :param page_size: The param of the ShowLogsRequest
        :type page_size: int
        :param page_number: The param of the ShowLogsRequest
        :type page_number: int
        :param enterprise_project_id: The param of the ShowLogsRequest
        :type enterprise_project_id: str
        """
        
        

        self._domain_name = None
        self._query_date = None
        self._page_size = None
        self._page_number = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.domain_name = domain_name
        self.query_date = query_date
        if page_size is not None:
            self.page_size = page_size
        if page_number is not None:
            self.page_number = page_number
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def domain_name(self):
        """Gets the domain_name of this ShowLogsRequest.

        :return: The domain_name of this ShowLogsRequest.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this ShowLogsRequest.

        :param domain_name: The domain_name of this ShowLogsRequest.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def query_date(self):
        """Gets the query_date of this ShowLogsRequest.

        :return: The query_date of this ShowLogsRequest.
        :rtype: int
        """
        return self._query_date

    @query_date.setter
    def query_date(self, query_date):
        """Sets the query_date of this ShowLogsRequest.

        :param query_date: The query_date of this ShowLogsRequest.
        :type query_date: int
        """
        self._query_date = query_date

    @property
    def page_size(self):
        """Gets the page_size of this ShowLogsRequest.

        :return: The page_size of this ShowLogsRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ShowLogsRequest.

        :param page_size: The page_size of this ShowLogsRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def page_number(self):
        """Gets the page_number of this ShowLogsRequest.

        :return: The page_number of this ShowLogsRequest.
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this ShowLogsRequest.

        :param page_number: The page_number of this ShowLogsRequest.
        :type page_number: int
        """
        self._page_number = page_number

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ShowLogsRequest.

        :return: The enterprise_project_id of this ShowLogsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ShowLogsRequest.

        :param enterprise_project_id: The enterprise_project_id of this ShowLogsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ShowLogsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
