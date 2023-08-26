# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackupForList:

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
        'databases': 'list[BackupDatabase]',
        'begin_time': 'str',
        'end_time': 'str',
        'status': 'str',
        'type': 'str',
        'size': 'int',
        'datastore': 'BackupDatastore',
        'associated_with_ddm': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'instance_id': 'instance_id',
        'name': 'name',
        'databases': 'databases',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'status': 'status',
        'type': 'type',
        'size': 'size',
        'datastore': 'datastore',
        'associated_with_ddm': 'associated_with_ddm'
    }

    def __init__(self, id=None, instance_id=None, name=None, databases=None, begin_time=None, end_time=None, status=None, type=None, size=None, datastore=None, associated_with_ddm=None):
        """BackupForList

        The model defined in g42cloud sdk

        :param id: The param of the BackupForList
        :type id: str
        :param instance_id: The param of the BackupForList
        :type instance_id: str
        :param name: The param of the BackupForList
        :type name: str
        :param databases: The param of the BackupForList
        :type databases: list[:class:`g42cloudsdkrds.v3.BackupDatabase`]
        :param begin_time: The param of the BackupForList
        :type begin_time: str
        :param end_time: The param of the BackupForList
        :type end_time: str
        :param status: The param of the BackupForList
        :type status: str
        :param type: The param of the BackupForList
        :type type: str
        :param size: The param of the BackupForList
        :type size: int
        :param datastore: The param of the BackupForList
        :type datastore: :class:`g42cloudsdkrds.v3.BackupDatastore`
        :param associated_with_ddm: The param of the BackupForList
        :type associated_with_ddm: bool
        """
        
        

        self._id = None
        self._instance_id = None
        self._name = None
        self._databases = None
        self._begin_time = None
        self._end_time = None
        self._status = None
        self._type = None
        self._size = None
        self._datastore = None
        self._associated_with_ddm = None
        self.discriminator = None

        self.id = id
        self.instance_id = instance_id
        self.name = name
        if databases is not None:
            self.databases = databases
        self.begin_time = begin_time
        self.end_time = end_time
        self.status = status
        self.type = type
        self.size = size
        self.datastore = datastore
        if associated_with_ddm is not None:
            self.associated_with_ddm = associated_with_ddm

    @property
    def id(self):
        """Gets the id of this BackupForList.

        :return: The id of this BackupForList.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BackupForList.

        :param id: The id of this BackupForList.
        :type id: str
        """
        self._id = id

    @property
    def instance_id(self):
        """Gets the instance_id of this BackupForList.

        :return: The instance_id of this BackupForList.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this BackupForList.

        :param instance_id: The instance_id of this BackupForList.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def name(self):
        """Gets the name of this BackupForList.

        :return: The name of this BackupForList.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BackupForList.

        :param name: The name of this BackupForList.
        :type name: str
        """
        self._name = name

    @property
    def databases(self):
        """Gets the databases of this BackupForList.

        :return: The databases of this BackupForList.
        :rtype: list[:class:`g42cloudsdkrds.v3.BackupDatabase`]
        """
        return self._databases

    @databases.setter
    def databases(self, databases):
        """Sets the databases of this BackupForList.

        :param databases: The databases of this BackupForList.
        :type databases: list[:class:`g42cloudsdkrds.v3.BackupDatabase`]
        """
        self._databases = databases

    @property
    def begin_time(self):
        """Gets the begin_time of this BackupForList.

        :return: The begin_time of this BackupForList.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this BackupForList.

        :param begin_time: The begin_time of this BackupForList.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this BackupForList.

        :return: The end_time of this BackupForList.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this BackupForList.

        :param end_time: The end_time of this BackupForList.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def status(self):
        """Gets the status of this BackupForList.

        :return: The status of this BackupForList.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BackupForList.

        :param status: The status of this BackupForList.
        :type status: str
        """
        self._status = status

    @property
    def type(self):
        """Gets the type of this BackupForList.

        :return: The type of this BackupForList.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BackupForList.

        :param type: The type of this BackupForList.
        :type type: str
        """
        self._type = type

    @property
    def size(self):
        """Gets the size of this BackupForList.

        :return: The size of this BackupForList.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this BackupForList.

        :param size: The size of this BackupForList.
        :type size: int
        """
        self._size = size

    @property
    def datastore(self):
        """Gets the datastore of this BackupForList.

        :return: The datastore of this BackupForList.
        :rtype: :class:`g42cloudsdkrds.v3.BackupDatastore`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        """Sets the datastore of this BackupForList.

        :param datastore: The datastore of this BackupForList.
        :type datastore: :class:`g42cloudsdkrds.v3.BackupDatastore`
        """
        self._datastore = datastore

    @property
    def associated_with_ddm(self):
        """Gets the associated_with_ddm of this BackupForList.

        :return: The associated_with_ddm of this BackupForList.
        :rtype: bool
        """
        return self._associated_with_ddm

    @associated_with_ddm.setter
    def associated_with_ddm(self, associated_with_ddm):
        """Sets the associated_with_ddm of this BackupForList.

        :param associated_with_ddm: The associated_with_ddm of this BackupForList.
        :type associated_with_ddm: bool
        """
        self._associated_with_ddm = associated_with_ddm

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
        if not isinstance(other, BackupForList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
