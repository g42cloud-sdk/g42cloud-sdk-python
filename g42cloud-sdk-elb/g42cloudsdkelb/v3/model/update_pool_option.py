# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePoolOption:

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
        'description': 'str',
        'lb_algorithm': 'str',
        'name': 'str',
        'session_persistence': 'UpdatePoolSessionPersistenceOption',
        'slow_start': 'UpdatePoolSlowStartOption',
        'member_deletion_protection_enable': 'bool',
        'vpc_id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'admin_state_up': 'admin_state_up',
        'description': 'description',
        'lb_algorithm': 'lb_algorithm',
        'name': 'name',
        'session_persistence': 'session_persistence',
        'slow_start': 'slow_start',
        'member_deletion_protection_enable': 'member_deletion_protection_enable',
        'vpc_id': 'vpc_id',
        'type': 'type'
    }

    def __init__(self, admin_state_up=None, description=None, lb_algorithm=None, name=None, session_persistence=None, slow_start=None, member_deletion_protection_enable=None, vpc_id=None, type=None):
        """UpdatePoolOption

        The model defined in g42cloud sdk

        :param admin_state_up: The param of the UpdatePoolOption
        :type admin_state_up: bool
        :param description: The param of the UpdatePoolOption
        :type description: str
        :param lb_algorithm: The param of the UpdatePoolOption
        :type lb_algorithm: str
        :param name: The param of the UpdatePoolOption
        :type name: str
        :param session_persistence: The param of the UpdatePoolOption
        :type session_persistence: :class:`g42cloudsdkelb.v3.UpdatePoolSessionPersistenceOption`
        :param slow_start: The param of the UpdatePoolOption
        :type slow_start: :class:`g42cloudsdkelb.v3.UpdatePoolSlowStartOption`
        :param member_deletion_protection_enable: The param of the UpdatePoolOption
        :type member_deletion_protection_enable: bool
        :param vpc_id: The param of the UpdatePoolOption
        :type vpc_id: str
        :param type: The param of the UpdatePoolOption
        :type type: str
        """
        
        

        self._admin_state_up = None
        self._description = None
        self._lb_algorithm = None
        self._name = None
        self._session_persistence = None
        self._slow_start = None
        self._member_deletion_protection_enable = None
        self._vpc_id = None
        self._type = None
        self.discriminator = None

        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if description is not None:
            self.description = description
        if lb_algorithm is not None:
            self.lb_algorithm = lb_algorithm
        if name is not None:
            self.name = name
        if session_persistence is not None:
            self.session_persistence = session_persistence
        if slow_start is not None:
            self.slow_start = slow_start
        if member_deletion_protection_enable is not None:
            self.member_deletion_protection_enable = member_deletion_protection_enable
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if type is not None:
            self.type = type

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this UpdatePoolOption.

        :return: The admin_state_up of this UpdatePoolOption.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this UpdatePoolOption.

        :param admin_state_up: The admin_state_up of this UpdatePoolOption.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def description(self):
        """Gets the description of this UpdatePoolOption.

        :return: The description of this UpdatePoolOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdatePoolOption.

        :param description: The description of this UpdatePoolOption.
        :type description: str
        """
        self._description = description

    @property
    def lb_algorithm(self):
        """Gets the lb_algorithm of this UpdatePoolOption.

        :return: The lb_algorithm of this UpdatePoolOption.
        :rtype: str
        """
        return self._lb_algorithm

    @lb_algorithm.setter
    def lb_algorithm(self, lb_algorithm):
        """Sets the lb_algorithm of this UpdatePoolOption.

        :param lb_algorithm: The lb_algorithm of this UpdatePoolOption.
        :type lb_algorithm: str
        """
        self._lb_algorithm = lb_algorithm

    @property
    def name(self):
        """Gets the name of this UpdatePoolOption.

        :return: The name of this UpdatePoolOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdatePoolOption.

        :param name: The name of this UpdatePoolOption.
        :type name: str
        """
        self._name = name

    @property
    def session_persistence(self):
        """Gets the session_persistence of this UpdatePoolOption.

        :return: The session_persistence of this UpdatePoolOption.
        :rtype: :class:`g42cloudsdkelb.v3.UpdatePoolSessionPersistenceOption`
        """
        return self._session_persistence

    @session_persistence.setter
    def session_persistence(self, session_persistence):
        """Sets the session_persistence of this UpdatePoolOption.

        :param session_persistence: The session_persistence of this UpdatePoolOption.
        :type session_persistence: :class:`g42cloudsdkelb.v3.UpdatePoolSessionPersistenceOption`
        """
        self._session_persistence = session_persistence

    @property
    def slow_start(self):
        """Gets the slow_start of this UpdatePoolOption.

        :return: The slow_start of this UpdatePoolOption.
        :rtype: :class:`g42cloudsdkelb.v3.UpdatePoolSlowStartOption`
        """
        return self._slow_start

    @slow_start.setter
    def slow_start(self, slow_start):
        """Sets the slow_start of this UpdatePoolOption.

        :param slow_start: The slow_start of this UpdatePoolOption.
        :type slow_start: :class:`g42cloudsdkelb.v3.UpdatePoolSlowStartOption`
        """
        self._slow_start = slow_start

    @property
    def member_deletion_protection_enable(self):
        """Gets the member_deletion_protection_enable of this UpdatePoolOption.

        :return: The member_deletion_protection_enable of this UpdatePoolOption.
        :rtype: bool
        """
        return self._member_deletion_protection_enable

    @member_deletion_protection_enable.setter
    def member_deletion_protection_enable(self, member_deletion_protection_enable):
        """Sets the member_deletion_protection_enable of this UpdatePoolOption.

        :param member_deletion_protection_enable: The member_deletion_protection_enable of this UpdatePoolOption.
        :type member_deletion_protection_enable: bool
        """
        self._member_deletion_protection_enable = member_deletion_protection_enable

    @property
    def vpc_id(self):
        """Gets the vpc_id of this UpdatePoolOption.

        :return: The vpc_id of this UpdatePoolOption.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this UpdatePoolOption.

        :param vpc_id: The vpc_id of this UpdatePoolOption.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def type(self):
        """Gets the type of this UpdatePoolOption.

        :return: The type of this UpdatePoolOption.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UpdatePoolOption.

        :param type: The type of this UpdatePoolOption.
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
        if not isinstance(other, UpdatePoolOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
