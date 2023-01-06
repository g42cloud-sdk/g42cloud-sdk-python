# coding: utf-8

import re
import six



from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class CopyImageInRegionRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cmk_id': 'str',
        'description': 'str',
        'enterprise_project_id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'cmk_id': 'cmk_id',
        'description': 'description',
        'enterprise_project_id': 'enterprise_project_id',
        'name': 'name'
    }

    def __init__(self, cmk_id=None, description=None, enterprise_project_id=None, name=None):
        """CopyImageInRegionRequestBody

        The model defined in g42cloud sdk

        :param cmk_id: The param of the CopyImageInRegionRequestBody
        :type cmk_id: str
        :param description: The param of the CopyImageInRegionRequestBody
        :type description: str
        :param enterprise_project_id: The param of the CopyImageInRegionRequestBody
        :type enterprise_project_id: str
        :param name: The param of the CopyImageInRegionRequestBody
        :type name: str
        """
        
        

        self._cmk_id = None
        self._description = None
        self._enterprise_project_id = None
        self._name = None
        self.discriminator = None

        if cmk_id is not None:
            self.cmk_id = cmk_id
        if description is not None:
            self.description = description
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.name = name

    @property
    def cmk_id(self):
        """Gets the cmk_id of this CopyImageInRegionRequestBody.

        :return: The cmk_id of this CopyImageInRegionRequestBody.
        :rtype: str
        """
        return self._cmk_id

    @cmk_id.setter
    def cmk_id(self, cmk_id):
        """Sets the cmk_id of this CopyImageInRegionRequestBody.

        :param cmk_id: The cmk_id of this CopyImageInRegionRequestBody.
        :type cmk_id: str
        """
        self._cmk_id = cmk_id

    @property
    def description(self):
        """Gets the description of this CopyImageInRegionRequestBody.

        :return: The description of this CopyImageInRegionRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CopyImageInRegionRequestBody.

        :param description: The description of this CopyImageInRegionRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CopyImageInRegionRequestBody.

        :return: The enterprise_project_id of this CopyImageInRegionRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CopyImageInRegionRequestBody.

        :param enterprise_project_id: The enterprise_project_id of this CopyImageInRegionRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def name(self):
        """Gets the name of this CopyImageInRegionRequestBody.

        :return: The name of this CopyImageInRegionRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CopyImageInRegionRequestBody.

        :param name: The name of this CopyImageInRegionRequestBody.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, CopyImageInRegionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other