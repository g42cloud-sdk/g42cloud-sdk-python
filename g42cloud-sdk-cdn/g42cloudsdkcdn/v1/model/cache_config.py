# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CacheConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ignore_url_parameter': 'bool',
        'follow_origin': 'bool',
        'compress': 'CompressResponse',
        'rules': 'list[Rules]'
    }

    attribute_map = {
        'ignore_url_parameter': 'ignore_url_parameter',
        'follow_origin': 'follow_origin',
        'compress': 'compress',
        'rules': 'rules'
    }

    def __init__(self, ignore_url_parameter=None, follow_origin=None, compress=None, rules=None):
        """CacheConfig

        The model defined in g42cloud sdk

        :param ignore_url_parameter: The param of the CacheConfig
        :type ignore_url_parameter: bool
        :param follow_origin: The param of the CacheConfig
        :type follow_origin: bool
        :param compress: The param of the CacheConfig
        :type compress: :class:`g42cloudsdkcdn.v1.CompressResponse`
        :param rules: The param of the CacheConfig
        :type rules: list[:class:`g42cloudsdkcdn.v1.Rules`]
        """
        
        

        self._ignore_url_parameter = None
        self._follow_origin = None
        self._compress = None
        self._rules = None
        self.discriminator = None

        if ignore_url_parameter is not None:
            self.ignore_url_parameter = ignore_url_parameter
        if follow_origin is not None:
            self.follow_origin = follow_origin
        if compress is not None:
            self.compress = compress
        if rules is not None:
            self.rules = rules

    @property
    def ignore_url_parameter(self):
        """Gets the ignore_url_parameter of this CacheConfig.

        :return: The ignore_url_parameter of this CacheConfig.
        :rtype: bool
        """
        return self._ignore_url_parameter

    @ignore_url_parameter.setter
    def ignore_url_parameter(self, ignore_url_parameter):
        """Sets the ignore_url_parameter of this CacheConfig.

        :param ignore_url_parameter: The ignore_url_parameter of this CacheConfig.
        :type ignore_url_parameter: bool
        """
        self._ignore_url_parameter = ignore_url_parameter

    @property
    def follow_origin(self):
        """Gets the follow_origin of this CacheConfig.

        :return: The follow_origin of this CacheConfig.
        :rtype: bool
        """
        return self._follow_origin

    @follow_origin.setter
    def follow_origin(self, follow_origin):
        """Sets the follow_origin of this CacheConfig.

        :param follow_origin: The follow_origin of this CacheConfig.
        :type follow_origin: bool
        """
        self._follow_origin = follow_origin

    @property
    def compress(self):
        """Gets the compress of this CacheConfig.

        :return: The compress of this CacheConfig.
        :rtype: :class:`g42cloudsdkcdn.v1.CompressResponse`
        """
        return self._compress

    @compress.setter
    def compress(self, compress):
        """Sets the compress of this CacheConfig.

        :param compress: The compress of this CacheConfig.
        :type compress: :class:`g42cloudsdkcdn.v1.CompressResponse`
        """
        self._compress = compress

    @property
    def rules(self):
        """Gets the rules of this CacheConfig.

        :return: The rules of this CacheConfig.
        :rtype: list[:class:`g42cloudsdkcdn.v1.Rules`]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this CacheConfig.

        :param rules: The rules of this CacheConfig.
        :type rules: list[:class:`g42cloudsdkcdn.v1.Rules`]
        """
        self._rules = rules

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
        if not isinstance(other, CacheConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
