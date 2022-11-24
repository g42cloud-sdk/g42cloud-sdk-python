# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnableConfigurationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'configuration_id': 'str',
        'configuration_name': 'str',
        'success': 'bool',
        'apply_results': 'list[ApplyConfigurationResponseApplyResults]'
    }

    attribute_map = {
        'configuration_id': 'configuration_id',
        'configuration_name': 'configuration_name',
        'success': 'success',
        'apply_results': 'apply_results'
    }

    def __init__(self, configuration_id=None, configuration_name=None, success=None, apply_results=None):
        """EnableConfigurationResponse

        The model defined in g42cloud sdk

        :param configuration_id: The param of the EnableConfigurationResponse
        :type configuration_id: str
        :param configuration_name: The param of the EnableConfigurationResponse
        :type configuration_name: str
        :param success: The param of the EnableConfigurationResponse
        :type success: bool
        :param apply_results: The param of the EnableConfigurationResponse
        :type apply_results: list[:class:`g42cloudsdkrds.v3.ApplyConfigurationResponseApplyResults`]
        """
        
        super(EnableConfigurationResponse, self).__init__()

        self._configuration_id = None
        self._configuration_name = None
        self._success = None
        self._apply_results = None
        self.discriminator = None

        if configuration_id is not None:
            self.configuration_id = configuration_id
        if configuration_name is not None:
            self.configuration_name = configuration_name
        if success is not None:
            self.success = success
        if apply_results is not None:
            self.apply_results = apply_results

    @property
    def configuration_id(self):
        """Gets the configuration_id of this EnableConfigurationResponse.

        :return: The configuration_id of this EnableConfigurationResponse.
        :rtype: str
        """
        return self._configuration_id

    @configuration_id.setter
    def configuration_id(self, configuration_id):
        """Sets the configuration_id of this EnableConfigurationResponse.

        :param configuration_id: The configuration_id of this EnableConfigurationResponse.
        :type configuration_id: str
        """
        self._configuration_id = configuration_id

    @property
    def configuration_name(self):
        """Gets the configuration_name of this EnableConfigurationResponse.

        :return: The configuration_name of this EnableConfigurationResponse.
        :rtype: str
        """
        return self._configuration_name

    @configuration_name.setter
    def configuration_name(self, configuration_name):
        """Sets the configuration_name of this EnableConfigurationResponse.

        :param configuration_name: The configuration_name of this EnableConfigurationResponse.
        :type configuration_name: str
        """
        self._configuration_name = configuration_name

    @property
    def success(self):
        """Gets the success of this EnableConfigurationResponse.

        :return: The success of this EnableConfigurationResponse.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this EnableConfigurationResponse.

        :param success: The success of this EnableConfigurationResponse.
        :type success: bool
        """
        self._success = success

    @property
    def apply_results(self):
        """Gets the apply_results of this EnableConfigurationResponse.

        :return: The apply_results of this EnableConfigurationResponse.
        :rtype: list[:class:`g42cloudsdkrds.v3.ApplyConfigurationResponseApplyResults`]
        """
        return self._apply_results

    @apply_results.setter
    def apply_results(self, apply_results):
        """Sets the apply_results of this EnableConfigurationResponse.

        :param apply_results: The apply_results of this EnableConfigurationResponse.
        :type apply_results: list[:class:`g42cloudsdkrds.v3.ApplyConfigurationResponseApplyResults`]
        """
        self._apply_results = apply_results

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
        if not isinstance(other, EnableConfigurationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
