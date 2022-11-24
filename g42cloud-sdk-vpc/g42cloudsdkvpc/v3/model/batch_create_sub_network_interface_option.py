# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateSubNetworkInterfaceOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'virsubnet_id': 'str',
        'parent_id': 'str',
        'security_groups': 'list[str]',
        'description': 'str',
        'ipv6_enable': 'bool',
        'project_id': 'str'
    }

    attribute_map = {
        'virsubnet_id': 'virsubnet_id',
        'parent_id': 'parent_id',
        'security_groups': 'security_groups',
        'description': 'description',
        'ipv6_enable': 'ipv6_enable',
        'project_id': 'project_id'
    }

    def __init__(self, virsubnet_id=None, parent_id=None, security_groups=None, description=None, ipv6_enable=None, project_id=None):
        """BatchCreateSubNetworkInterfaceOption

        The model defined in g42cloud sdk

        :param virsubnet_id: The param of the BatchCreateSubNetworkInterfaceOption
        :type virsubnet_id: str
        :param parent_id: The param of the BatchCreateSubNetworkInterfaceOption
        :type parent_id: str
        :param security_groups: The param of the BatchCreateSubNetworkInterfaceOption
        :type security_groups: list[str]
        :param description: The param of the BatchCreateSubNetworkInterfaceOption
        :type description: str
        :param ipv6_enable: The param of the BatchCreateSubNetworkInterfaceOption
        :type ipv6_enable: bool
        :param project_id: The param of the BatchCreateSubNetworkInterfaceOption
        :type project_id: str
        """
        
        

        self._virsubnet_id = None
        self._parent_id = None
        self._security_groups = None
        self._description = None
        self._ipv6_enable = None
        self._project_id = None
        self.discriminator = None

        self.virsubnet_id = virsubnet_id
        self.parent_id = parent_id
        if security_groups is not None:
            self.security_groups = security_groups
        if description is not None:
            self.description = description
        if ipv6_enable is not None:
            self.ipv6_enable = ipv6_enable
        if project_id is not None:
            self.project_id = project_id

    @property
    def virsubnet_id(self):
        """Gets the virsubnet_id of this BatchCreateSubNetworkInterfaceOption.

        :return: The virsubnet_id of this BatchCreateSubNetworkInterfaceOption.
        :rtype: str
        """
        return self._virsubnet_id

    @virsubnet_id.setter
    def virsubnet_id(self, virsubnet_id):
        """Sets the virsubnet_id of this BatchCreateSubNetworkInterfaceOption.

        :param virsubnet_id: The virsubnet_id of this BatchCreateSubNetworkInterfaceOption.
        :type virsubnet_id: str
        """
        self._virsubnet_id = virsubnet_id

    @property
    def parent_id(self):
        """Gets the parent_id of this BatchCreateSubNetworkInterfaceOption.

        :return: The parent_id of this BatchCreateSubNetworkInterfaceOption.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this BatchCreateSubNetworkInterfaceOption.

        :param parent_id: The parent_id of this BatchCreateSubNetworkInterfaceOption.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def security_groups(self):
        """Gets the security_groups of this BatchCreateSubNetworkInterfaceOption.

        :return: The security_groups of this BatchCreateSubNetworkInterfaceOption.
        :rtype: list[str]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this BatchCreateSubNetworkInterfaceOption.

        :param security_groups: The security_groups of this BatchCreateSubNetworkInterfaceOption.
        :type security_groups: list[str]
        """
        self._security_groups = security_groups

    @property
    def description(self):
        """Gets the description of this BatchCreateSubNetworkInterfaceOption.

        :return: The description of this BatchCreateSubNetworkInterfaceOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BatchCreateSubNetworkInterfaceOption.

        :param description: The description of this BatchCreateSubNetworkInterfaceOption.
        :type description: str
        """
        self._description = description

    @property
    def ipv6_enable(self):
        """Gets the ipv6_enable of this BatchCreateSubNetworkInterfaceOption.

        :return: The ipv6_enable of this BatchCreateSubNetworkInterfaceOption.
        :rtype: bool
        """
        return self._ipv6_enable

    @ipv6_enable.setter
    def ipv6_enable(self, ipv6_enable):
        """Sets the ipv6_enable of this BatchCreateSubNetworkInterfaceOption.

        :param ipv6_enable: The ipv6_enable of this BatchCreateSubNetworkInterfaceOption.
        :type ipv6_enable: bool
        """
        self._ipv6_enable = ipv6_enable

    @property
    def project_id(self):
        """Gets the project_id of this BatchCreateSubNetworkInterfaceOption.

        :return: The project_id of this BatchCreateSubNetworkInterfaceOption.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this BatchCreateSubNetworkInterfaceOption.

        :param project_id: The project_id of this BatchCreateSubNetworkInterfaceOption.
        :type project_id: str
        """
        self._project_id = project_id

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
        if not isinstance(other, BatchCreateSubNetworkInterfaceOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
