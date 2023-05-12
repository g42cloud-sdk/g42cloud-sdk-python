# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateHealthMonitorOption:

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
        'max_retries': 'int',
        'max_retries_down': 'int',
        'monitor_port': 'int',
        'name': 'str',
        'timeout': 'int',
        'url_path': 'str',
        'type': 'str'
    }

    attribute_map = {
        'admin_state_up': 'admin_state_up',
        'delay': 'delay',
        'domain_name': 'domain_name',
        'expected_codes': 'expected_codes',
        'http_method': 'http_method',
        'max_retries': 'max_retries',
        'max_retries_down': 'max_retries_down',
        'monitor_port': 'monitor_port',
        'name': 'name',
        'timeout': 'timeout',
        'url_path': 'url_path',
        'type': 'type'
    }

    def __init__(self, admin_state_up=None, delay=None, domain_name=None, expected_codes=None, http_method=None, max_retries=None, max_retries_down=None, monitor_port=None, name=None, timeout=None, url_path=None, type=None):
        """UpdateHealthMonitorOption

        The model defined in g42cloud sdk

        :param admin_state_up: The param of the UpdateHealthMonitorOption
        :type admin_state_up: bool
        :param delay: The param of the UpdateHealthMonitorOption
        :type delay: int
        :param domain_name: The param of the UpdateHealthMonitorOption
        :type domain_name: str
        :param expected_codes: The param of the UpdateHealthMonitorOption
        :type expected_codes: str
        :param http_method: The param of the UpdateHealthMonitorOption
        :type http_method: str
        :param max_retries: The param of the UpdateHealthMonitorOption
        :type max_retries: int
        :param max_retries_down: The param of the UpdateHealthMonitorOption
        :type max_retries_down: int
        :param monitor_port: The param of the UpdateHealthMonitorOption
        :type monitor_port: int
        :param name: The param of the UpdateHealthMonitorOption
        :type name: str
        :param timeout: The param of the UpdateHealthMonitorOption
        :type timeout: int
        :param url_path: The param of the UpdateHealthMonitorOption
        :type url_path: str
        :param type: The param of the UpdateHealthMonitorOption
        :type type: str
        """
        
        

        self._admin_state_up = None
        self._delay = None
        self._domain_name = None
        self._expected_codes = None
        self._http_method = None
        self._max_retries = None
        self._max_retries_down = None
        self._monitor_port = None
        self._name = None
        self._timeout = None
        self._url_path = None
        self._type = None
        self.discriminator = None

        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if delay is not None:
            self.delay = delay
        if domain_name is not None:
            self.domain_name = domain_name
        if expected_codes is not None:
            self.expected_codes = expected_codes
        if http_method is not None:
            self.http_method = http_method
        if max_retries is not None:
            self.max_retries = max_retries
        if max_retries_down is not None:
            self.max_retries_down = max_retries_down
        if monitor_port is not None:
            self.monitor_port = monitor_port
        if name is not None:
            self.name = name
        if timeout is not None:
            self.timeout = timeout
        if url_path is not None:
            self.url_path = url_path
        if type is not None:
            self.type = type

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this UpdateHealthMonitorOption.

        :return: The admin_state_up of this UpdateHealthMonitorOption.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this UpdateHealthMonitorOption.

        :param admin_state_up: The admin_state_up of this UpdateHealthMonitorOption.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def delay(self):
        """Gets the delay of this UpdateHealthMonitorOption.

        :return: The delay of this UpdateHealthMonitorOption.
        :rtype: int
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        """Sets the delay of this UpdateHealthMonitorOption.

        :param delay: The delay of this UpdateHealthMonitorOption.
        :type delay: int
        """
        self._delay = delay

    @property
    def domain_name(self):
        """Gets the domain_name of this UpdateHealthMonitorOption.

        :return: The domain_name of this UpdateHealthMonitorOption.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this UpdateHealthMonitorOption.

        :param domain_name: The domain_name of this UpdateHealthMonitorOption.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def expected_codes(self):
        """Gets the expected_codes of this UpdateHealthMonitorOption.

        :return: The expected_codes of this UpdateHealthMonitorOption.
        :rtype: str
        """
        return self._expected_codes

    @expected_codes.setter
    def expected_codes(self, expected_codes):
        """Sets the expected_codes of this UpdateHealthMonitorOption.

        :param expected_codes: The expected_codes of this UpdateHealthMonitorOption.
        :type expected_codes: str
        """
        self._expected_codes = expected_codes

    @property
    def http_method(self):
        """Gets the http_method of this UpdateHealthMonitorOption.

        :return: The http_method of this UpdateHealthMonitorOption.
        :rtype: str
        """
        return self._http_method

    @http_method.setter
    def http_method(self, http_method):
        """Sets the http_method of this UpdateHealthMonitorOption.

        :param http_method: The http_method of this UpdateHealthMonitorOption.
        :type http_method: str
        """
        self._http_method = http_method

    @property
    def max_retries(self):
        """Gets the max_retries of this UpdateHealthMonitorOption.

        :return: The max_retries of this UpdateHealthMonitorOption.
        :rtype: int
        """
        return self._max_retries

    @max_retries.setter
    def max_retries(self, max_retries):
        """Sets the max_retries of this UpdateHealthMonitorOption.

        :param max_retries: The max_retries of this UpdateHealthMonitorOption.
        :type max_retries: int
        """
        self._max_retries = max_retries

    @property
    def max_retries_down(self):
        """Gets the max_retries_down of this UpdateHealthMonitorOption.

        :return: The max_retries_down of this UpdateHealthMonitorOption.
        :rtype: int
        """
        return self._max_retries_down

    @max_retries_down.setter
    def max_retries_down(self, max_retries_down):
        """Sets the max_retries_down of this UpdateHealthMonitorOption.

        :param max_retries_down: The max_retries_down of this UpdateHealthMonitorOption.
        :type max_retries_down: int
        """
        self._max_retries_down = max_retries_down

    @property
    def monitor_port(self):
        """Gets the monitor_port of this UpdateHealthMonitorOption.

        :return: The monitor_port of this UpdateHealthMonitorOption.
        :rtype: int
        """
        return self._monitor_port

    @monitor_port.setter
    def monitor_port(self, monitor_port):
        """Sets the monitor_port of this UpdateHealthMonitorOption.

        :param monitor_port: The monitor_port of this UpdateHealthMonitorOption.
        :type monitor_port: int
        """
        self._monitor_port = monitor_port

    @property
    def name(self):
        """Gets the name of this UpdateHealthMonitorOption.

        :return: The name of this UpdateHealthMonitorOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateHealthMonitorOption.

        :param name: The name of this UpdateHealthMonitorOption.
        :type name: str
        """
        self._name = name

    @property
    def timeout(self):
        """Gets the timeout of this UpdateHealthMonitorOption.

        :return: The timeout of this UpdateHealthMonitorOption.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this UpdateHealthMonitorOption.

        :param timeout: The timeout of this UpdateHealthMonitorOption.
        :type timeout: int
        """
        self._timeout = timeout

    @property
    def url_path(self):
        """Gets the url_path of this UpdateHealthMonitorOption.

        :return: The url_path of this UpdateHealthMonitorOption.
        :rtype: str
        """
        return self._url_path

    @url_path.setter
    def url_path(self, url_path):
        """Sets the url_path of this UpdateHealthMonitorOption.

        :param url_path: The url_path of this UpdateHealthMonitorOption.
        :type url_path: str
        """
        self._url_path = url_path

    @property
    def type(self):
        """Gets the type of this UpdateHealthMonitorOption.

        :return: The type of this UpdateHealthMonitorOption.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UpdateHealthMonitorOption.

        :param type: The type of this UpdateHealthMonitorOption.
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
        if not isinstance(other, UpdateHealthMonitorOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
