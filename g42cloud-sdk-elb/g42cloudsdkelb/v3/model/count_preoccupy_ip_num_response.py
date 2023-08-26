# coding: utf-8

import six

from g42cloudsdkcore.sdk_response import SdkResponse
from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class CountPreoccupyIpNumResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'preoccupy_ip': 'PreoccupyIp',
        'request_id': 'str'
    }

    attribute_map = {
        'preoccupy_ip': 'preoccupy_ip',
        'request_id': 'request_id'
    }

    def __init__(self, preoccupy_ip=None, request_id=None):
        """CountPreoccupyIpNumResponse

        The model defined in g42cloud sdk

        :param preoccupy_ip: The param of the CountPreoccupyIpNumResponse
        :type preoccupy_ip: :class:`g42cloudsdkelb.v3.PreoccupyIp`
        :param request_id: The param of the CountPreoccupyIpNumResponse
        :type request_id: str
        """
        
        super(CountPreoccupyIpNumResponse, self).__init__()

        self._preoccupy_ip = None
        self._request_id = None
        self.discriminator = None

        if preoccupy_ip is not None:
            self.preoccupy_ip = preoccupy_ip
        if request_id is not None:
            self.request_id = request_id

    @property
    def preoccupy_ip(self):
        """Gets the preoccupy_ip of this CountPreoccupyIpNumResponse.

        :return: The preoccupy_ip of this CountPreoccupyIpNumResponse.
        :rtype: :class:`g42cloudsdkelb.v3.PreoccupyIp`
        """
        return self._preoccupy_ip

    @preoccupy_ip.setter
    def preoccupy_ip(self, preoccupy_ip):
        """Sets the preoccupy_ip of this CountPreoccupyIpNumResponse.

        :param preoccupy_ip: The preoccupy_ip of this CountPreoccupyIpNumResponse.
        :type preoccupy_ip: :class:`g42cloudsdkelb.v3.PreoccupyIp`
        """
        self._preoccupy_ip = preoccupy_ip

    @property
    def request_id(self):
        """Gets the request_id of this CountPreoccupyIpNumResponse.

        :return: The request_id of this CountPreoccupyIpNumResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this CountPreoccupyIpNumResponse.

        :param request_id: The request_id of this CountPreoccupyIpNumResponse.
        :type request_id: str
        """
        self._request_id = request_id

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
        if not isinstance(other, CountPreoccupyIpNumResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
