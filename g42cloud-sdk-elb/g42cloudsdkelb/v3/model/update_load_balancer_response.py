# coding: utf-8

import six

from g42cloudsdkcore.sdk_response import SdkResponse
from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateLoadBalancerResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'loadbalancer': 'LoadBalancer',
        'loadbalancer_id': 'str',
        'order_id': 'str',
        'request_id': 'str'
    }

    attribute_map = {
        'loadbalancer': 'loadbalancer',
        'loadbalancer_id': 'loadbalancer_id',
        'order_id': 'order_id',
        'request_id': 'request_id'
    }

    def __init__(self, loadbalancer=None, loadbalancer_id=None, order_id=None, request_id=None):
        """UpdateLoadBalancerResponse

        The model defined in g42cloud sdk

        :param loadbalancer: The param of the UpdateLoadBalancerResponse
        :type loadbalancer: :class:`g42cloudsdkelb.v3.LoadBalancer`
        :param loadbalancer_id: The param of the UpdateLoadBalancerResponse
        :type loadbalancer_id: str
        :param order_id: The param of the UpdateLoadBalancerResponse
        :type order_id: str
        :param request_id: The param of the UpdateLoadBalancerResponse
        :type request_id: str
        """
        
        super(UpdateLoadBalancerResponse, self).__init__()

        self._loadbalancer = None
        self._loadbalancer_id = None
        self._order_id = None
        self._request_id = None
        self.discriminator = None

        if loadbalancer is not None:
            self.loadbalancer = loadbalancer
        if loadbalancer_id is not None:
            self.loadbalancer_id = loadbalancer_id
        if order_id is not None:
            self.order_id = order_id
        if request_id is not None:
            self.request_id = request_id

    @property
    def loadbalancer(self):
        """Gets the loadbalancer of this UpdateLoadBalancerResponse.

        :return: The loadbalancer of this UpdateLoadBalancerResponse.
        :rtype: :class:`g42cloudsdkelb.v3.LoadBalancer`
        """
        return self._loadbalancer

    @loadbalancer.setter
    def loadbalancer(self, loadbalancer):
        """Sets the loadbalancer of this UpdateLoadBalancerResponse.

        :param loadbalancer: The loadbalancer of this UpdateLoadBalancerResponse.
        :type loadbalancer: :class:`g42cloudsdkelb.v3.LoadBalancer`
        """
        self._loadbalancer = loadbalancer

    @property
    def loadbalancer_id(self):
        """Gets the loadbalancer_id of this UpdateLoadBalancerResponse.

        :return: The loadbalancer_id of this UpdateLoadBalancerResponse.
        :rtype: str
        """
        return self._loadbalancer_id

    @loadbalancer_id.setter
    def loadbalancer_id(self, loadbalancer_id):
        """Sets the loadbalancer_id of this UpdateLoadBalancerResponse.

        :param loadbalancer_id: The loadbalancer_id of this UpdateLoadBalancerResponse.
        :type loadbalancer_id: str
        """
        self._loadbalancer_id = loadbalancer_id

    @property
    def order_id(self):
        """Gets the order_id of this UpdateLoadBalancerResponse.

        :return: The order_id of this UpdateLoadBalancerResponse.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this UpdateLoadBalancerResponse.

        :param order_id: The order_id of this UpdateLoadBalancerResponse.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def request_id(self):
        """Gets the request_id of this UpdateLoadBalancerResponse.

        :return: The request_id of this UpdateLoadBalancerResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this UpdateLoadBalancerResponse.

        :param request_id: The request_id of this UpdateLoadBalancerResponse.
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
        if not isinstance(other, UpdateLoadBalancerResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
