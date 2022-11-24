# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Volume:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'size': 'int',
        'volumetype': 'str',
        'extend_param': 'dict(str, object)',
        'cluster_id': 'str',
        'cluster_type': 'str',
        'hwpassthrough': 'bool',
        'metadata': 'VolumeMetadata'
    }

    attribute_map = {
        'size': 'size',
        'volumetype': 'volumetype',
        'extend_param': 'extendParam',
        'cluster_id': 'cluster_id',
        'cluster_type': 'cluster_type',
        'hwpassthrough': 'hw:passthrough',
        'metadata': 'metadata'
    }

    def __init__(self, size=None, volumetype=None, extend_param=None, cluster_id=None, cluster_type=None, hwpassthrough=None, metadata=None):
        """Volume

        The model defined in g42cloud sdk

        :param size: The param of the Volume
        :type size: int
        :param volumetype: The param of the Volume
        :type volumetype: str
        :param extend_param: The param of the Volume
        :type extend_param: dict(str, object)
        :param cluster_id: The param of the Volume
        :type cluster_id: str
        :param cluster_type: The param of the Volume
        :type cluster_type: str
        :param hwpassthrough: The param of the Volume
        :type hwpassthrough: bool
        :param metadata: The param of the Volume
        :type metadata: :class:`g42cloudsdkcce.v3.VolumeMetadata`
        """
        
        

        self._size = None
        self._volumetype = None
        self._extend_param = None
        self._cluster_id = None
        self._cluster_type = None
        self._hwpassthrough = None
        self._metadata = None
        self.discriminator = None

        self.size = size
        self.volumetype = volumetype
        if extend_param is not None:
            self.extend_param = extend_param
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_type is not None:
            self.cluster_type = cluster_type
        if hwpassthrough is not None:
            self.hwpassthrough = hwpassthrough
        if metadata is not None:
            self.metadata = metadata

    @property
    def size(self):
        """Gets the size of this Volume.

        :return: The size of this Volume.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this Volume.

        :param size: The size of this Volume.
        :type size: int
        """
        self._size = size

    @property
    def volumetype(self):
        """Gets the volumetype of this Volume.

        :return: The volumetype of this Volume.
        :rtype: str
        """
        return self._volumetype

    @volumetype.setter
    def volumetype(self, volumetype):
        """Sets the volumetype of this Volume.

        :param volumetype: The volumetype of this Volume.
        :type volumetype: str
        """
        self._volumetype = volumetype

    @property
    def extend_param(self):
        """Gets the extend_param of this Volume.

        :return: The extend_param of this Volume.
        :rtype: dict(str, object)
        """
        return self._extend_param

    @extend_param.setter
    def extend_param(self, extend_param):
        """Sets the extend_param of this Volume.

        :param extend_param: The extend_param of this Volume.
        :type extend_param: dict(str, object)
        """
        self._extend_param = extend_param

    @property
    def cluster_id(self):
        """Gets the cluster_id of this Volume.

        :return: The cluster_id of this Volume.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this Volume.

        :param cluster_id: The cluster_id of this Volume.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_type(self):
        """Gets the cluster_type of this Volume.

        :return: The cluster_type of this Volume.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        """Sets the cluster_type of this Volume.

        :param cluster_type: The cluster_type of this Volume.
        :type cluster_type: str
        """
        self._cluster_type = cluster_type

    @property
    def hwpassthrough(self):
        """Gets the hwpassthrough of this Volume.

        :return: The hwpassthrough of this Volume.
        :rtype: bool
        """
        return self._hwpassthrough

    @hwpassthrough.setter
    def hwpassthrough(self, hwpassthrough):
        """Sets the hwpassthrough of this Volume.

        :param hwpassthrough: The hwpassthrough of this Volume.
        :type hwpassthrough: bool
        """
        self._hwpassthrough = hwpassthrough

    @property
    def metadata(self):
        """Gets the metadata of this Volume.

        :return: The metadata of this Volume.
        :rtype: :class:`g42cloudsdkcce.v3.VolumeMetadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Volume.

        :param metadata: The metadata of this Volume.
        :type metadata: :class:`g42cloudsdkcce.v3.VolumeMetadata`
        """
        self._metadata = metadata

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
        if not isinstance(other, Volume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
