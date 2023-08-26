# coding: utf-8

import six

from g42cloudsdkcore.sdk_response import SdkResponse
from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTaskResponse(SdkResponse):

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
        'type': 'str',
        'os_type': 'str',
        'id': 'str',
        'priority': 'int',
        'speed_limit': 'int',
        'region_id': 'str',
        'start_target_server': 'bool',
        'enterprise_project_id': 'str',
        'migration_ip': 'str',
        'region_name': 'str',
        'project_name': 'str',
        'project_id': 'str',
        'vm_template_id': 'str',
        'source_server': 'SourceServerResponse',
        'target_server': 'TaskTargetServer',
        'state': 'str',
        'estimate_complete_time': 'int',
        'connected': 'bool',
        'create_date': 'int',
        'start_date': 'int',
        'finish_date': 'int',
        'migrate_speed': 'float',
        'compress_rate': 'float',
        'error_json': 'str',
        'total_time': 'int',
        'float_ip': 'str',
        'remain_seconds': 'int',
        'target_snapshot_id': 'str',
        'clone_server': 'CloneServer',
        'sub_tasks': 'list[SubTask]',
        'network_check_info': 'NetworkCheckInfoRequestBody'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'os_type': 'os_type',
        'id': 'id',
        'priority': 'priority',
        'speed_limit': 'speed_limit',
        'region_id': 'region_id',
        'start_target_server': 'start_target_server',
        'enterprise_project_id': 'enterprise_project_id',
        'migration_ip': 'migration_ip',
        'region_name': 'region_name',
        'project_name': 'project_name',
        'project_id': 'project_id',
        'vm_template_id': 'vm_template_id',
        'source_server': 'source_server',
        'target_server': 'target_server',
        'state': 'state',
        'estimate_complete_time': 'estimate_complete_time',
        'connected': 'connected',
        'create_date': 'create_date',
        'start_date': 'start_date',
        'finish_date': 'finish_date',
        'migrate_speed': 'migrate_speed',
        'compress_rate': 'compress_rate',
        'error_json': 'error_json',
        'total_time': 'total_time',
        'float_ip': 'float_ip',
        'remain_seconds': 'remain_seconds',
        'target_snapshot_id': 'target_snapshot_id',
        'clone_server': 'clone_server',
        'sub_tasks': 'sub_tasks',
        'network_check_info': 'network_check_info'
    }

    def __init__(self, name=None, type=None, os_type=None, id=None, priority=None, speed_limit=None, region_id=None, start_target_server=None, enterprise_project_id=None, migration_ip=None, region_name=None, project_name=None, project_id=None, vm_template_id=None, source_server=None, target_server=None, state=None, estimate_complete_time=None, connected=None, create_date=None, start_date=None, finish_date=None, migrate_speed=None, compress_rate=None, error_json=None, total_time=None, float_ip=None, remain_seconds=None, target_snapshot_id=None, clone_server=None, sub_tasks=None, network_check_info=None):
        """ShowTaskResponse

        The model defined in g42cloud sdk

        :param name: The param of the ShowTaskResponse
        :type name: str
        :param type: The param of the ShowTaskResponse
        :type type: str
        :param os_type: The param of the ShowTaskResponse
        :type os_type: str
        :param id: The param of the ShowTaskResponse
        :type id: str
        :param priority: The param of the ShowTaskResponse
        :type priority: int
        :param speed_limit: The param of the ShowTaskResponse
        :type speed_limit: int
        :param region_id: The param of the ShowTaskResponse
        :type region_id: str
        :param start_target_server: The param of the ShowTaskResponse
        :type start_target_server: bool
        :param enterprise_project_id: The param of the ShowTaskResponse
        :type enterprise_project_id: str
        :param migration_ip: The param of the ShowTaskResponse
        :type migration_ip: str
        :param region_name: The param of the ShowTaskResponse
        :type region_name: str
        :param project_name: The param of the ShowTaskResponse
        :type project_name: str
        :param project_id: The param of the ShowTaskResponse
        :type project_id: str
        :param vm_template_id: The param of the ShowTaskResponse
        :type vm_template_id: str
        :param source_server: The param of the ShowTaskResponse
        :type source_server: :class:`g42cloudsdksms.v3.SourceServerResponse`
        :param target_server: The param of the ShowTaskResponse
        :type target_server: :class:`g42cloudsdksms.v3.TaskTargetServer`
        :param state: The param of the ShowTaskResponse
        :type state: str
        :param estimate_complete_time: The param of the ShowTaskResponse
        :type estimate_complete_time: int
        :param connected: The param of the ShowTaskResponse
        :type connected: bool
        :param create_date: The param of the ShowTaskResponse
        :type create_date: int
        :param start_date: The param of the ShowTaskResponse
        :type start_date: int
        :param finish_date: The param of the ShowTaskResponse
        :type finish_date: int
        :param migrate_speed: The param of the ShowTaskResponse
        :type migrate_speed: float
        :param compress_rate: The param of the ShowTaskResponse
        :type compress_rate: float
        :param error_json: The param of the ShowTaskResponse
        :type error_json: str
        :param total_time: The param of the ShowTaskResponse
        :type total_time: int
        :param float_ip: The param of the ShowTaskResponse
        :type float_ip: str
        :param remain_seconds: The param of the ShowTaskResponse
        :type remain_seconds: int
        :param target_snapshot_id: The param of the ShowTaskResponse
        :type target_snapshot_id: str
        :param clone_server: The param of the ShowTaskResponse
        :type clone_server: :class:`g42cloudsdksms.v3.CloneServer`
        :param sub_tasks: The param of the ShowTaskResponse
        :type sub_tasks: list[:class:`g42cloudsdksms.v3.SubTask`]
        :param network_check_info: The param of the ShowTaskResponse
        :type network_check_info: :class:`g42cloudsdksms.v3.NetworkCheckInfoRequestBody`
        """
        
        super(ShowTaskResponse, self).__init__()

        self._name = None
        self._type = None
        self._os_type = None
        self._id = None
        self._priority = None
        self._speed_limit = None
        self._region_id = None
        self._start_target_server = None
        self._enterprise_project_id = None
        self._migration_ip = None
        self._region_name = None
        self._project_name = None
        self._project_id = None
        self._vm_template_id = None
        self._source_server = None
        self._target_server = None
        self._state = None
        self._estimate_complete_time = None
        self._connected = None
        self._create_date = None
        self._start_date = None
        self._finish_date = None
        self._migrate_speed = None
        self._compress_rate = None
        self._error_json = None
        self._total_time = None
        self._float_ip = None
        self._remain_seconds = None
        self._target_snapshot_id = None
        self._clone_server = None
        self._sub_tasks = None
        self._network_check_info = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if os_type is not None:
            self.os_type = os_type
        if id is not None:
            self.id = id
        if priority is not None:
            self.priority = priority
        if speed_limit is not None:
            self.speed_limit = speed_limit
        if region_id is not None:
            self.region_id = region_id
        if start_target_server is not None:
            self.start_target_server = start_target_server
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if migration_ip is not None:
            self.migration_ip = migration_ip
        if region_name is not None:
            self.region_name = region_name
        if project_name is not None:
            self.project_name = project_name
        if project_id is not None:
            self.project_id = project_id
        if vm_template_id is not None:
            self.vm_template_id = vm_template_id
        if source_server is not None:
            self.source_server = source_server
        if target_server is not None:
            self.target_server = target_server
        if state is not None:
            self.state = state
        if estimate_complete_time is not None:
            self.estimate_complete_time = estimate_complete_time
        if connected is not None:
            self.connected = connected
        if create_date is not None:
            self.create_date = create_date
        if start_date is not None:
            self.start_date = start_date
        if finish_date is not None:
            self.finish_date = finish_date
        if migrate_speed is not None:
            self.migrate_speed = migrate_speed
        if compress_rate is not None:
            self.compress_rate = compress_rate
        if error_json is not None:
            self.error_json = error_json
        if total_time is not None:
            self.total_time = total_time
        if float_ip is not None:
            self.float_ip = float_ip
        if remain_seconds is not None:
            self.remain_seconds = remain_seconds
        if target_snapshot_id is not None:
            self.target_snapshot_id = target_snapshot_id
        if clone_server is not None:
            self.clone_server = clone_server
        if sub_tasks is not None:
            self.sub_tasks = sub_tasks
        if network_check_info is not None:
            self.network_check_info = network_check_info

    @property
    def name(self):
        """Gets the name of this ShowTaskResponse.

        :return: The name of this ShowTaskResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowTaskResponse.

        :param name: The name of this ShowTaskResponse.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this ShowTaskResponse.

        :return: The type of this ShowTaskResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowTaskResponse.

        :param type: The type of this ShowTaskResponse.
        :type type: str
        """
        self._type = type

    @property
    def os_type(self):
        """Gets the os_type of this ShowTaskResponse.

        :return: The os_type of this ShowTaskResponse.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this ShowTaskResponse.

        :param os_type: The os_type of this ShowTaskResponse.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def id(self):
        """Gets the id of this ShowTaskResponse.

        :return: The id of this ShowTaskResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowTaskResponse.

        :param id: The id of this ShowTaskResponse.
        :type id: str
        """
        self._id = id

    @property
    def priority(self):
        """Gets the priority of this ShowTaskResponse.

        :return: The priority of this ShowTaskResponse.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this ShowTaskResponse.

        :param priority: The priority of this ShowTaskResponse.
        :type priority: int
        """
        self._priority = priority

    @property
    def speed_limit(self):
        """Gets the speed_limit of this ShowTaskResponse.

        :return: The speed_limit of this ShowTaskResponse.
        :rtype: int
        """
        return self._speed_limit

    @speed_limit.setter
    def speed_limit(self, speed_limit):
        """Sets the speed_limit of this ShowTaskResponse.

        :param speed_limit: The speed_limit of this ShowTaskResponse.
        :type speed_limit: int
        """
        self._speed_limit = speed_limit

    @property
    def region_id(self):
        """Gets the region_id of this ShowTaskResponse.

        :return: The region_id of this ShowTaskResponse.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this ShowTaskResponse.

        :param region_id: The region_id of this ShowTaskResponse.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def start_target_server(self):
        """Gets the start_target_server of this ShowTaskResponse.

        :return: The start_target_server of this ShowTaskResponse.
        :rtype: bool
        """
        return self._start_target_server

    @start_target_server.setter
    def start_target_server(self, start_target_server):
        """Sets the start_target_server of this ShowTaskResponse.

        :param start_target_server: The start_target_server of this ShowTaskResponse.
        :type start_target_server: bool
        """
        self._start_target_server = start_target_server

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ShowTaskResponse.

        :return: The enterprise_project_id of this ShowTaskResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ShowTaskResponse.

        :param enterprise_project_id: The enterprise_project_id of this ShowTaskResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def migration_ip(self):
        """Gets the migration_ip of this ShowTaskResponse.

        :return: The migration_ip of this ShowTaskResponse.
        :rtype: str
        """
        return self._migration_ip

    @migration_ip.setter
    def migration_ip(self, migration_ip):
        """Sets the migration_ip of this ShowTaskResponse.

        :param migration_ip: The migration_ip of this ShowTaskResponse.
        :type migration_ip: str
        """
        self._migration_ip = migration_ip

    @property
    def region_name(self):
        """Gets the region_name of this ShowTaskResponse.

        :return: The region_name of this ShowTaskResponse.
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        """Sets the region_name of this ShowTaskResponse.

        :param region_name: The region_name of this ShowTaskResponse.
        :type region_name: str
        """
        self._region_name = region_name

    @property
    def project_name(self):
        """Gets the project_name of this ShowTaskResponse.

        :return: The project_name of this ShowTaskResponse.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this ShowTaskResponse.

        :param project_name: The project_name of this ShowTaskResponse.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def project_id(self):
        """Gets the project_id of this ShowTaskResponse.

        :return: The project_id of this ShowTaskResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ShowTaskResponse.

        :param project_id: The project_id of this ShowTaskResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def vm_template_id(self):
        """Gets the vm_template_id of this ShowTaskResponse.

        :return: The vm_template_id of this ShowTaskResponse.
        :rtype: str
        """
        return self._vm_template_id

    @vm_template_id.setter
    def vm_template_id(self, vm_template_id):
        """Sets the vm_template_id of this ShowTaskResponse.

        :param vm_template_id: The vm_template_id of this ShowTaskResponse.
        :type vm_template_id: str
        """
        self._vm_template_id = vm_template_id

    @property
    def source_server(self):
        """Gets the source_server of this ShowTaskResponse.

        :return: The source_server of this ShowTaskResponse.
        :rtype: :class:`g42cloudsdksms.v3.SourceServerResponse`
        """
        return self._source_server

    @source_server.setter
    def source_server(self, source_server):
        """Sets the source_server of this ShowTaskResponse.

        :param source_server: The source_server of this ShowTaskResponse.
        :type source_server: :class:`g42cloudsdksms.v3.SourceServerResponse`
        """
        self._source_server = source_server

    @property
    def target_server(self):
        """Gets the target_server of this ShowTaskResponse.

        :return: The target_server of this ShowTaskResponse.
        :rtype: :class:`g42cloudsdksms.v3.TaskTargetServer`
        """
        return self._target_server

    @target_server.setter
    def target_server(self, target_server):
        """Sets the target_server of this ShowTaskResponse.

        :param target_server: The target_server of this ShowTaskResponse.
        :type target_server: :class:`g42cloudsdksms.v3.TaskTargetServer`
        """
        self._target_server = target_server

    @property
    def state(self):
        """Gets the state of this ShowTaskResponse.

        :return: The state of this ShowTaskResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ShowTaskResponse.

        :param state: The state of this ShowTaskResponse.
        :type state: str
        """
        self._state = state

    @property
    def estimate_complete_time(self):
        """Gets the estimate_complete_time of this ShowTaskResponse.

        :return: The estimate_complete_time of this ShowTaskResponse.
        :rtype: int
        """
        return self._estimate_complete_time

    @estimate_complete_time.setter
    def estimate_complete_time(self, estimate_complete_time):
        """Sets the estimate_complete_time of this ShowTaskResponse.

        :param estimate_complete_time: The estimate_complete_time of this ShowTaskResponse.
        :type estimate_complete_time: int
        """
        self._estimate_complete_time = estimate_complete_time

    @property
    def connected(self):
        """Gets the connected of this ShowTaskResponse.

        :return: The connected of this ShowTaskResponse.
        :rtype: bool
        """
        return self._connected

    @connected.setter
    def connected(self, connected):
        """Sets the connected of this ShowTaskResponse.

        :param connected: The connected of this ShowTaskResponse.
        :type connected: bool
        """
        self._connected = connected

    @property
    def create_date(self):
        """Gets the create_date of this ShowTaskResponse.

        :return: The create_date of this ShowTaskResponse.
        :rtype: int
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this ShowTaskResponse.

        :param create_date: The create_date of this ShowTaskResponse.
        :type create_date: int
        """
        self._create_date = create_date

    @property
    def start_date(self):
        """Gets the start_date of this ShowTaskResponse.

        :return: The start_date of this ShowTaskResponse.
        :rtype: int
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ShowTaskResponse.

        :param start_date: The start_date of this ShowTaskResponse.
        :type start_date: int
        """
        self._start_date = start_date

    @property
    def finish_date(self):
        """Gets the finish_date of this ShowTaskResponse.

        :return: The finish_date of this ShowTaskResponse.
        :rtype: int
        """
        return self._finish_date

    @finish_date.setter
    def finish_date(self, finish_date):
        """Sets the finish_date of this ShowTaskResponse.

        :param finish_date: The finish_date of this ShowTaskResponse.
        :type finish_date: int
        """
        self._finish_date = finish_date

    @property
    def migrate_speed(self):
        """Gets the migrate_speed of this ShowTaskResponse.

        :return: The migrate_speed of this ShowTaskResponse.
        :rtype: float
        """
        return self._migrate_speed

    @migrate_speed.setter
    def migrate_speed(self, migrate_speed):
        """Sets the migrate_speed of this ShowTaskResponse.

        :param migrate_speed: The migrate_speed of this ShowTaskResponse.
        :type migrate_speed: float
        """
        self._migrate_speed = migrate_speed

    @property
    def compress_rate(self):
        """Gets the compress_rate of this ShowTaskResponse.

        :return: The compress_rate of this ShowTaskResponse.
        :rtype: float
        """
        return self._compress_rate

    @compress_rate.setter
    def compress_rate(self, compress_rate):
        """Sets the compress_rate of this ShowTaskResponse.

        :param compress_rate: The compress_rate of this ShowTaskResponse.
        :type compress_rate: float
        """
        self._compress_rate = compress_rate

    @property
    def error_json(self):
        """Gets the error_json of this ShowTaskResponse.

        :return: The error_json of this ShowTaskResponse.
        :rtype: str
        """
        return self._error_json

    @error_json.setter
    def error_json(self, error_json):
        """Sets the error_json of this ShowTaskResponse.

        :param error_json: The error_json of this ShowTaskResponse.
        :type error_json: str
        """
        self._error_json = error_json

    @property
    def total_time(self):
        """Gets the total_time of this ShowTaskResponse.

        :return: The total_time of this ShowTaskResponse.
        :rtype: int
        """
        return self._total_time

    @total_time.setter
    def total_time(self, total_time):
        """Sets the total_time of this ShowTaskResponse.

        :param total_time: The total_time of this ShowTaskResponse.
        :type total_time: int
        """
        self._total_time = total_time

    @property
    def float_ip(self):
        """Gets the float_ip of this ShowTaskResponse.

        :return: The float_ip of this ShowTaskResponse.
        :rtype: str
        """
        return self._float_ip

    @float_ip.setter
    def float_ip(self, float_ip):
        """Sets the float_ip of this ShowTaskResponse.

        :param float_ip: The float_ip of this ShowTaskResponse.
        :type float_ip: str
        """
        self._float_ip = float_ip

    @property
    def remain_seconds(self):
        """Gets the remain_seconds of this ShowTaskResponse.

        :return: The remain_seconds of this ShowTaskResponse.
        :rtype: int
        """
        return self._remain_seconds

    @remain_seconds.setter
    def remain_seconds(self, remain_seconds):
        """Sets the remain_seconds of this ShowTaskResponse.

        :param remain_seconds: The remain_seconds of this ShowTaskResponse.
        :type remain_seconds: int
        """
        self._remain_seconds = remain_seconds

    @property
    def target_snapshot_id(self):
        """Gets the target_snapshot_id of this ShowTaskResponse.

        :return: The target_snapshot_id of this ShowTaskResponse.
        :rtype: str
        """
        return self._target_snapshot_id

    @target_snapshot_id.setter
    def target_snapshot_id(self, target_snapshot_id):
        """Sets the target_snapshot_id of this ShowTaskResponse.

        :param target_snapshot_id: The target_snapshot_id of this ShowTaskResponse.
        :type target_snapshot_id: str
        """
        self._target_snapshot_id = target_snapshot_id

    @property
    def clone_server(self):
        """Gets the clone_server of this ShowTaskResponse.

        :return: The clone_server of this ShowTaskResponse.
        :rtype: :class:`g42cloudsdksms.v3.CloneServer`
        """
        return self._clone_server

    @clone_server.setter
    def clone_server(self, clone_server):
        """Sets the clone_server of this ShowTaskResponse.

        :param clone_server: The clone_server of this ShowTaskResponse.
        :type clone_server: :class:`g42cloudsdksms.v3.CloneServer`
        """
        self._clone_server = clone_server

    @property
    def sub_tasks(self):
        """Gets the sub_tasks of this ShowTaskResponse.

        :return: The sub_tasks of this ShowTaskResponse.
        :rtype: list[:class:`g42cloudsdksms.v3.SubTask`]
        """
        return self._sub_tasks

    @sub_tasks.setter
    def sub_tasks(self, sub_tasks):
        """Sets the sub_tasks of this ShowTaskResponse.

        :param sub_tasks: The sub_tasks of this ShowTaskResponse.
        :type sub_tasks: list[:class:`g42cloudsdksms.v3.SubTask`]
        """
        self._sub_tasks = sub_tasks

    @property
    def network_check_info(self):
        """Gets the network_check_info of this ShowTaskResponse.

        :return: The network_check_info of this ShowTaskResponse.
        :rtype: :class:`g42cloudsdksms.v3.NetworkCheckInfoRequestBody`
        """
        return self._network_check_info

    @network_check_info.setter
    def network_check_info(self, network_check_info):
        """Sets the network_check_info of this ShowTaskResponse.

        :param network_check_info: The network_check_info of this ShowTaskResponse.
        :type network_check_info: :class:`g42cloudsdksms.v3.NetworkCheckInfoRequestBody`
        """
        self._network_check_info = network_check_info

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
        if not isinstance(other, ShowTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
