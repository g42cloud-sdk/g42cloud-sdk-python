# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class CinderListQuotasRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_project_id': 'str',
        'usage': 'str'
    }

    attribute_map = {
        'target_project_id': 'target_project_id',
        'usage': 'usage'
    }

    def __init__(self, target_project_id=None, usage=None):
        """CinderListQuotasRequest

        The model defined in g42cloud sdk

        :param target_project_id: The param of the CinderListQuotasRequest
        :type target_project_id: str
        :param usage: The param of the CinderListQuotasRequest
        :type usage: str
        """
        
        

        self._target_project_id = None
        self._usage = None
        self.discriminator = None

        self.target_project_id = target_project_id
        self.usage = usage

    @property
    def target_project_id(self):
        """Gets the target_project_id of this CinderListQuotasRequest.

        :return: The target_project_id of this CinderListQuotasRequest.
        :rtype: str
        """
        return self._target_project_id

    @target_project_id.setter
    def target_project_id(self, target_project_id):
        """Sets the target_project_id of this CinderListQuotasRequest.

        :param target_project_id: The target_project_id of this CinderListQuotasRequest.
        :type target_project_id: str
        """
        self._target_project_id = target_project_id

    @property
    def usage(self):
        """Gets the usage of this CinderListQuotasRequest.

        :return: The usage of this CinderListQuotasRequest.
        :rtype: str
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this CinderListQuotasRequest.

        :param usage: The usage of this CinderListQuotasRequest.
        :type usage: str
        """
        self._usage = usage

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
        if not isinstance(other, CinderListQuotasRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
