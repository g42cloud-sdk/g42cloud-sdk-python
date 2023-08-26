# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class Filter:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'condition': 'str',
        'is_support_filter': 'bool',
        'rule': 'list[str]'
    }

    attribute_map = {
        'condition': 'condition',
        'is_support_filter': 'is_support_filter',
        'rule': 'rule'
    }

    def __init__(self, condition=None, is_support_filter=None, rule=None):
        """Filter

        The model defined in g42cloud sdk

        :param condition: The param of the Filter
        :type condition: str
        :param is_support_filter: The param of the Filter
        :type is_support_filter: bool
        :param rule: The param of the Filter
        :type rule: list[str]
        """
        
        

        self._condition = None
        self._is_support_filter = None
        self._rule = None
        self.discriminator = None

        self.condition = condition
        self.is_support_filter = is_support_filter
        self.rule = rule

    @property
    def condition(self):
        """Gets the condition of this Filter.

        :return: The condition of this Filter.
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this Filter.

        :param condition: The condition of this Filter.
        :type condition: str
        """
        self._condition = condition

    @property
    def is_support_filter(self):
        """Gets the is_support_filter of this Filter.

        :return: The is_support_filter of this Filter.
        :rtype: bool
        """
        return self._is_support_filter

    @is_support_filter.setter
    def is_support_filter(self, is_support_filter):
        """Sets the is_support_filter of this Filter.

        :param is_support_filter: The is_support_filter of this Filter.
        :type is_support_filter: bool
        """
        self._is_support_filter = is_support_filter

    @property
    def rule(self):
        """Gets the rule of this Filter.

        :return: The rule of this Filter.
        :rtype: list[str]
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        """Sets the rule of this Filter.

        :param rule: The rule of this Filter.
        :type rule: list[str]
        """
        self._rule = rule

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
        if not isinstance(other, Filter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
