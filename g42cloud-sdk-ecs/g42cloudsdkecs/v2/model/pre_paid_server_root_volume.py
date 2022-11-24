# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrePaidServerRootVolume:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'volumetype': 'str',
        'size': 'int',
        'extendparam': 'PrePaidServerRootVolumeExtendParam',
        'cluster_type': 'str',
        'cluster_id': 'str',
        'hwpassthrough': 'bool'
    }

    attribute_map = {
        'volumetype': 'volumetype',
        'size': 'size',
        'extendparam': 'extendparam',
        'cluster_type': 'cluster_type',
        'cluster_id': 'cluster_id',
        'hwpassthrough': 'hw:passthrough'
    }

    def __init__(self, volumetype=None, size=None, extendparam=None, cluster_type=None, cluster_id=None, hwpassthrough=None):
        """PrePaidServerRootVolume

        The model defined in g42cloud sdk

        :param volumetype: The param of the PrePaidServerRootVolume
        :type volumetype: str
        :param size: The param of the PrePaidServerRootVolume
        :type size: int
        :param extendparam: The param of the PrePaidServerRootVolume
        :type extendparam: :class:`g42cloudsdkecs.v2.PrePaidServerRootVolumeExtendParam`
        :param cluster_type: The param of the PrePaidServerRootVolume
        :type cluster_type: str
        :param cluster_id: The param of the PrePaidServerRootVolume
        :type cluster_id: str
        :param hwpassthrough: The param of the PrePaidServerRootVolume
        :type hwpassthrough: bool
        """
        
        

        self._volumetype = None
        self._size = None
        self._extendparam = None
        self._cluster_type = None
        self._cluster_id = None
        self._hwpassthrough = None
        self.discriminator = None

        self.volumetype = volumetype
        if size is not None:
            self.size = size
        if extendparam is not None:
            self.extendparam = extendparam
        if cluster_type is not None:
            self.cluster_type = cluster_type
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if hwpassthrough is not None:
            self.hwpassthrough = hwpassthrough

    @property
    def volumetype(self):
        """Gets the volumetype of this PrePaidServerRootVolume.

        :return: The volumetype of this PrePaidServerRootVolume.
        :rtype: str
        """
        return self._volumetype

    @volumetype.setter
    def volumetype(self, volumetype):
        """Sets the volumetype of this PrePaidServerRootVolume.

        :param volumetype: The volumetype of this PrePaidServerRootVolume.
        :type volumetype: str
        """
        self._volumetype = volumetype

    @property
    def size(self):
        """Gets the size of this PrePaidServerRootVolume.

        :return: The size of this PrePaidServerRootVolume.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this PrePaidServerRootVolume.

        :param size: The size of this PrePaidServerRootVolume.
        :type size: int
        """
        self._size = size

    @property
    def extendparam(self):
        """Gets the extendparam of this PrePaidServerRootVolume.

        :return: The extendparam of this PrePaidServerRootVolume.
        :rtype: :class:`g42cloudsdkecs.v2.PrePaidServerRootVolumeExtendParam`
        """
        return self._extendparam

    @extendparam.setter
    def extendparam(self, extendparam):
        """Sets the extendparam of this PrePaidServerRootVolume.

        :param extendparam: The extendparam of this PrePaidServerRootVolume.
        :type extendparam: :class:`g42cloudsdkecs.v2.PrePaidServerRootVolumeExtendParam`
        """
        self._extendparam = extendparam

    @property
    def cluster_type(self):
        """Gets the cluster_type of this PrePaidServerRootVolume.

        :return: The cluster_type of this PrePaidServerRootVolume.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        """Sets the cluster_type of this PrePaidServerRootVolume.

        :param cluster_type: The cluster_type of this PrePaidServerRootVolume.
        :type cluster_type: str
        """
        self._cluster_type = cluster_type

    @property
    def cluster_id(self):
        """Gets the cluster_id of this PrePaidServerRootVolume.

        :return: The cluster_id of this PrePaidServerRootVolume.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this PrePaidServerRootVolume.

        :param cluster_id: The cluster_id of this PrePaidServerRootVolume.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def hwpassthrough(self):
        """Gets the hwpassthrough of this PrePaidServerRootVolume.

        :return: The hwpassthrough of this PrePaidServerRootVolume.
        :rtype: bool
        """
        return self._hwpassthrough

    @hwpassthrough.setter
    def hwpassthrough(self, hwpassthrough):
        """Sets the hwpassthrough of this PrePaidServerRootVolume.

        :param hwpassthrough: The hwpassthrough of this PrePaidServerRootVolume.
        :type hwpassthrough: bool
        """
        self._hwpassthrough = hwpassthrough

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
        if not isinstance(other, PrePaidServerRootVolume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
