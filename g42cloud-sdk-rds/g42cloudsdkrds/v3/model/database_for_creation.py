# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DatabaseForCreation:

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
        'character_set': 'str',
        'comment': 'str'
    }

    attribute_map = {
        'name': 'name',
        'character_set': 'character_set',
        'comment': 'comment'
    }

    def __init__(self, name=None, character_set=None, comment=None):
        """DatabaseForCreation

        The model defined in g42cloud sdk

        :param name: The param of the DatabaseForCreation
        :type name: str
        :param character_set: The param of the DatabaseForCreation
        :type character_set: str
        :param comment: The param of the DatabaseForCreation
        :type comment: str
        """
        
        

        self._name = None
        self._character_set = None
        self._comment = None
        self.discriminator = None

        self.name = name
        self.character_set = character_set
        if comment is not None:
            self.comment = comment

    @property
    def name(self):
        """Gets the name of this DatabaseForCreation.

        :return: The name of this DatabaseForCreation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DatabaseForCreation.

        :param name: The name of this DatabaseForCreation.
        :type name: str
        """
        self._name = name

    @property
    def character_set(self):
        """Gets the character_set of this DatabaseForCreation.

        :return: The character_set of this DatabaseForCreation.
        :rtype: str
        """
        return self._character_set

    @character_set.setter
    def character_set(self, character_set):
        """Sets the character_set of this DatabaseForCreation.

        :param character_set: The character_set of this DatabaseForCreation.
        :type character_set: str
        """
        self._character_set = character_set

    @property
    def comment(self):
        """Gets the comment of this DatabaseForCreation.

        :return: The comment of this DatabaseForCreation.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this DatabaseForCreation.

        :param comment: The comment of this DatabaseForCreation.
        :type comment: str
        """
        self._comment = comment

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
        if not isinstance(other, DatabaseForCreation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
