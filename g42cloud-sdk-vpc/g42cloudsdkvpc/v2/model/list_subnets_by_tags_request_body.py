# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSubnetsByTagsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'limit': 'int',
        'offset': 'int',
        'matches': 'list[Match]',
        'tags': 'list[ListTag]'
    }

    attribute_map = {
        'action': 'action',
        'limit': 'limit',
        'offset': 'offset',
        'matches': 'matches',
        'tags': 'tags'
    }

    def __init__(self, action=None, limit=None, offset=None, matches=None, tags=None):
        """ListSubnetsByTagsRequestBody

        The model defined in g42cloud sdk

        :param action: The param of the ListSubnetsByTagsRequestBody
        :type action: str
        :param limit: The param of the ListSubnetsByTagsRequestBody
        :type limit: int
        :param offset: The param of the ListSubnetsByTagsRequestBody
        :type offset: int
        :param matches: The param of the ListSubnetsByTagsRequestBody
        :type matches: list[:class:`g42cloudsdkvpc.v2.Match`]
        :param tags: The param of the ListSubnetsByTagsRequestBody
        :type tags: list[:class:`g42cloudsdkvpc.v2.ListTag`]
        """
        
        

        self._action = None
        self._limit = None
        self._offset = None
        self._matches = None
        self._tags = None
        self.discriminator = None

        self.action = action
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if matches is not None:
            self.matches = matches
        if tags is not None:
            self.tags = tags

    @property
    def action(self):
        """Gets the action of this ListSubnetsByTagsRequestBody.

        :return: The action of this ListSubnetsByTagsRequestBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ListSubnetsByTagsRequestBody.

        :param action: The action of this ListSubnetsByTagsRequestBody.
        :type action: str
        """
        self._action = action

    @property
    def limit(self):
        """Gets the limit of this ListSubnetsByTagsRequestBody.

        :return: The limit of this ListSubnetsByTagsRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListSubnetsByTagsRequestBody.

        :param limit: The limit of this ListSubnetsByTagsRequestBody.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListSubnetsByTagsRequestBody.

        :return: The offset of this ListSubnetsByTagsRequestBody.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListSubnetsByTagsRequestBody.

        :param offset: The offset of this ListSubnetsByTagsRequestBody.
        :type offset: int
        """
        self._offset = offset

    @property
    def matches(self):
        """Gets the matches of this ListSubnetsByTagsRequestBody.

        :return: The matches of this ListSubnetsByTagsRequestBody.
        :rtype: list[:class:`g42cloudsdkvpc.v2.Match`]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        """Sets the matches of this ListSubnetsByTagsRequestBody.

        :param matches: The matches of this ListSubnetsByTagsRequestBody.
        :type matches: list[:class:`g42cloudsdkvpc.v2.Match`]
        """
        self._matches = matches

    @property
    def tags(self):
        """Gets the tags of this ListSubnetsByTagsRequestBody.

        :return: The tags of this ListSubnetsByTagsRequestBody.
        :rtype: list[:class:`g42cloudsdkvpc.v2.ListTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListSubnetsByTagsRequestBody.

        :param tags: The tags of this ListSubnetsByTagsRequestBody.
        :type tags: list[:class:`g42cloudsdkvpc.v2.ListTag`]
        """
        self._tags = tags

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
        if not isinstance(other, ListSubnetsByTagsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
