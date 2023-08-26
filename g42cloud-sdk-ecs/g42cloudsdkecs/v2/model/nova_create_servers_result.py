# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class NovaCreateServersResult:

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
        'links': 'list[NovaLink]',
        'security_groups': 'list[NovaServerSecurityGroup]',
        'os_dc_fdisk_config': 'str',
        'reservation_id': 'str',
        'admin_pass': 'str'
    }

    attribute_map = {
        'id': 'id',
        'links': 'links',
        'security_groups': 'security_groups',
        'os_dc_fdisk_config': 'OS-DCF:diskConfig',
        'reservation_id': 'reservation_id',
        'admin_pass': 'adminPass'
    }

    def __init__(self, id=None, links=None, security_groups=None, os_dc_fdisk_config=None, reservation_id=None, admin_pass=None):
        """NovaCreateServersResult

        The model defined in g42cloud sdk

        :param id: The param of the NovaCreateServersResult
        :type id: str
        :param links: The param of the NovaCreateServersResult
        :type links: list[:class:`g42cloudsdkecs.v2.NovaLink`]
        :param security_groups: The param of the NovaCreateServersResult
        :type security_groups: list[:class:`g42cloudsdkecs.v2.NovaServerSecurityGroup`]
        :param os_dc_fdisk_config: The param of the NovaCreateServersResult
        :type os_dc_fdisk_config: str
        :param reservation_id: The param of the NovaCreateServersResult
        :type reservation_id: str
        :param admin_pass: The param of the NovaCreateServersResult
        :type admin_pass: str
        """
        
        

        self._id = None
        self._links = None
        self._security_groups = None
        self._os_dc_fdisk_config = None
        self._reservation_id = None
        self._admin_pass = None
        self.discriminator = None

        self.id = id
        self.links = links
        self.security_groups = security_groups
        self.os_dc_fdisk_config = os_dc_fdisk_config
        if reservation_id is not None:
            self.reservation_id = reservation_id
        self.admin_pass = admin_pass

    @property
    def id(self):
        """Gets the id of this NovaCreateServersResult.

        :return: The id of this NovaCreateServersResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NovaCreateServersResult.

        :param id: The id of this NovaCreateServersResult.
        :type id: str
        """
        self._id = id

    @property
    def links(self):
        """Gets the links of this NovaCreateServersResult.

        :return: The links of this NovaCreateServersResult.
        :rtype: list[:class:`g42cloudsdkecs.v2.NovaLink`]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this NovaCreateServersResult.

        :param links: The links of this NovaCreateServersResult.
        :type links: list[:class:`g42cloudsdkecs.v2.NovaLink`]
        """
        self._links = links

    @property
    def security_groups(self):
        """Gets the security_groups of this NovaCreateServersResult.

        :return: The security_groups of this NovaCreateServersResult.
        :rtype: list[:class:`g42cloudsdkecs.v2.NovaServerSecurityGroup`]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this NovaCreateServersResult.

        :param security_groups: The security_groups of this NovaCreateServersResult.
        :type security_groups: list[:class:`g42cloudsdkecs.v2.NovaServerSecurityGroup`]
        """
        self._security_groups = security_groups

    @property
    def os_dc_fdisk_config(self):
        """Gets the os_dc_fdisk_config of this NovaCreateServersResult.

        :return: The os_dc_fdisk_config of this NovaCreateServersResult.
        :rtype: str
        """
        return self._os_dc_fdisk_config

    @os_dc_fdisk_config.setter
    def os_dc_fdisk_config(self, os_dc_fdisk_config):
        """Sets the os_dc_fdisk_config of this NovaCreateServersResult.

        :param os_dc_fdisk_config: The os_dc_fdisk_config of this NovaCreateServersResult.
        :type os_dc_fdisk_config: str
        """
        self._os_dc_fdisk_config = os_dc_fdisk_config

    @property
    def reservation_id(self):
        """Gets the reservation_id of this NovaCreateServersResult.

        :return: The reservation_id of this NovaCreateServersResult.
        :rtype: str
        """
        return self._reservation_id

    @reservation_id.setter
    def reservation_id(self, reservation_id):
        """Sets the reservation_id of this NovaCreateServersResult.

        :param reservation_id: The reservation_id of this NovaCreateServersResult.
        :type reservation_id: str
        """
        self._reservation_id = reservation_id

    @property
    def admin_pass(self):
        """Gets the admin_pass of this NovaCreateServersResult.

        :return: The admin_pass of this NovaCreateServersResult.
        :rtype: str
        """
        return self._admin_pass

    @admin_pass.setter
    def admin_pass(self, admin_pass):
        """Sets the admin_pass of this NovaCreateServersResult.

        :param admin_pass: The admin_pass of this NovaCreateServersResult.
        :type admin_pass: str
        """
        self._admin_pass = admin_pass

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
        if not isinstance(other, NovaCreateServersResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
