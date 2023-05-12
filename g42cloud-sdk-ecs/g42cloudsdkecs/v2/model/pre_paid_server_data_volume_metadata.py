# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrePaidServerDataVolumeMetadata:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'system__encrypted': 'str',
        'system__cmkid': 'str'
    }

    attribute_map = {
        'system__encrypted': '__system__encrypted',
        'system__cmkid': '__system__cmkid'
    }

    def __init__(self, system__encrypted=None, system__cmkid=None):
        """PrePaidServerDataVolumeMetadata

        The model defined in g42cloud sdk

        :param system__encrypted: The param of the PrePaidServerDataVolumeMetadata
        :type system__encrypted: str
        :param system__cmkid: The param of the PrePaidServerDataVolumeMetadata
        :type system__cmkid: str
        """
        
        

        self._system__encrypted = None
        self._system__cmkid = None
        self.discriminator = None

        if system__encrypted is not None:
            self.system__encrypted = system__encrypted
        if system__cmkid is not None:
            self.system__cmkid = system__cmkid

    @property
    def system__encrypted(self):
        """Gets the system__encrypted of this PrePaidServerDataVolumeMetadata.

        :return: The system__encrypted of this PrePaidServerDataVolumeMetadata.
        :rtype: str
        """
        return self._system__encrypted

    @system__encrypted.setter
    def system__encrypted(self, system__encrypted):
        """Sets the system__encrypted of this PrePaidServerDataVolumeMetadata.

        :param system__encrypted: The system__encrypted of this PrePaidServerDataVolumeMetadata.
        :type system__encrypted: str
        """
        self._system__encrypted = system__encrypted

    @property
    def system__cmkid(self):
        """Gets the system__cmkid of this PrePaidServerDataVolumeMetadata.

        :return: The system__cmkid of this PrePaidServerDataVolumeMetadata.
        :rtype: str
        """
        return self._system__cmkid

    @system__cmkid.setter
    def system__cmkid(self, system__cmkid):
        """Sets the system__cmkid of this PrePaidServerDataVolumeMetadata.

        :param system__cmkid: The system__cmkid of this PrePaidServerDataVolumeMetadata.
        :type system__cmkid: str
        """
        self._system__cmkid = system__cmkid

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
        if not isinstance(other, PrePaidServerDataVolumeMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
