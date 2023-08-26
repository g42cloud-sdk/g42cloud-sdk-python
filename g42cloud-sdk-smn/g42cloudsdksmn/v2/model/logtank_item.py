# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class LogtankItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'log_group_id': 'str',
        'log_stream_id': 'str',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'log_group_id': 'log_group_id',
        'log_stream_id': 'log_stream_id',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, log_group_id=None, log_stream_id=None, create_time=None, update_time=None):
        """LogtankItem

        The model defined in g42cloud sdk

        :param id: The param of the LogtankItem
        :type id: str
        :param log_group_id: The param of the LogtankItem
        :type log_group_id: str
        :param log_stream_id: The param of the LogtankItem
        :type log_stream_id: str
        :param create_time: The param of the LogtankItem
        :type create_time: str
        :param update_time: The param of the LogtankItem
        :type update_time: str
        """
        
        

        self._id = None
        self._log_group_id = None
        self._log_stream_id = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        self.id = id
        self.log_group_id = log_group_id
        self.log_stream_id = log_stream_id
        self.create_time = create_time
        self.update_time = update_time

    @property
    def id(self):
        """Gets the id of this LogtankItem.

        :return: The id of this LogtankItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LogtankItem.

        :param id: The id of this LogtankItem.
        :type id: str
        """
        self._id = id

    @property
    def log_group_id(self):
        """Gets the log_group_id of this LogtankItem.

        :return: The log_group_id of this LogtankItem.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        """Sets the log_group_id of this LogtankItem.

        :param log_group_id: The log_group_id of this LogtankItem.
        :type log_group_id: str
        """
        self._log_group_id = log_group_id

    @property
    def log_stream_id(self):
        """Gets the log_stream_id of this LogtankItem.

        :return: The log_stream_id of this LogtankItem.
        :rtype: str
        """
        return self._log_stream_id

    @log_stream_id.setter
    def log_stream_id(self, log_stream_id):
        """Sets the log_stream_id of this LogtankItem.

        :param log_stream_id: The log_stream_id of this LogtankItem.
        :type log_stream_id: str
        """
        self._log_stream_id = log_stream_id

    @property
    def create_time(self):
        """Gets the create_time of this LogtankItem.

        :return: The create_time of this LogtankItem.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this LogtankItem.

        :param create_time: The create_time of this LogtankItem.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this LogtankItem.

        :return: The update_time of this LogtankItem.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this LogtankItem.

        :param update_time: The update_time of this LogtankItem.
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
        if not isinstance(other, LogtankItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
