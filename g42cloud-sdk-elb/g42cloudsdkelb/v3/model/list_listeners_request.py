# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListListenersRequest:

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
        'page_reverse': 'bool',
        'protocol_port': 'list[str]',
        'protocol': 'list[str]',
        'description': 'list[str]',
        'default_tls_container_ref': 'list[str]',
        'client_ca_tls_container_ref': 'list[str]',
        'admin_state_up': 'bool',
        'connection_limit': 'list[int]',
        'default_pool_id': 'list[str]',
        'id': 'list[str]',
        'name': 'list[str]',
        'http2_enable': 'bool',
        'loadbalancer_id': 'list[str]',
        'tls_ciphers_policy': 'list[str]',
        'member_address': 'list[str]',
        'member_device_id': 'list[str]',
        'enterprise_project_id': 'list[str]',
        'enable_member_retry': 'bool',
        'member_timeout': 'list[int]',
        'client_timeout': 'list[int]',
        'keepalive_timeout': 'list[int]',
        'transparent_client_ip_enable': 'bool',
        'enhance_l7policy_enable': 'bool',
        'member_instance_id': 'list[str]'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'page_reverse': 'page_reverse',
        'protocol_port': 'protocol_port',
        'protocol': 'protocol',
        'description': 'description',
        'default_tls_container_ref': 'default_tls_container_ref',
        'client_ca_tls_container_ref': 'client_ca_tls_container_ref',
        'admin_state_up': 'admin_state_up',
        'connection_limit': 'connection_limit',
        'default_pool_id': 'default_pool_id',
        'id': 'id',
        'name': 'name',
        'http2_enable': 'http2_enable',
        'loadbalancer_id': 'loadbalancer_id',
        'tls_ciphers_policy': 'tls_ciphers_policy',
        'member_address': 'member_address',
        'member_device_id': 'member_device_id',
        'enterprise_project_id': 'enterprise_project_id',
        'enable_member_retry': 'enable_member_retry',
        'member_timeout': 'member_timeout',
        'client_timeout': 'client_timeout',
        'keepalive_timeout': 'keepalive_timeout',
        'transparent_client_ip_enable': 'transparent_client_ip_enable',
        'enhance_l7policy_enable': 'enhance_l7policy_enable',
        'member_instance_id': 'member_instance_id'
    }

    def __init__(self, limit=None, marker=None, page_reverse=None, protocol_port=None, protocol=None, description=None, default_tls_container_ref=None, client_ca_tls_container_ref=None, admin_state_up=None, connection_limit=None, default_pool_id=None, id=None, name=None, http2_enable=None, loadbalancer_id=None, tls_ciphers_policy=None, member_address=None, member_device_id=None, enterprise_project_id=None, enable_member_retry=None, member_timeout=None, client_timeout=None, keepalive_timeout=None, transparent_client_ip_enable=None, enhance_l7policy_enable=None, member_instance_id=None):
        """ListListenersRequest

        The model defined in g42cloud sdk

        :param limit: The param of the ListListenersRequest
        :type limit: int
        :param marker: The param of the ListListenersRequest
        :type marker: str
        :param page_reverse: The param of the ListListenersRequest
        :type page_reverse: bool
        :param protocol_port: The param of the ListListenersRequest
        :type protocol_port: list[str]
        :param protocol: The param of the ListListenersRequest
        :type protocol: list[str]
        :param description: The param of the ListListenersRequest
        :type description: list[str]
        :param default_tls_container_ref: The param of the ListListenersRequest
        :type default_tls_container_ref: list[str]
        :param client_ca_tls_container_ref: The param of the ListListenersRequest
        :type client_ca_tls_container_ref: list[str]
        :param admin_state_up: The param of the ListListenersRequest
        :type admin_state_up: bool
        :param connection_limit: The param of the ListListenersRequest
        :type connection_limit: list[int]
        :param default_pool_id: The param of the ListListenersRequest
        :type default_pool_id: list[str]
        :param id: The param of the ListListenersRequest
        :type id: list[str]
        :param name: The param of the ListListenersRequest
        :type name: list[str]
        :param http2_enable: The param of the ListListenersRequest
        :type http2_enable: bool
        :param loadbalancer_id: The param of the ListListenersRequest
        :type loadbalancer_id: list[str]
        :param tls_ciphers_policy: The param of the ListListenersRequest
        :type tls_ciphers_policy: list[str]
        :param member_address: The param of the ListListenersRequest
        :type member_address: list[str]
        :param member_device_id: The param of the ListListenersRequest
        :type member_device_id: list[str]
        :param enterprise_project_id: The param of the ListListenersRequest
        :type enterprise_project_id: list[str]
        :param enable_member_retry: The param of the ListListenersRequest
        :type enable_member_retry: bool
        :param member_timeout: The param of the ListListenersRequest
        :type member_timeout: list[int]
        :param client_timeout: The param of the ListListenersRequest
        :type client_timeout: list[int]
        :param keepalive_timeout: The param of the ListListenersRequest
        :type keepalive_timeout: list[int]
        :param transparent_client_ip_enable: The param of the ListListenersRequest
        :type transparent_client_ip_enable: bool
        :param enhance_l7policy_enable: The param of the ListListenersRequest
        :type enhance_l7policy_enable: bool
        :param member_instance_id: The param of the ListListenersRequest
        :type member_instance_id: list[str]
        """
        
        

        self._limit = None
        self._marker = None
        self._page_reverse = None
        self._protocol_port = None
        self._protocol = None
        self._description = None
        self._default_tls_container_ref = None
        self._client_ca_tls_container_ref = None
        self._admin_state_up = None
        self._connection_limit = None
        self._default_pool_id = None
        self._id = None
        self._name = None
        self._http2_enable = None
        self._loadbalancer_id = None
        self._tls_ciphers_policy = None
        self._member_address = None
        self._member_device_id = None
        self._enterprise_project_id = None
        self._enable_member_retry = None
        self._member_timeout = None
        self._client_timeout = None
        self._keepalive_timeout = None
        self._transparent_client_ip_enable = None
        self._enhance_l7policy_enable = None
        self._member_instance_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if protocol_port is not None:
            self.protocol_port = protocol_port
        if protocol is not None:
            self.protocol = protocol
        if description is not None:
            self.description = description
        if default_tls_container_ref is not None:
            self.default_tls_container_ref = default_tls_container_ref
        if client_ca_tls_container_ref is not None:
            self.client_ca_tls_container_ref = client_ca_tls_container_ref
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if connection_limit is not None:
            self.connection_limit = connection_limit
        if default_pool_id is not None:
            self.default_pool_id = default_pool_id
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if http2_enable is not None:
            self.http2_enable = http2_enable
        if loadbalancer_id is not None:
            self.loadbalancer_id = loadbalancer_id
        if tls_ciphers_policy is not None:
            self.tls_ciphers_policy = tls_ciphers_policy
        if member_address is not None:
            self.member_address = member_address
        if member_device_id is not None:
            self.member_device_id = member_device_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if enable_member_retry is not None:
            self.enable_member_retry = enable_member_retry
        if member_timeout is not None:
            self.member_timeout = member_timeout
        if client_timeout is not None:
            self.client_timeout = client_timeout
        if keepalive_timeout is not None:
            self.keepalive_timeout = keepalive_timeout
        if transparent_client_ip_enable is not None:
            self.transparent_client_ip_enable = transparent_client_ip_enable
        if enhance_l7policy_enable is not None:
            self.enhance_l7policy_enable = enhance_l7policy_enable
        if member_instance_id is not None:
            self.member_instance_id = member_instance_id

    @property
    def limit(self):
        """Gets the limit of this ListListenersRequest.

        :return: The limit of this ListListenersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListListenersRequest.

        :param limit: The limit of this ListListenersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListListenersRequest.

        :return: The marker of this ListListenersRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListListenersRequest.

        :param marker: The marker of this ListListenersRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def page_reverse(self):
        """Gets the page_reverse of this ListListenersRequest.

        :return: The page_reverse of this ListListenersRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        """Sets the page_reverse of this ListListenersRequest.

        :param page_reverse: The page_reverse of this ListListenersRequest.
        :type page_reverse: bool
        """
        self._page_reverse = page_reverse

    @property
    def protocol_port(self):
        """Gets the protocol_port of this ListListenersRequest.

        :return: The protocol_port of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._protocol_port

    @protocol_port.setter
    def protocol_port(self, protocol_port):
        """Sets the protocol_port of this ListListenersRequest.

        :param protocol_port: The protocol_port of this ListListenersRequest.
        :type protocol_port: list[str]
        """
        self._protocol_port = protocol_port

    @property
    def protocol(self):
        """Gets the protocol of this ListListenersRequest.

        :return: The protocol of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ListListenersRequest.

        :param protocol: The protocol of this ListListenersRequest.
        :type protocol: list[str]
        """
        self._protocol = protocol

    @property
    def description(self):
        """Gets the description of this ListListenersRequest.

        :return: The description of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListListenersRequest.

        :param description: The description of this ListListenersRequest.
        :type description: list[str]
        """
        self._description = description

    @property
    def default_tls_container_ref(self):
        """Gets the default_tls_container_ref of this ListListenersRequest.

        :return: The default_tls_container_ref of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._default_tls_container_ref

    @default_tls_container_ref.setter
    def default_tls_container_ref(self, default_tls_container_ref):
        """Sets the default_tls_container_ref of this ListListenersRequest.

        :param default_tls_container_ref: The default_tls_container_ref of this ListListenersRequest.
        :type default_tls_container_ref: list[str]
        """
        self._default_tls_container_ref = default_tls_container_ref

    @property
    def client_ca_tls_container_ref(self):
        """Gets the client_ca_tls_container_ref of this ListListenersRequest.

        :return: The client_ca_tls_container_ref of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._client_ca_tls_container_ref

    @client_ca_tls_container_ref.setter
    def client_ca_tls_container_ref(self, client_ca_tls_container_ref):
        """Sets the client_ca_tls_container_ref of this ListListenersRequest.

        :param client_ca_tls_container_ref: The client_ca_tls_container_ref of this ListListenersRequest.
        :type client_ca_tls_container_ref: list[str]
        """
        self._client_ca_tls_container_ref = client_ca_tls_container_ref

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this ListListenersRequest.

        :return: The admin_state_up of this ListListenersRequest.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this ListListenersRequest.

        :param admin_state_up: The admin_state_up of this ListListenersRequest.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def connection_limit(self):
        """Gets the connection_limit of this ListListenersRequest.

        :return: The connection_limit of this ListListenersRequest.
        :rtype: list[int]
        """
        return self._connection_limit

    @connection_limit.setter
    def connection_limit(self, connection_limit):
        """Sets the connection_limit of this ListListenersRequest.

        :param connection_limit: The connection_limit of this ListListenersRequest.
        :type connection_limit: list[int]
        """
        self._connection_limit = connection_limit

    @property
    def default_pool_id(self):
        """Gets the default_pool_id of this ListListenersRequest.

        :return: The default_pool_id of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._default_pool_id

    @default_pool_id.setter
    def default_pool_id(self, default_pool_id):
        """Sets the default_pool_id of this ListListenersRequest.

        :param default_pool_id: The default_pool_id of this ListListenersRequest.
        :type default_pool_id: list[str]
        """
        self._default_pool_id = default_pool_id

    @property
    def id(self):
        """Gets the id of this ListListenersRequest.

        :return: The id of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListListenersRequest.

        :param id: The id of this ListListenersRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListListenersRequest.

        :return: The name of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListListenersRequest.

        :param name: The name of this ListListenersRequest.
        :type name: list[str]
        """
        self._name = name

    @property
    def http2_enable(self):
        """Gets the http2_enable of this ListListenersRequest.

        :return: The http2_enable of this ListListenersRequest.
        :rtype: bool
        """
        return self._http2_enable

    @http2_enable.setter
    def http2_enable(self, http2_enable):
        """Sets the http2_enable of this ListListenersRequest.

        :param http2_enable: The http2_enable of this ListListenersRequest.
        :type http2_enable: bool
        """
        self._http2_enable = http2_enable

    @property
    def loadbalancer_id(self):
        """Gets the loadbalancer_id of this ListListenersRequest.

        :return: The loadbalancer_id of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._loadbalancer_id

    @loadbalancer_id.setter
    def loadbalancer_id(self, loadbalancer_id):
        """Sets the loadbalancer_id of this ListListenersRequest.

        :param loadbalancer_id: The loadbalancer_id of this ListListenersRequest.
        :type loadbalancer_id: list[str]
        """
        self._loadbalancer_id = loadbalancer_id

    @property
    def tls_ciphers_policy(self):
        """Gets the tls_ciphers_policy of this ListListenersRequest.

        :return: The tls_ciphers_policy of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._tls_ciphers_policy

    @tls_ciphers_policy.setter
    def tls_ciphers_policy(self, tls_ciphers_policy):
        """Sets the tls_ciphers_policy of this ListListenersRequest.

        :param tls_ciphers_policy: The tls_ciphers_policy of this ListListenersRequest.
        :type tls_ciphers_policy: list[str]
        """
        self._tls_ciphers_policy = tls_ciphers_policy

    @property
    def member_address(self):
        """Gets the member_address of this ListListenersRequest.

        :return: The member_address of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._member_address

    @member_address.setter
    def member_address(self, member_address):
        """Sets the member_address of this ListListenersRequest.

        :param member_address: The member_address of this ListListenersRequest.
        :type member_address: list[str]
        """
        self._member_address = member_address

    @property
    def member_device_id(self):
        """Gets the member_device_id of this ListListenersRequest.

        :return: The member_device_id of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._member_device_id

    @member_device_id.setter
    def member_device_id(self, member_device_id):
        """Sets the member_device_id of this ListListenersRequest.

        :param member_device_id: The member_device_id of this ListListenersRequest.
        :type member_device_id: list[str]
        """
        self._member_device_id = member_device_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListListenersRequest.

        :return: The enterprise_project_id of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListListenersRequest.

        :param enterprise_project_id: The enterprise_project_id of this ListListenersRequest.
        :type enterprise_project_id: list[str]
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def enable_member_retry(self):
        """Gets the enable_member_retry of this ListListenersRequest.

        :return: The enable_member_retry of this ListListenersRequest.
        :rtype: bool
        """
        return self._enable_member_retry

    @enable_member_retry.setter
    def enable_member_retry(self, enable_member_retry):
        """Sets the enable_member_retry of this ListListenersRequest.

        :param enable_member_retry: The enable_member_retry of this ListListenersRequest.
        :type enable_member_retry: bool
        """
        self._enable_member_retry = enable_member_retry

    @property
    def member_timeout(self):
        """Gets the member_timeout of this ListListenersRequest.

        :return: The member_timeout of this ListListenersRequest.
        :rtype: list[int]
        """
        return self._member_timeout

    @member_timeout.setter
    def member_timeout(self, member_timeout):
        """Sets the member_timeout of this ListListenersRequest.

        :param member_timeout: The member_timeout of this ListListenersRequest.
        :type member_timeout: list[int]
        """
        self._member_timeout = member_timeout

    @property
    def client_timeout(self):
        """Gets the client_timeout of this ListListenersRequest.

        :return: The client_timeout of this ListListenersRequest.
        :rtype: list[int]
        """
        return self._client_timeout

    @client_timeout.setter
    def client_timeout(self, client_timeout):
        """Sets the client_timeout of this ListListenersRequest.

        :param client_timeout: The client_timeout of this ListListenersRequest.
        :type client_timeout: list[int]
        """
        self._client_timeout = client_timeout

    @property
    def keepalive_timeout(self):
        """Gets the keepalive_timeout of this ListListenersRequest.

        :return: The keepalive_timeout of this ListListenersRequest.
        :rtype: list[int]
        """
        return self._keepalive_timeout

    @keepalive_timeout.setter
    def keepalive_timeout(self, keepalive_timeout):
        """Sets the keepalive_timeout of this ListListenersRequest.

        :param keepalive_timeout: The keepalive_timeout of this ListListenersRequest.
        :type keepalive_timeout: list[int]
        """
        self._keepalive_timeout = keepalive_timeout

    @property
    def transparent_client_ip_enable(self):
        """Gets the transparent_client_ip_enable of this ListListenersRequest.

        :return: The transparent_client_ip_enable of this ListListenersRequest.
        :rtype: bool
        """
        return self._transparent_client_ip_enable

    @transparent_client_ip_enable.setter
    def transparent_client_ip_enable(self, transparent_client_ip_enable):
        """Sets the transparent_client_ip_enable of this ListListenersRequest.

        :param transparent_client_ip_enable: The transparent_client_ip_enable of this ListListenersRequest.
        :type transparent_client_ip_enable: bool
        """
        self._transparent_client_ip_enable = transparent_client_ip_enable

    @property
    def enhance_l7policy_enable(self):
        """Gets the enhance_l7policy_enable of this ListListenersRequest.

        :return: The enhance_l7policy_enable of this ListListenersRequest.
        :rtype: bool
        """
        return self._enhance_l7policy_enable

    @enhance_l7policy_enable.setter
    def enhance_l7policy_enable(self, enhance_l7policy_enable):
        """Sets the enhance_l7policy_enable of this ListListenersRequest.

        :param enhance_l7policy_enable: The enhance_l7policy_enable of this ListListenersRequest.
        :type enhance_l7policy_enable: bool
        """
        self._enhance_l7policy_enable = enhance_l7policy_enable

    @property
    def member_instance_id(self):
        """Gets the member_instance_id of this ListListenersRequest.

        :return: The member_instance_id of this ListListenersRequest.
        :rtype: list[str]
        """
        return self._member_instance_id

    @member_instance_id.setter
    def member_instance_id(self, member_instance_id):
        """Sets the member_instance_id of this ListListenersRequest.

        :param member_instance_id: The member_instance_id of this ListListenersRequest.
        :type member_instance_id: list[str]
        """
        self._member_instance_id = member_instance_id

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
        if not isinstance(other, ListListenersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
