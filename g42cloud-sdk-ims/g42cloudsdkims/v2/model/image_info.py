# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'backup_id': 'str',
        'data_origin': 'str',
        'description': 'str',
        'image_size': 'str',
        'image_source_type': 'str',
        'imagetype': 'str',
        'isregistered': 'str',
        'originalimagename': 'str',
        'os_bit': 'str',
        'os_type': 'str',
        'os_version': 'str',
        'platform': 'str',
        'productcode': 'str',
        'support_diskintensive': 'str',
        'support_highperformance': 'str',
        'support_kvm': 'str',
        'support_kvm_gpu_type': 'str',
        'support_kvm_infiniband': 'str',
        'support_largememory': 'str',
        'support_xen': 'str',
        'support_xen_gpu_type': 'str',
        'support_xen_hana': 'str',
        'system_support_market': 'bool',
        'checksum': 'str',
        'container_format': 'str',
        'created_at': 'str',
        'disk_format': 'str',
        'enterprise_project_id': 'str',
        'file': 'str',
        'id': 'str',
        'min_disk': 'int',
        'min_ram': 'int',
        'name': 'str',
        'owner': 'str',
        'protected': 'bool',
        'schema': 'str',
        '_self': 'str',
        'size': 'int',
        'status': 'str',
        'tags': 'list[str]',
        'updated_at': 'str',
        'virtual_env_type': 'str',
        'virtual_size': 'int',
        'visibility': 'str',
        'support_fc_inject': 'str',
        'hw_firmware_type': 'str',
        'support_arm': 'str',
        'max_ram': 'str',
        'system__cmkid': 'str',
        'os_feature_list': 'str',
        'account_code': 'str',
        'hw_vif_multiqueue_enabled': 'str',
        'is_offshelved': 'str',
        'lazyloading': 'str',
        'root_origin': 'str',
        'sequence_num': 'str',
        'active_at': 'str',
        'support_agent_list': 'str',
        'support_amd': 'str'
    }

    attribute_map = {
        'backup_id': '__backup_id',
        'data_origin': '__data_origin',
        'description': '__description',
        'image_size': '__image_size',
        'image_source_type': '__image_source_type',
        'imagetype': '__imagetype',
        'isregistered': '__isregistered',
        'originalimagename': '__originalimagename',
        'os_bit': '__os_bit',
        'os_type': '__os_type',
        'os_version': '__os_version',
        'platform': '__platform',
        'productcode': '__productcode',
        'support_diskintensive': '__support_diskintensive',
        'support_highperformance': '__support_highperformance',
        'support_kvm': '__support_kvm',
        'support_kvm_gpu_type': '__support_kvm_gpu_type',
        'support_kvm_infiniband': '__support_kvm_infiniband',
        'support_largememory': '__support_largememory',
        'support_xen': '__support_xen',
        'support_xen_gpu_type': '__support_xen_gpu_type',
        'support_xen_hana': '__support_xen_hana',
        'system_support_market': '__system_support_market',
        'checksum': 'checksum',
        'container_format': 'container_format',
        'created_at': 'created_at',
        'disk_format': 'disk_format',
        'enterprise_project_id': 'enterprise_project_id',
        'file': 'file',
        'id': 'id',
        'min_disk': 'min_disk',
        'min_ram': 'min_ram',
        'name': 'name',
        'owner': 'owner',
        'protected': 'protected',
        'schema': 'schema',
        '_self': 'self',
        'size': 'size',
        'status': 'status',
        'tags': 'tags',
        'updated_at': 'updated_at',
        'virtual_env_type': 'virtual_env_type',
        'virtual_size': 'virtual_size',
        'visibility': 'visibility',
        'support_fc_inject': '__support_fc_inject',
        'hw_firmware_type': 'hw_firmware_type',
        'support_arm': '__support_arm',
        'max_ram': 'max_ram',
        'system__cmkid': '__system__cmkid',
        'os_feature_list': '__os_feature_list',
        'account_code': '__account_code',
        'hw_vif_multiqueue_enabled': 'hw_vif_multiqueue_enabled',
        'is_offshelved': '__is_offshelved',
        'lazyloading': '__lazyloading',
        'root_origin': '__root_origin',
        'sequence_num': '__sequence_num',
        'active_at': 'active_at',
        'support_agent_list': '__support_agent_list',
        'support_amd': '__support_amd'
    }

    def __init__(self, backup_id=None, data_origin=None, description=None, image_size=None, image_source_type=None, imagetype=None, isregistered=None, originalimagename=None, os_bit=None, os_type=None, os_version=None, platform=None, productcode=None, support_diskintensive=None, support_highperformance=None, support_kvm=None, support_kvm_gpu_type=None, support_kvm_infiniband=None, support_largememory=None, support_xen=None, support_xen_gpu_type=None, support_xen_hana=None, system_support_market=None, checksum=None, container_format=None, created_at=None, disk_format=None, enterprise_project_id=None, file=None, id=None, min_disk=None, min_ram=None, name=None, owner=None, protected=None, schema=None, _self=None, size=None, status=None, tags=None, updated_at=None, virtual_env_type=None, virtual_size=None, visibility=None, support_fc_inject=None, hw_firmware_type=None, support_arm=None, max_ram=None, system__cmkid=None, os_feature_list=None, account_code=None, hw_vif_multiqueue_enabled=None, is_offshelved=None, lazyloading=None, root_origin=None, sequence_num=None, active_at=None, support_agent_list=None, support_amd=None):
        """ImageInfo

        The model defined in g42cloud sdk

        :param backup_id: The param of the ImageInfo
        :type backup_id: str
        :param data_origin: The param of the ImageInfo
        :type data_origin: str
        :param description: The param of the ImageInfo
        :type description: str
        :param image_size: The param of the ImageInfo
        :type image_size: str
        :param image_source_type: The param of the ImageInfo
        :type image_source_type: str
        :param imagetype: The param of the ImageInfo
        :type imagetype: str
        :param isregistered: The param of the ImageInfo
        :type isregistered: str
        :param originalimagename: The param of the ImageInfo
        :type originalimagename: str
        :param os_bit: The param of the ImageInfo
        :type os_bit: str
        :param os_type: The param of the ImageInfo
        :type os_type: str
        :param os_version: The param of the ImageInfo
        :type os_version: str
        :param platform: The param of the ImageInfo
        :type platform: str
        :param productcode: The param of the ImageInfo
        :type productcode: str
        :param support_diskintensive: The param of the ImageInfo
        :type support_diskintensive: str
        :param support_highperformance: The param of the ImageInfo
        :type support_highperformance: str
        :param support_kvm: The param of the ImageInfo
        :type support_kvm: str
        :param support_kvm_gpu_type: The param of the ImageInfo
        :type support_kvm_gpu_type: str
        :param support_kvm_infiniband: The param of the ImageInfo
        :type support_kvm_infiniband: str
        :param support_largememory: The param of the ImageInfo
        :type support_largememory: str
        :param support_xen: The param of the ImageInfo
        :type support_xen: str
        :param support_xen_gpu_type: The param of the ImageInfo
        :type support_xen_gpu_type: str
        :param support_xen_hana: The param of the ImageInfo
        :type support_xen_hana: str
        :param system_support_market: The param of the ImageInfo
        :type system_support_market: bool
        :param checksum: The param of the ImageInfo
        :type checksum: str
        :param container_format: The param of the ImageInfo
        :type container_format: str
        :param created_at: The param of the ImageInfo
        :type created_at: str
        :param disk_format: The param of the ImageInfo
        :type disk_format: str
        :param enterprise_project_id: The param of the ImageInfo
        :type enterprise_project_id: str
        :param file: The param of the ImageInfo
        :type file: str
        :param id: The param of the ImageInfo
        :type id: str
        :param min_disk: The param of the ImageInfo
        :type min_disk: int
        :param min_ram: The param of the ImageInfo
        :type min_ram: int
        :param name: The param of the ImageInfo
        :type name: str
        :param owner: The param of the ImageInfo
        :type owner: str
        :param protected: The param of the ImageInfo
        :type protected: bool
        :param schema: The param of the ImageInfo
        :type schema: str
        :param _self: The param of the ImageInfo
        :type _self: str
        :param size: The param of the ImageInfo
        :type size: int
        :param status: The param of the ImageInfo
        :type status: str
        :param tags: The param of the ImageInfo
        :type tags: list[str]
        :param updated_at: The param of the ImageInfo
        :type updated_at: str
        :param virtual_env_type: The param of the ImageInfo
        :type virtual_env_type: str
        :param virtual_size: The param of the ImageInfo
        :type virtual_size: int
        :param visibility: The param of the ImageInfo
        :type visibility: str
        :param support_fc_inject: The param of the ImageInfo
        :type support_fc_inject: str
        :param hw_firmware_type: The param of the ImageInfo
        :type hw_firmware_type: str
        :param support_arm: The param of the ImageInfo
        :type support_arm: str
        :param max_ram: The param of the ImageInfo
        :type max_ram: str
        :param system__cmkid: The param of the ImageInfo
        :type system__cmkid: str
        :param os_feature_list: The param of the ImageInfo
        :type os_feature_list: str
        :param account_code: The param of the ImageInfo
        :type account_code: str
        :param hw_vif_multiqueue_enabled: The param of the ImageInfo
        :type hw_vif_multiqueue_enabled: str
        :param is_offshelved: The param of the ImageInfo
        :type is_offshelved: str
        :param lazyloading: The param of the ImageInfo
        :type lazyloading: str
        :param root_origin: The param of the ImageInfo
        :type root_origin: str
        :param sequence_num: The param of the ImageInfo
        :type sequence_num: str
        :param active_at: The param of the ImageInfo
        :type active_at: str
        :param support_agent_list: The param of the ImageInfo
        :type support_agent_list: str
        :param support_amd: The param of the ImageInfo
        :type support_amd: str
        """
        
        

        self._backup_id = None
        self._data_origin = None
        self._description = None
        self._image_size = None
        self._image_source_type = None
        self._imagetype = None
        self._isregistered = None
        self._originalimagename = None
        self._os_bit = None
        self._os_type = None
        self._os_version = None
        self._platform = None
        self._productcode = None
        self._support_diskintensive = None
        self._support_highperformance = None
        self._support_kvm = None
        self._support_kvm_gpu_type = None
        self._support_kvm_infiniband = None
        self._support_largememory = None
        self._support_xen = None
        self._support_xen_gpu_type = None
        self._support_xen_hana = None
        self._system_support_market = None
        self._checksum = None
        self._container_format = None
        self._created_at = None
        self._disk_format = None
        self._enterprise_project_id = None
        self._file = None
        self._id = None
        self._min_disk = None
        self._min_ram = None
        self._name = None
        self._owner = None
        self._protected = None
        self._schema = None
        self.__self = None
        self._size = None
        self._status = None
        self._tags = None
        self._updated_at = None
        self._virtual_env_type = None
        self._virtual_size = None
        self._visibility = None
        self._support_fc_inject = None
        self._hw_firmware_type = None
        self._support_arm = None
        self._max_ram = None
        self._system__cmkid = None
        self._os_feature_list = None
        self._account_code = None
        self._hw_vif_multiqueue_enabled = None
        self._is_offshelved = None
        self._lazyloading = None
        self._root_origin = None
        self._sequence_num = None
        self._active_at = None
        self._support_agent_list = None
        self._support_amd = None
        self.discriminator = None

        if backup_id is not None:
            self.backup_id = backup_id
        if data_origin is not None:
            self.data_origin = data_origin
        if description is not None:
            self.description = description
        self.image_size = image_size
        self.image_source_type = image_source_type
        self.imagetype = imagetype
        self.isregistered = isregistered
        if originalimagename is not None:
            self.originalimagename = originalimagename
        if os_bit is not None:
            self.os_bit = os_bit
        self.os_type = os_type
        if os_version is not None:
            self.os_version = os_version
        if platform is not None:
            self.platform = platform
        if productcode is not None:
            self.productcode = productcode
        if support_diskintensive is not None:
            self.support_diskintensive = support_diskintensive
        if support_highperformance is not None:
            self.support_highperformance = support_highperformance
        if support_kvm is not None:
            self.support_kvm = support_kvm
        if support_kvm_gpu_type is not None:
            self.support_kvm_gpu_type = support_kvm_gpu_type
        if support_kvm_infiniband is not None:
            self.support_kvm_infiniband = support_kvm_infiniband
        if support_largememory is not None:
            self.support_largememory = support_largememory
        if support_xen is not None:
            self.support_xen = support_xen
        if support_xen_gpu_type is not None:
            self.support_xen_gpu_type = support_xen_gpu_type
        if support_xen_hana is not None:
            self.support_xen_hana = support_xen_hana
        if system_support_market is not None:
            self.system_support_market = system_support_market
        if checksum is not None:
            self.checksum = checksum
        self.container_format = container_format
        self.created_at = created_at
        if disk_format is not None:
            self.disk_format = disk_format
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if file is not None:
            self.file = file
        self.id = id
        self.min_disk = min_disk
        self.min_ram = min_ram
        self.name = name
        self.owner = owner
        self.protected = protected
        if schema is not None:
            self.schema = schema
        self._self = _self
        if size is not None:
            self.size = size
        self.status = status
        self.tags = tags
        self.updated_at = updated_at
        self.virtual_env_type = virtual_env_type
        if virtual_size is not None:
            self.virtual_size = virtual_size
        self.visibility = visibility
        if support_fc_inject is not None:
            self.support_fc_inject = support_fc_inject
        if hw_firmware_type is not None:
            self.hw_firmware_type = hw_firmware_type
        if support_arm is not None:
            self.support_arm = support_arm
        if max_ram is not None:
            self.max_ram = max_ram
        if system__cmkid is not None:
            self.system__cmkid = system__cmkid
        if os_feature_list is not None:
            self.os_feature_list = os_feature_list
        if account_code is not None:
            self.account_code = account_code
        if hw_vif_multiqueue_enabled is not None:
            self.hw_vif_multiqueue_enabled = hw_vif_multiqueue_enabled
        if is_offshelved is not None:
            self.is_offshelved = is_offshelved
        if lazyloading is not None:
            self.lazyloading = lazyloading
        if root_origin is not None:
            self.root_origin = root_origin
        if sequence_num is not None:
            self.sequence_num = sequence_num
        self.active_at = active_at
        if support_agent_list is not None:
            self.support_agent_list = support_agent_list
        if support_amd is not None:
            self.support_amd = support_amd

    @property
    def backup_id(self):
        """Gets the backup_id of this ImageInfo.

        :return: The backup_id of this ImageInfo.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        """Sets the backup_id of this ImageInfo.

        :param backup_id: The backup_id of this ImageInfo.
        :type backup_id: str
        """
        self._backup_id = backup_id

    @property
    def data_origin(self):
        """Gets the data_origin of this ImageInfo.

        :return: The data_origin of this ImageInfo.
        :rtype: str
        """
        return self._data_origin

    @data_origin.setter
    def data_origin(self, data_origin):
        """Sets the data_origin of this ImageInfo.

        :param data_origin: The data_origin of this ImageInfo.
        :type data_origin: str
        """
        self._data_origin = data_origin

    @property
    def description(self):
        """Gets the description of this ImageInfo.

        :return: The description of this ImageInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ImageInfo.

        :param description: The description of this ImageInfo.
        :type description: str
        """
        self._description = description

    @property
    def image_size(self):
        """Gets the image_size of this ImageInfo.

        :return: The image_size of this ImageInfo.
        :rtype: str
        """
        return self._image_size

    @image_size.setter
    def image_size(self, image_size):
        """Sets the image_size of this ImageInfo.

        :param image_size: The image_size of this ImageInfo.
        :type image_size: str
        """
        self._image_size = image_size

    @property
    def image_source_type(self):
        """Gets the image_source_type of this ImageInfo.

        :return: The image_source_type of this ImageInfo.
        :rtype: str
        """
        return self._image_source_type

    @image_source_type.setter
    def image_source_type(self, image_source_type):
        """Sets the image_source_type of this ImageInfo.

        :param image_source_type: The image_source_type of this ImageInfo.
        :type image_source_type: str
        """
        self._image_source_type = image_source_type

    @property
    def imagetype(self):
        """Gets the imagetype of this ImageInfo.

        :return: The imagetype of this ImageInfo.
        :rtype: str
        """
        return self._imagetype

    @imagetype.setter
    def imagetype(self, imagetype):
        """Sets the imagetype of this ImageInfo.

        :param imagetype: The imagetype of this ImageInfo.
        :type imagetype: str
        """
        self._imagetype = imagetype

    @property
    def isregistered(self):
        """Gets the isregistered of this ImageInfo.

        :return: The isregistered of this ImageInfo.
        :rtype: str
        """
        return self._isregistered

    @isregistered.setter
    def isregistered(self, isregistered):
        """Sets the isregistered of this ImageInfo.

        :param isregistered: The isregistered of this ImageInfo.
        :type isregistered: str
        """
        self._isregistered = isregistered

    @property
    def originalimagename(self):
        """Gets the originalimagename of this ImageInfo.

        :return: The originalimagename of this ImageInfo.
        :rtype: str
        """
        return self._originalimagename

    @originalimagename.setter
    def originalimagename(self, originalimagename):
        """Sets the originalimagename of this ImageInfo.

        :param originalimagename: The originalimagename of this ImageInfo.
        :type originalimagename: str
        """
        self._originalimagename = originalimagename

    @property
    def os_bit(self):
        """Gets the os_bit of this ImageInfo.

        :return: The os_bit of this ImageInfo.
        :rtype: str
        """
        return self._os_bit

    @os_bit.setter
    def os_bit(self, os_bit):
        """Sets the os_bit of this ImageInfo.

        :param os_bit: The os_bit of this ImageInfo.
        :type os_bit: str
        """
        self._os_bit = os_bit

    @property
    def os_type(self):
        """Gets the os_type of this ImageInfo.

        :return: The os_type of this ImageInfo.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this ImageInfo.

        :param os_type: The os_type of this ImageInfo.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def os_version(self):
        """Gets the os_version of this ImageInfo.

        :return: The os_version of this ImageInfo.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """Sets the os_version of this ImageInfo.

        :param os_version: The os_version of this ImageInfo.
        :type os_version: str
        """
        self._os_version = os_version

    @property
    def platform(self):
        """Gets the platform of this ImageInfo.

        :return: The platform of this ImageInfo.
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this ImageInfo.

        :param platform: The platform of this ImageInfo.
        :type platform: str
        """
        self._platform = platform

    @property
    def productcode(self):
        """Gets the productcode of this ImageInfo.

        :return: The productcode of this ImageInfo.
        :rtype: str
        """
        return self._productcode

    @productcode.setter
    def productcode(self, productcode):
        """Sets the productcode of this ImageInfo.

        :param productcode: The productcode of this ImageInfo.
        :type productcode: str
        """
        self._productcode = productcode

    @property
    def support_diskintensive(self):
        """Gets the support_diskintensive of this ImageInfo.

        :return: The support_diskintensive of this ImageInfo.
        :rtype: str
        """
        return self._support_diskintensive

    @support_diskintensive.setter
    def support_diskintensive(self, support_diskintensive):
        """Sets the support_diskintensive of this ImageInfo.

        :param support_diskintensive: The support_diskintensive of this ImageInfo.
        :type support_diskintensive: str
        """
        self._support_diskintensive = support_diskintensive

    @property
    def support_highperformance(self):
        """Gets the support_highperformance of this ImageInfo.

        :return: The support_highperformance of this ImageInfo.
        :rtype: str
        """
        return self._support_highperformance

    @support_highperformance.setter
    def support_highperformance(self, support_highperformance):
        """Sets the support_highperformance of this ImageInfo.

        :param support_highperformance: The support_highperformance of this ImageInfo.
        :type support_highperformance: str
        """
        self._support_highperformance = support_highperformance

    @property
    def support_kvm(self):
        """Gets the support_kvm of this ImageInfo.

        :return: The support_kvm of this ImageInfo.
        :rtype: str
        """
        return self._support_kvm

    @support_kvm.setter
    def support_kvm(self, support_kvm):
        """Sets the support_kvm of this ImageInfo.

        :param support_kvm: The support_kvm of this ImageInfo.
        :type support_kvm: str
        """
        self._support_kvm = support_kvm

    @property
    def support_kvm_gpu_type(self):
        """Gets the support_kvm_gpu_type of this ImageInfo.

        :return: The support_kvm_gpu_type of this ImageInfo.
        :rtype: str
        """
        return self._support_kvm_gpu_type

    @support_kvm_gpu_type.setter
    def support_kvm_gpu_type(self, support_kvm_gpu_type):
        """Sets the support_kvm_gpu_type of this ImageInfo.

        :param support_kvm_gpu_type: The support_kvm_gpu_type of this ImageInfo.
        :type support_kvm_gpu_type: str
        """
        self._support_kvm_gpu_type = support_kvm_gpu_type

    @property
    def support_kvm_infiniband(self):
        """Gets the support_kvm_infiniband of this ImageInfo.

        :return: The support_kvm_infiniband of this ImageInfo.
        :rtype: str
        """
        return self._support_kvm_infiniband

    @support_kvm_infiniband.setter
    def support_kvm_infiniband(self, support_kvm_infiniband):
        """Sets the support_kvm_infiniband of this ImageInfo.

        :param support_kvm_infiniband: The support_kvm_infiniband of this ImageInfo.
        :type support_kvm_infiniband: str
        """
        self._support_kvm_infiniband = support_kvm_infiniband

    @property
    def support_largememory(self):
        """Gets the support_largememory of this ImageInfo.

        :return: The support_largememory of this ImageInfo.
        :rtype: str
        """
        return self._support_largememory

    @support_largememory.setter
    def support_largememory(self, support_largememory):
        """Sets the support_largememory of this ImageInfo.

        :param support_largememory: The support_largememory of this ImageInfo.
        :type support_largememory: str
        """
        self._support_largememory = support_largememory

    @property
    def support_xen(self):
        """Gets the support_xen of this ImageInfo.

        :return: The support_xen of this ImageInfo.
        :rtype: str
        """
        return self._support_xen

    @support_xen.setter
    def support_xen(self, support_xen):
        """Sets the support_xen of this ImageInfo.

        :param support_xen: The support_xen of this ImageInfo.
        :type support_xen: str
        """
        self._support_xen = support_xen

    @property
    def support_xen_gpu_type(self):
        """Gets the support_xen_gpu_type of this ImageInfo.

        :return: The support_xen_gpu_type of this ImageInfo.
        :rtype: str
        """
        return self._support_xen_gpu_type

    @support_xen_gpu_type.setter
    def support_xen_gpu_type(self, support_xen_gpu_type):
        """Sets the support_xen_gpu_type of this ImageInfo.

        :param support_xen_gpu_type: The support_xen_gpu_type of this ImageInfo.
        :type support_xen_gpu_type: str
        """
        self._support_xen_gpu_type = support_xen_gpu_type

    @property
    def support_xen_hana(self):
        """Gets the support_xen_hana of this ImageInfo.

        :return: The support_xen_hana of this ImageInfo.
        :rtype: str
        """
        return self._support_xen_hana

    @support_xen_hana.setter
    def support_xen_hana(self, support_xen_hana):
        """Sets the support_xen_hana of this ImageInfo.

        :param support_xen_hana: The support_xen_hana of this ImageInfo.
        :type support_xen_hana: str
        """
        self._support_xen_hana = support_xen_hana

    @property
    def system_support_market(self):
        """Gets the system_support_market of this ImageInfo.

        :return: The system_support_market of this ImageInfo.
        :rtype: bool
        """
        return self._system_support_market

    @system_support_market.setter
    def system_support_market(self, system_support_market):
        """Sets the system_support_market of this ImageInfo.

        :param system_support_market: The system_support_market of this ImageInfo.
        :type system_support_market: bool
        """
        self._system_support_market = system_support_market

    @property
    def checksum(self):
        """Gets the checksum of this ImageInfo.

        :return: The checksum of this ImageInfo.
        :rtype: str
        """
        return self._checksum

    @checksum.setter
    def checksum(self, checksum):
        """Sets the checksum of this ImageInfo.

        :param checksum: The checksum of this ImageInfo.
        :type checksum: str
        """
        self._checksum = checksum

    @property
    def container_format(self):
        """Gets the container_format of this ImageInfo.

        :return: The container_format of this ImageInfo.
        :rtype: str
        """
        return self._container_format

    @container_format.setter
    def container_format(self, container_format):
        """Sets the container_format of this ImageInfo.

        :param container_format: The container_format of this ImageInfo.
        :type container_format: str
        """
        self._container_format = container_format

    @property
    def created_at(self):
        """Gets the created_at of this ImageInfo.

        :return: The created_at of this ImageInfo.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ImageInfo.

        :param created_at: The created_at of this ImageInfo.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def disk_format(self):
        """Gets the disk_format of this ImageInfo.

        :return: The disk_format of this ImageInfo.
        :rtype: str
        """
        return self._disk_format

    @disk_format.setter
    def disk_format(self, disk_format):
        """Sets the disk_format of this ImageInfo.

        :param disk_format: The disk_format of this ImageInfo.
        :type disk_format: str
        """
        self._disk_format = disk_format

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ImageInfo.

        :return: The enterprise_project_id of this ImageInfo.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ImageInfo.

        :param enterprise_project_id: The enterprise_project_id of this ImageInfo.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def file(self):
        """Gets the file of this ImageInfo.

        :return: The file of this ImageInfo.
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this ImageInfo.

        :param file: The file of this ImageInfo.
        :type file: str
        """
        self._file = file

    @property
    def id(self):
        """Gets the id of this ImageInfo.

        :return: The id of this ImageInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ImageInfo.

        :param id: The id of this ImageInfo.
        :type id: str
        """
        self._id = id

    @property
    def min_disk(self):
        """Gets the min_disk of this ImageInfo.

        :return: The min_disk of this ImageInfo.
        :rtype: int
        """
        return self._min_disk

    @min_disk.setter
    def min_disk(self, min_disk):
        """Sets the min_disk of this ImageInfo.

        :param min_disk: The min_disk of this ImageInfo.
        :type min_disk: int
        """
        self._min_disk = min_disk

    @property
    def min_ram(self):
        """Gets the min_ram of this ImageInfo.

        :return: The min_ram of this ImageInfo.
        :rtype: int
        """
        return self._min_ram

    @min_ram.setter
    def min_ram(self, min_ram):
        """Sets the min_ram of this ImageInfo.

        :param min_ram: The min_ram of this ImageInfo.
        :type min_ram: int
        """
        self._min_ram = min_ram

    @property
    def name(self):
        """Gets the name of this ImageInfo.

        :return: The name of this ImageInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ImageInfo.

        :param name: The name of this ImageInfo.
        :type name: str
        """
        self._name = name

    @property
    def owner(self):
        """Gets the owner of this ImageInfo.

        :return: The owner of this ImageInfo.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this ImageInfo.

        :param owner: The owner of this ImageInfo.
        :type owner: str
        """
        self._owner = owner

    @property
    def protected(self):
        """Gets the protected of this ImageInfo.

        :return: The protected of this ImageInfo.
        :rtype: bool
        """
        return self._protected

    @protected.setter
    def protected(self, protected):
        """Sets the protected of this ImageInfo.

        :param protected: The protected of this ImageInfo.
        :type protected: bool
        """
        self._protected = protected

    @property
    def schema(self):
        """Gets the schema of this ImageInfo.

        :return: The schema of this ImageInfo.
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this ImageInfo.

        :param schema: The schema of this ImageInfo.
        :type schema: str
        """
        self._schema = schema

    @property
    def _self(self):
        """Gets the _self of this ImageInfo.

        :return: The _self of this ImageInfo.
        :rtype: str
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this ImageInfo.

        :param _self: The _self of this ImageInfo.
        :type _self: str
        """
        self.__self = _self

    @property
    def size(self):
        """Gets the size of this ImageInfo.

        :return: The size of this ImageInfo.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ImageInfo.

        :param size: The size of this ImageInfo.
        :type size: int
        """
        self._size = size

    @property
    def status(self):
        """Gets the status of this ImageInfo.

        :return: The status of this ImageInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ImageInfo.

        :param status: The status of this ImageInfo.
        :type status: str
        """
        self._status = status

    @property
    def tags(self):
        """Gets the tags of this ImageInfo.

        :return: The tags of this ImageInfo.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ImageInfo.

        :param tags: The tags of this ImageInfo.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def updated_at(self):
        """Gets the updated_at of this ImageInfo.

        :return: The updated_at of this ImageInfo.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ImageInfo.

        :param updated_at: The updated_at of this ImageInfo.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def virtual_env_type(self):
        """Gets the virtual_env_type of this ImageInfo.

        :return: The virtual_env_type of this ImageInfo.
        :rtype: str
        """
        return self._virtual_env_type

    @virtual_env_type.setter
    def virtual_env_type(self, virtual_env_type):
        """Sets the virtual_env_type of this ImageInfo.

        :param virtual_env_type: The virtual_env_type of this ImageInfo.
        :type virtual_env_type: str
        """
        self._virtual_env_type = virtual_env_type

    @property
    def virtual_size(self):
        """Gets the virtual_size of this ImageInfo.

        :return: The virtual_size of this ImageInfo.
        :rtype: int
        """
        return self._virtual_size

    @virtual_size.setter
    def virtual_size(self, virtual_size):
        """Sets the virtual_size of this ImageInfo.

        :param virtual_size: The virtual_size of this ImageInfo.
        :type virtual_size: int
        """
        self._virtual_size = virtual_size

    @property
    def visibility(self):
        """Gets the visibility of this ImageInfo.

        :return: The visibility of this ImageInfo.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this ImageInfo.

        :param visibility: The visibility of this ImageInfo.
        :type visibility: str
        """
        self._visibility = visibility

    @property
    def support_fc_inject(self):
        """Gets the support_fc_inject of this ImageInfo.

        :return: The support_fc_inject of this ImageInfo.
        :rtype: str
        """
        return self._support_fc_inject

    @support_fc_inject.setter
    def support_fc_inject(self, support_fc_inject):
        """Sets the support_fc_inject of this ImageInfo.

        :param support_fc_inject: The support_fc_inject of this ImageInfo.
        :type support_fc_inject: str
        """
        self._support_fc_inject = support_fc_inject

    @property
    def hw_firmware_type(self):
        """Gets the hw_firmware_type of this ImageInfo.

        :return: The hw_firmware_type of this ImageInfo.
        :rtype: str
        """
        return self._hw_firmware_type

    @hw_firmware_type.setter
    def hw_firmware_type(self, hw_firmware_type):
        """Sets the hw_firmware_type of this ImageInfo.

        :param hw_firmware_type: The hw_firmware_type of this ImageInfo.
        :type hw_firmware_type: str
        """
        self._hw_firmware_type = hw_firmware_type

    @property
    def support_arm(self):
        """Gets the support_arm of this ImageInfo.

        :return: The support_arm of this ImageInfo.
        :rtype: str
        """
        return self._support_arm

    @support_arm.setter
    def support_arm(self, support_arm):
        """Sets the support_arm of this ImageInfo.

        :param support_arm: The support_arm of this ImageInfo.
        :type support_arm: str
        """
        self._support_arm = support_arm

    @property
    def max_ram(self):
        """Gets the max_ram of this ImageInfo.

        :return: The max_ram of this ImageInfo.
        :rtype: str
        """
        return self._max_ram

    @max_ram.setter
    def max_ram(self, max_ram):
        """Sets the max_ram of this ImageInfo.

        :param max_ram: The max_ram of this ImageInfo.
        :type max_ram: str
        """
        self._max_ram = max_ram

    @property
    def system__cmkid(self):
        """Gets the system__cmkid of this ImageInfo.

        :return: The system__cmkid of this ImageInfo.
        :rtype: str
        """
        return self._system__cmkid

    @system__cmkid.setter
    def system__cmkid(self, system__cmkid):
        """Sets the system__cmkid of this ImageInfo.

        :param system__cmkid: The system__cmkid of this ImageInfo.
        :type system__cmkid: str
        """
        self._system__cmkid = system__cmkid

    @property
    def os_feature_list(self):
        """Gets the os_feature_list of this ImageInfo.

        :return: The os_feature_list of this ImageInfo.
        :rtype: str
        """
        return self._os_feature_list

    @os_feature_list.setter
    def os_feature_list(self, os_feature_list):
        """Sets the os_feature_list of this ImageInfo.

        :param os_feature_list: The os_feature_list of this ImageInfo.
        :type os_feature_list: str
        """
        self._os_feature_list = os_feature_list

    @property
    def account_code(self):
        """Gets the account_code of this ImageInfo.

        :return: The account_code of this ImageInfo.
        :rtype: str
        """
        return self._account_code

    @account_code.setter
    def account_code(self, account_code):
        """Sets the account_code of this ImageInfo.

        :param account_code: The account_code of this ImageInfo.
        :type account_code: str
        """
        self._account_code = account_code

    @property
    def hw_vif_multiqueue_enabled(self):
        """Gets the hw_vif_multiqueue_enabled of this ImageInfo.

        :return: The hw_vif_multiqueue_enabled of this ImageInfo.
        :rtype: str
        """
        return self._hw_vif_multiqueue_enabled

    @hw_vif_multiqueue_enabled.setter
    def hw_vif_multiqueue_enabled(self, hw_vif_multiqueue_enabled):
        """Sets the hw_vif_multiqueue_enabled of this ImageInfo.

        :param hw_vif_multiqueue_enabled: The hw_vif_multiqueue_enabled of this ImageInfo.
        :type hw_vif_multiqueue_enabled: str
        """
        self._hw_vif_multiqueue_enabled = hw_vif_multiqueue_enabled

    @property
    def is_offshelved(self):
        """Gets the is_offshelved of this ImageInfo.

        :return: The is_offshelved of this ImageInfo.
        :rtype: str
        """
        return self._is_offshelved

    @is_offshelved.setter
    def is_offshelved(self, is_offshelved):
        """Sets the is_offshelved of this ImageInfo.

        :param is_offshelved: The is_offshelved of this ImageInfo.
        :type is_offshelved: str
        """
        self._is_offshelved = is_offshelved

    @property
    def lazyloading(self):
        """Gets the lazyloading of this ImageInfo.

        :return: The lazyloading of this ImageInfo.
        :rtype: str
        """
        return self._lazyloading

    @lazyloading.setter
    def lazyloading(self, lazyloading):
        """Sets the lazyloading of this ImageInfo.

        :param lazyloading: The lazyloading of this ImageInfo.
        :type lazyloading: str
        """
        self._lazyloading = lazyloading

    @property
    def root_origin(self):
        """Gets the root_origin of this ImageInfo.

        :return: The root_origin of this ImageInfo.
        :rtype: str
        """
        return self._root_origin

    @root_origin.setter
    def root_origin(self, root_origin):
        """Sets the root_origin of this ImageInfo.

        :param root_origin: The root_origin of this ImageInfo.
        :type root_origin: str
        """
        self._root_origin = root_origin

    @property
    def sequence_num(self):
        """Gets the sequence_num of this ImageInfo.

        :return: The sequence_num of this ImageInfo.
        :rtype: str
        """
        return self._sequence_num

    @sequence_num.setter
    def sequence_num(self, sequence_num):
        """Sets the sequence_num of this ImageInfo.

        :param sequence_num: The sequence_num of this ImageInfo.
        :type sequence_num: str
        """
        self._sequence_num = sequence_num

    @property
    def active_at(self):
        """Gets the active_at of this ImageInfo.

        :return: The active_at of this ImageInfo.
        :rtype: str
        """
        return self._active_at

    @active_at.setter
    def active_at(self, active_at):
        """Sets the active_at of this ImageInfo.

        :param active_at: The active_at of this ImageInfo.
        :type active_at: str
        """
        self._active_at = active_at

    @property
    def support_agent_list(self):
        """Gets the support_agent_list of this ImageInfo.

        :return: The support_agent_list of this ImageInfo.
        :rtype: str
        """
        return self._support_agent_list

    @support_agent_list.setter
    def support_agent_list(self, support_agent_list):
        """Sets the support_agent_list of this ImageInfo.

        :param support_agent_list: The support_agent_list of this ImageInfo.
        :type support_agent_list: str
        """
        self._support_agent_list = support_agent_list

    @property
    def support_amd(self):
        """Gets the support_amd of this ImageInfo.

        :return: The support_amd of this ImageInfo.
        :rtype: str
        """
        return self._support_amd

    @support_amd.setter
    def support_amd(self, support_amd):
        """Sets the support_amd of this ImageInfo.

        :param support_amd: The support_amd of this ImageInfo.
        :type support_amd: str
        """
        self._support_amd = support_amd

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
        if not isinstance(other, ImageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
