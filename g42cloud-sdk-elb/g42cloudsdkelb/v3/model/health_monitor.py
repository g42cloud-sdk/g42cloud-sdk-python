# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class HealthMonitor:

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
        'delay': 'int',
        'domain_name': 'str',
        'expected_codes': 'str',
        'http_method': 'str',
        'id': 'str',
        'max_retries': 'int',
        'max_retries_down': 'int',
        'monitor_port': 'int',
        'name': 'str',
        'pools': 'list[PoolRef]',
        'project_id': 'str',
        'timeout': 'int',
        'type': 'str',
        'url_path': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'admin_state_up': 'admin_state_up',
        'delay': 'delay',
        'domain_name': 'domain_name',
        'expected_codes': 'expected_codes',
        'http_method': 'http_method',
        'id': 'id',
        'max_retries': 'max_retries',
        'max_retries_down': 'max_retries_down',
        'monitor_port': 'monitor_port',
        'name': 'name',
        'pools': 'pools',
        'project_id': 'project_id',
        'timeout': 'timeout',
        'type': 'type',
        'url_path': 'url_path',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, admin_state_up=None, delay=None, domain_name=None, expected_codes=None, http_method=None, id=None, max_retries=None, max_retries_down=None, monitor_port=None, name=None, pools=None, project_id=None, timeout=None, type=None, url_path=None, created_at=None, updated_at=None):
        """HealthMonitor

        The model defined in g42cloud sdk

        :param admin_state_up: The param of the HealthMonitor
        :type admin_state_up: bool
        :param delay: The param of the HealthMonitor
        :type delay: int
        :param domain_name: The param of the HealthMonitor
        :type domain_name: str
        :param expected_codes: The param of the HealthMonitor
        :type expected_codes: str
        :param http_method: The param of the HealthMonitor
        :type http_method: str
        :param id: The param of the HealthMonitor
        :type id: str
        :param max_retries: The param of the HealthMonitor
        :type max_retries: int
        :param max_retries_down: The param of the HealthMonitor
        :type max_retries_down: int
        :param monitor_port: The param of the HealthMonitor
        :type monitor_port: int
        :param name: The param of the HealthMonitor
        :type name: str
        :param pools: The param of the HealthMonitor
        :type pools: list[:class:`g42cloudsdkelb.v3.PoolRef`]
        :param project_id: The param of the HealthMonitor
        :type project_id: str
        :param timeout: The param of the HealthMonitor
        :type timeout: int
        :param type: The param of the HealthMonitor
        :type type: str
        :param url_path: The param of the HealthMonitor
        :type url_path: str
        :param created_at: The param of the HealthMonitor
        :type created_at: str
        :param updated_at: The param of the HealthMonitor
        :type updated_at: str
        """
        
        

        self._admin_state_up = None
        self._delay = None
        self._domain_name = None
        self._expected_codes = None
        self._http_method = None
        self._id = None
        self._max_retries = None
        self._max_retries_down = None
        self._monitor_port = None
        self._name = None
        self._pools = None
        self._project_id = None
        self._timeout = None
        self._type = None
        self._url_path = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.admin_state_up = admin_state_up
        self.delay = delay
        self.domain_name = domain_name
        self.expected_codes = expected_codes
        self.http_method = http_method
        self.id = id
        self.max_retries = max_retries
        self.max_retries_down = max_retries_down
        self.monitor_port = monitor_port
        self.name = name
        self.pools = pools
        self.project_id = project_id
        self.timeout = timeout
        self.type = type
        self.url_path = url_path
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this HealthMonitor.

        :return: The admin_state_up of this HealthMonitor.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this HealthMonitor.

        :param admin_state_up: The admin_state_up of this HealthMonitor.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def delay(self):
        """Gets the delay of this HealthMonitor.

        :return: The delay of this HealthMonitor.
        :rtype: int
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        """Sets the delay of this HealthMonitor.

        :param delay: The delay of this HealthMonitor.
        :type delay: int
        """
        self._delay = delay

    @property
    def domain_name(self):
        """Gets the domain_name of this HealthMonitor.

        :return: The domain_name of this HealthMonitor.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this HealthMonitor.

        :param domain_name: The domain_name of this HealthMonitor.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def expected_codes(self):
        """Gets the expected_codes of this HealthMonitor.

        :return: The expected_codes of this HealthMonitor.
        :rtype: str
        """
        return self._expected_codes

    @expected_codes.setter
    def expected_codes(self, expected_codes):
        """Sets the expected_codes of this HealthMonitor.

        :param expected_codes: The expected_codes of this HealthMonitor.
        :type expected_codes: str
        """
        self._expected_codes = expected_codes

    @property
    def http_method(self):
        """Gets the http_method of this HealthMonitor.

        :return: The http_method of this HealthMonitor.
        :rtype: str
        """
        return self._http_method

    @http_method.setter
    def http_method(self, http_method):
        """Sets the http_method of this HealthMonitor.

        :param http_method: The http_method of this HealthMonitor.
        :type http_method: str
        """
        self._http_method = http_method

    @property
    def id(self):
        """Gets the id of this HealthMonitor.

        :return: The id of this HealthMonitor.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HealthMonitor.

        :param id: The id of this HealthMonitor.
        :type id: str
        """
        self._id = id

    @property
    def max_retries(self):
        """Gets the max_retries of this HealthMonitor.

        :return: The max_retries of this HealthMonitor.
        :rtype: int
        """
        return self._max_retries

    @max_retries.setter
    def max_retries(self, max_retries):
        """Sets the max_retries of this HealthMonitor.

        :param max_retries: The max_retries of this HealthMonitor.
        :type max_retries: int
        """
        self._max_retries = max_retries

    @property
    def max_retries_down(self):
        """Gets the max_retries_down of this HealthMonitor.

        :return: The max_retries_down of this HealthMonitor.
        :rtype: int
        """
        return self._max_retries_down

    @max_retries_down.setter
    def max_retries_down(self, max_retries_down):
        """Sets the max_retries_down of this HealthMonitor.

        :param max_retries_down: The max_retries_down of this HealthMonitor.
        :type max_retries_down: int
        """
        self._max_retries_down = max_retries_down

    @property
    def monitor_port(self):
        """Gets the monitor_port of this HealthMonitor.

        :return: The monitor_port of this HealthMonitor.
        :rtype: int
        """
        return self._monitor_port

    @monitor_port.setter
    def monitor_port(self, monitor_port):
        """Sets the monitor_port of this HealthMonitor.

        :param monitor_port: The monitor_port of this HealthMonitor.
        :type monitor_port: int
        """
        self._monitor_port = monitor_port

    @property
    def name(self):
        """Gets the name of this HealthMonitor.

        :return: The name of this HealthMonitor.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HealthMonitor.

        :param name: The name of this HealthMonitor.
        :type name: str
        """
        self._name = name

    @property
    def pools(self):
        """Gets the pools of this HealthMonitor.

        :return: The pools of this HealthMonitor.
        :rtype: list[:class:`g42cloudsdkelb.v3.PoolRef`]
        """
        return self._pools

    @pools.setter
    def pools(self, pools):
        """Sets the pools of this HealthMonitor.

        :param pools: The pools of this HealthMonitor.
        :type pools: list[:class:`g42cloudsdkelb.v3.PoolRef`]
        """
        self._pools = pools

    @property
    def project_id(self):
        """Gets the project_id of this HealthMonitor.

        :return: The project_id of this HealthMonitor.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this HealthMonitor.

        :param project_id: The project_id of this HealthMonitor.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def timeout(self):
        """Gets the timeout of this HealthMonitor.

        :return: The timeout of this HealthMonitor.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this HealthMonitor.

        :param timeout: The timeout of this HealthMonitor.
        :type timeout: int
        """
        self._timeout = timeout

    @property
    def type(self):
        """Gets the type of this HealthMonitor.

        :return: The type of this HealthMonitor.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this HealthMonitor.

        :param type: The type of this HealthMonitor.
        :type type: str
        """
        self._type = type

    @property
    def url_path(self):
        """Gets the url_path of this HealthMonitor.

        :return: The url_path of this HealthMonitor.
        :rtype: str
        """
        return self._url_path

    @url_path.setter
    def url_path(self, url_path):
        """Sets the url_path of this HealthMonitor.

        :param url_path: The url_path of this HealthMonitor.
        :type url_path: str
        """
        self._url_path = url_path

    @property
    def created_at(self):
        """Gets the created_at of this HealthMonitor.

        :return: The created_at of this HealthMonitor.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this HealthMonitor.

        :param created_at: The created_at of this HealthMonitor.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this HealthMonitor.

        :return: The updated_at of this HealthMonitor.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this HealthMonitor.

        :param updated_at: The updated_at of this HealthMonitor.
        :type updated_at: str
        """
        self._updated_at = updated_at

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
        if not isinstance(other, HealthMonitor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
