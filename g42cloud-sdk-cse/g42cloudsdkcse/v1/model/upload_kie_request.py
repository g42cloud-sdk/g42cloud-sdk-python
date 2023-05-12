# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadKieRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_enterprise_project_id': 'str',
        'x_engine_id': 'str',
        'override': 'str',
        'label': 'str',
        'body': 'UploadKieRequestBody'
    }

    attribute_map = {
        'x_enterprise_project_id': 'X-Enterprise-Project-ID',
        'x_engine_id': 'x-engine-id',
        'override': 'override',
        'label': 'label',
        'body': 'body'
    }

    def __init__(self, x_enterprise_project_id=None, x_engine_id=None, override=None, label=None, body=None):
        """UploadKieRequest

        The model defined in g42cloud sdk

        :param x_enterprise_project_id: The param of the UploadKieRequest
        :type x_enterprise_project_id: str
        :param x_engine_id: The param of the UploadKieRequest
        :type x_engine_id: str
        :param override: The param of the UploadKieRequest
        :type override: str
        :param label: The param of the UploadKieRequest
        :type label: str
        :param body: The param of the UploadKieRequest
        :type body: :class:`g42cloudsdkcse.v1.UploadKieRequestBody`
        """
        
        

        self._x_enterprise_project_id = None
        self._x_engine_id = None
        self._override = None
        self._label = None
        self._body = None
        self.discriminator = None

        if x_enterprise_project_id is not None:
            self.x_enterprise_project_id = x_enterprise_project_id
        self.x_engine_id = x_engine_id
        self.override = override
        if label is not None:
            self.label = label
        if body is not None:
            self.body = body

    @property
    def x_enterprise_project_id(self):
        """Gets the x_enterprise_project_id of this UploadKieRequest.

        :return: The x_enterprise_project_id of this UploadKieRequest.
        :rtype: str
        """
        return self._x_enterprise_project_id

    @x_enterprise_project_id.setter
    def x_enterprise_project_id(self, x_enterprise_project_id):
        """Sets the x_enterprise_project_id of this UploadKieRequest.

        :param x_enterprise_project_id: The x_enterprise_project_id of this UploadKieRequest.
        :type x_enterprise_project_id: str
        """
        self._x_enterprise_project_id = x_enterprise_project_id

    @property
    def x_engine_id(self):
        """Gets the x_engine_id of this UploadKieRequest.

        :return: The x_engine_id of this UploadKieRequest.
        :rtype: str
        """
        return self._x_engine_id

    @x_engine_id.setter
    def x_engine_id(self, x_engine_id):
        """Sets the x_engine_id of this UploadKieRequest.

        :param x_engine_id: The x_engine_id of this UploadKieRequest.
        :type x_engine_id: str
        """
        self._x_engine_id = x_engine_id

    @property
    def override(self):
        """Gets the override of this UploadKieRequest.

        :return: The override of this UploadKieRequest.
        :rtype: str
        """
        return self._override

    @override.setter
    def override(self, override):
        """Sets the override of this UploadKieRequest.

        :param override: The override of this UploadKieRequest.
        :type override: str
        """
        self._override = override

    @property
    def label(self):
        """Gets the label of this UploadKieRequest.

        :return: The label of this UploadKieRequest.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this UploadKieRequest.

        :param label: The label of this UploadKieRequest.
        :type label: str
        """
        self._label = label

    @property
    def body(self):
        """Gets the body of this UploadKieRequest.

        :return: The body of this UploadKieRequest.
        :rtype: :class:`g42cloudsdkcse.v1.UploadKieRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UploadKieRequest.

        :param body: The body of this UploadKieRequest.
        :type body: :class:`g42cloudsdkcse.v1.UploadKieRequestBody`
        """
        self._body = body

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
        if not isinstance(other, UploadKieRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
