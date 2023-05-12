# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPoolsRequest:

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
        'description': 'list[str]',
        'admin_state_up': 'bool',
        'healthmonitor_id': 'list[str]',
        'id': 'list[str]',
        'name': 'list[str]',
        'loadbalancer_id': 'list[str]',
        'protocol': 'list[str]',
        'lb_algorithm': 'list[str]',
        'enterprise_project_id': 'list[str]',
        'ip_version': 'list[str]',
        'member_address': 'list[str]',
        'member_device_id': 'list[str]',
        'member_deletion_protection_enable': 'bool',
        'listener_id': 'list[str]',
        'member_instance_id': 'list[str]',
        'vpc_id': 'list[str]',
        'type': 'list[str]'
    }

    attribute_map = {
        'marker': 'marker',
        'limit': 'limit',
        'page_reverse': 'page_reverse',
        'description': 'description',
        'admin_state_up': 'admin_state_up',
        'healthmonitor_id': 'healthmonitor_id',
        'id': 'id',
        'name': 'name',
        'loadbalancer_id': 'loadbalancer_id',
        'protocol': 'protocol',
        'lb_algorithm': 'lb_algorithm',
        'enterprise_project_id': 'enterprise_project_id',
        'ip_version': 'ip_version',
        'member_address': 'member_address',
        'member_device_id': 'member_device_id',
        'member_deletion_protection_enable': 'member_deletion_protection_enable',
        'listener_id': 'listener_id',
        'member_instance_id': 'member_instance_id',
        'vpc_id': 'vpc_id',
        'type': 'type'
    }

    def __init__(self, marker=None, limit=None, page_reverse=None, description=None, admin_state_up=None, healthmonitor_id=None, id=None, name=None, loadbalancer_id=None, protocol=None, lb_algorithm=None, enterprise_project_id=None, ip_version=None, member_address=None, member_device_id=None, member_deletion_protection_enable=None, listener_id=None, member_instance_id=None, vpc_id=None, type=None):
        """ListPoolsRequest

        The model defined in g42cloud sdk

        :param marker: The param of the ListPoolsRequest
        :type marker: str
        :param limit: The param of the ListPoolsRequest
        :type limit: int
        :param page_reverse: The param of the ListPoolsRequest
        :type page_reverse: bool
        :param description: The param of the ListPoolsRequest
        :type description: list[str]
        :param admin_state_up: The param of the ListPoolsRequest
        :type admin_state_up: bool
        :param healthmonitor_id: The param of the ListPoolsRequest
        :type healthmonitor_id: list[str]
        :param id: The param of the ListPoolsRequest
        :type id: list[str]
        :param name: The param of the ListPoolsRequest
        :type name: list[str]
        :param loadbalancer_id: The param of the ListPoolsRequest
        :type loadbalancer_id: list[str]
        :param protocol: The param of the ListPoolsRequest
        :type protocol: list[str]
        :param lb_algorithm: The param of the ListPoolsRequest
        :type lb_algorithm: list[str]
        :param enterprise_project_id: The param of the ListPoolsRequest
        :type enterprise_project_id: list[str]
        :param ip_version: The param of the ListPoolsRequest
        :type ip_version: list[str]
        :param member_address: The param of the ListPoolsRequest
        :type member_address: list[str]
        :param member_device_id: The param of the ListPoolsRequest
        :type member_device_id: list[str]
        :param member_deletion_protection_enable: The param of the ListPoolsRequest
        :type member_deletion_protection_enable: bool
        :param listener_id: The param of the ListPoolsRequest
        :type listener_id: list[str]
        :param member_instance_id: The param of the ListPoolsRequest
        :type member_instance_id: list[str]
        :param vpc_id: The param of the ListPoolsRequest
        :type vpc_id: list[str]
        :param type: The param of the ListPoolsRequest
        :type type: list[str]
        """
        
        

        self._marker = None
        self._limit = None
        self._page_reverse = None
        self._description = None
        self._admin_state_up = None
        self._healthmonitor_id = None
        self._id = None
        self._name = None
        self._loadbalancer_id = None
        self._protocol = None
        self._lb_algorithm = None
        self._enterprise_project_id = None
        self._ip_version = None
        self._member_address = None
        self._member_device_id = None
        self._member_deletion_protection_enable = None
        self._listener_id = None
        self._member_instance_id = None
        self._vpc_id = None
        self._type = None
        self.discriminator = None

        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if description is not None:
            self.description = description
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if healthmonitor_id is not None:
            self.healthmonitor_id = healthmonitor_id
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if loadbalancer_id is not None:
            self.loadbalancer_id = loadbalancer_id
        if protocol is not None:
            self.protocol = protocol
        if lb_algorithm is not None:
            self.lb_algorithm = lb_algorithm
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if ip_version is not None:
            self.ip_version = ip_version
        if member_address is not None:
            self.member_address = member_address
        if member_device_id is not None:
            self.member_device_id = member_device_id
        if member_deletion_protection_enable is not None:
            self.member_deletion_protection_enable = member_deletion_protection_enable
        if listener_id is not None:
            self.listener_id = listener_id
        if member_instance_id is not None:
            self.member_instance_id = member_instance_id
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if type is not None:
            self.type = type

    @property
    def marker(self):
        """Gets the marker of this ListPoolsRequest.

        :return: The marker of this ListPoolsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListPoolsRequest.

        :param marker: The marker of this ListPoolsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        """Gets the limit of this ListPoolsRequest.

        :return: The limit of this ListPoolsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPoolsRequest.

        :param limit: The limit of this ListPoolsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def page_reverse(self):
        """Gets the page_reverse of this ListPoolsRequest.

        :return: The page_reverse of this ListPoolsRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        """Sets the page_reverse of this ListPoolsRequest.

        :param page_reverse: The page_reverse of this ListPoolsRequest.
        :type page_reverse: bool
        """
        self._page_reverse = page_reverse

    @property
    def description(self):
        """Gets the description of this ListPoolsRequest.

        :return: The description of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListPoolsRequest.

        :param description: The description of this ListPoolsRequest.
        :type description: list[str]
        """
        self._description = description

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this ListPoolsRequest.

        :return: The admin_state_up of this ListPoolsRequest.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this ListPoolsRequest.

        :param admin_state_up: The admin_state_up of this ListPoolsRequest.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def healthmonitor_id(self):
        """Gets the healthmonitor_id of this ListPoolsRequest.

        :return: The healthmonitor_id of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._healthmonitor_id

    @healthmonitor_id.setter
    def healthmonitor_id(self, healthmonitor_id):
        """Sets the healthmonitor_id of this ListPoolsRequest.

        :param healthmonitor_id: The healthmonitor_id of this ListPoolsRequest.
        :type healthmonitor_id: list[str]
        """
        self._healthmonitor_id = healthmonitor_id

    @property
    def id(self):
        """Gets the id of this ListPoolsRequest.

        :return: The id of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListPoolsRequest.

        :param id: The id of this ListPoolsRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListPoolsRequest.

        :return: The name of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListPoolsRequest.

        :param name: The name of this ListPoolsRequest.
        :type name: list[str]
        """
        self._name = name

    @property
    def loadbalancer_id(self):
        """Gets the loadbalancer_id of this ListPoolsRequest.

        :return: The loadbalancer_id of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._loadbalancer_id

    @loadbalancer_id.setter
    def loadbalancer_id(self, loadbalancer_id):
        """Sets the loadbalancer_id of this ListPoolsRequest.

        :param loadbalancer_id: The loadbalancer_id of this ListPoolsRequest.
        :type loadbalancer_id: list[str]
        """
        self._loadbalancer_id = loadbalancer_id

    @property
    def protocol(self):
        """Gets the protocol of this ListPoolsRequest.

        :return: The protocol of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ListPoolsRequest.

        :param protocol: The protocol of this ListPoolsRequest.
        :type protocol: list[str]
        """
        self._protocol = protocol

    @property
    def lb_algorithm(self):
        """Gets the lb_algorithm of this ListPoolsRequest.

        :return: The lb_algorithm of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._lb_algorithm

    @lb_algorithm.setter
    def lb_algorithm(self, lb_algorithm):
        """Sets the lb_algorithm of this ListPoolsRequest.

        :param lb_algorithm: The lb_algorithm of this ListPoolsRequest.
        :type lb_algorithm: list[str]
        """
        self._lb_algorithm = lb_algorithm

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListPoolsRequest.

        :return: The enterprise_project_id of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListPoolsRequest.

        :param enterprise_project_id: The enterprise_project_id of this ListPoolsRequest.
        :type enterprise_project_id: list[str]
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def ip_version(self):
        """Gets the ip_version of this ListPoolsRequest.

        :return: The ip_version of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this ListPoolsRequest.

        :param ip_version: The ip_version of this ListPoolsRequest.
        :type ip_version: list[str]
        """
        self._ip_version = ip_version

    @property
    def member_address(self):
        """Gets the member_address of this ListPoolsRequest.

        :return: The member_address of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._member_address

    @member_address.setter
    def member_address(self, member_address):
        """Sets the member_address of this ListPoolsRequest.

        :param member_address: The member_address of this ListPoolsRequest.
        :type member_address: list[str]
        """
        self._member_address = member_address

    @property
    def member_device_id(self):
        """Gets the member_device_id of this ListPoolsRequest.

        :return: The member_device_id of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._member_device_id

    @member_device_id.setter
    def member_device_id(self, member_device_id):
        """Sets the member_device_id of this ListPoolsRequest.

        :param member_device_id: The member_device_id of this ListPoolsRequest.
        :type member_device_id: list[str]
        """
        self._member_device_id = member_device_id

    @property
    def member_deletion_protection_enable(self):
        """Gets the member_deletion_protection_enable of this ListPoolsRequest.

        :return: The member_deletion_protection_enable of this ListPoolsRequest.
        :rtype: bool
        """
        return self._member_deletion_protection_enable

    @member_deletion_protection_enable.setter
    def member_deletion_protection_enable(self, member_deletion_protection_enable):
        """Sets the member_deletion_protection_enable of this ListPoolsRequest.

        :param member_deletion_protection_enable: The member_deletion_protection_enable of this ListPoolsRequest.
        :type member_deletion_protection_enable: bool
        """
        self._member_deletion_protection_enable = member_deletion_protection_enable

    @property
    def listener_id(self):
        """Gets the listener_id of this ListPoolsRequest.

        :return: The listener_id of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._listener_id

    @listener_id.setter
    def listener_id(self, listener_id):
        """Sets the listener_id of this ListPoolsRequest.

        :param listener_id: The listener_id of this ListPoolsRequest.
        :type listener_id: list[str]
        """
        self._listener_id = listener_id

    @property
    def member_instance_id(self):
        """Gets the member_instance_id of this ListPoolsRequest.

        :return: The member_instance_id of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._member_instance_id

    @member_instance_id.setter
    def member_instance_id(self, member_instance_id):
        """Sets the member_instance_id of this ListPoolsRequest.

        :param member_instance_id: The member_instance_id of this ListPoolsRequest.
        :type member_instance_id: list[str]
        """
        self._member_instance_id = member_instance_id

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ListPoolsRequest.

        :return: The vpc_id of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ListPoolsRequest.

        :param vpc_id: The vpc_id of this ListPoolsRequest.
        :type vpc_id: list[str]
        """
        self._vpc_id = vpc_id

    @property
    def type(self):
        """Gets the type of this ListPoolsRequest.

        :return: The type of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListPoolsRequest.

        :param type: The type of this ListPoolsRequest.
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
        if not isinstance(other, ListPoolsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
