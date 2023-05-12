# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateL7PolicyOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'admin_state_up': 'bool',
        'description': 'str',
        'listener_id': 'str',
        'name': 'str',
        'position': 'int',
        'priority': 'int',
        'project_id': 'str',
        'redirect_listener_id': 'str',
        'redirect_pool_id': 'str',
        'redirect_pools_config': 'list[CreateRedirectPoolsConfig]',
        'redirect_url': 'str',
        'redirect_url_config': 'CreateRedirectUrlConfig',
        'fixed_response_config': 'CreateFixtedResponseConfig',
        'rules': 'list[CreateL7PolicyRuleOption]'
    }

    attribute_map = {
        'action': 'action',
        'admin_state_up': 'admin_state_up',
        'description': 'description',
        'listener_id': 'listener_id',
        'name': 'name',
        'position': 'position',
        'priority': 'priority',
        'project_id': 'project_id',
        'redirect_listener_id': 'redirect_listener_id',
        'redirect_pool_id': 'redirect_pool_id',
        'redirect_pools_config': 'redirect_pools_config',
        'redirect_url': 'redirect_url',
        'redirect_url_config': 'redirect_url_config',
        'fixed_response_config': 'fixed_response_config',
        'rules': 'rules'
    }

    def __init__(self, action=None, admin_state_up=None, description=None, listener_id=None, name=None, position=None, priority=None, project_id=None, redirect_listener_id=None, redirect_pool_id=None, redirect_pools_config=None, redirect_url=None, redirect_url_config=None, fixed_response_config=None, rules=None):
        """CreateL7PolicyOption

        The model defined in g42cloud sdk

        :param action: The param of the CreateL7PolicyOption
        :type action: str
        :param admin_state_up: The param of the CreateL7PolicyOption
        :type admin_state_up: bool
        :param description: The param of the CreateL7PolicyOption
        :type description: str
        :param listener_id: The param of the CreateL7PolicyOption
        :type listener_id: str
        :param name: The param of the CreateL7PolicyOption
        :type name: str
        :param position: The param of the CreateL7PolicyOption
        :type position: int
        :param priority: The param of the CreateL7PolicyOption
        :type priority: int
        :param project_id: The param of the CreateL7PolicyOption
        :type project_id: str
        :param redirect_listener_id: The param of the CreateL7PolicyOption
        :type redirect_listener_id: str
        :param redirect_pool_id: The param of the CreateL7PolicyOption
        :type redirect_pool_id: str
        :param redirect_pools_config: The param of the CreateL7PolicyOption
        :type redirect_pools_config: list[:class:`g42cloudsdkelb.v3.CreateRedirectPoolsConfig`]
        :param redirect_url: The param of the CreateL7PolicyOption
        :type redirect_url: str
        :param redirect_url_config: The param of the CreateL7PolicyOption
        :type redirect_url_config: :class:`g42cloudsdkelb.v3.CreateRedirectUrlConfig`
        :param fixed_response_config: The param of the CreateL7PolicyOption
        :type fixed_response_config: :class:`g42cloudsdkelb.v3.CreateFixtedResponseConfig`
        :param rules: The param of the CreateL7PolicyOption
        :type rules: list[:class:`g42cloudsdkelb.v3.CreateL7PolicyRuleOption`]
        """
        
        

        self._action = None
        self._admin_state_up = None
        self._description = None
        self._listener_id = None
        self._name = None
        self._position = None
        self._priority = None
        self._project_id = None
        self._redirect_listener_id = None
        self._redirect_pool_id = None
        self._redirect_pools_config = None
        self._redirect_url = None
        self._redirect_url_config = None
        self._fixed_response_config = None
        self._rules = None
        self.discriminator = None

        self.action = action
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if description is not None:
            self.description = description
        self.listener_id = listener_id
        if name is not None:
            self.name = name
        if position is not None:
            self.position = position
        if priority is not None:
            self.priority = priority
        if project_id is not None:
            self.project_id = project_id
        if redirect_listener_id is not None:
            self.redirect_listener_id = redirect_listener_id
        if redirect_pool_id is not None:
            self.redirect_pool_id = redirect_pool_id
        if redirect_pools_config is not None:
            self.redirect_pools_config = redirect_pools_config
        if redirect_url is not None:
            self.redirect_url = redirect_url
        if redirect_url_config is not None:
            self.redirect_url_config = redirect_url_config
        if fixed_response_config is not None:
            self.fixed_response_config = fixed_response_config
        if rules is not None:
            self.rules = rules

    @property
    def action(self):
        """Gets the action of this CreateL7PolicyOption.

        :return: The action of this CreateL7PolicyOption.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this CreateL7PolicyOption.

        :param action: The action of this CreateL7PolicyOption.
        :type action: str
        """
        self._action = action

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this CreateL7PolicyOption.

        :return: The admin_state_up of this CreateL7PolicyOption.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this CreateL7PolicyOption.

        :param admin_state_up: The admin_state_up of this CreateL7PolicyOption.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def description(self):
        """Gets the description of this CreateL7PolicyOption.

        :return: The description of this CreateL7PolicyOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateL7PolicyOption.

        :param description: The description of this CreateL7PolicyOption.
        :type description: str
        """
        self._description = description

    @property
    def listener_id(self):
        """Gets the listener_id of this CreateL7PolicyOption.

        :return: The listener_id of this CreateL7PolicyOption.
        :rtype: str
        """
        return self._listener_id

    @listener_id.setter
    def listener_id(self, listener_id):
        """Sets the listener_id of this CreateL7PolicyOption.

        :param listener_id: The listener_id of this CreateL7PolicyOption.
        :type listener_id: str
        """
        self._listener_id = listener_id

    @property
    def name(self):
        """Gets the name of this CreateL7PolicyOption.

        :return: The name of this CreateL7PolicyOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateL7PolicyOption.

        :param name: The name of this CreateL7PolicyOption.
        :type name: str
        """
        self._name = name

    @property
    def position(self):
        """Gets the position of this CreateL7PolicyOption.

        :return: The position of this CreateL7PolicyOption.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this CreateL7PolicyOption.

        :param position: The position of this CreateL7PolicyOption.
        :type position: int
        """
        self._position = position

    @property
    def priority(self):
        """Gets the priority of this CreateL7PolicyOption.

        :return: The priority of this CreateL7PolicyOption.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this CreateL7PolicyOption.

        :param priority: The priority of this CreateL7PolicyOption.
        :type priority: int
        """
        self._priority = priority

    @property
    def project_id(self):
        """Gets the project_id of this CreateL7PolicyOption.

        :return: The project_id of this CreateL7PolicyOption.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreateL7PolicyOption.

        :param project_id: The project_id of this CreateL7PolicyOption.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def redirect_listener_id(self):
        """Gets the redirect_listener_id of this CreateL7PolicyOption.

        :return: The redirect_listener_id of this CreateL7PolicyOption.
        :rtype: str
        """
        return self._redirect_listener_id

    @redirect_listener_id.setter
    def redirect_listener_id(self, redirect_listener_id):
        """Sets the redirect_listener_id of this CreateL7PolicyOption.

        :param redirect_listener_id: The redirect_listener_id of this CreateL7PolicyOption.
        :type redirect_listener_id: str
        """
        self._redirect_listener_id = redirect_listener_id

    @property
    def redirect_pool_id(self):
        """Gets the redirect_pool_id of this CreateL7PolicyOption.

        :return: The redirect_pool_id of this CreateL7PolicyOption.
        :rtype: str
        """
        return self._redirect_pool_id

    @redirect_pool_id.setter
    def redirect_pool_id(self, redirect_pool_id):
        """Sets the redirect_pool_id of this CreateL7PolicyOption.

        :param redirect_pool_id: The redirect_pool_id of this CreateL7PolicyOption.
        :type redirect_pool_id: str
        """
        self._redirect_pool_id = redirect_pool_id

    @property
    def redirect_pools_config(self):
        """Gets the redirect_pools_config of this CreateL7PolicyOption.

        :return: The redirect_pools_config of this CreateL7PolicyOption.
        :rtype: list[:class:`g42cloudsdkelb.v3.CreateRedirectPoolsConfig`]
        """
        return self._redirect_pools_config

    @redirect_pools_config.setter
    def redirect_pools_config(self, redirect_pools_config):
        """Sets the redirect_pools_config of this CreateL7PolicyOption.

        :param redirect_pools_config: The redirect_pools_config of this CreateL7PolicyOption.
        :type redirect_pools_config: list[:class:`g42cloudsdkelb.v3.CreateRedirectPoolsConfig`]
        """
        self._redirect_pools_config = redirect_pools_config

    @property
    def redirect_url(self):
        """Gets the redirect_url of this CreateL7PolicyOption.

        :return: The redirect_url of this CreateL7PolicyOption.
        :rtype: str
        """
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, redirect_url):
        """Sets the redirect_url of this CreateL7PolicyOption.

        :param redirect_url: The redirect_url of this CreateL7PolicyOption.
        :type redirect_url: str
        """
        self._redirect_url = redirect_url

    @property
    def redirect_url_config(self):
        """Gets the redirect_url_config of this CreateL7PolicyOption.

        :return: The redirect_url_config of this CreateL7PolicyOption.
        :rtype: :class:`g42cloudsdkelb.v3.CreateRedirectUrlConfig`
        """
        return self._redirect_url_config

    @redirect_url_config.setter
    def redirect_url_config(self, redirect_url_config):
        """Sets the redirect_url_config of this CreateL7PolicyOption.

        :param redirect_url_config: The redirect_url_config of this CreateL7PolicyOption.
        :type redirect_url_config: :class:`g42cloudsdkelb.v3.CreateRedirectUrlConfig`
        """
        self._redirect_url_config = redirect_url_config

    @property
    def fixed_response_config(self):
        """Gets the fixed_response_config of this CreateL7PolicyOption.

        :return: The fixed_response_config of this CreateL7PolicyOption.
        :rtype: :class:`g42cloudsdkelb.v3.CreateFixtedResponseConfig`
        """
        return self._fixed_response_config

    @fixed_response_config.setter
    def fixed_response_config(self, fixed_response_config):
        """Sets the fixed_response_config of this CreateL7PolicyOption.

        :param fixed_response_config: The fixed_response_config of this CreateL7PolicyOption.
        :type fixed_response_config: :class:`g42cloudsdkelb.v3.CreateFixtedResponseConfig`
        """
        self._fixed_response_config = fixed_response_config

    @property
    def rules(self):
        """Gets the rules of this CreateL7PolicyOption.

        :return: The rules of this CreateL7PolicyOption.
        :rtype: list[:class:`g42cloudsdkelb.v3.CreateL7PolicyRuleOption`]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this CreateL7PolicyOption.

        :param rules: The rules of this CreateL7PolicyOption.
        :type rules: list[:class:`g42cloudsdkelb.v3.CreateL7PolicyRuleOption`]
        """
        self._rules = rules

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
        if not isinstance(other, CreateL7PolicyOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
