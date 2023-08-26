# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tags': 'list[ResourceTags]',
        'tags_any': 'list[ResourceTags]',
        'not_tags': 'list[ResourceTags]',
        'not_tags_any': 'list[ResourceTags]',
        'offset': 'str',
        'limit': 'str',
        'action': 'str',
        'matches': 'list[TagMatch]'
    }

    attribute_map = {
        'tags': 'tags',
        'tags_any': 'tags_any',
        'not_tags': 'not_tags',
        'not_tags_any': 'not_tags_any',
        'offset': 'offset',
        'limit': 'limit',
        'action': 'action',
        'matches': 'matches'
    }

    def __init__(self, tags=None, tags_any=None, not_tags=None, not_tags_any=None, offset=None, limit=None, action=None, matches=None):
        """ListInstanceRequestBody

        The model defined in g42cloud sdk

        :param tags: The param of the ListInstanceRequestBody
        :type tags: list[:class:`g42cloudsdksmn.v2.ResourceTags`]
        :param tags_any: The param of the ListInstanceRequestBody
        :type tags_any: list[:class:`g42cloudsdksmn.v2.ResourceTags`]
        :param not_tags: The param of the ListInstanceRequestBody
        :type not_tags: list[:class:`g42cloudsdksmn.v2.ResourceTags`]
        :param not_tags_any: The param of the ListInstanceRequestBody
        :type not_tags_any: list[:class:`g42cloudsdksmn.v2.ResourceTags`]
        :param offset: The param of the ListInstanceRequestBody
        :type offset: str
        :param limit: The param of the ListInstanceRequestBody
        :type limit: str
        :param action: The param of the ListInstanceRequestBody
        :type action: str
        :param matches: The param of the ListInstanceRequestBody
        :type matches: list[:class:`g42cloudsdksmn.v2.TagMatch`]
        """
        
        

        self._tags = None
        self._tags_any = None
        self._not_tags = None
        self._not_tags_any = None
        self._offset = None
        self._limit = None
        self._action = None
        self._matches = None
        self.discriminator = None

        if tags is not None:
            self.tags = tags
        if tags_any is not None:
            self.tags_any = tags_any
        if not_tags is not None:
            self.not_tags = not_tags
        if not_tags_any is not None:
            self.not_tags_any = not_tags_any
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        self.action = action
        if matches is not None:
            self.matches = matches

    @property
    def tags(self):
        """Gets the tags of this ListInstanceRequestBody.

        :return: The tags of this ListInstanceRequestBody.
        :rtype: list[:class:`g42cloudsdksmn.v2.ResourceTags`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListInstanceRequestBody.

        :param tags: The tags of this ListInstanceRequestBody.
        :type tags: list[:class:`g42cloudsdksmn.v2.ResourceTags`]
        """
        self._tags = tags

    @property
    def tags_any(self):
        """Gets the tags_any of this ListInstanceRequestBody.

        :return: The tags_any of this ListInstanceRequestBody.
        :rtype: list[:class:`g42cloudsdksmn.v2.ResourceTags`]
        """
        return self._tags_any

    @tags_any.setter
    def tags_any(self, tags_any):
        """Sets the tags_any of this ListInstanceRequestBody.

        :param tags_any: The tags_any of this ListInstanceRequestBody.
        :type tags_any: list[:class:`g42cloudsdksmn.v2.ResourceTags`]
        """
        self._tags_any = tags_any

    @property
    def not_tags(self):
        """Gets the not_tags of this ListInstanceRequestBody.

        :return: The not_tags of this ListInstanceRequestBody.
        :rtype: list[:class:`g42cloudsdksmn.v2.ResourceTags`]
        """
        return self._not_tags

    @not_tags.setter
    def not_tags(self, not_tags):
        """Sets the not_tags of this ListInstanceRequestBody.

        :param not_tags: The not_tags of this ListInstanceRequestBody.
        :type not_tags: list[:class:`g42cloudsdksmn.v2.ResourceTags`]
        """
        self._not_tags = not_tags

    @property
    def not_tags_any(self):
        """Gets the not_tags_any of this ListInstanceRequestBody.

        :return: The not_tags_any of this ListInstanceRequestBody.
        :rtype: list[:class:`g42cloudsdksmn.v2.ResourceTags`]
        """
        return self._not_tags_any

    @not_tags_any.setter
    def not_tags_any(self, not_tags_any):
        """Sets the not_tags_any of this ListInstanceRequestBody.

        :param not_tags_any: The not_tags_any of this ListInstanceRequestBody.
        :type not_tags_any: list[:class:`g42cloudsdksmn.v2.ResourceTags`]
        """
        self._not_tags_any = not_tags_any

    @property
    def offset(self):
        """Gets the offset of this ListInstanceRequestBody.

        :return: The offset of this ListInstanceRequestBody.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListInstanceRequestBody.

        :param offset: The offset of this ListInstanceRequestBody.
        :type offset: str
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListInstanceRequestBody.

        :return: The limit of this ListInstanceRequestBody.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListInstanceRequestBody.

        :param limit: The limit of this ListInstanceRequestBody.
        :type limit: str
        """
        self._limit = limit

    @property
    def action(self):
        """Gets the action of this ListInstanceRequestBody.

        :return: The action of this ListInstanceRequestBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ListInstanceRequestBody.

        :param action: The action of this ListInstanceRequestBody.
        :type action: str
        """
        self._action = action

    @property
    def matches(self):
        """Gets the matches of this ListInstanceRequestBody.

        :return: The matches of this ListInstanceRequestBody.
        :rtype: list[:class:`g42cloudsdksmn.v2.TagMatch`]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        """Sets the matches of this ListInstanceRequestBody.

        :param matches: The matches of this ListInstanceRequestBody.
        :type matches: list[:class:`g42cloudsdksmn.v2.TagMatch`]
        """
        self._matches = matches

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
        if not isinstance(other, ListInstanceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
