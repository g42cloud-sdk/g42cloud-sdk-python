# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostAlarmsReqV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'namespace': 'str',
        'resource_group_id': 'str',
        'resources': 'list[list[Dimension]]',
        'policies': 'list[Policy]',
        'type': 'str',
        'alarm_notifications': 'list[Notification]',
        'ok_notifications': 'list[Notification]',
        'notification_begin_time': 'str',
        'notification_end_time': 'str',
        'enterprise_project_id': 'str',
        'enabled': 'bool',
        'notification_enabled': 'bool',
        'alarm_template_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'namespace': 'namespace',
        'resource_group_id': 'resource_group_id',
        'resources': 'resources',
        'policies': 'policies',
        'type': 'type',
        'alarm_notifications': 'alarm_notifications',
        'ok_notifications': 'ok_notifications',
        'notification_begin_time': 'notification_begin_time',
        'notification_end_time': 'notification_end_time',
        'enterprise_project_id': 'enterprise_project_id',
        'enabled': 'enabled',
        'notification_enabled': 'notification_enabled',
        'alarm_template_id': 'alarm_template_id'
    }

    def __init__(self, name=None, description=None, namespace=None, resource_group_id=None, resources=None, policies=None, type=None, alarm_notifications=None, ok_notifications=None, notification_begin_time=None, notification_end_time=None, enterprise_project_id=None, enabled=None, notification_enabled=None, alarm_template_id=None):
        """PostAlarmsReqV2

        The model defined in g42cloud sdk

        :param name: The param of the PostAlarmsReqV2
        :type name: str
        :param description: The param of the PostAlarmsReqV2
        :type description: str
        :param namespace: The param of the PostAlarmsReqV2
        :type namespace: str
        :param resource_group_id: The param of the PostAlarmsReqV2
        :type resource_group_id: str
        :param resources: The param of the PostAlarmsReqV2
        :type resources: list[list[Dimension]]
        :param policies: The param of the PostAlarmsReqV2
        :type policies: list[:class:`g42cloudsdkces.v2.Policy`]
        :param type: The param of the PostAlarmsReqV2
        :type type: str
        :param alarm_notifications: The param of the PostAlarmsReqV2
        :type alarm_notifications: list[:class:`g42cloudsdkces.v2.Notification`]
        :param ok_notifications: The param of the PostAlarmsReqV2
        :type ok_notifications: list[:class:`g42cloudsdkces.v2.Notification`]
        :param notification_begin_time: The param of the PostAlarmsReqV2
        :type notification_begin_time: str
        :param notification_end_time: The param of the PostAlarmsReqV2
        :type notification_end_time: str
        :param enterprise_project_id: The param of the PostAlarmsReqV2
        :type enterprise_project_id: str
        :param enabled: The param of the PostAlarmsReqV2
        :type enabled: bool
        :param notification_enabled: The param of the PostAlarmsReqV2
        :type notification_enabled: bool
        :param alarm_template_id: The param of the PostAlarmsReqV2
        :type alarm_template_id: str
        """
        
        

        self._name = None
        self._description = None
        self._namespace = None
        self._resource_group_id = None
        self._resources = None
        self._policies = None
        self._type = None
        self._alarm_notifications = None
        self._ok_notifications = None
        self._notification_begin_time = None
        self._notification_end_time = None
        self._enterprise_project_id = None
        self._enabled = None
        self._notification_enabled = None
        self._alarm_template_id = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.namespace = namespace
        if resource_group_id is not None:
            self.resource_group_id = resource_group_id
        self.resources = resources
        self.policies = policies
        self.type = type
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
        self.enabled = enabled
        self.notification_enabled = notification_enabled
        if alarm_template_id is not None:
            self.alarm_template_id = alarm_template_id

    @property
    def name(self):
        """Gets the name of this PostAlarmsReqV2.

        :return: The name of this PostAlarmsReqV2.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PostAlarmsReqV2.

        :param name: The name of this PostAlarmsReqV2.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this PostAlarmsReqV2.

        :return: The description of this PostAlarmsReqV2.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PostAlarmsReqV2.

        :param description: The description of this PostAlarmsReqV2.
        :type description: str
        """
        self._description = description

    @property
    def namespace(self):
        """Gets the namespace of this PostAlarmsReqV2.

        :return: The namespace of this PostAlarmsReqV2.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this PostAlarmsReqV2.

        :param namespace: The namespace of this PostAlarmsReqV2.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def resource_group_id(self):
        """Gets the resource_group_id of this PostAlarmsReqV2.

        :return: The resource_group_id of this PostAlarmsReqV2.
        :rtype: str
        """
        return self._resource_group_id

    @resource_group_id.setter
    def resource_group_id(self, resource_group_id):
        """Sets the resource_group_id of this PostAlarmsReqV2.

        :param resource_group_id: The resource_group_id of this PostAlarmsReqV2.
        :type resource_group_id: str
        """
        self._resource_group_id = resource_group_id

    @property
    def resources(self):
        """Gets the resources of this PostAlarmsReqV2.

        :return: The resources of this PostAlarmsReqV2.
        :rtype: list[list[Dimension]]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this PostAlarmsReqV2.

        :param resources: The resources of this PostAlarmsReqV2.
        :type resources: list[list[Dimension]]
        """
        self._resources = resources

    @property
    def policies(self):
        """Gets the policies of this PostAlarmsReqV2.

        :return: The policies of this PostAlarmsReqV2.
        :rtype: list[:class:`g42cloudsdkces.v2.Policy`]
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        """Sets the policies of this PostAlarmsReqV2.

        :param policies: The policies of this PostAlarmsReqV2.
        :type policies: list[:class:`g42cloudsdkces.v2.Policy`]
        """
        self._policies = policies

    @property
    def type(self):
        """Gets the type of this PostAlarmsReqV2.

        :return: The type of this PostAlarmsReqV2.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PostAlarmsReqV2.

        :param type: The type of this PostAlarmsReqV2.
        :type type: str
        """
        self._type = type

    @property
    def alarm_notifications(self):
        """Gets the alarm_notifications of this PostAlarmsReqV2.

        :return: The alarm_notifications of this PostAlarmsReqV2.
        :rtype: list[:class:`g42cloudsdkces.v2.Notification`]
        """
        return self._alarm_notifications

    @alarm_notifications.setter
    def alarm_notifications(self, alarm_notifications):
        """Sets the alarm_notifications of this PostAlarmsReqV2.

        :param alarm_notifications: The alarm_notifications of this PostAlarmsReqV2.
        :type alarm_notifications: list[:class:`g42cloudsdkces.v2.Notification`]
        """
        self._alarm_notifications = alarm_notifications

    @property
    def ok_notifications(self):
        """Gets the ok_notifications of this PostAlarmsReqV2.

        :return: The ok_notifications of this PostAlarmsReqV2.
        :rtype: list[:class:`g42cloudsdkces.v2.Notification`]
        """
        return self._ok_notifications

    @ok_notifications.setter
    def ok_notifications(self, ok_notifications):
        """Sets the ok_notifications of this PostAlarmsReqV2.

        :param ok_notifications: The ok_notifications of this PostAlarmsReqV2.
        :type ok_notifications: list[:class:`g42cloudsdkces.v2.Notification`]
        """
        self._ok_notifications = ok_notifications

    @property
    def notification_begin_time(self):
        """Gets the notification_begin_time of this PostAlarmsReqV2.

        :return: The notification_begin_time of this PostAlarmsReqV2.
        :rtype: str
        """
        return self._notification_begin_time

    @notification_begin_time.setter
    def notification_begin_time(self, notification_begin_time):
        """Sets the notification_begin_time of this PostAlarmsReqV2.

        :param notification_begin_time: The notification_begin_time of this PostAlarmsReqV2.
        :type notification_begin_time: str
        """
        self._notification_begin_time = notification_begin_time

    @property
    def notification_end_time(self):
        """Gets the notification_end_time of this PostAlarmsReqV2.

        :return: The notification_end_time of this PostAlarmsReqV2.
        :rtype: str
        """
        return self._notification_end_time

    @notification_end_time.setter
    def notification_end_time(self, notification_end_time):
        """Sets the notification_end_time of this PostAlarmsReqV2.

        :param notification_end_time: The notification_end_time of this PostAlarmsReqV2.
        :type notification_end_time: str
        """
        self._notification_end_time = notification_end_time

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this PostAlarmsReqV2.

        :return: The enterprise_project_id of this PostAlarmsReqV2.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this PostAlarmsReqV2.

        :param enterprise_project_id: The enterprise_project_id of this PostAlarmsReqV2.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def enabled(self):
        """Gets the enabled of this PostAlarmsReqV2.

        :return: The enabled of this PostAlarmsReqV2.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this PostAlarmsReqV2.

        :param enabled: The enabled of this PostAlarmsReqV2.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def notification_enabled(self):
        """Gets the notification_enabled of this PostAlarmsReqV2.

        :return: The notification_enabled of this PostAlarmsReqV2.
        :rtype: bool
        """
        return self._notification_enabled

    @notification_enabled.setter
    def notification_enabled(self, notification_enabled):
        """Sets the notification_enabled of this PostAlarmsReqV2.

        :param notification_enabled: The notification_enabled of this PostAlarmsReqV2.
        :type notification_enabled: bool
        """
        self._notification_enabled = notification_enabled

    @property
    def alarm_template_id(self):
        """Gets the alarm_template_id of this PostAlarmsReqV2.

        :return: The alarm_template_id of this PostAlarmsReqV2.
        :rtype: str
        """
        return self._alarm_template_id

    @alarm_template_id.setter
    def alarm_template_id(self, alarm_template_id):
        """Sets the alarm_template_id of this PostAlarmsReqV2.

        :param alarm_template_id: The alarm_template_id of this PostAlarmsReqV2.
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
        if not isinstance(other, PostAlarmsReqV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
