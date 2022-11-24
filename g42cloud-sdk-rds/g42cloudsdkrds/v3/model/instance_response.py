# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceResponse:

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
        'status': 'str',
        'enable_ssl': 'bool',
        'private_ips': 'list[str]',
        'private_dns_names': 'list[str]',
        'public_ips': 'list[str]',
        'type': 'str',
        'created': 'str',
        'updated': 'str',
        'db_user_name': 'str',
        'switch_strategy': 'str',
        'maintenance_window': 'str',
        'nodes': 'list[NodeResponse]',
        'related_instance': 'list[RelatedInstance]',
        'name': 'str',
        'datastore': 'Datastore',
        'ha': 'HaResponse',
        'port': 'int',
        'backup_strategy': 'BackupStrategyForResponse',
        'enterprise_project_id': 'str',
        'disk_encryption_id': 'str',
        'flavor_ref': 'str',
        'cpu': 'str',
        'mem': 'str',
        'volume': 'Volume',
        'region': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'security_group_id': 'str',
        'charge_info': 'ChargeInfoResponse',
        'time_zone': 'str',
        'tags': 'list[TagResponse]',
        'backup_used_space': 'float',
        'storage_used_space': 'float',
        'order_id': 'str',
        'associated_with_ddm': 'bool',
        'alias': 'str',
        'max_iops': 'int',
        'expiration_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'enable_ssl': 'enable_ssl',
        'private_ips': 'private_ips',
        'private_dns_names': 'private_dns_names',
        'public_ips': 'public_ips',
        'type': 'type',
        'created': 'created',
        'updated': 'updated',
        'db_user_name': 'db_user_name',
        'switch_strategy': 'switch_strategy',
        'maintenance_window': 'maintenance_window',
        'nodes': 'nodes',
        'related_instance': 'related_instance',
        'name': 'name',
        'datastore': 'datastore',
        'ha': 'ha',
        'port': 'port',
        'backup_strategy': 'backup_strategy',
        'enterprise_project_id': 'enterprise_project_id',
        'disk_encryption_id': 'disk_encryption_id',
        'flavor_ref': 'flavor_ref',
        'cpu': 'cpu',
        'mem': 'mem',
        'volume': 'volume',
        'region': 'region',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'security_group_id': 'security_group_id',
        'charge_info': 'charge_info',
        'time_zone': 'time_zone',
        'tags': 'tags',
        'backup_used_space': 'backup_used_space',
        'storage_used_space': 'storage_used_space',
        'order_id': 'order_id',
        'associated_with_ddm': 'associated_with_ddm',
        'alias': 'alias',
        'max_iops': 'max_iops',
        'expiration_time': 'expiration_time'
    }

    def __init__(self, id=None, status=None, enable_ssl=None, private_ips=None, private_dns_names=None, public_ips=None, type=None, created=None, updated=None, db_user_name=None, switch_strategy=None, maintenance_window=None, nodes=None, related_instance=None, name=None, datastore=None, ha=None, port=None, backup_strategy=None, enterprise_project_id=None, disk_encryption_id=None, flavor_ref=None, cpu=None, mem=None, volume=None, region=None, vpc_id=None, subnet_id=None, security_group_id=None, charge_info=None, time_zone=None, tags=None, backup_used_space=None, storage_used_space=None, order_id=None, associated_with_ddm=None, alias=None, max_iops=None, expiration_time=None):
        """InstanceResponse

        The model defined in g42cloud sdk

        :param id: The param of the InstanceResponse
        :type id: str
        :param status: The param of the InstanceResponse
        :type status: str
        :param enable_ssl: The param of the InstanceResponse
        :type enable_ssl: bool
        :param private_ips: The param of the InstanceResponse
        :type private_ips: list[str]
        :param private_dns_names: The param of the InstanceResponse
        :type private_dns_names: list[str]
        :param public_ips: The param of the InstanceResponse
        :type public_ips: list[str]
        :param type: The param of the InstanceResponse
        :type type: str
        :param created: The param of the InstanceResponse
        :type created: str
        :param updated: The param of the InstanceResponse
        :type updated: str
        :param db_user_name: The param of the InstanceResponse
        :type db_user_name: str
        :param switch_strategy: The param of the InstanceResponse
        :type switch_strategy: str
        :param maintenance_window: The param of the InstanceResponse
        :type maintenance_window: str
        :param nodes: The param of the InstanceResponse
        :type nodes: list[:class:`g42cloudsdkrds.v3.NodeResponse`]
        :param related_instance: The param of the InstanceResponse
        :type related_instance: list[:class:`g42cloudsdkrds.v3.RelatedInstance`]
        :param name: The param of the InstanceResponse
        :type name: str
        :param datastore: The param of the InstanceResponse
        :type datastore: :class:`g42cloudsdkrds.v3.Datastore`
        :param ha: The param of the InstanceResponse
        :type ha: :class:`g42cloudsdkrds.v3.HaResponse`
        :param port: The param of the InstanceResponse
        :type port: int
        :param backup_strategy: The param of the InstanceResponse
        :type backup_strategy: :class:`g42cloudsdkrds.v3.BackupStrategyForResponse`
        :param enterprise_project_id: The param of the InstanceResponse
        :type enterprise_project_id: str
        :param disk_encryption_id: The param of the InstanceResponse
        :type disk_encryption_id: str
        :param flavor_ref: The param of the InstanceResponse
        :type flavor_ref: str
        :param cpu: The param of the InstanceResponse
        :type cpu: str
        :param mem: The param of the InstanceResponse
        :type mem: str
        :param volume: The param of the InstanceResponse
        :type volume: :class:`g42cloudsdkrds.v3.Volume`
        :param region: The param of the InstanceResponse
        :type region: str
        :param vpc_id: The param of the InstanceResponse
        :type vpc_id: str
        :param subnet_id: The param of the InstanceResponse
        :type subnet_id: str
        :param security_group_id: The param of the InstanceResponse
        :type security_group_id: str
        :param charge_info: The param of the InstanceResponse
        :type charge_info: :class:`g42cloudsdkrds.v3.ChargeInfoResponse`
        :param time_zone: The param of the InstanceResponse
        :type time_zone: str
        :param tags: The param of the InstanceResponse
        :type tags: list[:class:`g42cloudsdkrds.v3.TagResponse`]
        :param backup_used_space: The param of the InstanceResponse
        :type backup_used_space: float
        :param storage_used_space: The param of the InstanceResponse
        :type storage_used_space: float
        :param order_id: The param of the InstanceResponse
        :type order_id: str
        :param associated_with_ddm: The param of the InstanceResponse
        :type associated_with_ddm: bool
        :param alias: The param of the InstanceResponse
        :type alias: str
        :param max_iops: The param of the InstanceResponse
        :type max_iops: int
        :param expiration_time: The param of the InstanceResponse
        :type expiration_time: str
        """
        
        

        self._id = None
        self._status = None
        self._enable_ssl = None
        self._private_ips = None
        self._private_dns_names = None
        self._public_ips = None
        self._type = None
        self._created = None
        self._updated = None
        self._db_user_name = None
        self._switch_strategy = None
        self._maintenance_window = None
        self._nodes = None
        self._related_instance = None
        self._name = None
        self._datastore = None
        self._ha = None
        self._port = None
        self._backup_strategy = None
        self._enterprise_project_id = None
        self._disk_encryption_id = None
        self._flavor_ref = None
        self._cpu = None
        self._mem = None
        self._volume = None
        self._region = None
        self._vpc_id = None
        self._subnet_id = None
        self._security_group_id = None
        self._charge_info = None
        self._time_zone = None
        self._tags = None
        self._backup_used_space = None
        self._storage_used_space = None
        self._order_id = None
        self._associated_with_ddm = None
        self._alias = None
        self._max_iops = None
        self._expiration_time = None
        self.discriminator = None

        self.id = id
        self.status = status
        self.enable_ssl = enable_ssl
        self.private_ips = private_ips
        if private_dns_names is not None:
            self.private_dns_names = private_dns_names
        self.public_ips = public_ips
        self.type = type
        self.created = created
        self.updated = updated
        self.db_user_name = db_user_name
        self.switch_strategy = switch_strategy
        self.maintenance_window = maintenance_window
        self.nodes = nodes
        self.related_instance = related_instance
        self.name = name
        self.datastore = datastore
        if ha is not None:
            self.ha = ha
        self.port = port
        self.backup_strategy = backup_strategy
        self.enterprise_project_id = enterprise_project_id
        self.disk_encryption_id = disk_encryption_id
        self.flavor_ref = flavor_ref
        if cpu is not None:
            self.cpu = cpu
        if mem is not None:
            self.mem = mem
        self.volume = volume
        self.region = region
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        self.security_group_id = security_group_id
        self.charge_info = charge_info
        self.time_zone = time_zone
        self.tags = tags
        if backup_used_space is not None:
            self.backup_used_space = backup_used_space
        if storage_used_space is not None:
            self.storage_used_space = storage_used_space
        if order_id is not None:
            self.order_id = order_id
        if associated_with_ddm is not None:
            self.associated_with_ddm = associated_with_ddm
        if alias is not None:
            self.alias = alias
        if max_iops is not None:
            self.max_iops = max_iops
        if expiration_time is not None:
            self.expiration_time = expiration_time

    @property
    def id(self):
        """Gets the id of this InstanceResponse.

        :return: The id of this InstanceResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InstanceResponse.

        :param id: The id of this InstanceResponse.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this InstanceResponse.

        :return: The status of this InstanceResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InstanceResponse.

        :param status: The status of this InstanceResponse.
        :type status: str
        """
        self._status = status

    @property
    def enable_ssl(self):
        """Gets the enable_ssl of this InstanceResponse.

        :return: The enable_ssl of this InstanceResponse.
        :rtype: bool
        """
        return self._enable_ssl

    @enable_ssl.setter
    def enable_ssl(self, enable_ssl):
        """Sets the enable_ssl of this InstanceResponse.

        :param enable_ssl: The enable_ssl of this InstanceResponse.
        :type enable_ssl: bool
        """
        self._enable_ssl = enable_ssl

    @property
    def private_ips(self):
        """Gets the private_ips of this InstanceResponse.

        :return: The private_ips of this InstanceResponse.
        :rtype: list[str]
        """
        return self._private_ips

    @private_ips.setter
    def private_ips(self, private_ips):
        """Sets the private_ips of this InstanceResponse.

        :param private_ips: The private_ips of this InstanceResponse.
        :type private_ips: list[str]
        """
        self._private_ips = private_ips

    @property
    def private_dns_names(self):
        """Gets the private_dns_names of this InstanceResponse.

        :return: The private_dns_names of this InstanceResponse.
        :rtype: list[str]
        """
        return self._private_dns_names

    @private_dns_names.setter
    def private_dns_names(self, private_dns_names):
        """Sets the private_dns_names of this InstanceResponse.

        :param private_dns_names: The private_dns_names of this InstanceResponse.
        :type private_dns_names: list[str]
        """
        self._private_dns_names = private_dns_names

    @property
    def public_ips(self):
        """Gets the public_ips of this InstanceResponse.

        :return: The public_ips of this InstanceResponse.
        :rtype: list[str]
        """
        return self._public_ips

    @public_ips.setter
    def public_ips(self, public_ips):
        """Sets the public_ips of this InstanceResponse.

        :param public_ips: The public_ips of this InstanceResponse.
        :type public_ips: list[str]
        """
        self._public_ips = public_ips

    @property
    def type(self):
        """Gets the type of this InstanceResponse.

        :return: The type of this InstanceResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InstanceResponse.

        :param type: The type of this InstanceResponse.
        :type type: str
        """
        self._type = type

    @property
    def created(self):
        """Gets the created of this InstanceResponse.

        :return: The created of this InstanceResponse.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this InstanceResponse.

        :param created: The created of this InstanceResponse.
        :type created: str
        """
        self._created = created

    @property
    def updated(self):
        """Gets the updated of this InstanceResponse.

        :return: The updated of this InstanceResponse.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this InstanceResponse.

        :param updated: The updated of this InstanceResponse.
        :type updated: str
        """
        self._updated = updated

    @property
    def db_user_name(self):
        """Gets the db_user_name of this InstanceResponse.

        :return: The db_user_name of this InstanceResponse.
        :rtype: str
        """
        return self._db_user_name

    @db_user_name.setter
    def db_user_name(self, db_user_name):
        """Sets the db_user_name of this InstanceResponse.

        :param db_user_name: The db_user_name of this InstanceResponse.
        :type db_user_name: str
        """
        self._db_user_name = db_user_name

    @property
    def switch_strategy(self):
        """Gets the switch_strategy of this InstanceResponse.

        :return: The switch_strategy of this InstanceResponse.
        :rtype: str
        """
        return self._switch_strategy

    @switch_strategy.setter
    def switch_strategy(self, switch_strategy):
        """Sets the switch_strategy of this InstanceResponse.

        :param switch_strategy: The switch_strategy of this InstanceResponse.
        :type switch_strategy: str
        """
        self._switch_strategy = switch_strategy

    @property
    def maintenance_window(self):
        """Gets the maintenance_window of this InstanceResponse.

        :return: The maintenance_window of this InstanceResponse.
        :rtype: str
        """
        return self._maintenance_window

    @maintenance_window.setter
    def maintenance_window(self, maintenance_window):
        """Sets the maintenance_window of this InstanceResponse.

        :param maintenance_window: The maintenance_window of this InstanceResponse.
        :type maintenance_window: str
        """
        self._maintenance_window = maintenance_window

    @property
    def nodes(self):
        """Gets the nodes of this InstanceResponse.

        :return: The nodes of this InstanceResponse.
        :rtype: list[:class:`g42cloudsdkrds.v3.NodeResponse`]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this InstanceResponse.

        :param nodes: The nodes of this InstanceResponse.
        :type nodes: list[:class:`g42cloudsdkrds.v3.NodeResponse`]
        """
        self._nodes = nodes

    @property
    def related_instance(self):
        """Gets the related_instance of this InstanceResponse.

        :return: The related_instance of this InstanceResponse.
        :rtype: list[:class:`g42cloudsdkrds.v3.RelatedInstance`]
        """
        return self._related_instance

    @related_instance.setter
    def related_instance(self, related_instance):
        """Sets the related_instance of this InstanceResponse.

        :param related_instance: The related_instance of this InstanceResponse.
        :type related_instance: list[:class:`g42cloudsdkrds.v3.RelatedInstance`]
        """
        self._related_instance = related_instance

    @property
    def name(self):
        """Gets the name of this InstanceResponse.

        :return: The name of this InstanceResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InstanceResponse.

        :param name: The name of this InstanceResponse.
        :type name: str
        """
        self._name = name

    @property
    def datastore(self):
        """Gets the datastore of this InstanceResponse.

        :return: The datastore of this InstanceResponse.
        :rtype: :class:`g42cloudsdkrds.v3.Datastore`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        """Sets the datastore of this InstanceResponse.

        :param datastore: The datastore of this InstanceResponse.
        :type datastore: :class:`g42cloudsdkrds.v3.Datastore`
        """
        self._datastore = datastore

    @property
    def ha(self):
        """Gets the ha of this InstanceResponse.

        :return: The ha of this InstanceResponse.
        :rtype: :class:`g42cloudsdkrds.v3.HaResponse`
        """
        return self._ha

    @ha.setter
    def ha(self, ha):
        """Sets the ha of this InstanceResponse.

        :param ha: The ha of this InstanceResponse.
        :type ha: :class:`g42cloudsdkrds.v3.HaResponse`
        """
        self._ha = ha

    @property
    def port(self):
        """Gets the port of this InstanceResponse.

        :return: The port of this InstanceResponse.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this InstanceResponse.

        :param port: The port of this InstanceResponse.
        :type port: int
        """
        self._port = port

    @property
    def backup_strategy(self):
        """Gets the backup_strategy of this InstanceResponse.

        :return: The backup_strategy of this InstanceResponse.
        :rtype: :class:`g42cloudsdkrds.v3.BackupStrategyForResponse`
        """
        return self._backup_strategy

    @backup_strategy.setter
    def backup_strategy(self, backup_strategy):
        """Sets the backup_strategy of this InstanceResponse.

        :param backup_strategy: The backup_strategy of this InstanceResponse.
        :type backup_strategy: :class:`g42cloudsdkrds.v3.BackupStrategyForResponse`
        """
        self._backup_strategy = backup_strategy

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this InstanceResponse.

        :return: The enterprise_project_id of this InstanceResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this InstanceResponse.

        :param enterprise_project_id: The enterprise_project_id of this InstanceResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def disk_encryption_id(self):
        """Gets the disk_encryption_id of this InstanceResponse.

        :return: The disk_encryption_id of this InstanceResponse.
        :rtype: str
        """
        return self._disk_encryption_id

    @disk_encryption_id.setter
    def disk_encryption_id(self, disk_encryption_id):
        """Sets the disk_encryption_id of this InstanceResponse.

        :param disk_encryption_id: The disk_encryption_id of this InstanceResponse.
        :type disk_encryption_id: str
        """
        self._disk_encryption_id = disk_encryption_id

    @property
    def flavor_ref(self):
        """Gets the flavor_ref of this InstanceResponse.

        :return: The flavor_ref of this InstanceResponse.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        """Sets the flavor_ref of this InstanceResponse.

        :param flavor_ref: The flavor_ref of this InstanceResponse.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def cpu(self):
        """Gets the cpu of this InstanceResponse.

        :return: The cpu of this InstanceResponse.
        :rtype: str
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this InstanceResponse.

        :param cpu: The cpu of this InstanceResponse.
        :type cpu: str
        """
        self._cpu = cpu

    @property
    def mem(self):
        """Gets the mem of this InstanceResponse.

        :return: The mem of this InstanceResponse.
        :rtype: str
        """
        return self._mem

    @mem.setter
    def mem(self, mem):
        """Sets the mem of this InstanceResponse.

        :param mem: The mem of this InstanceResponse.
        :type mem: str
        """
        self._mem = mem

    @property
    def volume(self):
        """Gets the volume of this InstanceResponse.

        :return: The volume of this InstanceResponse.
        :rtype: :class:`g42cloudsdkrds.v3.Volume`
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this InstanceResponse.

        :param volume: The volume of this InstanceResponse.
        :type volume: :class:`g42cloudsdkrds.v3.Volume`
        """
        self._volume = volume

    @property
    def region(self):
        """Gets the region of this InstanceResponse.

        :return: The region of this InstanceResponse.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this InstanceResponse.

        :param region: The region of this InstanceResponse.
        :type region: str
        """
        self._region = region

    @property
    def vpc_id(self):
        """Gets the vpc_id of this InstanceResponse.

        :return: The vpc_id of this InstanceResponse.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this InstanceResponse.

        :param vpc_id: The vpc_id of this InstanceResponse.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this InstanceResponse.

        :return: The subnet_id of this InstanceResponse.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this InstanceResponse.

        :param subnet_id: The subnet_id of this InstanceResponse.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        """Gets the security_group_id of this InstanceResponse.

        :return: The security_group_id of this InstanceResponse.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this InstanceResponse.

        :param security_group_id: The security_group_id of this InstanceResponse.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def charge_info(self):
        """Gets the charge_info of this InstanceResponse.

        :return: The charge_info of this InstanceResponse.
        :rtype: :class:`g42cloudsdkrds.v3.ChargeInfoResponse`
        """
        return self._charge_info

    @charge_info.setter
    def charge_info(self, charge_info):
        """Sets the charge_info of this InstanceResponse.

        :param charge_info: The charge_info of this InstanceResponse.
        :type charge_info: :class:`g42cloudsdkrds.v3.ChargeInfoResponse`
        """
        self._charge_info = charge_info

    @property
    def time_zone(self):
        """Gets the time_zone of this InstanceResponse.

        :return: The time_zone of this InstanceResponse.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this InstanceResponse.

        :param time_zone: The time_zone of this InstanceResponse.
        :type time_zone: str
        """
        self._time_zone = time_zone

    @property
    def tags(self):
        """Gets the tags of this InstanceResponse.

        :return: The tags of this InstanceResponse.
        :rtype: list[:class:`g42cloudsdkrds.v3.TagResponse`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this InstanceResponse.

        :param tags: The tags of this InstanceResponse.
        :type tags: list[:class:`g42cloudsdkrds.v3.TagResponse`]
        """
        self._tags = tags

    @property
    def backup_used_space(self):
        """Gets the backup_used_space of this InstanceResponse.

        :return: The backup_used_space of this InstanceResponse.
        :rtype: float
        """
        return self._backup_used_space

    @backup_used_space.setter
    def backup_used_space(self, backup_used_space):
        """Sets the backup_used_space of this InstanceResponse.

        :param backup_used_space: The backup_used_space of this InstanceResponse.
        :type backup_used_space: float
        """
        self._backup_used_space = backup_used_space

    @property
    def storage_used_space(self):
        """Gets the storage_used_space of this InstanceResponse.

        :return: The storage_used_space of this InstanceResponse.
        :rtype: float
        """
        return self._storage_used_space

    @storage_used_space.setter
    def storage_used_space(self, storage_used_space):
        """Sets the storage_used_space of this InstanceResponse.

        :param storage_used_space: The storage_used_space of this InstanceResponse.
        :type storage_used_space: float
        """
        self._storage_used_space = storage_used_space

    @property
    def order_id(self):
        """Gets the order_id of this InstanceResponse.

        :return: The order_id of this InstanceResponse.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this InstanceResponse.

        :param order_id: The order_id of this InstanceResponse.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def associated_with_ddm(self):
        """Gets the associated_with_ddm of this InstanceResponse.

        :return: The associated_with_ddm of this InstanceResponse.
        :rtype: bool
        """
        return self._associated_with_ddm

    @associated_with_ddm.setter
    def associated_with_ddm(self, associated_with_ddm):
        """Sets the associated_with_ddm of this InstanceResponse.

        :param associated_with_ddm: The associated_with_ddm of this InstanceResponse.
        :type associated_with_ddm: bool
        """
        self._associated_with_ddm = associated_with_ddm

    @property
    def alias(self):
        """Gets the alias of this InstanceResponse.

        :return: The alias of this InstanceResponse.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this InstanceResponse.

        :param alias: The alias of this InstanceResponse.
        :type alias: str
        """
        self._alias = alias

    @property
    def max_iops(self):
        """Gets the max_iops of this InstanceResponse.

        :return: The max_iops of this InstanceResponse.
        :rtype: int
        """
        return self._max_iops

    @max_iops.setter
    def max_iops(self, max_iops):
        """Sets the max_iops of this InstanceResponse.

        :param max_iops: The max_iops of this InstanceResponse.
        :type max_iops: int
        """
        self._max_iops = max_iops

    @property
    def expiration_time(self):
        """Gets the expiration_time of this InstanceResponse.

        :return: The expiration_time of this InstanceResponse.
        :rtype: str
        """
        return self._expiration_time

    @expiration_time.setter
    def expiration_time(self, expiration_time):
        """Sets the expiration_time of this InstanceResponse.

        :param expiration_time: The expiration_time of this InstanceResponse.
        :type expiration_time: str
        """
        self._expiration_time = expiration_time

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
        if not isinstance(other, InstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
