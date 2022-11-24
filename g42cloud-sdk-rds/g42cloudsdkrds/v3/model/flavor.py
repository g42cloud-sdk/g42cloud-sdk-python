# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Flavor:

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
        'vcpus': 'str',
        'ram': 'int',
        'spec_code': 'str',
        'instance_mode': 'str',
        'az_status': 'dict(str, str)',
        'az_desc': 'dict(str, str)',
        'version_name': 'list[str]',
        'group_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'vcpus': 'vcpus',
        'ram': 'ram',
        'spec_code': 'spec_code',
        'instance_mode': 'instance_mode',
        'az_status': 'az_status',
        'az_desc': 'az_desc',
        'version_name': 'version_name',
        'group_type': 'group_type'
    }

    def __init__(self, id=None, vcpus=None, ram=None, spec_code=None, instance_mode=None, az_status=None, az_desc=None, version_name=None, group_type=None):
        """Flavor

        The model defined in g42cloud sdk

        :param id: The param of the Flavor
        :type id: str
        :param vcpus: The param of the Flavor
        :type vcpus: str
        :param ram: The param of the Flavor
        :type ram: int
        :param spec_code: The param of the Flavor
        :type spec_code: str
        :param instance_mode: The param of the Flavor
        :type instance_mode: str
        :param az_status: The param of the Flavor
        :type az_status: dict(str, str)
        :param az_desc: The param of the Flavor
        :type az_desc: dict(str, str)
        :param version_name: The param of the Flavor
        :type version_name: list[str]
        :param group_type: The param of the Flavor
        :type group_type: str
        """
        
        

        self._id = None
        self._vcpus = None
        self._ram = None
        self._spec_code = None
        self._instance_mode = None
        self._az_status = None
        self._az_desc = None
        self._version_name = None
        self._group_type = None
        self.discriminator = None

        self.id = id
        self.vcpus = vcpus
        self.ram = ram
        self.spec_code = spec_code
        self.instance_mode = instance_mode
        self.az_status = az_status
        self.az_desc = az_desc
        self.version_name = version_name
        self.group_type = group_type

    @property
    def id(self):
        """Gets the id of this Flavor.

        :return: The id of this Flavor.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Flavor.

        :param id: The id of this Flavor.
        :type id: str
        """
        self._id = id

    @property
    def vcpus(self):
        """Gets the vcpus of this Flavor.

        :return: The vcpus of this Flavor.
        :rtype: str
        """
        return self._vcpus

    @vcpus.setter
    def vcpus(self, vcpus):
        """Sets the vcpus of this Flavor.

        :param vcpus: The vcpus of this Flavor.
        :type vcpus: str
        """
        self._vcpus = vcpus

    @property
    def ram(self):
        """Gets the ram of this Flavor.

        :return: The ram of this Flavor.
        :rtype: int
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this Flavor.

        :param ram: The ram of this Flavor.
        :type ram: int
        """
        self._ram = ram

    @property
    def spec_code(self):
        """Gets the spec_code of this Flavor.

        :return: The spec_code of this Flavor.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        """Sets the spec_code of this Flavor.

        :param spec_code: The spec_code of this Flavor.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def instance_mode(self):
        """Gets the instance_mode of this Flavor.

        :return: The instance_mode of this Flavor.
        :rtype: str
        """
        return self._instance_mode

    @instance_mode.setter
    def instance_mode(self, instance_mode):
        """Sets the instance_mode of this Flavor.

        :param instance_mode: The instance_mode of this Flavor.
        :type instance_mode: str
        """
        self._instance_mode = instance_mode

    @property
    def az_status(self):
        """Gets the az_status of this Flavor.

        :return: The az_status of this Flavor.
        :rtype: dict(str, str)
        """
        return self._az_status

    @az_status.setter
    def az_status(self, az_status):
        """Sets the az_status of this Flavor.

        :param az_status: The az_status of this Flavor.
        :type az_status: dict(str, str)
        """
        self._az_status = az_status

    @property
    def az_desc(self):
        """Gets the az_desc of this Flavor.

        :return: The az_desc of this Flavor.
        :rtype: dict(str, str)
        """
        return self._az_desc

    @az_desc.setter
    def az_desc(self, az_desc):
        """Sets the az_desc of this Flavor.

        :param az_desc: The az_desc of this Flavor.
        :type az_desc: dict(str, str)
        """
        self._az_desc = az_desc

    @property
    def version_name(self):
        """Gets the version_name of this Flavor.

        :return: The version_name of this Flavor.
        :rtype: list[str]
        """
        return self._version_name

    @version_name.setter
    def version_name(self, version_name):
        """Sets the version_name of this Flavor.

        :param version_name: The version_name of this Flavor.
        :type version_name: list[str]
        """
        self._version_name = version_name

    @property
    def group_type(self):
        """Gets the group_type of this Flavor.

        :return: The group_type of this Flavor.
        :rtype: str
        """
        return self._group_type

    @group_type.setter
    def group_type(self, group_type):
        """Sets the group_type of this Flavor.

        :param group_type: The group_type of this Flavor.
        :type group_type: str
        """
        self._group_type = group_type

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
        if not isinstance(other, Flavor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
