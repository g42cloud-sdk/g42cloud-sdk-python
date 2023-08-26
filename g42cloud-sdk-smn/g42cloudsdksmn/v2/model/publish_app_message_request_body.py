# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublishAppMessageRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'message': 'str',
        'message_structure': 'str',
        'time_to_live': 'str'
    }

    attribute_map = {
        'message': 'message',
        'message_structure': 'message_structure',
        'time_to_live': 'time_to_live'
    }

    def __init__(self, message=None, message_structure=None, time_to_live=None):
        """PublishAppMessageRequestBody

        The model defined in g42cloud sdk

        :param message: The param of the PublishAppMessageRequestBody
        :type message: str
        :param message_structure: The param of the PublishAppMessageRequestBody
        :type message_structure: str
        :param time_to_live: The param of the PublishAppMessageRequestBody
        :type time_to_live: str
        """
        
        

        self._message = None
        self._message_structure = None
        self._time_to_live = None
        self.discriminator = None

        if message is not None:
            self.message = message
        if message_structure is not None:
            self.message_structure = message_structure
        if time_to_live is not None:
            self.time_to_live = time_to_live

    @property
    def message(self):
        """Gets the message of this PublishAppMessageRequestBody.

        :return: The message of this PublishAppMessageRequestBody.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this PublishAppMessageRequestBody.

        :param message: The message of this PublishAppMessageRequestBody.
        :type message: str
        """
        self._message = message

    @property
    def message_structure(self):
        """Gets the message_structure of this PublishAppMessageRequestBody.

        :return: The message_structure of this PublishAppMessageRequestBody.
        :rtype: str
        """
        return self._message_structure

    @message_structure.setter
    def message_structure(self, message_structure):
        """Sets the message_structure of this PublishAppMessageRequestBody.

        :param message_structure: The message_structure of this PublishAppMessageRequestBody.
        :type message_structure: str
        """
        self._message_structure = message_structure

    @property
    def time_to_live(self):
        """Gets the time_to_live of this PublishAppMessageRequestBody.

        :return: The time_to_live of this PublishAppMessageRequestBody.
        :rtype: str
        """
        return self._time_to_live

    @time_to_live.setter
    def time_to_live(self, time_to_live):
        """Sets the time_to_live of this PublishAppMessageRequestBody.

        :param time_to_live: The time_to_live of this PublishAppMessageRequestBody.
        :type time_to_live: str
        """
        self._time_to_live = time_to_live

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
        if not isinstance(other, PublishAppMessageRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
