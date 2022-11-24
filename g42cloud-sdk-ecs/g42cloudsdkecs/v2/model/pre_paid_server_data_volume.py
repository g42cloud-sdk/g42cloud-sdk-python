# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrePaidServerDataVolume:

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
        'shareable': 'bool',
        'multiattach': 'bool',
        'hwpassthrough': 'bool',
        'extendparam': 'PrePaidServerDataVolumeExtendParam',
        'cluster_type': 'str',
        'cluster_id': 'str',
        'metadata': 'PrePaidServerDataVolumeMetadata',
        'data_image_id': 'str'
    }

    attribute_map = {
        'volumetype': 'volumetype',
        'size': 'size',
        'shareable': 'shareable',
        'multiattach': 'multiattach',
        'hwpassthrough': 'hw:passthrough',
        'extendparam': 'extendparam',
        'cluster_type': 'cluster_type',
        'cluster_id': 'cluster_id',
        'metadata': 'metadata',
        'data_image_id': 'data_image_id'
    }

    def __init__(self, volumetype=None, size=None, shareable=None, multiattach=None, hwpassthrough=None, extendparam=None, cluster_type=None, cluster_id=None, metadata=None, data_image_id=None):
        """PrePaidServerDataVolume

        The model defined in g42cloud sdk

        :param volumetype: The param of the PrePaidServerDataVolume
        :type volumetype: str
        :param size: The param of the PrePaidServerDataVolume
        :type size: int
        :param shareable: The param of the PrePaidServerDataVolume
        :type shareable: bool
        :param multiattach: The param of the PrePaidServerDataVolume
        :type multiattach: bool
        :param hwpassthrough: The param of the PrePaidServerDataVolume
        :type hwpassthrough: bool
        :param extendparam: The param of the PrePaidServerDataVolume
        :type extendparam: :class:`g42cloudsdkecs.v2.PrePaidServerDataVolumeExtendParam`
        :param cluster_type: The param of the PrePaidServerDataVolume
        :type cluster_type: str
        :param cluster_id: The param of the PrePaidServerDataVolume
        :type cluster_id: str
        :param metadata: The param of the PrePaidServerDataVolume
        :type metadata: :class:`g42cloudsdkecs.v2.PrePaidServerDataVolumeMetadata`
        :param data_image_id: The param of the PrePaidServerDataVolume
        :type data_image_id: str
        """
        
        

        self._volumetype = None
        self._size = None
        self._shareable = None
        self._multiattach = None
        self._hwpassthrough = None
        self._extendparam = None
        self._cluster_type = None
        self._cluster_id = None
        self._metadata = None
        self._data_image_id = None
        self.discriminator = None

        self.volumetype = volumetype
        self.size = size
        if shareable is not None:
            self.shareable = shareable
        if multiattach is not None:
            self.multiattach = multiattach
        if hwpassthrough is not None:
            self.hwpassthrough = hwpassthrough
        if extendparam is not None:
            self.extendparam = extendparam
        if cluster_type is not None:
            self.cluster_type = cluster_type
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if metadata is not None:
            self.metadata = metadata
        if data_image_id is not None:
            self.data_image_id = data_image_id

    @property
    def volumetype(self):
        """Gets the volumetype of this PrePaidServerDataVolume.

        :return: The volumetype of this PrePaidServerDataVolume.
        :rtype: str
        """
        return self._volumetype

    @volumetype.setter
    def volumetype(self, volumetype):
        """Sets the volumetype of this PrePaidServerDataVolume.

        :param volumetype: The volumetype of this PrePaidServerDataVolume.
        :type volumetype: str
        """
        self._volumetype = volumetype

    @property
    def size(self):
        """Gets the size of this PrePaidServerDataVolume.

        :return: The size of this PrePaidServerDataVolume.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this PrePaidServerDataVolume.

        :param size: The size of this PrePaidServerDataVolume.
        :type size: int
        """
        self._size = size

    @property
    def shareable(self):
        """Gets the shareable of this PrePaidServerDataVolume.

        :return: The shareable of this PrePaidServerDataVolume.
        :rtype: bool
        """
        return self._shareable

    @shareable.setter
    def shareable(self, shareable):
        """Sets the shareable of this PrePaidServerDataVolume.

        :param shareable: The shareable of this PrePaidServerDataVolume.
        :type shareable: bool
        """
        self._shareable = shareable

    @property
    def multiattach(self):
        """Gets the multiattach of this PrePaidServerDataVolume.

        :return: The multiattach of this PrePaidServerDataVolume.
        :rtype: bool
        """
        return self._multiattach

    @multiattach.setter
    def multiattach(self, multiattach):
        """Sets the multiattach of this PrePaidServerDataVolume.

        :param multiattach: The multiattach of this PrePaidServerDataVolume.
        :type multiattach: bool
        """
        self._multiattach = multiattach

    @property
    def hwpassthrough(self):
        """Gets the hwpassthrough of this PrePaidServerDataVolume.

        :return: The hwpassthrough of this PrePaidServerDataVolume.
        :rtype: bool
        """
        return self._hwpassthrough

    @hwpassthrough.setter
    def hwpassthrough(self, hwpassthrough):
        """Sets the hwpassthrough of this PrePaidServerDataVolume.

        :param hwpassthrough: The hwpassthrough of this PrePaidServerDataVolume.
        :type hwpassthrough: bool
        """
        self._hwpassthrough = hwpassthrough

    @property
    def extendparam(self):
        """Gets the extendparam of this PrePaidServerDataVolume.

        :return: The extendparam of this PrePaidServerDataVolume.
        :rtype: :class:`g42cloudsdkecs.v2.PrePaidServerDataVolumeExtendParam`
        """
        return self._extendparam

    @extendparam.setter
    def extendparam(self, extendparam):
        """Sets the extendparam of this PrePaidServerDataVolume.

        :param extendparam: The extendparam of this PrePaidServerDataVolume.
        :type extendparam: :class:`g42cloudsdkecs.v2.PrePaidServerDataVolumeExtendParam`
        """
        self._extendparam = extendparam

    @property
    def cluster_type(self):
        """Gets the cluster_type of this PrePaidServerDataVolume.

        :return: The cluster_type of this PrePaidServerDataVolume.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        """Sets the cluster_type of this PrePaidServerDataVolume.

        :param cluster_type: The cluster_type of this PrePaidServerDataVolume.
        :type cluster_type: str
        """
        self._cluster_type = cluster_type

    @property
    def cluster_id(self):
        """Gets the cluster_id of this PrePaidServerDataVolume.

        :return: The cluster_id of this PrePaidServerDataVolume.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this PrePaidServerDataVolume.

        :param cluster_id: The cluster_id of this PrePaidServerDataVolume.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def metadata(self):
        """Gets the metadata of this PrePaidServerDataVolume.

        :return: The metadata of this PrePaidServerDataVolume.
        :rtype: :class:`g42cloudsdkecs.v2.PrePaidServerDataVolumeMetadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this PrePaidServerDataVolume.

        :param metadata: The metadata of this PrePaidServerDataVolume.
        :type metadata: :class:`g42cloudsdkecs.v2.PrePaidServerDataVolumeMetadata`
        """
        self._metadata = metadata

    @property
    def data_image_id(self):
        """Gets the data_image_id of this PrePaidServerDataVolume.

        :return: The data_image_id of this PrePaidServerDataVolume.
        :rtype: str
        """
        return self._data_image_id

    @data_image_id.setter
    def data_image_id(self, data_image_id):
        """Sets the data_image_id of this PrePaidServerDataVolume.

        :param data_image_id: The data_image_id of this PrePaidServerDataVolume.
        :type data_image_id: str
        """
        self._data_image_id = data_image_id

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
        if not isinstance(other, PrePaidServerDataVolume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
