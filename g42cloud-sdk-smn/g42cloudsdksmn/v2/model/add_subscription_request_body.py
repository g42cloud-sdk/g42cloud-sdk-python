# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddSubscriptionRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'protocol': 'str',
        'endpoint': 'str',
        'remark': 'str',
        'extension': 'SubscriptionExtension'
    }

    attribute_map = {
        'protocol': 'protocol',
        'endpoint': 'endpoint',
        'remark': 'remark',
        'extension': 'extension'
    }

    def __init__(self, protocol=None, endpoint=None, remark=None, extension=None):
        """AddSubscriptionRequestBody

        The model defined in g42cloud sdk

        :param protocol: The param of the AddSubscriptionRequestBody
        :type protocol: str
        :param endpoint: The param of the AddSubscriptionRequestBody
        :type endpoint: str
        :param remark: The param of the AddSubscriptionRequestBody
        :type remark: str
        :param extension: The param of the AddSubscriptionRequestBody
        :type extension: :class:`g42cloudsdksmn.v2.SubscriptionExtension`
        """
        
        

        self._protocol = None
        self._endpoint = None
        self._remark = None
        self._extension = None
        self.discriminator = None

        self.protocol = protocol
        self.endpoint = endpoint
        if remark is not None:
            self.remark = remark
        if extension is not None:
            self.extension = extension

    @property
    def protocol(self):
        """Gets the protocol of this AddSubscriptionRequestBody.

        :return: The protocol of this AddSubscriptionRequestBody.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this AddSubscriptionRequestBody.

        :param protocol: The protocol of this AddSubscriptionRequestBody.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def endpoint(self):
        """Gets the endpoint of this AddSubscriptionRequestBody.

        :return: The endpoint of this AddSubscriptionRequestBody.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this AddSubscriptionRequestBody.

        :param endpoint: The endpoint of this AddSubscriptionRequestBody.
        :type endpoint: str
        """
        self._endpoint = endpoint

    @property
    def remark(self):
        """Gets the remark of this AddSubscriptionRequestBody.

        :return: The remark of this AddSubscriptionRequestBody.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this AddSubscriptionRequestBody.

        :param remark: The remark of this AddSubscriptionRequestBody.
        :type remark: str
        """
        self._remark = remark

    @property
    def extension(self):
        """Gets the extension of this AddSubscriptionRequestBody.

        :return: The extension of this AddSubscriptionRequestBody.
        :rtype: :class:`g42cloudsdksmn.v2.SubscriptionExtension`
        """
        return self._extension

    @extension.setter
    def extension(self, extension):
        """Sets the extension of this AddSubscriptionRequestBody.

        :param extension: The extension of this AddSubscriptionRequestBody.
        :type extension: :class:`g42cloudsdksmn.v2.SubscriptionExtension`
        """
        self._extension = extension

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
        if not isinstance(other, AddSubscriptionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
