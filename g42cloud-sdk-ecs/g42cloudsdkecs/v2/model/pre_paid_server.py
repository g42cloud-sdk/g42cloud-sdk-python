# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrePaidServer:

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
        'user_data': 'str',
        'admin_pass': 'str',
        'key_name': 'str',
        'vpcid': 'str',
        'nics': 'list[PrePaidServerNic]',
        'publicip': 'PrePaidServerPublicip',
        'count': 'int',
        'is_auto_rename': 'bool',
        'root_volume': 'PrePaidServerRootVolume',
        'data_volumes': 'list[PrePaidServerDataVolume]',
        'security_groups': 'list[PrePaidServerSecurityGroup]',
        'availability_zone': 'str',
        'batch_create_in_multi_az': 'bool',
        'extendparam': 'PrePaidServerExtendParam',
        'metadata': 'dict(str, str)',
        'osscheduler_hints': 'PrePaidServerSchedulerHints',
        'tags': 'list[str]',
        'server_tags': 'list[PrePaidServerTag]',
        'description': 'str'
    }

    attribute_map = {
        'auto_terminate_time': 'auto_terminate_time',
        'image_ref': 'imageRef',
        'flavor_ref': 'flavorRef',
        'name': 'name',
        'user_data': 'user_data',
        'admin_pass': 'adminPass',
        'key_name': 'key_name',
        'vpcid': 'vpcid',
        'nics': 'nics',
        'publicip': 'publicip',
        'count': 'count',
        'is_auto_rename': 'isAutoRename',
        'root_volume': 'root_volume',
        'data_volumes': 'data_volumes',
        'security_groups': 'security_groups',
        'availability_zone': 'availability_zone',
        'batch_create_in_multi_az': 'batch_create_in_multi_az',
        'extendparam': 'extendparam',
        'metadata': 'metadata',
        'osscheduler_hints': 'os:scheduler_hints',
        'tags': 'tags',
        'server_tags': 'server_tags',
        'description': 'description'
    }

    def __init__(self, auto_terminate_time=None, image_ref=None, flavor_ref=None, name=None, user_data=None, admin_pass=None, key_name=None, vpcid=None, nics=None, publicip=None, count=None, is_auto_rename=None, root_volume=None, data_volumes=None, security_groups=None, availability_zone=None, batch_create_in_multi_az=None, extendparam=None, metadata=None, osscheduler_hints=None, tags=None, server_tags=None, description=None):
        """PrePaidServer

        The model defined in g42cloud sdk

        :param auto_terminate_time: The param of the PrePaidServer
        :type auto_terminate_time: str
        :param image_ref: The param of the PrePaidServer
        :type image_ref: str
        :param flavor_ref: The param of the PrePaidServer
        :type flavor_ref: str
        :param name: The param of the PrePaidServer
        :type name: str
        :param user_data: The param of the PrePaidServer
        :type user_data: str
        :param admin_pass: The param of the PrePaidServer
        :type admin_pass: str
        :param key_name: The param of the PrePaidServer
        :type key_name: str
        :param vpcid: The param of the PrePaidServer
        :type vpcid: str
        :param nics: The param of the PrePaidServer
        :type nics: list[:class:`g42cloudsdkecs.v2.PrePaidServerNic`]
        :param publicip: The param of the PrePaidServer
        :type publicip: :class:`g42cloudsdkecs.v2.PrePaidServerPublicip`
        :param count: The param of the PrePaidServer
        :type count: int
        :param is_auto_rename: The param of the PrePaidServer
        :type is_auto_rename: bool
        :param root_volume: The param of the PrePaidServer
        :type root_volume: :class:`g42cloudsdkecs.v2.PrePaidServerRootVolume`
        :param data_volumes: The param of the PrePaidServer
        :type data_volumes: list[:class:`g42cloudsdkecs.v2.PrePaidServerDataVolume`]
        :param security_groups: The param of the PrePaidServer
        :type security_groups: list[:class:`g42cloudsdkecs.v2.PrePaidServerSecurityGroup`]
        :param availability_zone: The param of the PrePaidServer
        :type availability_zone: str
        :param batch_create_in_multi_az: The param of the PrePaidServer
        :type batch_create_in_multi_az: bool
        :param extendparam: The param of the PrePaidServer
        :type extendparam: :class:`g42cloudsdkecs.v2.PrePaidServerExtendParam`
        :param metadata: The param of the PrePaidServer
        :type metadata: dict(str, str)
        :param osscheduler_hints: The param of the PrePaidServer
        :type osscheduler_hints: :class:`g42cloudsdkecs.v2.PrePaidServerSchedulerHints`
        :param tags: The param of the PrePaidServer
        :type tags: list[str]
        :param server_tags: The param of the PrePaidServer
        :type server_tags: list[:class:`g42cloudsdkecs.v2.PrePaidServerTag`]
        :param description: The param of the PrePaidServer
        :type description: str
        """
        
        

        self._auto_terminate_time = None
        self._image_ref = None
        self._flavor_ref = None
        self._name = None
        self._user_data = None
        self._admin_pass = None
        self._key_name = None
        self._vpcid = None
        self._nics = None
        self._publicip = None
        self._count = None
        self._is_auto_rename = None
        self._root_volume = None
        self._data_volumes = None
        self._security_groups = None
        self._availability_zone = None
        self._batch_create_in_multi_az = None
        self._extendparam = None
        self._metadata = None
        self._osscheduler_hints = None
        self._tags = None
        self._server_tags = None
        self._description = None
        self.discriminator = None

        if auto_terminate_time is not None:
            self.auto_terminate_time = auto_terminate_time
        self.image_ref = image_ref
        self.flavor_ref = flavor_ref
        self.name = name
        if user_data is not None:
            self.user_data = user_data
        if admin_pass is not None:
            self.admin_pass = admin_pass
        if key_name is not None:
            self.key_name = key_name
        self.vpcid = vpcid
        self.nics = nics
        if publicip is not None:
            self.publicip = publicip
        if count is not None:
            self.count = count
        if is_auto_rename is not None:
            self.is_auto_rename = is_auto_rename
        self.root_volume = root_volume
        if data_volumes is not None:
            self.data_volumes = data_volumes
        if security_groups is not None:
            self.security_groups = security_groups
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if batch_create_in_multi_az is not None:
            self.batch_create_in_multi_az = batch_create_in_multi_az
        if extendparam is not None:
            self.extendparam = extendparam
        if metadata is not None:
            self.metadata = metadata
        if osscheduler_hints is not None:
            self.osscheduler_hints = osscheduler_hints
        if tags is not None:
            self.tags = tags
        if server_tags is not None:
            self.server_tags = server_tags
        if description is not None:
            self.description = description

    @property
    def auto_terminate_time(self):
        """Gets the auto_terminate_time of this PrePaidServer.

        :return: The auto_terminate_time of this PrePaidServer.
        :rtype: str
        """
        return self._auto_terminate_time

    @auto_terminate_time.setter
    def auto_terminate_time(self, auto_terminate_time):
        """Sets the auto_terminate_time of this PrePaidServer.

        :param auto_terminate_time: The auto_terminate_time of this PrePaidServer.
        :type auto_terminate_time: str
        """
        self._auto_terminate_time = auto_terminate_time

    @property
    def image_ref(self):
        """Gets the image_ref of this PrePaidServer.

        :return: The image_ref of this PrePaidServer.
        :rtype: str
        """
        return self._image_ref

    @image_ref.setter
    def image_ref(self, image_ref):
        """Sets the image_ref of this PrePaidServer.

        :param image_ref: The image_ref of this PrePaidServer.
        :type image_ref: str
        """
        self._image_ref = image_ref

    @property
    def flavor_ref(self):
        """Gets the flavor_ref of this PrePaidServer.

        :return: The flavor_ref of this PrePaidServer.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        """Sets the flavor_ref of this PrePaidServer.

        :param flavor_ref: The flavor_ref of this PrePaidServer.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def name(self):
        """Gets the name of this PrePaidServer.

        :return: The name of this PrePaidServer.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PrePaidServer.

        :param name: The name of this PrePaidServer.
        :type name: str
        """
        self._name = name

    @property
    def user_data(self):
        """Gets the user_data of this PrePaidServer.

        :return: The user_data of this PrePaidServer.
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this PrePaidServer.

        :param user_data: The user_data of this PrePaidServer.
        :type user_data: str
        """
        self._user_data = user_data

    @property
    def admin_pass(self):
        """Gets the admin_pass of this PrePaidServer.

        :return: The admin_pass of this PrePaidServer.
        :rtype: str
        """
        return self._admin_pass

    @admin_pass.setter
    def admin_pass(self, admin_pass):
        """Sets the admin_pass of this PrePaidServer.

        :param admin_pass: The admin_pass of this PrePaidServer.
        :type admin_pass: str
        """
        self._admin_pass = admin_pass

    @property
    def key_name(self):
        """Gets the key_name of this PrePaidServer.

        :return: The key_name of this PrePaidServer.
        :rtype: str
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        """Sets the key_name of this PrePaidServer.

        :param key_name: The key_name of this PrePaidServer.
        :type key_name: str
        """
        self._key_name = key_name

    @property
    def vpcid(self):
        """Gets the vpcid of this PrePaidServer.

        :return: The vpcid of this PrePaidServer.
        :rtype: str
        """
        return self._vpcid

    @vpcid.setter
    def vpcid(self, vpcid):
        """Sets the vpcid of this PrePaidServer.

        :param vpcid: The vpcid of this PrePaidServer.
        :type vpcid: str
        """
        self._vpcid = vpcid

    @property
    def nics(self):
        """Gets the nics of this PrePaidServer.

        :return: The nics of this PrePaidServer.
        :rtype: list[:class:`g42cloudsdkecs.v2.PrePaidServerNic`]
        """
        return self._nics

    @nics.setter
    def nics(self, nics):
        """Sets the nics of this PrePaidServer.

        :param nics: The nics of this PrePaidServer.
        :type nics: list[:class:`g42cloudsdkecs.v2.PrePaidServerNic`]
        """
        self._nics = nics

    @property
    def publicip(self):
        """Gets the publicip of this PrePaidServer.

        :return: The publicip of this PrePaidServer.
        :rtype: :class:`g42cloudsdkecs.v2.PrePaidServerPublicip`
        """
        return self._publicip

    @publicip.setter
    def publicip(self, publicip):
        """Sets the publicip of this PrePaidServer.

        :param publicip: The publicip of this PrePaidServer.
        :type publicip: :class:`g42cloudsdkecs.v2.PrePaidServerPublicip`
        """
        self._publicip = publicip

    @property
    def count(self):
        """Gets the count of this PrePaidServer.

        :return: The count of this PrePaidServer.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this PrePaidServer.

        :param count: The count of this PrePaidServer.
        :type count: int
        """
        self._count = count

    @property
    def is_auto_rename(self):
        """Gets the is_auto_rename of this PrePaidServer.

        :return: The is_auto_rename of this PrePaidServer.
        :rtype: bool
        """
        return self._is_auto_rename

    @is_auto_rename.setter
    def is_auto_rename(self, is_auto_rename):
        """Sets the is_auto_rename of this PrePaidServer.

        :param is_auto_rename: The is_auto_rename of this PrePaidServer.
        :type is_auto_rename: bool
        """
        self._is_auto_rename = is_auto_rename

    @property
    def root_volume(self):
        """Gets the root_volume of this PrePaidServer.

        :return: The root_volume of this PrePaidServer.
        :rtype: :class:`g42cloudsdkecs.v2.PrePaidServerRootVolume`
        """
        return self._root_volume

    @root_volume.setter
    def root_volume(self, root_volume):
        """Sets the root_volume of this PrePaidServer.

        :param root_volume: The root_volume of this PrePaidServer.
        :type root_volume: :class:`g42cloudsdkecs.v2.PrePaidServerRootVolume`
        """
        self._root_volume = root_volume

    @property
    def data_volumes(self):
        """Gets the data_volumes of this PrePaidServer.

        :return: The data_volumes of this PrePaidServer.
        :rtype: list[:class:`g42cloudsdkecs.v2.PrePaidServerDataVolume`]
        """
        return self._data_volumes

    @data_volumes.setter
    def data_volumes(self, data_volumes):
        """Sets the data_volumes of this PrePaidServer.

        :param data_volumes: The data_volumes of this PrePaidServer.
        :type data_volumes: list[:class:`g42cloudsdkecs.v2.PrePaidServerDataVolume`]
        """
        self._data_volumes = data_volumes

    @property
    def security_groups(self):
        """Gets the security_groups of this PrePaidServer.

        :return: The security_groups of this PrePaidServer.
        :rtype: list[:class:`g42cloudsdkecs.v2.PrePaidServerSecurityGroup`]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this PrePaidServer.

        :param security_groups: The security_groups of this PrePaidServer.
        :type security_groups: list[:class:`g42cloudsdkecs.v2.PrePaidServerSecurityGroup`]
        """
        self._security_groups = security_groups

    @property
    def availability_zone(self):
        """Gets the availability_zone of this PrePaidServer.

        :return: The availability_zone of this PrePaidServer.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this PrePaidServer.

        :param availability_zone: The availability_zone of this PrePaidServer.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def batch_create_in_multi_az(self):
        """Gets the batch_create_in_multi_az of this PrePaidServer.

        :return: The batch_create_in_multi_az of this PrePaidServer.
        :rtype: bool
        """
        return self._batch_create_in_multi_az

    @batch_create_in_multi_az.setter
    def batch_create_in_multi_az(self, batch_create_in_multi_az):
        """Sets the batch_create_in_multi_az of this PrePaidServer.

        :param batch_create_in_multi_az: The batch_create_in_multi_az of this PrePaidServer.
        :type batch_create_in_multi_az: bool
        """
        self._batch_create_in_multi_az = batch_create_in_multi_az

    @property
    def extendparam(self):
        """Gets the extendparam of this PrePaidServer.

        :return: The extendparam of this PrePaidServer.
        :rtype: :class:`g42cloudsdkecs.v2.PrePaidServerExtendParam`
        """
        return self._extendparam

    @extendparam.setter
    def extendparam(self, extendparam):
        """Sets the extendparam of this PrePaidServer.

        :param extendparam: The extendparam of this PrePaidServer.
        :type extendparam: :class:`g42cloudsdkecs.v2.PrePaidServerExtendParam`
        """
        self._extendparam = extendparam

    @property
    def metadata(self):
        """Gets the metadata of this PrePaidServer.

        :return: The metadata of this PrePaidServer.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this PrePaidServer.

        :param metadata: The metadata of this PrePaidServer.
        :type metadata: dict(str, str)
        """
        self._metadata = metadata

    @property
    def osscheduler_hints(self):
        """Gets the osscheduler_hints of this PrePaidServer.

        :return: The osscheduler_hints of this PrePaidServer.
        :rtype: :class:`g42cloudsdkecs.v2.PrePaidServerSchedulerHints`
        """
        return self._osscheduler_hints

    @osscheduler_hints.setter
    def osscheduler_hints(self, osscheduler_hints):
        """Sets the osscheduler_hints of this PrePaidServer.

        :param osscheduler_hints: The osscheduler_hints of this PrePaidServer.
        :type osscheduler_hints: :class:`g42cloudsdkecs.v2.PrePaidServerSchedulerHints`
        """
        self._osscheduler_hints = osscheduler_hints

    @property
    def tags(self):
        """Gets the tags of this PrePaidServer.

        :return: The tags of this PrePaidServer.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this PrePaidServer.

        :param tags: The tags of this PrePaidServer.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def server_tags(self):
        """Gets the server_tags of this PrePaidServer.

        :return: The server_tags of this PrePaidServer.
        :rtype: list[:class:`g42cloudsdkecs.v2.PrePaidServerTag`]
        """
        return self._server_tags

    @server_tags.setter
    def server_tags(self, server_tags):
        """Sets the server_tags of this PrePaidServer.

        :param server_tags: The server_tags of this PrePaidServer.
        :type server_tags: list[:class:`g42cloudsdkecs.v2.PrePaidServerTag`]
        """
        self._server_tags = server_tags

    @property
    def description(self):
        """Gets the description of this PrePaidServer.

        :return: The description of this PrePaidServer.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PrePaidServer.

        :param description: The description of this PrePaidServer.
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
        if not isinstance(other, PrePaidServer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
