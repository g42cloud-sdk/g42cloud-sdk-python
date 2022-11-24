# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodePoolNodeAutoscaling:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable': 'bool',
        'min_node_count': 'int',
        'max_node_count': 'int',
        'scale_down_cooldown_time': 'int',
        'priority': 'int'
    }

    attribute_map = {
        'enable': 'enable',
        'min_node_count': 'minNodeCount',
        'max_node_count': 'maxNodeCount',
        'scale_down_cooldown_time': 'scaleDownCooldownTime',
        'priority': 'priority'
    }

    def __init__(self, enable=None, min_node_count=None, max_node_count=None, scale_down_cooldown_time=None, priority=None):
        """NodePoolNodeAutoscaling

        The model defined in g42cloud sdk

        :param enable: The param of the NodePoolNodeAutoscaling
        :type enable: bool
        :param min_node_count: The param of the NodePoolNodeAutoscaling
        :type min_node_count: int
        :param max_node_count: The param of the NodePoolNodeAutoscaling
        :type max_node_count: int
        :param scale_down_cooldown_time: The param of the NodePoolNodeAutoscaling
        :type scale_down_cooldown_time: int
        :param priority: The param of the NodePoolNodeAutoscaling
        :type priority: int
        """
        
        

        self._enable = None
        self._min_node_count = None
        self._max_node_count = None
        self._scale_down_cooldown_time = None
        self._priority = None
        self.discriminator = None

        if enable is not None:
            self.enable = enable
        if min_node_count is not None:
            self.min_node_count = min_node_count
        if max_node_count is not None:
            self.max_node_count = max_node_count
        if scale_down_cooldown_time is not None:
            self.scale_down_cooldown_time = scale_down_cooldown_time
        if priority is not None:
            self.priority = priority

    @property
    def enable(self):
        """Gets the enable of this NodePoolNodeAutoscaling.

        :return: The enable of this NodePoolNodeAutoscaling.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this NodePoolNodeAutoscaling.

        :param enable: The enable of this NodePoolNodeAutoscaling.
        :type enable: bool
        """
        self._enable = enable

    @property
    def min_node_count(self):
        """Gets the min_node_count of this NodePoolNodeAutoscaling.

        :return: The min_node_count of this NodePoolNodeAutoscaling.
        :rtype: int
        """
        return self._min_node_count

    @min_node_count.setter
    def min_node_count(self, min_node_count):
        """Sets the min_node_count of this NodePoolNodeAutoscaling.

        :param min_node_count: The min_node_count of this NodePoolNodeAutoscaling.
        :type min_node_count: int
        """
        self._min_node_count = min_node_count

    @property
    def max_node_count(self):
        """Gets the max_node_count of this NodePoolNodeAutoscaling.

        :return: The max_node_count of this NodePoolNodeAutoscaling.
        :rtype: int
        """
        return self._max_node_count

    @max_node_count.setter
    def max_node_count(self, max_node_count):
        """Sets the max_node_count of this NodePoolNodeAutoscaling.

        :param max_node_count: The max_node_count of this NodePoolNodeAutoscaling.
        :type max_node_count: int
        """
        self._max_node_count = max_node_count

    @property
    def scale_down_cooldown_time(self):
        """Gets the scale_down_cooldown_time of this NodePoolNodeAutoscaling.

        :return: The scale_down_cooldown_time of this NodePoolNodeAutoscaling.
        :rtype: int
        """
        return self._scale_down_cooldown_time

    @scale_down_cooldown_time.setter
    def scale_down_cooldown_time(self, scale_down_cooldown_time):
        """Sets the scale_down_cooldown_time of this NodePoolNodeAutoscaling.

        :param scale_down_cooldown_time: The scale_down_cooldown_time of this NodePoolNodeAutoscaling.
        :type scale_down_cooldown_time: int
        """
        self._scale_down_cooldown_time = scale_down_cooldown_time

    @property
    def priority(self):
        """Gets the priority of this NodePoolNodeAutoscaling.

        :return: The priority of this NodePoolNodeAutoscaling.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this NodePoolNodeAutoscaling.

        :param priority: The priority of this NodePoolNodeAutoscaling.
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
        if not isinstance(other, NodePoolNodeAutoscaling):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
