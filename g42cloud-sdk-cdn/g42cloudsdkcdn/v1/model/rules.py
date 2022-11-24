# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Rules:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule_type': 'int',
        'content': 'str',
        'ttl': 'int',
        'ttl_type': 'int',
        'priority': 'int'
    }

    attribute_map = {
        'rule_type': 'rule_type',
        'content': 'content',
        'ttl': 'ttl',
        'ttl_type': 'ttl_type',
        'priority': 'priority'
    }

    def __init__(self, rule_type=None, content=None, ttl=None, ttl_type=None, priority=None):
        """Rules

        The model defined in g42cloud sdk

        :param rule_type: The param of the Rules
        :type rule_type: int
        :param content: The param of the Rules
        :type content: str
        :param ttl: The param of the Rules
        :type ttl: int
        :param ttl_type: The param of the Rules
        :type ttl_type: int
        :param priority: The param of the Rules
        :type priority: int
        """
        
        

        self._rule_type = None
        self._content = None
        self._ttl = None
        self._ttl_type = None
        self._priority = None
        self.discriminator = None

        self.rule_type = rule_type
        if content is not None:
            self.content = content
        self.ttl = ttl
        self.ttl_type = ttl_type
        self.priority = priority

    @property
    def rule_type(self):
        """Gets the rule_type of this Rules.

        :return: The rule_type of this Rules.
        :rtype: int
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        """Sets the rule_type of this Rules.

        :param rule_type: The rule_type of this Rules.
        :type rule_type: int
        """
        self._rule_type = rule_type

    @property
    def content(self):
        """Gets the content of this Rules.

        :return: The content of this Rules.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this Rules.

        :param content: The content of this Rules.
        :type content: str
        """
        self._content = content

    @property
    def ttl(self):
        """Gets the ttl of this Rules.

        :return: The ttl of this Rules.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this Rules.

        :param ttl: The ttl of this Rules.
        :type ttl: int
        """
        self._ttl = ttl

    @property
    def ttl_type(self):
        """Gets the ttl_type of this Rules.

        :return: The ttl_type of this Rules.
        :rtype: int
        """
        return self._ttl_type

    @ttl_type.setter
    def ttl_type(self, ttl_type):
        """Sets the ttl_type of this Rules.

        :param ttl_type: The ttl_type of this Rules.
        :type ttl_type: int
        """
        self._ttl_type = ttl_type

    @property
    def priority(self):
        """Gets the priority of this Rules.

        :return: The priority of this Rules.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this Rules.

        :param priority: The priority of this Rules.
        :type priority: int
        """
        self._priority = priority

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
        if not isinstance(other, Rules):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
