# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class Datapoint:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'max': 'float',
        'min': 'float',
        'average': 'float',
        'sum': 'float',
        'variance': 'float',
        'timestamp': 'int',
        'unit': 'str'
    }

    attribute_map = {
        'max': 'max',
        'min': 'min',
        'average': 'average',
        'sum': 'sum',
        'variance': 'variance',
        'timestamp': 'timestamp',
        'unit': 'unit'
    }

    def __init__(self, max=None, min=None, average=None, sum=None, variance=None, timestamp=None, unit=None):
        """Datapoint

        The model defined in g42cloud sdk

        :param max: The param of the Datapoint
        :type max: float
        :param min: The param of the Datapoint
        :type min: float
        :param average: The param of the Datapoint
        :type average: float
        :param sum: The param of the Datapoint
        :type sum: float
        :param variance: The param of the Datapoint
        :type variance: float
        :param timestamp: The param of the Datapoint
        :type timestamp: int
        :param unit: The param of the Datapoint
        :type unit: str
        """
        
        

        self._max = None
        self._min = None
        self._average = None
        self._sum = None
        self._variance = None
        self._timestamp = None
        self._unit = None
        self.discriminator = None

        if max is not None:
            self.max = max
        if min is not None:
            self.min = min
        if average is not None:
            self.average = average
        if sum is not None:
            self.sum = sum
        if variance is not None:
            self.variance = variance
        self.timestamp = timestamp
        if unit is not None:
            self.unit = unit

    @property
    def max(self):
        """Gets the max of this Datapoint.

        :return: The max of this Datapoint.
        :rtype: float
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this Datapoint.

        :param max: The max of this Datapoint.
        :type max: float
        """
        self._max = max

    @property
    def min(self):
        """Gets the min of this Datapoint.

        :return: The min of this Datapoint.
        :rtype: float
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this Datapoint.

        :param min: The min of this Datapoint.
        :type min: float
        """
        self._min = min

    @property
    def average(self):
        """Gets the average of this Datapoint.

        :return: The average of this Datapoint.
        :rtype: float
        """
        return self._average

    @average.setter
    def average(self, average):
        """Sets the average of this Datapoint.

        :param average: The average of this Datapoint.
        :type average: float
        """
        self._average = average

    @property
    def sum(self):
        """Gets the sum of this Datapoint.

        :return: The sum of this Datapoint.
        :rtype: float
        """
        return self._sum

    @sum.setter
    def sum(self, sum):
        """Sets the sum of this Datapoint.

        :param sum: The sum of this Datapoint.
        :type sum: float
        """
        self._sum = sum

    @property
    def variance(self):
        """Gets the variance of this Datapoint.

        :return: The variance of this Datapoint.
        :rtype: float
        """
        return self._variance

    @variance.setter
    def variance(self, variance):
        """Sets the variance of this Datapoint.

        :param variance: The variance of this Datapoint.
        :type variance: float
        """
        self._variance = variance

    @property
    def timestamp(self):
        """Gets the timestamp of this Datapoint.

        :return: The timestamp of this Datapoint.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this Datapoint.

        :param timestamp: The timestamp of this Datapoint.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def unit(self):
        """Gets the unit of this Datapoint.

        :return: The unit of this Datapoint.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this Datapoint.

        :param unit: The unit of this Datapoint.
        :type unit: str
        """
        self._unit = unit

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
        if not isinstance(other, Datapoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
