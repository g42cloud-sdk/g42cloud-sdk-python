# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRuleOption:

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
        'compare_type': 'str',
        'key': 'str',
        'value': 'str',
        'project_id': 'str',
        'type': 'str',
        'invert': 'bool',
        'conditions': 'list[CreateRuleCondition]'
    }

    attribute_map = {
        'admin_state_up': 'admin_state_up',
        'compare_type': 'compare_type',
        'key': 'key',
        'value': 'value',
        'project_id': 'project_id',
        'type': 'type',
        'invert': 'invert',
        'conditions': 'conditions'
    }

    def __init__(self, admin_state_up=None, compare_type=None, key=None, value=None, project_id=None, type=None, invert=None, conditions=None):
        """CreateRuleOption

        The model defined in g42cloud sdk

        :param admin_state_up: The param of the CreateRuleOption
        :type admin_state_up: bool
        :param compare_type: The param of the CreateRuleOption
        :type compare_type: str
        :param key: The param of the CreateRuleOption
        :type key: str
        :param value: The param of the CreateRuleOption
        :type value: str
        :param project_id: The param of the CreateRuleOption
        :type project_id: str
        :param type: The param of the CreateRuleOption
        :type type: str
        :param invert: The param of the CreateRuleOption
        :type invert: bool
        :param conditions: The param of the CreateRuleOption
        :type conditions: list[:class:`g42cloudsdkelb.v3.CreateRuleCondition`]
        """
        
        

        self._admin_state_up = None
        self._compare_type = None
        self._key = None
        self._value = None
        self._project_id = None
        self._type = None
        self._invert = None
        self._conditions = None
        self.discriminator = None

        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        self.compare_type = compare_type
        if key is not None:
            self.key = key
        self.value = value
        if project_id is not None:
            self.project_id = project_id
        self.type = type
        if invert is not None:
            self.invert = invert
        if conditions is not None:
            self.conditions = conditions

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this CreateRuleOption.

        :return: The admin_state_up of this CreateRuleOption.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this CreateRuleOption.

        :param admin_state_up: The admin_state_up of this CreateRuleOption.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def compare_type(self):
        """Gets the compare_type of this CreateRuleOption.

        :return: The compare_type of this CreateRuleOption.
        :rtype: str
        """
        return self._compare_type

    @compare_type.setter
    def compare_type(self, compare_type):
        """Sets the compare_type of this CreateRuleOption.

        :param compare_type: The compare_type of this CreateRuleOption.
        :type compare_type: str
        """
        self._compare_type = compare_type

    @property
    def key(self):
        """Gets the key of this CreateRuleOption.

        :return: The key of this CreateRuleOption.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this CreateRuleOption.

        :param key: The key of this CreateRuleOption.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        """Gets the value of this CreateRuleOption.

        :return: The value of this CreateRuleOption.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CreateRuleOption.

        :param value: The value of this CreateRuleOption.
        :type value: str
        """
        self._value = value

    @property
    def project_id(self):
        """Gets the project_id of this CreateRuleOption.

        :return: The project_id of this CreateRuleOption.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreateRuleOption.

        :param project_id: The project_id of this CreateRuleOption.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def type(self):
        """Gets the type of this CreateRuleOption.

        :return: The type of this CreateRuleOption.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateRuleOption.

        :param type: The type of this CreateRuleOption.
        :type type: str
        """
        self._type = type

    @property
    def invert(self):
        """Gets the invert of this CreateRuleOption.

        :return: The invert of this CreateRuleOption.
        :rtype: bool
        """
        return self._invert

    @invert.setter
    def invert(self, invert):
        """Sets the invert of this CreateRuleOption.

        :param invert: The invert of this CreateRuleOption.
        :type invert: bool
        """
        self._invert = invert

    @property
    def conditions(self):
        """Gets the conditions of this CreateRuleOption.

        :return: The conditions of this CreateRuleOption.
        :rtype: list[:class:`g42cloudsdkelb.v3.CreateRuleCondition`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this CreateRuleOption.

        :param conditions: The conditions of this CreateRuleOption.
        :type conditions: list[:class:`g42cloudsdkelb.v3.CreateRuleCondition`]
        """
        self._conditions = conditions

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
        if not isinstance(other, CreateRuleOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
