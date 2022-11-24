# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityGroupInfo:

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
        'project_id': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'enterprise_project_id': 'str',
        'security_group_rules': 'list[SecurityGroupRule]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'project_id': 'project_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'enterprise_project_id': 'enterprise_project_id',
        'security_group_rules': 'security_group_rules'
    }

    def __init__(self, id=None, name=None, description=None, project_id=None, created_at=None, updated_at=None, enterprise_project_id=None, security_group_rules=None):
        """SecurityGroupInfo

        The model defined in g42cloud sdk

        :param id: The param of the SecurityGroupInfo
        :type id: str
        :param name: The param of the SecurityGroupInfo
        :type name: str
        :param description: The param of the SecurityGroupInfo
        :type description: str
        :param project_id: The param of the SecurityGroupInfo
        :type project_id: str
        :param created_at: The param of the SecurityGroupInfo
        :type created_at: datetime
        :param updated_at: The param of the SecurityGroupInfo
        :type updated_at: datetime
        :param enterprise_project_id: The param of the SecurityGroupInfo
        :type enterprise_project_id: str
        :param security_group_rules: The param of the SecurityGroupInfo
        :type security_group_rules: list[:class:`g42cloudsdkvpc.v3.SecurityGroupRule`]
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._project_id = None
        self._created_at = None
        self._updated_at = None
        self._enterprise_project_id = None
        self._security_group_rules = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.description = description
        self.project_id = project_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.enterprise_project_id = enterprise_project_id
        self.security_group_rules = security_group_rules

    @property
    def id(self):
        """Gets the id of this SecurityGroupInfo.

        :return: The id of this SecurityGroupInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SecurityGroupInfo.

        :param id: The id of this SecurityGroupInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this SecurityGroupInfo.

        :return: The name of this SecurityGroupInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SecurityGroupInfo.

        :param name: The name of this SecurityGroupInfo.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this SecurityGroupInfo.

        :return: The description of this SecurityGroupInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SecurityGroupInfo.

        :param description: The description of this SecurityGroupInfo.
        :type description: str
        """
        self._description = description

    @property
    def project_id(self):
        """Gets the project_id of this SecurityGroupInfo.

        :return: The project_id of this SecurityGroupInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this SecurityGroupInfo.

        :param project_id: The project_id of this SecurityGroupInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def created_at(self):
        """Gets the created_at of this SecurityGroupInfo.

        :return: The created_at of this SecurityGroupInfo.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this SecurityGroupInfo.

        :param created_at: The created_at of this SecurityGroupInfo.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this SecurityGroupInfo.

        :return: The updated_at of this SecurityGroupInfo.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this SecurityGroupInfo.

        :param updated_at: The updated_at of this SecurityGroupInfo.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this SecurityGroupInfo.

        :return: The enterprise_project_id of this SecurityGroupInfo.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this SecurityGroupInfo.

        :param enterprise_project_id: The enterprise_project_id of this SecurityGroupInfo.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def security_group_rules(self):
        """Gets the security_group_rules of this SecurityGroupInfo.

        :return: The security_group_rules of this SecurityGroupInfo.
        :rtype: list[:class:`g42cloudsdkvpc.v3.SecurityGroupRule`]
        """
        return self._security_group_rules

    @security_group_rules.setter
    def security_group_rules(self, security_group_rules):
        """Sets the security_group_rules of this SecurityGroupInfo.

        :param security_group_rules: The security_group_rules of this SecurityGroupInfo.
        :type security_group_rules: list[:class:`g42cloudsdkvpc.v3.SecurityGroupRule`]
        """
        self._security_group_rules = security_group_rules

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
        if not isinstance(other, SecurityGroupInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
