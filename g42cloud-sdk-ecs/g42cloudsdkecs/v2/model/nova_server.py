# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NovaServer:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'id': 'str',
        'status': 'str',
        'created': 'str',
        'updated': 'str',
        'flavor': 'NovaServerFlavor',
        'image': 'NovaServerImage',
        'tenant_id': 'str',
        'key_name': 'str',
        'user_id': 'str',
        'metadata': 'dict(str, str)',
        'host_id': 'str',
        'addresses': 'dict(str, list[NovaNetwork])',
        'security_groups': 'list[NovaServerSecurityGroup]',
        'links': 'list[NovaLink]',
        'os_dc_fdisk_config': 'str',
        'os_ext_a_zavailability_zone': 'str',
        'os_ext_srv_att_rhost': 'str',
        'os_ext_srv_att_rhypervisor_hostname': 'str',
        'os_ext_srv_att_rinstance_name': 'str',
        'os_ext_st_spower_state': 'int',
        'os_ext_st_stask_state': 'str',
        'os_ext_st_svm_state': 'str',
        'os_srv_us_glaunched_at': 'str',
        'os_srv_us_gterminated_at': 'str',
        'os_extended_volumesvolumes_attached': 'list[NovaServerVolume]',
        'fault': 'NovaServerFault',
        'description': 'str',
        'host_status': 'str',
        'os_ext_srv_att_rhostname': 'str',
        'os_ext_srv_att_rreservation_id': 'str',
        'os_ext_srv_att_rlaunch_index': 'int',
        'os_ext_srv_att_rkernel_id': 'str',
        'os_ext_srv_att_rramdisk_id': 'str',
        'os_ext_srv_att_rroot_device_name': 'str',
        'os_ext_srv_att_ruser_data': 'str',
        'tags': 'list[str]',
        'locked': 'bool',
        'access_i_pv4': 'str',
        'access_i_pv6': 'str',
        'config_drive': 'str',
        'progress': 'int',
        'osscheduler_hints': 'NovaServerSchedulerHints'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'status': 'status',
        'created': 'created',
        'updated': 'updated',
        'flavor': 'flavor',
        'image': 'image',
        'tenant_id': 'tenant_id',
        'key_name': 'key_name',
        'user_id': 'user_id',
        'metadata': 'metadata',
        'host_id': 'hostId',
        'addresses': 'addresses',
        'security_groups': 'security_groups',
        'links': 'links',
        'os_dc_fdisk_config': 'OS-DCF:diskConfig',
        'os_ext_a_zavailability_zone': 'OS-EXT-AZ:availability_zone',
        'os_ext_srv_att_rhost': 'OS-EXT-SRV-ATTR:host',
        'os_ext_srv_att_rhypervisor_hostname': 'OS-EXT-SRV-ATTR:hypervisor_hostname',
        'os_ext_srv_att_rinstance_name': 'OS-EXT-SRV-ATTR:instance_name',
        'os_ext_st_spower_state': 'OS-EXT-STS:power_state',
        'os_ext_st_stask_state': 'OS-EXT-STS:task_state',
        'os_ext_st_svm_state': 'OS-EXT-STS:vm_state',
        'os_srv_us_glaunched_at': 'OS-SRV-USG:launched_at',
        'os_srv_us_gterminated_at': 'OS-SRV-USG:terminated_at',
        'os_extended_volumesvolumes_attached': 'os-extended-volumes:volumes_attached',
        'fault': 'fault',
        'description': 'description',
        'host_status': 'host_status',
        'os_ext_srv_att_rhostname': 'OS-EXT-SRV-ATTR:hostname',
        'os_ext_srv_att_rreservation_id': 'OS-EXT-SRV-ATTR:reservation_id',
        'os_ext_srv_att_rlaunch_index': 'OS-EXT-SRV-ATTR:launch_index',
        'os_ext_srv_att_rkernel_id': 'OS-EXT-SRV-ATTR:kernel_id',
        'os_ext_srv_att_rramdisk_id': 'OS-EXT-SRV-ATTR:ramdisk_id',
        'os_ext_srv_att_rroot_device_name': 'OS-EXT-SRV-ATTR:root_device_name',
        'os_ext_srv_att_ruser_data': 'OS-EXT-SRV-ATTR:user_data',
        'tags': 'tags',
        'locked': 'locked',
        'access_i_pv4': 'accessIPv4',
        'access_i_pv6': 'accessIPv6',
        'config_drive': 'config_drive',
        'progress': 'progress',
        'osscheduler_hints': 'os:scheduler_hints'
    }

    def __init__(self, name=None, id=None, status=None, created=None, updated=None, flavor=None, image=None, tenant_id=None, key_name=None, user_id=None, metadata=None, host_id=None, addresses=None, security_groups=None, links=None, os_dc_fdisk_config=None, os_ext_a_zavailability_zone=None, os_ext_srv_att_rhost=None, os_ext_srv_att_rhypervisor_hostname=None, os_ext_srv_att_rinstance_name=None, os_ext_st_spower_state=None, os_ext_st_stask_state=None, os_ext_st_svm_state=None, os_srv_us_glaunched_at=None, os_srv_us_gterminated_at=None, os_extended_volumesvolumes_attached=None, fault=None, description=None, host_status=None, os_ext_srv_att_rhostname=None, os_ext_srv_att_rreservation_id=None, os_ext_srv_att_rlaunch_index=None, os_ext_srv_att_rkernel_id=None, os_ext_srv_att_rramdisk_id=None, os_ext_srv_att_rroot_device_name=None, os_ext_srv_att_ruser_data=None, tags=None, locked=None, access_i_pv4=None, access_i_pv6=None, config_drive=None, progress=None, osscheduler_hints=None):
        """NovaServer

        The model defined in g42cloud sdk

        :param name: The param of the NovaServer
        :type name: str
        :param id: The param of the NovaServer
        :type id: str
        :param status: The param of the NovaServer
        :type status: str
        :param created: The param of the NovaServer
        :type created: str
        :param updated: The param of the NovaServer
        :type updated: str
        :param flavor: The param of the NovaServer
        :type flavor: :class:`g42cloudsdkecs.v2.NovaServerFlavor`
        :param image: The param of the NovaServer
        :type image: :class:`g42cloudsdkecs.v2.NovaServerImage`
        :param tenant_id: The param of the NovaServer
        :type tenant_id: str
        :param key_name: The param of the NovaServer
        :type key_name: str
        :param user_id: The param of the NovaServer
        :type user_id: str
        :param metadata: The param of the NovaServer
        :type metadata: dict(str, str)
        :param host_id: The param of the NovaServer
        :type host_id: str
        :param addresses: The param of the NovaServer
        :type addresses: dict(str, list[NovaNetwork])
        :param security_groups: The param of the NovaServer
        :type security_groups: list[:class:`g42cloudsdkecs.v2.NovaServerSecurityGroup`]
        :param links: The param of the NovaServer
        :type links: list[:class:`g42cloudsdkecs.v2.NovaLink`]
        :param os_dc_fdisk_config: The param of the NovaServer
        :type os_dc_fdisk_config: str
        :param os_ext_a_zavailability_zone: The param of the NovaServer
        :type os_ext_a_zavailability_zone: str
        :param os_ext_srv_att_rhost: The param of the NovaServer
        :type os_ext_srv_att_rhost: str
        :param os_ext_srv_att_rhypervisor_hostname: The param of the NovaServer
        :type os_ext_srv_att_rhypervisor_hostname: str
        :param os_ext_srv_att_rinstance_name: The param of the NovaServer
        :type os_ext_srv_att_rinstance_name: str
        :param os_ext_st_spower_state: The param of the NovaServer
        :type os_ext_st_spower_state: int
        :param os_ext_st_stask_state: The param of the NovaServer
        :type os_ext_st_stask_state: str
        :param os_ext_st_svm_state: The param of the NovaServer
        :type os_ext_st_svm_state: str
        :param os_srv_us_glaunched_at: The param of the NovaServer
        :type os_srv_us_glaunched_at: str
        :param os_srv_us_gterminated_at: The param of the NovaServer
        :type os_srv_us_gterminated_at: str
        :param os_extended_volumesvolumes_attached: The param of the NovaServer
        :type os_extended_volumesvolumes_attached: list[:class:`g42cloudsdkecs.v2.NovaServerVolume`]
        :param fault: The param of the NovaServer
        :type fault: :class:`g42cloudsdkecs.v2.NovaServerFault`
        :param description: The param of the NovaServer
        :type description: str
        :param host_status: The param of the NovaServer
        :type host_status: str
        :param os_ext_srv_att_rhostname: The param of the NovaServer
        :type os_ext_srv_att_rhostname: str
        :param os_ext_srv_att_rreservation_id: The param of the NovaServer
        :type os_ext_srv_att_rreservation_id: str
        :param os_ext_srv_att_rlaunch_index: The param of the NovaServer
        :type os_ext_srv_att_rlaunch_index: int
        :param os_ext_srv_att_rkernel_id: The param of the NovaServer
        :type os_ext_srv_att_rkernel_id: str
        :param os_ext_srv_att_rramdisk_id: The param of the NovaServer
        :type os_ext_srv_att_rramdisk_id: str
        :param os_ext_srv_att_rroot_device_name: The param of the NovaServer
        :type os_ext_srv_att_rroot_device_name: str
        :param os_ext_srv_att_ruser_data: The param of the NovaServer
        :type os_ext_srv_att_ruser_data: str
        :param tags: The param of the NovaServer
        :type tags: list[str]
        :param locked: The param of the NovaServer
        :type locked: bool
        :param access_i_pv4: The param of the NovaServer
        :type access_i_pv4: str
        :param access_i_pv6: The param of the NovaServer
        :type access_i_pv6: str
        :param config_drive: The param of the NovaServer
        :type config_drive: str
        :param progress: The param of the NovaServer
        :type progress: int
        :param osscheduler_hints: The param of the NovaServer
        :type osscheduler_hints: :class:`g42cloudsdkecs.v2.NovaServerSchedulerHints`
        """
        
        

        self._name = None
        self._id = None
        self._status = None
        self._created = None
        self._updated = None
        self._flavor = None
        self._image = None
        self._tenant_id = None
        self._key_name = None
        self._user_id = None
        self._metadata = None
        self._host_id = None
        self._addresses = None
        self._security_groups = None
        self._links = None
        self._os_dc_fdisk_config = None
        self._os_ext_a_zavailability_zone = None
        self._os_ext_srv_att_rhost = None
        self._os_ext_srv_att_rhypervisor_hostname = None
        self._os_ext_srv_att_rinstance_name = None
        self._os_ext_st_spower_state = None
        self._os_ext_st_stask_state = None
        self._os_ext_st_svm_state = None
        self._os_srv_us_glaunched_at = None
        self._os_srv_us_gterminated_at = None
        self._os_extended_volumesvolumes_attached = None
        self._fault = None
        self._description = None
        self._host_status = None
        self._os_ext_srv_att_rhostname = None
        self._os_ext_srv_att_rreservation_id = None
        self._os_ext_srv_att_rlaunch_index = None
        self._os_ext_srv_att_rkernel_id = None
        self._os_ext_srv_att_rramdisk_id = None
        self._os_ext_srv_att_rroot_device_name = None
        self._os_ext_srv_att_ruser_data = None
        self._tags = None
        self._locked = None
        self._access_i_pv4 = None
        self._access_i_pv6 = None
        self._config_drive = None
        self._progress = None
        self._osscheduler_hints = None
        self.discriminator = None

        self.name = name
        self.id = id
        self.status = status
        self.created = created
        self.updated = updated
        self.flavor = flavor
        self.image = image
        self.tenant_id = tenant_id
        self.key_name = key_name
        self.user_id = user_id
        self.metadata = metadata
        self.host_id = host_id
        self.addresses = addresses
        self.security_groups = security_groups
        self.links = links
        self.os_dc_fdisk_config = os_dc_fdisk_config
        self.os_ext_a_zavailability_zone = os_ext_a_zavailability_zone
        self.os_ext_srv_att_rhost = os_ext_srv_att_rhost
        self.os_ext_srv_att_rhypervisor_hostname = os_ext_srv_att_rhypervisor_hostname
        self.os_ext_srv_att_rinstance_name = os_ext_srv_att_rinstance_name
        self.os_ext_st_spower_state = os_ext_st_spower_state
        self.os_ext_st_stask_state = os_ext_st_stask_state
        self.os_ext_st_svm_state = os_ext_st_svm_state
        self.os_srv_us_glaunched_at = os_srv_us_glaunched_at
        self.os_srv_us_gterminated_at = os_srv_us_gterminated_at
        self.os_extended_volumesvolumes_attached = os_extended_volumesvolumes_attached
        if fault is not None:
            self.fault = fault
        if description is not None:
            self.description = description
        self.host_status = host_status
        if os_ext_srv_att_rhostname is not None:
            self.os_ext_srv_att_rhostname = os_ext_srv_att_rhostname
        if os_ext_srv_att_rreservation_id is not None:
            self.os_ext_srv_att_rreservation_id = os_ext_srv_att_rreservation_id
        if os_ext_srv_att_rlaunch_index is not None:
            self.os_ext_srv_att_rlaunch_index = os_ext_srv_att_rlaunch_index
        if os_ext_srv_att_rkernel_id is not None:
            self.os_ext_srv_att_rkernel_id = os_ext_srv_att_rkernel_id
        if os_ext_srv_att_rramdisk_id is not None:
            self.os_ext_srv_att_rramdisk_id = os_ext_srv_att_rramdisk_id
        if os_ext_srv_att_rroot_device_name is not None:
            self.os_ext_srv_att_rroot_device_name = os_ext_srv_att_rroot_device_name
        if os_ext_srv_att_ruser_data is not None:
            self.os_ext_srv_att_ruser_data = os_ext_srv_att_ruser_data
        self.tags = tags
        if locked is not None:
            self.locked = locked
        self.access_i_pv4 = access_i_pv4
        self.access_i_pv6 = access_i_pv6
        self.config_drive = config_drive
        self.progress = progress
        if osscheduler_hints is not None:
            self.osscheduler_hints = osscheduler_hints

    @property
    def name(self):
        """Gets the name of this NovaServer.

        :return: The name of this NovaServer.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NovaServer.

        :param name: The name of this NovaServer.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        """Gets the id of this NovaServer.

        :return: The id of this NovaServer.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NovaServer.

        :param id: The id of this NovaServer.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this NovaServer.

        :return: The status of this NovaServer.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NovaServer.

        :param status: The status of this NovaServer.
        :type status: str
        """
        self._status = status

    @property
    def created(self):
        """Gets the created of this NovaServer.

        :return: The created of this NovaServer.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this NovaServer.

        :param created: The created of this NovaServer.
        :type created: str
        """
        self._created = created

    @property
    def updated(self):
        """Gets the updated of this NovaServer.

        :return: The updated of this NovaServer.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this NovaServer.

        :param updated: The updated of this NovaServer.
        :type updated: str
        """
        self._updated = updated

    @property
    def flavor(self):
        """Gets the flavor of this NovaServer.

        :return: The flavor of this NovaServer.
        :rtype: :class:`g42cloudsdkecs.v2.NovaServerFlavor`
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this NovaServer.

        :param flavor: The flavor of this NovaServer.
        :type flavor: :class:`g42cloudsdkecs.v2.NovaServerFlavor`
        """
        self._flavor = flavor

    @property
    def image(self):
        """Gets the image of this NovaServer.

        :return: The image of this NovaServer.
        :rtype: :class:`g42cloudsdkecs.v2.NovaServerImage`
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this NovaServer.

        :param image: The image of this NovaServer.
        :type image: :class:`g42cloudsdkecs.v2.NovaServerImage`
        """
        self._image = image

    @property
    def tenant_id(self):
        """Gets the tenant_id of this NovaServer.

        :return: The tenant_id of this NovaServer.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this NovaServer.

        :param tenant_id: The tenant_id of this NovaServer.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def key_name(self):
        """Gets the key_name of this NovaServer.

        :return: The key_name of this NovaServer.
        :rtype: str
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        """Sets the key_name of this NovaServer.

        :param key_name: The key_name of this NovaServer.
        :type key_name: str
        """
        self._key_name = key_name

    @property
    def user_id(self):
        """Gets the user_id of this NovaServer.

        :return: The user_id of this NovaServer.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this NovaServer.

        :param user_id: The user_id of this NovaServer.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def metadata(self):
        """Gets the metadata of this NovaServer.

        :return: The metadata of this NovaServer.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this NovaServer.

        :param metadata: The metadata of this NovaServer.
        :type metadata: dict(str, str)
        """
        self._metadata = metadata

    @property
    def host_id(self):
        """Gets the host_id of this NovaServer.

        :return: The host_id of this NovaServer.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this NovaServer.

        :param host_id: The host_id of this NovaServer.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def addresses(self):
        """Gets the addresses of this NovaServer.

        :return: The addresses of this NovaServer.
        :rtype: dict(str, list[NovaNetwork])
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this NovaServer.

        :param addresses: The addresses of this NovaServer.
        :type addresses: dict(str, list[NovaNetwork])
        """
        self._addresses = addresses

    @property
    def security_groups(self):
        """Gets the security_groups of this NovaServer.

        :return: The security_groups of this NovaServer.
        :rtype: list[:class:`g42cloudsdkecs.v2.NovaServerSecurityGroup`]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this NovaServer.

        :param security_groups: The security_groups of this NovaServer.
        :type security_groups: list[:class:`g42cloudsdkecs.v2.NovaServerSecurityGroup`]
        """
        self._security_groups = security_groups

    @property
    def links(self):
        """Gets the links of this NovaServer.

        :return: The links of this NovaServer.
        :rtype: list[:class:`g42cloudsdkecs.v2.NovaLink`]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this NovaServer.

        :param links: The links of this NovaServer.
        :type links: list[:class:`g42cloudsdkecs.v2.NovaLink`]
        """
        self._links = links

    @property
    def os_dc_fdisk_config(self):
        """Gets the os_dc_fdisk_config of this NovaServer.

        :return: The os_dc_fdisk_config of this NovaServer.
        :rtype: str
        """
        return self._os_dc_fdisk_config

    @os_dc_fdisk_config.setter
    def os_dc_fdisk_config(self, os_dc_fdisk_config):
        """Sets the os_dc_fdisk_config of this NovaServer.

        :param os_dc_fdisk_config: The os_dc_fdisk_config of this NovaServer.
        :type os_dc_fdisk_config: str
        """
        self._os_dc_fdisk_config = os_dc_fdisk_config

    @property
    def os_ext_a_zavailability_zone(self):
        """Gets the os_ext_a_zavailability_zone of this NovaServer.

        :return: The os_ext_a_zavailability_zone of this NovaServer.
        :rtype: str
        """
        return self._os_ext_a_zavailability_zone

    @os_ext_a_zavailability_zone.setter
    def os_ext_a_zavailability_zone(self, os_ext_a_zavailability_zone):
        """Sets the os_ext_a_zavailability_zone of this NovaServer.

        :param os_ext_a_zavailability_zone: The os_ext_a_zavailability_zone of this NovaServer.
        :type os_ext_a_zavailability_zone: str
        """
        self._os_ext_a_zavailability_zone = os_ext_a_zavailability_zone

    @property
    def os_ext_srv_att_rhost(self):
        """Gets the os_ext_srv_att_rhost of this NovaServer.

        :return: The os_ext_srv_att_rhost of this NovaServer.
        :rtype: str
        """
        return self._os_ext_srv_att_rhost

    @os_ext_srv_att_rhost.setter
    def os_ext_srv_att_rhost(self, os_ext_srv_att_rhost):
        """Sets the os_ext_srv_att_rhost of this NovaServer.

        :param os_ext_srv_att_rhost: The os_ext_srv_att_rhost of this NovaServer.
        :type os_ext_srv_att_rhost: str
        """
        self._os_ext_srv_att_rhost = os_ext_srv_att_rhost

    @property
    def os_ext_srv_att_rhypervisor_hostname(self):
        """Gets the os_ext_srv_att_rhypervisor_hostname of this NovaServer.

        :return: The os_ext_srv_att_rhypervisor_hostname of this NovaServer.
        :rtype: str
        """
        return self._os_ext_srv_att_rhypervisor_hostname

    @os_ext_srv_att_rhypervisor_hostname.setter
    def os_ext_srv_att_rhypervisor_hostname(self, os_ext_srv_att_rhypervisor_hostname):
        """Sets the os_ext_srv_att_rhypervisor_hostname of this NovaServer.

        :param os_ext_srv_att_rhypervisor_hostname: The os_ext_srv_att_rhypervisor_hostname of this NovaServer.
        :type os_ext_srv_att_rhypervisor_hostname: str
        """
        self._os_ext_srv_att_rhypervisor_hostname = os_ext_srv_att_rhypervisor_hostname

    @property
    def os_ext_srv_att_rinstance_name(self):
        """Gets the os_ext_srv_att_rinstance_name of this NovaServer.

        :return: The os_ext_srv_att_rinstance_name of this NovaServer.
        :rtype: str
        """
        return self._os_ext_srv_att_rinstance_name

    @os_ext_srv_att_rinstance_name.setter
    def os_ext_srv_att_rinstance_name(self, os_ext_srv_att_rinstance_name):
        """Sets the os_ext_srv_att_rinstance_name of this NovaServer.

        :param os_ext_srv_att_rinstance_name: The os_ext_srv_att_rinstance_name of this NovaServer.
        :type os_ext_srv_att_rinstance_name: str
        """
        self._os_ext_srv_att_rinstance_name = os_ext_srv_att_rinstance_name

    @property
    def os_ext_st_spower_state(self):
        """Gets the os_ext_st_spower_state of this NovaServer.

        :return: The os_ext_st_spower_state of this NovaServer.
        :rtype: int
        """
        return self._os_ext_st_spower_state

    @os_ext_st_spower_state.setter
    def os_ext_st_spower_state(self, os_ext_st_spower_state):
        """Sets the os_ext_st_spower_state of this NovaServer.

        :param os_ext_st_spower_state: The os_ext_st_spower_state of this NovaServer.
        :type os_ext_st_spower_state: int
        """
        self._os_ext_st_spower_state = os_ext_st_spower_state

    @property
    def os_ext_st_stask_state(self):
        """Gets the os_ext_st_stask_state of this NovaServer.

        :return: The os_ext_st_stask_state of this NovaServer.
        :rtype: str
        """
        return self._os_ext_st_stask_state

    @os_ext_st_stask_state.setter
    def os_ext_st_stask_state(self, os_ext_st_stask_state):
        """Sets the os_ext_st_stask_state of this NovaServer.

        :param os_ext_st_stask_state: The os_ext_st_stask_state of this NovaServer.
        :type os_ext_st_stask_state: str
        """
        self._os_ext_st_stask_state = os_ext_st_stask_state

    @property
    def os_ext_st_svm_state(self):
        """Gets the os_ext_st_svm_state of this NovaServer.

        :return: The os_ext_st_svm_state of this NovaServer.
        :rtype: str
        """
        return self._os_ext_st_svm_state

    @os_ext_st_svm_state.setter
    def os_ext_st_svm_state(self, os_ext_st_svm_state):
        """Sets the os_ext_st_svm_state of this NovaServer.

        :param os_ext_st_svm_state: The os_ext_st_svm_state of this NovaServer.
        :type os_ext_st_svm_state: str
        """
        self._os_ext_st_svm_state = os_ext_st_svm_state

    @property
    def os_srv_us_glaunched_at(self):
        """Gets the os_srv_us_glaunched_at of this NovaServer.

        :return: The os_srv_us_glaunched_at of this NovaServer.
        :rtype: str
        """
        return self._os_srv_us_glaunched_at

    @os_srv_us_glaunched_at.setter
    def os_srv_us_glaunched_at(self, os_srv_us_glaunched_at):
        """Sets the os_srv_us_glaunched_at of this NovaServer.

        :param os_srv_us_glaunched_at: The os_srv_us_glaunched_at of this NovaServer.
        :type os_srv_us_glaunched_at: str
        """
        self._os_srv_us_glaunched_at = os_srv_us_glaunched_at

    @property
    def os_srv_us_gterminated_at(self):
        """Gets the os_srv_us_gterminated_at of this NovaServer.

        :return: The os_srv_us_gterminated_at of this NovaServer.
        :rtype: str
        """
        return self._os_srv_us_gterminated_at

    @os_srv_us_gterminated_at.setter
    def os_srv_us_gterminated_at(self, os_srv_us_gterminated_at):
        """Sets the os_srv_us_gterminated_at of this NovaServer.

        :param os_srv_us_gterminated_at: The os_srv_us_gterminated_at of this NovaServer.
        :type os_srv_us_gterminated_at: str
        """
        self._os_srv_us_gterminated_at = os_srv_us_gterminated_at

    @property
    def os_extended_volumesvolumes_attached(self):
        """Gets the os_extended_volumesvolumes_attached of this NovaServer.

        :return: The os_extended_volumesvolumes_attached of this NovaServer.
        :rtype: list[:class:`g42cloudsdkecs.v2.NovaServerVolume`]
        """
        return self._os_extended_volumesvolumes_attached

    @os_extended_volumesvolumes_attached.setter
    def os_extended_volumesvolumes_attached(self, os_extended_volumesvolumes_attached):
        """Sets the os_extended_volumesvolumes_attached of this NovaServer.

        :param os_extended_volumesvolumes_attached: The os_extended_volumesvolumes_attached of this NovaServer.
        :type os_extended_volumesvolumes_attached: list[:class:`g42cloudsdkecs.v2.NovaServerVolume`]
        """
        self._os_extended_volumesvolumes_attached = os_extended_volumesvolumes_attached

    @property
    def fault(self):
        """Gets the fault of this NovaServer.

        :return: The fault of this NovaServer.
        :rtype: :class:`g42cloudsdkecs.v2.NovaServerFault`
        """
        return self._fault

    @fault.setter
    def fault(self, fault):
        """Sets the fault of this NovaServer.

        :param fault: The fault of this NovaServer.
        :type fault: :class:`g42cloudsdkecs.v2.NovaServerFault`
        """
        self._fault = fault

    @property
    def description(self):
        """Gets the description of this NovaServer.

        :return: The description of this NovaServer.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NovaServer.

        :param description: The description of this NovaServer.
        :type description: str
        """
        self._description = description

    @property
    def host_status(self):
        """Gets the host_status of this NovaServer.

        :return: The host_status of this NovaServer.
        :rtype: str
        """
        return self._host_status

    @host_status.setter
    def host_status(self, host_status):
        """Sets the host_status of this NovaServer.

        :param host_status: The host_status of this NovaServer.
        :type host_status: str
        """
        self._host_status = host_status

    @property
    def os_ext_srv_att_rhostname(self):
        """Gets the os_ext_srv_att_rhostname of this NovaServer.

        :return: The os_ext_srv_att_rhostname of this NovaServer.
        :rtype: str
        """
        return self._os_ext_srv_att_rhostname

    @os_ext_srv_att_rhostname.setter
    def os_ext_srv_att_rhostname(self, os_ext_srv_att_rhostname):
        """Sets the os_ext_srv_att_rhostname of this NovaServer.

        :param os_ext_srv_att_rhostname: The os_ext_srv_att_rhostname of this NovaServer.
        :type os_ext_srv_att_rhostname: str
        """
        self._os_ext_srv_att_rhostname = os_ext_srv_att_rhostname

    @property
    def os_ext_srv_att_rreservation_id(self):
        """Gets the os_ext_srv_att_rreservation_id of this NovaServer.

        :return: The os_ext_srv_att_rreservation_id of this NovaServer.
        :rtype: str
        """
        return self._os_ext_srv_att_rreservation_id

    @os_ext_srv_att_rreservation_id.setter
    def os_ext_srv_att_rreservation_id(self, os_ext_srv_att_rreservation_id):
        """Sets the os_ext_srv_att_rreservation_id of this NovaServer.

        :param os_ext_srv_att_rreservation_id: The os_ext_srv_att_rreservation_id of this NovaServer.
        :type os_ext_srv_att_rreservation_id: str
        """
        self._os_ext_srv_att_rreservation_id = os_ext_srv_att_rreservation_id

    @property
    def os_ext_srv_att_rlaunch_index(self):
        """Gets the os_ext_srv_att_rlaunch_index of this NovaServer.

        :return: The os_ext_srv_att_rlaunch_index of this NovaServer.
        :rtype: int
        """
        return self._os_ext_srv_att_rlaunch_index

    @os_ext_srv_att_rlaunch_index.setter
    def os_ext_srv_att_rlaunch_index(self, os_ext_srv_att_rlaunch_index):
        """Sets the os_ext_srv_att_rlaunch_index of this NovaServer.

        :param os_ext_srv_att_rlaunch_index: The os_ext_srv_att_rlaunch_index of this NovaServer.
        :type os_ext_srv_att_rlaunch_index: int
        """
        self._os_ext_srv_att_rlaunch_index = os_ext_srv_att_rlaunch_index

    @property
    def os_ext_srv_att_rkernel_id(self):
        """Gets the os_ext_srv_att_rkernel_id of this NovaServer.

        :return: The os_ext_srv_att_rkernel_id of this NovaServer.
        :rtype: str
        """
        return self._os_ext_srv_att_rkernel_id

    @os_ext_srv_att_rkernel_id.setter
    def os_ext_srv_att_rkernel_id(self, os_ext_srv_att_rkernel_id):
        """Sets the os_ext_srv_att_rkernel_id of this NovaServer.

        :param os_ext_srv_att_rkernel_id: The os_ext_srv_att_rkernel_id of this NovaServer.
        :type os_ext_srv_att_rkernel_id: str
        """
        self._os_ext_srv_att_rkernel_id = os_ext_srv_att_rkernel_id

    @property
    def os_ext_srv_att_rramdisk_id(self):
        """Gets the os_ext_srv_att_rramdisk_id of this NovaServer.

        :return: The os_ext_srv_att_rramdisk_id of this NovaServer.
        :rtype: str
        """
        return self._os_ext_srv_att_rramdisk_id

    @os_ext_srv_att_rramdisk_id.setter
    def os_ext_srv_att_rramdisk_id(self, os_ext_srv_att_rramdisk_id):
        """Sets the os_ext_srv_att_rramdisk_id of this NovaServer.

        :param os_ext_srv_att_rramdisk_id: The os_ext_srv_att_rramdisk_id of this NovaServer.
        :type os_ext_srv_att_rramdisk_id: str
        """
        self._os_ext_srv_att_rramdisk_id = os_ext_srv_att_rramdisk_id

    @property
    def os_ext_srv_att_rroot_device_name(self):
        """Gets the os_ext_srv_att_rroot_device_name of this NovaServer.

        :return: The os_ext_srv_att_rroot_device_name of this NovaServer.
        :rtype: str
        """
        return self._os_ext_srv_att_rroot_device_name

    @os_ext_srv_att_rroot_device_name.setter
    def os_ext_srv_att_rroot_device_name(self, os_ext_srv_att_rroot_device_name):
        """Sets the os_ext_srv_att_rroot_device_name of this NovaServer.

        :param os_ext_srv_att_rroot_device_name: The os_ext_srv_att_rroot_device_name of this NovaServer.
        :type os_ext_srv_att_rroot_device_name: str
        """
        self._os_ext_srv_att_rroot_device_name = os_ext_srv_att_rroot_device_name

    @property
    def os_ext_srv_att_ruser_data(self):
        """Gets the os_ext_srv_att_ruser_data of this NovaServer.

        :return: The os_ext_srv_att_ruser_data of this NovaServer.
        :rtype: str
        """
        return self._os_ext_srv_att_ruser_data

    @os_ext_srv_att_ruser_data.setter
    def os_ext_srv_att_ruser_data(self, os_ext_srv_att_ruser_data):
        """Sets the os_ext_srv_att_ruser_data of this NovaServer.

        :param os_ext_srv_att_ruser_data: The os_ext_srv_att_ruser_data of this NovaServer.
        :type os_ext_srv_att_ruser_data: str
        """
        self._os_ext_srv_att_ruser_data = os_ext_srv_att_ruser_data

    @property
    def tags(self):
        """Gets the tags of this NovaServer.

        :return: The tags of this NovaServer.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this NovaServer.

        :param tags: The tags of this NovaServer.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def locked(self):
        """Gets the locked of this NovaServer.

        :return: The locked of this NovaServer.
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this NovaServer.

        :param locked: The locked of this NovaServer.
        :type locked: bool
        """
        self._locked = locked

    @property
    def access_i_pv4(self):
        """Gets the access_i_pv4 of this NovaServer.

        :return: The access_i_pv4 of this NovaServer.
        :rtype: str
        """
        return self._access_i_pv4

    @access_i_pv4.setter
    def access_i_pv4(self, access_i_pv4):
        """Sets the access_i_pv4 of this NovaServer.

        :param access_i_pv4: The access_i_pv4 of this NovaServer.
        :type access_i_pv4: str
        """
        self._access_i_pv4 = access_i_pv4

    @property
    def access_i_pv6(self):
        """Gets the access_i_pv6 of this NovaServer.

        :return: The access_i_pv6 of this NovaServer.
        :rtype: str
        """
        return self._access_i_pv6

    @access_i_pv6.setter
    def access_i_pv6(self, access_i_pv6):
        """Sets the access_i_pv6 of this NovaServer.

        :param access_i_pv6: The access_i_pv6 of this NovaServer.
        :type access_i_pv6: str
        """
        self._access_i_pv6 = access_i_pv6

    @property
    def config_drive(self):
        """Gets the config_drive of this NovaServer.

        :return: The config_drive of this NovaServer.
        :rtype: str
        """
        return self._config_drive

    @config_drive.setter
    def config_drive(self, config_drive):
        """Sets the config_drive of this NovaServer.

        :param config_drive: The config_drive of this NovaServer.
        :type config_drive: str
        """
        self._config_drive = config_drive

    @property
    def progress(self):
        """Gets the progress of this NovaServer.

        :return: The progress of this NovaServer.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this NovaServer.

        :param progress: The progress of this NovaServer.
        :type progress: int
        """
        self._progress = progress

    @property
    def osscheduler_hints(self):
        """Gets the osscheduler_hints of this NovaServer.

        :return: The osscheduler_hints of this NovaServer.
        :rtype: :class:`g42cloudsdkecs.v2.NovaServerSchedulerHints`
        """
        return self._osscheduler_hints

    @osscheduler_hints.setter
    def osscheduler_hints(self, osscheduler_hints):
        """Sets the osscheduler_hints of this NovaServer.

        :param osscheduler_hints: The osscheduler_hints of this NovaServer.
        :type osscheduler_hints: :class:`g42cloudsdkecs.v2.NovaServerSchedulerHints`
        """
        self._osscheduler_hints = osscheduler_hints

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
        if not isinstance(other, NovaServer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other