# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NovaCreateServersOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'auto_terminate_time': 'str',
        'image_ref': 'str',
        'flavor_ref': 'str',
        'name': 'str',
        'metadata': 'dict(str, str)',
        'admin_pass': 'str',
        'block_device_mapping_v2': 'list[NovaServerBlockDeviceMapping]',
        'config_drive': 'str',
        'security_groups': 'list[NovaServerSecurityGroup]',
        'networks': 'list[NovaServerNetwork]',
        'key_name': 'str',
        'user_data': 'str',
        'availability_zone': 'str',
        'return_reservation_id': 'bool',
        'min_count': 'int',
        'max_count': 'int',
        'os_dc_fdisk_config': 'str',
        'description': 'str'
    }

    attribute_map = {
        'auto_terminate_time': 'auto_terminate_time',
        'image_ref': 'imageRef',
        'flavor_ref': 'flavorRef',
        'name': 'name',
        'metadata': 'metadata',
        'admin_pass': 'adminPass',
        'block_device_mapping_v2': 'block_device_mapping_v2',
        'config_drive': 'config_drive',
        'security_groups': 'security_groups',
        'networks': 'networks',
        'key_name': 'key_name',
        'user_data': 'user_data',
        'availability_zone': 'availability_zone',
        'return_reservation_id': 'return_reservation_id',
        'min_count': 'min_count',
        'max_count': 'max_count',
        'os_dc_fdisk_config': 'OS-DCF:diskConfig',
        'description': 'description'
    }

    def __init__(self, auto_terminate_time=None, image_ref=None, flavor_ref=None, name=None, metadata=None, admin_pass=None, block_device_mapping_v2=None, config_drive=None, security_groups=None, networks=None, key_name=None, user_data=None, availability_zone=None, return_reservation_id=None, min_count=None, max_count=None, os_dc_fdisk_config=None, description=None):
        """NovaCreateServersOption

        The model defined in g42cloud sdk

        :param auto_terminate_time: The param of the NovaCreateServersOption
        :type auto_terminate_time: str
        :param image_ref: The param of the NovaCreateServersOption
        :type image_ref: str
        :param flavor_ref: The param of the NovaCreateServersOption
        :type flavor_ref: str
        :param name: The param of the NovaCreateServersOption
        :type name: str
        :param metadata: The param of the NovaCreateServersOption
        :type metadata: dict(str, str)
        :param admin_pass: The param of the NovaCreateServersOption
        :type admin_pass: str
        :param block_device_mapping_v2: The param of the NovaCreateServersOption
        :type block_device_mapping_v2: list[:class:`g42cloudsdkecs.v2.NovaServerBlockDeviceMapping`]
        :param config_drive: The param of the NovaCreateServersOption
        :type config_drive: str
        :param security_groups: The param of the NovaCreateServersOption
        :type security_groups: list[:class:`g42cloudsdkecs.v2.NovaServerSecurityGroup`]
        :param networks: The param of the NovaCreateServersOption
        :type networks: list[:class:`g42cloudsdkecs.v2.NovaServerNetwork`]
        :param key_name: The param of the NovaCreateServersOption
        :type key_name: str
        :param user_data: The param of the NovaCreateServersOption
        :type user_data: str
        :param availability_zone: The param of the NovaCreateServersOption
        :type availability_zone: str
        :param return_reservation_id: The param of the NovaCreateServersOption
        :type return_reservation_id: bool
        :param min_count: The param of the NovaCreateServersOption
        :type min_count: int
        :param max_count: The param of the NovaCreateServersOption
        :type max_count: int
        :param os_dc_fdisk_config: The param of the NovaCreateServersOption
        :type os_dc_fdisk_config: str
        :param description: The param of the NovaCreateServersOption
        :type description: str
        """
        
        

        self._auto_terminate_time = None
        self._image_ref = None
        self._flavor_ref = None
        self._name = None
        self._metadata = None
        self._admin_pass = None
        self._block_device_mapping_v2 = None
        self._config_drive = None
        self._security_groups = None
        self._networks = None
        self._key_name = None
        self._user_data = None
        self._availability_zone = None
        self._return_reservation_id = None
        self._min_count = None
        self._max_count = None
        self._os_dc_fdisk_config = None
        self._description = None
        self.discriminator = None

        if auto_terminate_time is not None:
            self.auto_terminate_time = auto_terminate_time
        if image_ref is not None:
            self.image_ref = image_ref
        self.flavor_ref = flavor_ref
        self.name = name
        if metadata is not None:
            self.metadata = metadata
        if admin_pass is not None:
            self.admin_pass = admin_pass
        if block_device_mapping_v2 is not None:
            self.block_device_mapping_v2 = block_device_mapping_v2
        if config_drive is not None:
            self.config_drive = config_drive
        if security_groups is not None:
            self.security_groups = security_groups
        self.networks = networks
        if key_name is not None:
            self.key_name = key_name
        if user_data is not None:
            self.user_data = user_data
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if return_reservation_id is not None:
            self.return_reservation_id = return_reservation_id
        if min_count is not None:
            self.min_count = min_count
        if max_count is not None:
            self.max_count = max_count
        if os_dc_fdisk_config is not None:
            self.os_dc_fdisk_config = os_dc_fdisk_config
        if description is not None:
            self.description = description

    @property
    def auto_terminate_time(self):
        """Gets the auto_terminate_time of this NovaCreateServersOption.

        :return: The auto_terminate_time of this NovaCreateServersOption.
        :rtype: str
        """
        return self._auto_terminate_time

    @auto_terminate_time.setter
    def auto_terminate_time(self, auto_terminate_time):
        """Sets the auto_terminate_time of this NovaCreateServersOption.

        :param auto_terminate_time: The auto_terminate_time of this NovaCreateServersOption.
        :type auto_terminate_time: str
        """
        self._auto_terminate_time = auto_terminate_time

    @property
    def image_ref(self):
        """Gets the image_ref of this NovaCreateServersOption.

        :return: The image_ref of this NovaCreateServersOption.
        :rtype: str
        """
        return self._image_ref

    @image_ref.setter
    def image_ref(self, image_ref):
        """Sets the image_ref of this NovaCreateServersOption.

        :param image_ref: The image_ref of this NovaCreateServersOption.
        :type image_ref: str
        """
        self._image_ref = image_ref

    @property
    def flavor_ref(self):
        """Gets the flavor_ref of this NovaCreateServersOption.

        :return: The flavor_ref of this NovaCreateServersOption.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        """Sets the flavor_ref of this NovaCreateServersOption.

        :param flavor_ref: The flavor_ref of this NovaCreateServersOption.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def name(self):
        """Gets the name of this NovaCreateServersOption.

        :return: The name of this NovaCreateServersOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NovaCreateServersOption.

        :param name: The name of this NovaCreateServersOption.
        :type name: str
        """
        self._name = name

    @property
    def metadata(self):
        """Gets the metadata of this NovaCreateServersOption.

        :return: The metadata of this NovaCreateServersOption.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this NovaCreateServersOption.

        :param metadata: The metadata of this NovaCreateServersOption.
        :type metadata: dict(str, str)
        """
        self._metadata = metadata

    @property
    def admin_pass(self):
        """Gets the admin_pass of this NovaCreateServersOption.

        :return: The admin_pass of this NovaCreateServersOption.
        :rtype: str
        """
        return self._admin_pass

    @admin_pass.setter
    def admin_pass(self, admin_pass):
        """Sets the admin_pass of this NovaCreateServersOption.

        :param admin_pass: The admin_pass of this NovaCreateServersOption.
        :type admin_pass: str
        """
        self._admin_pass = admin_pass

    @property
    def block_device_mapping_v2(self):
        """Gets the block_device_mapping_v2 of this NovaCreateServersOption.

        :return: The block_device_mapping_v2 of this NovaCreateServersOption.
        :rtype: list[:class:`g42cloudsdkecs.v2.NovaServerBlockDeviceMapping`]
        """
        return self._block_device_mapping_v2

    @block_device_mapping_v2.setter
    def block_device_mapping_v2(self, block_device_mapping_v2):
        """Sets the block_device_mapping_v2 of this NovaCreateServersOption.

        :param block_device_mapping_v2: The block_device_mapping_v2 of this NovaCreateServersOption.
        :type block_device_mapping_v2: list[:class:`g42cloudsdkecs.v2.NovaServerBlockDeviceMapping`]
        """
        self._block_device_mapping_v2 = block_device_mapping_v2

    @property
    def config_drive(self):
        """Gets the config_drive of this NovaCreateServersOption.

        :return: The config_drive of this NovaCreateServersOption.
        :rtype: str
        """
        return self._config_drive

    @config_drive.setter
    def config_drive(self, config_drive):
        """Sets the config_drive of this NovaCreateServersOption.

        :param config_drive: The config_drive of this NovaCreateServersOption.
        :type config_drive: str
        """
        self._config_drive = config_drive

    @property
    def security_groups(self):
        """Gets the security_groups of this NovaCreateServersOption.

        :return: The security_groups of this NovaCreateServersOption.
        :rtype: list[:class:`g42cloudsdkecs.v2.NovaServerSecurityGroup`]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this NovaCreateServersOption.

        :param security_groups: The security_groups of this NovaCreateServersOption.
        :type security_groups: list[:class:`g42cloudsdkecs.v2.NovaServerSecurityGroup`]
        """
        self._security_groups = security_groups

    @property
    def networks(self):
        """Gets the networks of this NovaCreateServersOption.

        :return: The networks of this NovaCreateServersOption.
        :rtype: list[:class:`g42cloudsdkecs.v2.NovaServerNetwork`]
        """
        return self._networks

    @networks.setter
    def networks(self, networks):
        """Sets the networks of this NovaCreateServersOption.

        :param networks: The networks of this NovaCreateServersOption.
        :type networks: list[:class:`g42cloudsdkecs.v2.NovaServerNetwork`]
        """
        self._networks = networks

    @property
    def key_name(self):
        """Gets the key_name of this NovaCreateServersOption.

        :return: The key_name of this NovaCreateServersOption.
        :rtype: str
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        """Sets the key_name of this NovaCreateServersOption.

        :param key_name: The key_name of this NovaCreateServersOption.
        :type key_name: str
        """
        self._key_name = key_name

    @property
    def user_data(self):
        """Gets the user_data of this NovaCreateServersOption.

        :return: The user_data of this NovaCreateServersOption.
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this NovaCreateServersOption.

        :param user_data: The user_data of this NovaCreateServersOption.
        :type user_data: str
        """
        self._user_data = user_data

    @property
    def availability_zone(self):
        """Gets the availability_zone of this NovaCreateServersOption.

        :return: The availability_zone of this NovaCreateServersOption.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this NovaCreateServersOption.

        :param availability_zone: The availability_zone of this NovaCreateServersOption.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def return_reservation_id(self):
        """Gets the return_reservation_id of this NovaCreateServersOption.

        :return: The return_reservation_id of this NovaCreateServersOption.
        :rtype: bool
        """
        return self._return_reservation_id

    @return_reservation_id.setter
    def return_reservation_id(self, return_reservation_id):
        """Sets the return_reservation_id of this NovaCreateServersOption.

        :param return_reservation_id: The return_reservation_id of this NovaCreateServersOption.
        :type return_reservation_id: bool
        """
        self._return_reservation_id = return_reservation_id

    @property
    def min_count(self):
        """Gets the min_count of this NovaCreateServersOption.

        :return: The min_count of this NovaCreateServersOption.
        :rtype: int
        """
        return self._min_count

    @min_count.setter
    def min_count(self, min_count):
        """Sets the min_count of this NovaCreateServersOption.

        :param min_count: The min_count of this NovaCreateServersOption.
        :type min_count: int
        """
        self._min_count = min_count

    @property
    def max_count(self):
        """Gets the max_count of this NovaCreateServersOption.

        :return: The max_count of this NovaCreateServersOption.
        :rtype: int
        """
        return self._max_count

    @max_count.setter
    def max_count(self, max_count):
        """Sets the max_count of this NovaCreateServersOption.

        :param max_count: The max_count of this NovaCreateServersOption.
        :type max_count: int
        """
        self._max_count = max_count

    @property
    def os_dc_fdisk_config(self):
        """Gets the os_dc_fdisk_config of this NovaCreateServersOption.

        :return: The os_dc_fdisk_config of this NovaCreateServersOption.
        :rtype: str
        """
        return self._os_dc_fdisk_config

    @os_dc_fdisk_config.setter
    def os_dc_fdisk_config(self, os_dc_fdisk_config):
        """Sets the os_dc_fdisk_config of this NovaCreateServersOption.

        :param os_dc_fdisk_config: The os_dc_fdisk_config of this NovaCreateServersOption.
        :type os_dc_fdisk_config: str
        """
        self._os_dc_fdisk_config = os_dc_fdisk_config

    @property
    def description(self):
        """Gets the description of this NovaCreateServersOption.

        :return: The description of this NovaCreateServersOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NovaCreateServersOption.

        :param description: The description of this NovaCreateServersOption.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, NovaCreateServersOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
