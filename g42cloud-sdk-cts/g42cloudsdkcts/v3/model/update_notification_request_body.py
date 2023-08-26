# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateNotificationRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'notification_name': 'str',
        'operation_type': 'str',
        'operations': 'list[Operations]',
        'notify_user_list': 'list[NotificationUsers]',
        'status': 'str',
        'topic_id': 'str',
        'notification_id': 'str',
        'filter': 'Filter'
    }

    attribute_map = {
        'notification_name': 'notification_name',
        'operation_type': 'operation_type',
        'operations': 'operations',
        'notify_user_list': 'notify_user_list',
        'status': 'status',
        'topic_id': 'topic_id',
        'notification_id': 'notification_id',
        'filter': 'filter'
    }

    def __init__(self, notification_name=None, operation_type=None, operations=None, notify_user_list=None, status=None, topic_id=None, notification_id=None, filter=None):
        """UpdateNotificationRequestBody

        The model defined in g42cloud sdk

        :param notification_name: The param of the UpdateNotificationRequestBody
        :type notification_name: str
        :param operation_type: The param of the UpdateNotificationRequestBody
        :type operation_type: str
        :param operations: The param of the UpdateNotificationRequestBody
        :type operations: list[:class:`g42cloudsdkcts.v3.Operations`]
        :param notify_user_list: The param of the UpdateNotificationRequestBody
        :type notify_user_list: list[:class:`g42cloudsdkcts.v3.NotificationUsers`]
        :param status: The param of the UpdateNotificationRequestBody
        :type status: str
        :param topic_id: The param of the UpdateNotificationRequestBody
        :type topic_id: str
        :param notification_id: The param of the UpdateNotificationRequestBody
        :type notification_id: str
        :param filter: The param of the UpdateNotificationRequestBody
        :type filter: :class:`g42cloudsdkcts.v3.Filter`
        """
        
        

        self._notification_name = None
        self._operation_type = None
        self._operations = None
        self._notify_user_list = None
        self._status = None
        self._topic_id = None
        self._notification_id = None
        self._filter = None
        self.discriminator = None

        self.notification_name = notification_name
        self.operation_type = operation_type
        if operations is not None:
            self.operations = operations
        if notify_user_list is not None:
            self.notify_user_list = notify_user_list
        self.status = status
        if topic_id is not None:
            self.topic_id = topic_id
        self.notification_id = notification_id
        if filter is not None:
            self.filter = filter

    @property
    def notification_name(self):
        """Gets the notification_name of this UpdateNotificationRequestBody.

        :return: The notification_name of this UpdateNotificationRequestBody.
        :rtype: str
        """
        return self._notification_name

    @notification_name.setter
    def notification_name(self, notification_name):
        """Sets the notification_name of this UpdateNotificationRequestBody.

        :param notification_name: The notification_name of this UpdateNotificationRequestBody.
        :type notification_name: str
        """
        self._notification_name = notification_name

    @property
    def operation_type(self):
        """Gets the operation_type of this UpdateNotificationRequestBody.

        :return: The operation_type of this UpdateNotificationRequestBody.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """Sets the operation_type of this UpdateNotificationRequestBody.

        :param operation_type: The operation_type of this UpdateNotificationRequestBody.
        :type operation_type: str
        """
        self._operation_type = operation_type

    @property
    def operations(self):
        """Gets the operations of this UpdateNotificationRequestBody.

        :return: The operations of this UpdateNotificationRequestBody.
        :rtype: list[:class:`g42cloudsdkcts.v3.Operations`]
        """
        return self._operations

    @operations.setter
    def operations(self, operations):
        """Sets the operations of this UpdateNotificationRequestBody.

        :param operations: The operations of this UpdateNotificationRequestBody.
        :type operations: list[:class:`g42cloudsdkcts.v3.Operations`]
        """
        self._operations = operations

    @property
    def notify_user_list(self):
        """Gets the notify_user_list of this UpdateNotificationRequestBody.

        :return: The notify_user_list of this UpdateNotificationRequestBody.
        :rtype: list[:class:`g42cloudsdkcts.v3.NotificationUsers`]
        """
        return self._notify_user_list

    @notify_user_list.setter
    def notify_user_list(self, notify_user_list):
        """Sets the notify_user_list of this UpdateNotificationRequestBody.

        :param notify_user_list: The notify_user_list of this UpdateNotificationRequestBody.
        :type notify_user_list: list[:class:`g42cloudsdkcts.v3.NotificationUsers`]
        """
        self._notify_user_list = notify_user_list

    @property
    def status(self):
        """Gets the status of this UpdateNotificationRequestBody.

        :return: The status of this UpdateNotificationRequestBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateNotificationRequestBody.

        :param status: The status of this UpdateNotificationRequestBody.
        :type status: str
        """
        self._status = status

    @property
    def topic_id(self):
        """Gets the topic_id of this UpdateNotificationRequestBody.

        :return: The topic_id of this UpdateNotificationRequestBody.
        :rtype: str
        """
        return self._topic_id

    @topic_id.setter
    def topic_id(self, topic_id):
        """Sets the topic_id of this UpdateNotificationRequestBody.

        :param topic_id: The topic_id of this UpdateNotificationRequestBody.
        :type topic_id: str
        """
        self._topic_id = topic_id

    @property
    def notification_id(self):
        """Gets the notification_id of this UpdateNotificationRequestBody.

        :return: The notification_id of this UpdateNotificationRequestBody.
        :rtype: str
        """
        return self._notification_id

    @notification_id.setter
    def notification_id(self, notification_id):
        """Sets the notification_id of this UpdateNotificationRequestBody.

        :param notification_id: The notification_id of this UpdateNotificationRequestBody.
        :type notification_id: str
        """
        self._notification_id = notification_id

    @property
    def filter(self):
        """Gets the filter of this UpdateNotificationRequestBody.

        :return: The filter of this UpdateNotificationRequestBody.
        :rtype: :class:`g42cloudsdkcts.v3.Filter`
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this UpdateNotificationRequestBody.

        :param filter: The filter of this UpdateNotificationRequestBody.
        :type filter: :class:`g42cloudsdkcts.v3.Filter`
        """
        self._filter = filter

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
        if not isinstance(other, UpdateNotificationRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
