# coding: utf-8

import six

from g42cloudsdkcore.sdk_response import SdkResponse
from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePoolResponse(SdkResponse):

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
        'pool': 'Pool'
    }

    attribute_map = {
        'request_id': 'request_id',
        'pool': 'pool'
    }

    def __init__(self, request_id=None, pool=None):
        """UpdatePoolResponse

        The model defined in g42cloud sdk

        :param request_id: The param of the UpdatePoolResponse
        :type request_id: str
        :param pool: The param of the UpdatePoolResponse
        :type pool: :class:`g42cloudsdkelb.v3.Pool`
        """
        
        super(UpdatePoolResponse, self).__init__()

        self._request_id = None
        self._pool = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if pool is not None:
            self.pool = pool

    @property
    def request_id(self):
        """Gets the request_id of this UpdatePoolResponse.

        :return: The request_id of this UpdatePoolResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this UpdatePoolResponse.

        :param request_id: The request_id of this UpdatePoolResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def pool(self):
        """Gets the pool of this UpdatePoolResponse.

        :return: The pool of this UpdatePoolResponse.
        :rtype: :class:`g42cloudsdkelb.v3.Pool`
        """
        return self._pool

    @pool.setter
    def pool(self, pool):
        """Sets the pool of this UpdatePoolResponse.

        :param pool: The pool of this UpdatePoolResponse.
        :type pool: :class:`g42cloudsdkelb.v3.Pool`
        """
        self._pool = pool

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
        if not isinstance(other, UpdatePoolResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
