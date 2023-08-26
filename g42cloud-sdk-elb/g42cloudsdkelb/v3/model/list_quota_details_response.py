# coding: utf-8

import six

from g42cloudsdkcore.sdk_response import SdkResponse
from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListQuotaDetailsResponse(SdkResponse):

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
        'quotas': 'list[QuotaInfo]'
    }

    attribute_map = {
        'request_id': 'request_id',
        'quotas': 'quotas'
    }

    def __init__(self, request_id=None, quotas=None):
        """ListQuotaDetailsResponse

        The model defined in g42cloud sdk

        :param request_id: The param of the ListQuotaDetailsResponse
        :type request_id: str
        :param quotas: The param of the ListQuotaDetailsResponse
        :type quotas: list[:class:`g42cloudsdkelb.v3.QuotaInfo`]
        """
        
        super(ListQuotaDetailsResponse, self).__init__()

        self._request_id = None
        self._quotas = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if quotas is not None:
            self.quotas = quotas

    @property
    def request_id(self):
        """Gets the request_id of this ListQuotaDetailsResponse.

        :return: The request_id of this ListQuotaDetailsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListQuotaDetailsResponse.

        :param request_id: The request_id of this ListQuotaDetailsResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def quotas(self):
        """Gets the quotas of this ListQuotaDetailsResponse.

        :return: The quotas of this ListQuotaDetailsResponse.
        :rtype: list[:class:`g42cloudsdkelb.v3.QuotaInfo`]
        """
        return self._quotas

    @quotas.setter
    def quotas(self, quotas):
        """Sets the quotas of this ListQuotaDetailsResponse.

        :param quotas: The quotas of this ListQuotaDetailsResponse.
        :type quotas: list[:class:`g42cloudsdkelb.v3.QuotaInfo`]
        """
        self._quotas = quotas

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
        if not isinstance(other, ListQuotaDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
