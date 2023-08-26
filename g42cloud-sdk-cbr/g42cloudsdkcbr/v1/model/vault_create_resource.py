# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class VaultCreateResource:

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
        'threshold': 'int',
        'err_text': 'str',
        'ret_code': 'str',
        'orders': 'list[CbcOrderResult]'
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
        'threshold': 'threshold',
        'err_text': 'errText',
        'ret_code': 'retCode',
        'orders': 'orders'
    }

    def __init__(self, billing=None, description=None, id=None, name=None, project_id=None, provider_id=None, resources=None, tags=None, enterprise_project_id=None, auto_bind=None, bind_rules=None, user_id=None, created_at=None, auto_expand=None, smn_notify=None, threshold=None, err_text=None, ret_code=None, orders=None):
        """VaultCreateResource

        The model defined in g42cloud sdk

        :param billing: The param of the VaultCreateResource
        :type billing: :class:`g42cloudsdkcbr.v1.Billing`
        :param description: The param of the VaultCreateResource
        :type description: str
        :param id: The param of the VaultCreateResource
        :type id: str
        :param name: The param of the VaultCreateResource
        :type name: str
        :param project_id: The param of the VaultCreateResource
        :type project_id: str
        :param provider_id: The param of the VaultCreateResource
        :type provider_id: str
        :param resources: The param of the VaultCreateResource
        :type resources: list[:class:`g42cloudsdkcbr.v1.ResourceResp`]
        :param tags: The param of the VaultCreateResource
        :type tags: list[:class:`g42cloudsdkcbr.v1.Tag`]
        :param enterprise_project_id: The param of the VaultCreateResource
        :type enterprise_project_id: str
        :param auto_bind: The param of the VaultCreateResource
        :type auto_bind: bool
        :param bind_rules: The param of the VaultCreateResource
        :type bind_rules: :class:`g42cloudsdkcbr.v1.VaultBindRules`
        :param user_id: The param of the VaultCreateResource
        :type user_id: str
        :param created_at: The param of the VaultCreateResource
        :type created_at: str
        :param auto_expand: The param of the VaultCreateResource
        :type auto_expand: bool
        :param smn_notify: The param of the VaultCreateResource
        :type smn_notify: bool
        :param threshold: The param of the VaultCreateResource
        :type threshold: int
        :param err_text: The param of the VaultCreateResource
        :type err_text: str
        :param ret_code: The param of the VaultCreateResource
        :type ret_code: str
        :param orders: The param of the VaultCreateResource
        :type orders: list[:class:`g42cloudsdkcbr.v1.CbcOrderResult`]
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
        self._err_text = None
        self._ret_code = None
        self._orders = None
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
        if err_text is not None:
            self.err_text = err_text
        if ret_code is not None:
            self.ret_code = ret_code
        if orders is not None:
            self.orders = orders

    @property
    def billing(self):
        """Gets the billing of this VaultCreateResource.

        :return: The billing of this VaultCreateResource.
        :rtype: :class:`g42cloudsdkcbr.v1.Billing`
        """
        return self._billing

    @billing.setter
    def billing(self, billing):
        """Sets the billing of this VaultCreateResource.

        :param billing: The billing of this VaultCreateResource.
        :type billing: :class:`g42cloudsdkcbr.v1.Billing`
        """
        self._billing = billing

    @property
    def description(self):
        """Gets the description of this VaultCreateResource.

        :return: The description of this VaultCreateResource.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VaultCreateResource.

        :param description: The description of this VaultCreateResource.
        :type description: str
        """
        self._description = description

    @property
    def id(self):
        """Gets the id of this VaultCreateResource.

        :return: The id of this VaultCreateResource.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VaultCreateResource.

        :param id: The id of this VaultCreateResource.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this VaultCreateResource.

        :return: The name of this VaultCreateResource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VaultCreateResource.

        :param name: The name of this VaultCreateResource.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        """Gets the project_id of this VaultCreateResource.

        :return: The project_id of this VaultCreateResource.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this VaultCreateResource.

        :param project_id: The project_id of this VaultCreateResource.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def provider_id(self):
        """Gets the provider_id of this VaultCreateResource.

        :return: The provider_id of this VaultCreateResource.
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        """Sets the provider_id of this VaultCreateResource.

        :param provider_id: The provider_id of this VaultCreateResource.
        :type provider_id: str
        """
        self._provider_id = provider_id

    @property
    def resources(self):
        """Gets the resources of this VaultCreateResource.

        :return: The resources of this VaultCreateResource.
        :rtype: list[:class:`g42cloudsdkcbr.v1.ResourceResp`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this VaultCreateResource.

        :param resources: The resources of this VaultCreateResource.
        :type resources: list[:class:`g42cloudsdkcbr.v1.ResourceResp`]
        """
        self._resources = resources

    @property
    def tags(self):
        """Gets the tags of this VaultCreateResource.

        :return: The tags of this VaultCreateResource.
        :rtype: list[:class:`g42cloudsdkcbr.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this VaultCreateResource.

        :param tags: The tags of this VaultCreateResource.
        :type tags: list[:class:`g42cloudsdkcbr.v1.Tag`]
        """
        self._tags = tags

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this VaultCreateResource.

        :return: The enterprise_project_id of this VaultCreateResource.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this VaultCreateResource.

        :param enterprise_project_id: The enterprise_project_id of this VaultCreateResource.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def auto_bind(self):
        """Gets the auto_bind of this VaultCreateResource.

        :return: The auto_bind of this VaultCreateResource.
        :rtype: bool
        """
        return self._auto_bind

    @auto_bind.setter
    def auto_bind(self, auto_bind):
        """Sets the auto_bind of this VaultCreateResource.

        :param auto_bind: The auto_bind of this VaultCreateResource.
        :type auto_bind: bool
        """
        self._auto_bind = auto_bind

    @property
    def bind_rules(self):
        """Gets the bind_rules of this VaultCreateResource.

        :return: The bind_rules of this VaultCreateResource.
        :rtype: :class:`g42cloudsdkcbr.v1.VaultBindRules`
        """
        return self._bind_rules

    @bind_rules.setter
    def bind_rules(self, bind_rules):
        """Sets the bind_rules of this VaultCreateResource.

        :param bind_rules: The bind_rules of this VaultCreateResource.
        :type bind_rules: :class:`g42cloudsdkcbr.v1.VaultBindRules`
        """
        self._bind_rules = bind_rules

    @property
    def user_id(self):
        """Gets the user_id of this VaultCreateResource.

        :return: The user_id of this VaultCreateResource.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this VaultCreateResource.

        :param user_id: The user_id of this VaultCreateResource.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def created_at(self):
        """Gets the created_at of this VaultCreateResource.

        :return: The created_at of this VaultCreateResource.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this VaultCreateResource.

        :param created_at: The created_at of this VaultCreateResource.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def auto_expand(self):
        """Gets the auto_expand of this VaultCreateResource.

        :return: The auto_expand of this VaultCreateResource.
        :rtype: bool
        """
        return self._auto_expand

    @auto_expand.setter
    def auto_expand(self, auto_expand):
        """Sets the auto_expand of this VaultCreateResource.

        :param auto_expand: The auto_expand of this VaultCreateResource.
        :type auto_expand: bool
        """
        self._auto_expand = auto_expand

    @property
    def smn_notify(self):
        """Gets the smn_notify of this VaultCreateResource.

        :return: The smn_notify of this VaultCreateResource.
        :rtype: bool
        """
        return self._smn_notify

    @smn_notify.setter
    def smn_notify(self, smn_notify):
        """Sets the smn_notify of this VaultCreateResource.

        :param smn_notify: The smn_notify of this VaultCreateResource.
        :type smn_notify: bool
        """
        self._smn_notify = smn_notify

    @property
    def threshold(self):
        """Gets the threshold of this VaultCreateResource.

        :return: The threshold of this VaultCreateResource.
        :rtype: int
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this VaultCreateResource.

        :param threshold: The threshold of this VaultCreateResource.
        :type threshold: int
        """
        self._threshold = threshold

    @property
    def err_text(self):
        """Gets the err_text of this VaultCreateResource.

        :return: The err_text of this VaultCreateResource.
        :rtype: str
        """
        return self._err_text

    @err_text.setter
    def err_text(self, err_text):
        """Sets the err_text of this VaultCreateResource.

        :param err_text: The err_text of this VaultCreateResource.
        :type err_text: str
        """
        self._err_text = err_text

    @property
    def ret_code(self):
        """Gets the ret_code of this VaultCreateResource.

        :return: The ret_code of this VaultCreateResource.
        :rtype: str
        """
        return self._ret_code

    @ret_code.setter
    def ret_code(self, ret_code):
        """Sets the ret_code of this VaultCreateResource.

        :param ret_code: The ret_code of this VaultCreateResource.
        :type ret_code: str
        """
        self._ret_code = ret_code

    @property
    def orders(self):
        """Gets the orders of this VaultCreateResource.

        :return: The orders of this VaultCreateResource.
        :rtype: list[:class:`g42cloudsdkcbr.v1.CbcOrderResult`]
        """
        return self._orders

    @orders.setter
    def orders(self, orders):
        """Sets the orders of this VaultCreateResource.

        :param orders: The orders of this VaultCreateResource.
        :type orders: list[:class:`g42cloudsdkcbr.v1.CbcOrderResult`]
        """
        self._orders = orders

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
        if not isinstance(other, VaultCreateResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
