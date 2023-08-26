# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class CdnIps:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ip': 'str',
        'belongs': 'bool',
        'region': 'str',
        'isp': 'str',
        'platform': 'str'
    }

    attribute_map = {
        'ip': 'ip',
        'belongs': 'belongs',
        'region': 'region',
        'isp': 'isp',
        'platform': 'platform'
    }

    def __init__(self, ip=None, belongs=None, region=None, isp=None, platform=None):
        """CdnIps

        The model defined in g42cloud sdk

        :param ip: The param of the CdnIps
        :type ip: str
        :param belongs: The param of the CdnIps
        :type belongs: bool
        :param region: The param of the CdnIps
        :type region: str
        :param isp: The param of the CdnIps
        :type isp: str
        :param platform: The param of the CdnIps
        :type platform: str
        """
        
        

        self._ip = None
        self._belongs = None
        self._region = None
        self._isp = None
        self._platform = None
        self.discriminator = None

        if ip is not None:
            self.ip = ip
        if belongs is not None:
            self.belongs = belongs
        if region is not None:
            self.region = region
        if isp is not None:
            self.isp = isp
        if platform is not None:
            self.platform = platform

    @property
    def ip(self):
        """Gets the ip of this CdnIps.

        :return: The ip of this CdnIps.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this CdnIps.

        :param ip: The ip of this CdnIps.
        :type ip: str
        """
        self._ip = ip

    @property
    def belongs(self):
        """Gets the belongs of this CdnIps.

        :return: The belongs of this CdnIps.
        :rtype: bool
        """
        return self._belongs

    @belongs.setter
    def belongs(self, belongs):
        """Sets the belongs of this CdnIps.

        :param belongs: The belongs of this CdnIps.
        :type belongs: bool
        """
        self._belongs = belongs

    @property
    def region(self):
        """Gets the region of this CdnIps.

        :return: The region of this CdnIps.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this CdnIps.

        :param region: The region of this CdnIps.
        :type region: str
        """
        self._region = region

    @property
    def isp(self):
        """Gets the isp of this CdnIps.

        :return: The isp of this CdnIps.
        :rtype: str
        """
        return self._isp

    @isp.setter
    def isp(self, isp):
        """Sets the isp of this CdnIps.

        :param isp: The isp of this CdnIps.
        :type isp: str
        """
        self._isp = isp

    @property
    def platform(self):
        """Gets the platform of this CdnIps.

        :return: The platform of this CdnIps.
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this CdnIps.

        :param platform: The platform of this CdnIps.
        :type platform: str
        """
        self._platform = platform

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
        if not isinstance(other, CdnIps):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
