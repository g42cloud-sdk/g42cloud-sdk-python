# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRestoreInstanceRequestBody:

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
        'datastore': 'Datastore',
        'ha': 'Ha',
        'configuration_id': 'str',
        'port': 'str',
        'password': 'str',
        'backup_strategy': 'BackupStrategy',
        'enterprise_project_id': 'str',
        'disk_encryption_id': 'str',
        'flavor_ref': 'str',
        'volume': 'Volume',
        'region': 'str',
        'availability_zone': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'data_vip': 'str',
        'security_group_id': 'str',
        'charge_info': 'ChargeInfo',
        'time_zone': 'str',
        'dsspool_id': 'str',
        'replica_of_id': 'str',
        'restore_point': 'RestorePoint',
        'collation': 'str',
        'tags': 'list[TagWithKeyValue]',
        'unchangeable_param': 'UnchangeableParam',
        'dry_run': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'datastore': 'datastore',
        'ha': 'ha',
        'configuration_id': 'configuration_id',
        'port': 'port',
        'password': 'password',
        'backup_strategy': 'backup_strategy',
        'enterprise_project_id': 'enterprise_project_id',
        'disk_encryption_id': 'disk_encryption_id',
        'flavor_ref': 'flavor_ref',
        'volume': 'volume',
        'region': 'region',
        'availability_zone': 'availability_zone',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'data_vip': 'data_vip',
        'security_group_id': 'security_group_id',
        'charge_info': 'charge_info',
        'time_zone': 'time_zone',
        'dsspool_id': 'dsspool_id',
        'replica_of_id': 'replica_of_id',
        'restore_point': 'restore_point',
        'collation': 'collation',
        'tags': 'tags',
        'unchangeable_param': 'unchangeable_param',
        'dry_run': 'dry_run'
    }

    def __init__(self, name=None, datastore=None, ha=None, configuration_id=None, port=None, password=None, backup_strategy=None, enterprise_project_id=None, disk_encryption_id=None, flavor_ref=None, volume=None, region=None, availability_zone=None, vpc_id=None, subnet_id=None, data_vip=None, security_group_id=None, charge_info=None, time_zone=None, dsspool_id=None, replica_of_id=None, restore_point=None, collation=None, tags=None, unchangeable_param=None, dry_run=None):
        """CreateRestoreInstanceRequestBody

        The model defined in g42cloud sdk

        :param name: The param of the CreateRestoreInstanceRequestBody
        :type name: str
        :param datastore: The param of the CreateRestoreInstanceRequestBody
        :type datastore: :class:`g42cloudsdkrds.v3.Datastore`
        :param ha: The param of the CreateRestoreInstanceRequestBody
        :type ha: :class:`g42cloudsdkrds.v3.Ha`
        :param configuration_id: The param of the CreateRestoreInstanceRequestBody
        :type configuration_id: str
        :param port: The param of the CreateRestoreInstanceRequestBody
        :type port: str
        :param password: The param of the CreateRestoreInstanceRequestBody
        :type password: str
        :param backup_strategy: The param of the CreateRestoreInstanceRequestBody
        :type backup_strategy: :class:`g42cloudsdkrds.v3.BackupStrategy`
        :param enterprise_project_id: The param of the CreateRestoreInstanceRequestBody
        :type enterprise_project_id: str
        :param disk_encryption_id: The param of the CreateRestoreInstanceRequestBody
        :type disk_encryption_id: str
        :param flavor_ref: The param of the CreateRestoreInstanceRequestBody
        :type flavor_ref: str
        :param volume: The param of the CreateRestoreInstanceRequestBody
        :type volume: :class:`g42cloudsdkrds.v3.Volume`
        :param region: The param of the CreateRestoreInstanceRequestBody
        :type region: str
        :param availability_zone: The param of the CreateRestoreInstanceRequestBody
        :type availability_zone: str
        :param vpc_id: The param of the CreateRestoreInstanceRequestBody
        :type vpc_id: str
        :param subnet_id: The param of the CreateRestoreInstanceRequestBody
        :type subnet_id: str
        :param data_vip: The param of the CreateRestoreInstanceRequestBody
        :type data_vip: str
        :param security_group_id: The param of the CreateRestoreInstanceRequestBody
        :type security_group_id: str
        :param charge_info: The param of the CreateRestoreInstanceRequestBody
        :type charge_info: :class:`g42cloudsdkrds.v3.ChargeInfo`
        :param time_zone: The param of the CreateRestoreInstanceRequestBody
        :type time_zone: str
        :param dsspool_id: The param of the CreateRestoreInstanceRequestBody
        :type dsspool_id: str
        :param replica_of_id: The param of the CreateRestoreInstanceRequestBody
        :type replica_of_id: str
        :param restore_point: The param of the CreateRestoreInstanceRequestBody
        :type restore_point: :class:`g42cloudsdkrds.v3.RestorePoint`
        :param collation: The param of the CreateRestoreInstanceRequestBody
        :type collation: str
        :param tags: The param of the CreateRestoreInstanceRequestBody
        :type tags: list[:class:`g42cloudsdkrds.v3.TagWithKeyValue`]
        :param unchangeable_param: The param of the CreateRestoreInstanceRequestBody
        :type unchangeable_param: :class:`g42cloudsdkrds.v3.UnchangeableParam`
        :param dry_run: The param of the CreateRestoreInstanceRequestBody
        :type dry_run: bool
        """
        
        

        self._name = None
        self._datastore = None
        self._ha = None
        self._configuration_id = None
        self._port = None
        self._password = None
        self._backup_strategy = None
        self._enterprise_project_id = None
        self._disk_encryption_id = None
        self._flavor_ref = None
        self._volume = None
        self._region = None
        self._availability_zone = None
        self._vpc_id = None
        self._subnet_id = None
        self._data_vip = None
        self._security_group_id = None
        self._charge_info = None
        self._time_zone = None
        self._dsspool_id = None
        self._replica_of_id = None
        self._restore_point = None
        self._collation = None
        self._tags = None
        self._unchangeable_param = None
        self._dry_run = None
        self.discriminator = None

        self.name = name
        self.datastore = datastore
        if ha is not None:
            self.ha = ha
        if configuration_id is not None:
            self.configuration_id = configuration_id
        if port is not None:
            self.port = port
        if password is not None:
            self.password = password
        if backup_strategy is not None:
            self.backup_strategy = backup_strategy
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if disk_encryption_id is not None:
            self.disk_encryption_id = disk_encryption_id
        self.flavor_ref = flavor_ref
        self.volume = volume
        self.region = region
        self.availability_zone = availability_zone
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        if data_vip is not None:
            self.data_vip = data_vip
        self.security_group_id = security_group_id
        if charge_info is not None:
            self.charge_info = charge_info
        if time_zone is not None:
            self.time_zone = time_zone
        if dsspool_id is not None:
            self.dsspool_id = dsspool_id
        if replica_of_id is not None:
            self.replica_of_id = replica_of_id
        if restore_point is not None:
            self.restore_point = restore_point
        if collation is not None:
            self.collation = collation
        if tags is not None:
            self.tags = tags
        if unchangeable_param is not None:
            self.unchangeable_param = unchangeable_param
        if dry_run is not None:
            self.dry_run = dry_run

    @property
    def name(self):
        """Gets the name of this CreateRestoreInstanceRequestBody.

        :return: The name of this CreateRestoreInstanceRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateRestoreInstanceRequestBody.

        :param name: The name of this CreateRestoreInstanceRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def datastore(self):
        """Gets the datastore of this CreateRestoreInstanceRequestBody.

        :return: The datastore of this CreateRestoreInstanceRequestBody.
        :rtype: :class:`g42cloudsdkrds.v3.Datastore`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        """Sets the datastore of this CreateRestoreInstanceRequestBody.

        :param datastore: The datastore of this CreateRestoreInstanceRequestBody.
        :type datastore: :class:`g42cloudsdkrds.v3.Datastore`
        """
        self._datastore = datastore

    @property
    def ha(self):
        """Gets the ha of this CreateRestoreInstanceRequestBody.

        :return: The ha of this CreateRestoreInstanceRequestBody.
        :rtype: :class:`g42cloudsdkrds.v3.Ha`
        """
        return self._ha

    @ha.setter
    def ha(self, ha):
        """Sets the ha of this CreateRestoreInstanceRequestBody.

        :param ha: The ha of this CreateRestoreInstanceRequestBody.
        :type ha: :class:`g42cloudsdkrds.v3.Ha`
        """
        self._ha = ha

    @property
    def configuration_id(self):
        """Gets the configuration_id of this CreateRestoreInstanceRequestBody.

        :return: The configuration_id of this CreateRestoreInstanceRequestBody.
        :rtype: str
        """
        return self._configuration_id

    @configuration_id.setter
    def configuration_id(self, configuration_id):
        """Sets the configuration_id of this CreateRestoreInstanceRequestBody.

        :param configuration_id: The configuration_id of this CreateRestoreInstanceRequestBody.
        :type configuration_id: str
        """
        self._configuration_id = configuration_id

    @property
    def port(self):
        """Gets the port of this CreateRestoreInstanceRequestBody.

        :return: The port of this CreateRestoreInstanceRequestBody.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this CreateRestoreInstanceRequestBody.

        :param port: The port of this CreateRestoreInstanceRequestBody.
        :type port: str
        """
        self._port = port

    @property
    def password(self):
        """Gets the password of this CreateRestoreInstanceRequestBody.

        :return: The password of this CreateRestoreInstanceRequestBody.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this CreateRestoreInstanceRequestBody.

        :param password: The password of this CreateRestoreInstanceRequestBody.
        :type password: str
        """
        self._password = password

    @property
    def backup_strategy(self):
        """Gets the backup_strategy of this CreateRestoreInstanceRequestBody.

        :return: The backup_strategy of this CreateRestoreInstanceRequestBody.
        :rtype: :class:`g42cloudsdkrds.v3.BackupStrategy`
        """
        return self._backup_strategy

    @backup_strategy.setter
    def backup_strategy(self, backup_strategy):
        """Sets the backup_strategy of this CreateRestoreInstanceRequestBody.

        :param backup_strategy: The backup_strategy of this CreateRestoreInstanceRequestBody.
        :type backup_strategy: :class:`g42cloudsdkrds.v3.BackupStrategy`
        """
        self._backup_strategy = backup_strategy

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateRestoreInstanceRequestBody.

        :return: The enterprise_project_id of this CreateRestoreInstanceRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateRestoreInstanceRequestBody.

        :param enterprise_project_id: The enterprise_project_id of this CreateRestoreInstanceRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def disk_encryption_id(self):
        """Gets the disk_encryption_id of this CreateRestoreInstanceRequestBody.

        :return: The disk_encryption_id of this CreateRestoreInstanceRequestBody.
        :rtype: str
        """
        return self._disk_encryption_id

    @disk_encryption_id.setter
    def disk_encryption_id(self, disk_encryption_id):
        """Sets the disk_encryption_id of this CreateRestoreInstanceRequestBody.

        :param disk_encryption_id: The disk_encryption_id of this CreateRestoreInstanceRequestBody.
        :type disk_encryption_id: str
        """
        self._disk_encryption_id = disk_encryption_id

    @property
    def flavor_ref(self):
        """Gets the flavor_ref of this CreateRestoreInstanceRequestBody.

        :return: The flavor_ref of this CreateRestoreInstanceRequestBody.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        """Sets the flavor_ref of this CreateRestoreInstanceRequestBody.

        :param flavor_ref: The flavor_ref of this CreateRestoreInstanceRequestBody.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def volume(self):
        """Gets the volume of this CreateRestoreInstanceRequestBody.

        :return: The volume of this CreateRestoreInstanceRequestBody.
        :rtype: :class:`g42cloudsdkrds.v3.Volume`
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this CreateRestoreInstanceRequestBody.

        :param volume: The volume of this CreateRestoreInstanceRequestBody.
        :type volume: :class:`g42cloudsdkrds.v3.Volume`
        """
        self._volume = volume

    @property
    def region(self):
        """Gets the region of this CreateRestoreInstanceRequestBody.

        :return: The region of this CreateRestoreInstanceRequestBody.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this CreateRestoreInstanceRequestBody.

        :param region: The region of this CreateRestoreInstanceRequestBody.
        :type region: str
        """
        self._region = region

    @property
    def availability_zone(self):
        """Gets the availability_zone of this CreateRestoreInstanceRequestBody.

        :return: The availability_zone of this CreateRestoreInstanceRequestBody.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this CreateRestoreInstanceRequestBody.

        :param availability_zone: The availability_zone of this CreateRestoreInstanceRequestBody.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def vpc_id(self):
        """Gets the vpc_id of this CreateRestoreInstanceRequestBody.

        :return: The vpc_id of this CreateRestoreInstanceRequestBody.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this CreateRestoreInstanceRequestBody.

        :param vpc_id: The vpc_id of this CreateRestoreInstanceRequestBody.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this CreateRestoreInstanceRequestBody.

        :return: The subnet_id of this CreateRestoreInstanceRequestBody.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this CreateRestoreInstanceRequestBody.

        :param subnet_id: The subnet_id of this CreateRestoreInstanceRequestBody.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def data_vip(self):
        """Gets the data_vip of this CreateRestoreInstanceRequestBody.

        :return: The data_vip of this CreateRestoreInstanceRequestBody.
        :rtype: str
        """
        return self._data_vip

    @data_vip.setter
    def data_vip(self, data_vip):
        """Sets the data_vip of this CreateRestoreInstanceRequestBody.

        :param data_vip: The data_vip of this CreateRestoreInstanceRequestBody.
        :type data_vip: str
        """
        self._data_vip = data_vip

    @property
    def security_group_id(self):
        """Gets the security_group_id of this CreateRestoreInstanceRequestBody.

        :return: The security_group_id of this CreateRestoreInstanceRequestBody.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this CreateRestoreInstanceRequestBody.

        :param security_group_id: The security_group_id of this CreateRestoreInstanceRequestBody.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def charge_info(self):
        """Gets the charge_info of this CreateRestoreInstanceRequestBody.

        :return: The charge_info of this CreateRestoreInstanceRequestBody.
        :rtype: :class:`g42cloudsdkrds.v3.ChargeInfo`
        """
        return self._charge_info

    @charge_info.setter
    def charge_info(self, charge_info):
        """Sets the charge_info of this CreateRestoreInstanceRequestBody.

        :param charge_info: The charge_info of this CreateRestoreInstanceRequestBody.
        :type charge_info: :class:`g42cloudsdkrds.v3.ChargeInfo`
        """
        self._charge_info = charge_info

    @property
    def time_zone(self):
        """Gets the time_zone of this CreateRestoreInstanceRequestBody.

        :return: The time_zone of this CreateRestoreInstanceRequestBody.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this CreateRestoreInstanceRequestBody.

        :param time_zone: The time_zone of this CreateRestoreInstanceRequestBody.
        :type time_zone: str
        """
        self._time_zone = time_zone

    @property
    def dsspool_id(self):
        """Gets the dsspool_id of this CreateRestoreInstanceRequestBody.

        :return: The dsspool_id of this CreateRestoreInstanceRequestBody.
        :rtype: str
        """
        return self._dsspool_id

    @dsspool_id.setter
    def dsspool_id(self, dsspool_id):
        """Sets the dsspool_id of this CreateRestoreInstanceRequestBody.

        :param dsspool_id: The dsspool_id of this CreateRestoreInstanceRequestBody.
        :type dsspool_id: str
        """
        self._dsspool_id = dsspool_id

    @property
    def replica_of_id(self):
        """Gets the replica_of_id of this CreateRestoreInstanceRequestBody.

        :return: The replica_of_id of this CreateRestoreInstanceRequestBody.
        :rtype: str
        """
        return self._replica_of_id

    @replica_of_id.setter
    def replica_of_id(self, replica_of_id):
        """Sets the replica_of_id of this CreateRestoreInstanceRequestBody.

        :param replica_of_id: The replica_of_id of this CreateRestoreInstanceRequestBody.
        :type replica_of_id: str
        """
        self._replica_of_id = replica_of_id

    @property
    def restore_point(self):
        """Gets the restore_point of this CreateRestoreInstanceRequestBody.

        :return: The restore_point of this CreateRestoreInstanceRequestBody.
        :rtype: :class:`g42cloudsdkrds.v3.RestorePoint`
        """
        return self._restore_point

    @restore_point.setter
    def restore_point(self, restore_point):
        """Sets the restore_point of this CreateRestoreInstanceRequestBody.

        :param restore_point: The restore_point of this CreateRestoreInstanceRequestBody.
        :type restore_point: :class:`g42cloudsdkrds.v3.RestorePoint`
        """
        self._restore_point = restore_point

    @property
    def collation(self):
        """Gets the collation of this CreateRestoreInstanceRequestBody.

        :return: The collation of this CreateRestoreInstanceRequestBody.
        :rtype: str
        """
        return self._collation

    @collation.setter
    def collation(self, collation):
        """Sets the collation of this CreateRestoreInstanceRequestBody.

        :param collation: The collation of this CreateRestoreInstanceRequestBody.
        :type collation: str
        """
        self._collation = collation

    @property
    def tags(self):
        """Gets the tags of this CreateRestoreInstanceRequestBody.

        :return: The tags of this CreateRestoreInstanceRequestBody.
        :rtype: list[:class:`g42cloudsdkrds.v3.TagWithKeyValue`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateRestoreInstanceRequestBody.

        :param tags: The tags of this CreateRestoreInstanceRequestBody.
        :type tags: list[:class:`g42cloudsdkrds.v3.TagWithKeyValue`]
        """
        self._tags = tags

    @property
    def unchangeable_param(self):
        """Gets the unchangeable_param of this CreateRestoreInstanceRequestBody.

        :return: The unchangeable_param of this CreateRestoreInstanceRequestBody.
        :rtype: :class:`g42cloudsdkrds.v3.UnchangeableParam`
        """
        return self._unchangeable_param

    @unchangeable_param.setter
    def unchangeable_param(self, unchangeable_param):
        """Sets the unchangeable_param of this CreateRestoreInstanceRequestBody.

        :param unchangeable_param: The unchangeable_param of this CreateRestoreInstanceRequestBody.
        :type unchangeable_param: :class:`g42cloudsdkrds.v3.UnchangeableParam`
        """
        self._unchangeable_param = unchangeable_param

    @property
    def dry_run(self):
        """Gets the dry_run of this CreateRestoreInstanceRequestBody.

        :return: The dry_run of this CreateRestoreInstanceRequestBody.
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        """Sets the dry_run of this CreateRestoreInstanceRequestBody.

        :param dry_run: The dry_run of this CreateRestoreInstanceRequestBody.
        :type dry_run: bool
        """
        self._dry_run = dry_run

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
        if not isinstance(other, CreateRestoreInstanceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
