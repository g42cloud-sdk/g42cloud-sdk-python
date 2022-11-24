# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DomainBody:

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
        'sources': 'list[Sources]',
        'service_area': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'domain_name': 'domain_name',
        'business_type': 'business_type',
        'sources': 'sources',
        'service_area': 'service_area',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, domain_name=None, business_type=None, sources=None, service_area=None, enterprise_project_id=None):
        """DomainBody

        The model defined in g42cloud sdk

        :param domain_name: The param of the DomainBody
        :type domain_name: str
        :param business_type: The param of the DomainBody
        :type business_type: str
        :param sources: The param of the DomainBody
        :type sources: list[:class:`g42cloudsdkcdn.v1.Sources`]
        :param service_area: The param of the DomainBody
        :type service_area: str
        :param enterprise_project_id: The param of the DomainBody
        :type enterprise_project_id: str
        """
        
        

        self._domain_name = None
        self._business_type = None
        self._sources = None
        self._service_area = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.domain_name = domain_name
        self.business_type = business_type
        self.sources = sources
        self.service_area = service_area
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def domain_name(self):
        """Gets the domain_name of this DomainBody.

        :return: The domain_name of this DomainBody.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this DomainBody.

        :param domain_name: The domain_name of this DomainBody.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def business_type(self):
        """Gets the business_type of this DomainBody.

        :return: The business_type of this DomainBody.
        :rtype: str
        """
        return self._business_type

    @business_type.setter
    def business_type(self, business_type):
        """Sets the business_type of this DomainBody.

        :param business_type: The business_type of this DomainBody.
        :type business_type: str
        """
        self._business_type = business_type

    @property
    def sources(self):
        """Gets the sources of this DomainBody.

        :return: The sources of this DomainBody.
        :rtype: list[:class:`g42cloudsdkcdn.v1.Sources`]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this DomainBody.

        :param sources: The sources of this DomainBody.
        :type sources: list[:class:`g42cloudsdkcdn.v1.Sources`]
        """
        self._sources = sources

    @property
    def service_area(self):
        """Gets the service_area of this DomainBody.

        :return: The service_area of this DomainBody.
        :rtype: str
        """
        return self._service_area

    @service_area.setter
    def service_area(self, service_area):
        """Sets the service_area of this DomainBody.

        :param service_area: The service_area of this DomainBody.
        :type service_area: str
        """
        self._service_area = service_area

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this DomainBody.

        :return: The enterprise_project_id of this DomainBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this DomainBody.

        :param enterprise_project_id: The enterprise_project_id of this DomainBody.
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
        if not isinstance(other, DomainBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
