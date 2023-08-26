# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateL7RuleOption:

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
        'invert': 'bool',
        'key': 'str',
        'value': 'str',
        'conditions': 'list[UpdateRuleCondition]'
    }

    attribute_map = {
        'admin_state_up': 'admin_state_up',
        'compare_type': 'compare_type',
        'invert': 'invert',
        'key': 'key',
        'value': 'value',
        'conditions': 'conditions'
    }

    def __init__(self, admin_state_up=None, compare_type=None, invert=None, key=None, value=None, conditions=None):
        """UpdateL7RuleOption

        The model defined in g42cloud sdk

        :param admin_state_up: The param of the UpdateL7RuleOption
        :type admin_state_up: bool
        :param compare_type: The param of the UpdateL7RuleOption
        :type compare_type: str
        :param invert: The param of the UpdateL7RuleOption
        :type invert: bool
        :param key: The param of the UpdateL7RuleOption
        :type key: str
        :param value: The param of the UpdateL7RuleOption
        :type value: str
        :param conditions: The param of the UpdateL7RuleOption
        :type conditions: list[:class:`g42cloudsdkelb.v3.UpdateRuleCondition`]
        """
        
        

        self._admin_state_up = None
        self._compare_type = None
        self._invert = None
        self._key = None
        self._value = None
        self._conditions = None
        self.discriminator = None

        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if compare_type is not None:
            self.compare_type = compare_type
        if invert is not None:
            self.invert = invert
        if key is not None:
            self.key = key
        if value is not None:
            self.value = value
        if conditions is not None:
            self.conditions = conditions

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this UpdateL7RuleOption.

        :return: The admin_state_up of this UpdateL7RuleOption.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this UpdateL7RuleOption.

        :param admin_state_up: The admin_state_up of this UpdateL7RuleOption.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def compare_type(self):
        """Gets the compare_type of this UpdateL7RuleOption.

        :return: The compare_type of this UpdateL7RuleOption.
        :rtype: str
        """
        return self._compare_type

    @compare_type.setter
    def compare_type(self, compare_type):
        """Sets the compare_type of this UpdateL7RuleOption.

        :param compare_type: The compare_type of this UpdateL7RuleOption.
        :type compare_type: str
        """
        self._compare_type = compare_type

    @property
    def invert(self):
        """Gets the invert of this UpdateL7RuleOption.

        :return: The invert of this UpdateL7RuleOption.
        :rtype: bool
        """
        return self._invert

    @invert.setter
    def invert(self, invert):
        """Sets the invert of this UpdateL7RuleOption.

        :param invert: The invert of this UpdateL7RuleOption.
        :type invert: bool
        """
        self._invert = invert

    @property
    def key(self):
        """Gets the key of this UpdateL7RuleOption.

        :return: The key of this UpdateL7RuleOption.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this UpdateL7RuleOption.

        :param key: The key of this UpdateL7RuleOption.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        """Gets the value of this UpdateL7RuleOption.

        :return: The value of this UpdateL7RuleOption.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this UpdateL7RuleOption.

        :param value: The value of this UpdateL7RuleOption.
        :type value: str
        """
        self._value = value

    @property
    def conditions(self):
        """Gets the conditions of this UpdateL7RuleOption.

        :return: The conditions of this UpdateL7RuleOption.
        :rtype: list[:class:`g42cloudsdkelb.v3.UpdateRuleCondition`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this UpdateL7RuleOption.

        :param conditions: The conditions of this UpdateL7RuleOption.
        :type conditions: list[:class:`g42cloudsdkelb.v3.UpdateRuleCondition`]
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
        if not isinstance(other, UpdateL7RuleOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
