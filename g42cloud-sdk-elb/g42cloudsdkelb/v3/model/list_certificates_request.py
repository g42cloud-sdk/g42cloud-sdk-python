# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCertificatesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'marker': 'str',
        'limit': 'int',
        'page_reverse': 'bool',
        'id': 'list[str]',
        'name': 'list[str]',
        'description': 'list[str]',
        'admin_state_up': 'bool',
        'domain': 'list[str]',
        'type': 'list[str]'
    }

    attribute_map = {
        'marker': 'marker',
        'limit': 'limit',
        'page_reverse': 'page_reverse',
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'admin_state_up': 'admin_state_up',
        'domain': 'domain',
        'type': 'type'
    }

    def __init__(self, marker=None, limit=None, page_reverse=None, id=None, name=None, description=None, admin_state_up=None, domain=None, type=None):
        """ListCertificatesRequest

        The model defined in g42cloud sdk

        :param marker: The param of the ListCertificatesRequest
        :type marker: str
        :param limit: The param of the ListCertificatesRequest
        :type limit: int
        :param page_reverse: The param of the ListCertificatesRequest
        :type page_reverse: bool
        :param id: The param of the ListCertificatesRequest
        :type id: list[str]
        :param name: The param of the ListCertificatesRequest
        :type name: list[str]
        :param description: The param of the ListCertificatesRequest
        :type description: list[str]
        :param admin_state_up: The param of the ListCertificatesRequest
        :type admin_state_up: bool
        :param domain: The param of the ListCertificatesRequest
        :type domain: list[str]
        :param type: The param of the ListCertificatesRequest
        :type type: list[str]
        """
        
        

        self._marker = None
        self._limit = None
        self._page_reverse = None
        self._id = None
        self._name = None
        self._description = None
        self._admin_state_up = None
        self._domain = None
        self._type = None
        self.discriminator = None

        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if domain is not None:
            self.domain = domain
        if type is not None:
            self.type = type

    @property
    def marker(self):
        """Gets the marker of this ListCertificatesRequest.

        :return: The marker of this ListCertificatesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListCertificatesRequest.

        :param marker: The marker of this ListCertificatesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        """Gets the limit of this ListCertificatesRequest.

        :return: The limit of this ListCertificatesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListCertificatesRequest.

        :param limit: The limit of this ListCertificatesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def page_reverse(self):
        """Gets the page_reverse of this ListCertificatesRequest.

        :return: The page_reverse of this ListCertificatesRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        """Sets the page_reverse of this ListCertificatesRequest.

        :param page_reverse: The page_reverse of this ListCertificatesRequest.
        :type page_reverse: bool
        """
        self._page_reverse = page_reverse

    @property
    def id(self):
        """Gets the id of this ListCertificatesRequest.

        :return: The id of this ListCertificatesRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListCertificatesRequest.

        :param id: The id of this ListCertificatesRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListCertificatesRequest.

        :return: The name of this ListCertificatesRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListCertificatesRequest.

        :param name: The name of this ListCertificatesRequest.
        :type name: list[str]
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ListCertificatesRequest.

        :return: The description of this ListCertificatesRequest.
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListCertificatesRequest.

        :param description: The description of this ListCertificatesRequest.
        :type description: list[str]
        """
        self._description = description

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this ListCertificatesRequest.

        :return: The admin_state_up of this ListCertificatesRequest.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this ListCertificatesRequest.

        :param admin_state_up: The admin_state_up of this ListCertificatesRequest.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def domain(self):
        """Gets the domain of this ListCertificatesRequest.

        :return: The domain of this ListCertificatesRequest.
        :rtype: list[str]
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this ListCertificatesRequest.

        :param domain: The domain of this ListCertificatesRequest.
        :type domain: list[str]
        """
        self._domain = domain

    @property
    def type(self):
        """Gets the type of this ListCertificatesRequest.

        :return: The type of this ListCertificatesRequest.
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListCertificatesRequest.

        :param type: The type of this ListCertificatesRequest.
        :type type: list[str]
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
        if not isinstance(other, ListCertificatesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
