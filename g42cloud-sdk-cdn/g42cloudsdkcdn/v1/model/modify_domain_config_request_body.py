# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyDomainConfigRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'configs': 'Configs'
    }

    attribute_map = {
        'configs': 'configs'
    }

    def __init__(self, configs=None):
        """ModifyDomainConfigRequestBody

        The model defined in g42cloud sdk

        :param configs: The param of the ModifyDomainConfigRequestBody
        :type configs: :class:`g42cloudsdkcdn.v1.Configs`
        """
        
        

        self._configs = None
        self.discriminator = None

        if configs is not None:
            self.configs = configs

    @property
    def configs(self):
        """Gets the configs of this ModifyDomainConfigRequestBody.

        :return: The configs of this ModifyDomainConfigRequestBody.
        :rtype: :class:`g42cloudsdkcdn.v1.Configs`
        """
        return self._configs

    @configs.setter
    def configs(self, configs):
        """Sets the configs of this ModifyDomainConfigRequestBody.

        :param configs: The configs of this ModifyDomainConfigRequestBody.
        :type configs: :class:`g42cloudsdkcdn.v1.Configs`
        """
        self._configs = configs

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
        if not isinstance(other, ModifyDomainConfigRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other