# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackupInfo:

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
        'instance_id': 'str',
        'name': 'str',
        'description': 'str',
        'databases': 'list[BackupDatabase]',
        'begin_time': 'str',
        'status': 'str',
        'type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'instance_id': 'instance_id',
        'name': 'name',
        'description': 'description',
        'databases': 'databases',
        'begin_time': 'begin_time',
        'status': 'status',
        'type': 'type'
    }

    def __init__(self, id=None, instance_id=None, name=None, description=None, databases=None, begin_time=None, status=None, type=None):
        """BackupInfo

        The model defined in g42cloud sdk

        :param id: The param of the BackupInfo
        :type id: str
        :param instance_id: The param of the BackupInfo
        :type instance_id: str
        :param name: The param of the BackupInfo
        :type name: str
        :param description: The param of the BackupInfo
        :type description: str
        :param databases: The param of the BackupInfo
        :type databases: list[:class:`g42cloudsdkrds.v3.BackupDatabase`]
        :param begin_time: The param of the BackupInfo
        :type begin_time: str
        :param status: The param of the BackupInfo
        :type status: str
        :param type: The param of the BackupInfo
        :type type: str
        """
        
        

        self._id = None
        self._instance_id = None
        self._name = None
        self._description = None
        self._databases = None
        self._begin_time = None
        self._status = None
        self._type = None
        self.discriminator = None

        self.id = id
        self.instance_id = instance_id
        self.name = name
        if description is not None:
            self.description = description
        if databases is not None:
            self.databases = databases
        self.begin_time = begin_time
        self.status = status
        self.type = type

    @property
    def id(self):
        """Gets the id of this BackupInfo.

        :return: The id of this BackupInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BackupInfo.

        :param id: The id of this BackupInfo.
        :type id: str
        """
        self._id = id

    @property
    def instance_id(self):
        """Gets the instance_id of this BackupInfo.

        :return: The instance_id of this BackupInfo.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this BackupInfo.

        :param instance_id: The instance_id of this BackupInfo.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def name(self):
        """Gets the name of this BackupInfo.

        :return: The name of this BackupInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BackupInfo.

        :param name: The name of this BackupInfo.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this BackupInfo.

        :return: The description of this BackupInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BackupInfo.

        :param description: The description of this BackupInfo.
        :type description: str
        """
        self._description = description

    @property
    def databases(self):
        """Gets the databases of this BackupInfo.

        :return: The databases of this BackupInfo.
        :rtype: list[:class:`g42cloudsdkrds.v3.BackupDatabase`]
        """
        return self._databases

    @databases.setter
    def databases(self, databases):
        """Sets the databases of this BackupInfo.

        :param databases: The databases of this BackupInfo.
        :type databases: list[:class:`g42cloudsdkrds.v3.BackupDatabase`]
        """
        self._databases = databases

    @property
    def begin_time(self):
        """Gets the begin_time of this BackupInfo.

        :return: The begin_time of this BackupInfo.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this BackupInfo.

        :param begin_time: The begin_time of this BackupInfo.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def status(self):
        """Gets the status of this BackupInfo.

        :return: The status of this BackupInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BackupInfo.

        :param status: The status of this BackupInfo.
        :type status: str
        """
        self._status = status

    @property
    def type(self):
        """Gets the type of this BackupInfo.

        :return: The type of this BackupInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BackupInfo.

        :param type: The type of this BackupInfo.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, BackupInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
