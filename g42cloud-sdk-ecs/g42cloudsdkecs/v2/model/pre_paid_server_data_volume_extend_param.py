# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrePaidServerDataVolumeExtendParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_spec_code': 'str',
        'resource_type': 'str',
        'snapshot_id': 'str'
    }

    attribute_map = {
        'resource_spec_code': 'resourceSpecCode',
        'resource_type': 'resourceType',
        'snapshot_id': 'snapshotId'
    }

    def __init__(self, resource_spec_code=None, resource_type=None, snapshot_id=None):
        """PrePaidServerDataVolumeExtendParam

        The model defined in g42cloud sdk

        :param resource_spec_code: The param of the PrePaidServerDataVolumeExtendParam
        :type resource_spec_code: str
        :param resource_type: The param of the PrePaidServerDataVolumeExtendParam
        :type resource_type: str
        :param snapshot_id: The param of the PrePaidServerDataVolumeExtendParam
        :type snapshot_id: str
        """
        
        

        self._resource_spec_code = None
        self._resource_type = None
        self._snapshot_id = None
        self.discriminator = None

        if resource_spec_code is not None:
            self.resource_spec_code = resource_spec_code
        if resource_type is not None:
            self.resource_type = resource_type
        if snapshot_id is not None:
            self.snapshot_id = snapshot_id

    @property
    def resource_spec_code(self):
        """Gets the resource_spec_code of this PrePaidServerDataVolumeExtendParam.

        :return: The resource_spec_code of this PrePaidServerDataVolumeExtendParam.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        """Sets the resource_spec_code of this PrePaidServerDataVolumeExtendParam.

        :param resource_spec_code: The resource_spec_code of this PrePaidServerDataVolumeExtendParam.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def resource_type(self):
        """Gets the resource_type of this PrePaidServerDataVolumeExtendParam.

        :return: The resource_type of this PrePaidServerDataVolumeExtendParam.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this PrePaidServerDataVolumeExtendParam.

        :param resource_type: The resource_type of this PrePaidServerDataVolumeExtendParam.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def snapshot_id(self):
        """Gets the snapshot_id of this PrePaidServerDataVolumeExtendParam.

        :return: The snapshot_id of this PrePaidServerDataVolumeExtendParam.
        :rtype: str
        """
        return self._snapshot_id

    @snapshot_id.setter
    def snapshot_id(self, snapshot_id):
        """Sets the snapshot_id of this PrePaidServerDataVolumeExtendParam.

        :param snapshot_id: The snapshot_id of this PrePaidServerDataVolumeExtendParam.
        :type snapshot_id: str
        """
        self._snapshot_id = snapshot_id

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
        if not isinstance(other, PrePaidServerDataVolumeExtendParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
