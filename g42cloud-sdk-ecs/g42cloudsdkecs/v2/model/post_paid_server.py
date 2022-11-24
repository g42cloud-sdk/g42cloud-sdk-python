# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostPaidServer:

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
        'admin_pass': 'str',
        'availability_zone': 'str',
        'batch_create_in_multi_az': 'bool',
        'count': 'int',
        'data_volumes': 'list[PostPaidServerDataVolume]',
        'extendparam': 'PostPaidServerExtendParam',
        'flavor_ref': 'str',
        'image_ref': 'str',
        'is_auto_rename': 'bool',
        'key_name': 'str',
        'metadata': 'dict(str, str)',
        'name': 'str',
        'nics': 'list[PostPaidServerNic]',
        'osscheduler_hints': 'PostPaidServerSchedulerHints',
        'publicip': 'PostPaidServerPublicip',
        'root_volume': 'PostPaidServerRootVolume',
        'security_groups': 'list[PostPaidServerSecurityGroup]',
        'server_tags': 'list[PostPaidServerTag]',
        'tags': 'list[str]',
        'user_data': 'str',
        'vpcid': 'str',
        'description': 'str'
    }

    attribute_map = {
        'auto_terminate_time': 'auto_terminate_time',
        'admin_pass': 'adminPass',
        'availability_zone': 'availability_zone',
        'batch_create_in_multi_az': 'batch_create_in_multi_az',
        'count': 'count',
        'data_volumes': 'data_volumes',
        'extendparam': 'extendparam',
        'flavor_ref': 'flavorRef',
        'image_ref': 'imageRef',
        'is_auto_rename': 'isAutoRename',
        'key_name': 'key_name',
        'metadata': 'metadata',
        'name': 'name',
        'nics': 'nics',
        'osscheduler_hints': 'os:scheduler_hints',
        'publicip': 'publicip',
        'root_volume': 'root_volume',
        'security_groups': 'security_groups',
        'server_tags': 'server_tags',
        'tags': 'tags',
        'user_data': 'user_data',
        'vpcid': 'vpcid',
        'description': 'description'
    }

    def __init__(self, auto_terminate_time=None, admin_pass=None, availability_zone=None, batch_create_in_multi_az=None, count=None, data_volumes=None, extendparam=None, flavor_ref=None, image_ref=None, is_auto_rename=None, key_name=None, metadata=None, name=None, nics=None, osscheduler_hints=None, publicip=None, root_volume=None, security_groups=None, server_tags=None, tags=None, user_data=None, vpcid=None, description=None):
        """PostPaidServer

        The model defined in g42cloud sdk

        :param auto_terminate_time: The param of the PostPaidServer
        :type auto_terminate_time: str
        :param admin_pass: The param of the PostPaidServer
        :type admin_pass: str
        :param availability_zone: The param of the PostPaidServer
        :type availability_zone: str
        :param batch_create_in_multi_az: The param of the PostPaidServer
        :type batch_create_in_multi_az: bool
        :param count: The param of the PostPaidServer
        :type count: int
        :param data_volumes: The param of the PostPaidServer
        :type data_volumes: list[:class:`g42cloudsdkecs.v2.PostPaidServerDataVolume`]
        :param extendparam: The param of the PostPaidServer
        :type extendparam: :class:`g42cloudsdkecs.v2.PostPaidServerExtendParam`
        :param flavor_ref: The param of the PostPaidServer
        :type flavor_ref: str
        :param image_ref: The param of the PostPaidServer
        :type image_ref: str
        :param is_auto_rename: The param of the PostPaidServer
        :type is_auto_rename: bool
        :param key_name: The param of the PostPaidServer
        :type key_name: str
        :param metadata: The param of the PostPaidServer
        :type metadata: dict(str, str)
        :param name: The param of the PostPaidServer
        :type name: str
        :param nics: The param of the PostPaidServer
        :type nics: list[:class:`g42cloudsdkecs.v2.PostPaidServerNic`]
        :param osscheduler_hints: The param of the PostPaidServer
        :type osscheduler_hints: :class:`g42cloudsdkecs.v2.PostPaidServerSchedulerHints`
        :param publicip: The param of the PostPaidServer
        :type publicip: :class:`g42cloudsdkecs.v2.PostPaidServerPublicip`
        :param root_volume: The param of the PostPaidServer
        :type root_volume: :class:`g42cloudsdkecs.v2.PostPaidServerRootVolume`
        :param security_groups: The param of the PostPaidServer
        :type security_groups: list[:class:`g42cloudsdkecs.v2.PostPaidServerSecurityGroup`]
        :param server_tags: The param of the PostPaidServer
        :type server_tags: list[:class:`g42cloudsdkecs.v2.PostPaidServerTag`]
        :param tags: The param of the PostPaidServer
        :type tags: list[str]
        :param user_data: The param of the PostPaidServer
        :type user_data: str
        :param vpcid: The param of the PostPaidServer
        :type vpcid: str
        :param description: The param of the PostPaidServer
        :type description: str
        """
        
        

        self._auto_terminate_time = None
        self._admin_pass = None
        self._availability_zone = None
        self._batch_create_in_multi_az = None
        self._count = None
        self._data_volumes = None
        self._extendparam = None
        self._flavor_ref = None
        self._image_ref = None
        self._is_auto_rename = None
        self._key_name = None
        self._metadata = None
        self._name = None
        self._nics = None
        self._osscheduler_hints = None
        self._publicip = None
        self._root_volume = None
        self._security_groups = None
        self._server_tags = None
        self._tags = None
        self._user_data = None
        self._vpcid = None
        self._description = None
        self.discriminator = None

        if auto_terminate_time is not None:
            self.auto_terminate_time = auto_terminate_time
        if admin_pass is not None:
            self.admin_pass = admin_pass
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if batch_create_in_multi_az is not None:
            self.batch_create_in_multi_az = batch_create_in_multi_az
        if count is not None:
            self.count = count
        if data_volumes is not None:
            self.data_volumes = data_volumes
        if extendparam is not None:
            self.extendparam = extendparam
        self.flavor_ref = flavor_ref
        self.image_ref = image_ref
        if is_auto_rename is not None:
            self.is_auto_rename = is_auto_rename
        if key_name is not None:
            self.key_name = key_name
        if metadata is not None:
            self.metadata = metadata
        self.name = name
        self.nics = nics
        if osscheduler_hints is not None:
            self.osscheduler_hints = osscheduler_hints
        if publicip is not None:
            self.publicip = publicip
        self.root_volume = root_volume
        if security_groups is not None:
            self.security_groups = security_groups
        if server_tags is not None:
            self.server_tags = server_tags
        if tags is not None:
            self.tags = tags
        if user_data is not None:
            self.user_data = user_data
        self.vpcid = vpcid
        if description is not None:
            self.description = description

    @property
    def auto_terminate_time(self):
        """Gets the auto_terminate_time of this PostPaidServer.

        :return: The auto_terminate_time of this PostPaidServer.
        :rtype: str
        """
        return self._auto_terminate_time

    @auto_terminate_time.setter
    def auto_terminate_time(self, auto_terminate_time):
        """Sets the auto_terminate_time of this PostPaidServer.

        :param auto_terminate_time: The auto_terminate_time of this PostPaidServer.
        :type auto_terminate_time: str
        """
        self._auto_terminate_time = auto_terminate_time

    @property
    def admin_pass(self):
        """Gets the admin_pass of this PostPaidServer.

        :return: The admin_pass of this PostPaidServer.
        :rtype: str
        """
        return self._admin_pass

    @admin_pass.setter
    def admin_pass(self, admin_pass):
        """Sets the admin_pass of this PostPaidServer.

        :param admin_pass: The admin_pass of this PostPaidServer.
        :type admin_pass: str
        """
        self._admin_pass = admin_pass

    @property
    def availability_zone(self):
        """Gets the availability_zone of this PostPaidServer.

        :return: The availability_zone of this PostPaidServer.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this PostPaidServer.

        :param availability_zone: The availability_zone of this PostPaidServer.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def batch_create_in_multi_az(self):
        """Gets the batch_create_in_multi_az of this PostPaidServer.

        :return: The batch_create_in_multi_az of this PostPaidServer.
        :rtype: bool
        """
        return self._batch_create_in_multi_az

    @batch_create_in_multi_az.setter
    def batch_create_in_multi_az(self, batch_create_in_multi_az):
        """Sets the batch_create_in_multi_az of this PostPaidServer.

        :param batch_create_in_multi_az: The batch_create_in_multi_az of this PostPaidServer.
        :type batch_create_in_multi_az: bool
        """
        self._batch_create_in_multi_az = batch_create_in_multi_az

    @property
    def count(self):
        """Gets the count of this PostPaidServer.

        :return: The count of this PostPaidServer.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this PostPaidServer.

        :param count: The count of this PostPaidServer.
        :type count: int
        """
        self._count = count

    @property
    def data_volumes(self):
        """Gets the data_volumes of this PostPaidServer.

        :return: The data_volumes of this PostPaidServer.
        :rtype: list[:class:`g42cloudsdkecs.v2.PostPaidServerDataVolume`]
        """
        return self._data_volumes

    @data_volumes.setter
    def data_volumes(self, data_volumes):
        """Sets the data_volumes of this PostPaidServer.

        :param data_volumes: The data_volumes of this PostPaidServer.
        :type data_volumes: list[:class:`g42cloudsdkecs.v2.PostPaidServerDataVolume`]
        """
        self._data_volumes = data_volumes

    @property
    def extendparam(self):
        """Gets the extendparam of this PostPaidServer.

        :return: The extendparam of this PostPaidServer.
        :rtype: :class:`g42cloudsdkecs.v2.PostPaidServerExtendParam`
        """
        return self._extendparam

    @extendparam.setter
    def extendparam(self, extendparam):
        """Sets the extendparam of this PostPaidServer.

        :param extendparam: The extendparam of this PostPaidServer.
        :type extendparam: :class:`g42cloudsdkecs.v2.PostPaidServerExtendParam`
        """
        self._extendparam = extendparam

    @property
    def flavor_ref(self):
        """Gets the flavor_ref of this PostPaidServer.

        :return: The flavor_ref of this PostPaidServer.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        """Sets the flavor_ref of this PostPaidServer.

        :param flavor_ref: The flavor_ref of this PostPaidServer.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def image_ref(self):
        """Gets the image_ref of this PostPaidServer.

        :return: The image_ref of this PostPaidServer.
        :rtype: str
        """
        return self._image_ref

    @image_ref.setter
    def image_ref(self, image_ref):
        """Sets the image_ref of this PostPaidServer.

        :param image_ref: The image_ref of this PostPaidServer.
        :type image_ref: str
        """
        self._image_ref = image_ref

    @property
    def is_auto_rename(self):
        """Gets the is_auto_rename of this PostPaidServer.

        :return: The is_auto_rename of this PostPaidServer.
        :rtype: bool
        """
        return self._is_auto_rename

    @is_auto_rename.setter
    def is_auto_rename(self, is_auto_rename):
        """Sets the is_auto_rename of this PostPaidServer.

        :param is_auto_rename: The is_auto_rename of this PostPaidServer.
        :type is_auto_rename: bool
        """
        self._is_auto_rename = is_auto_rename

    @property
    def key_name(self):
        """Gets the key_name of this PostPaidServer.

        :return: The key_name of this PostPaidServer.
        :rtype: str
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        """Sets the key_name of this PostPaidServer.

        :param key_name: The key_name of this PostPaidServer.
        :type key_name: str
        """
        self._key_name = key_name

    @property
    def metadata(self):
        """Gets the metadata of this PostPaidServer.

        :return: The metadata of this PostPaidServer.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this PostPaidServer.

        :param metadata: The metadata of this PostPaidServer.
        :type metadata: dict(str, str)
        """
        self._metadata = metadata

    @property
    def name(self):
        """Gets the name of this PostPaidServer.

        :return: The name of this PostPaidServer.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PostPaidServer.

        :param name: The name of this PostPaidServer.
        :type name: str
        """
        self._name = name

    @property
    def nics(self):
        """Gets the nics of this PostPaidServer.

        :return: The nics of this PostPaidServer.
        :rtype: list[:class:`g42cloudsdkecs.v2.PostPaidServerNic`]
        """
        return self._nics

    @nics.setter
    def nics(self, nics):
        """Sets the nics of this PostPaidServer.

        :param nics: The nics of this PostPaidServer.
        :type nics: list[:class:`g42cloudsdkecs.v2.PostPaidServerNic`]
        """
        self._nics = nics

    @property
    def osscheduler_hints(self):
        """Gets the osscheduler_hints of this PostPaidServer.

        :return: The osscheduler_hints of this PostPaidServer.
        :rtype: :class:`g42cloudsdkecs.v2.PostPaidServerSchedulerHints`
        """
        return self._osscheduler_hints

    @osscheduler_hints.setter
    def osscheduler_hints(self, osscheduler_hints):
        """Sets the osscheduler_hints of this PostPaidServer.

        :param osscheduler_hints: The osscheduler_hints of this PostPaidServer.
        :type osscheduler_hints: :class:`g42cloudsdkecs.v2.PostPaidServerSchedulerHints`
        """
        self._osscheduler_hints = osscheduler_hints

    @property
    def publicip(self):
        """Gets the publicip of this PostPaidServer.

        :return: The publicip of this PostPaidServer.
        :rtype: :class:`g42cloudsdkecs.v2.PostPaidServerPublicip`
        """
        return self._publicip

    @publicip.setter
    def publicip(self, publicip):
        """Sets the publicip of this PostPaidServer.

        :param publicip: The publicip of this PostPaidServer.
        :type publicip: :class:`g42cloudsdkecs.v2.PostPaidServerPublicip`
        """
        self._publicip = publicip

    @property
    def root_volume(self):
        """Gets the root_volume of this PostPaidServer.

        :return: The root_volume of this PostPaidServer.
        :rtype: :class:`g42cloudsdkecs.v2.PostPaidServerRootVolume`
        """
        return self._root_volume

    @root_volume.setter
    def root_volume(self, root_volume):
        """Sets the root_volume of this PostPaidServer.

        :param root_volume: The root_volume of this PostPaidServer.
        :type root_volume: :class:`g42cloudsdkecs.v2.PostPaidServerRootVolume`
        """
        self._root_volume = root_volume

    @property
    def security_groups(self):
        """Gets the security_groups of this PostPaidServer.

        :return: The security_groups of this PostPaidServer.
        :rtype: list[:class:`g42cloudsdkecs.v2.PostPaidServerSecurityGroup`]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this PostPaidServer.

        :param security_groups: The security_groups of this PostPaidServer.
        :type security_groups: list[:class:`g42cloudsdkecs.v2.PostPaidServerSecurityGroup`]
        """
        self._security_groups = security_groups

    @property
    def server_tags(self):
        """Gets the server_tags of this PostPaidServer.

        :return: The server_tags of this PostPaidServer.
        :rtype: list[:class:`g42cloudsdkecs.v2.PostPaidServerTag`]
        """
        return self._server_tags

    @server_tags.setter
    def server_tags(self, server_tags):
        """Sets the server_tags of this PostPaidServer.

        :param server_tags: The server_tags of this PostPaidServer.
        :type server_tags: list[:class:`g42cloudsdkecs.v2.PostPaidServerTag`]
        """
        self._server_tags = server_tags

    @property
    def tags(self):
        """Gets the tags of this PostPaidServer.

        :return: The tags of this PostPaidServer.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this PostPaidServer.

        :param tags: The tags of this PostPaidServer.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def user_data(self):
        """Gets the user_data of this PostPaidServer.

        :return: The user_data of this PostPaidServer.
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this PostPaidServer.

        :param user_data: The user_data of this PostPaidServer.
        :type user_data: str
        """
        self._user_data = user_data

    @property
    def vpcid(self):
        """Gets the vpcid of this PostPaidServer.

        :return: The vpcid of this PostPaidServer.
        :rtype: str
        """
        return self._vpcid

    @vpcid.setter
    def vpcid(self, vpcid):
        """Sets the vpcid of this PostPaidServer.

        :param vpcid: The vpcid of this PostPaidServer.
        :type vpcid: str
        """
        self._vpcid = vpcid

    @property
    def description(self):
        """Gets the description of this PostPaidServer.

        :return: The description of this PostPaidServer.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PostPaidServer.

        :param description: The description of this PostPaidServer.
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
        if not isinstance(other, PostPaidServer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
