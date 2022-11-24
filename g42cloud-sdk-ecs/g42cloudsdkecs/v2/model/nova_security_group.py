# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NovaSecurityGroup:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'id': 'str',
        'name': 'str',
        'tenant_id': 'str',
        'rules': 'list[NovaSecurityGroupCommonRule]'
    }

    attribute_map = {
        'description': 'description',
        'id': 'id',
        'name': 'name',
        'tenant_id': 'tenant_id',
        'rules': 'rules'
    }

    def __init__(self, description=None, id=None, name=None, tenant_id=None, rules=None):
        """NovaSecurityGroup

        The model defined in g42cloud sdk

        :param description: The param of the NovaSecurityGroup
        :type description: str
        :param id: The param of the NovaSecurityGroup
        :type id: str
        :param name: The param of the NovaSecurityGroup
        :type name: str
        :param tenant_id: The param of the NovaSecurityGroup
        :type tenant_id: str
        :param rules: The param of the NovaSecurityGroup
        :type rules: list[:class:`g42cloudsdkecs.v2.NovaSecurityGroupCommonRule`]
        """
        
        

        self._description = None
        self._id = None
        self._name = None
        self._tenant_id = None
        self._rules = None
        self.discriminator = None

        self.description = description
        self.id = id
        self.name = name
        self.tenant_id = tenant_id
        self.rules = rules

    @property
    def description(self):
        """Gets the description of this NovaSecurityGroup.

        :return: The description of this NovaSecurityGroup.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NovaSecurityGroup.

        :param description: The description of this NovaSecurityGroup.
        :type description: str
        """
        self._description = description

    @property
    def id(self):
        """Gets the id of this NovaSecurityGroup.

        :return: The id of this NovaSecurityGroup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NovaSecurityGroup.

        :param id: The id of this NovaSecurityGroup.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this NovaSecurityGroup.

        :return: The name of this NovaSecurityGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NovaSecurityGroup.

        :param name: The name of this NovaSecurityGroup.
        :type name: str
        """
        self._name = name

    @property
    def tenant_id(self):
        """Gets the tenant_id of this NovaSecurityGroup.

        :return: The tenant_id of this NovaSecurityGroup.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this NovaSecurityGroup.

        :param tenant_id: The tenant_id of this NovaSecurityGroup.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def rules(self):
        """Gets the rules of this NovaSecurityGroup.

        :return: The rules of this NovaSecurityGroup.
        :rtype: list[:class:`g42cloudsdkecs.v2.NovaSecurityGroupCommonRule`]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this NovaSecurityGroup.

        :param rules: The rules of this NovaSecurityGroup.
        :type rules: list[:class:`g42cloudsdkecs.v2.NovaSecurityGroupCommonRule`]
        """
        self._rules = rules

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
        if not isinstance(other, NovaSecurityGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
