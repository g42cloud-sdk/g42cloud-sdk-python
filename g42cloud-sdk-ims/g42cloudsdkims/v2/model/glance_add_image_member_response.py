# coding: utf-8

import six

from g42cloudsdkcore.sdk_response import SdkResponse
from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class GlanceAddImageMemberResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'image_id': 'str',
        'member_id': 'str',
        'schema': 'str'
    }

    attribute_map = {
        'status': 'status',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'image_id': 'image_id',
        'member_id': 'member_id',
        'schema': 'schema'
    }

    def __init__(self, status=None, created_at=None, updated_at=None, image_id=None, member_id=None, schema=None):
        """GlanceAddImageMemberResponse

        The model defined in g42cloud sdk

        :param status: The param of the GlanceAddImageMemberResponse
        :type status: str
        :param created_at: The param of the GlanceAddImageMemberResponse
        :type created_at: str
        :param updated_at: The param of the GlanceAddImageMemberResponse
        :type updated_at: str
        :param image_id: The param of the GlanceAddImageMemberResponse
        :type image_id: str
        :param member_id: The param of the GlanceAddImageMemberResponse
        :type member_id: str
        :param schema: The param of the GlanceAddImageMemberResponse
        :type schema: str
        """
        
        super(GlanceAddImageMemberResponse, self).__init__()

        self._status = None
        self._created_at = None
        self._updated_at = None
        self._image_id = None
        self._member_id = None
        self._schema = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if image_id is not None:
            self.image_id = image_id
        if member_id is not None:
            self.member_id = member_id
        if schema is not None:
            self.schema = schema

    @property
    def status(self):
        """Gets the status of this GlanceAddImageMemberResponse.

        :return: The status of this GlanceAddImageMemberResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GlanceAddImageMemberResponse.

        :param status: The status of this GlanceAddImageMemberResponse.
        :type status: str
        """
        self._status = status

    @property
    def created_at(self):
        """Gets the created_at of this GlanceAddImageMemberResponse.

        :return: The created_at of this GlanceAddImageMemberResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this GlanceAddImageMemberResponse.

        :param created_at: The created_at of this GlanceAddImageMemberResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this GlanceAddImageMemberResponse.

        :return: The updated_at of this GlanceAddImageMemberResponse.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this GlanceAddImageMemberResponse.

        :param updated_at: The updated_at of this GlanceAddImageMemberResponse.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def image_id(self):
        """Gets the image_id of this GlanceAddImageMemberResponse.

        :return: The image_id of this GlanceAddImageMemberResponse.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this GlanceAddImageMemberResponse.

        :param image_id: The image_id of this GlanceAddImageMemberResponse.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def member_id(self):
        """Gets the member_id of this GlanceAddImageMemberResponse.

        :return: The member_id of this GlanceAddImageMemberResponse.
        :rtype: str
        """
        return self._member_id

    @member_id.setter
    def member_id(self, member_id):
        """Sets the member_id of this GlanceAddImageMemberResponse.

        :param member_id: The member_id of this GlanceAddImageMemberResponse.
        :type member_id: str
        """
        self._member_id = member_id

    @property
    def schema(self):
        """Gets the schema of this GlanceAddImageMemberResponse.

        :return: The schema of this GlanceAddImageMemberResponse.
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this GlanceAddImageMemberResponse.

        :param schema: The schema of this GlanceAddImageMemberResponse.
        :type schema: str
        """
        self._schema = schema

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
        if not isinstance(other, GlanceAddImageMemberResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
