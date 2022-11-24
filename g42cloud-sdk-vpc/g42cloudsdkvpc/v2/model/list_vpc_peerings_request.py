# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVpcPeeringsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'marker': 'str',
        'id': 'str',
        'name': 'str',
        'status': 'str',
        'tenant_id': 'str',
        'vpc_id': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'tenant_id': 'tenant_id',
        'vpc_id': 'vpc_id'
    }

    def __init__(self, limit=None, marker=None, id=None, name=None, status=None, tenant_id=None, vpc_id=None):
        """ListVpcPeeringsRequest

        The model defined in g42cloud sdk

        :param limit: The param of the ListVpcPeeringsRequest
        :type limit: int
        :param marker: The param of the ListVpcPeeringsRequest
        :type marker: str
        :param id: The param of the ListVpcPeeringsRequest
        :type id: str
        :param name: The param of the ListVpcPeeringsRequest
        :type name: str
        :param status: The param of the ListVpcPeeringsRequest
        :type status: str
        :param tenant_id: The param of the ListVpcPeeringsRequest
        :type tenant_id: str
        :param vpc_id: The param of the ListVpcPeeringsRequest
        :type vpc_id: str
        """
        
        

        self._limit = None
        self._marker = None
        self._id = None
        self._name = None
        self._status = None
        self._tenant_id = None
        self._vpc_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if vpc_id is not None:
            self.vpc_id = vpc_id

    @property
    def limit(self):
        """Gets the limit of this ListVpcPeeringsRequest.

        :return: The limit of this ListVpcPeeringsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListVpcPeeringsRequest.

        :param limit: The limit of this ListVpcPeeringsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListVpcPeeringsRequest.

        :return: The marker of this ListVpcPeeringsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListVpcPeeringsRequest.

        :param marker: The marker of this ListVpcPeeringsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def id(self):
        """Gets the id of this ListVpcPeeringsRequest.

        :return: The id of this ListVpcPeeringsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListVpcPeeringsRequest.

        :param id: The id of this ListVpcPeeringsRequest.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListVpcPeeringsRequest.

        :return: The name of this ListVpcPeeringsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListVpcPeeringsRequest.

        :param name: The name of this ListVpcPeeringsRequest.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this ListVpcPeeringsRequest.

        :return: The status of this ListVpcPeeringsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListVpcPeeringsRequest.

        :param status: The status of this ListVpcPeeringsRequest.
        :type status: str
        """
        self._status = status

    @property
    def tenant_id(self):
        """Gets the tenant_id of this ListVpcPeeringsRequest.

        :return: The tenant_id of this ListVpcPeeringsRequest.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this ListVpcPeeringsRequest.

        :param tenant_id: The tenant_id of this ListVpcPeeringsRequest.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ListVpcPeeringsRequest.

        :return: The vpc_id of this ListVpcPeeringsRequest.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ListVpcPeeringsRequest.

        :param vpc_id: The vpc_id of this ListVpcPeeringsRequest.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

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
        if not isinstance(other, ListVpcPeeringsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
