# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAgentDimensionInfoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'dim_name': 'str',
        'dim_value': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'dim_name': 'dim_name',
        'dim_value': 'dim_value',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, instance_id=None, dim_name=None, dim_value=None, offset=None, limit=None):
        """ListAgentDimensionInfoRequest

        The model defined in g42cloud sdk

        :param instance_id: The param of the ListAgentDimensionInfoRequest
        :type instance_id: str
        :param dim_name: The param of the ListAgentDimensionInfoRequest
        :type dim_name: str
        :param dim_value: The param of the ListAgentDimensionInfoRequest
        :type dim_value: str
        :param offset: The param of the ListAgentDimensionInfoRequest
        :type offset: int
        :param limit: The param of the ListAgentDimensionInfoRequest
        :type limit: int
        """
        
        

        self._instance_id = None
        self._dim_name = None
        self._dim_value = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.instance_id = instance_id
        self.dim_name = dim_name
        if dim_value is not None:
            self.dim_value = dim_value
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def instance_id(self):
        """Gets the instance_id of this ListAgentDimensionInfoRequest.

        :return: The instance_id of this ListAgentDimensionInfoRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListAgentDimensionInfoRequest.

        :param instance_id: The instance_id of this ListAgentDimensionInfoRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def dim_name(self):
        """Gets the dim_name of this ListAgentDimensionInfoRequest.

        :return: The dim_name of this ListAgentDimensionInfoRequest.
        :rtype: str
        """
        return self._dim_name

    @dim_name.setter
    def dim_name(self, dim_name):
        """Sets the dim_name of this ListAgentDimensionInfoRequest.

        :param dim_name: The dim_name of this ListAgentDimensionInfoRequest.
        :type dim_name: str
        """
        self._dim_name = dim_name

    @property
    def dim_value(self):
        """Gets the dim_value of this ListAgentDimensionInfoRequest.

        :return: The dim_value of this ListAgentDimensionInfoRequest.
        :rtype: str
        """
        return self._dim_value

    @dim_value.setter
    def dim_value(self, dim_value):
        """Sets the dim_value of this ListAgentDimensionInfoRequest.

        :param dim_value: The dim_value of this ListAgentDimensionInfoRequest.
        :type dim_value: str
        """
        self._dim_value = dim_value

    @property
    def offset(self):
        """Gets the offset of this ListAgentDimensionInfoRequest.

        :return: The offset of this ListAgentDimensionInfoRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListAgentDimensionInfoRequest.

        :param offset: The offset of this ListAgentDimensionInfoRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListAgentDimensionInfoRequest.

        :return: The limit of this ListAgentDimensionInfoRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAgentDimensionInfoRequest.

        :param limit: The limit of this ListAgentDimensionInfoRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListAgentDimensionInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
