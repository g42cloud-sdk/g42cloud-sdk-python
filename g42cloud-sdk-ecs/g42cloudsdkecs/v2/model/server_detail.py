# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'updated': 'str',
        'auto_terminate_time': 'str',
        'host_id': 'str',
        'os_ext_srv_att_rhost': 'str',
        'addresses': 'dict(str, list[ServerAddress])',
        'key_name': 'str',
        'image': 'ServerImage',
        'os_ext_st_stask_state': 'str',
        'os_ext_st_svm_state': 'str',
        'os_ext_srv_att_rinstance_name': 'str',
        'os_ext_srv_att_rhypervisor_hostname': 'str',
        'flavor': 'ServerFlavor',
        'id': 'str',
        'security_groups': 'list[ServerSecurityGroup]',
        'os_ext_a_zavailability_zone': 'str',
        'user_id': 'str',
        'name': 'str',
        'created': 'str',
        'tenant_id': 'str',
        'os_dc_fdisk_config': 'str',
        'access_i_pv4': 'str',
        'access_i_pv6': 'str',
        'fault': 'ServerFault',
        'progress': 'int',
        'os_ext_st_spower_state': 'int',
        'config_drive': 'str',
        'metadata': 'dict(str, str)',
        'os_srv_us_glaunched_at': 'str',
        'os_srv_us_gterminated_at': 'str',
        'os_extended_volumesvolumes_attached': 'list[ServerExtendVolumeAttachment]',
        'description': 'str',
        'host_status': 'str',
        'os_ext_srv_att_rhostname': 'str',
        'os_ext_srv_att_rreservation_id': 'str',
        'os_ext_srv_att_rlaunch_index': 'int',
        'os_ext_srv_att_rkernel_id': 'str',
        'os_ext_srv_att_rramdisk_id': 'str',
        'os_ext_srv_att_rroot_device_name': 'str',
        'os_ext_srv_att_ruser_data': 'str',
        'locked': 'bool',
        'tags': 'list[str]',
        'osscheduler_hints': 'ServerSchedulerHints',
        'enterprise_project_id': 'str',
        'sys_tags': 'list[ServerSystemTag]',
        'cpu_options': 'CpuOptions',
        'hypervisor': 'Hypervisor'
    }

    attribute_map = {
        'status': 'status',
        'updated': 'updated',
        'auto_terminate_time': 'auto_terminate_time',
        'host_id': 'hostId',
        'os_ext_srv_att_rhost': 'OS-EXT-SRV-ATTR:host',
        'addresses': 'addresses',
        'key_name': 'key_name',
        'image': 'image',
        'os_ext_st_stask_state': 'OS-EXT-STS:task_state',
        'os_ext_st_svm_state': 'OS-EXT-STS:vm_state',
        'os_ext_srv_att_rinstance_name': 'OS-EXT-SRV-ATTR:instance_name',
        'os_ext_srv_att_rhypervisor_hostname': 'OS-EXT-SRV-ATTR:hypervisor_hostname',
        'flavor': 'flavor',
        'id': 'id',
        'security_groups': 'security_groups',
        'os_ext_a_zavailability_zone': 'OS-EXT-AZ:availability_zone',
        'user_id': 'user_id',
        'name': 'name',
        'created': 'created',
        'tenant_id': 'tenant_id',
        'os_dc_fdisk_config': 'OS-DCF:diskConfig',
        'access_i_pv4': 'accessIPv4',
        'access_i_pv6': 'accessIPv6',
        'fault': 'fault',
        'progress': 'progress',
        'os_ext_st_spower_state': 'OS-EXT-STS:power_state',
        'config_drive': 'config_drive',
        'metadata': 'metadata',
        'os_srv_us_glaunched_at': 'OS-SRV-USG:launched_at',
        'os_srv_us_gterminated_at': 'OS-SRV-USG:terminated_at',
        'os_extended_volumesvolumes_attached': 'os-extended-volumes:volumes_attached',
        'description': 'description',
        'host_status': 'host_status',
        'os_ext_srv_att_rhostname': 'OS-EXT-SRV-ATTR:hostname',
        'os_ext_srv_att_rreservation_id': 'OS-EXT-SRV-ATTR:reservation_id',
        'os_ext_srv_att_rlaunch_index': 'OS-EXT-SRV-ATTR:launch_index',
        'os_ext_srv_att_rkernel_id': 'OS-EXT-SRV-ATTR:kernel_id',
        'os_ext_srv_att_rramdisk_id': 'OS-EXT-SRV-ATTR:ramdisk_id',
        'os_ext_srv_att_rroot_device_name': 'OS-EXT-SRV-ATTR:root_device_name',
        'os_ext_srv_att_ruser_data': 'OS-EXT-SRV-ATTR:user_data',
        'locked': 'locked',
        'tags': 'tags',
        'osscheduler_hints': 'os:scheduler_hints',
        'enterprise_project_id': 'enterprise_project_id',
        'sys_tags': 'sys_tags',
        'cpu_options': 'cpu_options',
        'hypervisor': 'hypervisor'
    }

    def __init__(self, status=None, updated=None, auto_terminate_time=None, host_id=None, os_ext_srv_att_rhost=None, addresses=None, key_name=None, image=None, os_ext_st_stask_state=None, os_ext_st_svm_state=None, os_ext_srv_att_rinstance_name=None, os_ext_srv_att_rhypervisor_hostname=None, flavor=None, id=None, security_groups=None, os_ext_a_zavailability_zone=None, user_id=None, name=None, created=None, tenant_id=None, os_dc_fdisk_config=None, access_i_pv4=None, access_i_pv6=None, fault=None, progress=None, os_ext_st_spower_state=None, config_drive=None, metadata=None, os_srv_us_glaunched_at=None, os_srv_us_gterminated_at=None, os_extended_volumesvolumes_attached=None, description=None, host_status=None, os_ext_srv_att_rhostname=None, os_ext_srv_att_rreservation_id=None, os_ext_srv_att_rlaunch_index=None, os_ext_srv_att_rkernel_id=None, os_ext_srv_att_rramdisk_id=None, os_ext_srv_att_rroot_device_name=None, os_ext_srv_att_ruser_data=None, locked=None, tags=None, osscheduler_hints=None, enterprise_project_id=None, sys_tags=None, cpu_options=None, hypervisor=None):
        """ServerDetail

        The model defined in g42cloud sdk

        :param status: The param of the ServerDetail
        :type status: str
        :param updated: The param of the ServerDetail
        :type updated: str
        :param auto_terminate_time: The param of the ServerDetail
        :type auto_terminate_time: str
        :param host_id: The param of the ServerDetail
        :type host_id: str
        :param os_ext_srv_att_rhost: The param of the ServerDetail
        :type os_ext_srv_att_rhost: str
        :param addresses: The param of the ServerDetail
        :type addresses: dict(str, list[ServerAddress])
        :param key_name: The param of the ServerDetail
        :type key_name: str
        :param image: The param of the ServerDetail
        :type image: :class:`g42cloudsdkecs.v2.ServerImage`
        :param os_ext_st_stask_state: The param of the ServerDetail
        :type os_ext_st_stask_state: str
        :param os_ext_st_svm_state: The param of the ServerDetail
        :type os_ext_st_svm_state: str
        :param os_ext_srv_att_rinstance_name: The param of the ServerDetail
        :type os_ext_srv_att_rinstance_name: str
        :param os_ext_srv_att_rhypervisor_hostname: The param of the ServerDetail
        :type os_ext_srv_att_rhypervisor_hostname: str
        :param flavor: The param of the ServerDetail
        :type flavor: :class:`g42cloudsdkecs.v2.ServerFlavor`
        :param id: The param of the ServerDetail
        :type id: str
        :param security_groups: The param of the ServerDetail
        :type security_groups: list[:class:`g42cloudsdkecs.v2.ServerSecurityGroup`]
        :param os_ext_a_zavailability_zone: The param of the ServerDetail
        :type os_ext_a_zavailability_zone: str
        :param user_id: The param of the ServerDetail
        :type user_id: str
        :param name: The param of the ServerDetail
        :type name: str
        :param created: The param of the ServerDetail
        :type created: str
        :param tenant_id: The param of the ServerDetail
        :type tenant_id: str
        :param os_dc_fdisk_config: The param of the ServerDetail
        :type os_dc_fdisk_config: str
        :param access_i_pv4: The param of the ServerDetail
        :type access_i_pv4: str
        :param access_i_pv6: The param of the ServerDetail
        :type access_i_pv6: str
        :param fault: The param of the ServerDetail
        :type fault: :class:`g42cloudsdkecs.v2.ServerFault`
        :param progress: The param of the ServerDetail
        :type progress: int
        :param os_ext_st_spower_state: The param of the ServerDetail
        :type os_ext_st_spower_state: int
        :param config_drive: The param of the ServerDetail
        :type config_drive: str
        :param metadata: The param of the ServerDetail
        :type metadata: dict(str, str)
        :param os_srv_us_glaunched_at: The param of the ServerDetail
        :type os_srv_us_glaunched_at: str
        :param os_srv_us_gterminated_at: The param of the ServerDetail
        :type os_srv_us_gterminated_at: str
        :param os_extended_volumesvolumes_attached: The param of the ServerDetail
        :type os_extended_volumesvolumes_attached: list[:class:`g42cloudsdkecs.v2.ServerExtendVolumeAttachment`]
        :param description: The param of the ServerDetail
        :type description: str
        :param host_status: The param of the ServerDetail
        :type host_status: str
        :param os_ext_srv_att_rhostname: The param of the ServerDetail
        :type os_ext_srv_att_rhostname: str
        :param os_ext_srv_att_rreservation_id: The param of the ServerDetail
        :type os_ext_srv_att_rreservation_id: str
        :param os_ext_srv_att_rlaunch_index: The param of the ServerDetail
        :type os_ext_srv_att_rlaunch_index: int
        :param os_ext_srv_att_rkernel_id: The param of the ServerDetail
        :type os_ext_srv_att_rkernel_id: str
        :param os_ext_srv_att_rramdisk_id: The param of the ServerDetail
        :type os_ext_srv_att_rramdisk_id: str
        :param os_ext_srv_att_rroot_device_name: The param of the ServerDetail
        :type os_ext_srv_att_rroot_device_name: str
        :param os_ext_srv_att_ruser_data: The param of the ServerDetail
        :type os_ext_srv_att_ruser_data: str
        :param locked: The param of the ServerDetail
        :type locked: bool
        :param tags: The param of the ServerDetail
        :type tags: list[str]
        :param osscheduler_hints: The param of the ServerDetail
        :type osscheduler_hints: :class:`g42cloudsdkecs.v2.ServerSchedulerHints`
        :param enterprise_project_id: The param of the ServerDetail
        :type enterprise_project_id: str
        :param sys_tags: The param of the ServerDetail
        :type sys_tags: list[:class:`g42cloudsdkecs.v2.ServerSystemTag`]
        :param cpu_options: The param of the ServerDetail
        :type cpu_options: :class:`g42cloudsdkecs.v2.CpuOptions`
        :param hypervisor: The param of the ServerDetail
        :type hypervisor: :class:`g42cloudsdkecs.v2.Hypervisor`
        """
        
        

        self._status = None
        self._updated = None
        self._auto_terminate_time = None
        self._host_id = None
        self._os_ext_srv_att_rhost = None
        self._addresses = None
        self._key_name = None
        self._image = None
        self._os_ext_st_stask_state = None
        self._os_ext_st_svm_state = None
        self._os_ext_srv_att_rinstance_name = None
        self._os_ext_srv_att_rhypervisor_hostname = None
        self._flavor = None
        self._id = None
        self._security_groups = None
        self._os_ext_a_zavailability_zone = None
        self._user_id = None
        self._name = None
        self._created = None
        self._tenant_id = None
        self._os_dc_fdisk_config = None
        self._access_i_pv4 = None
        self._access_i_pv6 = None
        self._fault = None
        self._progress = None
        self._os_ext_st_spower_state = None
        self._config_drive = None
        self._metadata = None
        self._os_srv_us_glaunched_at = None
        self._os_srv_us_gterminated_at = None
        self._os_extended_volumesvolumes_attached = None
        self._description = None
        self._host_status = None
        self._os_ext_srv_att_rhostname = None
        self._os_ext_srv_att_rreservation_id = None
        self._os_ext_srv_att_rlaunch_index = None
        self._os_ext_srv_att_rkernel_id = None
        self._os_ext_srv_att_rramdisk_id = None
        self._os_ext_srv_att_rroot_device_name = None
        self._os_ext_srv_att_ruser_data = None
        self._locked = None
        self._tags = None
        self._osscheduler_hints = None
        self._enterprise_project_id = None
        self._sys_tags = None
        self._cpu_options = None
        self._hypervisor = None
        self.discriminator = None

        self.status = status
        self.updated = updated
        self.auto_terminate_time = auto_terminate_time
        self.host_id = host_id
        self.os_ext_srv_att_rhost = os_ext_srv_att_rhost
        self.addresses = addresses
        self.key_name = key_name
        self.image = image
        self.os_ext_st_stask_state = os_ext_st_stask_state
        self.os_ext_st_svm_state = os_ext_st_svm_state
        self.os_ext_srv_att_rinstance_name = os_ext_srv_att_rinstance_name
        self.os_ext_srv_att_rhypervisor_hostname = os_ext_srv_att_rhypervisor_hostname
        self.flavor = flavor
        self.id = id
        self.security_groups = security_groups
        self.os_ext_a_zavailability_zone = os_ext_a_zavailability_zone
        self.user_id = user_id
        self.name = name
        self.created = created
        self.tenant_id = tenant_id
        if os_dc_fdisk_config is not None:
            self.os_dc_fdisk_config = os_dc_fdisk_config
        self.access_i_pv4 = access_i_pv4
        self.access_i_pv6 = access_i_pv6
        if fault is not None:
            self.fault = fault
        if progress is not None:
            self.progress = progress
        self.os_ext_st_spower_state = os_ext_st_spower_state
        self.config_drive = config_drive
        self.metadata = metadata
        self.os_srv_us_glaunched_at = os_srv_us_glaunched_at
        self.os_srv_us_gterminated_at = os_srv_us_gterminated_at
        self.os_extended_volumesvolumes_attached = os_extended_volumesvolumes_attached
        if description is not None:
            self.description = description
        self.host_status = host_status
        self.os_ext_srv_att_rhostname = os_ext_srv_att_rhostname
        if os_ext_srv_att_rreservation_id is not None:
            self.os_ext_srv_att_rreservation_id = os_ext_srv_att_rreservation_id
        self.os_ext_srv_att_rlaunch_index = os_ext_srv_att_rlaunch_index
        self.os_ext_srv_att_rkernel_id = os_ext_srv_att_rkernel_id
        self.os_ext_srv_att_rramdisk_id = os_ext_srv_att_rramdisk_id
        self.os_ext_srv_att_rroot_device_name = os_ext_srv_att_rroot_device_name
        if os_ext_srv_att_ruser_data is not None:
            self.os_ext_srv_att_ruser_data = os_ext_srv_att_ruser_data
        self.locked = locked
        if tags is not None:
            self.tags = tags
        if osscheduler_hints is not None:
            self.osscheduler_hints = osscheduler_hints
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if sys_tags is not None:
            self.sys_tags = sys_tags
        if cpu_options is not None:
            self.cpu_options = cpu_options
        if hypervisor is not None:
            self.hypervisor = hypervisor

    @property
    def status(self):
        """Gets the status of this ServerDetail.

        :return: The status of this ServerDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ServerDetail.

        :param status: The status of this ServerDetail.
        :type status: str
        """
        self._status = status

    @property
    def updated(self):
        """Gets the updated of this ServerDetail.

        :return: The updated of this ServerDetail.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this ServerDetail.

        :param updated: The updated of this ServerDetail.
        :type updated: str
        """
        self._updated = updated

    @property
    def auto_terminate_time(self):
        """Gets the auto_terminate_time of this ServerDetail.

        :return: The auto_terminate_time of this ServerDetail.
        :rtype: str
        """
        return self._auto_terminate_time

    @auto_terminate_time.setter
    def auto_terminate_time(self, auto_terminate_time):
        """Sets the auto_terminate_time of this ServerDetail.

        :param auto_terminate_time: The auto_terminate_time of this ServerDetail.
        :type auto_terminate_time: str
        """
        self._auto_terminate_time = auto_terminate_time

    @property
    def host_id(self):
        """Gets the host_id of this ServerDetail.

        :return: The host_id of this ServerDetail.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this ServerDetail.

        :param host_id: The host_id of this ServerDetail.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def os_ext_srv_att_rhost(self):
        """Gets the os_ext_srv_att_rhost of this ServerDetail.

        :return: The os_ext_srv_att_rhost of this ServerDetail.
        :rtype: str
        """
        return self._os_ext_srv_att_rhost

    @os_ext_srv_att_rhost.setter
    def os_ext_srv_att_rhost(self, os_ext_srv_att_rhost):
        """Sets the os_ext_srv_att_rhost of this ServerDetail.

        :param os_ext_srv_att_rhost: The os_ext_srv_att_rhost of this ServerDetail.
        :type os_ext_srv_att_rhost: str
        """
        self._os_ext_srv_att_rhost = os_ext_srv_att_rhost

    @property
    def addresses(self):
        """Gets the addresses of this ServerDetail.

        :return: The addresses of this ServerDetail.
        :rtype: dict(str, list[ServerAddress])
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this ServerDetail.

        :param addresses: The addresses of this ServerDetail.
        :type addresses: dict(str, list[ServerAddress])
        """
        self._addresses = addresses

    @property
    def key_name(self):
        """Gets the key_name of this ServerDetail.

        :return: The key_name of this ServerDetail.
        :rtype: str
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        """Sets the key_name of this ServerDetail.

        :param key_name: The key_name of this ServerDetail.
        :type key_name: str
        """
        self._key_name = key_name

    @property
    def image(self):
        """Gets the image of this ServerDetail.

        :return: The image of this ServerDetail.
        :rtype: :class:`g42cloudsdkecs.v2.ServerImage`
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this ServerDetail.

        :param image: The image of this ServerDetail.
        :type image: :class:`g42cloudsdkecs.v2.ServerImage`
        """
        self._image = image

    @property
    def os_ext_st_stask_state(self):
        """Gets the os_ext_st_stask_state of this ServerDetail.

        :return: The os_ext_st_stask_state of this ServerDetail.
        :rtype: str
        """
        return self._os_ext_st_stask_state

    @os_ext_st_stask_state.setter
    def os_ext_st_stask_state(self, os_ext_st_stask_state):
        """Sets the os_ext_st_stask_state of this ServerDetail.

        :param os_ext_st_stask_state: The os_ext_st_stask_state of this ServerDetail.
        :type os_ext_st_stask_state: str
        """
        self._os_ext_st_stask_state = os_ext_st_stask_state

    @property
    def os_ext_st_svm_state(self):
        """Gets the os_ext_st_svm_state of this ServerDetail.

        :return: The os_ext_st_svm_state of this ServerDetail.
        :rtype: str
        """
        return self._os_ext_st_svm_state

    @os_ext_st_svm_state.setter
    def os_ext_st_svm_state(self, os_ext_st_svm_state):
        """Sets the os_ext_st_svm_state of this ServerDetail.

        :param os_ext_st_svm_state: The os_ext_st_svm_state of this ServerDetail.
        :type os_ext_st_svm_state: str
        """
        self._os_ext_st_svm_state = os_ext_st_svm_state

    @property
    def os_ext_srv_att_rinstance_name(self):
        """Gets the os_ext_srv_att_rinstance_name of this ServerDetail.

        :return: The os_ext_srv_att_rinstance_name of this ServerDetail.
        :rtype: str
        """
        return self._os_ext_srv_att_rinstance_name

    @os_ext_srv_att_rinstance_name.setter
    def os_ext_srv_att_rinstance_name(self, os_ext_srv_att_rinstance_name):
        """Sets the os_ext_srv_att_rinstance_name of this ServerDetail.

        :param os_ext_srv_att_rinstance_name: The os_ext_srv_att_rinstance_name of this ServerDetail.
        :type os_ext_srv_att_rinstance_name: str
        """
        self._os_ext_srv_att_rinstance_name = os_ext_srv_att_rinstance_name

    @property
    def os_ext_srv_att_rhypervisor_hostname(self):
        """Gets the os_ext_srv_att_rhypervisor_hostname of this ServerDetail.

        :return: The os_ext_srv_att_rhypervisor_hostname of this ServerDetail.
        :rtype: str
        """
        return self._os_ext_srv_att_rhypervisor_hostname

    @os_ext_srv_att_rhypervisor_hostname.setter
    def os_ext_srv_att_rhypervisor_hostname(self, os_ext_srv_att_rhypervisor_hostname):
        """Sets the os_ext_srv_att_rhypervisor_hostname of this ServerDetail.

        :param os_ext_srv_att_rhypervisor_hostname: The os_ext_srv_att_rhypervisor_hostname of this ServerDetail.
        :type os_ext_srv_att_rhypervisor_hostname: str
        """
        self._os_ext_srv_att_rhypervisor_hostname = os_ext_srv_att_rhypervisor_hostname

    @property
    def flavor(self):
        """Gets the flavor of this ServerDetail.

        :return: The flavor of this ServerDetail.
        :rtype: :class:`g42cloudsdkecs.v2.ServerFlavor`
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this ServerDetail.

        :param flavor: The flavor of this ServerDetail.
        :type flavor: :class:`g42cloudsdkecs.v2.ServerFlavor`
        """
        self._flavor = flavor

    @property
    def id(self):
        """Gets the id of this ServerDetail.

        :return: The id of this ServerDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ServerDetail.

        :param id: The id of this ServerDetail.
        :type id: str
        """
        self._id = id

    @property
    def security_groups(self):
        """Gets the security_groups of this ServerDetail.

        :return: The security_groups of this ServerDetail.
        :rtype: list[:class:`g42cloudsdkecs.v2.ServerSecurityGroup`]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this ServerDetail.

        :param security_groups: The security_groups of this ServerDetail.
        :type security_groups: list[:class:`g42cloudsdkecs.v2.ServerSecurityGroup`]
        """
        self._security_groups = security_groups

    @property
    def os_ext_a_zavailability_zone(self):
        """Gets the os_ext_a_zavailability_zone of this ServerDetail.

        :return: The os_ext_a_zavailability_zone of this ServerDetail.
        :rtype: str
        """
        return self._os_ext_a_zavailability_zone

    @os_ext_a_zavailability_zone.setter
    def os_ext_a_zavailability_zone(self, os_ext_a_zavailability_zone):
        """Sets the os_ext_a_zavailability_zone of this ServerDetail.

        :param os_ext_a_zavailability_zone: The os_ext_a_zavailability_zone of this ServerDetail.
        :type os_ext_a_zavailability_zone: str
        """
        self._os_ext_a_zavailability_zone = os_ext_a_zavailability_zone

    @property
    def user_id(self):
        """Gets the user_id of this ServerDetail.

        :return: The user_id of this ServerDetail.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ServerDetail.

        :param user_id: The user_id of this ServerDetail.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def name(self):
        """Gets the name of this ServerDetail.

        :return: The name of this ServerDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ServerDetail.

        :param name: The name of this ServerDetail.
        :type name: str
        """
        self._name = name

    @property
    def created(self):
        """Gets the created of this ServerDetail.

        :return: The created of this ServerDetail.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ServerDetail.

        :param created: The created of this ServerDetail.
        :type created: str
        """
        self._created = created

    @property
    def tenant_id(self):
        """Gets the tenant_id of this ServerDetail.

        :return: The tenant_id of this ServerDetail.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this ServerDetail.

        :param tenant_id: The tenant_id of this ServerDetail.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def os_dc_fdisk_config(self):
        """Gets the os_dc_fdisk_config of this ServerDetail.

        :return: The os_dc_fdisk_config of this ServerDetail.
        :rtype: str
        """
        return self._os_dc_fdisk_config

    @os_dc_fdisk_config.setter
    def os_dc_fdisk_config(self, os_dc_fdisk_config):
        """Sets the os_dc_fdisk_config of this ServerDetail.

        :param os_dc_fdisk_config: The os_dc_fdisk_config of this ServerDetail.
        :type os_dc_fdisk_config: str
        """
        self._os_dc_fdisk_config = os_dc_fdisk_config

    @property
    def access_i_pv4(self):
        """Gets the access_i_pv4 of this ServerDetail.

        :return: The access_i_pv4 of this ServerDetail.
        :rtype: str
        """
        return self._access_i_pv4

    @access_i_pv4.setter
    def access_i_pv4(self, access_i_pv4):
        """Sets the access_i_pv4 of this ServerDetail.

        :param access_i_pv4: The access_i_pv4 of this ServerDetail.
        :type access_i_pv4: str
        """
        self._access_i_pv4 = access_i_pv4

    @property
    def access_i_pv6(self):
        """Gets the access_i_pv6 of this ServerDetail.

        :return: The access_i_pv6 of this ServerDetail.
        :rtype: str
        """
        return self._access_i_pv6

    @access_i_pv6.setter
    def access_i_pv6(self, access_i_pv6):
        """Sets the access_i_pv6 of this ServerDetail.

        :param access_i_pv6: The access_i_pv6 of this ServerDetail.
        :type access_i_pv6: str
        """
        self._access_i_pv6 = access_i_pv6

    @property
    def fault(self):
        """Gets the fault of this ServerDetail.

        :return: The fault of this ServerDetail.
        :rtype: :class:`g42cloudsdkecs.v2.ServerFault`
        """
        return self._fault

    @fault.setter
    def fault(self, fault):
        """Sets the fault of this ServerDetail.

        :param fault: The fault of this ServerDetail.
        :type fault: :class:`g42cloudsdkecs.v2.ServerFault`
        """
        self._fault = fault

    @property
    def progress(self):
        """Gets the progress of this ServerDetail.

        :return: The progress of this ServerDetail.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this ServerDetail.

        :param progress: The progress of this ServerDetail.
        :type progress: int
        """
        self._progress = progress

    @property
    def os_ext_st_spower_state(self):
        """Gets the os_ext_st_spower_state of this ServerDetail.

        :return: The os_ext_st_spower_state of this ServerDetail.
        :rtype: int
        """
        return self._os_ext_st_spower_state

    @os_ext_st_spower_state.setter
    def os_ext_st_spower_state(self, os_ext_st_spower_state):
        """Sets the os_ext_st_spower_state of this ServerDetail.

        :param os_ext_st_spower_state: The os_ext_st_spower_state of this ServerDetail.
        :type os_ext_st_spower_state: int
        """
        self._os_ext_st_spower_state = os_ext_st_spower_state

    @property
    def config_drive(self):
        """Gets the config_drive of this ServerDetail.

        :return: The config_drive of this ServerDetail.
        :rtype: str
        """
        return self._config_drive

    @config_drive.setter
    def config_drive(self, config_drive):
        """Sets the config_drive of this ServerDetail.

        :param config_drive: The config_drive of this ServerDetail.
        :type config_drive: str
        """
        self._config_drive = config_drive

    @property
    def metadata(self):
        """Gets the metadata of this ServerDetail.

        :return: The metadata of this ServerDetail.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ServerDetail.

        :param metadata: The metadata of this ServerDetail.
        :type metadata: dict(str, str)
        """
        self._metadata = metadata

    @property
    def os_srv_us_glaunched_at(self):
        """Gets the os_srv_us_glaunched_at of this ServerDetail.

        :return: The os_srv_us_glaunched_at of this ServerDetail.
        :rtype: str
        """
        return self._os_srv_us_glaunched_at

    @os_srv_us_glaunched_at.setter
    def os_srv_us_glaunched_at(self, os_srv_us_glaunched_at):
        """Sets the os_srv_us_glaunched_at of this ServerDetail.

        :param os_srv_us_glaunched_at: The os_srv_us_glaunched_at of this ServerDetail.
        :type os_srv_us_glaunched_at: str
        """
        self._os_srv_us_glaunched_at = os_srv_us_glaunched_at

    @property
    def os_srv_us_gterminated_at(self):
        """Gets the os_srv_us_gterminated_at of this ServerDetail.

        :return: The os_srv_us_gterminated_at of this ServerDetail.
        :rtype: str
        """
        return self._os_srv_us_gterminated_at

    @os_srv_us_gterminated_at.setter
    def os_srv_us_gterminated_at(self, os_srv_us_gterminated_at):
        """Sets the os_srv_us_gterminated_at of this ServerDetail.

        :param os_srv_us_gterminated_at: The os_srv_us_gterminated_at of this ServerDetail.
        :type os_srv_us_gterminated_at: str
        """
        self._os_srv_us_gterminated_at = os_srv_us_gterminated_at

    @property
    def os_extended_volumesvolumes_attached(self):
        """Gets the os_extended_volumesvolumes_attached of this ServerDetail.

        :return: The os_extended_volumesvolumes_attached of this ServerDetail.
        :rtype: list[:class:`g42cloudsdkecs.v2.ServerExtendVolumeAttachment`]
        """
        return self._os_extended_volumesvolumes_attached

    @os_extended_volumesvolumes_attached.setter
    def os_extended_volumesvolumes_attached(self, os_extended_volumesvolumes_attached):
        """Sets the os_extended_volumesvolumes_attached of this ServerDetail.

        :param os_extended_volumesvolumes_attached: The os_extended_volumesvolumes_attached of this ServerDetail.
        :type os_extended_volumesvolumes_attached: list[:class:`g42cloudsdkecs.v2.ServerExtendVolumeAttachment`]
        """
        self._os_extended_volumesvolumes_attached = os_extended_volumesvolumes_attached

    @property
    def description(self):
        """Gets the description of this ServerDetail.

        :return: The description of this ServerDetail.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ServerDetail.

        :param description: The description of this ServerDetail.
        :type description: str
        """
        self._description = description

    @property
    def host_status(self):
        """Gets the host_status of this ServerDetail.

        :return: The host_status of this ServerDetail.
        :rtype: str
        """
        return self._host_status

    @host_status.setter
    def host_status(self, host_status):
        """Sets the host_status of this ServerDetail.

        :param host_status: The host_status of this ServerDetail.
        :type host_status: str
        """
        self._host_status = host_status

    @property
    def os_ext_srv_att_rhostname(self):
        """Gets the os_ext_srv_att_rhostname of this ServerDetail.

        :return: The os_ext_srv_att_rhostname of this ServerDetail.
        :rtype: str
        """
        return self._os_ext_srv_att_rhostname

    @os_ext_srv_att_rhostname.setter
    def os_ext_srv_att_rhostname(self, os_ext_srv_att_rhostname):
        """Sets the os_ext_srv_att_rhostname of this ServerDetail.

        :param os_ext_srv_att_rhostname: The os_ext_srv_att_rhostname of this ServerDetail.
        :type os_ext_srv_att_rhostname: str
        """
        self._os_ext_srv_att_rhostname = os_ext_srv_att_rhostname

    @property
    def os_ext_srv_att_rreservation_id(self):
        """Gets the os_ext_srv_att_rreservation_id of this ServerDetail.

        :return: The os_ext_srv_att_rreservation_id of this ServerDetail.
        :rtype: str
        """
        return self._os_ext_srv_att_rreservation_id

    @os_ext_srv_att_rreservation_id.setter
    def os_ext_srv_att_rreservation_id(self, os_ext_srv_att_rreservation_id):
        """Sets the os_ext_srv_att_rreservation_id of this ServerDetail.

        :param os_ext_srv_att_rreservation_id: The os_ext_srv_att_rreservation_id of this ServerDetail.
        :type os_ext_srv_att_rreservation_id: str
        """
        self._os_ext_srv_att_rreservation_id = os_ext_srv_att_rreservation_id

    @property
    def os_ext_srv_att_rlaunch_index(self):
        """Gets the os_ext_srv_att_rlaunch_index of this ServerDetail.

        :return: The os_ext_srv_att_rlaunch_index of this ServerDetail.
        :rtype: int
        """
        return self._os_ext_srv_att_rlaunch_index

    @os_ext_srv_att_rlaunch_index.setter
    def os_ext_srv_att_rlaunch_index(self, os_ext_srv_att_rlaunch_index):
        """Sets the os_ext_srv_att_rlaunch_index of this ServerDetail.

        :param os_ext_srv_att_rlaunch_index: The os_ext_srv_att_rlaunch_index of this ServerDetail.
        :type os_ext_srv_att_rlaunch_index: int
        """
        self._os_ext_srv_att_rlaunch_index = os_ext_srv_att_rlaunch_index

    @property
    def os_ext_srv_att_rkernel_id(self):
        """Gets the os_ext_srv_att_rkernel_id of this ServerDetail.

        :return: The os_ext_srv_att_rkernel_id of this ServerDetail.
        :rtype: str
        """
        return self._os_ext_srv_att_rkernel_id

    @os_ext_srv_att_rkernel_id.setter
    def os_ext_srv_att_rkernel_id(self, os_ext_srv_att_rkernel_id):
        """Sets the os_ext_srv_att_rkernel_id of this ServerDetail.

        :param os_ext_srv_att_rkernel_id: The os_ext_srv_att_rkernel_id of this ServerDetail.
        :type os_ext_srv_att_rkernel_id: str
        """
        self._os_ext_srv_att_rkernel_id = os_ext_srv_att_rkernel_id

    @property
    def os_ext_srv_att_rramdisk_id(self):
        """Gets the os_ext_srv_att_rramdisk_id of this ServerDetail.

        :return: The os_ext_srv_att_rramdisk_id of this ServerDetail.
        :rtype: str
        """
        return self._os_ext_srv_att_rramdisk_id

    @os_ext_srv_att_rramdisk_id.setter
    def os_ext_srv_att_rramdisk_id(self, os_ext_srv_att_rramdisk_id):
        """Sets the os_ext_srv_att_rramdisk_id of this ServerDetail.

        :param os_ext_srv_att_rramdisk_id: The os_ext_srv_att_rramdisk_id of this ServerDetail.
        :type os_ext_srv_att_rramdisk_id: str
        """
        self._os_ext_srv_att_rramdisk_id = os_ext_srv_att_rramdisk_id

    @property
    def os_ext_srv_att_rroot_device_name(self):
        """Gets the os_ext_srv_att_rroot_device_name of this ServerDetail.

        :return: The os_ext_srv_att_rroot_device_name of this ServerDetail.
        :rtype: str
        """
        return self._os_ext_srv_att_rroot_device_name

    @os_ext_srv_att_rroot_device_name.setter
    def os_ext_srv_att_rroot_device_name(self, os_ext_srv_att_rroot_device_name):
        """Sets the os_ext_srv_att_rroot_device_name of this ServerDetail.

        :param os_ext_srv_att_rroot_device_name: The os_ext_srv_att_rroot_device_name of this ServerDetail.
        :type os_ext_srv_att_rroot_device_name: str
        """
        self._os_ext_srv_att_rroot_device_name = os_ext_srv_att_rroot_device_name

    @property
    def os_ext_srv_att_ruser_data(self):
        """Gets the os_ext_srv_att_ruser_data of this ServerDetail.

        :return: The os_ext_srv_att_ruser_data of this ServerDetail.
        :rtype: str
        """
        return self._os_ext_srv_att_ruser_data

    @os_ext_srv_att_ruser_data.setter
    def os_ext_srv_att_ruser_data(self, os_ext_srv_att_ruser_data):
        """Sets the os_ext_srv_att_ruser_data of this ServerDetail.

        :param os_ext_srv_att_ruser_data: The os_ext_srv_att_ruser_data of this ServerDetail.
        :type os_ext_srv_att_ruser_data: str
        """
        self._os_ext_srv_att_ruser_data = os_ext_srv_att_ruser_data

    @property
    def locked(self):
        """Gets the locked of this ServerDetail.

        :return: The locked of this ServerDetail.
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this ServerDetail.

        :param locked: The locked of this ServerDetail.
        :type locked: bool
        """
        self._locked = locked

    @property
    def tags(self):
        """Gets the tags of this ServerDetail.

        :return: The tags of this ServerDetail.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ServerDetail.

        :param tags: The tags of this ServerDetail.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def osscheduler_hints(self):
        """Gets the osscheduler_hints of this ServerDetail.

        :return: The osscheduler_hints of this ServerDetail.
        :rtype: :class:`g42cloudsdkecs.v2.ServerSchedulerHints`
        """
        return self._osscheduler_hints

    @osscheduler_hints.setter
    def osscheduler_hints(self, osscheduler_hints):
        """Sets the osscheduler_hints of this ServerDetail.

        :param osscheduler_hints: The osscheduler_hints of this ServerDetail.
        :type osscheduler_hints: :class:`g42cloudsdkecs.v2.ServerSchedulerHints`
        """
        self._osscheduler_hints = osscheduler_hints

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ServerDetail.

        :return: The enterprise_project_id of this ServerDetail.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ServerDetail.

        :param enterprise_project_id: The enterprise_project_id of this ServerDetail.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def sys_tags(self):
        """Gets the sys_tags of this ServerDetail.

        :return: The sys_tags of this ServerDetail.
        :rtype: list[:class:`g42cloudsdkecs.v2.ServerSystemTag`]
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        """Sets the sys_tags of this ServerDetail.

        :param sys_tags: The sys_tags of this ServerDetail.
        :type sys_tags: list[:class:`g42cloudsdkecs.v2.ServerSystemTag`]
        """
        self._sys_tags = sys_tags

    @property
    def cpu_options(self):
        """Gets the cpu_options of this ServerDetail.

        :return: The cpu_options of this ServerDetail.
        :rtype: :class:`g42cloudsdkecs.v2.CpuOptions`
        """
        return self._cpu_options

    @cpu_options.setter
    def cpu_options(self, cpu_options):
        """Sets the cpu_options of this ServerDetail.

        :param cpu_options: The cpu_options of this ServerDetail.
        :type cpu_options: :class:`g42cloudsdkecs.v2.CpuOptions`
        """
        self._cpu_options = cpu_options

    @property
    def hypervisor(self):
        """Gets the hypervisor of this ServerDetail.

        :return: The hypervisor of this ServerDetail.
        :rtype: :class:`g42cloudsdkecs.v2.Hypervisor`
        """
        return self._hypervisor

    @hypervisor.setter
    def hypervisor(self, hypervisor):
        """Sets the hypervisor of this ServerDetail.

        :param hypervisor: The hypervisor of this ServerDetail.
        :type hypervisor: :class:`g42cloudsdkecs.v2.Hypervisor`
        """
        self._hypervisor = hypervisor

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
        if not isinstance(other, ServerDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
