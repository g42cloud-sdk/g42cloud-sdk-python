# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class Member:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'backup_id': 'str',
        'image_id': 'str',
        'dest_project_id': 'str',
        'vault_id': 'str',
        'id': 'str'
    }

    attribute_map = {
        'status': 'status',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'backup_id': 'backup_id',
        'image_id': 'image_id',
        'dest_project_id': 'dest_project_id',
        'vault_id': 'vault_id',
        'id': 'id'
    }

    def __init__(self, status=None, created_at=None, updated_at=None, backup_id=None, image_id=None, dest_project_id=None, vault_id=None, id=None):
        """Member

        The model defined in g42cloud sdk

        :param status: The param of the Member
        :type status: str
        :param created_at: The param of the Member
        :type created_at: str
        :param updated_at: The param of the Member
        :type updated_at: str
        :param backup_id: The param of the Member
        :type backup_id: str
        :param image_id: The param of the Member
        :type image_id: str
        :param dest_project_id: The param of the Member
        :type dest_project_id: str
        :param vault_id: The param of the Member
        :type vault_id: str
        :param id: The param of the Member
        :type id: str
        """
        
        

        self._status = None
        self._created_at = None
        self._updated_at = None
        self._backup_id = None
        self._image_id = None
        self._dest_project_id = None
        self._vault_id = None
        self._id = None
        self.discriminator = None

        self.status = status
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if backup_id is not None:
            self.backup_id = backup_id
        if image_id is not None:
            self.image_id = image_id
        if dest_project_id is not None:
            self.dest_project_id = dest_project_id
        if vault_id is not None:
            self.vault_id = vault_id
        if id is not None:
            self.id = id

    @property
    def status(self):
        """Gets the status of this Member.

        :return: The status of this Member.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Member.

        :param status: The status of this Member.
        :type status: str
        """
        self._status = status

    @property
    def created_at(self):
        """Gets the created_at of this Member.

        :return: The created_at of this Member.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Member.

        :param created_at: The created_at of this Member.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Member.

        :return: The updated_at of this Member.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Member.

        :param updated_at: The updated_at of this Member.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def backup_id(self):
        """Gets the backup_id of this Member.

        :return: The backup_id of this Member.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        """Sets the backup_id of this Member.

        :param backup_id: The backup_id of this Member.
        :type backup_id: str
        """
        self._backup_id = backup_id

    @property
    def image_id(self):
        """Gets the image_id of this Member.

        :return: The image_id of this Member.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this Member.

        :param image_id: The image_id of this Member.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def dest_project_id(self):
        """Gets the dest_project_id of this Member.

        :return: The dest_project_id of this Member.
        :rtype: str
        """
        return self._dest_project_id

    @dest_project_id.setter
    def dest_project_id(self, dest_project_id):
        """Sets the dest_project_id of this Member.

        :param dest_project_id: The dest_project_id of this Member.
        :type dest_project_id: str
        """
        self._dest_project_id = dest_project_id

    @property
    def vault_id(self):
        """Gets the vault_id of this Member.

        :return: The vault_id of this Member.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        """Sets the vault_id of this Member.

        :param vault_id: The vault_id of this Member.
        :type vault_id: str
        """
        self._vault_id = vault_id

    @property
    def id(self):
        """Gets the id of this Member.

        :return: The id of this Member.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Member.

        :param id: The id of this Member.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, Member):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
