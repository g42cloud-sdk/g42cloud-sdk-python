# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodePoolCondition:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'status': 'str',
        'last_probe_time': 'str',
        'last_transit_time': 'str',
        'reason': 'str',
        'message': 'str'
    }

    attribute_map = {
        'type': 'type',
        'status': 'status',
        'last_probe_time': 'lastProbeTime',
        'last_transit_time': 'lastTransitTime',
        'reason': 'reason',
        'message': 'message'
    }

    def __init__(self, type=None, status=None, last_probe_time=None, last_transit_time=None, reason=None, message=None):
        """NodePoolCondition

        The model defined in g42cloud sdk

        :param type: The param of the NodePoolCondition
        :type type: str
        :param status: The param of the NodePoolCondition
        :type status: str
        :param last_probe_time: The param of the NodePoolCondition
        :type last_probe_time: str
        :param last_transit_time: The param of the NodePoolCondition
        :type last_transit_time: str
        :param reason: The param of the NodePoolCondition
        :type reason: str
        :param message: The param of the NodePoolCondition
        :type message: str
        """
        
        

        self._type = None
        self._status = None
        self._last_probe_time = None
        self._last_transit_time = None
        self._reason = None
        self._message = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if last_probe_time is not None:
            self.last_probe_time = last_probe_time
        if last_transit_time is not None:
            self.last_transit_time = last_transit_time
        if reason is not None:
            self.reason = reason
        if message is not None:
            self.message = message

    @property
    def type(self):
        """Gets the type of this NodePoolCondition.

        :return: The type of this NodePoolCondition.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NodePoolCondition.

        :param type: The type of this NodePoolCondition.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        """Gets the status of this NodePoolCondition.

        :return: The status of this NodePoolCondition.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NodePoolCondition.

        :param status: The status of this NodePoolCondition.
        :type status: str
        """
        self._status = status

    @property
    def last_probe_time(self):
        """Gets the last_probe_time of this NodePoolCondition.

        :return: The last_probe_time of this NodePoolCondition.
        :rtype: str
        """
        return self._last_probe_time

    @last_probe_time.setter
    def last_probe_time(self, last_probe_time):
        """Sets the last_probe_time of this NodePoolCondition.

        :param last_probe_time: The last_probe_time of this NodePoolCondition.
        :type last_probe_time: str
        """
        self._last_probe_time = last_probe_time

    @property
    def last_transit_time(self):
        """Gets the last_transit_time of this NodePoolCondition.

        :return: The last_transit_time of this NodePoolCondition.
        :rtype: str
        """
        return self._last_transit_time

    @last_transit_time.setter
    def last_transit_time(self, last_transit_time):
        """Sets the last_transit_time of this NodePoolCondition.

        :param last_transit_time: The last_transit_time of this NodePoolCondition.
        :type last_transit_time: str
        """
        self._last_transit_time = last_transit_time

    @property
    def reason(self):
        """Gets the reason of this NodePoolCondition.

        :return: The reason of this NodePoolCondition.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this NodePoolCondition.

        :param reason: The reason of this NodePoolCondition.
        :type reason: str
        """
        self._reason = reason

    @property
    def message(self):
        """Gets the message of this NodePoolCondition.

        :return: The message of this NodePoolCondition.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this NodePoolCondition.

        :param message: The message of this NodePoolCondition.
        :type message: str
        """
        self._message = message

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
        if not isinstance(other, NodePoolCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
