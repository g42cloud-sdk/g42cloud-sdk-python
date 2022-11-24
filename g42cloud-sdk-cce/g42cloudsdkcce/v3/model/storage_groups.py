# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StorageGroups:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'cce_managed': 'bool',
        'selector_names': 'list[str]',
        'virtual_spaces': 'list[VirtualSpace]'
    }

    attribute_map = {
        'name': 'name',
        'cce_managed': 'cceManaged',
        'selector_names': 'selectorNames',
        'virtual_spaces': 'virtualSpaces'
    }

    def __init__(self, name=None, cce_managed=None, selector_names=None, virtual_spaces=None):
        """StorageGroups

        The model defined in g42cloud sdk

        :param name: The param of the StorageGroups
        :type name: str
        :param cce_managed: The param of the StorageGroups
        :type cce_managed: bool
        :param selector_names: The param of the StorageGroups
        :type selector_names: list[str]
        :param virtual_spaces: The param of the StorageGroups
        :type virtual_spaces: list[:class:`g42cloudsdkcce.v3.VirtualSpace`]
        """
        
        

        self._name = None
        self._cce_managed = None
        self._selector_names = None
        self._virtual_spaces = None
        self.discriminator = None

        self.name = name
        if cce_managed is not None:
            self.cce_managed = cce_managed
        self.selector_names = selector_names
        self.virtual_spaces = virtual_spaces

    @property
    def name(self):
        """Gets the name of this StorageGroups.

        :return: The name of this StorageGroups.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StorageGroups.

        :param name: The name of this StorageGroups.
        :type name: str
        """
        self._name = name

    @property
    def cce_managed(self):
        """Gets the cce_managed of this StorageGroups.

        :return: The cce_managed of this StorageGroups.
        :rtype: bool
        """
        return self._cce_managed

    @cce_managed.setter
    def cce_managed(self, cce_managed):
        """Sets the cce_managed of this StorageGroups.

        :param cce_managed: The cce_managed of this StorageGroups.
        :type cce_managed: bool
        """
        self._cce_managed = cce_managed

    @property
    def selector_names(self):
        """Gets the selector_names of this StorageGroups.

        :return: The selector_names of this StorageGroups.
        :rtype: list[str]
        """
        return self._selector_names

    @selector_names.setter
    def selector_names(self, selector_names):
        """Sets the selector_names of this StorageGroups.

        :param selector_names: The selector_names of this StorageGroups.
        :type selector_names: list[str]
        """
        self._selector_names = selector_names

    @property
    def virtual_spaces(self):
        """Gets the virtual_spaces of this StorageGroups.

        :return: The virtual_spaces of this StorageGroups.
        :rtype: list[:class:`g42cloudsdkcce.v3.VirtualSpace`]
        """
        return self._virtual_spaces

    @virtual_spaces.setter
    def virtual_spaces(self, virtual_spaces):
        """Sets the virtual_spaces of this StorageGroups.

        :param virtual_spaces: The virtual_spaces of this StorageGroups.
        :type virtual_spaces: list[:class:`g42cloudsdkcce.v3.VirtualSpace`]
        """
        self._virtual_spaces = virtual_spaces

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
        if not isinstance(other, StorageGroups):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
