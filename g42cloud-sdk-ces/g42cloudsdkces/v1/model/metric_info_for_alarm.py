# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetricInfoForAlarm:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'namespace': 'str',
        'metric_name': 'str',
        'dimensions': 'list[MetricsDimension]',
        'resource_group_id': 'str',
        'resource_group_name': 'str'
    }

    attribute_map = {
        'namespace': 'namespace',
        'metric_name': 'metric_name',
        'dimensions': 'dimensions',
        'resource_group_id': 'resource_group_id',
        'resource_group_name': 'resource_group_name'
    }

    def __init__(self, namespace=None, metric_name=None, dimensions=None, resource_group_id=None, resource_group_name=None):
        """MetricInfoForAlarm

        The model defined in g42cloud sdk

        :param namespace: The param of the MetricInfoForAlarm
        :type namespace: str
        :param metric_name: The param of the MetricInfoForAlarm
        :type metric_name: str
        :param dimensions: The param of the MetricInfoForAlarm
        :type dimensions: list[:class:`g42cloudsdkces.v1.MetricsDimension`]
        :param resource_group_id: The param of the MetricInfoForAlarm
        :type resource_group_id: str
        :param resource_group_name: The param of the MetricInfoForAlarm
        :type resource_group_name: str
        """
        
        

        self._namespace = None
        self._metric_name = None
        self._dimensions = None
        self._resource_group_id = None
        self._resource_group_name = None
        self.discriminator = None

        self.namespace = namespace
        self.metric_name = metric_name
        self.dimensions = dimensions
        if resource_group_id is not None:
            self.resource_group_id = resource_group_id
        if resource_group_name is not None:
            self.resource_group_name = resource_group_name

    @property
    def namespace(self):
        """Gets the namespace of this MetricInfoForAlarm.

        :return: The namespace of this MetricInfoForAlarm.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this MetricInfoForAlarm.

        :param namespace: The namespace of this MetricInfoForAlarm.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def metric_name(self):
        """Gets the metric_name of this MetricInfoForAlarm.

        :return: The metric_name of this MetricInfoForAlarm.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this MetricInfoForAlarm.

        :param metric_name: The metric_name of this MetricInfoForAlarm.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def dimensions(self):
        """Gets the dimensions of this MetricInfoForAlarm.

        :return: The dimensions of this MetricInfoForAlarm.
        :rtype: list[:class:`g42cloudsdkces.v1.MetricsDimension`]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """Sets the dimensions of this MetricInfoForAlarm.

        :param dimensions: The dimensions of this MetricInfoForAlarm.
        :type dimensions: list[:class:`g42cloudsdkces.v1.MetricsDimension`]
        """
        self._dimensions = dimensions

    @property
    def resource_group_id(self):
        """Gets the resource_group_id of this MetricInfoForAlarm.

        :return: The resource_group_id of this MetricInfoForAlarm.
        :rtype: str
        """
        return self._resource_group_id

    @resource_group_id.setter
    def resource_group_id(self, resource_group_id):
        """Sets the resource_group_id of this MetricInfoForAlarm.

        :param resource_group_id: The resource_group_id of this MetricInfoForAlarm.
        :type resource_group_id: str
        """
        self._resource_group_id = resource_group_id

    @property
    def resource_group_name(self):
        """Gets the resource_group_name of this MetricInfoForAlarm.

        :return: The resource_group_name of this MetricInfoForAlarm.
        :rtype: str
        """
        return self._resource_group_name

    @resource_group_name.setter
    def resource_group_name(self, resource_group_name):
        """Sets the resource_group_name of this MetricInfoForAlarm.

        :param resource_group_name: The resource_group_name of this MetricInfoForAlarm.
        :type resource_group_name: str
        """
        self._resource_group_name = resource_group_name

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
        if not isinstance(other, MetricInfoForAlarm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
