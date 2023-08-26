# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSubNetworkInterfaceRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dry_run': 'bool',
        'sub_network_interface': 'UpdateSubNetworkInterfaceOption'
    }

    attribute_map = {
        'dry_run': 'dry_run',
        'sub_network_interface': 'sub_network_interface'
    }

    def __init__(self, dry_run=None, sub_network_interface=None):
        """UpdateSubNetworkInterfaceRequestBody

        The model defined in g42cloud sdk

        :param dry_run: The param of the UpdateSubNetworkInterfaceRequestBody
        :type dry_run: bool
        :param sub_network_interface: The param of the UpdateSubNetworkInterfaceRequestBody
        :type sub_network_interface: :class:`g42cloudsdkvpc.v3.UpdateSubNetworkInterfaceOption`
        """
        
        

        self._dry_run = None
        self._sub_network_interface = None
        self.discriminator = None

        if dry_run is not None:
            self.dry_run = dry_run
        self.sub_network_interface = sub_network_interface

    @property
    def dry_run(self):
        """Gets the dry_run of this UpdateSubNetworkInterfaceRequestBody.

        :return: The dry_run of this UpdateSubNetworkInterfaceRequestBody.
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        """Sets the dry_run of this UpdateSubNetworkInterfaceRequestBody.

        :param dry_run: The dry_run of this UpdateSubNetworkInterfaceRequestBody.
        :type dry_run: bool
        """
        self._dry_run = dry_run

    @property
    def sub_network_interface(self):
        """Gets the sub_network_interface of this UpdateSubNetworkInterfaceRequestBody.

        :return: The sub_network_interface of this UpdateSubNetworkInterfaceRequestBody.
        :rtype: :class:`g42cloudsdkvpc.v3.UpdateSubNetworkInterfaceOption`
        """
        return self._sub_network_interface

    @sub_network_interface.setter
    def sub_network_interface(self, sub_network_interface):
        """Sets the sub_network_interface of this UpdateSubNetworkInterfaceRequestBody.

        :param sub_network_interface: The sub_network_interface of this UpdateSubNetworkInterfaceRequestBody.
        :type sub_network_interface: :class:`g42cloudsdkvpc.v3.UpdateSubNetworkInterfaceOption`
        """
        self._sub_network_interface = sub_network_interface

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
        if not isinstance(other, UpdateSubNetworkInterfaceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
