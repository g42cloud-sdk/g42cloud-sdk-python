# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateL7PolicyOption:

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
        'description': 'str',
        'name': 'str',
        'redirect_listener_id': 'str',
        'redirect_pool_id': 'str',
        'redirect_url_config': 'UpdateRedirectUrlConfig',
        'fixed_response_config': 'UpdateFixtedResponseConfig',
        'rules': 'list[CreateRuleOption]',
        'priority': 'int',
        'redirect_pools_config': 'list[CreateRedirectPoolsConfig]'
    }

    attribute_map = {
        'admin_state_up': 'admin_state_up',
        'description': 'description',
        'name': 'name',
        'redirect_listener_id': 'redirect_listener_id',
        'redirect_pool_id': 'redirect_pool_id',
        'redirect_url_config': 'redirect_url_config',
        'fixed_response_config': 'fixed_response_config',
        'rules': 'rules',
        'priority': 'priority',
        'redirect_pools_config': 'redirect_pools_config'
    }

    def __init__(self, admin_state_up=None, description=None, name=None, redirect_listener_id=None, redirect_pool_id=None, redirect_url_config=None, fixed_response_config=None, rules=None, priority=None, redirect_pools_config=None):
        """UpdateL7PolicyOption

        The model defined in g42cloud sdk

        :param admin_state_up: The param of the UpdateL7PolicyOption
        :type admin_state_up: bool
        :param description: The param of the UpdateL7PolicyOption
        :type description: str
        :param name: The param of the UpdateL7PolicyOption
        :type name: str
        :param redirect_listener_id: The param of the UpdateL7PolicyOption
        :type redirect_listener_id: str
        :param redirect_pool_id: The param of the UpdateL7PolicyOption
        :type redirect_pool_id: str
        :param redirect_url_config: The param of the UpdateL7PolicyOption
        :type redirect_url_config: :class:`g42cloudsdkelb.v3.UpdateRedirectUrlConfig`
        :param fixed_response_config: The param of the UpdateL7PolicyOption
        :type fixed_response_config: :class:`g42cloudsdkelb.v3.UpdateFixtedResponseConfig`
        :param rules: The param of the UpdateL7PolicyOption
        :type rules: list[:class:`g42cloudsdkelb.v3.CreateRuleOption`]
        :param priority: The param of the UpdateL7PolicyOption
        :type priority: int
        :param redirect_pools_config: The param of the UpdateL7PolicyOption
        :type redirect_pools_config: list[:class:`g42cloudsdkelb.v3.CreateRedirectPoolsConfig`]
        """
        
        

        self._admin_state_up = None
        self._description = None
        self._name = None
        self._redirect_listener_id = None
        self._redirect_pool_id = None
        self._redirect_url_config = None
        self._fixed_response_config = None
        self._rules = None
        self._priority = None
        self._redirect_pools_config = None
        self.discriminator = None

        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if redirect_listener_id is not None:
            self.redirect_listener_id = redirect_listener_id
        if redirect_pool_id is not None:
            self.redirect_pool_id = redirect_pool_id
        if redirect_url_config is not None:
            self.redirect_url_config = redirect_url_config
        if fixed_response_config is not None:
            self.fixed_response_config = fixed_response_config
        if rules is not None:
            self.rules = rules
        if priority is not None:
            self.priority = priority
        if redirect_pools_config is not None:
            self.redirect_pools_config = redirect_pools_config

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this UpdateL7PolicyOption.

        :return: The admin_state_up of this UpdateL7PolicyOption.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this UpdateL7PolicyOption.

        :param admin_state_up: The admin_state_up of this UpdateL7PolicyOption.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def description(self):
        """Gets the description of this UpdateL7PolicyOption.

        :return: The description of this UpdateL7PolicyOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateL7PolicyOption.

        :param description: The description of this UpdateL7PolicyOption.
        :type description: str
        """
        self._description = description

    @property
    def name(self):
        """Gets the name of this UpdateL7PolicyOption.

        :return: The name of this UpdateL7PolicyOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateL7PolicyOption.

        :param name: The name of this UpdateL7PolicyOption.
        :type name: str
        """
        self._name = name

    @property
    def redirect_listener_id(self):
        """Gets the redirect_listener_id of this UpdateL7PolicyOption.

        :return: The redirect_listener_id of this UpdateL7PolicyOption.
        :rtype: str
        """
        return self._redirect_listener_id

    @redirect_listener_id.setter
    def redirect_listener_id(self, redirect_listener_id):
        """Sets the redirect_listener_id of this UpdateL7PolicyOption.

        :param redirect_listener_id: The redirect_listener_id of this UpdateL7PolicyOption.
        :type redirect_listener_id: str
        """
        self._redirect_listener_id = redirect_listener_id

    @property
    def redirect_pool_id(self):
        """Gets the redirect_pool_id of this UpdateL7PolicyOption.

        :return: The redirect_pool_id of this UpdateL7PolicyOption.
        :rtype: str
        """
        return self._redirect_pool_id

    @redirect_pool_id.setter
    def redirect_pool_id(self, redirect_pool_id):
        """Sets the redirect_pool_id of this UpdateL7PolicyOption.

        :param redirect_pool_id: The redirect_pool_id of this UpdateL7PolicyOption.
        :type redirect_pool_id: str
        """
        self._redirect_pool_id = redirect_pool_id

    @property
    def redirect_url_config(self):
        """Gets the redirect_url_config of this UpdateL7PolicyOption.

        :return: The redirect_url_config of this UpdateL7PolicyOption.
        :rtype: :class:`g42cloudsdkelb.v3.UpdateRedirectUrlConfig`
        """
        return self._redirect_url_config

    @redirect_url_config.setter
    def redirect_url_config(self, redirect_url_config):
        """Sets the redirect_url_config of this UpdateL7PolicyOption.

        :param redirect_url_config: The redirect_url_config of this UpdateL7PolicyOption.
        :type redirect_url_config: :class:`g42cloudsdkelb.v3.UpdateRedirectUrlConfig`
        """
        self._redirect_url_config = redirect_url_config

    @property
    def fixed_response_config(self):
        """Gets the fixed_response_config of this UpdateL7PolicyOption.

        :return: The fixed_response_config of this UpdateL7PolicyOption.
        :rtype: :class:`g42cloudsdkelb.v3.UpdateFixtedResponseConfig`
        """
        return self._fixed_response_config

    @fixed_response_config.setter
    def fixed_response_config(self, fixed_response_config):
        """Sets the fixed_response_config of this UpdateL7PolicyOption.

        :param fixed_response_config: The fixed_response_config of this UpdateL7PolicyOption.
        :type fixed_response_config: :class:`g42cloudsdkelb.v3.UpdateFixtedResponseConfig`
        """
        self._fixed_response_config = fixed_response_config

    @property
    def rules(self):
        """Gets the rules of this UpdateL7PolicyOption.

        :return: The rules of this UpdateL7PolicyOption.
        :rtype: list[:class:`g42cloudsdkelb.v3.CreateRuleOption`]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this UpdateL7PolicyOption.

        :param rules: The rules of this UpdateL7PolicyOption.
        :type rules: list[:class:`g42cloudsdkelb.v3.CreateRuleOption`]
        """
        self._rules = rules

    @property
    def priority(self):
        """Gets the priority of this UpdateL7PolicyOption.

        :return: The priority of this UpdateL7PolicyOption.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this UpdateL7PolicyOption.

        :param priority: The priority of this UpdateL7PolicyOption.
        :type priority: int
        """
        self._priority = priority

    @property
    def redirect_pools_config(self):
        """Gets the redirect_pools_config of this UpdateL7PolicyOption.

        :return: The redirect_pools_config of this UpdateL7PolicyOption.
        :rtype: list[:class:`g42cloudsdkelb.v3.CreateRedirectPoolsConfig`]
        """
        return self._redirect_pools_config

    @redirect_pools_config.setter
    def redirect_pools_config(self, redirect_pools_config):
        """Sets the redirect_pools_config of this UpdateL7PolicyOption.

        :param redirect_pools_config: The redirect_pools_config of this UpdateL7PolicyOption.
        :type redirect_pools_config: list[:class:`g42cloudsdkelb.v3.CreateRedirectPoolsConfig`]
        """
        self._redirect_pools_config = redirect_pools_config

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
        if not isinstance(other, UpdateL7PolicyOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
