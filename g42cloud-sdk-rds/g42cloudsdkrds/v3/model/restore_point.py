# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestorePoint:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'type': 'str',
        'backup_id': 'str',
        'restore_time': 'int',
        'database_name': 'dict(str, str)'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'type': 'type',
        'backup_id': 'backup_id',
        'restore_time': 'restore_time',
        'database_name': 'database_name'
    }

    def __init__(self, instance_id=None, type=None, backup_id=None, restore_time=None, database_name=None):
        """RestorePoint

        The model defined in g42cloud sdk

        :param instance_id: The param of the RestorePoint
        :type instance_id: str
        :param type: The param of the RestorePoint
        :type type: str
        :param backup_id: The param of the RestorePoint
        :type backup_id: str
        :param restore_time: The param of the RestorePoint
        :type restore_time: int
        :param database_name: The param of the RestorePoint
        :type database_name: dict(str, str)
        """
        
        

        self._instance_id = None
        self._type = None
        self._backup_id = None
        self._restore_time = None
        self._database_name = None
        self.discriminator = None

        self.instance_id = instance_id
        self.type = type
        if backup_id is not None:
            self.backup_id = backup_id
        if restore_time is not None:
            self.restore_time = restore_time
        if database_name is not None:
            self.database_name = database_name

    @property
    def instance_id(self):
        """Gets the instance_id of this RestorePoint.

        :return: The instance_id of this RestorePoint.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this RestorePoint.

        :param instance_id: The instance_id of this RestorePoint.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def type(self):
        """Gets the type of this RestorePoint.

        :return: The type of this RestorePoint.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RestorePoint.

        :param type: The type of this RestorePoint.
        :type type: str
        """
        self._type = type

    @property
    def backup_id(self):
        """Gets the backup_id of this RestorePoint.

        :return: The backup_id of this RestorePoint.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        """Sets the backup_id of this RestorePoint.

        :param backup_id: The backup_id of this RestorePoint.
        :type backup_id: str
        """
        self._backup_id = backup_id

    @property
    def restore_time(self):
        """Gets the restore_time of this RestorePoint.

        :return: The restore_time of this RestorePoint.
        :rtype: int
        """
        return self._restore_time

    @restore_time.setter
    def restore_time(self, restore_time):
        """Sets the restore_time of this RestorePoint.

        :param restore_time: The restore_time of this RestorePoint.
        :type restore_time: int
        """
        self._restore_time = restore_time

    @property
    def database_name(self):
        """Gets the database_name of this RestorePoint.

        :return: The database_name of this RestorePoint.
        :rtype: dict(str, str)
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this RestorePoint.

        :param database_name: The database_name of this RestorePoint.
        :type database_name: dict(str, str)
        """
        self._database_name = database_name

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
        if not isinstance(other, RestorePoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
