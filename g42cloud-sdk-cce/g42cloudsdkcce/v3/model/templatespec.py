# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Templatespec:

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
        'require': 'bool',
        'labels': 'list[str]',
        'logo_url': 'str',
        'readme_url': 'str',
        'description': 'str',
        'versions': 'list[Versions]'
    }

    attribute_map = {
        'type': 'type',
        'require': 'require',
        'labels': 'labels',
        'logo_url': 'logoURL',
        'readme_url': 'readmeURL',
        'description': 'description',
        'versions': 'versions'
    }

    def __init__(self, type=None, require=None, labels=None, logo_url=None, readme_url=None, description=None, versions=None):
        """Templatespec

        The model defined in g42cloud sdk

        :param type: The param of the Templatespec
        :type type: str
        :param require: The param of the Templatespec
        :type require: bool
        :param labels: The param of the Templatespec
        :type labels: list[str]
        :param logo_url: The param of the Templatespec
        :type logo_url: str
        :param readme_url: The param of the Templatespec
        :type readme_url: str
        :param description: The param of the Templatespec
        :type description: str
        :param versions: The param of the Templatespec
        :type versions: list[:class:`g42cloudsdkcce.v3.Versions`]
        """
        
        

        self._type = None
        self._require = None
        self._labels = None
        self._logo_url = None
        self._readme_url = None
        self._description = None
        self._versions = None
        self.discriminator = None

        self.type = type
        if require is not None:
            self.require = require
        self.labels = labels
        self.logo_url = logo_url
        self.readme_url = readme_url
        self.description = description
        self.versions = versions

    @property
    def type(self):
        """Gets the type of this Templatespec.

        :return: The type of this Templatespec.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Templatespec.

        :param type: The type of this Templatespec.
        :type type: str
        """
        self._type = type

    @property
    def require(self):
        """Gets the require of this Templatespec.

        :return: The require of this Templatespec.
        :rtype: bool
        """
        return self._require

    @require.setter
    def require(self, require):
        """Sets the require of this Templatespec.

        :param require: The require of this Templatespec.
        :type require: bool
        """
        self._require = require

    @property
    def labels(self):
        """Gets the labels of this Templatespec.

        :return: The labels of this Templatespec.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this Templatespec.

        :param labels: The labels of this Templatespec.
        :type labels: list[str]
        """
        self._labels = labels

    @property
    def logo_url(self):
        """Gets the logo_url of this Templatespec.

        :return: The logo_url of this Templatespec.
        :rtype: str
        """
        return self._logo_url

    @logo_url.setter
    def logo_url(self, logo_url):
        """Sets the logo_url of this Templatespec.

        :param logo_url: The logo_url of this Templatespec.
        :type logo_url: str
        """
        self._logo_url = logo_url

    @property
    def readme_url(self):
        """Gets the readme_url of this Templatespec.

        :return: The readme_url of this Templatespec.
        :rtype: str
        """
        return self._readme_url

    @readme_url.setter
    def readme_url(self, readme_url):
        """Sets the readme_url of this Templatespec.

        :param readme_url: The readme_url of this Templatespec.
        :type readme_url: str
        """
        self._readme_url = readme_url

    @property
    def description(self):
        """Gets the description of this Templatespec.

        :return: The description of this Templatespec.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Templatespec.

        :param description: The description of this Templatespec.
        :type description: str
        """
        self._description = description

    @property
    def versions(self):
        """Gets the versions of this Templatespec.

        :return: The versions of this Templatespec.
        :rtype: list[:class:`g42cloudsdkcce.v3.Versions`]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        """Sets the versions of this Templatespec.

        :param versions: The versions of this Templatespec.
        :type versions: list[:class:`g42cloudsdkcce.v3.Versions`]
        """
        self._versions = versions

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
        if not isinstance(other, Templatespec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
