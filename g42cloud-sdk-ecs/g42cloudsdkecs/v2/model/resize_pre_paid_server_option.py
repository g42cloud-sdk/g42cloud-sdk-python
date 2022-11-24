# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResizePrePaidServerOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flavor_ref': 'str',
        'dedicated_host_id': 'str',
        'extendparam': 'ResizeServerExtendParam',
        'mode': 'str'
    }

    attribute_map = {
        'flavor_ref': 'flavorRef',
        'dedicated_host_id': 'dedicated_host_id',
        'extendparam': 'extendparam',
        'mode': 'mode'
    }

    def __init__(self, flavor_ref=None, dedicated_host_id=None, extendparam=None, mode=None):
        """ResizePrePaidServerOption

        The model defined in g42cloud sdk

        :param flavor_ref: The param of the ResizePrePaidServerOption
        :type flavor_ref: str
        :param dedicated_host_id: The param of the ResizePrePaidServerOption
        :type dedicated_host_id: str
        :param extendparam: The param of the ResizePrePaidServerOption
        :type extendparam: :class:`g42cloudsdkecs.v2.ResizeServerExtendParam`
        :param mode: The param of the ResizePrePaidServerOption
        :type mode: str
        """
        
        

        self._flavor_ref = None
        self._dedicated_host_id = None
        self._extendparam = None
        self._mode = None
        self.discriminator = None

        self.flavor_ref = flavor_ref
        if dedicated_host_id is not None:
            self.dedicated_host_id = dedicated_host_id
        if extendparam is not None:
            self.extendparam = extendparam
        if mode is not None:
            self.mode = mode

    @property
    def flavor_ref(self):
        """Gets the flavor_ref of this ResizePrePaidServerOption.

        :return: The flavor_ref of this ResizePrePaidServerOption.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        """Sets the flavor_ref of this ResizePrePaidServerOption.

        :param flavor_ref: The flavor_ref of this ResizePrePaidServerOption.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def dedicated_host_id(self):
        """Gets the dedicated_host_id of this ResizePrePaidServerOption.

        :return: The dedicated_host_id of this ResizePrePaidServerOption.
        :rtype: str
        """
        return self._dedicated_host_id

    @dedicated_host_id.setter
    def dedicated_host_id(self, dedicated_host_id):
        """Sets the dedicated_host_id of this ResizePrePaidServerOption.

        :param dedicated_host_id: The dedicated_host_id of this ResizePrePaidServerOption.
        :type dedicated_host_id: str
        """
        self._dedicated_host_id = dedicated_host_id

    @property
    def extendparam(self):
        """Gets the extendparam of this ResizePrePaidServerOption.

        :return: The extendparam of this ResizePrePaidServerOption.
        :rtype: :class:`g42cloudsdkecs.v2.ResizeServerExtendParam`
        """
        return self._extendparam

    @extendparam.setter
    def extendparam(self, extendparam):
        """Sets the extendparam of this ResizePrePaidServerOption.

        :param extendparam: The extendparam of this ResizePrePaidServerOption.
        :type extendparam: :class:`g42cloudsdkecs.v2.ResizeServerExtendParam`
        """
        self._extendparam = extendparam

    @property
    def mode(self):
        """Gets the mode of this ResizePrePaidServerOption.

        :return: The mode of this ResizePrePaidServerOption.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this ResizePrePaidServerOption.

        :param mode: The mode of this ResizePrePaidServerOption.
        :type mode: str
        """
        self._mode = mode

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
        if not isinstance(other, ResizePrePaidServerOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
