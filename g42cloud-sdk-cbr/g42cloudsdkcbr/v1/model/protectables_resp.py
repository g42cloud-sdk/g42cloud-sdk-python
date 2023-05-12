# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProtectablesResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'children': 'list[object]',
        'detail': 'object',
        'id': 'str',
        'name': 'str',
        'protectable': 'ProtectableResult',
        'size': 'int',
        'status': 'str',
        'type': 'str'
    }

    attribute_map = {
        'children': 'children',
        'detail': 'detail',
        'id': 'id',
        'name': 'name',
        'protectable': 'protectable',
        'size': 'size',
        'status': 'status',
        'type': 'type'
    }

    def __init__(self, children=None, detail=None, id=None, name=None, protectable=None, size=None, status=None, type=None):
        """ProtectablesResp

        The model defined in g42cloud sdk

        :param children: The param of the ProtectablesResp
        :type children: list[object]
        :param detail: The param of the ProtectablesResp
        :type detail: object
        :param id: The param of the ProtectablesResp
        :type id: str
        :param name: The param of the ProtectablesResp
        :type name: str
        :param protectable: The param of the ProtectablesResp
        :type protectable: :class:`g42cloudsdkcbr.v1.ProtectableResult`
        :param size: The param of the ProtectablesResp
        :type size: int
        :param status: The param of the ProtectablesResp
        :type status: str
        :param type: The param of the ProtectablesResp
        :type type: str
        """
        
        

        self._children = None
        self._detail = None
        self._id = None
        self._name = None
        self._protectable = None
        self._size = None
        self._status = None
        self._type = None
        self.discriminator = None

        self.children = children
        if detail is not None:
            self.detail = detail
        self.id = id
        self.name = name
        self.protectable = protectable
        if size is not None:
            self.size = size
        if status is not None:
            self.status = status
        self.type = type

    @property
    def children(self):
        """Gets the children of this ProtectablesResp.

        :return: The children of this ProtectablesResp.
        :rtype: list[object]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this ProtectablesResp.

        :param children: The children of this ProtectablesResp.
        :type children: list[object]
        """
        self._children = children

    @property
    def detail(self):
        """Gets the detail of this ProtectablesResp.

        :return: The detail of this ProtectablesResp.
        :rtype: object
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this ProtectablesResp.

        :param detail: The detail of this ProtectablesResp.
        :type detail: object
        """
        self._detail = detail

    @property
    def id(self):
        """Gets the id of this ProtectablesResp.

        :return: The id of this ProtectablesResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProtectablesResp.

        :param id: The id of this ProtectablesResp.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ProtectablesResp.

        :return: The name of this ProtectablesResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProtectablesResp.

        :param name: The name of this ProtectablesResp.
        :type name: str
        """
        self._name = name

    @property
    def protectable(self):
        """Gets the protectable of this ProtectablesResp.

        :return: The protectable of this ProtectablesResp.
        :rtype: :class:`g42cloudsdkcbr.v1.ProtectableResult`
        """
        return self._protectable

    @protectable.setter
    def protectable(self, protectable):
        """Sets the protectable of this ProtectablesResp.

        :param protectable: The protectable of this ProtectablesResp.
        :type protectable: :class:`g42cloudsdkcbr.v1.ProtectableResult`
        """
        self._protectable = protectable

    @property
    def size(self):
        """Gets the size of this ProtectablesResp.

        :return: The size of this ProtectablesResp.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ProtectablesResp.

        :param size: The size of this ProtectablesResp.
        :type size: int
        """
        self._size = size

    @property
    def status(self):
        """Gets the status of this ProtectablesResp.

        :return: The status of this ProtectablesResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ProtectablesResp.

        :param status: The status of this ProtectablesResp.
        :type status: str
        """
        self._status = status

    @property
    def type(self):
        """Gets the type of this ProtectablesResp.

        :return: The type of this ProtectablesResp.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ProtectablesResp.

        :param type: The type of this ProtectablesResp.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ProtectablesResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
