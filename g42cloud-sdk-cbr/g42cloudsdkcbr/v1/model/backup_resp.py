# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackupResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'checkpoint_id': 'str',
        'created_at': 'datetime',
        'description': 'str',
        'expired_at': 'datetime',
        'extend_info': 'BackupExtendInfo',
        'id': 'str',
        'image_type': 'str',
        'name': 'str',
        'parent_id': 'str',
        'project_id': 'str',
        'protected_at': 'date',
        'resource_az': 'str',
        'resource_id': 'str',
        'resource_name': 'str',
        'resource_size': 'int',
        'resource_type': 'str',
        'status': 'str',
        'updated_at': 'datetime',
        'vault_id': 'str',
        'replication_records': 'list[ReplicationRecordGet]',
        'enterprise_project_id': 'str',
        'provider_id': 'str',
        'children': 'list[BackupResp]'
    }

    attribute_map = {
        'checkpoint_id': 'checkpoint_id',
        'created_at': 'created_at',
        'description': 'description',
        'expired_at': 'expired_at',
        'extend_info': 'extend_info',
        'id': 'id',
        'image_type': 'image_type',
        'name': 'name',
        'parent_id': 'parent_id',
        'project_id': 'project_id',
        'protected_at': 'protected_at',
        'resource_az': 'resource_az',
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'resource_size': 'resource_size',
        'resource_type': 'resource_type',
        'status': 'status',
        'updated_at': 'updated_at',
        'vault_id': 'vault_id',
        'replication_records': 'replication_records',
        'enterprise_project_id': 'enterprise_project_id',
        'provider_id': 'provider_id',
        'children': 'children'
    }

    def __init__(self, checkpoint_id=None, created_at=None, description=None, expired_at=None, extend_info=None, id=None, image_type=None, name=None, parent_id=None, project_id=None, protected_at=None, resource_az=None, resource_id=None, resource_name=None, resource_size=None, resource_type=None, status=None, updated_at=None, vault_id=None, replication_records=None, enterprise_project_id=None, provider_id=None, children=None):
        """BackupResp

        The model defined in g42cloud sdk

        :param checkpoint_id: The param of the BackupResp
        :type checkpoint_id: str
        :param created_at: The param of the BackupResp
        :type created_at: datetime
        :param description: The param of the BackupResp
        :type description: str
        :param expired_at: The param of the BackupResp
        :type expired_at: datetime
        :param extend_info: The param of the BackupResp
        :type extend_info: :class:`g42cloudsdkcbr.v1.BackupExtendInfo`
        :param id: The param of the BackupResp
        :type id: str
        :param image_type: The param of the BackupResp
        :type image_type: str
        :param name: The param of the BackupResp
        :type name: str
        :param parent_id: The param of the BackupResp
        :type parent_id: str
        :param project_id: The param of the BackupResp
        :type project_id: str
        :param protected_at: The param of the BackupResp
        :type protected_at: date
        :param resource_az: The param of the BackupResp
        :type resource_az: str
        :param resource_id: The param of the BackupResp
        :type resource_id: str
        :param resource_name: The param of the BackupResp
        :type resource_name: str
        :param resource_size: The param of the BackupResp
        :type resource_size: int
        :param resource_type: The param of the BackupResp
        :type resource_type: str
        :param status: The param of the BackupResp
        :type status: str
        :param updated_at: The param of the BackupResp
        :type updated_at: datetime
        :param vault_id: The param of the BackupResp
        :type vault_id: str
        :param replication_records: The param of the BackupResp
        :type replication_records: list[:class:`g42cloudsdkcbr.v1.ReplicationRecordGet`]
        :param enterprise_project_id: The param of the BackupResp
        :type enterprise_project_id: str
        :param provider_id: The param of the BackupResp
        :type provider_id: str
        :param children: The param of the BackupResp
        :type children: list[:class:`g42cloudsdkcbr.v1.BackupResp`]
        """
        
        

        self._checkpoint_id = None
        self._created_at = None
        self._description = None
        self._expired_at = None
        self._extend_info = None
        self._id = None
        self._image_type = None
        self._name = None
        self._parent_id = None
        self._project_id = None
        self._protected_at = None
        self._resource_az = None
        self._resource_id = None
        self._resource_name = None
        self._resource_size = None
        self._resource_type = None
        self._status = None
        self._updated_at = None
        self._vault_id = None
        self._replication_records = None
        self._enterprise_project_id = None
        self._provider_id = None
        self._children = None
        self.discriminator = None

        self.checkpoint_id = checkpoint_id
        self.created_at = created_at
        self.description = description
        self.expired_at = expired_at
        self.extend_info = extend_info
        self.id = id
        self.image_type = image_type
        self.name = name
        self.parent_id = parent_id
        self.project_id = project_id
        self.protected_at = protected_at
        self.resource_az = resource_az
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_size = resource_size
        self.resource_type = resource_type
        self.status = status
        self.updated_at = updated_at
        self.vault_id = vault_id
        if replication_records is not None:
            self.replication_records = replication_records
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.provider_id = provider_id
        if children is not None:
            self.children = children

    @property
    def checkpoint_id(self):
        """Gets the checkpoint_id of this BackupResp.

        :return: The checkpoint_id of this BackupResp.
        :rtype: str
        """
        return self._checkpoint_id

    @checkpoint_id.setter
    def checkpoint_id(self, checkpoint_id):
        """Sets the checkpoint_id of this BackupResp.

        :param checkpoint_id: The checkpoint_id of this BackupResp.
        :type checkpoint_id: str
        """
        self._checkpoint_id = checkpoint_id

    @property
    def created_at(self):
        """Gets the created_at of this BackupResp.

        :return: The created_at of this BackupResp.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this BackupResp.

        :param created_at: The created_at of this BackupResp.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def description(self):
        """Gets the description of this BackupResp.

        :return: The description of this BackupResp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BackupResp.

        :param description: The description of this BackupResp.
        :type description: str
        """
        self._description = description

    @property
    def expired_at(self):
        """Gets the expired_at of this BackupResp.

        :return: The expired_at of this BackupResp.
        :rtype: datetime
        """
        return self._expired_at

    @expired_at.setter
    def expired_at(self, expired_at):
        """Sets the expired_at of this BackupResp.

        :param expired_at: The expired_at of this BackupResp.
        :type expired_at: datetime
        """
        self._expired_at = expired_at

    @property
    def extend_info(self):
        """Gets the extend_info of this BackupResp.

        :return: The extend_info of this BackupResp.
        :rtype: :class:`g42cloudsdkcbr.v1.BackupExtendInfo`
        """
        return self._extend_info

    @extend_info.setter
    def extend_info(self, extend_info):
        """Sets the extend_info of this BackupResp.

        :param extend_info: The extend_info of this BackupResp.
        :type extend_info: :class:`g42cloudsdkcbr.v1.BackupExtendInfo`
        """
        self._extend_info = extend_info

    @property
    def id(self):
        """Gets the id of this BackupResp.

        :return: The id of this BackupResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BackupResp.

        :param id: The id of this BackupResp.
        :type id: str
        """
        self._id = id

    @property
    def image_type(self):
        """Gets the image_type of this BackupResp.

        :return: The image_type of this BackupResp.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        """Sets the image_type of this BackupResp.

        :param image_type: The image_type of this BackupResp.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def name(self):
        """Gets the name of this BackupResp.

        :return: The name of this BackupResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BackupResp.

        :param name: The name of this BackupResp.
        :type name: str
        """
        self._name = name

    @property
    def parent_id(self):
        """Gets the parent_id of this BackupResp.

        :return: The parent_id of this BackupResp.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this BackupResp.

        :param parent_id: The parent_id of this BackupResp.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def project_id(self):
        """Gets the project_id of this BackupResp.

        :return: The project_id of this BackupResp.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this BackupResp.

        :param project_id: The project_id of this BackupResp.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def protected_at(self):
        """Gets the protected_at of this BackupResp.

        :return: The protected_at of this BackupResp.
        :rtype: date
        """
        return self._protected_at

    @protected_at.setter
    def protected_at(self, protected_at):
        """Sets the protected_at of this BackupResp.

        :param protected_at: The protected_at of this BackupResp.
        :type protected_at: date
        """
        self._protected_at = protected_at

    @property
    def resource_az(self):
        """Gets the resource_az of this BackupResp.

        :return: The resource_az of this BackupResp.
        :rtype: str
        """
        return self._resource_az

    @resource_az.setter
    def resource_az(self, resource_az):
        """Sets the resource_az of this BackupResp.

        :param resource_az: The resource_az of this BackupResp.
        :type resource_az: str
        """
        self._resource_az = resource_az

    @property
    def resource_id(self):
        """Gets the resource_id of this BackupResp.

        :return: The resource_id of this BackupResp.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this BackupResp.

        :param resource_id: The resource_id of this BackupResp.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        """Gets the resource_name of this BackupResp.

        :return: The resource_name of this BackupResp.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this BackupResp.

        :param resource_name: The resource_name of this BackupResp.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def resource_size(self):
        """Gets the resource_size of this BackupResp.

        :return: The resource_size of this BackupResp.
        :rtype: int
        """
        return self._resource_size

    @resource_size.setter
    def resource_size(self, resource_size):
        """Sets the resource_size of this BackupResp.

        :param resource_size: The resource_size of this BackupResp.
        :type resource_size: int
        """
        self._resource_size = resource_size

    @property
    def resource_type(self):
        """Gets the resource_type of this BackupResp.

        :return: The resource_type of this BackupResp.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this BackupResp.

        :param resource_type: The resource_type of this BackupResp.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def status(self):
        """Gets the status of this BackupResp.

        :return: The status of this BackupResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BackupResp.

        :param status: The status of this BackupResp.
        :type status: str
        """
        self._status = status

    @property
    def updated_at(self):
        """Gets the updated_at of this BackupResp.

        :return: The updated_at of this BackupResp.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this BackupResp.

        :param updated_at: The updated_at of this BackupResp.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def vault_id(self):
        """Gets the vault_id of this BackupResp.

        :return: The vault_id of this BackupResp.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        """Sets the vault_id of this BackupResp.

        :param vault_id: The vault_id of this BackupResp.
        :type vault_id: str
        """
        self._vault_id = vault_id

    @property
    def replication_records(self):
        """Gets the replication_records of this BackupResp.

        :return: The replication_records of this BackupResp.
        :rtype: list[:class:`g42cloudsdkcbr.v1.ReplicationRecordGet`]
        """
        return self._replication_records

    @replication_records.setter
    def replication_records(self, replication_records):
        """Sets the replication_records of this BackupResp.

        :param replication_records: The replication_records of this BackupResp.
        :type replication_records: list[:class:`g42cloudsdkcbr.v1.ReplicationRecordGet`]
        """
        self._replication_records = replication_records

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this BackupResp.

        :return: The enterprise_project_id of this BackupResp.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this BackupResp.

        :param enterprise_project_id: The enterprise_project_id of this BackupResp.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def provider_id(self):
        """Gets the provider_id of this BackupResp.

        :return: The provider_id of this BackupResp.
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        """Sets the provider_id of this BackupResp.

        :param provider_id: The provider_id of this BackupResp.
        :type provider_id: str
        """
        self._provider_id = provider_id

    @property
    def children(self):
        """Gets the children of this BackupResp.

        :return: The children of this BackupResp.
        :rtype: list[:class:`g42cloudsdkcbr.v1.BackupResp`]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this BackupResp.

        :param children: The children of this BackupResp.
        :type children: list[:class:`g42cloudsdkcbr.v1.BackupResp`]
        """
        self._children = children

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
        if not isinstance(other, BackupResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
