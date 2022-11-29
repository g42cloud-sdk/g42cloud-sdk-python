# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateMemberOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'address': 'str',
        'admin_state_up': 'bool',
        'name': 'str',
        'project_id': 'str',
        'protocol_port': 'int',
        'subnet_cidr_id': 'str',
        'weight': 'int'
    }

    attribute_map = {
        'address': 'address',
        'admin_state_up': 'admin_state_up',
        'name': 'name',
        'project_id': 'project_id',
        'protocol_port': 'protocol_port',
        'subnet_cidr_id': 'subnet_cidr_id',
        'weight': 'weight'
    }

    def __init__(self, address=None, admin_state_up=None, name=None, project_id=None, protocol_port=None, subnet_cidr_id=None, weight=None):
        """CreateMemberOption

        The model defined in g42cloud sdk

        :param address: The param of the CreateMemberOption
        :type address: str
        :param admin_state_up: The param of the CreateMemberOption
        :type admin_state_up: bool
        :param name: The param of the CreateMemberOption
        :type name: str
        :param project_id: The param of the CreateMemberOption
        :type project_id: str
        :param protocol_port: The param of the CreateMemberOption
        :type protocol_port: int
        :param subnet_cidr_id: The param of the CreateMemberOption
        :type subnet_cidr_id: str
        :param weight: The param of the CreateMemberOption
        :type weight: int
        """
        
        

        self._address = None
        self._admin_state_up = None
        self._name = None
        self._project_id = None
        self._protocol_port = None
        self._subnet_cidr_id = None
        self._weight = None
        self.discriminator = None

        self.address = address
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if name is not None:
            self.name = name
        if project_id is not None:
            self.project_id = project_id
        self.protocol_port = protocol_port
        if subnet_cidr_id is not None:
            self.subnet_cidr_id = subnet_cidr_id
        if weight is not None:
            self.weight = weight

    @property
    def address(self):
        """Gets the address of this CreateMemberOption.

        :return: The address of this CreateMemberOption.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this CreateMemberOption.

        :param address: The address of this CreateMemberOption.
        :type address: str
        """
        self._address = address

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this CreateMemberOption.

        :return: The admin_state_up of this CreateMemberOption.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this CreateMemberOption.

        :param admin_state_up: The admin_state_up of this CreateMemberOption.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def name(self):
        """Gets the name of this CreateMemberOption.

        :return: The name of this CreateMemberOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateMemberOption.

        :param name: The name of this CreateMemberOption.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        """Gets the project_id of this CreateMemberOption.

        :return: The project_id of this CreateMemberOption.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreateMemberOption.

        :param project_id: The project_id of this CreateMemberOption.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def protocol_port(self):
        """Gets the protocol_port of this CreateMemberOption.

        :return: The protocol_port of this CreateMemberOption.
        :rtype: int
        """
        return self._protocol_port

    @protocol_port.setter
    def protocol_port(self, protocol_port):
        """Sets the protocol_port of this CreateMemberOption.

        :param protocol_port: The protocol_port of this CreateMemberOption.
        :type protocol_port: int
        """
        self._protocol_port = protocol_port

    @property
    def subnet_cidr_id(self):
        """Gets the subnet_cidr_id of this CreateMemberOption.

        :return: The subnet_cidr_id of this CreateMemberOption.
        :rtype: str
        """
        return self._subnet_cidr_id

    @subnet_cidr_id.setter
    def subnet_cidr_id(self, subnet_cidr_id):
        """Sets the subnet_cidr_id of this CreateMemberOption.

        :param subnet_cidr_id: The subnet_cidr_id of this CreateMemberOption.
        :type subnet_cidr_id: str
        """
        self._subnet_cidr_id = subnet_cidr_id

    @property
    def weight(self):
        """Gets the weight of this CreateMemberOption.

        :return: The weight of this CreateMemberOption.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this CreateMemberOption.

        :param weight: The weight of this CreateMemberOption.
        :type weight: int
        """
        self._weight = weight

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
        if not isinstance(other, CreateMemberOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
