# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class PersistentVolumeClaimStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_modes': 'list[str]',
        'capacity': 'str',
        'phase': 'str'
    }

    attribute_map = {
        'access_modes': 'accessModes',
        'capacity': 'capacity',
        'phase': 'phase'
    }

    def __init__(self, access_modes=None, capacity=None, phase=None):
        """PersistentVolumeClaimStatus

        The model defined in g42cloud sdk

        :param access_modes: The param of the PersistentVolumeClaimStatus
        :type access_modes: list[str]
        :param capacity: The param of the PersistentVolumeClaimStatus
        :type capacity: str
        :param phase: The param of the PersistentVolumeClaimStatus
        :type phase: str
        """
        
        

        self._access_modes = None
        self._capacity = None
        self._phase = None
        self.discriminator = None

        if access_modes is not None:
            self.access_modes = access_modes
        if capacity is not None:
            self.capacity = capacity
        if phase is not None:
            self.phase = phase

    @property
    def access_modes(self):
        """Gets the access_modes of this PersistentVolumeClaimStatus.

        :return: The access_modes of this PersistentVolumeClaimStatus.
        :rtype: list[str]
        """
        return self._access_modes

    @access_modes.setter
    def access_modes(self, access_modes):
        """Sets the access_modes of this PersistentVolumeClaimStatus.

        :param access_modes: The access_modes of this PersistentVolumeClaimStatus.
        :type access_modes: list[str]
        """
        self._access_modes = access_modes

    @property
    def capacity(self):
        """Gets the capacity of this PersistentVolumeClaimStatus.

        :return: The capacity of this PersistentVolumeClaimStatus.
        :rtype: str
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this PersistentVolumeClaimStatus.

        :param capacity: The capacity of this PersistentVolumeClaimStatus.
        :type capacity: str
        """
        self._capacity = capacity

    @property
    def phase(self):
        """Gets the phase of this PersistentVolumeClaimStatus.

        :return: The phase of this PersistentVolumeClaimStatus.
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this PersistentVolumeClaimStatus.

        :param phase: The phase of this PersistentVolumeClaimStatus.
        :type phase: str
        """
        self._phase = phase

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
        if not isinstance(other, PersistentVolumeClaimStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
