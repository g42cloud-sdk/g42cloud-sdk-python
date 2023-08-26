# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class MessageTemplate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'message_template_id': 'str',
        'message_template_name': 'str',
        'protocol': 'str',
        'tag_names': 'list[str]',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'message_template_id': 'message_template_id',
        'message_template_name': 'message_template_name',
        'protocol': 'protocol',
        'tag_names': 'tag_names',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, message_template_id=None, message_template_name=None, protocol=None, tag_names=None, create_time=None, update_time=None):
        """MessageTemplate

        The model defined in g42cloud sdk

        :param message_template_id: The param of the MessageTemplate
        :type message_template_id: str
        :param message_template_name: The param of the MessageTemplate
        :type message_template_name: str
        :param protocol: The param of the MessageTemplate
        :type protocol: str
        :param tag_names: The param of the MessageTemplate
        :type tag_names: list[str]
        :param create_time: The param of the MessageTemplate
        :type create_time: str
        :param update_time: The param of the MessageTemplate
        :type update_time: str
        """
        
        

        self._message_template_id = None
        self._message_template_name = None
        self._protocol = None
        self._tag_names = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        self.message_template_id = message_template_id
        self.message_template_name = message_template_name
        self.protocol = protocol
        self.tag_names = tag_names
        self.create_time = create_time
        self.update_time = update_time

    @property
    def message_template_id(self):
        """Gets the message_template_id of this MessageTemplate.

        :return: The message_template_id of this MessageTemplate.
        :rtype: str
        """
        return self._message_template_id

    @message_template_id.setter
    def message_template_id(self, message_template_id):
        """Sets the message_template_id of this MessageTemplate.

        :param message_template_id: The message_template_id of this MessageTemplate.
        :type message_template_id: str
        """
        self._message_template_id = message_template_id

    @property
    def message_template_name(self):
        """Gets the message_template_name of this MessageTemplate.

        :return: The message_template_name of this MessageTemplate.
        :rtype: str
        """
        return self._message_template_name

    @message_template_name.setter
    def message_template_name(self, message_template_name):
        """Sets the message_template_name of this MessageTemplate.

        :param message_template_name: The message_template_name of this MessageTemplate.
        :type message_template_name: str
        """
        self._message_template_name = message_template_name

    @property
    def protocol(self):
        """Gets the protocol of this MessageTemplate.

        :return: The protocol of this MessageTemplate.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this MessageTemplate.

        :param protocol: The protocol of this MessageTemplate.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def tag_names(self):
        """Gets the tag_names of this MessageTemplate.

        :return: The tag_names of this MessageTemplate.
        :rtype: list[str]
        """
        return self._tag_names

    @tag_names.setter
    def tag_names(self, tag_names):
        """Sets the tag_names of this MessageTemplate.

        :param tag_names: The tag_names of this MessageTemplate.
        :type tag_names: list[str]
        """
        self._tag_names = tag_names

    @property
    def create_time(self):
        """Gets the create_time of this MessageTemplate.

        :return: The create_time of this MessageTemplate.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this MessageTemplate.

        :param create_time: The create_time of this MessageTemplate.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this MessageTemplate.

        :return: The update_time of this MessageTemplate.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this MessageTemplate.

        :param update_time: The update_time of this MessageTemplate.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, MessageTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
