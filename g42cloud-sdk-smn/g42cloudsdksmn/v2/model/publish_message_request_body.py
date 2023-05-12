# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublishMessageRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'subject': 'str',
        'message': 'str',
        'message_structure': 'str',
        'message_template_name': 'str',
        'tags': 'dict(str, str)',
        'time_to_live': 'str'
    }

    attribute_map = {
        'subject': 'subject',
        'message': 'message',
        'message_structure': 'message_structure',
        'message_template_name': 'message_template_name',
        'tags': 'tags',
        'time_to_live': 'time_to_live'
    }

    def __init__(self, subject=None, message=None, message_structure=None, message_template_name=None, tags=None, time_to_live=None):
        """PublishMessageRequestBody

        The model defined in g42cloud sdk

        :param subject: The param of the PublishMessageRequestBody
        :type subject: str
        :param message: The param of the PublishMessageRequestBody
        :type message: str
        :param message_structure: The param of the PublishMessageRequestBody
        :type message_structure: str
        :param message_template_name: The param of the PublishMessageRequestBody
        :type message_template_name: str
        :param tags: The param of the PublishMessageRequestBody
        :type tags: dict(str, str)
        :param time_to_live: The param of the PublishMessageRequestBody
        :type time_to_live: str
        """
        
        

        self._subject = None
        self._message = None
        self._message_structure = None
        self._message_template_name = None
        self._tags = None
        self._time_to_live = None
        self.discriminator = None

        if subject is not None:
            self.subject = subject
        if message is not None:
            self.message = message
        if message_structure is not None:
            self.message_structure = message_structure
        if message_template_name is not None:
            self.message_template_name = message_template_name
        if tags is not None:
            self.tags = tags
        if time_to_live is not None:
            self.time_to_live = time_to_live

    @property
    def subject(self):
        """Gets the subject of this PublishMessageRequestBody.

        :return: The subject of this PublishMessageRequestBody.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this PublishMessageRequestBody.

        :param subject: The subject of this PublishMessageRequestBody.
        :type subject: str
        """
        self._subject = subject

    @property
    def message(self):
        """Gets the message of this PublishMessageRequestBody.

        :return: The message of this PublishMessageRequestBody.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this PublishMessageRequestBody.

        :param message: The message of this PublishMessageRequestBody.
        :type message: str
        """
        self._message = message

    @property
    def message_structure(self):
        """Gets the message_structure of this PublishMessageRequestBody.

        :return: The message_structure of this PublishMessageRequestBody.
        :rtype: str
        """
        return self._message_structure

    @message_structure.setter
    def message_structure(self, message_structure):
        """Sets the message_structure of this PublishMessageRequestBody.

        :param message_structure: The message_structure of this PublishMessageRequestBody.
        :type message_structure: str
        """
        self._message_structure = message_structure

    @property
    def message_template_name(self):
        """Gets the message_template_name of this PublishMessageRequestBody.

        :return: The message_template_name of this PublishMessageRequestBody.
        :rtype: str
        """
        return self._message_template_name

    @message_template_name.setter
    def message_template_name(self, message_template_name):
        """Sets the message_template_name of this PublishMessageRequestBody.

        :param message_template_name: The message_template_name of this PublishMessageRequestBody.
        :type message_template_name: str
        """
        self._message_template_name = message_template_name

    @property
    def tags(self):
        """Gets the tags of this PublishMessageRequestBody.

        :return: The tags of this PublishMessageRequestBody.
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this PublishMessageRequestBody.

        :param tags: The tags of this PublishMessageRequestBody.
        :type tags: dict(str, str)
        """
        self._tags = tags

    @property
    def time_to_live(self):
        """Gets the time_to_live of this PublishMessageRequestBody.

        :return: The time_to_live of this PublishMessageRequestBody.
        :rtype: str
        """
        return self._time_to_live

    @time_to_live.setter
    def time_to_live(self, time_to_live):
        """Sets the time_to_live of this PublishMessageRequestBody.

        :param time_to_live: The time_to_live of this PublishMessageRequestBody.
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
        if not isinstance(other, PublishMessageRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
