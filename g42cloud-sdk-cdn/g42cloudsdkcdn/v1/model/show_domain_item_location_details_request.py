# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDomainItemLocationDetailsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'domain_name': 'str',
        'stat_type': 'str',
        'region': 'str',
        'isp': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'domain_name': 'domain_name',
        'stat_type': 'stat_type',
        'region': 'region',
        'isp': 'isp'
    }

    def __init__(self, enterprise_project_id=None, start_time=None, end_time=None, domain_name=None, stat_type=None, region=None, isp=None):
        """ShowDomainItemLocationDetailsRequest

        The model defined in g42cloud sdk

        :param enterprise_project_id: The param of the ShowDomainItemLocationDetailsRequest
        :type enterprise_project_id: str
        :param start_time: The param of the ShowDomainItemLocationDetailsRequest
        :type start_time: int
        :param end_time: The param of the ShowDomainItemLocationDetailsRequest
        :type end_time: int
        :param domain_name: The param of the ShowDomainItemLocationDetailsRequest
        :type domain_name: str
        :param stat_type: The param of the ShowDomainItemLocationDetailsRequest
        :type stat_type: str
        :param region: The param of the ShowDomainItemLocationDetailsRequest
        :type region: str
        :param isp: The param of the ShowDomainItemLocationDetailsRequest
        :type isp: str
        """
        
        

        self._enterprise_project_id = None
        self._start_time = None
        self._end_time = None
        self._domain_name = None
        self._stat_type = None
        self._region = None
        self._isp = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.start_time = start_time
        self.end_time = end_time
        self.domain_name = domain_name
        self.stat_type = stat_type
        self.region = region
        self.isp = isp

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ShowDomainItemLocationDetailsRequest.

        :return: The enterprise_project_id of this ShowDomainItemLocationDetailsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ShowDomainItemLocationDetailsRequest.

        :param enterprise_project_id: The enterprise_project_id of this ShowDomainItemLocationDetailsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def start_time(self):
        """Gets the start_time of this ShowDomainItemLocationDetailsRequest.

        :return: The start_time of this ShowDomainItemLocationDetailsRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowDomainItemLocationDetailsRequest.

        :param start_time: The start_time of this ShowDomainItemLocationDetailsRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowDomainItemLocationDetailsRequest.

        :return: The end_time of this ShowDomainItemLocationDetailsRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowDomainItemLocationDetailsRequest.

        :param end_time: The end_time of this ShowDomainItemLocationDetailsRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def domain_name(self):
        """Gets the domain_name of this ShowDomainItemLocationDetailsRequest.

        :return: The domain_name of this ShowDomainItemLocationDetailsRequest.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this ShowDomainItemLocationDetailsRequest.

        :param domain_name: The domain_name of this ShowDomainItemLocationDetailsRequest.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def stat_type(self):
        """Gets the stat_type of this ShowDomainItemLocationDetailsRequest.

        :return: The stat_type of this ShowDomainItemLocationDetailsRequest.
        :rtype: str
        """
        return self._stat_type

    @stat_type.setter
    def stat_type(self, stat_type):
        """Sets the stat_type of this ShowDomainItemLocationDetailsRequest.

        :param stat_type: The stat_type of this ShowDomainItemLocationDetailsRequest.
        :type stat_type: str
        """
        self._stat_type = stat_type

    @property
    def region(self):
        """Gets the region of this ShowDomainItemLocationDetailsRequest.

        :return: The region of this ShowDomainItemLocationDetailsRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ShowDomainItemLocationDetailsRequest.

        :param region: The region of this ShowDomainItemLocationDetailsRequest.
        :type region: str
        """
        self._region = region

    @property
    def isp(self):
        """Gets the isp of this ShowDomainItemLocationDetailsRequest.

        :return: The isp of this ShowDomainItemLocationDetailsRequest.
        :rtype: str
        """
        return self._isp

    @isp.setter
    def isp(self, isp):
        """Sets the isp of this ShowDomainItemLocationDetailsRequest.

        :param isp: The isp of this ShowDomainItemLocationDetailsRequest.
        :type isp: str
        """
        self._isp = isp

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
        if not isinstance(other, ShowDomainItemLocationDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
