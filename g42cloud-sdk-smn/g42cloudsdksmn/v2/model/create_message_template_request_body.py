# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateMessageTemplateRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'message_template_name': 'str',
        'protocol': 'str',
        'content': 'str'
    }

    attribute_map = {
        'message_template_name': 'message_template_name',
        'protocol': 'protocol',
        'content': 'content'
    }

    def __init__(self, message_template_name=None, protocol=None, content=None):
        """CreateMessageTemplateRequestBody

        The model defined in g42cloud sdk

        :param message_template_name: The param of the CreateMessageTemplateRequestBody
        :type message_template_name: str
        :param protocol: The param of the CreateMessageTemplateRequestBody
        :type protocol: str
        :param content: The param of the CreateMessageTemplateRequestBody
        :type content: str
        """
        
        

        self._message_template_name = None
        self._protocol = None
        self._content = None
        self.discriminator = None

        self.message_template_name = message_template_name
        self.protocol = protocol
        self.content = content

    @property
    def message_template_name(self):
        """Gets the message_template_name of this CreateMessageTemplateRequestBody.

        :return: The message_template_name of this CreateMessageTemplateRequestBody.
        :rtype: str
        """
        return self._message_template_name

    @message_template_name.setter
    def message_template_name(self, message_template_name):
        """Sets the message_template_name of this CreateMessageTemplateRequestBody.

        :param message_template_name: The message_template_name of this CreateMessageTemplateRequestBody.
        :type message_template_name: str
        """
        self._message_template_name = message_template_name

    @property
    def protocol(self):
        """Gets the protocol of this CreateMessageTemplateRequestBody.

        :return: The protocol of this CreateMessageTemplateRequestBody.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this CreateMessageTemplateRequestBody.

        :param protocol: The protocol of this CreateMessageTemplateRequestBody.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def content(self):
        """Gets the content of this CreateMessageTemplateRequestBody.

        :return: The content of this CreateMessageTemplateRequestBody.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this CreateMessageTemplateRequestBody.

        :param content: The content of this CreateMessageTemplateRequestBody.
        :type content: str
        """
        self._content = content

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
        if not isinstance(other, CreateMessageTemplateRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
