# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterInformationSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'custom_san': 'list[str]',
        'container_network': 'ContainerNetworkUpdate'
    }

    attribute_map = {
        'description': 'description',
        'custom_san': 'customSan',
        'container_network': 'containerNetwork'
    }

    def __init__(self, description=None, custom_san=None, container_network=None):
        """ClusterInformationSpec

        The model defined in g42cloud sdk

        :param description: The param of the ClusterInformationSpec
        :type description: str
        :param custom_san: The param of the ClusterInformationSpec
        :type custom_san: list[str]
        :param container_network: The param of the ClusterInformationSpec
        :type container_network: :class:`g42cloudsdkcce.v3.ContainerNetworkUpdate`
        """
        
        

        self._description = None
        self._custom_san = None
        self._container_network = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if custom_san is not None:
            self.custom_san = custom_san
        if container_network is not None:
            self.container_network = container_network

    @property
    def description(self):
        """Gets the description of this ClusterInformationSpec.

        :return: The description of this ClusterInformationSpec.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ClusterInformationSpec.

        :param description: The description of this ClusterInformationSpec.
        :type description: str
        """
        self._description = description

    @property
    def custom_san(self):
        """Gets the custom_san of this ClusterInformationSpec.

        :return: The custom_san of this ClusterInformationSpec.
        :rtype: list[str]
        """
        return self._custom_san

    @custom_san.setter
    def custom_san(self, custom_san):
        """Sets the custom_san of this ClusterInformationSpec.

        :param custom_san: The custom_san of this ClusterInformationSpec.
        :type custom_san: list[str]
        """
        self._custom_san = custom_san

    @property
    def container_network(self):
        """Gets the container_network of this ClusterInformationSpec.

        :return: The container_network of this ClusterInformationSpec.
        :rtype: :class:`g42cloudsdkcce.v3.ContainerNetworkUpdate`
        """
        return self._container_network

    @container_network.setter
    def container_network(self, container_network):
        """Sets the container_network of this ClusterInformationSpec.

        :param container_network: The container_network of this ClusterInformationSpec.
        :type container_network: :class:`g42cloudsdkcce.v3.ContainerNetworkUpdate`
        """
        self._container_network = container_network

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
        if not isinstance(other, ClusterInformationSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
