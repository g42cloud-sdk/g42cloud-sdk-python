# coding: utf-8

import six

from g42cloudsdkcore.sdk_response import SdkResponse
from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowListenerResponse(SdkResponse):

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
        'listener': 'Listener'
    }

    attribute_map = {
        'request_id': 'request_id',
        'listener': 'listener'
    }

    def __init__(self, request_id=None, listener=None):
        """ShowListenerResponse

        The model defined in g42cloud sdk

        :param request_id: The param of the ShowListenerResponse
        :type request_id: str
        :param listener: The param of the ShowListenerResponse
        :type listener: :class:`g42cloudsdkelb.v3.Listener`
        """
        
        super(ShowListenerResponse, self).__init__()

        self._request_id = None
        self._listener = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if listener is not None:
            self.listener = listener

    @property
    def request_id(self):
        """Gets the request_id of this ShowListenerResponse.

        :return: The request_id of this ShowListenerResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ShowListenerResponse.

        :param request_id: The request_id of this ShowListenerResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def listener(self):
        """Gets the listener of this ShowListenerResponse.

        :return: The listener of this ShowListenerResponse.
        :rtype: :class:`g42cloudsdkelb.v3.Listener`
        """
        return self._listener

    @listener.setter
    def listener(self, listener):
        """Sets the listener of this ShowListenerResponse.

        :param listener: The listener of this ShowListenerResponse.
        :type listener: :class:`g42cloudsdkelb.v3.Listener`
        """
        self._listener = listener

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
        if not isinstance(other, ShowListenerResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
