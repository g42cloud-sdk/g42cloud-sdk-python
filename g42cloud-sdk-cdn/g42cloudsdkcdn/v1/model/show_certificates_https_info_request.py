# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCertificatesHttpsInfoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'page_size': 'int',
        'page_number': 'int',
        'domain_name': 'str',
        'user_domain_id': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'page_size': 'page_size',
        'page_number': 'page_number',
        'domain_name': 'domain_name',
        'user_domain_id': 'user_domain_id',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, page_size=None, page_number=None, domain_name=None, user_domain_id=None, enterprise_project_id=None):
        """ShowCertificatesHttpsInfoRequest

        The model defined in g42cloud sdk

        :param page_size: The param of the ShowCertificatesHttpsInfoRequest
        :type page_size: int
        :param page_number: The param of the ShowCertificatesHttpsInfoRequest
        :type page_number: int
        :param domain_name: The param of the ShowCertificatesHttpsInfoRequest
        :type domain_name: str
        :param user_domain_id: The param of the ShowCertificatesHttpsInfoRequest
        :type user_domain_id: str
        :param enterprise_project_id: The param of the ShowCertificatesHttpsInfoRequest
        :type enterprise_project_id: str
        """
        
        

        self._page_size = None
        self._page_number = None
        self._domain_name = None
        self._user_domain_id = None
        self._enterprise_project_id = None
        self.discriminator = None

        if page_size is not None:
            self.page_size = page_size
        if page_number is not None:
            self.page_number = page_number
        if domain_name is not None:
            self.domain_name = domain_name
        if user_domain_id is not None:
            self.user_domain_id = user_domain_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def page_size(self):
        """Gets the page_size of this ShowCertificatesHttpsInfoRequest.

        :return: The page_size of this ShowCertificatesHttpsInfoRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ShowCertificatesHttpsInfoRequest.

        :param page_size: The page_size of this ShowCertificatesHttpsInfoRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def page_number(self):
        """Gets the page_number of this ShowCertificatesHttpsInfoRequest.

        :return: The page_number of this ShowCertificatesHttpsInfoRequest.
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this ShowCertificatesHttpsInfoRequest.

        :param page_number: The page_number of this ShowCertificatesHttpsInfoRequest.
        :type page_number: int
        """
        self._page_number = page_number

    @property
    def domain_name(self):
        """Gets the domain_name of this ShowCertificatesHttpsInfoRequest.

        :return: The domain_name of this ShowCertificatesHttpsInfoRequest.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this ShowCertificatesHttpsInfoRequest.

        :param domain_name: The domain_name of this ShowCertificatesHttpsInfoRequest.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def user_domain_id(self):
        """Gets the user_domain_id of this ShowCertificatesHttpsInfoRequest.

        :return: The user_domain_id of this ShowCertificatesHttpsInfoRequest.
        :rtype: str
        """
        return self._user_domain_id

    @user_domain_id.setter
    def user_domain_id(self, user_domain_id):
        """Sets the user_domain_id of this ShowCertificatesHttpsInfoRequest.

        :param user_domain_id: The user_domain_id of this ShowCertificatesHttpsInfoRequest.
        :type user_domain_id: str
        """
        self._user_domain_id = user_domain_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ShowCertificatesHttpsInfoRequest.

        :return: The enterprise_project_id of this ShowCertificatesHttpsInfoRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ShowCertificatesHttpsInfoRequest.

        :param enterprise_project_id: The enterprise_project_id of this ShowCertificatesHttpsInfoRequest.
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
        if not isinstance(other, ShowCertificatesHttpsInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
