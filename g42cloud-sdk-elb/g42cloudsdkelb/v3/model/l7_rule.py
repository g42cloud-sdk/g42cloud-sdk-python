# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class L7Rule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'admin_state_up': 'bool',
        'compare_type': 'str',
        'key': 'str',
        'project_id': 'str',
        'type': 'str',
        'value': 'str',
        'provisioning_status': 'str',
        'invert': 'bool',
        'id': 'str',
        'conditions': 'list[RuleCondition]',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'admin_state_up': 'admin_state_up',
        'compare_type': 'compare_type',
        'key': 'key',
        'project_id': 'project_id',
        'type': 'type',
        'value': 'value',
        'provisioning_status': 'provisioning_status',
        'invert': 'invert',
        'id': 'id',
        'conditions': 'conditions',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, admin_state_up=None, compare_type=None, key=None, project_id=None, type=None, value=None, provisioning_status=None, invert=None, id=None, conditions=None, created_at=None, updated_at=None):
        """L7Rule

        The model defined in g42cloud sdk

        :param admin_state_up: The param of the L7Rule
        :type admin_state_up: bool
        :param compare_type: The param of the L7Rule
        :type compare_type: str
        :param key: The param of the L7Rule
        :type key: str
        :param project_id: The param of the L7Rule
        :type project_id: str
        :param type: The param of the L7Rule
        :type type: str
        :param value: The param of the L7Rule
        :type value: str
        :param provisioning_status: The param of the L7Rule
        :type provisioning_status: str
        :param invert: The param of the L7Rule
        :type invert: bool
        :param id: The param of the L7Rule
        :type id: str
        :param conditions: The param of the L7Rule
        :type conditions: list[:class:`g42cloudsdkelb.v3.RuleCondition`]
        :param created_at: The param of the L7Rule
        :type created_at: str
        :param updated_at: The param of the L7Rule
        :type updated_at: str
        """
        
        

        self._admin_state_up = None
        self._compare_type = None
        self._key = None
        self._project_id = None
        self._type = None
        self._value = None
        self._provisioning_status = None
        self._invert = None
        self._id = None
        self._conditions = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.admin_state_up = admin_state_up
        self.compare_type = compare_type
        self.key = key
        self.project_id = project_id
        self.type = type
        self.value = value
        self.provisioning_status = provisioning_status
        self.invert = invert
        self.id = id
        self.conditions = conditions
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this L7Rule.

        :return: The admin_state_up of this L7Rule.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this L7Rule.

        :param admin_state_up: The admin_state_up of this L7Rule.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def compare_type(self):
        """Gets the compare_type of this L7Rule.

        :return: The compare_type of this L7Rule.
        :rtype: str
        """
        return self._compare_type

    @compare_type.setter
    def compare_type(self, compare_type):
        """Sets the compare_type of this L7Rule.

        :param compare_type: The compare_type of this L7Rule.
        :type compare_type: str
        """
        self._compare_type = compare_type

    @property
    def key(self):
        """Gets the key of this L7Rule.

        :return: The key of this L7Rule.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this L7Rule.

        :param key: The key of this L7Rule.
        :type key: str
        """
        self._key = key

    @property
    def project_id(self):
        """Gets the project_id of this L7Rule.

        :return: The project_id of this L7Rule.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this L7Rule.

        :param project_id: The project_id of this L7Rule.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def type(self):
        """Gets the type of this L7Rule.

        :return: The type of this L7Rule.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this L7Rule.

        :param type: The type of this L7Rule.
        :type type: str
        """
        self._type = type

    @property
    def value(self):
        """Gets the value of this L7Rule.

        :return: The value of this L7Rule.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this L7Rule.

        :param value: The value of this L7Rule.
        :type value: str
        """
        self._value = value

    @property
    def provisioning_status(self):
        """Gets the provisioning_status of this L7Rule.

        :return: The provisioning_status of this L7Rule.
        :rtype: str
        """
        return self._provisioning_status

    @provisioning_status.setter
    def provisioning_status(self, provisioning_status):
        """Sets the provisioning_status of this L7Rule.

        :param provisioning_status: The provisioning_status of this L7Rule.
        :type provisioning_status: str
        """
        self._provisioning_status = provisioning_status

    @property
    def invert(self):
        """Gets the invert of this L7Rule.

        :return: The invert of this L7Rule.
        :rtype: bool
        """
        return self._invert

    @invert.setter
    def invert(self, invert):
        """Sets the invert of this L7Rule.

        :param invert: The invert of this L7Rule.
        :type invert: bool
        """
        self._invert = invert

    @property
    def id(self):
        """Gets the id of this L7Rule.

        :return: The id of this L7Rule.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this L7Rule.

        :param id: The id of this L7Rule.
        :type id: str
        """
        self._id = id

    @property
    def conditions(self):
        """Gets the conditions of this L7Rule.

        :return: The conditions of this L7Rule.
        :rtype: list[:class:`g42cloudsdkelb.v3.RuleCondition`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this L7Rule.

        :param conditions: The conditions of this L7Rule.
        :type conditions: list[:class:`g42cloudsdkelb.v3.RuleCondition`]
        """
        self._conditions = conditions

    @property
    def created_at(self):
        """Gets the created_at of this L7Rule.

        :return: The created_at of this L7Rule.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this L7Rule.

        :param created_at: The created_at of this L7Rule.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this L7Rule.

        :return: The updated_at of this L7Rule.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this L7Rule.

        :param updated_at: The updated_at of this L7Rule.
        :type updated_at: str
        """
        self._updated_at = updated_at

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
        if not isinstance(other, L7Rule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
