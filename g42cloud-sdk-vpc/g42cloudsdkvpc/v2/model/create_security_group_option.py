# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSecurityGroupOption:

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
        'vpc_id': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'vpc_id': 'vpc_id',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, name=None, vpc_id=None, enterprise_project_id=None):
        """CreateSecurityGroupOption

        The model defined in g42cloud sdk

        :param name: The param of the CreateSecurityGroupOption
        :type name: str
        :param vpc_id: The param of the CreateSecurityGroupOption
        :type vpc_id: str
        :param enterprise_project_id: The param of the CreateSecurityGroupOption
        :type enterprise_project_id: str
        """
        
        

        self._name = None
        self._vpc_id = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.name = name
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def name(self):
        """Gets the name of this CreateSecurityGroupOption.

        :return: The name of this CreateSecurityGroupOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateSecurityGroupOption.

        :param name: The name of this CreateSecurityGroupOption.
        :type name: str
        """
        self._name = name

    @property
    def vpc_id(self):
        """Gets the vpc_id of this CreateSecurityGroupOption.

        :return: The vpc_id of this CreateSecurityGroupOption.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this CreateSecurityGroupOption.

        :param vpc_id: The vpc_id of this CreateSecurityGroupOption.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateSecurityGroupOption.

        :return: The enterprise_project_id of this CreateSecurityGroupOption.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateSecurityGroupOption.

        :param enterprise_project_id: The enterprise_project_id of this CreateSecurityGroupOption.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, CreateSecurityGroupOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
