# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdatePriorityRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'priority': 'int'
    }

    attribute_map = {
        'id': 'id',
        'priority': 'priority'
    }

    def __init__(self, id=None, priority=None):
        """BatchUpdatePriorityRequestBody

        The model defined in g42cloud sdk

        :param id: The param of the BatchUpdatePriorityRequestBody
        :type id: str
        :param priority: The param of the BatchUpdatePriorityRequestBody
        :type priority: int
        """
        
        

        self._id = None
        self._priority = None
        self.discriminator = None

        self.id = id
        self.priority = priority

    @property
    def id(self):
        """Gets the id of this BatchUpdatePriorityRequestBody.

        :return: The id of this BatchUpdatePriorityRequestBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BatchUpdatePriorityRequestBody.

        :param id: The id of this BatchUpdatePriorityRequestBody.
        :type id: str
        """
        self._id = id

    @property
    def priority(self):
        """Gets the priority of this BatchUpdatePriorityRequestBody.

        :return: The priority of this BatchUpdatePriorityRequestBody.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this BatchUpdatePriorityRequestBody.

        :param priority: The priority of this BatchUpdatePriorityRequestBody.
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
        if not isinstance(other, BatchUpdatePriorityRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
