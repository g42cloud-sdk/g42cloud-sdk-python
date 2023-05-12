# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchMetricData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'unit': 'str',
        'datapoints': 'list[DatapointForBatchMetric]',
        'namespace': 'str',
        'metric_name': 'str',
        'dimensions': 'list[MetricsDimension]'
    }

    attribute_map = {
        'unit': 'unit',
        'datapoints': 'datapoints',
        'namespace': 'namespace',
        'metric_name': 'metric_name',
        'dimensions': 'dimensions'
    }

    def __init__(self, unit=None, datapoints=None, namespace=None, metric_name=None, dimensions=None):
        """BatchMetricData

        The model defined in g42cloud sdk

        :param unit: The param of the BatchMetricData
        :type unit: str
        :param datapoints: The param of the BatchMetricData
        :type datapoints: list[:class:`g42cloudsdkces.v1.DatapointForBatchMetric`]
        :param namespace: The param of the BatchMetricData
        :type namespace: str
        :param metric_name: The param of the BatchMetricData
        :type metric_name: str
        :param dimensions: The param of the BatchMetricData
        :type dimensions: list[:class:`g42cloudsdkces.v1.MetricsDimension`]
        """
        
        

        self._unit = None
        self._datapoints = None
        self._namespace = None
        self._metric_name = None
        self._dimensions = None
        self.discriminator = None

        if unit is not None:
            self.unit = unit
        self.datapoints = datapoints
        if namespace is not None:
            self.namespace = namespace
        self.metric_name = metric_name
        if dimensions is not None:
            self.dimensions = dimensions

    @property
    def unit(self):
        """Gets the unit of this BatchMetricData.

        :return: The unit of this BatchMetricData.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this BatchMetricData.

        :param unit: The unit of this BatchMetricData.
        :type unit: str
        """
        self._unit = unit

    @property
    def datapoints(self):
        """Gets the datapoints of this BatchMetricData.

        :return: The datapoints of this BatchMetricData.
        :rtype: list[:class:`g42cloudsdkces.v1.DatapointForBatchMetric`]
        """
        return self._datapoints

    @datapoints.setter
    def datapoints(self, datapoints):
        """Sets the datapoints of this BatchMetricData.

        :param datapoints: The datapoints of this BatchMetricData.
        :type datapoints: list[:class:`g42cloudsdkces.v1.DatapointForBatchMetric`]
        """
        self._datapoints = datapoints

    @property
    def namespace(self):
        """Gets the namespace of this BatchMetricData.

        :return: The namespace of this BatchMetricData.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this BatchMetricData.

        :param namespace: The namespace of this BatchMetricData.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def metric_name(self):
        """Gets the metric_name of this BatchMetricData.

        :return: The metric_name of this BatchMetricData.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this BatchMetricData.

        :param metric_name: The metric_name of this BatchMetricData.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def dimensions(self):
        """Gets the dimensions of this BatchMetricData.

        :return: The dimensions of this BatchMetricData.
        :rtype: list[:class:`g42cloudsdkces.v1.MetricsDimension`]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """Sets the dimensions of this BatchMetricData.

        :param dimensions: The dimensions of this BatchMetricData.
        :type dimensions: list[:class:`g42cloudsdkces.v1.MetricsDimension`]
        """
        self._dimensions = dimensions

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
        if not isinstance(other, BatchMetricData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
