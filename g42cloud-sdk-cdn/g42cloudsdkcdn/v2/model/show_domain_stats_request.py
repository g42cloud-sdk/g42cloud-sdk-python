# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDomainStatsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'domain_name': 'str',
        'stat_type': 'str',
        'interval': 'int',
        'group_by': 'str',
        'service_area': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'action': 'action',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'domain_name': 'domain_name',
        'stat_type': 'stat_type',
        'interval': 'interval',
        'group_by': 'group_by',
        'service_area': 'service_area',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, action=None, start_time=None, end_time=None, domain_name=None, stat_type=None, interval=None, group_by=None, service_area=None, enterprise_project_id=None):
        """ShowDomainStatsRequest

        The model defined in g42cloud sdk

        :param action: The param of the ShowDomainStatsRequest
        :type action: str
        :param start_time: The param of the ShowDomainStatsRequest
        :type start_time: int
        :param end_time: The param of the ShowDomainStatsRequest
        :type end_time: int
        :param domain_name: The param of the ShowDomainStatsRequest
        :type domain_name: str
        :param stat_type: The param of the ShowDomainStatsRequest
        :type stat_type: str
        :param interval: The param of the ShowDomainStatsRequest
        :type interval: int
        :param group_by: The param of the ShowDomainStatsRequest
        :type group_by: str
        :param service_area: The param of the ShowDomainStatsRequest
        :type service_area: str
        :param enterprise_project_id: The param of the ShowDomainStatsRequest
        :type enterprise_project_id: str
        """
        
        

        self._action = None
        self._start_time = None
        self._end_time = None
        self._domain_name = None
        self._stat_type = None
        self._interval = None
        self._group_by = None
        self._service_area = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.action = action
        self.start_time = start_time
        self.end_time = end_time
        self.domain_name = domain_name
        self.stat_type = stat_type
        if interval is not None:
            self.interval = interval
        if group_by is not None:
            self.group_by = group_by
        if service_area is not None:
            self.service_area = service_area
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def action(self):
        """Gets the action of this ShowDomainStatsRequest.

        :return: The action of this ShowDomainStatsRequest.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ShowDomainStatsRequest.

        :param action: The action of this ShowDomainStatsRequest.
        :type action: str
        """
        self._action = action

    @property
    def start_time(self):
        """Gets the start_time of this ShowDomainStatsRequest.

        :return: The start_time of this ShowDomainStatsRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowDomainStatsRequest.

        :param start_time: The start_time of this ShowDomainStatsRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowDomainStatsRequest.

        :return: The end_time of this ShowDomainStatsRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowDomainStatsRequest.

        :param end_time: The end_time of this ShowDomainStatsRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def domain_name(self):
        """Gets the domain_name of this ShowDomainStatsRequest.

        :return: The domain_name of this ShowDomainStatsRequest.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this ShowDomainStatsRequest.

        :param domain_name: The domain_name of this ShowDomainStatsRequest.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def stat_type(self):
        """Gets the stat_type of this ShowDomainStatsRequest.

        :return: The stat_type of this ShowDomainStatsRequest.
        :rtype: str
        """
        return self._stat_type

    @stat_type.setter
    def stat_type(self, stat_type):
        """Sets the stat_type of this ShowDomainStatsRequest.

        :param stat_type: The stat_type of this ShowDomainStatsRequest.
        :type stat_type: str
        """
        self._stat_type = stat_type

    @property
    def interval(self):
        """Gets the interval of this ShowDomainStatsRequest.

        :return: The interval of this ShowDomainStatsRequest.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this ShowDomainStatsRequest.

        :param interval: The interval of this ShowDomainStatsRequest.
        :type interval: int
        """
        self._interval = interval

    @property
    def group_by(self):
        """Gets the group_by of this ShowDomainStatsRequest.

        :return: The group_by of this ShowDomainStatsRequest.
        :rtype: str
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        """Sets the group_by of this ShowDomainStatsRequest.

        :param group_by: The group_by of this ShowDomainStatsRequest.
        :type group_by: str
        """
        self._group_by = group_by

    @property
    def service_area(self):
        """Gets the service_area of this ShowDomainStatsRequest.

        :return: The service_area of this ShowDomainStatsRequest.
        :rtype: str
        """
        return self._service_area

    @service_area.setter
    def service_area(self, service_area):
        """Sets the service_area of this ShowDomainStatsRequest.

        :param service_area: The service_area of this ShowDomainStatsRequest.
        :type service_area: str
        """
        self._service_area = service_area

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ShowDomainStatsRequest.

        :return: The enterprise_project_id of this ShowDomainStatsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ShowDomainStatsRequest.

        :param enterprise_project_id: The enterprise_project_id of this ShowDomainStatsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ShowDomainStatsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
