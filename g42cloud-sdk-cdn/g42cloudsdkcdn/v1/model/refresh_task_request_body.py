# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RefreshTaskRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'urls': 'list[str]'
    }

    attribute_map = {
        'type': 'type',
        'urls': 'urls'
    }

    def __init__(self, type=None, urls=None):
        """RefreshTaskRequestBody

        The model defined in g42cloud sdk

        :param type: The param of the RefreshTaskRequestBody
        :type type: str
        :param urls: The param of the RefreshTaskRequestBody
        :type urls: list[str]
        """
        
        

        self._type = None
        self._urls = None
        self.discriminator = None

        if type is not None:
            self.type = type
        self.urls = urls

    @property
    def type(self):
        """Gets the type of this RefreshTaskRequestBody.

        :return: The type of this RefreshTaskRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RefreshTaskRequestBody.

        :param type: The type of this RefreshTaskRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def urls(self):
        """Gets the urls of this RefreshTaskRequestBody.

        :return: The urls of this RefreshTaskRequestBody.
        :rtype: list[str]
        """
        return self._urls

    @urls.setter
    def urls(self, urls):
        """Sets the urls of this RefreshTaskRequestBody.

        :param urls: The urls of this RefreshTaskRequestBody.
        :type urls: list[str]
        """
        self._urls = urls

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
        if not isinstance(other, RefreshTaskRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
