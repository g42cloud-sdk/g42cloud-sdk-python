# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceExtraInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'exclude_volumes': 'list[str]',
        'include_volumes': 'list[ResourceExtraInfoIncludeVolumes]'
    }

    attribute_map = {
        'exclude_volumes': 'exclude_volumes',
        'include_volumes': 'include_volumes'
    }

    def __init__(self, exclude_volumes=None, include_volumes=None):
        """ResourceExtraInfo

        The model defined in g42cloud sdk

        :param exclude_volumes: The param of the ResourceExtraInfo
        :type exclude_volumes: list[str]
        :param include_volumes: The param of the ResourceExtraInfo
        :type include_volumes: list[:class:`g42cloudsdkcbr.v1.ResourceExtraInfoIncludeVolumes`]
        """
        
        

        self._exclude_volumes = None
        self._include_volumes = None
        self.discriminator = None

        if exclude_volumes is not None:
            self.exclude_volumes = exclude_volumes
        if include_volumes is not None:
            self.include_volumes = include_volumes

    @property
    def exclude_volumes(self):
        """Gets the exclude_volumes of this ResourceExtraInfo.

        :return: The exclude_volumes of this ResourceExtraInfo.
        :rtype: list[str]
        """
        return self._exclude_volumes

    @exclude_volumes.setter
    def exclude_volumes(self, exclude_volumes):
        """Sets the exclude_volumes of this ResourceExtraInfo.

        :param exclude_volumes: The exclude_volumes of this ResourceExtraInfo.
        :type exclude_volumes: list[str]
        """
        self._exclude_volumes = exclude_volumes

    @property
    def include_volumes(self):
        """Gets the include_volumes of this ResourceExtraInfo.

        :return: The include_volumes of this ResourceExtraInfo.
        :rtype: list[:class:`g42cloudsdkcbr.v1.ResourceExtraInfoIncludeVolumes`]
        """
        return self._include_volumes

    @include_volumes.setter
    def include_volumes(self, include_volumes):
        """Sets the include_volumes of this ResourceExtraInfo.

        :param include_volumes: The include_volumes of this ResourceExtraInfo.
        :type include_volumes: list[:class:`g42cloudsdkcbr.v1.ResourceExtraInfoIncludeVolumes`]
        """
        self._include_volumes = include_volumes

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
        if not isinstance(other, ResourceExtraInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
