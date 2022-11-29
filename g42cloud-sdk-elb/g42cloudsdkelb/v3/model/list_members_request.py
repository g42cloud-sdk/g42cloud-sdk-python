# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMembersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pool_id': 'str',
        'marker': 'str',
        'limit': 'int',
        'page_reverse': 'bool',
        'name': 'list[str]',
        'weight': 'list[int]',
        'admin_state_up': 'bool',
        'subnet_cidr_id': 'list[str]',
        'address': 'list[str]',
        'protocol_port': 'list[int]',
        'id': 'list[str]',
        'operating_status': 'list[str]',
        'enterprise_project_id': 'list[str]',
        'ip_version': 'list[str]',
        'member_type': 'list[str]',
        'instance_id': 'list[str]'
    }

    attribute_map = {
        'pool_id': 'pool_id',
        'marker': 'marker',
        'limit': 'limit',
        'page_reverse': 'page_reverse',
        'name': 'name',
        'weight': 'weight',
        'admin_state_up': 'admin_state_up',
        'subnet_cidr_id': 'subnet_cidr_id',
        'address': 'address',
        'protocol_port': 'protocol_port',
        'id': 'id',
        'operating_status': 'operating_status',
        'enterprise_project_id': 'enterprise_project_id',
        'ip_version': 'ip_version',
        'member_type': 'member_type',
        'instance_id': 'instance_id'
    }

    def __init__(self, pool_id=None, marker=None, limit=None, page_reverse=None, name=None, weight=None, admin_state_up=None, subnet_cidr_id=None, address=None, protocol_port=None, id=None, operating_status=None, enterprise_project_id=None, ip_version=None, member_type=None, instance_id=None):
        """ListMembersRequest

        The model defined in g42cloud sdk

        :param pool_id: The param of the ListMembersRequest
        :type pool_id: str
        :param marker: The param of the ListMembersRequest
        :type marker: str
        :param limit: The param of the ListMembersRequest
        :type limit: int
        :param page_reverse: The param of the ListMembersRequest
        :type page_reverse: bool
        :param name: The param of the ListMembersRequest
        :type name: list[str]
        :param weight: The param of the ListMembersRequest
        :type weight: list[int]
        :param admin_state_up: The param of the ListMembersRequest
        :type admin_state_up: bool
        :param subnet_cidr_id: The param of the ListMembersRequest
        :type subnet_cidr_id: list[str]
        :param address: The param of the ListMembersRequest
        :type address: list[str]
        :param protocol_port: The param of the ListMembersRequest
        :type protocol_port: list[int]
        :param id: The param of the ListMembersRequest
        :type id: list[str]
        :param operating_status: The param of the ListMembersRequest
        :type operating_status: list[str]
        :param enterprise_project_id: The param of the ListMembersRequest
        :type enterprise_project_id: list[str]
        :param ip_version: The param of the ListMembersRequest
        :type ip_version: list[str]
        :param member_type: The param of the ListMembersRequest
        :type member_type: list[str]
        :param instance_id: The param of the ListMembersRequest
        :type instance_id: list[str]
        """
        
        

        self._pool_id = None
        self._marker = None
        self._limit = None
        self._page_reverse = None
        self._name = None
        self._weight = None
        self._admin_state_up = None
        self._subnet_cidr_id = None
        self._address = None
        self._protocol_port = None
        self._id = None
        self._operating_status = None
        self._enterprise_project_id = None
        self._ip_version = None
        self._member_type = None
        self._instance_id = None
        self.discriminator = None

        self.pool_id = pool_id
        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if name is not None:
            self.name = name
        if weight is not None:
            self.weight = weight
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if subnet_cidr_id is not None:
            self.subnet_cidr_id = subnet_cidr_id
        if address is not None:
            self.address = address
        if protocol_port is not None:
            self.protocol_port = protocol_port
        if id is not None:
            self.id = id
        if operating_status is not None:
            self.operating_status = operating_status
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if ip_version is not None:
            self.ip_version = ip_version
        if member_type is not None:
            self.member_type = member_type
        if instance_id is not None:
            self.instance_id = instance_id

    @property
    def pool_id(self):
        """Gets the pool_id of this ListMembersRequest.

        :return: The pool_id of this ListMembersRequest.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        """Sets the pool_id of this ListMembersRequest.

        :param pool_id: The pool_id of this ListMembersRequest.
        :type pool_id: str
        """
        self._pool_id = pool_id

    @property
    def marker(self):
        """Gets the marker of this ListMembersRequest.

        :return: The marker of this ListMembersRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListMembersRequest.

        :param marker: The marker of this ListMembersRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        """Gets the limit of this ListMembersRequest.

        :return: The limit of this ListMembersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListMembersRequest.

        :param limit: The limit of this ListMembersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def page_reverse(self):
        """Gets the page_reverse of this ListMembersRequest.

        :return: The page_reverse of this ListMembersRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        """Sets the page_reverse of this ListMembersRequest.

        :param page_reverse: The page_reverse of this ListMembersRequest.
        :type page_reverse: bool
        """
        self._page_reverse = page_reverse

    @property
    def name(self):
        """Gets the name of this ListMembersRequest.

        :return: The name of this ListMembersRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListMembersRequest.

        :param name: The name of this ListMembersRequest.
        :type name: list[str]
        """
        self._name = name

    @property
    def weight(self):
        """Gets the weight of this ListMembersRequest.

        :return: The weight of this ListMembersRequest.
        :rtype: list[int]
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this ListMembersRequest.

        :param weight: The weight of this ListMembersRequest.
        :type weight: list[int]
        """
        self._weight = weight

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this ListMembersRequest.

        :return: The admin_state_up of this ListMembersRequest.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this ListMembersRequest.

        :param admin_state_up: The admin_state_up of this ListMembersRequest.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def subnet_cidr_id(self):
        """Gets the subnet_cidr_id of this ListMembersRequest.

        :return: The subnet_cidr_id of this ListMembersRequest.
        :rtype: list[str]
        """
        return self._subnet_cidr_id

    @subnet_cidr_id.setter
    def subnet_cidr_id(self, subnet_cidr_id):
        """Sets the subnet_cidr_id of this ListMembersRequest.

        :param subnet_cidr_id: The subnet_cidr_id of this ListMembersRequest.
        :type subnet_cidr_id: list[str]
        """
        self._subnet_cidr_id = subnet_cidr_id

    @property
    def address(self):
        """Gets the address of this ListMembersRequest.

        :return: The address of this ListMembersRequest.
        :rtype: list[str]
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ListMembersRequest.

        :param address: The address of this ListMembersRequest.
        :type address: list[str]
        """
        self._address = address

    @property
    def protocol_port(self):
        """Gets the protocol_port of this ListMembersRequest.

        :return: The protocol_port of this ListMembersRequest.
        :rtype: list[int]
        """
        return self._protocol_port

    @protocol_port.setter
    def protocol_port(self, protocol_port):
        """Sets the protocol_port of this ListMembersRequest.

        :param protocol_port: The protocol_port of this ListMembersRequest.
        :type protocol_port: list[int]
        """
        self._protocol_port = protocol_port

    @property
    def id(self):
        """Gets the id of this ListMembersRequest.

        :return: The id of this ListMembersRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListMembersRequest.

        :param id: The id of this ListMembersRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def operating_status(self):
        """Gets the operating_status of this ListMembersRequest.

        :return: The operating_status of this ListMembersRequest.
        :rtype: list[str]
        """
        return self._operating_status

    @operating_status.setter
    def operating_status(self, operating_status):
        """Sets the operating_status of this ListMembersRequest.

        :param operating_status: The operating_status of this ListMembersRequest.
        :type operating_status: list[str]
        """
        self._operating_status = operating_status

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListMembersRequest.

        :return: The enterprise_project_id of this ListMembersRequest.
        :rtype: list[str]
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListMembersRequest.

        :param enterprise_project_id: The enterprise_project_id of this ListMembersRequest.
        :type enterprise_project_id: list[str]
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def ip_version(self):
        """Gets the ip_version of this ListMembersRequest.

        :return: The ip_version of this ListMembersRequest.
        :rtype: list[str]
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this ListMembersRequest.

        :param ip_version: The ip_version of this ListMembersRequest.
        :type ip_version: list[str]
        """
        self._ip_version = ip_version

    @property
    def member_type(self):
        """Gets the member_type of this ListMembersRequest.

        :return: The member_type of this ListMembersRequest.
        :rtype: list[str]
        """
        return self._member_type

    @member_type.setter
    def member_type(self, member_type):
        """Sets the member_type of this ListMembersRequest.

        :param member_type: The member_type of this ListMembersRequest.
        :type member_type: list[str]
        """
        self._member_type = member_type

    @property
    def instance_id(self):
        """Gets the instance_id of this ListMembersRequest.

        :return: The instance_id of this ListMembersRequest.
        :rtype: list[str]
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListMembersRequest.

        :param instance_id: The instance_id of this ListMembersRequest.
        :type instance_id: list[str]
        """
        self._instance_id = instance_id

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
        if not isinstance(other, ListMembersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
