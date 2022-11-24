# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostgresqlListDatabase:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'owner': 'str',
        'character_set': 'str',
        'collate_set': 'str',
        'size': 'int'
    }

    attribute_map = {
        'name': 'name',
        'owner': 'owner',
        'character_set': 'character_set',
        'collate_set': 'collate_set',
        'size': 'size'
    }

    def __init__(self, name=None, owner=None, character_set=None, collate_set=None, size=None):
        """PostgresqlListDatabase

        The model defined in g42cloud sdk

        :param name: The param of the PostgresqlListDatabase
        :type name: str
        :param owner: The param of the PostgresqlListDatabase
        :type owner: str
        :param character_set: The param of the PostgresqlListDatabase
        :type character_set: str
        :param collate_set: The param of the PostgresqlListDatabase
        :type collate_set: str
        :param size: The param of the PostgresqlListDatabase
        :type size: int
        """
        
        

        self._name = None
        self._owner = None
        self._character_set = None
        self._collate_set = None
        self._size = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if owner is not None:
            self.owner = owner
        if character_set is not None:
            self.character_set = character_set
        if collate_set is not None:
            self.collate_set = collate_set
        if size is not None:
            self.size = size

    @property
    def name(self):
        """Gets the name of this PostgresqlListDatabase.

        :return: The name of this PostgresqlListDatabase.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PostgresqlListDatabase.

        :param name: The name of this PostgresqlListDatabase.
        :type name: str
        """
        self._name = name

    @property
    def owner(self):
        """Gets the owner of this PostgresqlListDatabase.

        :return: The owner of this PostgresqlListDatabase.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this PostgresqlListDatabase.

        :param owner: The owner of this PostgresqlListDatabase.
        :type owner: str
        """
        self._owner = owner

    @property
    def character_set(self):
        """Gets the character_set of this PostgresqlListDatabase.

        :return: The character_set of this PostgresqlListDatabase.
        :rtype: str
        """
        return self._character_set

    @character_set.setter
    def character_set(self, character_set):
        """Sets the character_set of this PostgresqlListDatabase.

        :param character_set: The character_set of this PostgresqlListDatabase.
        :type character_set: str
        """
        self._character_set = character_set

    @property
    def collate_set(self):
        """Gets the collate_set of this PostgresqlListDatabase.

        :return: The collate_set of this PostgresqlListDatabase.
        :rtype: str
        """
        return self._collate_set

    @collate_set.setter
    def collate_set(self, collate_set):
        """Sets the collate_set of this PostgresqlListDatabase.

        :param collate_set: The collate_set of this PostgresqlListDatabase.
        :type collate_set: str
        """
        self._collate_set = collate_set

    @property
    def size(self):
        """Gets the size of this PostgresqlListDatabase.

        :return: The size of this PostgresqlListDatabase.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this PostgresqlListDatabase.

        :param size: The size of this PostgresqlListDatabase.
        :type size: int
        """
        self._size = size

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
        if not isinstance(other, PostgresqlListDatabase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
