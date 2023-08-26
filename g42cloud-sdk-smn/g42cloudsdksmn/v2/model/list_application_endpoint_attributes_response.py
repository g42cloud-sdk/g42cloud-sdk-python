# coding: utf-8

import six

from g42cloudsdkcore.sdk_response import SdkResponse
from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListApplicationEndpointAttributesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'attributes': 'ListApplicationEndpointAttributesResponseBodyAttributes'
    }

    attribute_map = {
        'request_id': 'request_id',
        'attributes': 'attributes'
    }

    def __init__(self, request_id=None, attributes=None):
        """ListApplicationEndpointAttributesResponse

        The model defined in g42cloud sdk

        :param request_id: The param of the ListApplicationEndpointAttributesResponse
        :type request_id: str
        :param attributes: The param of the ListApplicationEndpointAttributesResponse
        :type attributes: :class:`g42cloudsdksmn.v2.ListApplicationEndpointAttributesResponseBodyAttributes`
        """
        
        super(ListApplicationEndpointAttributesResponse, self).__init__()

        self._request_id = None
        self._attributes = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if attributes is not None:
            self.attributes = attributes

    @property
    def request_id(self):
        """Gets the request_id of this ListApplicationEndpointAttributesResponse.

        :return: The request_id of this ListApplicationEndpointAttributesResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListApplicationEndpointAttributesResponse.

        :param request_id: The request_id of this ListApplicationEndpointAttributesResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def attributes(self):
        """Gets the attributes of this ListApplicationEndpointAttributesResponse.

        :return: The attributes of this ListApplicationEndpointAttributesResponse.
        :rtype: :class:`g42cloudsdksmn.v2.ListApplicationEndpointAttributesResponseBodyAttributes`
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this ListApplicationEndpointAttributesResponse.

        :param attributes: The attributes of this ListApplicationEndpointAttributesResponse.
        :type attributes: :class:`g42cloudsdksmn.v2.ListApplicationEndpointAttributesResponseBodyAttributes`
        """
        self._attributes = attributes

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
        if not isinstance(other, ListApplicationEndpointAttributesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
