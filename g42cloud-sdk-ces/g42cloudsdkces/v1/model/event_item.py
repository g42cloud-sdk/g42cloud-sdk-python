# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'event_name': 'str',
        'event_source': 'str',
        'time': 'int',
        'detail': 'EventItemDetail'
    }

    attribute_map = {
        'event_name': 'event_name',
        'event_source': 'event_source',
        'time': 'time',
        'detail': 'detail'
    }

    def __init__(self, event_name=None, event_source=None, time=None, detail=None):
        """EventItem

        The model defined in g42cloud sdk

        :param event_name: The param of the EventItem
        :type event_name: str
        :param event_source: The param of the EventItem
        :type event_source: str
        :param time: The param of the EventItem
        :type time: int
        :param detail: The param of the EventItem
        :type detail: :class:`g42cloudsdkces.v1.EventItemDetail`
        """
        
        

        self._event_name = None
        self._event_source = None
        self._time = None
        self._detail = None
        self.discriminator = None

        self.event_name = event_name
        self.event_source = event_source
        self.time = time
        self.detail = detail

    @property
    def event_name(self):
        """Gets the event_name of this EventItem.

        :return: The event_name of this EventItem.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """Sets the event_name of this EventItem.

        :param event_name: The event_name of this EventItem.
        :type event_name: str
        """
        self._event_name = event_name

    @property
    def event_source(self):
        """Gets the event_source of this EventItem.

        :return: The event_source of this EventItem.
        :rtype: str
        """
        return self._event_source

    @event_source.setter
    def event_source(self, event_source):
        """Sets the event_source of this EventItem.

        :param event_source: The event_source of this EventItem.
        :type event_source: str
        """
        self._event_source = event_source

    @property
    def time(self):
        """Gets the time of this EventItem.

        :return: The time of this EventItem.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this EventItem.

        :param time: The time of this EventItem.
        :type time: int
        """
        self._time = time

    @property
    def detail(self):
        """Gets the detail of this EventItem.

        :return: The detail of this EventItem.
        :rtype: :class:`g42cloudsdkces.v1.EventItemDetail`
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this EventItem.

        :param detail: The detail of this EventItem.
        :type detail: :class:`g42cloudsdkces.v1.EventItemDetail`
        """
        self._detail = detail

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
        if not isinstance(other, EventItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
