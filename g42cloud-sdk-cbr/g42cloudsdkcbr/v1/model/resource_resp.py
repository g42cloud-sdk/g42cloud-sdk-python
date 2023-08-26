# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'extra_info': 'ResourceExtraInfo',
        'id': 'str',
        'name': 'str',
        'protect_status': 'str',
        'size': 'int',
        'type': 'str',
        'backup_size': 'int',
        'backup_count': 'int',
        'auto_protect': 'bool'
    }

    attribute_map = {
        'extra_info': 'extra_info',
        'id': 'id',
        'name': 'name',
        'protect_status': 'protect_status',
        'size': 'size',
        'type': 'type',
        'backup_size': 'backup_size',
        'backup_count': 'backup_count',
        'auto_protect': 'auto_protect'
    }

    def __init__(self, extra_info=None, id=None, name=None, protect_status=None, size=None, type=None, backup_size=None, backup_count=None, auto_protect=None):
        """ResourceResp

        The model defined in g42cloud sdk

        :param extra_info: The param of the ResourceResp
        :type extra_info: :class:`g42cloudsdkcbr.v1.ResourceExtraInfo`
        :param id: The param of the ResourceResp
        :type id: str
        :param name: The param of the ResourceResp
        :type name: str
        :param protect_status: The param of the ResourceResp
        :type protect_status: str
        :param size: The param of the ResourceResp
        :type size: int
        :param type: The param of the ResourceResp
        :type type: str
        :param backup_size: The param of the ResourceResp
        :type backup_size: int
        :param backup_count: The param of the ResourceResp
        :type backup_count: int
        :param auto_protect: The param of the ResourceResp
        :type auto_protect: bool
        """
        
        

        self._extra_info = None
        self._id = None
        self._name = None
        self._protect_status = None
        self._size = None
        self._type = None
        self._backup_size = None
        self._backup_count = None
        self._auto_protect = None
        self.discriminator = None

        if extra_info is not None:
            self.extra_info = extra_info
        self.id = id
        self.name = name
        if protect_status is not None:
            self.protect_status = protect_status
        if size is not None:
            self.size = size
        self.type = type
        if backup_size is not None:
            self.backup_size = backup_size
        if backup_count is not None:
            self.backup_count = backup_count
        if auto_protect is not None:
            self.auto_protect = auto_protect

    @property
    def extra_info(self):
        """Gets the extra_info of this ResourceResp.

        :return: The extra_info of this ResourceResp.
        :rtype: :class:`g42cloudsdkcbr.v1.ResourceExtraInfo`
        """
        return self._extra_info

    @extra_info.setter
    def extra_info(self, extra_info):
        """Sets the extra_info of this ResourceResp.

        :param extra_info: The extra_info of this ResourceResp.
        :type extra_info: :class:`g42cloudsdkcbr.v1.ResourceExtraInfo`
        """
        self._extra_info = extra_info

    @property
    def id(self):
        """Gets the id of this ResourceResp.

        :return: The id of this ResourceResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResourceResp.

        :param id: The id of this ResourceResp.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ResourceResp.

        :return: The name of this ResourceResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ResourceResp.

        :param name: The name of this ResourceResp.
        :type name: str
        """
        self._name = name

    @property
    def protect_status(self):
        """Gets the protect_status of this ResourceResp.

        :return: The protect_status of this ResourceResp.
        :rtype: str
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        """Sets the protect_status of this ResourceResp.

        :param protect_status: The protect_status of this ResourceResp.
        :type protect_status: str
        """
        self._protect_status = protect_status

    @property
    def size(self):
        """Gets the size of this ResourceResp.

        :return: The size of this ResourceResp.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ResourceResp.

        :param size: The size of this ResourceResp.
        :type size: int
        """
        self._size = size

    @property
    def type(self):
        """Gets the type of this ResourceResp.

        :return: The type of this ResourceResp.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ResourceResp.

        :param type: The type of this ResourceResp.
        :type type: str
        """
        self._type = type

    @property
    def backup_size(self):
        """Gets the backup_size of this ResourceResp.

        :return: The backup_size of this ResourceResp.
        :rtype: int
        """
        return self._backup_size

    @backup_size.setter
    def backup_size(self, backup_size):
        """Sets the backup_size of this ResourceResp.

        :param backup_size: The backup_size of this ResourceResp.
        :type backup_size: int
        """
        self._backup_size = backup_size

    @property
    def backup_count(self):
        """Gets the backup_count of this ResourceResp.

        :return: The backup_count of this ResourceResp.
        :rtype: int
        """
        return self._backup_count

    @backup_count.setter
    def backup_count(self, backup_count):
        """Sets the backup_count of this ResourceResp.

        :param backup_count: The backup_count of this ResourceResp.
        :type backup_count: int
        """
        self._backup_count = backup_count

    @property
    def auto_protect(self):
        """Gets the auto_protect of this ResourceResp.

        :return: The auto_protect of this ResourceResp.
        :rtype: bool
        """
        return self._auto_protect

    @auto_protect.setter
    def auto_protect(self, auto_protect):
        """Sets the auto_protect of this ResourceResp.

        :param auto_protect: The auto_protect of this ResourceResp.
        :type auto_protect: bool
        """
        self._auto_protect = auto_protect

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
        if not isinstance(other, ResourceResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
