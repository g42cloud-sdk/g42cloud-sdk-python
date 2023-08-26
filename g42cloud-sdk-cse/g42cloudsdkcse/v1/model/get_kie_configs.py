# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetKieConfigs:

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
        'key': 'str',
        'labels': 'object',
        'value': 'str',
        'value_type': 'str',
        'status': 'str',
        'create_time': 'int',
        'update_time': 'int',
        'create_revision': 'int',
        'update_revision': 'int'
    }

    attribute_map = {
        'id': 'id',
        'key': 'key',
        'labels': 'labels',
        'value': 'value',
        'value_type': 'value_type',
        'status': 'status',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'create_revision': 'create_revision',
        'update_revision': 'update_revision'
    }

    def __init__(self, id=None, key=None, labels=None, value=None, value_type=None, status=None, create_time=None, update_time=None, create_revision=None, update_revision=None):
        """GetKieConfigs

        The model defined in g42cloud sdk

        :param id: The param of the GetKieConfigs
        :type id: str
        :param key: The param of the GetKieConfigs
        :type key: str
        :param labels: The param of the GetKieConfigs
        :type labels: object
        :param value: The param of the GetKieConfigs
        :type value: str
        :param value_type: The param of the GetKieConfigs
        :type value_type: str
        :param status: The param of the GetKieConfigs
        :type status: str
        :param create_time: The param of the GetKieConfigs
        :type create_time: int
        :param update_time: The param of the GetKieConfigs
        :type update_time: int
        :param create_revision: The param of the GetKieConfigs
        :type create_revision: int
        :param update_revision: The param of the GetKieConfigs
        :type update_revision: int
        """
        
        

        self._id = None
        self._key = None
        self._labels = None
        self._value = None
        self._value_type = None
        self._status = None
        self._create_time = None
        self._update_time = None
        self._create_revision = None
        self._update_revision = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if key is not None:
            self.key = key
        if labels is not None:
            self.labels = labels
        if value is not None:
            self.value = value
        if value_type is not None:
            self.value_type = value_type
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if create_revision is not None:
            self.create_revision = create_revision
        if update_revision is not None:
            self.update_revision = update_revision

    @property
    def id(self):
        """Gets the id of this GetKieConfigs.

        :return: The id of this GetKieConfigs.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetKieConfigs.

        :param id: The id of this GetKieConfigs.
        :type id: str
        """
        self._id = id

    @property
    def key(self):
        """Gets the key of this GetKieConfigs.

        :return: The key of this GetKieConfigs.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this GetKieConfigs.

        :param key: The key of this GetKieConfigs.
        :type key: str
        """
        self._key = key

    @property
    def labels(self):
        """Gets the labels of this GetKieConfigs.

        :return: The labels of this GetKieConfigs.
        :rtype: object
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this GetKieConfigs.

        :param labels: The labels of this GetKieConfigs.
        :type labels: object
        """
        self._labels = labels

    @property
    def value(self):
        """Gets the value of this GetKieConfigs.

        :return: The value of this GetKieConfigs.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this GetKieConfigs.

        :param value: The value of this GetKieConfigs.
        :type value: str
        """
        self._value = value

    @property
    def value_type(self):
        """Gets the value_type of this GetKieConfigs.

        :return: The value_type of this GetKieConfigs.
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """Sets the value_type of this GetKieConfigs.

        :param value_type: The value_type of this GetKieConfigs.
        :type value_type: str
        """
        self._value_type = value_type

    @property
    def status(self):
        """Gets the status of this GetKieConfigs.

        :return: The status of this GetKieConfigs.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GetKieConfigs.

        :param status: The status of this GetKieConfigs.
        :type status: str
        """
        self._status = status

    @property
    def create_time(self):
        """Gets the create_time of this GetKieConfigs.

        :return: The create_time of this GetKieConfigs.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this GetKieConfigs.

        :param create_time: The create_time of this GetKieConfigs.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this GetKieConfigs.

        :return: The update_time of this GetKieConfigs.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this GetKieConfigs.

        :param update_time: The update_time of this GetKieConfigs.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def create_revision(self):
        """Gets the create_revision of this GetKieConfigs.

        :return: The create_revision of this GetKieConfigs.
        :rtype: int
        """
        return self._create_revision

    @create_revision.setter
    def create_revision(self, create_revision):
        """Sets the create_revision of this GetKieConfigs.

        :param create_revision: The create_revision of this GetKieConfigs.
        :type create_revision: int
        """
        self._create_revision = create_revision

    @property
    def update_revision(self):
        """Gets the update_revision of this GetKieConfigs.

        :return: The update_revision of this GetKieConfigs.
        :rtype: int
        """
        return self._update_revision

    @update_revision.setter
    def update_revision(self, update_revision):
        """Sets the update_revision of this GetKieConfigs.

        :param update_revision: The update_revision of this GetKieConfigs.
        :type update_revision: int
        """
        self._update_revision = update_revision

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
        if not isinstance(other, GetKieConfigs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
