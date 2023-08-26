# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class Listener:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'admin_state_up': 'bool',
        'client_ca_tls_container_ref': 'str',
        'connection_limit': 'int',
        'created_at': 'str',
        'default_pool_id': 'str',
        'default_tls_container_ref': 'str',
        'description': 'str',
        'http2_enable': 'bool',
        'id': 'str',
        'insert_headers': 'ListenerInsertHeaders',
        'loadbalancers': 'list[LoadBalancerRef]',
        'name': 'str',
        'project_id': 'str',
        'protocol': 'str',
        'protocol_port': 'int',
        'sni_container_refs': 'list[str]',
        'sni_match_algo': 'str',
        'tags': 'list[Tag]',
        'updated_at': 'str',
        'tls_ciphers_policy': 'str',
        'security_policy_id': 'str',
        'enable_member_retry': 'bool',
        'keepalive_timeout': 'int',
        'client_timeout': 'int',
        'member_timeout': 'int',
        'ipgroup': 'ListenerIpGroup',
        'transparent_client_ip_enable': 'bool',
        'enhance_l7policy_enable': 'bool',
        'quic_config': 'ListenerQuicConfig'
    }

    attribute_map = {
        'admin_state_up': 'admin_state_up',
        'client_ca_tls_container_ref': 'client_ca_tls_container_ref',
        'connection_limit': 'connection_limit',
        'created_at': 'created_at',
        'default_pool_id': 'default_pool_id',
        'default_tls_container_ref': 'default_tls_container_ref',
        'description': 'description',
        'http2_enable': 'http2_enable',
        'id': 'id',
        'insert_headers': 'insert_headers',
        'loadbalancers': 'loadbalancers',
        'name': 'name',
        'project_id': 'project_id',
        'protocol': 'protocol',
        'protocol_port': 'protocol_port',
        'sni_container_refs': 'sni_container_refs',
        'sni_match_algo': 'sni_match_algo',
        'tags': 'tags',
        'updated_at': 'updated_at',
        'tls_ciphers_policy': 'tls_ciphers_policy',
        'security_policy_id': 'security_policy_id',
        'enable_member_retry': 'enable_member_retry',
        'keepalive_timeout': 'keepalive_timeout',
        'client_timeout': 'client_timeout',
        'member_timeout': 'member_timeout',
        'ipgroup': 'ipgroup',
        'transparent_client_ip_enable': 'transparent_client_ip_enable',
        'enhance_l7policy_enable': 'enhance_l7policy_enable',
        'quic_config': 'quic_config'
    }

    def __init__(self, admin_state_up=None, client_ca_tls_container_ref=None, connection_limit=None, created_at=None, default_pool_id=None, default_tls_container_ref=None, description=None, http2_enable=None, id=None, insert_headers=None, loadbalancers=None, name=None, project_id=None, protocol=None, protocol_port=None, sni_container_refs=None, sni_match_algo=None, tags=None, updated_at=None, tls_ciphers_policy=None, security_policy_id=None, enable_member_retry=None, keepalive_timeout=None, client_timeout=None, member_timeout=None, ipgroup=None, transparent_client_ip_enable=None, enhance_l7policy_enable=None, quic_config=None):
        """Listener

        The model defined in g42cloud sdk

        :param admin_state_up: The param of the Listener
        :type admin_state_up: bool
        :param client_ca_tls_container_ref: The param of the Listener
        :type client_ca_tls_container_ref: str
        :param connection_limit: The param of the Listener
        :type connection_limit: int
        :param created_at: The param of the Listener
        :type created_at: str
        :param default_pool_id: The param of the Listener
        :type default_pool_id: str
        :param default_tls_container_ref: The param of the Listener
        :type default_tls_container_ref: str
        :param description: The param of the Listener
        :type description: str
        :param http2_enable: The param of the Listener
        :type http2_enable: bool
        :param id: The param of the Listener
        :type id: str
        :param insert_headers: The param of the Listener
        :type insert_headers: :class:`g42cloudsdkelb.v3.ListenerInsertHeaders`
        :param loadbalancers: The param of the Listener
        :type loadbalancers: list[:class:`g42cloudsdkelb.v3.LoadBalancerRef`]
        :param name: The param of the Listener
        :type name: str
        :param project_id: The param of the Listener
        :type project_id: str
        :param protocol: The param of the Listener
        :type protocol: str
        :param protocol_port: The param of the Listener
        :type protocol_port: int
        :param sni_container_refs: The param of the Listener
        :type sni_container_refs: list[str]
        :param sni_match_algo: The param of the Listener
        :type sni_match_algo: str
        :param tags: The param of the Listener
        :type tags: list[:class:`g42cloudsdkelb.v3.Tag`]
        :param updated_at: The param of the Listener
        :type updated_at: str
        :param tls_ciphers_policy: The param of the Listener
        :type tls_ciphers_policy: str
        :param security_policy_id: The param of the Listener
        :type security_policy_id: str
        :param enable_member_retry: The param of the Listener
        :type enable_member_retry: bool
        :param keepalive_timeout: The param of the Listener
        :type keepalive_timeout: int
        :param client_timeout: The param of the Listener
        :type client_timeout: int
        :param member_timeout: The param of the Listener
        :type member_timeout: int
        :param ipgroup: The param of the Listener
        :type ipgroup: :class:`g42cloudsdkelb.v3.ListenerIpGroup`
        :param transparent_client_ip_enable: The param of the Listener
        :type transparent_client_ip_enable: bool
        :param enhance_l7policy_enable: The param of the Listener
        :type enhance_l7policy_enable: bool
        :param quic_config: The param of the Listener
        :type quic_config: :class:`g42cloudsdkelb.v3.ListenerQuicConfig`
        """
        
        

        self._admin_state_up = None
        self._client_ca_tls_container_ref = None
        self._connection_limit = None
        self._created_at = None
        self._default_pool_id = None
        self._default_tls_container_ref = None
        self._description = None
        self._http2_enable = None
        self._id = None
        self._insert_headers = None
        self._loadbalancers = None
        self._name = None
        self._project_id = None
        self._protocol = None
        self._protocol_port = None
        self._sni_container_refs = None
        self._sni_match_algo = None
        self._tags = None
        self._updated_at = None
        self._tls_ciphers_policy = None
        self._security_policy_id = None
        self._enable_member_retry = None
        self._keepalive_timeout = None
        self._client_timeout = None
        self._member_timeout = None
        self._ipgroup = None
        self._transparent_client_ip_enable = None
        self._enhance_l7policy_enable = None
        self._quic_config = None
        self.discriminator = None

        self.admin_state_up = admin_state_up
        self.client_ca_tls_container_ref = client_ca_tls_container_ref
        self.connection_limit = connection_limit
        self.created_at = created_at
        self.default_pool_id = default_pool_id
        self.default_tls_container_ref = default_tls_container_ref
        self.description = description
        self.http2_enable = http2_enable
        self.id = id
        self.insert_headers = insert_headers
        self.loadbalancers = loadbalancers
        self.name = name
        self.project_id = project_id
        self.protocol = protocol
        self.protocol_port = protocol_port
        self.sni_container_refs = sni_container_refs
        self.sni_match_algo = sni_match_algo
        self.tags = tags
        self.updated_at = updated_at
        self.tls_ciphers_policy = tls_ciphers_policy
        self.security_policy_id = security_policy_id
        self.enable_member_retry = enable_member_retry
        self.keepalive_timeout = keepalive_timeout
        self.client_timeout = client_timeout
        self.member_timeout = member_timeout
        self.ipgroup = ipgroup
        self.transparent_client_ip_enable = transparent_client_ip_enable
        self.enhance_l7policy_enable = enhance_l7policy_enable
        if quic_config is not None:
            self.quic_config = quic_config

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this Listener.

        :return: The admin_state_up of this Listener.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this Listener.

        :param admin_state_up: The admin_state_up of this Listener.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def client_ca_tls_container_ref(self):
        """Gets the client_ca_tls_container_ref of this Listener.

        :return: The client_ca_tls_container_ref of this Listener.
        :rtype: str
        """
        return self._client_ca_tls_container_ref

    @client_ca_tls_container_ref.setter
    def client_ca_tls_container_ref(self, client_ca_tls_container_ref):
        """Sets the client_ca_tls_container_ref of this Listener.

        :param client_ca_tls_container_ref: The client_ca_tls_container_ref of this Listener.
        :type client_ca_tls_container_ref: str
        """
        self._client_ca_tls_container_ref = client_ca_tls_container_ref

    @property
    def connection_limit(self):
        """Gets the connection_limit of this Listener.

        :return: The connection_limit of this Listener.
        :rtype: int
        """
        return self._connection_limit

    @connection_limit.setter
    def connection_limit(self, connection_limit):
        """Sets the connection_limit of this Listener.

        :param connection_limit: The connection_limit of this Listener.
        :type connection_limit: int
        """
        self._connection_limit = connection_limit

    @property
    def created_at(self):
        """Gets the created_at of this Listener.

        :return: The created_at of this Listener.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Listener.

        :param created_at: The created_at of this Listener.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def default_pool_id(self):
        """Gets the default_pool_id of this Listener.

        :return: The default_pool_id of this Listener.
        :rtype: str
        """
        return self._default_pool_id

    @default_pool_id.setter
    def default_pool_id(self, default_pool_id):
        """Sets the default_pool_id of this Listener.

        :param default_pool_id: The default_pool_id of this Listener.
        :type default_pool_id: str
        """
        self._default_pool_id = default_pool_id

    @property
    def default_tls_container_ref(self):
        """Gets the default_tls_container_ref of this Listener.

        :return: The default_tls_container_ref of this Listener.
        :rtype: str
        """
        return self._default_tls_container_ref

    @default_tls_container_ref.setter
    def default_tls_container_ref(self, default_tls_container_ref):
        """Sets the default_tls_container_ref of this Listener.

        :param default_tls_container_ref: The default_tls_container_ref of this Listener.
        :type default_tls_container_ref: str
        """
        self._default_tls_container_ref = default_tls_container_ref

    @property
    def description(self):
        """Gets the description of this Listener.

        :return: The description of this Listener.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Listener.

        :param description: The description of this Listener.
        :type description: str
        """
        self._description = description

    @property
    def http2_enable(self):
        """Gets the http2_enable of this Listener.

        :return: The http2_enable of this Listener.
        :rtype: bool
        """
        return self._http2_enable

    @http2_enable.setter
    def http2_enable(self, http2_enable):
        """Sets the http2_enable of this Listener.

        :param http2_enable: The http2_enable of this Listener.
        :type http2_enable: bool
        """
        self._http2_enable = http2_enable

    @property
    def id(self):
        """Gets the id of this Listener.

        :return: The id of this Listener.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Listener.

        :param id: The id of this Listener.
        :type id: str
        """
        self._id = id

    @property
    def insert_headers(self):
        """Gets the insert_headers of this Listener.

        :return: The insert_headers of this Listener.
        :rtype: :class:`g42cloudsdkelb.v3.ListenerInsertHeaders`
        """
        return self._insert_headers

    @insert_headers.setter
    def insert_headers(self, insert_headers):
        """Sets the insert_headers of this Listener.

        :param insert_headers: The insert_headers of this Listener.
        :type insert_headers: :class:`g42cloudsdkelb.v3.ListenerInsertHeaders`
        """
        self._insert_headers = insert_headers

    @property
    def loadbalancers(self):
        """Gets the loadbalancers of this Listener.

        :return: The loadbalancers of this Listener.
        :rtype: list[:class:`g42cloudsdkelb.v3.LoadBalancerRef`]
        """
        return self._loadbalancers

    @loadbalancers.setter
    def loadbalancers(self, loadbalancers):
        """Sets the loadbalancers of this Listener.

        :param loadbalancers: The loadbalancers of this Listener.
        :type loadbalancers: list[:class:`g42cloudsdkelb.v3.LoadBalancerRef`]
        """
        self._loadbalancers = loadbalancers

    @property
    def name(self):
        """Gets the name of this Listener.

        :return: The name of this Listener.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Listener.

        :param name: The name of this Listener.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        """Gets the project_id of this Listener.

        :return: The project_id of this Listener.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Listener.

        :param project_id: The project_id of this Listener.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def protocol(self):
        """Gets the protocol of this Listener.

        :return: The protocol of this Listener.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this Listener.

        :param protocol: The protocol of this Listener.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def protocol_port(self):
        """Gets the protocol_port of this Listener.

        :return: The protocol_port of this Listener.
        :rtype: int
        """
        return self._protocol_port

    @protocol_port.setter
    def protocol_port(self, protocol_port):
        """Sets the protocol_port of this Listener.

        :param protocol_port: The protocol_port of this Listener.
        :type protocol_port: int
        """
        self._protocol_port = protocol_port

    @property
    def sni_container_refs(self):
        """Gets the sni_container_refs of this Listener.

        :return: The sni_container_refs of this Listener.
        :rtype: list[str]
        """
        return self._sni_container_refs

    @sni_container_refs.setter
    def sni_container_refs(self, sni_container_refs):
        """Sets the sni_container_refs of this Listener.

        :param sni_container_refs: The sni_container_refs of this Listener.
        :type sni_container_refs: list[str]
        """
        self._sni_container_refs = sni_container_refs

    @property
    def sni_match_algo(self):
        """Gets the sni_match_algo of this Listener.

        :return: The sni_match_algo of this Listener.
        :rtype: str
        """
        return self._sni_match_algo

    @sni_match_algo.setter
    def sni_match_algo(self, sni_match_algo):
        """Sets the sni_match_algo of this Listener.

        :param sni_match_algo: The sni_match_algo of this Listener.
        :type sni_match_algo: str
        """
        self._sni_match_algo = sni_match_algo

    @property
    def tags(self):
        """Gets the tags of this Listener.

        :return: The tags of this Listener.
        :rtype: list[:class:`g42cloudsdkelb.v3.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Listener.

        :param tags: The tags of this Listener.
        :type tags: list[:class:`g42cloudsdkelb.v3.Tag`]
        """
        self._tags = tags

    @property
    def updated_at(self):
        """Gets the updated_at of this Listener.

        :return: The updated_at of this Listener.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Listener.

        :param updated_at: The updated_at of this Listener.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def tls_ciphers_policy(self):
        """Gets the tls_ciphers_policy of this Listener.

        :return: The tls_ciphers_policy of this Listener.
        :rtype: str
        """
        return self._tls_ciphers_policy

    @tls_ciphers_policy.setter
    def tls_ciphers_policy(self, tls_ciphers_policy):
        """Sets the tls_ciphers_policy of this Listener.

        :param tls_ciphers_policy: The tls_ciphers_policy of this Listener.
        :type tls_ciphers_policy: str
        """
        self._tls_ciphers_policy = tls_ciphers_policy

    @property
    def security_policy_id(self):
        """Gets the security_policy_id of this Listener.

        :return: The security_policy_id of this Listener.
        :rtype: str
        """
        return self._security_policy_id

    @security_policy_id.setter
    def security_policy_id(self, security_policy_id):
        """Sets the security_policy_id of this Listener.

        :param security_policy_id: The security_policy_id of this Listener.
        :type security_policy_id: str
        """
        self._security_policy_id = security_policy_id

    @property
    def enable_member_retry(self):
        """Gets the enable_member_retry of this Listener.

        :return: The enable_member_retry of this Listener.
        :rtype: bool
        """
        return self._enable_member_retry

    @enable_member_retry.setter
    def enable_member_retry(self, enable_member_retry):
        """Sets the enable_member_retry of this Listener.

        :param enable_member_retry: The enable_member_retry of this Listener.
        :type enable_member_retry: bool
        """
        self._enable_member_retry = enable_member_retry

    @property
    def keepalive_timeout(self):
        """Gets the keepalive_timeout of this Listener.

        :return: The keepalive_timeout of this Listener.
        :rtype: int
        """
        return self._keepalive_timeout

    @keepalive_timeout.setter
    def keepalive_timeout(self, keepalive_timeout):
        """Sets the keepalive_timeout of this Listener.

        :param keepalive_timeout: The keepalive_timeout of this Listener.
        :type keepalive_timeout: int
        """
        self._keepalive_timeout = keepalive_timeout

    @property
    def client_timeout(self):
        """Gets the client_timeout of this Listener.

        :return: The client_timeout of this Listener.
        :rtype: int
        """
        return self._client_timeout

    @client_timeout.setter
    def client_timeout(self, client_timeout):
        """Sets the client_timeout of this Listener.

        :param client_timeout: The client_timeout of this Listener.
        :type client_timeout: int
        """
        self._client_timeout = client_timeout

    @property
    def member_timeout(self):
        """Gets the member_timeout of this Listener.

        :return: The member_timeout of this Listener.
        :rtype: int
        """
        return self._member_timeout

    @member_timeout.setter
    def member_timeout(self, member_timeout):
        """Sets the member_timeout of this Listener.

        :param member_timeout: The member_timeout of this Listener.
        :type member_timeout: int
        """
        self._member_timeout = member_timeout

    @property
    def ipgroup(self):
        """Gets the ipgroup of this Listener.

        :return: The ipgroup of this Listener.
        :rtype: :class:`g42cloudsdkelb.v3.ListenerIpGroup`
        """
        return self._ipgroup

    @ipgroup.setter
    def ipgroup(self, ipgroup):
        """Sets the ipgroup of this Listener.

        :param ipgroup: The ipgroup of this Listener.
        :type ipgroup: :class:`g42cloudsdkelb.v3.ListenerIpGroup`
        """
        self._ipgroup = ipgroup

    @property
    def transparent_client_ip_enable(self):
        """Gets the transparent_client_ip_enable of this Listener.

        :return: The transparent_client_ip_enable of this Listener.
        :rtype: bool
        """
        return self._transparent_client_ip_enable

    @transparent_client_ip_enable.setter
    def transparent_client_ip_enable(self, transparent_client_ip_enable):
        """Sets the transparent_client_ip_enable of this Listener.

        :param transparent_client_ip_enable: The transparent_client_ip_enable of this Listener.
        :type transparent_client_ip_enable: bool
        """
        self._transparent_client_ip_enable = transparent_client_ip_enable

    @property
    def enhance_l7policy_enable(self):
        """Gets the enhance_l7policy_enable of this Listener.

        :return: The enhance_l7policy_enable of this Listener.
        :rtype: bool
        """
        return self._enhance_l7policy_enable

    @enhance_l7policy_enable.setter
    def enhance_l7policy_enable(self, enhance_l7policy_enable):
        """Sets the enhance_l7policy_enable of this Listener.

        :param enhance_l7policy_enable: The enhance_l7policy_enable of this Listener.
        :type enhance_l7policy_enable: bool
        """
        self._enhance_l7policy_enable = enhance_l7policy_enable

    @property
    def quic_config(self):
        """Gets the quic_config of this Listener.

        :return: The quic_config of this Listener.
        :rtype: :class:`g42cloudsdkelb.v3.ListenerQuicConfig`
        """
        return self._quic_config

    @quic_config.setter
    def quic_config(self, quic_config):
        """Sets the quic_config of this Listener.

        :param quic_config: The quic_config of this Listener.
        :type quic_config: :class:`g42cloudsdkelb.v3.ListenerQuicConfig`
        """
        self._quic_config = quic_config

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
        if not isinstance(other, Listener):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
