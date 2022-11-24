# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateInstanceRespItem:

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
        'name': 'str',
        'status': 'str',
        'datastore': 'Datastore',
        'ha': 'Ha',
        'configuration_id': 'str',
        'port': 'str',
        'backup_strategy': 'BackupStrategy',
        'enterprise_project_id': 'str',
        'disk_encryption_id': 'str',
        'flavor_ref': 'str',
        'volume': 'Volume',
        'region': 'str',
        'availability_zone': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'security_group_id': 'str',
        'charge_info': 'ChargeInfo',
        'collation': 'str',
        'restore_point': 'RestorePoint'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'datastore': 'datastore',
        'ha': 'ha',
        'configuration_id': 'configuration_id',
        'port': 'port',
        'backup_strategy': 'backup_strategy',
        'enterprise_project_id': 'enterprise_project_id',
        'disk_encryption_id': 'disk_encryption_id',
        'flavor_ref': 'flavor_ref',
        'volume': 'volume',
        'region': 'region',
        'availability_zone': 'availability_zone',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'security_group_id': 'security_group_id',
        'charge_info': 'charge_info',
        'collation': 'collation',
        'restore_point': 'restore_point'
    }

    def __init__(self, id=None, name=None, status=None, datastore=None, ha=None, configuration_id=None, port=None, backup_strategy=None, enterprise_project_id=None, disk_encryption_id=None, flavor_ref=None, volume=None, region=None, availability_zone=None, vpc_id=None, subnet_id=None, security_group_id=None, charge_info=None, collation=None, restore_point=None):
        """CreateInstanceRespItem

        The model defined in g42cloud sdk

        :param id: The param of the CreateInstanceRespItem
        :type id: str
        :param name: The param of the CreateInstanceRespItem
        :type name: str
        :param status: The param of the CreateInstanceRespItem
        :type status: str
        :param datastore: The param of the CreateInstanceRespItem
        :type datastore: :class:`g42cloudsdkrds.v3.Datastore`
        :param ha: The param of the CreateInstanceRespItem
        :type ha: :class:`g42cloudsdkrds.v3.Ha`
        :param configuration_id: The param of the CreateInstanceRespItem
        :type configuration_id: str
        :param port: The param of the CreateInstanceRespItem
        :type port: str
        :param backup_strategy: The param of the CreateInstanceRespItem
        :type backup_strategy: :class:`g42cloudsdkrds.v3.BackupStrategy`
        :param enterprise_project_id: The param of the CreateInstanceRespItem
        :type enterprise_project_id: str
        :param disk_encryption_id: The param of the CreateInstanceRespItem
        :type disk_encryption_id: str
        :param flavor_ref: The param of the CreateInstanceRespItem
        :type flavor_ref: str
        :param volume: The param of the CreateInstanceRespItem
        :type volume: :class:`g42cloudsdkrds.v3.Volume`
        :param region: The param of the CreateInstanceRespItem
        :type region: str
        :param availability_zone: The param of the CreateInstanceRespItem
        :type availability_zone: str
        :param vpc_id: The param of the CreateInstanceRespItem
        :type vpc_id: str
        :param subnet_id: The param of the CreateInstanceRespItem
        :type subnet_id: str
        :param security_group_id: The param of the CreateInstanceRespItem
        :type security_group_id: str
        :param charge_info: The param of the CreateInstanceRespItem
        :type charge_info: :class:`g42cloudsdkrds.v3.ChargeInfo`
        :param collation: The param of the CreateInstanceRespItem
        :type collation: str
        :param restore_point: The param of the CreateInstanceRespItem
        :type restore_point: :class:`g42cloudsdkrds.v3.RestorePoint`
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._datastore = None
        self._ha = None
        self._configuration_id = None
        self._port = None
        self._backup_strategy = None
        self._enterprise_project_id = None
        self._disk_encryption_id = None
        self._flavor_ref = None
        self._volume = None
        self._region = None
        self._availability_zone = None
        self._vpc_id = None
        self._subnet_id = None
        self._security_group_id = None
        self._charge_info = None
        self._collation = None
        self._restore_point = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if status is not None:
            self.status = status
        self.datastore = datastore
        if ha is not None:
            self.ha = ha
        if configuration_id is not None:
            self.configuration_id = configuration_id
        if port is not None:
            self.port = port
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
        self.security_group_id = security_group_id
        if charge_info is not None:
            self.charge_info = charge_info
        if collation is not None:
            self.collation = collation
        if restore_point is not None:
            self.restore_point = restore_point

    @property
    def id(self):
        """Gets the id of this CreateInstanceRespItem.

        :return: The id of this CreateInstanceRespItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateInstanceRespItem.

        :param id: The id of this CreateInstanceRespItem.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this CreateInstanceRespItem.

        :return: The name of this CreateInstanceRespItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateInstanceRespItem.

        :param name: The name of this CreateInstanceRespItem.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this CreateInstanceRespItem.

        :return: The status of this CreateInstanceRespItem.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateInstanceRespItem.

        :param status: The status of this CreateInstanceRespItem.
        :type status: str
        """
        self._status = status

    @property
    def datastore(self):
        """Gets the datastore of this CreateInstanceRespItem.

        :return: The datastore of this CreateInstanceRespItem.
        :rtype: :class:`g42cloudsdkrds.v3.Datastore`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        """Sets the datastore of this CreateInstanceRespItem.

        :param datastore: The datastore of this CreateInstanceRespItem.
        :type datastore: :class:`g42cloudsdkrds.v3.Datastore`
        """
        self._datastore = datastore

    @property
    def ha(self):
        """Gets the ha of this CreateInstanceRespItem.

        :return: The ha of this CreateInstanceRespItem.
        :rtype: :class:`g42cloudsdkrds.v3.Ha`
        """
        return self._ha

    @ha.setter
    def ha(self, ha):
        """Sets the ha of this CreateInstanceRespItem.

        :param ha: The ha of this CreateInstanceRespItem.
        :type ha: :class:`g42cloudsdkrds.v3.Ha`
        """
        self._ha = ha

    @property
    def configuration_id(self):
        """Gets the configuration_id of this CreateInstanceRespItem.

        :return: The configuration_id of this CreateInstanceRespItem.
        :rtype: str
        """
        return self._configuration_id

    @configuration_id.setter
    def configuration_id(self, configuration_id):
        """Sets the configuration_id of this CreateInstanceRespItem.

        :param configuration_id: The configuration_id of this CreateInstanceRespItem.
        :type configuration_id: str
        """
        self._configuration_id = configuration_id

    @property
    def port(self):
        """Gets the port of this CreateInstanceRespItem.

        :return: The port of this CreateInstanceRespItem.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this CreateInstanceRespItem.

        :param port: The port of this CreateInstanceRespItem.
        :type port: str
        """
        self._port = port

    @property
    def backup_strategy(self):
        """Gets the backup_strategy of this CreateInstanceRespItem.

        :return: The backup_strategy of this CreateInstanceRespItem.
        :rtype: :class:`g42cloudsdkrds.v3.BackupStrategy`
        """
        return self._backup_strategy

    @backup_strategy.setter
    def backup_strategy(self, backup_strategy):
        """Sets the backup_strategy of this CreateInstanceRespItem.

        :param backup_strategy: The backup_strategy of this CreateInstanceRespItem.
        :type backup_strategy: :class:`g42cloudsdkrds.v3.BackupStrategy`
        """
        self._backup_strategy = backup_strategy

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateInstanceRespItem.

        :return: The enterprise_project_id of this CreateInstanceRespItem.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateInstanceRespItem.

        :param enterprise_project_id: The enterprise_project_id of this CreateInstanceRespItem.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def disk_encryption_id(self):
        """Gets the disk_encryption_id of this CreateInstanceRespItem.

        :return: The disk_encryption_id of this CreateInstanceRespItem.
        :rtype: str
        """
        return self._disk_encryption_id

    @disk_encryption_id.setter
    def disk_encryption_id(self, disk_encryption_id):
        """Sets the disk_encryption_id of this CreateInstanceRespItem.

        :param disk_encryption_id: The disk_encryption_id of this CreateInstanceRespItem.
        :type disk_encryption_id: str
        """
        self._disk_encryption_id = disk_encryption_id

    @property
    def flavor_ref(self):
        """Gets the flavor_ref of this CreateInstanceRespItem.

        :return: The flavor_ref of this CreateInstanceRespItem.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        """Sets the flavor_ref of this CreateInstanceRespItem.

        :param flavor_ref: The flavor_ref of this CreateInstanceRespItem.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def volume(self):
        """Gets the volume of this CreateInstanceRespItem.

        :return: The volume of this CreateInstanceRespItem.
        :rtype: :class:`g42cloudsdkrds.v3.Volume`
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this CreateInstanceRespItem.

        :param volume: The volume of this CreateInstanceRespItem.
        :type volume: :class:`g42cloudsdkrds.v3.Volume`
        """
        self._volume = volume

    @property
    def region(self):
        """Gets the region of this CreateInstanceRespItem.

        :return: The region of this CreateInstanceRespItem.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this CreateInstanceRespItem.

        :param region: The region of this CreateInstanceRespItem.
        :type region: str
        """
        self._region = region

    @property
    def availability_zone(self):
        """Gets the availability_zone of this CreateInstanceRespItem.

        :return: The availability_zone of this CreateInstanceRespItem.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this CreateInstanceRespItem.

        :param availability_zone: The availability_zone of this CreateInstanceRespItem.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def vpc_id(self):
        """Gets the vpc_id of this CreateInstanceRespItem.

        :return: The vpc_id of this CreateInstanceRespItem.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this CreateInstanceRespItem.

        :param vpc_id: The vpc_id of this CreateInstanceRespItem.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this CreateInstanceRespItem.

        :return: The subnet_id of this CreateInstanceRespItem.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this CreateInstanceRespItem.

        :param subnet_id: The subnet_id of this CreateInstanceRespItem.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        """Gets the security_group_id of this CreateInstanceRespItem.

        :return: The security_group_id of this CreateInstanceRespItem.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this CreateInstanceRespItem.

        :param security_group_id: The security_group_id of this CreateInstanceRespItem.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def charge_info(self):
        """Gets the charge_info of this CreateInstanceRespItem.

        :return: The charge_info of this CreateInstanceRespItem.
        :rtype: :class:`g42cloudsdkrds.v3.ChargeInfo`
        """
        return self._charge_info

    @charge_info.setter
    def charge_info(self, charge_info):
        """Sets the charge_info of this CreateInstanceRespItem.

        :param charge_info: The charge_info of this CreateInstanceRespItem.
        :type charge_info: :class:`g42cloudsdkrds.v3.ChargeInfo`
        """
        self._charge_info = charge_info

    @property
    def collation(self):
        """Gets the collation of this CreateInstanceRespItem.

        :return: The collation of this CreateInstanceRespItem.
        :rtype: str
        """
        return self._collation

    @collation.setter
    def collation(self, collation):
        """Sets the collation of this CreateInstanceRespItem.

        :param collation: The collation of this CreateInstanceRespItem.
        :type collation: str
        """
        self._collation = collation

    @property
    def restore_point(self):
        """Gets the restore_point of this CreateInstanceRespItem.

        :return: The restore_point of this CreateInstanceRespItem.
        :rtype: :class:`g42cloudsdkrds.v3.RestorePoint`
        """
        return self._restore_point

    @restore_point.setter
    def restore_point(self, restore_point):
        """Sets the restore_point of this CreateInstanceRespItem.

        :param restore_point: The restore_point of this CreateInstanceRespItem.
        :type restore_point: :class:`g42cloudsdkrds.v3.RestorePoint`
        """
        self._restore_point = restore_point

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
        if not isinstance(other, CreateInstanceRespItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
