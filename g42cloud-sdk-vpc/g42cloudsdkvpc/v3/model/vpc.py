# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Vpc:

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
        'name': 'str',
        'description': 'str',
        'cidr': 'str',
        'extend_cidrs': 'list[str]',
        'status': 'str',
        'project_id': 'str',
        'enterprise_project_id': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'cloud_resources': 'list[CloudResource]',
        'tags': 'list[Tag]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'cidr': 'cidr',
        'extend_cidrs': 'extend_cidrs',
        'status': 'status',
        'project_id': 'project_id',
        'enterprise_project_id': 'enterprise_project_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'cloud_resources': 'cloud_resources',
        'tags': 'tags'
    }

    def __init__(self, id=None, name=None, description=None, cidr=None, extend_cidrs=None, status=None, project_id=None, enterprise_project_id=None, created_at=None, updated_at=None, cloud_resources=None, tags=None):
        """Vpc

        The model defined in g42cloud sdk

        :param id: The param of the Vpc
        :type id: str
        :param name: The param of the Vpc
        :type name: str
        :param description: The param of the Vpc
        :type description: str
        :param cidr: The param of the Vpc
        :type cidr: str
        :param extend_cidrs: The param of the Vpc
        :type extend_cidrs: list[str]
        :param status: The param of the Vpc
        :type status: str
        :param project_id: The param of the Vpc
        :type project_id: str
        :param enterprise_project_id: The param of the Vpc
        :type enterprise_project_id: str
        :param created_at: The param of the Vpc
        :type created_at: datetime
        :param updated_at: The param of the Vpc
        :type updated_at: datetime
        :param cloud_resources: The param of the Vpc
        :type cloud_resources: list[:class:`g42cloudsdkvpc.v3.CloudResource`]
        :param tags: The param of the Vpc
        :type tags: list[:class:`g42cloudsdkvpc.v3.Tag`]
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._cidr = None
        self._extend_cidrs = None
        self._status = None
        self._project_id = None
        self._enterprise_project_id = None
        self._created_at = None
        self._updated_at = None
        self._cloud_resources = None
        self._tags = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.description = description
        self.cidr = cidr
        self.extend_cidrs = extend_cidrs
        self.status = status
        self.project_id = project_id
        self.enterprise_project_id = enterprise_project_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.cloud_resources = cloud_resources
        self.tags = tags

    @property
    def id(self):
        """Gets the id of this Vpc.

        :return: The id of this Vpc.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Vpc.

        :param id: The id of this Vpc.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this Vpc.

        :return: The name of this Vpc.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Vpc.

        :param name: The name of this Vpc.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this Vpc.

        :return: The description of this Vpc.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Vpc.

        :param description: The description of this Vpc.
        :type description: str
        """
        self._description = description

    @property
    def cidr(self):
        """Gets the cidr of this Vpc.

        :return: The cidr of this Vpc.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this Vpc.

        :param cidr: The cidr of this Vpc.
        :type cidr: str
        """
        self._cidr = cidr

    @property
    def extend_cidrs(self):
        """Gets the extend_cidrs of this Vpc.

        :return: The extend_cidrs of this Vpc.
        :rtype: list[str]
        """
        return self._extend_cidrs

    @extend_cidrs.setter
    def extend_cidrs(self, extend_cidrs):
        """Sets the extend_cidrs of this Vpc.

        :param extend_cidrs: The extend_cidrs of this Vpc.
        :type extend_cidrs: list[str]
        """
        self._extend_cidrs = extend_cidrs

    @property
    def status(self):
        """Gets the status of this Vpc.

        :return: The status of this Vpc.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Vpc.

        :param status: The status of this Vpc.
        :type status: str
        """
        self._status = status

    @property
    def project_id(self):
        """Gets the project_id of this Vpc.

        :return: The project_id of this Vpc.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Vpc.

        :param project_id: The project_id of this Vpc.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this Vpc.

        :return: The enterprise_project_id of this Vpc.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this Vpc.

        :param enterprise_project_id: The enterprise_project_id of this Vpc.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def created_at(self):
        """Gets the created_at of this Vpc.

        :return: The created_at of this Vpc.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Vpc.

        :param created_at: The created_at of this Vpc.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Vpc.

        :return: The updated_at of this Vpc.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Vpc.

        :param updated_at: The updated_at of this Vpc.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def cloud_resources(self):
        """Gets the cloud_resources of this Vpc.

        :return: The cloud_resources of this Vpc.
        :rtype: list[:class:`g42cloudsdkvpc.v3.CloudResource`]
        """
        return self._cloud_resources

    @cloud_resources.setter
    def cloud_resources(self, cloud_resources):
        """Sets the cloud_resources of this Vpc.

        :param cloud_resources: The cloud_resources of this Vpc.
        :type cloud_resources: list[:class:`g42cloudsdkvpc.v3.CloudResource`]
        """
        self._cloud_resources = cloud_resources

    @property
    def tags(self):
        """Gets the tags of this Vpc.

        :return: The tags of this Vpc.
        :rtype: list[:class:`g42cloudsdkvpc.v3.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Vpc.

        :param tags: The tags of this Vpc.
        :type tags: list[:class:`g42cloudsdkvpc.v3.Tag`]
        """
        self._tags = tags

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
        if not isinstance(other, Vpc):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
