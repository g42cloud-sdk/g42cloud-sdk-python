# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class Pool:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'admin_state_up': 'bool',
        'description': 'str',
        'healthmonitor_id': 'str',
        'id': 'str',
        'lb_algorithm': 'str',
        'listeners': 'list[ListenerRef]',
        'loadbalancers': 'list[LoadBalancerRef]',
        'members': 'list[MemberRef]',
        'name': 'str',
        'project_id': 'str',
        'protocol': 'str',
        'session_persistence': 'SessionPersistence',
        'ip_version': 'str',
        'slow_start': 'SlowStart',
        'member_deletion_protection_enable': 'bool',
        'created_at': 'str',
        'updated_at': 'str',
        'vpc_id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'admin_state_up': 'admin_state_up',
        'description': 'description',
        'healthmonitor_id': 'healthmonitor_id',
        'id': 'id',
        'lb_algorithm': 'lb_algorithm',
        'listeners': 'listeners',
        'loadbalancers': 'loadbalancers',
        'members': 'members',
        'name': 'name',
        'project_id': 'project_id',
        'protocol': 'protocol',
        'session_persistence': 'session_persistence',
        'ip_version': 'ip_version',
        'slow_start': 'slow_start',
        'member_deletion_protection_enable': 'member_deletion_protection_enable',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'vpc_id': 'vpc_id',
        'type': 'type'
    }

    def __init__(self, admin_state_up=None, description=None, healthmonitor_id=None, id=None, lb_algorithm=None, listeners=None, loadbalancers=None, members=None, name=None, project_id=None, protocol=None, session_persistence=None, ip_version=None, slow_start=None, member_deletion_protection_enable=None, created_at=None, updated_at=None, vpc_id=None, type=None):
        """Pool

        The model defined in g42cloud sdk

        :param admin_state_up: The param of the Pool
        :type admin_state_up: bool
        :param description: The param of the Pool
        :type description: str
        :param healthmonitor_id: The param of the Pool
        :type healthmonitor_id: str
        :param id: The param of the Pool
        :type id: str
        :param lb_algorithm: The param of the Pool
        :type lb_algorithm: str
        :param listeners: The param of the Pool
        :type listeners: list[:class:`g42cloudsdkelb.v3.ListenerRef`]
        :param loadbalancers: The param of the Pool
        :type loadbalancers: list[:class:`g42cloudsdkelb.v3.LoadBalancerRef`]
        :param members: The param of the Pool
        :type members: list[:class:`g42cloudsdkelb.v3.MemberRef`]
        :param name: The param of the Pool
        :type name: str
        :param project_id: The param of the Pool
        :type project_id: str
        :param protocol: The param of the Pool
        :type protocol: str
        :param session_persistence: The param of the Pool
        :type session_persistence: :class:`g42cloudsdkelb.v3.SessionPersistence`
        :param ip_version: The param of the Pool
        :type ip_version: str
        :param slow_start: The param of the Pool
        :type slow_start: :class:`g42cloudsdkelb.v3.SlowStart`
        :param member_deletion_protection_enable: The param of the Pool
        :type member_deletion_protection_enable: bool
        :param created_at: The param of the Pool
        :type created_at: str
        :param updated_at: The param of the Pool
        :type updated_at: str
        :param vpc_id: The param of the Pool
        :type vpc_id: str
        :param type: The param of the Pool
        :type type: str
        """
        
        

        self._admin_state_up = None
        self._description = None
        self._healthmonitor_id = None
        self._id = None
        self._lb_algorithm = None
        self._listeners = None
        self._loadbalancers = None
        self._members = None
        self._name = None
        self._project_id = None
        self._protocol = None
        self._session_persistence = None
        self._ip_version = None
        self._slow_start = None
        self._member_deletion_protection_enable = None
        self._created_at = None
        self._updated_at = None
        self._vpc_id = None
        self._type = None
        self.discriminator = None

        self.admin_state_up = admin_state_up
        self.description = description
        self.healthmonitor_id = healthmonitor_id
        self.id = id
        self.lb_algorithm = lb_algorithm
        self.listeners = listeners
        self.loadbalancers = loadbalancers
        self.members = members
        self.name = name
        self.project_id = project_id
        self.protocol = protocol
        self.session_persistence = session_persistence
        self.ip_version = ip_version
        self.slow_start = slow_start
        self.member_deletion_protection_enable = member_deletion_protection_enable
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        self.vpc_id = vpc_id
        self.type = type

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this Pool.

        :return: The admin_state_up of this Pool.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this Pool.

        :param admin_state_up: The admin_state_up of this Pool.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def description(self):
        """Gets the description of this Pool.

        :return: The description of this Pool.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Pool.

        :param description: The description of this Pool.
        :type description: str
        """
        self._description = description

    @property
    def healthmonitor_id(self):
        """Gets the healthmonitor_id of this Pool.

        :return: The healthmonitor_id of this Pool.
        :rtype: str
        """
        return self._healthmonitor_id

    @healthmonitor_id.setter
    def healthmonitor_id(self, healthmonitor_id):
        """Sets the healthmonitor_id of this Pool.

        :param healthmonitor_id: The healthmonitor_id of this Pool.
        :type healthmonitor_id: str
        """
        self._healthmonitor_id = healthmonitor_id

    @property
    def id(self):
        """Gets the id of this Pool.

        :return: The id of this Pool.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Pool.

        :param id: The id of this Pool.
        :type id: str
        """
        self._id = id

    @property
    def lb_algorithm(self):
        """Gets the lb_algorithm of this Pool.

        :return: The lb_algorithm of this Pool.
        :rtype: str
        """
        return self._lb_algorithm

    @lb_algorithm.setter
    def lb_algorithm(self, lb_algorithm):
        """Sets the lb_algorithm of this Pool.

        :param lb_algorithm: The lb_algorithm of this Pool.
        :type lb_algorithm: str
        """
        self._lb_algorithm = lb_algorithm

    @property
    def listeners(self):
        """Gets the listeners of this Pool.

        :return: The listeners of this Pool.
        :rtype: list[:class:`g42cloudsdkelb.v3.ListenerRef`]
        """
        return self._listeners

    @listeners.setter
    def listeners(self, listeners):
        """Sets the listeners of this Pool.

        :param listeners: The listeners of this Pool.
        :type listeners: list[:class:`g42cloudsdkelb.v3.ListenerRef`]
        """
        self._listeners = listeners

    @property
    def loadbalancers(self):
        """Gets the loadbalancers of this Pool.

        :return: The loadbalancers of this Pool.
        :rtype: list[:class:`g42cloudsdkelb.v3.LoadBalancerRef`]
        """
        return self._loadbalancers

    @loadbalancers.setter
    def loadbalancers(self, loadbalancers):
        """Sets the loadbalancers of this Pool.

        :param loadbalancers: The loadbalancers of this Pool.
        :type loadbalancers: list[:class:`g42cloudsdkelb.v3.LoadBalancerRef`]
        """
        self._loadbalancers = loadbalancers

    @property
    def members(self):
        """Gets the members of this Pool.

        :return: The members of this Pool.
        :rtype: list[:class:`g42cloudsdkelb.v3.MemberRef`]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this Pool.

        :param members: The members of this Pool.
        :type members: list[:class:`g42cloudsdkelb.v3.MemberRef`]
        """
        self._members = members

    @property
    def name(self):
        """Gets the name of this Pool.

        :return: The name of this Pool.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Pool.

        :param name: The name of this Pool.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        """Gets the project_id of this Pool.

        :return: The project_id of this Pool.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Pool.

        :param project_id: The project_id of this Pool.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def protocol(self):
        """Gets the protocol of this Pool.

        :return: The protocol of this Pool.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this Pool.

        :param protocol: The protocol of this Pool.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def session_persistence(self):
        """Gets the session_persistence of this Pool.

        :return: The session_persistence of this Pool.
        :rtype: :class:`g42cloudsdkelb.v3.SessionPersistence`
        """
        return self._session_persistence

    @session_persistence.setter
    def session_persistence(self, session_persistence):
        """Sets the session_persistence of this Pool.

        :param session_persistence: The session_persistence of this Pool.
        :type session_persistence: :class:`g42cloudsdkelb.v3.SessionPersistence`
        """
        self._session_persistence = session_persistence

    @property
    def ip_version(self):
        """Gets the ip_version of this Pool.

        :return: The ip_version of this Pool.
        :rtype: str
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this Pool.

        :param ip_version: The ip_version of this Pool.
        :type ip_version: str
        """
        self._ip_version = ip_version

    @property
    def slow_start(self):
        """Gets the slow_start of this Pool.

        :return: The slow_start of this Pool.
        :rtype: :class:`g42cloudsdkelb.v3.SlowStart`
        """
        return self._slow_start

    @slow_start.setter
    def slow_start(self, slow_start):
        """Sets the slow_start of this Pool.

        :param slow_start: The slow_start of this Pool.
        :type slow_start: :class:`g42cloudsdkelb.v3.SlowStart`
        """
        self._slow_start = slow_start

    @property
    def member_deletion_protection_enable(self):
        """Gets the member_deletion_protection_enable of this Pool.

        :return: The member_deletion_protection_enable of this Pool.
        :rtype: bool
        """
        return self._member_deletion_protection_enable

    @member_deletion_protection_enable.setter
    def member_deletion_protection_enable(self, member_deletion_protection_enable):
        """Sets the member_deletion_protection_enable of this Pool.

        :param member_deletion_protection_enable: The member_deletion_protection_enable of this Pool.
        :type member_deletion_protection_enable: bool
        """
        self._member_deletion_protection_enable = member_deletion_protection_enable

    @property
    def created_at(self):
        """Gets the created_at of this Pool.

        :return: The created_at of this Pool.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Pool.

        :param created_at: The created_at of this Pool.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Pool.

        :return: The updated_at of this Pool.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Pool.

        :param updated_at: The updated_at of this Pool.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def vpc_id(self):
        """Gets the vpc_id of this Pool.

        :return: The vpc_id of this Pool.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this Pool.

        :param vpc_id: The vpc_id of this Pool.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def type(self):
        """Gets the type of this Pool.

        :return: The type of this Pool.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Pool.

        :param type: The type of this Pool.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, Pool):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
