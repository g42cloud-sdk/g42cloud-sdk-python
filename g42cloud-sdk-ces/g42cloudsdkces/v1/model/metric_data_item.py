# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetricDataItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metric': 'MetricInfo',
        'ttl': 'int',
        'collect_time': 'int',
        'value': 'float',
        'unit': 'str',
        'type': 'str'
    }

    attribute_map = {
        'metric': 'metric',
        'ttl': 'ttl',
        'collect_time': 'collect_time',
        'value': 'value',
        'unit': 'unit',
        'type': 'type'
    }

    def __init__(self, metric=None, ttl=None, collect_time=None, value=None, unit=None, type=None):
        """MetricDataItem

        The model defined in g42cloud sdk

        :param metric: The param of the MetricDataItem
        :type metric: :class:`g42cloudsdkces.v1.MetricInfo`
        :param ttl: The param of the MetricDataItem
        :type ttl: int
        :param collect_time: The param of the MetricDataItem
        :type collect_time: int
        :param value: The param of the MetricDataItem
        :type value: float
        :param unit: The param of the MetricDataItem
        :type unit: str
        :param type: The param of the MetricDataItem
        :type type: str
        """
        
        

        self._metric = None
        self._ttl = None
        self._collect_time = None
        self._value = None
        self._unit = None
        self._type = None
        self.discriminator = None

        self.metric = metric
        self.ttl = ttl
        self.collect_time = collect_time
        self.value = value
        if unit is not None:
            self.unit = unit
        if type is not None:
            self.type = type

    @property
    def metric(self):
        """Gets the metric of this MetricDataItem.

        :return: The metric of this MetricDataItem.
        :rtype: :class:`g42cloudsdkces.v1.MetricInfo`
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this MetricDataItem.

        :param metric: The metric of this MetricDataItem.
        :type metric: :class:`g42cloudsdkces.v1.MetricInfo`
        """
        self._metric = metric

    @property
    def ttl(self):
        """Gets the ttl of this MetricDataItem.

        :return: The ttl of this MetricDataItem.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this MetricDataItem.

        :param ttl: The ttl of this MetricDataItem.
        :type ttl: int
        """
        self._ttl = ttl

    @property
    def collect_time(self):
        """Gets the collect_time of this MetricDataItem.

        :return: The collect_time of this MetricDataItem.
        :rtype: int
        """
        return self._collect_time

    @collect_time.setter
    def collect_time(self, collect_time):
        """Sets the collect_time of this MetricDataItem.

        :param collect_time: The collect_time of this MetricDataItem.
        :type collect_time: int
        """
        self._collect_time = collect_time

    @property
    def value(self):
        """Gets the value of this MetricDataItem.

        :return: The value of this MetricDataItem.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this MetricDataItem.

        :param value: The value of this MetricDataItem.
        :type value: float
        """
        self._value = value

    @property
    def unit(self):
        """Gets the unit of this MetricDataItem.

        :return: The unit of this MetricDataItem.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this MetricDataItem.

        :param unit: The unit of this MetricDataItem.
        :type unit: str
        """
        self._unit = unit

    @property
    def type(self):
        """Gets the type of this MetricDataItem.

        :return: The type of this MetricDataItem.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MetricDataItem.

        :param type: The type of this MetricDataItem.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, MetricDataItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
