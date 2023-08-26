# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchListMetricDataRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metrics': 'list[MetricInfo]',
        'period': 'str',
        'filter': 'str',
        '_from': 'int',
        'to': 'int'
    }

    attribute_map = {
        'metrics': 'metrics',
        'period': 'period',
        'filter': 'filter',
        '_from': 'from',
        'to': 'to'
    }

    def __init__(self, metrics=None, period=None, filter=None, _from=None, to=None):
        """BatchListMetricDataRequestBody

        The model defined in g42cloud sdk

        :param metrics: The param of the BatchListMetricDataRequestBody
        :type metrics: list[:class:`g42cloudsdkces.v1.MetricInfo`]
        :param period: The param of the BatchListMetricDataRequestBody
        :type period: str
        :param filter: The param of the BatchListMetricDataRequestBody
        :type filter: str
        :param _from: The param of the BatchListMetricDataRequestBody
        :type _from: int
        :param to: The param of the BatchListMetricDataRequestBody
        :type to: int
        """
        
        

        self._metrics = None
        self._period = None
        self._filter = None
        self.__from = None
        self._to = None
        self.discriminator = None

        self.metrics = metrics
        self.period = period
        self.filter = filter
        self._from = _from
        self.to = to

    @property
    def metrics(self):
        """Gets the metrics of this BatchListMetricDataRequestBody.

        :return: The metrics of this BatchListMetricDataRequestBody.
        :rtype: list[:class:`g42cloudsdkces.v1.MetricInfo`]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this BatchListMetricDataRequestBody.

        :param metrics: The metrics of this BatchListMetricDataRequestBody.
        :type metrics: list[:class:`g42cloudsdkces.v1.MetricInfo`]
        """
        self._metrics = metrics

    @property
    def period(self):
        """Gets the period of this BatchListMetricDataRequestBody.

        :return: The period of this BatchListMetricDataRequestBody.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this BatchListMetricDataRequestBody.

        :param period: The period of this BatchListMetricDataRequestBody.
        :type period: str
        """
        self._period = period

    @property
    def filter(self):
        """Gets the filter of this BatchListMetricDataRequestBody.

        :return: The filter of this BatchListMetricDataRequestBody.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this BatchListMetricDataRequestBody.

        :param filter: The filter of this BatchListMetricDataRequestBody.
        :type filter: str
        """
        self._filter = filter

    @property
    def _from(self):
        """Gets the _from of this BatchListMetricDataRequestBody.

        :return: The _from of this BatchListMetricDataRequestBody.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this BatchListMetricDataRequestBody.

        :param _from: The _from of this BatchListMetricDataRequestBody.
        :type _from: int
        """
        self.__from = _from

    @property
    def to(self):
        """Gets the to of this BatchListMetricDataRequestBody.

        :return: The to of this BatchListMetricDataRequestBody.
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this BatchListMetricDataRequestBody.

        :param to: The to of this BatchListMetricDataRequestBody.
        :type to: int
        """
        self._to = to

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
        if not isinstance(other, BatchListMetricDataRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
