# coding: utf-8

import six

from g42cloudsdkcore.sdk_response import SdkResponse
from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class GlanceListImageMemberSchemasResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'links': 'list[Links]',
        'name': 'str',
        'properties': 'object'
    }

    attribute_map = {
        'links': 'links',
        'name': 'name',
        'properties': 'properties'
    }

    def __init__(self, links=None, name=None, properties=None):
        """GlanceListImageMemberSchemasResponse

        The model defined in g42cloud sdk

        :param links: The param of the GlanceListImageMemberSchemasResponse
        :type links: list[:class:`g42cloudsdkims.v2.Links`]
        :param name: The param of the GlanceListImageMemberSchemasResponse
        :type name: str
        :param properties: The param of the GlanceListImageMemberSchemasResponse
        :type properties: object
        """
        
        super(GlanceListImageMemberSchemasResponse, self).__init__()

        self._links = None
        self._name = None
        self._properties = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if name is not None:
            self.name = name
        if properties is not None:
            self.properties = properties

    @property
    def links(self):
        """Gets the links of this GlanceListImageMemberSchemasResponse.

        :return: The links of this GlanceListImageMemberSchemasResponse.
        :rtype: list[:class:`g42cloudsdkims.v2.Links`]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this GlanceListImageMemberSchemasResponse.

        :param links: The links of this GlanceListImageMemberSchemasResponse.
        :type links: list[:class:`g42cloudsdkims.v2.Links`]
        """
        self._links = links

    @property
    def name(self):
        """Gets the name of this GlanceListImageMemberSchemasResponse.

        :return: The name of this GlanceListImageMemberSchemasResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GlanceListImageMemberSchemasResponse.

        :param name: The name of this GlanceListImageMemberSchemasResponse.
        :type name: str
        """
        self._name = name

    @property
    def properties(self):
        """Gets the properties of this GlanceListImageMemberSchemasResponse.

        :return: The properties of this GlanceListImageMemberSchemasResponse.
        :rtype: object
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this GlanceListImageMemberSchemasResponse.

        :param properties: The properties of this GlanceListImageMemberSchemasResponse.
        :type properties: object
        """
        self._properties = properties

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
        if not isinstance(other, GlanceListImageMemberSchemasResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
