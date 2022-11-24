# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDomainsRequest:

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
        'business_type': 'str',
        'domain_status': 'str',
        'service_area': 'str',
        'page_size': 'int',
        'page_number': 'int',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'domain_name': 'domain_name',
        'business_type': 'business_type',
        'domain_status': 'domain_status',
        'service_area': 'service_area',
        'page_size': 'page_size',
        'page_number': 'page_number',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, domain_name=None, business_type=None, domain_status=None, service_area=None, page_size=None, page_number=None, enterprise_project_id=None):
        """ListDomainsRequest

        The model defined in g42cloud sdk

        :param domain_name: The param of the ListDomainsRequest
        :type domain_name: str
        :param business_type: The param of the ListDomainsRequest
        :type business_type: str
        :param domain_status: The param of the ListDomainsRequest
        :type domain_status: str
        :param service_area: The param of the ListDomainsRequest
        :type service_area: str
        :param page_size: The param of the ListDomainsRequest
        :type page_size: int
        :param page_number: The param of the ListDomainsRequest
        :type page_number: int
        :param enterprise_project_id: The param of the ListDomainsRequest
        :type enterprise_project_id: str
        """
        
        

        self._domain_name = None
        self._business_type = None
        self._domain_status = None
        self._service_area = None
        self._page_size = None
        self._page_number = None
        self._enterprise_project_id = None
        self.discriminator = None

        if domain_name is not None:
            self.domain_name = domain_name
        if business_type is not None:
            self.business_type = business_type
        if domain_status is not None:
            self.domain_status = domain_status
        if service_area is not None:
            self.service_area = service_area
        if page_size is not None:
            self.page_size = page_size
        if page_number is not None:
            self.page_number = page_number
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def domain_name(self):
        """Gets the domain_name of this ListDomainsRequest.

        :return: The domain_name of this ListDomainsRequest.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this ListDomainsRequest.

        :param domain_name: The domain_name of this ListDomainsRequest.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def business_type(self):
        """Gets the business_type of this ListDomainsRequest.

        :return: The business_type of this ListDomainsRequest.
        :rtype: str
        """
        return self._business_type

    @business_type.setter
    def business_type(self, business_type):
        """Sets the business_type of this ListDomainsRequest.

        :param business_type: The business_type of this ListDomainsRequest.
        :type business_type: str
        """
        self._business_type = business_type

    @property
    def domain_status(self):
        """Gets the domain_status of this ListDomainsRequest.

        :return: The domain_status of this ListDomainsRequest.
        :rtype: str
        """
        return self._domain_status

    @domain_status.setter
    def domain_status(self, domain_status):
        """Sets the domain_status of this ListDomainsRequest.

        :param domain_status: The domain_status of this ListDomainsRequest.
        :type domain_status: str
        """
        self._domain_status = domain_status

    @property
    def service_area(self):
        """Gets the service_area of this ListDomainsRequest.

        :return: The service_area of this ListDomainsRequest.
        :rtype: str
        """
        return self._service_area

    @service_area.setter
    def service_area(self, service_area):
        """Sets the service_area of this ListDomainsRequest.

        :param service_area: The service_area of this ListDomainsRequest.
        :type service_area: str
        """
        self._service_area = service_area

    @property
    def page_size(self):
        """Gets the page_size of this ListDomainsRequest.

        :return: The page_size of this ListDomainsRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ListDomainsRequest.

        :param page_size: The page_size of this ListDomainsRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def page_number(self):
        """Gets the page_number of this ListDomainsRequest.

        :return: The page_number of this ListDomainsRequest.
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this ListDomainsRequest.

        :param page_number: The page_number of this ListDomainsRequest.
        :type page_number: int
        """
        self._page_number = page_number

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListDomainsRequest.

        :return: The enterprise_project_id of this ListDomainsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListDomainsRequest.

        :param enterprise_project_id: The enterprise_project_id of this ListDomainsRequest.
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
        if not isinstance(other, ListDomainsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
