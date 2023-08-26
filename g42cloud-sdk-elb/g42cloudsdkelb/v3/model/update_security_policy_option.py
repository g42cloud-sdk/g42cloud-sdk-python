# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSecurityPolicyOption:

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
        'description': 'str',
        'protocols': 'list[str]',
        'ciphers': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'protocols': 'protocols',
        'ciphers': 'ciphers'
    }

    def __init__(self, name=None, description=None, protocols=None, ciphers=None):
        """UpdateSecurityPolicyOption

        The model defined in g42cloud sdk

        :param name: The param of the UpdateSecurityPolicyOption
        :type name: str
        :param description: The param of the UpdateSecurityPolicyOption
        :type description: str
        :param protocols: The param of the UpdateSecurityPolicyOption
        :type protocols: list[str]
        :param ciphers: The param of the UpdateSecurityPolicyOption
        :type ciphers: list[str]
        """
        
        

        self._name = None
        self._description = None
        self._protocols = None
        self._ciphers = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if protocols is not None:
            self.protocols = protocols
        if ciphers is not None:
            self.ciphers = ciphers

    @property
    def name(self):
        """Gets the name of this UpdateSecurityPolicyOption.

        :return: The name of this UpdateSecurityPolicyOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateSecurityPolicyOption.

        :param name: The name of this UpdateSecurityPolicyOption.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateSecurityPolicyOption.

        :return: The description of this UpdateSecurityPolicyOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateSecurityPolicyOption.

        :param description: The description of this UpdateSecurityPolicyOption.
        :type description: str
        """
        self._description = description

    @property
    def protocols(self):
        """Gets the protocols of this UpdateSecurityPolicyOption.

        :return: The protocols of this UpdateSecurityPolicyOption.
        :rtype: list[str]
        """
        return self._protocols

    @protocols.setter
    def protocols(self, protocols):
        """Sets the protocols of this UpdateSecurityPolicyOption.

        :param protocols: The protocols of this UpdateSecurityPolicyOption.
        :type protocols: list[str]
        """
        self._protocols = protocols

    @property
    def ciphers(self):
        """Gets the ciphers of this UpdateSecurityPolicyOption.

        :return: The ciphers of this UpdateSecurityPolicyOption.
        :rtype: list[str]
        """
        return self._ciphers

    @ciphers.setter
    def ciphers(self, ciphers):
        """Sets the ciphers of this UpdateSecurityPolicyOption.

        :param ciphers: The ciphers of this UpdateSecurityPolicyOption.
        :type ciphers: list[str]
        """
        self._ciphers = ciphers

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
        if not isinstance(other, UpdateSecurityPolicyOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
