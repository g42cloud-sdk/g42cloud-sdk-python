# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateListenerOption:

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
        'default_pool_id': 'str',
        'default_tls_container_ref': 'str',
        'description': 'str',
        'http2_enable': 'bool',
        'insert_headers': 'ListenerInsertHeaders',
        'name': 'str',
        'sni_container_refs': 'list[str]',
        'sni_match_algo': 'str',
        'tls_ciphers_policy': 'str',
        'security_policy_id': 'str',
        'enable_member_retry': 'bool',
        'member_timeout': 'int',
        'client_timeout': 'int',
        'keepalive_timeout': 'int',
        'ipgroup': 'UpdateListenerIpGroupOption',
        'transparent_client_ip_enable': 'bool',
        'enhance_l7policy_enable': 'bool',
        'quic_config': 'UpdateListenerQuicConfigOption'
    }

    attribute_map = {
        'admin_state_up': 'admin_state_up',
        'client_ca_tls_container_ref': 'client_ca_tls_container_ref',
        'default_pool_id': 'default_pool_id',
        'default_tls_container_ref': 'default_tls_container_ref',
        'description': 'description',
        'http2_enable': 'http2_enable',
        'insert_headers': 'insert_headers',
        'name': 'name',
        'sni_container_refs': 'sni_container_refs',
        'sni_match_algo': 'sni_match_algo',
        'tls_ciphers_policy': 'tls_ciphers_policy',
        'security_policy_id': 'security_policy_id',
        'enable_member_retry': 'enable_member_retry',
        'member_timeout': 'member_timeout',
        'client_timeout': 'client_timeout',
        'keepalive_timeout': 'keepalive_timeout',
        'ipgroup': 'ipgroup',
        'transparent_client_ip_enable': 'transparent_client_ip_enable',
        'enhance_l7policy_enable': 'enhance_l7policy_enable',
        'quic_config': 'quic_config'
    }

    def __init__(self, admin_state_up=None, client_ca_tls_container_ref=None, default_pool_id=None, default_tls_container_ref=None, description=None, http2_enable=None, insert_headers=None, name=None, sni_container_refs=None, sni_match_algo=None, tls_ciphers_policy=None, security_policy_id=None, enable_member_retry=None, member_timeout=None, client_timeout=None, keepalive_timeout=None, ipgroup=None, transparent_client_ip_enable=None, enhance_l7policy_enable=None, quic_config=None):
        """UpdateListenerOption

        The model defined in g42cloud sdk

        :param admin_state_up: The param of the UpdateListenerOption
        :type admin_state_up: bool
        :param client_ca_tls_container_ref: The param of the UpdateListenerOption
        :type client_ca_tls_container_ref: str
        :param default_pool_id: The param of the UpdateListenerOption
        :type default_pool_id: str
        :param default_tls_container_ref: The param of the UpdateListenerOption
        :type default_tls_container_ref: str
        :param description: The param of the UpdateListenerOption
        :type description: str
        :param http2_enable: The param of the UpdateListenerOption
        :type http2_enable: bool
        :param insert_headers: The param of the UpdateListenerOption
        :type insert_headers: :class:`g42cloudsdkelb.v3.ListenerInsertHeaders`
        :param name: The param of the UpdateListenerOption
        :type name: str
        :param sni_container_refs: The param of the UpdateListenerOption
        :type sni_container_refs: list[str]
        :param sni_match_algo: The param of the UpdateListenerOption
        :type sni_match_algo: str
        :param tls_ciphers_policy: The param of the UpdateListenerOption
        :type tls_ciphers_policy: str
        :param security_policy_id: The param of the UpdateListenerOption
        :type security_policy_id: str
        :param enable_member_retry: The param of the UpdateListenerOption
        :type enable_member_retry: bool
        :param member_timeout: The param of the UpdateListenerOption
        :type member_timeout: int
        :param client_timeout: The param of the UpdateListenerOption
        :type client_timeout: int
        :param keepalive_timeout: The param of the UpdateListenerOption
        :type keepalive_timeout: int
        :param ipgroup: The param of the UpdateListenerOption
        :type ipgroup: :class:`g42cloudsdkelb.v3.UpdateListenerIpGroupOption`
        :param transparent_client_ip_enable: The param of the UpdateListenerOption
        :type transparent_client_ip_enable: bool
        :param enhance_l7policy_enable: The param of the UpdateListenerOption
        :type enhance_l7policy_enable: bool
        :param quic_config: The param of the UpdateListenerOption
        :type quic_config: :class:`g42cloudsdkelb.v3.UpdateListenerQuicConfigOption`
        """
        
        

        self._admin_state_up = None
        self._client_ca_tls_container_ref = None
        self._default_pool_id = None
        self._default_tls_container_ref = None
        self._description = None
        self._http2_enable = None
        self._insert_headers = None
        self._name = None
        self._sni_container_refs = None
        self._sni_match_algo = None
        self._tls_ciphers_policy = None
        self._security_policy_id = None
        self._enable_member_retry = None
        self._member_timeout = None
        self._client_timeout = None
        self._keepalive_timeout = None
        self._ipgroup = None
        self._transparent_client_ip_enable = None
        self._enhance_l7policy_enable = None
        self._quic_config = None
        self.discriminator = None

        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if client_ca_tls_container_ref is not None:
            self.client_ca_tls_container_ref = client_ca_tls_container_ref
        if default_pool_id is not None:
            self.default_pool_id = default_pool_id
        if default_tls_container_ref is not None:
            self.default_tls_container_ref = default_tls_container_ref
        if description is not None:
            self.description = description
        if http2_enable is not None:
            self.http2_enable = http2_enable
        if insert_headers is not None:
            self.insert_headers = insert_headers
        if name is not None:
            self.name = name
        if sni_container_refs is not None:
            self.sni_container_refs = sni_container_refs
        if sni_match_algo is not None:
            self.sni_match_algo = sni_match_algo
        if tls_ciphers_policy is not None:
            self.tls_ciphers_policy = tls_ciphers_policy
        if security_policy_id is not None:
            self.security_policy_id = security_policy_id
        if enable_member_retry is not None:
            self.enable_member_retry = enable_member_retry
        if member_timeout is not None:
            self.member_timeout = member_timeout
        if client_timeout is not None:
            self.client_timeout = client_timeout
        if keepalive_timeout is not None:
            self.keepalive_timeout = keepalive_timeout
        if ipgroup is not None:
            self.ipgroup = ipgroup
        if transparent_client_ip_enable is not None:
            self.transparent_client_ip_enable = transparent_client_ip_enable
        if enhance_l7policy_enable is not None:
            self.enhance_l7policy_enable = enhance_l7policy_enable
        if quic_config is not None:
            self.quic_config = quic_config

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this UpdateListenerOption.

        :return: The admin_state_up of this UpdateListenerOption.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this UpdateListenerOption.

        :param admin_state_up: The admin_state_up of this UpdateListenerOption.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def client_ca_tls_container_ref(self):
        """Gets the client_ca_tls_container_ref of this UpdateListenerOption.

        :return: The client_ca_tls_container_ref of this UpdateListenerOption.
        :rtype: str
        """
        return self._client_ca_tls_container_ref

    @client_ca_tls_container_ref.setter
    def client_ca_tls_container_ref(self, client_ca_tls_container_ref):
        """Sets the client_ca_tls_container_ref of this UpdateListenerOption.

        :param client_ca_tls_container_ref: The client_ca_tls_container_ref of this UpdateListenerOption.
        :type client_ca_tls_container_ref: str
        """
        self._client_ca_tls_container_ref = client_ca_tls_container_ref

    @property
    def default_pool_id(self):
        """Gets the default_pool_id of this UpdateListenerOption.

        :return: The default_pool_id of this UpdateListenerOption.
        :rtype: str
        """
        return self._default_pool_id

    @default_pool_id.setter
    def default_pool_id(self, default_pool_id):
        """Sets the default_pool_id of this UpdateListenerOption.

        :param default_pool_id: The default_pool_id of this UpdateListenerOption.
        :type default_pool_id: str
        """
        self._default_pool_id = default_pool_id

    @property
    def default_tls_container_ref(self):
        """Gets the default_tls_container_ref of this UpdateListenerOption.

        :return: The default_tls_container_ref of this UpdateListenerOption.
        :rtype: str
        """
        return self._default_tls_container_ref

    @default_tls_container_ref.setter
    def default_tls_container_ref(self, default_tls_container_ref):
        """Sets the default_tls_container_ref of this UpdateListenerOption.

        :param default_tls_container_ref: The default_tls_container_ref of this UpdateListenerOption.
        :type default_tls_container_ref: str
        """
        self._default_tls_container_ref = default_tls_container_ref

    @property
    def description(self):
        """Gets the description of this UpdateListenerOption.

        :return: The description of this UpdateListenerOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateListenerOption.

        :param description: The description of this UpdateListenerOption.
        :type description: str
        """
        self._description = description

    @property
    def http2_enable(self):
        """Gets the http2_enable of this UpdateListenerOption.

        :return: The http2_enable of this UpdateListenerOption.
        :rtype: bool
        """
        return self._http2_enable

    @http2_enable.setter
    def http2_enable(self, http2_enable):
        """Sets the http2_enable of this UpdateListenerOption.

        :param http2_enable: The http2_enable of this UpdateListenerOption.
        :type http2_enable: bool
        """
        self._http2_enable = http2_enable

    @property
    def insert_headers(self):
        """Gets the insert_headers of this UpdateListenerOption.

        :return: The insert_headers of this UpdateListenerOption.
        :rtype: :class:`g42cloudsdkelb.v3.ListenerInsertHeaders`
        """
        return self._insert_headers

    @insert_headers.setter
    def insert_headers(self, insert_headers):
        """Sets the insert_headers of this UpdateListenerOption.

        :param insert_headers: The insert_headers of this UpdateListenerOption.
        :type insert_headers: :class:`g42cloudsdkelb.v3.ListenerInsertHeaders`
        """
        self._insert_headers = insert_headers

    @property
    def name(self):
        """Gets the name of this UpdateListenerOption.

        :return: The name of this UpdateListenerOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateListenerOption.

        :param name: The name of this UpdateListenerOption.
        :type name: str
        """
        self._name = name

    @property
    def sni_container_refs(self):
        """Gets the sni_container_refs of this UpdateListenerOption.

        :return: The sni_container_refs of this UpdateListenerOption.
        :rtype: list[str]
        """
        return self._sni_container_refs

    @sni_container_refs.setter
    def sni_container_refs(self, sni_container_refs):
        """Sets the sni_container_refs of this UpdateListenerOption.

        :param sni_container_refs: The sni_container_refs of this UpdateListenerOption.
        :type sni_container_refs: list[str]
        """
        self._sni_container_refs = sni_container_refs

    @property
    def sni_match_algo(self):
        """Gets the sni_match_algo of this UpdateListenerOption.

        :return: The sni_match_algo of this UpdateListenerOption.
        :rtype: str
        """
        return self._sni_match_algo

    @sni_match_algo.setter
    def sni_match_algo(self, sni_match_algo):
        """Sets the sni_match_algo of this UpdateListenerOption.

        :param sni_match_algo: The sni_match_algo of this UpdateListenerOption.
        :type sni_match_algo: str
        """
        self._sni_match_algo = sni_match_algo

    @property
    def tls_ciphers_policy(self):
        """Gets the tls_ciphers_policy of this UpdateListenerOption.

        :return: The tls_ciphers_policy of this UpdateListenerOption.
        :rtype: str
        """
        return self._tls_ciphers_policy

    @tls_ciphers_policy.setter
    def tls_ciphers_policy(self, tls_ciphers_policy):
        """Sets the tls_ciphers_policy of this UpdateListenerOption.

        :param tls_ciphers_policy: The tls_ciphers_policy of this UpdateListenerOption.
        :type tls_ciphers_policy: str
        """
        self._tls_ciphers_policy = tls_ciphers_policy

    @property
    def security_policy_id(self):
        """Gets the security_policy_id of this UpdateListenerOption.

        :return: The security_policy_id of this UpdateListenerOption.
        :rtype: str
        """
        return self._security_policy_id

    @security_policy_id.setter
    def security_policy_id(self, security_policy_id):
        """Sets the security_policy_id of this UpdateListenerOption.

        :param security_policy_id: The security_policy_id of this UpdateListenerOption.
        :type security_policy_id: str
        """
        self._security_policy_id = security_policy_id

    @property
    def enable_member_retry(self):
        """Gets the enable_member_retry of this UpdateListenerOption.

        :return: The enable_member_retry of this UpdateListenerOption.
        :rtype: bool
        """
        return self._enable_member_retry

    @enable_member_retry.setter
    def enable_member_retry(self, enable_member_retry):
        """Sets the enable_member_retry of this UpdateListenerOption.

        :param enable_member_retry: The enable_member_retry of this UpdateListenerOption.
        :type enable_member_retry: bool
        """
        self._enable_member_retry = enable_member_retry

    @property
    def member_timeout(self):
        """Gets the member_timeout of this UpdateListenerOption.

        :return: The member_timeout of this UpdateListenerOption.
        :rtype: int
        """
        return self._member_timeout

    @member_timeout.setter
    def member_timeout(self, member_timeout):
        """Sets the member_timeout of this UpdateListenerOption.

        :param member_timeout: The member_timeout of this UpdateListenerOption.
        :type member_timeout: int
        """
        self._member_timeout = member_timeout

    @property
    def client_timeout(self):
        """Gets the client_timeout of this UpdateListenerOption.

        :return: The client_timeout of this UpdateListenerOption.
        :rtype: int
        """
        return self._client_timeout

    @client_timeout.setter
    def client_timeout(self, client_timeout):
        """Sets the client_timeout of this UpdateListenerOption.

        :param client_timeout: The client_timeout of this UpdateListenerOption.
        :type client_timeout: int
        """
        self._client_timeout = client_timeout

    @property
    def keepalive_timeout(self):
        """Gets the keepalive_timeout of this UpdateListenerOption.

        :return: The keepalive_timeout of this UpdateListenerOption.
        :rtype: int
        """
        return self._keepalive_timeout

    @keepalive_timeout.setter
    def keepalive_timeout(self, keepalive_timeout):
        """Sets the keepalive_timeout of this UpdateListenerOption.

        :param keepalive_timeout: The keepalive_timeout of this UpdateListenerOption.
        :type keepalive_timeout: int
        """
        self._keepalive_timeout = keepalive_timeout

    @property
    def ipgroup(self):
        """Gets the ipgroup of this UpdateListenerOption.

        :return: The ipgroup of this UpdateListenerOption.
        :rtype: :class:`g42cloudsdkelb.v3.UpdateListenerIpGroupOption`
        """
        return self._ipgroup

    @ipgroup.setter
    def ipgroup(self, ipgroup):
        """Sets the ipgroup of this UpdateListenerOption.

        :param ipgroup: The ipgroup of this UpdateListenerOption.
        :type ipgroup: :class:`g42cloudsdkelb.v3.UpdateListenerIpGroupOption`
        """
        self._ipgroup = ipgroup

    @property
    def transparent_client_ip_enable(self):
        """Gets the transparent_client_ip_enable of this UpdateListenerOption.

        :return: The transparent_client_ip_enable of this UpdateListenerOption.
        :rtype: bool
        """
        return self._transparent_client_ip_enable

    @transparent_client_ip_enable.setter
    def transparent_client_ip_enable(self, transparent_client_ip_enable):
        """Sets the transparent_client_ip_enable of this UpdateListenerOption.

        :param transparent_client_ip_enable: The transparent_client_ip_enable of this UpdateListenerOption.
        :type transparent_client_ip_enable: bool
        """
        self._transparent_client_ip_enable = transparent_client_ip_enable

    @property
    def enhance_l7policy_enable(self):
        """Gets the enhance_l7policy_enable of this UpdateListenerOption.

        :return: The enhance_l7policy_enable of this UpdateListenerOption.
        :rtype: bool
        """
        return self._enhance_l7policy_enable

    @enhance_l7policy_enable.setter
    def enhance_l7policy_enable(self, enhance_l7policy_enable):
        """Sets the enhance_l7policy_enable of this UpdateListenerOption.

        :param enhance_l7policy_enable: The enhance_l7policy_enable of this UpdateListenerOption.
        :type enhance_l7policy_enable: bool
        """
        self._enhance_l7policy_enable = enhance_l7policy_enable

    @property
    def quic_config(self):
        """Gets the quic_config of this UpdateListenerOption.

        :return: The quic_config of this UpdateListenerOption.
        :rtype: :class:`g42cloudsdkelb.v3.UpdateListenerQuicConfigOption`
        """
        return self._quic_config

    @quic_config.setter
    def quic_config(self, quic_config):
        """Sets the quic_config of this UpdateListenerOption.

        :param quic_config: The quic_config of this UpdateListenerOption.
        :type quic_config: :class:`g42cloudsdkelb.v3.UpdateListenerQuicConfigOption`
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
        if not isinstance(other, UpdateListenerOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
