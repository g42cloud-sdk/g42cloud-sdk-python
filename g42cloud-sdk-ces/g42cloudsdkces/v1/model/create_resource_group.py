# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateResourceGroup:

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
        'dimensions': 'list[MetricsDimension]'
    }

    attribute_map = {
        'namespace': 'namespace',
        'dimensions': 'dimensions'
    }

    def __init__(self, namespace=None, dimensions=None):
        """CreateResourceGroup

        The model defined in g42cloud sdk

        :param namespace: The param of the CreateResourceGroup
        :type namespace: str
        :param dimensions: The param of the CreateResourceGroup
        :type dimensions: list[:class:`g42cloudsdkces.v1.MetricsDimension`]
        """
        
        

        self._namespace = None
        self._dimensions = None
        self.discriminator = None

        self.namespace = namespace
        self.dimensions = dimensions

    @property
    def namespace(self):
        """Gets the namespace of this CreateResourceGroup.

        :return: The namespace of this CreateResourceGroup.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this CreateResourceGroup.

        :param namespace: The namespace of this CreateResourceGroup.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def dimensions(self):
        """Gets the dimensions of this CreateResourceGroup.

        :return: The dimensions of this CreateResourceGroup.
        :rtype: list[:class:`g42cloudsdkces.v1.MetricsDimension`]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """Sets the dimensions of this CreateResourceGroup.

        :param dimensions: The dimensions of this CreateResourceGroup.
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
        if not isinstance(other, CreateResourceGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
