# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAlarmResponseAlarms:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_id': 'str',
        'name': 'str',
        'description': 'str',
        'namespace': 'str',
        'policies': 'list[Policy]',
        'resources': 'list[ResourcesInListResp]',
        'type': 'str',
        'enabled': 'bool',
        'notification_enabled': 'bool',
        'alarm_notifications': 'list[Notification]',
        'ok_notifications': 'list[Notification]',
        'notification_begin_time': 'str',
        'notification_end_time': 'str',
        'enterprise_project_id': 'str',
        'alarm_template_id': 'str'
    }

    attribute_map = {
        'alarm_id': 'alarm_id',
        'name': 'name',
        'description': 'description',
        'namespace': 'namespace',
        'policies': 'policies',
        'resources': 'resources',
        'type': 'type',
        'enabled': 'enabled',
        'notification_enabled': 'notification_enabled',
        'alarm_notifications': 'alarm_notifications',
        'ok_notifications': 'ok_notifications',
        'notification_begin_time': 'notification_begin_time',
        'notification_end_time': 'notification_end_time',
        'enterprise_project_id': 'enterprise_project_id',
        'alarm_template_id': 'alarm_template_id'
    }

    def __init__(self, alarm_id=None, name=None, description=None, namespace=None, policies=None, resources=None, type=None, enabled=None, notification_enabled=None, alarm_notifications=None, ok_notifications=None, notification_begin_time=None, notification_end_time=None, enterprise_project_id=None, alarm_template_id=None):
        """ListAlarmResponseAlarms

        The model defined in g42cloud sdk

        :param alarm_id: The param of the ListAlarmResponseAlarms
        :type alarm_id: str
        :param name: The param of the ListAlarmResponseAlarms
        :type name: str
        :param description: The param of the ListAlarmResponseAlarms
        :type description: str
        :param namespace: The param of the ListAlarmResponseAlarms
        :type namespace: str
        :param policies: The param of the ListAlarmResponseAlarms
        :type policies: list[:class:`g42cloudsdkces.v2.Policy`]
        :param resources: The param of the ListAlarmResponseAlarms
        :type resources: list[:class:`g42cloudsdkces.v2.ResourcesInListResp`]
        :param type: The param of the ListAlarmResponseAlarms
        :type type: str
        :param enabled: The param of the ListAlarmResponseAlarms
        :type enabled: bool
        :param notification_enabled: The param of the ListAlarmResponseAlarms
        :type notification_enabled: bool
        :param alarm_notifications: The param of the ListAlarmResponseAlarms
        :type alarm_notifications: list[:class:`g42cloudsdkces.v2.Notification`]
        :param ok_notifications: The param of the ListAlarmResponseAlarms
        :type ok_notifications: list[:class:`g42cloudsdkces.v2.Notification`]
        :param notification_begin_time: The param of the ListAlarmResponseAlarms
        :type notification_begin_time: str
        :param notification_end_time: The param of the ListAlarmResponseAlarms
        :type notification_end_time: str
        :param enterprise_project_id: The param of the ListAlarmResponseAlarms
        :type enterprise_project_id: str
        :param alarm_template_id: The param of the ListAlarmResponseAlarms
        :type alarm_template_id: str
        """
        
        

        self._alarm_id = None
        self._name = None
        self._description = None
        self._namespace = None
        self._policies = None
        self._resources = None
        self._type = None
        self._enabled = None
        self._notification_enabled = None
        self._alarm_notifications = None
        self._ok_notifications = None
        self._notification_begin_time = None
        self._notification_end_time = None
        self._enterprise_project_id = None
        self._alarm_template_id = None
        self.discriminator = None

        if alarm_id is not None:
            self.alarm_id = alarm_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if namespace is not None:
            self.namespace = namespace
        if policies is not None:
            self.policies = policies
        if resources is not None:
            self.resources = resources
        if type is not None:
            self.type = type
        if enabled is not None:
            self.enabled = enabled
        if notification_enabled is not None:
            self.notification_enabled = notification_enabled
        if alarm_notifications is not None:
            self.alarm_notifications = alarm_notifications
        if ok_notifications is not None:
            self.ok_notifications = ok_notifications
        if notification_begin_time is not None:
            self.notification_begin_time = notification_begin_time
        if notification_end_time is not None:
            self.notification_end_time = notification_end_time
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if alarm_template_id is not None:
            self.alarm_template_id = alarm_template_id

    @property
    def alarm_id(self):
        """Gets the alarm_id of this ListAlarmResponseAlarms.

        :return: The alarm_id of this ListAlarmResponseAlarms.
        :rtype: str
        """
        return self._alarm_id

    @alarm_id.setter
    def alarm_id(self, alarm_id):
        """Sets the alarm_id of this ListAlarmResponseAlarms.

        :param alarm_id: The alarm_id of this ListAlarmResponseAlarms.
        :type alarm_id: str
        """
        self._alarm_id = alarm_id

    @property
    def name(self):
        """Gets the name of this ListAlarmResponseAlarms.

        :return: The name of this ListAlarmResponseAlarms.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListAlarmResponseAlarms.

        :param name: The name of this ListAlarmResponseAlarms.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ListAlarmResponseAlarms.

        :return: The description of this ListAlarmResponseAlarms.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListAlarmResponseAlarms.

        :param description: The description of this ListAlarmResponseAlarms.
        :type description: str
        """
        self._description = description

    @property
    def namespace(self):
        """Gets the namespace of this ListAlarmResponseAlarms.

        :return: The namespace of this ListAlarmResponseAlarms.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this ListAlarmResponseAlarms.

        :param namespace: The namespace of this ListAlarmResponseAlarms.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def policies(self):
        """Gets the policies of this ListAlarmResponseAlarms.

        :return: The policies of this ListAlarmResponseAlarms.
        :rtype: list[:class:`g42cloudsdkces.v2.Policy`]
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        """Sets the policies of this ListAlarmResponseAlarms.

        :param policies: The policies of this ListAlarmResponseAlarms.
        :type policies: list[:class:`g42cloudsdkces.v2.Policy`]
        """
        self._policies = policies

    @property
    def resources(self):
        """Gets the resources of this ListAlarmResponseAlarms.

        :return: The resources of this ListAlarmResponseAlarms.
        :rtype: list[:class:`g42cloudsdkces.v2.ResourcesInListResp`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this ListAlarmResponseAlarms.

        :param resources: The resources of this ListAlarmResponseAlarms.
        :type resources: list[:class:`g42cloudsdkces.v2.ResourcesInListResp`]
        """
        self._resources = resources

    @property
    def type(self):
        """Gets the type of this ListAlarmResponseAlarms.

        :return: The type of this ListAlarmResponseAlarms.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListAlarmResponseAlarms.

        :param type: The type of this ListAlarmResponseAlarms.
        :type type: str
        """
        self._type = type

    @property
    def enabled(self):
        """Gets the enabled of this ListAlarmResponseAlarms.

        :return: The enabled of this ListAlarmResponseAlarms.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ListAlarmResponseAlarms.

        :param enabled: The enabled of this ListAlarmResponseAlarms.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def notification_enabled(self):
        """Gets the notification_enabled of this ListAlarmResponseAlarms.

        :return: The notification_enabled of this ListAlarmResponseAlarms.
        :rtype: bool
        """
        return self._notification_enabled

    @notification_enabled.setter
    def notification_enabled(self, notification_enabled):
        """Sets the notification_enabled of this ListAlarmResponseAlarms.

        :param notification_enabled: The notification_enabled of this ListAlarmResponseAlarms.
        :type notification_enabled: bool
        """
        self._notification_enabled = notification_enabled

    @property
    def alarm_notifications(self):
        """Gets the alarm_notifications of this ListAlarmResponseAlarms.

        :return: The alarm_notifications of this ListAlarmResponseAlarms.
        :rtype: list[:class:`g42cloudsdkces.v2.Notification`]
        """
        return self._alarm_notifications

    @alarm_notifications.setter
    def alarm_notifications(self, alarm_notifications):
        """Sets the alarm_notifications of this ListAlarmResponseAlarms.

        :param alarm_notifications: The alarm_notifications of this ListAlarmResponseAlarms.
        :type alarm_notifications: list[:class:`g42cloudsdkces.v2.Notification`]
        """
        self._alarm_notifications = alarm_notifications

    @property
    def ok_notifications(self):
        """Gets the ok_notifications of this ListAlarmResponseAlarms.

        :return: The ok_notifications of this ListAlarmResponseAlarms.
        :rtype: list[:class:`g42cloudsdkces.v2.Notification`]
        """
        return self._ok_notifications

    @ok_notifications.setter
    def ok_notifications(self, ok_notifications):
        """Sets the ok_notifications of this ListAlarmResponseAlarms.

        :param ok_notifications: The ok_notifications of this ListAlarmResponseAlarms.
        :type ok_notifications: list[:class:`g42cloudsdkces.v2.Notification`]
        """
        self._ok_notifications = ok_notifications

    @property
    def notification_begin_time(self):
        """Gets the notification_begin_time of this ListAlarmResponseAlarms.

        :return: The notification_begin_time of this ListAlarmResponseAlarms.
        :rtype: str
        """
        return self._notification_begin_time

    @notification_begin_time.setter
    def notification_begin_time(self, notification_begin_time):
        """Sets the notification_begin_time of this ListAlarmResponseAlarms.

        :param notification_begin_time: The notification_begin_time of this ListAlarmResponseAlarms.
        :type notification_begin_time: str
        """
        self._notification_begin_time = notification_begin_time

    @property
    def notification_end_time(self):
        """Gets the notification_end_time of this ListAlarmResponseAlarms.

        :return: The notification_end_time of this ListAlarmResponseAlarms.
        :rtype: str
        """
        return self._notification_end_time

    @notification_end_time.setter
    def notification_end_time(self, notification_end_time):
        """Sets the notification_end_time of this ListAlarmResponseAlarms.

        :param notification_end_time: The notification_end_time of this ListAlarmResponseAlarms.
        :type notification_end_time: str
        """
        self._notification_end_time = notification_end_time

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListAlarmResponseAlarms.

        :return: The enterprise_project_id of this ListAlarmResponseAlarms.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListAlarmResponseAlarms.

        :param enterprise_project_id: The enterprise_project_id of this ListAlarmResponseAlarms.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def alarm_template_id(self):
        """Gets the alarm_template_id of this ListAlarmResponseAlarms.

        :return: The alarm_template_id of this ListAlarmResponseAlarms.
        :rtype: str
        """
        return self._alarm_template_id

    @alarm_template_id.setter
    def alarm_template_id(self, alarm_template_id):
        """Sets the alarm_template_id of this ListAlarmResponseAlarms.

        :param alarm_template_id: The alarm_template_id of this ListAlarmResponseAlarms.
        :type alarm_template_id: str
        """
        self._alarm_template_id = alarm_template_id

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
        if not isinstance(other, ListAlarmResponseAlarms):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
