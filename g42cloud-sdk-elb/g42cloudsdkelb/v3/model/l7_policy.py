# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class L7Policy:

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
        'id': 'str',
        'listener_id': 'str',
        'name': 'str',
        'position': 'int',
        'priority': 'int',
        'project_id': 'str',
        'provisioning_status': 'str',
        'redirect_pool_id': 'str',
        'redirect_pools_config': 'list[CreateRedirectPoolsConfig]',
        'redirect_listener_id': 'str',
        'redirect_url': 'str',
        'rules': 'list[RuleRef]',
        'redirect_url_config': 'RedirectUrlConfig',
        'fixed_response_config': 'FixtedResponseConfig',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'action': 'action',
        'admin_state_up': 'admin_state_up',
        'description': 'description',
        'id': 'id',
        'listener_id': 'listener_id',
        'name': 'name',
        'position': 'position',
        'priority': 'priority',
        'project_id': 'project_id',
        'provisioning_status': 'provisioning_status',
        'redirect_pool_id': 'redirect_pool_id',
        'redirect_pools_config': 'redirect_pools_config',
        'redirect_listener_id': 'redirect_listener_id',
        'redirect_url': 'redirect_url',
        'rules': 'rules',
        'redirect_url_config': 'redirect_url_config',
        'fixed_response_config': 'fixed_response_config',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, action=None, admin_state_up=None, description=None, id=None, listener_id=None, name=None, position=None, priority=None, project_id=None, provisioning_status=None, redirect_pool_id=None, redirect_pools_config=None, redirect_listener_id=None, redirect_url=None, rules=None, redirect_url_config=None, fixed_response_config=None, created_at=None, updated_at=None):
        """L7Policy

        The model defined in g42cloud sdk

        :param action: The param of the L7Policy
        :type action: str
        :param admin_state_up: The param of the L7Policy
        :type admin_state_up: bool
        :param description: The param of the L7Policy
        :type description: str
        :param id: The param of the L7Policy
        :type id: str
        :param listener_id: The param of the L7Policy
        :type listener_id: str
        :param name: The param of the L7Policy
        :type name: str
        :param position: The param of the L7Policy
        :type position: int
        :param priority: The param of the L7Policy
        :type priority: int
        :param project_id: The param of the L7Policy
        :type project_id: str
        :param provisioning_status: The param of the L7Policy
        :type provisioning_status: str
        :param redirect_pool_id: The param of the L7Policy
        :type redirect_pool_id: str
        :param redirect_pools_config: The param of the L7Policy
        :type redirect_pools_config: list[:class:`g42cloudsdkelb.v3.CreateRedirectPoolsConfig`]
        :param redirect_listener_id: The param of the L7Policy
        :type redirect_listener_id: str
        :param redirect_url: The param of the L7Policy
        :type redirect_url: str
        :param rules: The param of the L7Policy
        :type rules: list[:class:`g42cloudsdkelb.v3.RuleRef`]
        :param redirect_url_config: The param of the L7Policy
        :type redirect_url_config: :class:`g42cloudsdkelb.v3.RedirectUrlConfig`
        :param fixed_response_config: The param of the L7Policy
        :type fixed_response_config: :class:`g42cloudsdkelb.v3.FixtedResponseConfig`
        :param created_at: The param of the L7Policy
        :type created_at: str
        :param updated_at: The param of the L7Policy
        :type updated_at: str
        """
        
        

        self._action = None
        self._admin_state_up = None
        self._description = None
        self._id = None
        self._listener_id = None
        self._name = None
        self._position = None
        self._priority = None
        self._project_id = None
        self._provisioning_status = None
        self._redirect_pool_id = None
        self._redirect_pools_config = None
        self._redirect_listener_id = None
        self._redirect_url = None
        self._rules = None
        self._redirect_url_config = None
        self._fixed_response_config = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.action = action
        self.admin_state_up = admin_state_up
        self.description = description
        self.id = id
        self.listener_id = listener_id
        self.name = name
        self.position = position
        if priority is not None:
            self.priority = priority
        self.project_id = project_id
        self.provisioning_status = provisioning_status
        self.redirect_pool_id = redirect_pool_id
        self.redirect_pools_config = redirect_pools_config
        self.redirect_listener_id = redirect_listener_id
        self.redirect_url = redirect_url
        self.rules = rules
        self.redirect_url_config = redirect_url_config
        self.fixed_response_config = fixed_response_config
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def action(self):
        """Gets the action of this L7Policy.

        :return: The action of this L7Policy.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this L7Policy.

        :param action: The action of this L7Policy.
        :type action: str
        """
        self._action = action

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this L7Policy.

        :return: The admin_state_up of this L7Policy.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this L7Policy.

        :param admin_state_up: The admin_state_up of this L7Policy.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def description(self):
        """Gets the description of this L7Policy.

        :return: The description of this L7Policy.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this L7Policy.

        :param description: The description of this L7Policy.
        :type description: str
        """
        self._description = description

    @property
    def id(self):
        """Gets the id of this L7Policy.

        :return: The id of this L7Policy.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this L7Policy.

        :param id: The id of this L7Policy.
        :type id: str
        """
        self._id = id

    @property
    def listener_id(self):
        """Gets the listener_id of this L7Policy.

        :return: The listener_id of this L7Policy.
        :rtype: str
        """
        return self._listener_id

    @listener_id.setter
    def listener_id(self, listener_id):
        """Sets the listener_id of this L7Policy.

        :param listener_id: The listener_id of this L7Policy.
        :type listener_id: str
        """
        self._listener_id = listener_id

    @property
    def name(self):
        """Gets the name of this L7Policy.

        :return: The name of this L7Policy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this L7Policy.

        :param name: The name of this L7Policy.
        :type name: str
        """
        self._name = name

    @property
    def position(self):
        """Gets the position of this L7Policy.

        :return: The position of this L7Policy.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this L7Policy.

        :param position: The position of this L7Policy.
        :type position: int
        """
        self._position = position

    @property
    def priority(self):
        """Gets the priority of this L7Policy.

        :return: The priority of this L7Policy.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this L7Policy.

        :param priority: The priority of this L7Policy.
        :type priority: int
        """
        self._priority = priority

    @property
    def project_id(self):
        """Gets the project_id of this L7Policy.

        :return: The project_id of this L7Policy.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this L7Policy.

        :param project_id: The project_id of this L7Policy.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def provisioning_status(self):
        """Gets the provisioning_status of this L7Policy.

        :return: The provisioning_status of this L7Policy.
        :rtype: str
        """
        return self._provisioning_status

    @provisioning_status.setter
    def provisioning_status(self, provisioning_status):
        """Sets the provisioning_status of this L7Policy.

        :param provisioning_status: The provisioning_status of this L7Policy.
        :type provisioning_status: str
        """
        self._provisioning_status = provisioning_status

    @property
    def redirect_pool_id(self):
        """Gets the redirect_pool_id of this L7Policy.

        :return: The redirect_pool_id of this L7Policy.
        :rtype: str
        """
        return self._redirect_pool_id

    @redirect_pool_id.setter
    def redirect_pool_id(self, redirect_pool_id):
        """Sets the redirect_pool_id of this L7Policy.

        :param redirect_pool_id: The redirect_pool_id of this L7Policy.
        :type redirect_pool_id: str
        """
        self._redirect_pool_id = redirect_pool_id

    @property
    def redirect_pools_config(self):
        """Gets the redirect_pools_config of this L7Policy.

        :return: The redirect_pools_config of this L7Policy.
        :rtype: list[:class:`g42cloudsdkelb.v3.CreateRedirectPoolsConfig`]
        """
        return self._redirect_pools_config

    @redirect_pools_config.setter
    def redirect_pools_config(self, redirect_pools_config):
        """Sets the redirect_pools_config of this L7Policy.

        :param redirect_pools_config: The redirect_pools_config of this L7Policy.
        :type redirect_pools_config: list[:class:`g42cloudsdkelb.v3.CreateRedirectPoolsConfig`]
        """
        self._redirect_pools_config = redirect_pools_config

    @property
    def redirect_listener_id(self):
        """Gets the redirect_listener_id of this L7Policy.

        :return: The redirect_listener_id of this L7Policy.
        :rtype: str
        """
        return self._redirect_listener_id

    @redirect_listener_id.setter
    def redirect_listener_id(self, redirect_listener_id):
        """Sets the redirect_listener_id of this L7Policy.

        :param redirect_listener_id: The redirect_listener_id of this L7Policy.
        :type redirect_listener_id: str
        """
        self._redirect_listener_id = redirect_listener_id

    @property
    def redirect_url(self):
        """Gets the redirect_url of this L7Policy.

        :return: The redirect_url of this L7Policy.
        :rtype: str
        """
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, redirect_url):
        """Sets the redirect_url of this L7Policy.

        :param redirect_url: The redirect_url of this L7Policy.
        :type redirect_url: str
        """
        self._redirect_url = redirect_url

    @property
    def rules(self):
        """Gets the rules of this L7Policy.

        :return: The rules of this L7Policy.
        :rtype: list[:class:`g42cloudsdkelb.v3.RuleRef`]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this L7Policy.

        :param rules: The rules of this L7Policy.
        :type rules: list[:class:`g42cloudsdkelb.v3.RuleRef`]
        """
        self._rules = rules

    @property
    def redirect_url_config(self):
        """Gets the redirect_url_config of this L7Policy.

        :return: The redirect_url_config of this L7Policy.
        :rtype: :class:`g42cloudsdkelb.v3.RedirectUrlConfig`
        """
        return self._redirect_url_config

    @redirect_url_config.setter
    def redirect_url_config(self, redirect_url_config):
        """Sets the redirect_url_config of this L7Policy.

        :param redirect_url_config: The redirect_url_config of this L7Policy.
        :type redirect_url_config: :class:`g42cloudsdkelb.v3.RedirectUrlConfig`
        """
        self._redirect_url_config = redirect_url_config

    @property
    def fixed_response_config(self):
        """Gets the fixed_response_config of this L7Policy.

        :return: The fixed_response_config of this L7Policy.
        :rtype: :class:`g42cloudsdkelb.v3.FixtedResponseConfig`
        """
        return self._fixed_response_config

    @fixed_response_config.setter
    def fixed_response_config(self, fixed_response_config):
        """Sets the fixed_response_config of this L7Policy.

        :param fixed_response_config: The fixed_response_config of this L7Policy.
        :type fixed_response_config: :class:`g42cloudsdkelb.v3.FixtedResponseConfig`
        """
        self._fixed_response_config = fixed_response_config

    @property
    def created_at(self):
        """Gets the created_at of this L7Policy.

        :return: The created_at of this L7Policy.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this L7Policy.

        :param created_at: The created_at of this L7Policy.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this L7Policy.

        :return: The updated_at of this L7Policy.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this L7Policy.

        :param updated_at: The updated_at of this L7Policy.
        :type updated_at: str
        """
        self._updated_at = updated_at

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
        if not isinstance(other, L7Policy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
