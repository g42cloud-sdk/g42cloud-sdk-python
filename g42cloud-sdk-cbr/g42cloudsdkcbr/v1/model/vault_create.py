# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class VaultCreate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'backup_policy_id': 'str',
        'billing': 'BillingCreate',
        'description': 'str',
        'name': 'str',
        'resources': 'list[ResourceCreate]',
        'tags': 'list[Tag]',
        'enterprise_project_id': 'str',
        'auto_bind': 'bool',
        'bind_rules': 'VaultBindRules',
        'auto_expand': 'bool'
    }

    attribute_map = {
        'backup_policy_id': 'backup_policy_id',
        'billing': 'billing',
        'description': 'description',
        'name': 'name',
        'resources': 'resources',
        'tags': 'tags',
        'enterprise_project_id': 'enterprise_project_id',
        'auto_bind': 'auto_bind',
        'bind_rules': 'bind_rules',
        'auto_expand': 'auto_expand'
    }

    def __init__(self, backup_policy_id=None, billing=None, description=None, name=None, resources=None, tags=None, enterprise_project_id=None, auto_bind=None, bind_rules=None, auto_expand=None):
        """VaultCreate

        The model defined in g42cloud sdk

        :param backup_policy_id: The param of the VaultCreate
        :type backup_policy_id: str
        :param billing: The param of the VaultCreate
        :type billing: :class:`g42cloudsdkcbr.v1.BillingCreate`
        :param description: The param of the VaultCreate
        :type description: str
        :param name: The param of the VaultCreate
        :type name: str
        :param resources: The param of the VaultCreate
        :type resources: list[:class:`g42cloudsdkcbr.v1.ResourceCreate`]
        :param tags: The param of the VaultCreate
        :type tags: list[:class:`g42cloudsdkcbr.v1.Tag`]
        :param enterprise_project_id: The param of the VaultCreate
        :type enterprise_project_id: str
        :param auto_bind: The param of the VaultCreate
        :type auto_bind: bool
        :param bind_rules: The param of the VaultCreate
        :type bind_rules: :class:`g42cloudsdkcbr.v1.VaultBindRules`
        :param auto_expand: The param of the VaultCreate
        :type auto_expand: bool
        """
        
        

        self._backup_policy_id = None
        self._billing = None
        self._description = None
        self._name = None
        self._resources = None
        self._tags = None
        self._enterprise_project_id = None
        self._auto_bind = None
        self._bind_rules = None
        self._auto_expand = None
        self.discriminator = None

        if backup_policy_id is not None:
            self.backup_policy_id = backup_policy_id
        self.billing = billing
        if description is not None:
            self.description = description
        self.name = name
        self.resources = resources
        if tags is not None:
            self.tags = tags
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if auto_bind is not None:
            self.auto_bind = auto_bind
        if bind_rules is not None:
            self.bind_rules = bind_rules
        if auto_expand is not None:
            self.auto_expand = auto_expand

    @property
    def backup_policy_id(self):
        """Gets the backup_policy_id of this VaultCreate.

        :return: The backup_policy_id of this VaultCreate.
        :rtype: str
        """
        return self._backup_policy_id

    @backup_policy_id.setter
    def backup_policy_id(self, backup_policy_id):
        """Sets the backup_policy_id of this VaultCreate.

        :param backup_policy_id: The backup_policy_id of this VaultCreate.
        :type backup_policy_id: str
        """
        self._backup_policy_id = backup_policy_id

    @property
    def billing(self):
        """Gets the billing of this VaultCreate.

        :return: The billing of this VaultCreate.
        :rtype: :class:`g42cloudsdkcbr.v1.BillingCreate`
        """
        return self._billing

    @billing.setter
    def billing(self, billing):
        """Sets the billing of this VaultCreate.

        :param billing: The billing of this VaultCreate.
        :type billing: :class:`g42cloudsdkcbr.v1.BillingCreate`
        """
        self._billing = billing

    @property
    def description(self):
        """Gets the description of this VaultCreate.

        :return: The description of this VaultCreate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VaultCreate.

        :param description: The description of this VaultCreate.
        :type description: str
        """
        self._description = description

    @property
    def name(self):
        """Gets the name of this VaultCreate.

        :return: The name of this VaultCreate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VaultCreate.

        :param name: The name of this VaultCreate.
        :type name: str
        """
        self._name = name

    @property
    def resources(self):
        """Gets the resources of this VaultCreate.

        :return: The resources of this VaultCreate.
        :rtype: list[:class:`g42cloudsdkcbr.v1.ResourceCreate`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this VaultCreate.

        :param resources: The resources of this VaultCreate.
        :type resources: list[:class:`g42cloudsdkcbr.v1.ResourceCreate`]
        """
        self._resources = resources

    @property
    def tags(self):
        """Gets the tags of this VaultCreate.

        :return: The tags of this VaultCreate.
        :rtype: list[:class:`g42cloudsdkcbr.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this VaultCreate.

        :param tags: The tags of this VaultCreate.
        :type tags: list[:class:`g42cloudsdkcbr.v1.Tag`]
        """
        self._tags = tags

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this VaultCreate.

        :return: The enterprise_project_id of this VaultCreate.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this VaultCreate.

        :param enterprise_project_id: The enterprise_project_id of this VaultCreate.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def auto_bind(self):
        """Gets the auto_bind of this VaultCreate.

        :return: The auto_bind of this VaultCreate.
        :rtype: bool
        """
        return self._auto_bind

    @auto_bind.setter
    def auto_bind(self, auto_bind):
        """Sets the auto_bind of this VaultCreate.

        :param auto_bind: The auto_bind of this VaultCreate.
        :type auto_bind: bool
        """
        self._auto_bind = auto_bind

    @property
    def bind_rules(self):
        """Gets the bind_rules of this VaultCreate.

        :return: The bind_rules of this VaultCreate.
        :rtype: :class:`g42cloudsdkcbr.v1.VaultBindRules`
        """
        return self._bind_rules

    @bind_rules.setter
    def bind_rules(self, bind_rules):
        """Sets the bind_rules of this VaultCreate.

        :param bind_rules: The bind_rules of this VaultCreate.
        :type bind_rules: :class:`g42cloudsdkcbr.v1.VaultBindRules`
        """
        self._bind_rules = bind_rules

    @property
    def auto_expand(self):
        """Gets the auto_expand of this VaultCreate.

        :return: The auto_expand of this VaultCreate.
        :rtype: bool
        """
        return self._auto_expand

    @auto_expand.setter
    def auto_expand(self, auto_expand):
        """Sets the auto_expand of this VaultCreate.

        :param auto_expand: The auto_expand of this VaultCreate.
        :type auto_expand: bool
        """
        self._auto_expand = auto_expand

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
        if not isinstance(other, VaultCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
