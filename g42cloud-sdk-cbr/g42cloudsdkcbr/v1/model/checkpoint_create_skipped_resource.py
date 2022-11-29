# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckpointCreateSkippedResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'type': 'str',
        'name': 'str',
        'code': 'str',
        'reason': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'name': 'name',
        'code': 'code',
        'reason': 'reason'
    }

    def __init__(self, id=None, type=None, name=None, code=None, reason=None):
        """CheckpointCreateSkippedResource

        The model defined in g42cloud sdk

        :param id: The param of the CheckpointCreateSkippedResource
        :type id: str
        :param type: The param of the CheckpointCreateSkippedResource
        :type type: str
        :param name: The param of the CheckpointCreateSkippedResource
        :type name: str
        :param code: The param of the CheckpointCreateSkippedResource
        :type code: str
        :param reason: The param of the CheckpointCreateSkippedResource
        :type reason: str
        """
        
        

        self._id = None
        self._type = None
        self._name = None
        self._code = None
        self._reason = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if name is not None:
            self.name = name
        if code is not None:
            self.code = code
        if reason is not None:
            self.reason = reason

    @property
    def id(self):
        """Gets the id of this CheckpointCreateSkippedResource.

        :return: The id of this CheckpointCreateSkippedResource.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CheckpointCreateSkippedResource.

        :param id: The id of this CheckpointCreateSkippedResource.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        """Gets the type of this CheckpointCreateSkippedResource.

        :return: The type of this CheckpointCreateSkippedResource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CheckpointCreateSkippedResource.

        :param type: The type of this CheckpointCreateSkippedResource.
        :type type: str
        """
        self._type = type

    @property
    def name(self):
        """Gets the name of this CheckpointCreateSkippedResource.

        :return: The name of this CheckpointCreateSkippedResource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CheckpointCreateSkippedResource.

        :param name: The name of this CheckpointCreateSkippedResource.
        :type name: str
        """
        self._name = name

    @property
    def code(self):
        """Gets the code of this CheckpointCreateSkippedResource.

        :return: The code of this CheckpointCreateSkippedResource.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this CheckpointCreateSkippedResource.

        :param code: The code of this CheckpointCreateSkippedResource.
        :type code: str
        """
        self._code = code

    @property
    def reason(self):
        """Gets the reason of this CheckpointCreateSkippedResource.

        :return: The reason of this CheckpointCreateSkippedResource.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this CheckpointCreateSkippedResource.

        :param reason: The reason of this CheckpointCreateSkippedResource.
        :type reason: str
        """
        self._reason = reason

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
        if not isinstance(other, CheckpointCreateSkippedResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
