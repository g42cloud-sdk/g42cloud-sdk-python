# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTopicsItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'topic_urn': 'str',
        'name': 'str',
        'display_name': 'str',
        'push_policy': 'int',
        'enterprise_project_id': 'str',
        'topic_id': 'str'
    }

    attribute_map = {
        'topic_urn': 'topic_urn',
        'name': 'name',
        'display_name': 'display_name',
        'push_policy': 'push_policy',
        'enterprise_project_id': 'enterprise_project_id',
        'topic_id': 'topic_id'
    }

    def __init__(self, topic_urn=None, name=None, display_name=None, push_policy=None, enterprise_project_id=None, topic_id=None):
        """ListTopicsItem

        The model defined in g42cloud sdk

        :param topic_urn: The param of the ListTopicsItem
        :type topic_urn: str
        :param name: The param of the ListTopicsItem
        :type name: str
        :param display_name: The param of the ListTopicsItem
        :type display_name: str
        :param push_policy: The param of the ListTopicsItem
        :type push_policy: int
        :param enterprise_project_id: The param of the ListTopicsItem
        :type enterprise_project_id: str
        :param topic_id: The param of the ListTopicsItem
        :type topic_id: str
        """
        
        

        self._topic_urn = None
        self._name = None
        self._display_name = None
        self._push_policy = None
        self._enterprise_project_id = None
        self._topic_id = None
        self.discriminator = None

        self.topic_urn = topic_urn
        self.name = name
        self.display_name = display_name
        self.push_policy = push_policy
        self.enterprise_project_id = enterprise_project_id
        self.topic_id = topic_id

    @property
    def topic_urn(self):
        """Gets the topic_urn of this ListTopicsItem.

        :return: The topic_urn of this ListTopicsItem.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        """Sets the topic_urn of this ListTopicsItem.

        :param topic_urn: The topic_urn of this ListTopicsItem.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

    @property
    def name(self):
        """Gets the name of this ListTopicsItem.

        :return: The name of this ListTopicsItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListTopicsItem.

        :param name: The name of this ListTopicsItem.
        :type name: str
        """
        self._name = name

    @property
    def display_name(self):
        """Gets the display_name of this ListTopicsItem.

        :return: The display_name of this ListTopicsItem.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ListTopicsItem.

        :param display_name: The display_name of this ListTopicsItem.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def push_policy(self):
        """Gets the push_policy of this ListTopicsItem.

        :return: The push_policy of this ListTopicsItem.
        :rtype: int
        """
        return self._push_policy

    @push_policy.setter
    def push_policy(self, push_policy):
        """Sets the push_policy of this ListTopicsItem.

        :param push_policy: The push_policy of this ListTopicsItem.
        :type push_policy: int
        """
        self._push_policy = push_policy

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListTopicsItem.

        :return: The enterprise_project_id of this ListTopicsItem.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListTopicsItem.

        :param enterprise_project_id: The enterprise_project_id of this ListTopicsItem.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def topic_id(self):
        """Gets the topic_id of this ListTopicsItem.

        :return: The topic_id of this ListTopicsItem.
        :rtype: str
        """
        return self._topic_id

    @topic_id.setter
    def topic_id(self, topic_id):
        """Sets the topic_id of this ListTopicsItem.

        :param topic_id: The topic_id of this ListTopicsItem.
        :type topic_id: str
        """
        self._topic_id = topic_id

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
        if not isinstance(other, ListTopicsItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
