# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowImageByTagsResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_id': 'str',
        'resource_detail': 'QueryImageByTagsResourceDetail',
        'tags': 'list[TagKeyValue]',
        'resource_name': 'str'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'resource_detail': 'resource_detail',
        'tags': 'tags',
        'resource_name': 'resource_name'
    }

    def __init__(self, resource_id=None, resource_detail=None, tags=None, resource_name=None):
        """ShowImageByTagsResource

        The model defined in g42cloud sdk

        :param resource_id: The param of the ShowImageByTagsResource
        :type resource_id: str
        :param resource_detail: The param of the ShowImageByTagsResource
        :type resource_detail: :class:`g42cloudsdkims.v2.QueryImageByTagsResourceDetail`
        :param tags: The param of the ShowImageByTagsResource
        :type tags: list[:class:`g42cloudsdkims.v2.TagKeyValue`]
        :param resource_name: The param of the ShowImageByTagsResource
        :type resource_name: str
        """
        
        

        self._resource_id = None
        self._resource_detail = None
        self._tags = None
        self._resource_name = None
        self.discriminator = None

        self.resource_id = resource_id
        self.resource_detail = resource_detail
        self.tags = tags
        self.resource_name = resource_name

    @property
    def resource_id(self):
        """Gets the resource_id of this ShowImageByTagsResource.

        :return: The resource_id of this ShowImageByTagsResource.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ShowImageByTagsResource.

        :param resource_id: The resource_id of this ShowImageByTagsResource.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_detail(self):
        """Gets the resource_detail of this ShowImageByTagsResource.

        :return: The resource_detail of this ShowImageByTagsResource.
        :rtype: :class:`g42cloudsdkims.v2.QueryImageByTagsResourceDetail`
        """
        return self._resource_detail

    @resource_detail.setter
    def resource_detail(self, resource_detail):
        """Sets the resource_detail of this ShowImageByTagsResource.

        :param resource_detail: The resource_detail of this ShowImageByTagsResource.
        :type resource_detail: :class:`g42cloudsdkims.v2.QueryImageByTagsResourceDetail`
        """
        self._resource_detail = resource_detail

    @property
    def tags(self):
        """Gets the tags of this ShowImageByTagsResource.

        :return: The tags of this ShowImageByTagsResource.
        :rtype: list[:class:`g42cloudsdkims.v2.TagKeyValue`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ShowImageByTagsResource.

        :param tags: The tags of this ShowImageByTagsResource.
        :type tags: list[:class:`g42cloudsdkims.v2.TagKeyValue`]
        """
        self._tags = tags

    @property
    def resource_name(self):
        """Gets the resource_name of this ShowImageByTagsResource.

        :return: The resource_name of this ShowImageByTagsResource.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this ShowImageByTagsResource.

        :param resource_name: The resource_name of this ShowImageByTagsResource.
        :type resource_name: str
        """
        self._resource_name = resource_name

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
        if not isinstance(other, ShowImageByTagsResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
