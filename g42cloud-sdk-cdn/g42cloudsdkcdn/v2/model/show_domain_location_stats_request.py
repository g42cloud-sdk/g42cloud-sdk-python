# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDomainLocationStatsRequest:

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
        'country': 'str',
        'province': 'str',
        'isp': 'str',
        'group_by': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'action': 'action',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'domain_name': 'domain_name',
        'stat_type': 'stat_type',
        'interval': 'interval',
        'country': 'country',
        'province': 'province',
        'isp': 'isp',
        'group_by': 'group_by',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, action=None, start_time=None, end_time=None, domain_name=None, stat_type=None, interval=None, country=None, province=None, isp=None, group_by=None, enterprise_project_id=None):
        """ShowDomainLocationStatsRequest

        The model defined in g42cloud sdk

        :param action: The param of the ShowDomainLocationStatsRequest
        :type action: str
        :param start_time: The param of the ShowDomainLocationStatsRequest
        :type start_time: int
        :param end_time: The param of the ShowDomainLocationStatsRequest
        :type end_time: int
        :param domain_name: The param of the ShowDomainLocationStatsRequest
        :type domain_name: str
        :param stat_type: The param of the ShowDomainLocationStatsRequest
        :type stat_type: str
        :param interval: The param of the ShowDomainLocationStatsRequest
        :type interval: int
        :param country: The param of the ShowDomainLocationStatsRequest
        :type country: str
        :param province: The param of the ShowDomainLocationStatsRequest
        :type province: str
        :param isp: The param of the ShowDomainLocationStatsRequest
        :type isp: str
        :param group_by: The param of the ShowDomainLocationStatsRequest
        :type group_by: str
        :param enterprise_project_id: The param of the ShowDomainLocationStatsRequest
        :type enterprise_project_id: str
        """
        
        

        self._action = None
        self._start_time = None
        self._end_time = None
        self._domain_name = None
        self._stat_type = None
        self._interval = None
        self._country = None
        self._province = None
        self._isp = None
        self._group_by = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.action = action
        self.start_time = start_time
        self.end_time = end_time
        self.domain_name = domain_name
        self.stat_type = stat_type
        if interval is not None:
            self.interval = interval
        if country is not None:
            self.country = country
        if province is not None:
            self.province = province
        if isp is not None:
            self.isp = isp
        if group_by is not None:
            self.group_by = group_by
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def action(self):
        """Gets the action of this ShowDomainLocationStatsRequest.

        :return: The action of this ShowDomainLocationStatsRequest.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ShowDomainLocationStatsRequest.

        :param action: The action of this ShowDomainLocationStatsRequest.
        :type action: str
        """
        self._action = action

    @property
    def start_time(self):
        """Gets the start_time of this ShowDomainLocationStatsRequest.

        :return: The start_time of this ShowDomainLocationStatsRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowDomainLocationStatsRequest.

        :param start_time: The start_time of this ShowDomainLocationStatsRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowDomainLocationStatsRequest.

        :return: The end_time of this ShowDomainLocationStatsRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowDomainLocationStatsRequest.

        :param end_time: The end_time of this ShowDomainLocationStatsRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def domain_name(self):
        """Gets the domain_name of this ShowDomainLocationStatsRequest.

        :return: The domain_name of this ShowDomainLocationStatsRequest.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this ShowDomainLocationStatsRequest.

        :param domain_name: The domain_name of this ShowDomainLocationStatsRequest.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def stat_type(self):
        """Gets the stat_type of this ShowDomainLocationStatsRequest.

        :return: The stat_type of this ShowDomainLocationStatsRequest.
        :rtype: str
        """
        return self._stat_type

    @stat_type.setter
    def stat_type(self, stat_type):
        """Sets the stat_type of this ShowDomainLocationStatsRequest.

        :param stat_type: The stat_type of this ShowDomainLocationStatsRequest.
        :type stat_type: str
        """
        self._stat_type = stat_type

    @property
    def interval(self):
        """Gets the interval of this ShowDomainLocationStatsRequest.

        :return: The interval of this ShowDomainLocationStatsRequest.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this ShowDomainLocationStatsRequest.

        :param interval: The interval of this ShowDomainLocationStatsRequest.
        :type interval: int
        """
        self._interval = interval

    @property
    def country(self):
        """Gets the country of this ShowDomainLocationStatsRequest.

        :return: The country of this ShowDomainLocationStatsRequest.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this ShowDomainLocationStatsRequest.

        :param country: The country of this ShowDomainLocationStatsRequest.
        :type country: str
        """
        self._country = country

    @property
    def province(self):
        """Gets the province of this ShowDomainLocationStatsRequest.

        :return: The province of this ShowDomainLocationStatsRequest.
        :rtype: str
        """
        return self._province

    @province.setter
    def province(self, province):
        """Sets the province of this ShowDomainLocationStatsRequest.

        :param province: The province of this ShowDomainLocationStatsRequest.
        :type province: str
        """
        self._province = province

    @property
    def isp(self):
        """Gets the isp of this ShowDomainLocationStatsRequest.

        :return: The isp of this ShowDomainLocationStatsRequest.
        :rtype: str
        """
        return self._isp

    @isp.setter
    def isp(self, isp):
        """Sets the isp of this ShowDomainLocationStatsRequest.

        :param isp: The isp of this ShowDomainLocationStatsRequest.
        :type isp: str
        """
        self._isp = isp

    @property
    def group_by(self):
        """Gets the group_by of this ShowDomainLocationStatsRequest.

        :return: The group_by of this ShowDomainLocationStatsRequest.
        :rtype: str
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        """Sets the group_by of this ShowDomainLocationStatsRequest.

        :param group_by: The group_by of this ShowDomainLocationStatsRequest.
        :type group_by: str
        """
        self._group_by = group_by

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ShowDomainLocationStatsRequest.

        :return: The enterprise_project_id of this ShowDomainLocationStatsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ShowDomainLocationStatsRequest.

        :param enterprise_project_id: The enterprise_project_id of this ShowDomainLocationStatsRequest.
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
        if not isinstance(other, ShowDomainLocationStatsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
