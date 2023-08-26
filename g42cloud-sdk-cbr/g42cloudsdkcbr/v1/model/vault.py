# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class Vault:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'billing': 'Billing',
        'description': 'str',
        'id': 'str',
        'name': 'str',
        'project_id': 'str',
        'provider_id': 'str',
        'resources': 'list[ResourceResp]',
        'tags': 'list[Tag]',
        'enterprise_project_id': 'str',
        'auto_bind': 'bool',
        'bind_rules': 'VaultBindRules',
        'user_id': 'str',
        'created_at': 'str',
        'auto_expand': 'bool',
        'smn_notify': 'bool',
        'threshold': 'int'
    }

    attribute_map = {
        'billing': 'billing',
        'description': 'description',
        'id': 'id',
        'name': 'name',
        'project_id': 'project_id',
        'provider_id': 'provider_id',
        'resources': 'resources',
        'tags': 'tags',
        'enterprise_project_id': 'enterprise_project_id',
        'auto_bind': 'auto_bind',
        'bind_rules': 'bind_rules',
        'user_id': 'user_id',
        'created_at': 'created_at',
        'auto_expand': 'auto_expand',
        'smn_notify': 'smn_notify',
        'threshold': 'threshold'
    }

    def __init__(self, billing=None, description=None, id=None, name=None, project_id=None, provider_id=None, resources=None, tags=None, enterprise_project_id=None, auto_bind=None, bind_rules=None, user_id=None, created_at=None, auto_expand=None, smn_notify=None, threshold=None):
        """Vault

        The model defined in g42cloud sdk

        :param billing: The param of the Vault
        :type billing: :class:`g42cloudsdkcbr.v1.Billing`
        :param description: The param of the Vault
        :type description: str
        :param id: The param of the Vault
        :type id: str
        :param name: The param of the Vault
        :type name: str
        :param project_id: The param of the Vault
        :type project_id: str
        :param provider_id: The param of the Vault
        :type provider_id: str
        :param resources: The param of the Vault
        :type resources: list[:class:`g42cloudsdkcbr.v1.ResourceResp`]
        :param tags: The param of the Vault
        :type tags: list[:class:`g42cloudsdkcbr.v1.Tag`]
        :param enterprise_project_id: The param of the Vault
        :type enterprise_project_id: str
        :param auto_bind: The param of the Vault
        :type auto_bind: bool
        :param bind_rules: The param of the Vault
        :type bind_rules: :class:`g42cloudsdkcbr.v1.VaultBindRules`
        :param user_id: The param of the Vault
        :type user_id: str
        :param created_at: The param of the Vault
        :type created_at: str
        :param auto_expand: The param of the Vault
        :type auto_expand: bool
        :param smn_notify: The param of the Vault
        :type smn_notify: bool
        :param threshold: The param of the Vault
        :type threshold: int
        """
        
        

        self._billing = None
        self._description = None
        self._id = None
        self._name = None
        self._project_id = None
        self._provider_id = None
        self._resources = None
        self._tags = None
        self._enterprise_project_id = None
        self._auto_bind = None
        self._bind_rules = None
        self._user_id = None
        self._created_at = None
        self._auto_expand = None
        self._smn_notify = None
        self._threshold = None
        self.discriminator = None

        self.billing = billing
        if description is not None:
            self.description = description
        self.id = id
        self.name = name
        self.project_id = project_id
        self.provider_id = provider_id
        self.resources = resources
        if tags is not None:
            self.tags = tags
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if auto_bind is not None:
            self.auto_bind = auto_bind
        if bind_rules is not None:
            self.bind_rules = bind_rules
        if user_id is not None:
            self.user_id = user_id
        if created_at is not None:
            self.created_at = created_at
        if auto_expand is not None:
            self.auto_expand = auto_expand
        if smn_notify is not None:
            self.smn_notify = smn_notify
        if threshold is not None:
            self.threshold = threshold

    @property
    def billing(self):
        """Gets the billing of this Vault.

        :return: The billing of this Vault.
        :rtype: :class:`g42cloudsdkcbr.v1.Billing`
        """
        return self._billing

    @billing.setter
    def billing(self, billing):
        """Sets the billing of this Vault.

        :param billing: The billing of this Vault.
        :type billing: :class:`g42cloudsdkcbr.v1.Billing`
        """
        self._billing = billing

    @property
    def description(self):
        """Gets the description of this Vault.

        :return: The description of this Vault.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Vault.

        :param description: The description of this Vault.
        :type description: str
        """
        self._description = description

    @property
    def id(self):
        """Gets the id of this Vault.

        :return: The id of this Vault.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Vault.

        :param id: The id of this Vault.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this Vault.

        :return: The name of this Vault.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Vault.

        :param name: The name of this Vault.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        """Gets the project_id of this Vault.

        :return: The project_id of this Vault.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Vault.

        :param project_id: The project_id of this Vault.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def provider_id(self):
        """Gets the provider_id of this Vault.

        :return: The provider_id of this Vault.
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        """Sets the provider_id of this Vault.

        :param provider_id: The provider_id of this Vault.
        :type provider_id: str
        """
        self._provider_id = provider_id

    @property
    def resources(self):
        """Gets the resources of this Vault.

        :return: The resources of this Vault.
        :rtype: list[:class:`g42cloudsdkcbr.v1.ResourceResp`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this Vault.

        :param resources: The resources of this Vault.
        :type resources: list[:class:`g42cloudsdkcbr.v1.ResourceResp`]
        """
        self._resources = resources

    @property
    def tags(self):
        """Gets the tags of this Vault.

        :return: The tags of this Vault.
        :rtype: list[:class:`g42cloudsdkcbr.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Vault.

        :param tags: The tags of this Vault.
        :type tags: list[:class:`g42cloudsdkcbr.v1.Tag`]
        """
        self._tags = tags

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this Vault.

        :return: The enterprise_project_id of this Vault.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this Vault.

        :param enterprise_project_id: The enterprise_project_id of this Vault.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def auto_bind(self):
        """Gets the auto_bind of this Vault.

        :return: The auto_bind of this Vault.
        :rtype: bool
        """
        return self._auto_bind

    @auto_bind.setter
    def auto_bind(self, auto_bind):
        """Sets the auto_bind of this Vault.

        :param auto_bind: The auto_bind of this Vault.
        :type auto_bind: bool
        """
        self._auto_bind = auto_bind

    @property
    def bind_rules(self):
        """Gets the bind_rules of this Vault.

        :return: The bind_rules of this Vault.
        :rtype: :class:`g42cloudsdkcbr.v1.VaultBindRules`
        """
        return self._bind_rules

    @bind_rules.setter
    def bind_rules(self, bind_rules):
        """Sets the bind_rules of this Vault.

        :param bind_rules: The bind_rules of this Vault.
        :type bind_rules: :class:`g42cloudsdkcbr.v1.VaultBindRules`
        """
        self._bind_rules = bind_rules

    @property
    def user_id(self):
        """Gets the user_id of this Vault.

        :return: The user_id of this Vault.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this Vault.

        :param user_id: The user_id of this Vault.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def created_at(self):
        """Gets the created_at of this Vault.

        :return: The created_at of this Vault.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Vault.

        :param created_at: The created_at of this Vault.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def auto_expand(self):
        """Gets the auto_expand of this Vault.

        :return: The auto_expand of this Vault.
        :rtype: bool
        """
        return self._auto_expand

    @auto_expand.setter
    def auto_expand(self, auto_expand):
        """Sets the auto_expand of this Vault.

        :param auto_expand: The auto_expand of this Vault.
        :type auto_expand: bool
        """
        self._auto_expand = auto_expand

    @property
    def smn_notify(self):
        """Gets the smn_notify of this Vault.

        :return: The smn_notify of this Vault.
        :rtype: bool
        """
        return self._smn_notify

    @smn_notify.setter
    def smn_notify(self, smn_notify):
        """Sets the smn_notify of this Vault.

        :param smn_notify: The smn_notify of this Vault.
        :type smn_notify: bool
        """
        self._smn_notify = smn_notify

    @property
    def threshold(self):
        """Gets the threshold of this Vault.

        :return: The threshold of this Vault.
        :rtype: int
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this Vault.

        :param threshold: The threshold of this Vault.
        :type threshold: int
        """
        self._threshold = threshold

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
        if not isinstance(other, Vault):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
