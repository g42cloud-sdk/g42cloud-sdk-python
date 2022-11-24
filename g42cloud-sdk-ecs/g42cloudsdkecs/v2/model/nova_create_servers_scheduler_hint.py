# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NovaCreateServersSchedulerHint:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group': 'str',
        'different_host': 'list[str]',
        'same_host': 'list[str]',
        'cidr': 'str',
        'build_near_host_ip': 'str',
        'tenancy': 'str',
        'dedicated_host_id': 'str'
    }

    attribute_map = {
        'group': 'group',
        'different_host': 'different_host',
        'same_host': 'same_host',
        'cidr': 'cidr',
        'build_near_host_ip': 'build_near_host_ip',
        'tenancy': 'tenancy',
        'dedicated_host_id': 'dedicated_host_id'
    }

    def __init__(self, group=None, different_host=None, same_host=None, cidr=None, build_near_host_ip=None, tenancy=None, dedicated_host_id=None):
        """NovaCreateServersSchedulerHint

        The model defined in g42cloud sdk

        :param group: The param of the NovaCreateServersSchedulerHint
        :type group: str
        :param different_host: The param of the NovaCreateServersSchedulerHint
        :type different_host: list[str]
        :param same_host: The param of the NovaCreateServersSchedulerHint
        :type same_host: list[str]
        :param cidr: The param of the NovaCreateServersSchedulerHint
        :type cidr: str
        :param build_near_host_ip: The param of the NovaCreateServersSchedulerHint
        :type build_near_host_ip: str
        :param tenancy: The param of the NovaCreateServersSchedulerHint
        :type tenancy: str
        :param dedicated_host_id: The param of the NovaCreateServersSchedulerHint
        :type dedicated_host_id: str
        """
        
        

        self._group = None
        self._different_host = None
        self._same_host = None
        self._cidr = None
        self._build_near_host_ip = None
        self._tenancy = None
        self._dedicated_host_id = None
        self.discriminator = None

        if group is not None:
            self.group = group
        if different_host is not None:
            self.different_host = different_host
        if same_host is not None:
            self.same_host = same_host
        if cidr is not None:
            self.cidr = cidr
        if build_near_host_ip is not None:
            self.build_near_host_ip = build_near_host_ip
        if tenancy is not None:
            self.tenancy = tenancy
        if dedicated_host_id is not None:
            self.dedicated_host_id = dedicated_host_id

    @property
    def group(self):
        """Gets the group of this NovaCreateServersSchedulerHint.

        :return: The group of this NovaCreateServersSchedulerHint.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this NovaCreateServersSchedulerHint.

        :param group: The group of this NovaCreateServersSchedulerHint.
        :type group: str
        """
        self._group = group

    @property
    def different_host(self):
        """Gets the different_host of this NovaCreateServersSchedulerHint.

        :return: The different_host of this NovaCreateServersSchedulerHint.
        :rtype: list[str]
        """
        return self._different_host

    @different_host.setter
    def different_host(self, different_host):
        """Sets the different_host of this NovaCreateServersSchedulerHint.

        :param different_host: The different_host of this NovaCreateServersSchedulerHint.
        :type different_host: list[str]
        """
        self._different_host = different_host

    @property
    def same_host(self):
        """Gets the same_host of this NovaCreateServersSchedulerHint.

        :return: The same_host of this NovaCreateServersSchedulerHint.
        :rtype: list[str]
        """
        return self._same_host

    @same_host.setter
    def same_host(self, same_host):
        """Sets the same_host of this NovaCreateServersSchedulerHint.

        :param same_host: The same_host of this NovaCreateServersSchedulerHint.
        :type same_host: list[str]
        """
        self._same_host = same_host

    @property
    def cidr(self):
        """Gets the cidr of this NovaCreateServersSchedulerHint.

        :return: The cidr of this NovaCreateServersSchedulerHint.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this NovaCreateServersSchedulerHint.

        :param cidr: The cidr of this NovaCreateServersSchedulerHint.
        :type cidr: str
        """
        self._cidr = cidr

    @property
    def build_near_host_ip(self):
        """Gets the build_near_host_ip of this NovaCreateServersSchedulerHint.

        :return: The build_near_host_ip of this NovaCreateServersSchedulerHint.
        :rtype: str
        """
        return self._build_near_host_ip

    @build_near_host_ip.setter
    def build_near_host_ip(self, build_near_host_ip):
        """Sets the build_near_host_ip of this NovaCreateServersSchedulerHint.

        :param build_near_host_ip: The build_near_host_ip of this NovaCreateServersSchedulerHint.
        :type build_near_host_ip: str
        """
        self._build_near_host_ip = build_near_host_ip

    @property
    def tenancy(self):
        """Gets the tenancy of this NovaCreateServersSchedulerHint.

        :return: The tenancy of this NovaCreateServersSchedulerHint.
        :rtype: str
        """
        return self._tenancy

    @tenancy.setter
    def tenancy(self, tenancy):
        """Sets the tenancy of this NovaCreateServersSchedulerHint.

        :param tenancy: The tenancy of this NovaCreateServersSchedulerHint.
        :type tenancy: str
        """
        self._tenancy = tenancy

    @property
    def dedicated_host_id(self):
        """Gets the dedicated_host_id of this NovaCreateServersSchedulerHint.

        :return: The dedicated_host_id of this NovaCreateServersSchedulerHint.
        :rtype: str
        """
        return self._dedicated_host_id

    @dedicated_host_id.setter
    def dedicated_host_id(self, dedicated_host_id):
        """Sets the dedicated_host_id of this NovaCreateServersSchedulerHint.

        :param dedicated_host_id: The dedicated_host_id of this NovaCreateServersSchedulerHint.
        :type dedicated_host_id: str
        """
        self._dedicated_host_id = dedicated_host_id

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
        if not isinstance(other, NovaCreateServersSchedulerHint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
