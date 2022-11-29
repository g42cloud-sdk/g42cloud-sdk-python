# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckpointParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'auto_trigger': 'bool',
        'description': 'str',
        'incremental': 'bool',
        'name': 'str',
        'resources': 'list[str]',
        'resource_details': 'list[Resource]'
    }

    attribute_map = {
        'auto_trigger': 'auto_trigger',
        'description': 'description',
        'incremental': 'incremental',
        'name': 'name',
        'resources': 'resources',
        'resource_details': 'resource_details'
    }

    def __init__(self, auto_trigger=None, description=None, incremental=None, name=None, resources=None, resource_details=None):
        """CheckpointParam

        The model defined in g42cloud sdk

        :param auto_trigger: The param of the CheckpointParam
        :type auto_trigger: bool
        :param description: The param of the CheckpointParam
        :type description: str
        :param incremental: The param of the CheckpointParam
        :type incremental: bool
        :param name: The param of the CheckpointParam
        :type name: str
        :param resources: The param of the CheckpointParam
        :type resources: list[str]
        :param resource_details: The param of the CheckpointParam
        :type resource_details: list[:class:`g42cloudsdkcbr.v1.Resource`]
        """
        
        

        self._auto_trigger = None
        self._description = None
        self._incremental = None
        self._name = None
        self._resources = None
        self._resource_details = None
        self.discriminator = None

        if auto_trigger is not None:
            self.auto_trigger = auto_trigger
        if description is not None:
            self.description = description
        if incremental is not None:
            self.incremental = incremental
        if name is not None:
            self.name = name
        if resources is not None:
            self.resources = resources
        if resource_details is not None:
            self.resource_details = resource_details

    @property
    def auto_trigger(self):
        """Gets the auto_trigger of this CheckpointParam.

        :return: The auto_trigger of this CheckpointParam.
        :rtype: bool
        """
        return self._auto_trigger

    @auto_trigger.setter
    def auto_trigger(self, auto_trigger):
        """Sets the auto_trigger of this CheckpointParam.

        :param auto_trigger: The auto_trigger of this CheckpointParam.
        :type auto_trigger: bool
        """
        self._auto_trigger = auto_trigger

    @property
    def description(self):
        """Gets the description of this CheckpointParam.

        :return: The description of this CheckpointParam.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CheckpointParam.

        :param description: The description of this CheckpointParam.
        :type description: str
        """
        self._description = description

    @property
    def incremental(self):
        """Gets the incremental of this CheckpointParam.

        :return: The incremental of this CheckpointParam.
        :rtype: bool
        """
        return self._incremental

    @incremental.setter
    def incremental(self, incremental):
        """Sets the incremental of this CheckpointParam.

        :param incremental: The incremental of this CheckpointParam.
        :type incremental: bool
        """
        self._incremental = incremental

    @property
    def name(self):
        """Gets the name of this CheckpointParam.

        :return: The name of this CheckpointParam.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CheckpointParam.

        :param name: The name of this CheckpointParam.
        :type name: str
        """
        self._name = name

    @property
    def resources(self):
        """Gets the resources of this CheckpointParam.

        :return: The resources of this CheckpointParam.
        :rtype: list[str]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this CheckpointParam.

        :param resources: The resources of this CheckpointParam.
        :type resources: list[str]
        """
        self._resources = resources

    @property
    def resource_details(self):
        """Gets the resource_details of this CheckpointParam.

        :return: The resource_details of this CheckpointParam.
        :rtype: list[:class:`g42cloudsdkcbr.v1.Resource`]
        """
        return self._resource_details

    @resource_details.setter
    def resource_details(self, resource_details):
        """Sets the resource_details of this CheckpointParam.

        :param resource_details: The resource_details of this CheckpointParam.
        :type resource_details: list[:class:`g42cloudsdkcbr.v1.Resource`]
        """
        self._resource_details = resource_details

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
        if not isinstance(other, CheckpointParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
