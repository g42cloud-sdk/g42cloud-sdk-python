# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeSpecUpdate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'taints': 'list[Taint]',
        'k8s_tags': 'dict(str, str)',
        'user_tags': 'list[UserTag]'
    }

    attribute_map = {
        'taints': 'taints',
        'k8s_tags': 'k8sTags',
        'user_tags': 'userTags'
    }

    def __init__(self, taints=None, k8s_tags=None, user_tags=None):
        """NodeSpecUpdate

        The model defined in g42cloud sdk

        :param taints: The param of the NodeSpecUpdate
        :type taints: list[:class:`g42cloudsdkcce.v3.Taint`]
        :param k8s_tags: The param of the NodeSpecUpdate
        :type k8s_tags: dict(str, str)
        :param user_tags: The param of the NodeSpecUpdate
        :type user_tags: list[:class:`g42cloudsdkcce.v3.UserTag`]
        """
        
        

        self._taints = None
        self._k8s_tags = None
        self._user_tags = None
        self.discriminator = None

        self.taints = taints
        self.k8s_tags = k8s_tags
        self.user_tags = user_tags

    @property
    def taints(self):
        """Gets the taints of this NodeSpecUpdate.

        :return: The taints of this NodeSpecUpdate.
        :rtype: list[:class:`g42cloudsdkcce.v3.Taint`]
        """
        return self._taints

    @taints.setter
    def taints(self, taints):
        """Sets the taints of this NodeSpecUpdate.

        :param taints: The taints of this NodeSpecUpdate.
        :type taints: list[:class:`g42cloudsdkcce.v3.Taint`]
        """
        self._taints = taints

    @property
    def k8s_tags(self):
        """Gets the k8s_tags of this NodeSpecUpdate.

        :return: The k8s_tags of this NodeSpecUpdate.
        :rtype: dict(str, str)
        """
        return self._k8s_tags

    @k8s_tags.setter
    def k8s_tags(self, k8s_tags):
        """Sets the k8s_tags of this NodeSpecUpdate.

        :param k8s_tags: The k8s_tags of this NodeSpecUpdate.
        :type k8s_tags: dict(str, str)
        """
        self._k8s_tags = k8s_tags

    @property
    def user_tags(self):
        """Gets the user_tags of this NodeSpecUpdate.

        :return: The user_tags of this NodeSpecUpdate.
        :rtype: list[:class:`g42cloudsdkcce.v3.UserTag`]
        """
        return self._user_tags

    @user_tags.setter
    def user_tags(self, user_tags):
        """Sets the user_tags of this NodeSpecUpdate.

        :param user_tags: The user_tags of this NodeSpecUpdate.
        :type user_tags: list[:class:`g42cloudsdkcce.v3.UserTag`]
        """
        self._user_tags = user_tags

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
        if not isinstance(other, NodeSpecUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
