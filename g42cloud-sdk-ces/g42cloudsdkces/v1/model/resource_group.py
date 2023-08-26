# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceGroup:

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
        'dimensions': 'list[MetricsDimension]',
        'status': 'str'
    }

    attribute_map = {
        'namespace': 'namespace',
        'dimensions': 'dimensions',
        'status': 'status'
    }

    def __init__(self, namespace=None, dimensions=None, status=None):
        """ResourceGroup

        The model defined in g42cloud sdk

        :param namespace: The param of the ResourceGroup
        :type namespace: str
        :param dimensions: The param of the ResourceGroup
        :type dimensions: list[:class:`g42cloudsdkces.v1.MetricsDimension`]
        :param status: The param of the ResourceGroup
        :type status: str
        """
        
        

        self._namespace = None
        self._dimensions = None
        self._status = None
        self.discriminator = None

        if namespace is not None:
            self.namespace = namespace
        if dimensions is not None:
            self.dimensions = dimensions
        if status is not None:
            self.status = status

    @property
    def namespace(self):
        """Gets the namespace of this ResourceGroup.

        :return: The namespace of this ResourceGroup.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this ResourceGroup.

        :param namespace: The namespace of this ResourceGroup.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def dimensions(self):
        """Gets the dimensions of this ResourceGroup.

        :return: The dimensions of this ResourceGroup.
        :rtype: list[:class:`g42cloudsdkces.v1.MetricsDimension`]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """Sets the dimensions of this ResourceGroup.

        :param dimensions: The dimensions of this ResourceGroup.
        :type dimensions: list[:class:`g42cloudsdkces.v1.MetricsDimension`]
        """
        self._dimensions = dimensions

    @property
    def status(self):
        """Gets the status of this ResourceGroup.

        :return: The status of this ResourceGroup.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ResourceGroup.

        :param status: The status of this ResourceGroup.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ResourceGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
