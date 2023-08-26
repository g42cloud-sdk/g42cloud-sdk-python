# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListImagesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'imagetype': 'str',
        'isregistered': 'str',
        'os_bit': 'str',
        'os_type': 'str',
        'platform': 'str',
        'support_diskintensive': 'str',
        'support_highperformance': 'str',
        'support_kvm': 'str',
        'support_kvm_gpu_type': 'str',
        'support_kvm_infiniband': 'str',
        'support_largememory': 'str',
        'support_xen': 'str',
        'support_xen_gpu_type': 'str',
        'support_xen_hana': 'str',
        'container_format': 'str',
        'disk_format': 'str',
        'enterprise_project_id': 'str',
        'id': 'str',
        'limit': 'int',
        'marker': 'str',
        'member_status': 'str',
        'min_disk': 'int',
        'min_ram': 'int',
        'name': 'str',
        'owner': 'str',
        'protected': 'bool',
        'sort_dir': 'str',
        'sort_key': 'str',
        'status': 'str',
        'tag': 'str',
        'virtual_env_type': 'str',
        'visibility': 'str',
        'x_sdk_date': 'str',
        'flavor_id': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'architecture': 'str'
    }

    attribute_map = {
        'imagetype': '__imagetype',
        'isregistered': '__isregistered',
        'os_bit': '__os_bit',
        'os_type': '__os_type',
        'platform': '__platform',
        'support_diskintensive': '__support_diskintensive',
        'support_highperformance': '__support_highperformance',
        'support_kvm': '__support_kvm',
        'support_kvm_gpu_type': '__support_kvm_gpu_type',
        'support_kvm_infiniband': '__support_kvm_infiniband',
        'support_largememory': '__support_largememory',
        'support_xen': '__support_xen',
        'support_xen_gpu_type': '__support_xen_gpu_type',
        'support_xen_hana': '__support_xen_hana',
        'container_format': 'container_format',
        'disk_format': 'disk_format',
        'enterprise_project_id': 'enterprise_project_id',
        'id': 'id',
        'limit': 'limit',
        'marker': 'marker',
        'member_status': 'member_status',
        'min_disk': 'min_disk',
        'min_ram': 'min_ram',
        'name': 'name',
        'owner': 'owner',
        'protected': 'protected',
        'sort_dir': 'sort_dir',
        'sort_key': 'sort_key',
        'status': 'status',
        'tag': 'tag',
        'virtual_env_type': 'virtual_env_type',
        'visibility': 'visibility',
        'x_sdk_date': 'X-Sdk-Date',
        'flavor_id': 'flavor_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'architecture': 'architecture'
    }

    def __init__(self, imagetype=None, isregistered=None, os_bit=None, os_type=None, platform=None, support_diskintensive=None, support_highperformance=None, support_kvm=None, support_kvm_gpu_type=None, support_kvm_infiniband=None, support_largememory=None, support_xen=None, support_xen_gpu_type=None, support_xen_hana=None, container_format=None, disk_format=None, enterprise_project_id=None, id=None, limit=None, marker=None, member_status=None, min_disk=None, min_ram=None, name=None, owner=None, protected=None, sort_dir=None, sort_key=None, status=None, tag=None, virtual_env_type=None, visibility=None, x_sdk_date=None, flavor_id=None, created_at=None, updated_at=None, architecture=None):
        """ListImagesRequest

        The model defined in g42cloud sdk

        :param imagetype: The param of the ListImagesRequest
        :type imagetype: str
        :param isregistered: The param of the ListImagesRequest
        :type isregistered: str
        :param os_bit: The param of the ListImagesRequest
        :type os_bit: str
        :param os_type: The param of the ListImagesRequest
        :type os_type: str
        :param platform: The param of the ListImagesRequest
        :type platform: str
        :param support_diskintensive: The param of the ListImagesRequest
        :type support_diskintensive: str
        :param support_highperformance: The param of the ListImagesRequest
        :type support_highperformance: str
        :param support_kvm: The param of the ListImagesRequest
        :type support_kvm: str
        :param support_kvm_gpu_type: The param of the ListImagesRequest
        :type support_kvm_gpu_type: str
        :param support_kvm_infiniband: The param of the ListImagesRequest
        :type support_kvm_infiniband: str
        :param support_largememory: The param of the ListImagesRequest
        :type support_largememory: str
        :param support_xen: The param of the ListImagesRequest
        :type support_xen: str
        :param support_xen_gpu_type: The param of the ListImagesRequest
        :type support_xen_gpu_type: str
        :param support_xen_hana: The param of the ListImagesRequest
        :type support_xen_hana: str
        :param container_format: The param of the ListImagesRequest
        :type container_format: str
        :param disk_format: The param of the ListImagesRequest
        :type disk_format: str
        :param enterprise_project_id: The param of the ListImagesRequest
        :type enterprise_project_id: str
        :param id: The param of the ListImagesRequest
        :type id: str
        :param limit: The param of the ListImagesRequest
        :type limit: int
        :param marker: The param of the ListImagesRequest
        :type marker: str
        :param member_status: The param of the ListImagesRequest
        :type member_status: str
        :param min_disk: The param of the ListImagesRequest
        :type min_disk: int
        :param min_ram: The param of the ListImagesRequest
        :type min_ram: int
        :param name: The param of the ListImagesRequest
        :type name: str
        :param owner: The param of the ListImagesRequest
        :type owner: str
        :param protected: The param of the ListImagesRequest
        :type protected: bool
        :param sort_dir: The param of the ListImagesRequest
        :type sort_dir: str
        :param sort_key: The param of the ListImagesRequest
        :type sort_key: str
        :param status: The param of the ListImagesRequest
        :type status: str
        :param tag: The param of the ListImagesRequest
        :type tag: str
        :param virtual_env_type: The param of the ListImagesRequest
        :type virtual_env_type: str
        :param visibility: The param of the ListImagesRequest
        :type visibility: str
        :param x_sdk_date: The param of the ListImagesRequest
        :type x_sdk_date: str
        :param flavor_id: The param of the ListImagesRequest
        :type flavor_id: str
        :param created_at: The param of the ListImagesRequest
        :type created_at: str
        :param updated_at: The param of the ListImagesRequest
        :type updated_at: str
        :param architecture: The param of the ListImagesRequest
        :type architecture: str
        """
        
        

        self._imagetype = None
        self._isregistered = None
        self._os_bit = None
        self._os_type = None
        self._platform = None
        self._support_diskintensive = None
        self._support_highperformance = None
        self._support_kvm = None
        self._support_kvm_gpu_type = None
        self._support_kvm_infiniband = None
        self._support_largememory = None
        self._support_xen = None
        self._support_xen_gpu_type = None
        self._support_xen_hana = None
        self._container_format = None
        self._disk_format = None
        self._enterprise_project_id = None
        self._id = None
        self._limit = None
        self._marker = None
        self._member_status = None
        self._min_disk = None
        self._min_ram = None
        self._name = None
        self._owner = None
        self._protected = None
        self._sort_dir = None
        self._sort_key = None
        self._status = None
        self._tag = None
        self._virtual_env_type = None
        self._visibility = None
        self._x_sdk_date = None
        self._flavor_id = None
        self._created_at = None
        self._updated_at = None
        self._architecture = None
        self.discriminator = None

        if imagetype is not None:
            self.imagetype = imagetype
        if isregistered is not None:
            self.isregistered = isregistered
        if os_bit is not None:
            self.os_bit = os_bit
        if os_type is not None:
            self.os_type = os_type
        if platform is not None:
            self.platform = platform
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
        if container_format is not None:
            self.container_format = container_format
        if disk_format is not None:
            self.disk_format = disk_format
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if id is not None:
            self.id = id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if member_status is not None:
            self.member_status = member_status
        if min_disk is not None:
            self.min_disk = min_disk
        if min_ram is not None:
            self.min_ram = min_ram
        if name is not None:
            self.name = name
        if owner is not None:
            self.owner = owner
        if protected is not None:
            self.protected = protected
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if sort_key is not None:
            self.sort_key = sort_key
        if status is not None:
            self.status = status
        if tag is not None:
            self.tag = tag
        if virtual_env_type is not None:
            self.virtual_env_type = virtual_env_type
        if visibility is not None:
            self.visibility = visibility
        if x_sdk_date is not None:
            self.x_sdk_date = x_sdk_date
        if flavor_id is not None:
            self.flavor_id = flavor_id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if architecture is not None:
            self.architecture = architecture

    @property
    def imagetype(self):
        """Gets the imagetype of this ListImagesRequest.

        :return: The imagetype of this ListImagesRequest.
        :rtype: str
        """
        return self._imagetype

    @imagetype.setter
    def imagetype(self, imagetype):
        """Sets the imagetype of this ListImagesRequest.

        :param imagetype: The imagetype of this ListImagesRequest.
        :type imagetype: str
        """
        self._imagetype = imagetype

    @property
    def isregistered(self):
        """Gets the isregistered of this ListImagesRequest.

        :return: The isregistered of this ListImagesRequest.
        :rtype: str
        """
        return self._isregistered

    @isregistered.setter
    def isregistered(self, isregistered):
        """Sets the isregistered of this ListImagesRequest.

        :param isregistered: The isregistered of this ListImagesRequest.
        :type isregistered: str
        """
        self._isregistered = isregistered

    @property
    def os_bit(self):
        """Gets the os_bit of this ListImagesRequest.

        :return: The os_bit of this ListImagesRequest.
        :rtype: str
        """
        return self._os_bit

    @os_bit.setter
    def os_bit(self, os_bit):
        """Sets the os_bit of this ListImagesRequest.

        :param os_bit: The os_bit of this ListImagesRequest.
        :type os_bit: str
        """
        self._os_bit = os_bit

    @property
    def os_type(self):
        """Gets the os_type of this ListImagesRequest.

        :return: The os_type of this ListImagesRequest.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this ListImagesRequest.

        :param os_type: The os_type of this ListImagesRequest.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def platform(self):
        """Gets the platform of this ListImagesRequest.

        :return: The platform of this ListImagesRequest.
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this ListImagesRequest.

        :param platform: The platform of this ListImagesRequest.
        :type platform: str
        """
        self._platform = platform

    @property
    def support_diskintensive(self):
        """Gets the support_diskintensive of this ListImagesRequest.

        :return: The support_diskintensive of this ListImagesRequest.
        :rtype: str
        """
        return self._support_diskintensive

    @support_diskintensive.setter
    def support_diskintensive(self, support_diskintensive):
        """Sets the support_diskintensive of this ListImagesRequest.

        :param support_diskintensive: The support_diskintensive of this ListImagesRequest.
        :type support_diskintensive: str
        """
        self._support_diskintensive = support_diskintensive

    @property
    def support_highperformance(self):
        """Gets the support_highperformance of this ListImagesRequest.

        :return: The support_highperformance of this ListImagesRequest.
        :rtype: str
        """
        return self._support_highperformance

    @support_highperformance.setter
    def support_highperformance(self, support_highperformance):
        """Sets the support_highperformance of this ListImagesRequest.

        :param support_highperformance: The support_highperformance of this ListImagesRequest.
        :type support_highperformance: str
        """
        self._support_highperformance = support_highperformance

    @property
    def support_kvm(self):
        """Gets the support_kvm of this ListImagesRequest.

        :return: The support_kvm of this ListImagesRequest.
        :rtype: str
        """
        return self._support_kvm

    @support_kvm.setter
    def support_kvm(self, support_kvm):
        """Sets the support_kvm of this ListImagesRequest.

        :param support_kvm: The support_kvm of this ListImagesRequest.
        :type support_kvm: str
        """
        self._support_kvm = support_kvm

    @property
    def support_kvm_gpu_type(self):
        """Gets the support_kvm_gpu_type of this ListImagesRequest.

        :return: The support_kvm_gpu_type of this ListImagesRequest.
        :rtype: str
        """
        return self._support_kvm_gpu_type

    @support_kvm_gpu_type.setter
    def support_kvm_gpu_type(self, support_kvm_gpu_type):
        """Sets the support_kvm_gpu_type of this ListImagesRequest.

        :param support_kvm_gpu_type: The support_kvm_gpu_type of this ListImagesRequest.
        :type support_kvm_gpu_type: str
        """
        self._support_kvm_gpu_type = support_kvm_gpu_type

    @property
    def support_kvm_infiniband(self):
        """Gets the support_kvm_infiniband of this ListImagesRequest.

        :return: The support_kvm_infiniband of this ListImagesRequest.
        :rtype: str
        """
        return self._support_kvm_infiniband

    @support_kvm_infiniband.setter
    def support_kvm_infiniband(self, support_kvm_infiniband):
        """Sets the support_kvm_infiniband of this ListImagesRequest.

        :param support_kvm_infiniband: The support_kvm_infiniband of this ListImagesRequest.
        :type support_kvm_infiniband: str
        """
        self._support_kvm_infiniband = support_kvm_infiniband

    @property
    def support_largememory(self):
        """Gets the support_largememory of this ListImagesRequest.

        :return: The support_largememory of this ListImagesRequest.
        :rtype: str
        """
        return self._support_largememory

    @support_largememory.setter
    def support_largememory(self, support_largememory):
        """Sets the support_largememory of this ListImagesRequest.

        :param support_largememory: The support_largememory of this ListImagesRequest.
        :type support_largememory: str
        """
        self._support_largememory = support_largememory

    @property
    def support_xen(self):
        """Gets the support_xen of this ListImagesRequest.

        :return: The support_xen of this ListImagesRequest.
        :rtype: str
        """
        return self._support_xen

    @support_xen.setter
    def support_xen(self, support_xen):
        """Sets the support_xen of this ListImagesRequest.

        :param support_xen: The support_xen of this ListImagesRequest.
        :type support_xen: str
        """
        self._support_xen = support_xen

    @property
    def support_xen_gpu_type(self):
        """Gets the support_xen_gpu_type of this ListImagesRequest.

        :return: The support_xen_gpu_type of this ListImagesRequest.
        :rtype: str
        """
        return self._support_xen_gpu_type

    @support_xen_gpu_type.setter
    def support_xen_gpu_type(self, support_xen_gpu_type):
        """Sets the support_xen_gpu_type of this ListImagesRequest.

        :param support_xen_gpu_type: The support_xen_gpu_type of this ListImagesRequest.
        :type support_xen_gpu_type: str
        """
        self._support_xen_gpu_type = support_xen_gpu_type

    @property
    def support_xen_hana(self):
        """Gets the support_xen_hana of this ListImagesRequest.

        :return: The support_xen_hana of this ListImagesRequest.
        :rtype: str
        """
        return self._support_xen_hana

    @support_xen_hana.setter
    def support_xen_hana(self, support_xen_hana):
        """Sets the support_xen_hana of this ListImagesRequest.

        :param support_xen_hana: The support_xen_hana of this ListImagesRequest.
        :type support_xen_hana: str
        """
        self._support_xen_hana = support_xen_hana

    @property
    def container_format(self):
        """Gets the container_format of this ListImagesRequest.

        :return: The container_format of this ListImagesRequest.
        :rtype: str
        """
        return self._container_format

    @container_format.setter
    def container_format(self, container_format):
        """Sets the container_format of this ListImagesRequest.

        :param container_format: The container_format of this ListImagesRequest.
        :type container_format: str
        """
        self._container_format = container_format

    @property
    def disk_format(self):
        """Gets the disk_format of this ListImagesRequest.

        :return: The disk_format of this ListImagesRequest.
        :rtype: str
        """
        return self._disk_format

    @disk_format.setter
    def disk_format(self, disk_format):
        """Sets the disk_format of this ListImagesRequest.

        :param disk_format: The disk_format of this ListImagesRequest.
        :type disk_format: str
        """
        self._disk_format = disk_format

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListImagesRequest.

        :return: The enterprise_project_id of this ListImagesRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListImagesRequest.

        :param enterprise_project_id: The enterprise_project_id of this ListImagesRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def id(self):
        """Gets the id of this ListImagesRequest.

        :return: The id of this ListImagesRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListImagesRequest.

        :param id: The id of this ListImagesRequest.
        :type id: str
        """
        self._id = id

    @property
    def limit(self):
        """Gets the limit of this ListImagesRequest.

        :return: The limit of this ListImagesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListImagesRequest.

        :param limit: The limit of this ListImagesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListImagesRequest.

        :return: The marker of this ListImagesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListImagesRequest.

        :param marker: The marker of this ListImagesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def member_status(self):
        """Gets the member_status of this ListImagesRequest.

        :return: The member_status of this ListImagesRequest.
        :rtype: str
        """
        return self._member_status

    @member_status.setter
    def member_status(self, member_status):
        """Sets the member_status of this ListImagesRequest.

        :param member_status: The member_status of this ListImagesRequest.
        :type member_status: str
        """
        self._member_status = member_status

    @property
    def min_disk(self):
        """Gets the min_disk of this ListImagesRequest.

        :return: The min_disk of this ListImagesRequest.
        :rtype: int
        """
        return self._min_disk

    @min_disk.setter
    def min_disk(self, min_disk):
        """Sets the min_disk of this ListImagesRequest.

        :param min_disk: The min_disk of this ListImagesRequest.
        :type min_disk: int
        """
        self._min_disk = min_disk

    @property
    def min_ram(self):
        """Gets the min_ram of this ListImagesRequest.

        :return: The min_ram of this ListImagesRequest.
        :rtype: int
        """
        return self._min_ram

    @min_ram.setter
    def min_ram(self, min_ram):
        """Sets the min_ram of this ListImagesRequest.

        :param min_ram: The min_ram of this ListImagesRequest.
        :type min_ram: int
        """
        self._min_ram = min_ram

    @property
    def name(self):
        """Gets the name of this ListImagesRequest.

        :return: The name of this ListImagesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListImagesRequest.

        :param name: The name of this ListImagesRequest.
        :type name: str
        """
        self._name = name

    @property
    def owner(self):
        """Gets the owner of this ListImagesRequest.

        :return: The owner of this ListImagesRequest.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this ListImagesRequest.

        :param owner: The owner of this ListImagesRequest.
        :type owner: str
        """
        self._owner = owner

    @property
    def protected(self):
        """Gets the protected of this ListImagesRequest.

        :return: The protected of this ListImagesRequest.
        :rtype: bool
        """
        return self._protected

    @protected.setter
    def protected(self, protected):
        """Sets the protected of this ListImagesRequest.

        :param protected: The protected of this ListImagesRequest.
        :type protected: bool
        """
        self._protected = protected

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListImagesRequest.

        :return: The sort_dir of this ListImagesRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListImagesRequest.

        :param sort_dir: The sort_dir of this ListImagesRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def sort_key(self):
        """Gets the sort_key of this ListImagesRequest.

        :return: The sort_key of this ListImagesRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListImagesRequest.

        :param sort_key: The sort_key of this ListImagesRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def status(self):
        """Gets the status of this ListImagesRequest.

        :return: The status of this ListImagesRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListImagesRequest.

        :param status: The status of this ListImagesRequest.
        :type status: str
        """
        self._status = status

    @property
    def tag(self):
        """Gets the tag of this ListImagesRequest.

        :return: The tag of this ListImagesRequest.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this ListImagesRequest.

        :param tag: The tag of this ListImagesRequest.
        :type tag: str
        """
        self._tag = tag

    @property
    def virtual_env_type(self):
        """Gets the virtual_env_type of this ListImagesRequest.

        :return: The virtual_env_type of this ListImagesRequest.
        :rtype: str
        """
        return self._virtual_env_type

    @virtual_env_type.setter
    def virtual_env_type(self, virtual_env_type):
        """Sets the virtual_env_type of this ListImagesRequest.

        :param virtual_env_type: The virtual_env_type of this ListImagesRequest.
        :type virtual_env_type: str
        """
        self._virtual_env_type = virtual_env_type

    @property
    def visibility(self):
        """Gets the visibility of this ListImagesRequest.

        :return: The visibility of this ListImagesRequest.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this ListImagesRequest.

        :param visibility: The visibility of this ListImagesRequest.
        :type visibility: str
        """
        self._visibility = visibility

    @property
    def x_sdk_date(self):
        """Gets the x_sdk_date of this ListImagesRequest.

        :return: The x_sdk_date of this ListImagesRequest.
        :rtype: str
        """
        return self._x_sdk_date

    @x_sdk_date.setter
    def x_sdk_date(self, x_sdk_date):
        """Sets the x_sdk_date of this ListImagesRequest.

        :param x_sdk_date: The x_sdk_date of this ListImagesRequest.
        :type x_sdk_date: str
        """
        self._x_sdk_date = x_sdk_date

    @property
    def flavor_id(self):
        """Gets the flavor_id of this ListImagesRequest.

        :return: The flavor_id of this ListImagesRequest.
        :rtype: str
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id):
        """Sets the flavor_id of this ListImagesRequest.

        :param flavor_id: The flavor_id of this ListImagesRequest.
        :type flavor_id: str
        """
        self._flavor_id = flavor_id

    @property
    def created_at(self):
        """Gets the created_at of this ListImagesRequest.

        :return: The created_at of this ListImagesRequest.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ListImagesRequest.

        :param created_at: The created_at of this ListImagesRequest.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ListImagesRequest.

        :return: The updated_at of this ListImagesRequest.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ListImagesRequest.

        :param updated_at: The updated_at of this ListImagesRequest.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def architecture(self):
        """Gets the architecture of this ListImagesRequest.

        :return: The architecture of this ListImagesRequest.
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        """Sets the architecture of this ListImagesRequest.

        :param architecture: The architecture of this ListImagesRequest.
        :type architecture: str
        """
        self._architecture = architecture

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
        if not isinstance(other, ListImagesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
