# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSubNetworkInterfaceOption:

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
        'vlan_id': 'str',
        'parent_id': 'str',
        'description': 'str',
        'ipv6_enable': 'bool',
        'private_ip_address': 'str',
        'ipv6_ip_address': 'str',
        'security_groups': 'list[str]',
        'project_id': 'str'
    }

    attribute_map = {
        'virsubnet_id': 'virsubnet_id',
        'vlan_id': 'vlan_id',
        'parent_id': 'parent_id',
        'description': 'description',
        'ipv6_enable': 'ipv6_enable',
        'private_ip_address': 'private_ip_address',
        'ipv6_ip_address': 'ipv6_ip_address',
        'security_groups': 'security_groups',
        'project_id': 'project_id'
    }

    def __init__(self, virsubnet_id=None, vlan_id=None, parent_id=None, description=None, ipv6_enable=None, private_ip_address=None, ipv6_ip_address=None, security_groups=None, project_id=None):
        """CreateSubNetworkInterfaceOption

        The model defined in g42cloud sdk

        :param virsubnet_id: The param of the CreateSubNetworkInterfaceOption
        :type virsubnet_id: str
        :param vlan_id: The param of the CreateSubNetworkInterfaceOption
        :type vlan_id: str
        :param parent_id: The param of the CreateSubNetworkInterfaceOption
        :type parent_id: str
        :param description: The param of the CreateSubNetworkInterfaceOption
        :type description: str
        :param ipv6_enable: The param of the CreateSubNetworkInterfaceOption
        :type ipv6_enable: bool
        :param private_ip_address: The param of the CreateSubNetworkInterfaceOption
        :type private_ip_address: str
        :param ipv6_ip_address: The param of the CreateSubNetworkInterfaceOption
        :type ipv6_ip_address: str
        :param security_groups: The param of the CreateSubNetworkInterfaceOption
        :type security_groups: list[str]
        :param project_id: The param of the CreateSubNetworkInterfaceOption
        :type project_id: str
        """
        
        

        self._virsubnet_id = None
        self._vlan_id = None
        self._parent_id = None
        self._description = None
        self._ipv6_enable = None
        self._private_ip_address = None
        self._ipv6_ip_address = None
        self._security_groups = None
        self._project_id = None
        self.discriminator = None

        self.virsubnet_id = virsubnet_id
        if vlan_id is not None:
            self.vlan_id = vlan_id
        self.parent_id = parent_id
        if description is not None:
            self.description = description
        if ipv6_enable is not None:
            self.ipv6_enable = ipv6_enable
        if private_ip_address is not None:
            self.private_ip_address = private_ip_address
        if ipv6_ip_address is not None:
            self.ipv6_ip_address = ipv6_ip_address
        if security_groups is not None:
            self.security_groups = security_groups
        if project_id is not None:
            self.project_id = project_id

    @property
    def virsubnet_id(self):
        """Gets the virsubnet_id of this CreateSubNetworkInterfaceOption.

        :return: The virsubnet_id of this CreateSubNetworkInterfaceOption.
        :rtype: str
        """
        return self._virsubnet_id

    @virsubnet_id.setter
    def virsubnet_id(self, virsubnet_id):
        """Sets the virsubnet_id of this CreateSubNetworkInterfaceOption.

        :param virsubnet_id: The virsubnet_id of this CreateSubNetworkInterfaceOption.
        :type virsubnet_id: str
        """
        self._virsubnet_id = virsubnet_id

    @property
    def vlan_id(self):
        """Gets the vlan_id of this CreateSubNetworkInterfaceOption.

        :return: The vlan_id of this CreateSubNetworkInterfaceOption.
        :rtype: str
        """
        return self._vlan_id

    @vlan_id.setter
    def vlan_id(self, vlan_id):
        """Sets the vlan_id of this CreateSubNetworkInterfaceOption.

        :param vlan_id: The vlan_id of this CreateSubNetworkInterfaceOption.
        :type vlan_id: str
        """
        self._vlan_id = vlan_id

    @property
    def parent_id(self):
        """Gets the parent_id of this CreateSubNetworkInterfaceOption.

        :return: The parent_id of this CreateSubNetworkInterfaceOption.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this CreateSubNetworkInterfaceOption.

        :param parent_id: The parent_id of this CreateSubNetworkInterfaceOption.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def description(self):
        """Gets the description of this CreateSubNetworkInterfaceOption.

        :return: The description of this CreateSubNetworkInterfaceOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateSubNetworkInterfaceOption.

        :param description: The description of this CreateSubNetworkInterfaceOption.
        :type description: str
        """
        self._description = description

    @property
    def ipv6_enable(self):
        """Gets the ipv6_enable of this CreateSubNetworkInterfaceOption.

        :return: The ipv6_enable of this CreateSubNetworkInterfaceOption.
        :rtype: bool
        """
        return self._ipv6_enable

    @ipv6_enable.setter
    def ipv6_enable(self, ipv6_enable):
        """Sets the ipv6_enable of this CreateSubNetworkInterfaceOption.

        :param ipv6_enable: The ipv6_enable of this CreateSubNetworkInterfaceOption.
        :type ipv6_enable: bool
        """
        self._ipv6_enable = ipv6_enable

    @property
    def private_ip_address(self):
        """Gets the private_ip_address of this CreateSubNetworkInterfaceOption.

        :return: The private_ip_address of this CreateSubNetworkInterfaceOption.
        :rtype: str
        """
        return self._private_ip_address

    @private_ip_address.setter
    def private_ip_address(self, private_ip_address):
        """Sets the private_ip_address of this CreateSubNetworkInterfaceOption.

        :param private_ip_address: The private_ip_address of this CreateSubNetworkInterfaceOption.
        :type private_ip_address: str
        """
        self._private_ip_address = private_ip_address

    @property
    def ipv6_ip_address(self):
        """Gets the ipv6_ip_address of this CreateSubNetworkInterfaceOption.

        :return: The ipv6_ip_address of this CreateSubNetworkInterfaceOption.
        :rtype: str
        """
        return self._ipv6_ip_address

    @ipv6_ip_address.setter
    def ipv6_ip_address(self, ipv6_ip_address):
        """Sets the ipv6_ip_address of this CreateSubNetworkInterfaceOption.

        :param ipv6_ip_address: The ipv6_ip_address of this CreateSubNetworkInterfaceOption.
        :type ipv6_ip_address: str
        """
        self._ipv6_ip_address = ipv6_ip_address

    @property
    def security_groups(self):
        """Gets the security_groups of this CreateSubNetworkInterfaceOption.

        :return: The security_groups of this CreateSubNetworkInterfaceOption.
        :rtype: list[str]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this CreateSubNetworkInterfaceOption.

        :param security_groups: The security_groups of this CreateSubNetworkInterfaceOption.
        :type security_groups: list[str]
        """
        self._security_groups = security_groups

    @property
    def project_id(self):
        """Gets the project_id of this CreateSubNetworkInterfaceOption.

        :return: The project_id of this CreateSubNetworkInterfaceOption.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreateSubNetworkInterfaceOption.

        :param project_id: The project_id of this CreateSubNetworkInterfaceOption.
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
        if not isinstance(other, CreateSubNetworkInterfaceOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
