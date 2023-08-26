# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class TemplateItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metric_name': 'str',
        'condition': 'AlarmTemplateCondition',
        'alarm_level': 'int'
    }

    attribute_map = {
        'metric_name': 'metric_name',
        'condition': 'condition',
        'alarm_level': 'alarm_level'
    }

    def __init__(self, metric_name=None, condition=None, alarm_level=None):
        """TemplateItem

        The model defined in g42cloud sdk

        :param metric_name: The param of the TemplateItem
        :type metric_name: str
        :param condition: The param of the TemplateItem
        :type condition: :class:`g42cloudsdkces.v1.AlarmTemplateCondition`
        :param alarm_level: The param of the TemplateItem
        :type alarm_level: int
        """
        
        

        self._metric_name = None
        self._condition = None
        self._alarm_level = None
        self.discriminator = None

        self.metric_name = metric_name
        self.condition = condition
        if alarm_level is not None:
            self.alarm_level = alarm_level

    @property
    def metric_name(self):
        """Gets the metric_name of this TemplateItem.

        :return: The metric_name of this TemplateItem.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this TemplateItem.

        :param metric_name: The metric_name of this TemplateItem.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def condition(self):
        """Gets the condition of this TemplateItem.

        :return: The condition of this TemplateItem.
        :rtype: :class:`g42cloudsdkces.v1.AlarmTemplateCondition`
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this TemplateItem.

        :param condition: The condition of this TemplateItem.
        :type condition: :class:`g42cloudsdkces.v1.AlarmTemplateCondition`
        """
        self._condition = condition

    @property
    def alarm_level(self):
        """Gets the alarm_level of this TemplateItem.

        :return: The alarm_level of this TemplateItem.
        :rtype: int
        """
        return self._alarm_level

    @alarm_level.setter
    def alarm_level(self, alarm_level):
        """Sets the alarm_level of this TemplateItem.

        :param alarm_level: The alarm_level of this TemplateItem.
        :type alarm_level: int
        """
        self._alarm_level = alarm_level

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
        if not isinstance(other, TemplateItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
