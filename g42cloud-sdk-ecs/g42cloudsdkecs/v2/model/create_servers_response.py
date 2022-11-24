# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateServersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'order_id': 'str',
        'server_ids': 'list[str]'
    }

    attribute_map = {
        'job_id': 'job_id',
        'order_id': 'order_id',
        'server_ids': 'serverIds'
    }

    def __init__(self, job_id=None, order_id=None, server_ids=None):
        """CreateServersResponse

        The model defined in g42cloud sdk

        :param job_id: The param of the CreateServersResponse
        :type job_id: str
        :param order_id: The param of the CreateServersResponse
        :type order_id: str
        :param server_ids: The param of the CreateServersResponse
        :type server_ids: list[str]
        """
        
        super(CreateServersResponse, self).__init__()

        self._job_id = None
        self._order_id = None
        self._server_ids = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if order_id is not None:
            self.order_id = order_id
        if server_ids is not None:
            self.server_ids = server_ids

    @property
    def job_id(self):
        """Gets the job_id of this CreateServersResponse.

        :return: The job_id of this CreateServersResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this CreateServersResponse.

        :param job_id: The job_id of this CreateServersResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def order_id(self):
        """Gets the order_id of this CreateServersResponse.

        :return: The order_id of this CreateServersResponse.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this CreateServersResponse.

        :param order_id: The order_id of this CreateServersResponse.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def server_ids(self):
        """Gets the server_ids of this CreateServersResponse.

        :return: The server_ids of this CreateServersResponse.
        :rtype: list[str]
        """
        return self._server_ids

    @server_ids.setter
    def server_ids(self, server_ids):
        """Sets the server_ids of this CreateServersResponse.

        :param server_ids: The server_ids of this CreateServersResponse.
        :type server_ids: list[str]
        """
        self._server_ids = server_ids

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
        if not isinstance(other, CreateServersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
