# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PersistentVolumeClaimSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'volume_id': 'str',
        'storage_type': 'str',
        'access_modes': 'list[str]',
        'storage_class_name': 'str',
        'volume_name': 'str',
        'resources': 'ResourceRequirements',
        'volume_mode': 'str'
    }

    attribute_map = {
        'volume_id': 'volumeID',
        'storage_type': 'storageType',
        'access_modes': 'accessModes',
        'storage_class_name': 'storageClassName',
        'volume_name': 'volumeName',
        'resources': 'resources',
        'volume_mode': 'volumeMode'
    }

    def __init__(self, volume_id=None, storage_type=None, access_modes=None, storage_class_name=None, volume_name=None, resources=None, volume_mode=None):
        """PersistentVolumeClaimSpec

        The model defined in g42cloud sdk

        :param volume_id: The param of the PersistentVolumeClaimSpec
        :type volume_id: str
        :param storage_type: The param of the PersistentVolumeClaimSpec
        :type storage_type: str
        :param access_modes: The param of the PersistentVolumeClaimSpec
        :type access_modes: list[str]
        :param storage_class_name: The param of the PersistentVolumeClaimSpec
        :type storage_class_name: str
        :param volume_name: The param of the PersistentVolumeClaimSpec
        :type volume_name: str
        :param resources: The param of the PersistentVolumeClaimSpec
        :type resources: :class:`g42cloudsdkcce.v3.ResourceRequirements`
        :param volume_mode: The param of the PersistentVolumeClaimSpec
        :type volume_mode: str
        """
        
        

        self._volume_id = None
        self._storage_type = None
        self._access_modes = None
        self._storage_class_name = None
        self._volume_name = None
        self._resources = None
        self._volume_mode = None
        self.discriminator = None

        self.volume_id = volume_id
        self.storage_type = storage_type
        self.access_modes = access_modes
        if storage_class_name is not None:
            self.storage_class_name = storage_class_name
        if volume_name is not None:
            self.volume_name = volume_name
        if resources is not None:
            self.resources = resources
        if volume_mode is not None:
            self.volume_mode = volume_mode

    @property
    def volume_id(self):
        """Gets the volume_id of this PersistentVolumeClaimSpec.

        :return: The volume_id of this PersistentVolumeClaimSpec.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """Sets the volume_id of this PersistentVolumeClaimSpec.

        :param volume_id: The volume_id of this PersistentVolumeClaimSpec.
        :type volume_id: str
        """
        self._volume_id = volume_id

    @property
    def storage_type(self):
        """Gets the storage_type of this PersistentVolumeClaimSpec.

        :return: The storage_type of this PersistentVolumeClaimSpec.
        :rtype: str
        """
        return self._storage_type

    @storage_type.setter
    def storage_type(self, storage_type):
        """Sets the storage_type of this PersistentVolumeClaimSpec.

        :param storage_type: The storage_type of this PersistentVolumeClaimSpec.
        :type storage_type: str
        """
        self._storage_type = storage_type

    @property
    def access_modes(self):
        """Gets the access_modes of this PersistentVolumeClaimSpec.

        :return: The access_modes of this PersistentVolumeClaimSpec.
        :rtype: list[str]
        """
        return self._access_modes

    @access_modes.setter
    def access_modes(self, access_modes):
        """Sets the access_modes of this PersistentVolumeClaimSpec.

        :param access_modes: The access_modes of this PersistentVolumeClaimSpec.
        :type access_modes: list[str]
        """
        self._access_modes = access_modes

    @property
    def storage_class_name(self):
        """Gets the storage_class_name of this PersistentVolumeClaimSpec.

        :return: The storage_class_name of this PersistentVolumeClaimSpec.
        :rtype: str
        """
        return self._storage_class_name

    @storage_class_name.setter
    def storage_class_name(self, storage_class_name):
        """Sets the storage_class_name of this PersistentVolumeClaimSpec.

        :param storage_class_name: The storage_class_name of this PersistentVolumeClaimSpec.
        :type storage_class_name: str
        """
        self._storage_class_name = storage_class_name

    @property
    def volume_name(self):
        """Gets the volume_name of this PersistentVolumeClaimSpec.

        :return: The volume_name of this PersistentVolumeClaimSpec.
        :rtype: str
        """
        return self._volume_name

    @volume_name.setter
    def volume_name(self, volume_name):
        """Sets the volume_name of this PersistentVolumeClaimSpec.

        :param volume_name: The volume_name of this PersistentVolumeClaimSpec.
        :type volume_name: str
        """
        self._volume_name = volume_name

    @property
    def resources(self):
        """Gets the resources of this PersistentVolumeClaimSpec.

        :return: The resources of this PersistentVolumeClaimSpec.
        :rtype: :class:`g42cloudsdkcce.v3.ResourceRequirements`
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this PersistentVolumeClaimSpec.

        :param resources: The resources of this PersistentVolumeClaimSpec.
        :type resources: :class:`g42cloudsdkcce.v3.ResourceRequirements`
        """
        self._resources = resources

    @property
    def volume_mode(self):
        """Gets the volume_mode of this PersistentVolumeClaimSpec.

        :return: The volume_mode of this PersistentVolumeClaimSpec.
        :rtype: str
        """
        return self._volume_mode

    @volume_mode.setter
    def volume_mode(self, volume_mode):
        """Sets the volume_mode of this PersistentVolumeClaimSpec.

        :param volume_mode: The volume_mode of this PersistentVolumeClaimSpec.
        :type volume_mode: str
        """
        self._volume_mode = volume_mode

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
        if not isinstance(other, PersistentVolumeClaimSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
