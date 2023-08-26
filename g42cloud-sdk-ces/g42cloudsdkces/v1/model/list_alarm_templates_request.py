# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAlarmTemplatesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_template_id': 'str',
        'namespace': 'str',
        'dname': 'str',
        'start': 'str',
        'limit': 'str'
    }

    attribute_map = {
        'alarm_template_id': 'alarmTemplateId',
        'namespace': 'namespace',
        'dname': 'dname',
        'start': 'start',
        'limit': 'limit'
    }

    def __init__(self, alarm_template_id=None, namespace=None, dname=None, start=None, limit=None):
        """ListAlarmTemplatesRequest

        The model defined in g42cloud sdk

        :param alarm_template_id: The param of the ListAlarmTemplatesRequest
        :type alarm_template_id: str
        :param namespace: The param of the ListAlarmTemplatesRequest
        :type namespace: str
        :param dname: The param of the ListAlarmTemplatesRequest
        :type dname: str
        :param start: The param of the ListAlarmTemplatesRequest
        :type start: str
        :param limit: The param of the ListAlarmTemplatesRequest
        :type limit: str
        """
        
        

        self._alarm_template_id = None
        self._namespace = None
        self._dname = None
        self._start = None
        self._limit = None
        self.discriminator = None

        if alarm_template_id is not None:
            self.alarm_template_id = alarm_template_id
        if namespace is not None:
            self.namespace = namespace
        if dname is not None:
            self.dname = dname
        if start is not None:
            self.start = start
        if limit is not None:
            self.limit = limit

    @property
    def alarm_template_id(self):
        """Gets the alarm_template_id of this ListAlarmTemplatesRequest.

        :return: The alarm_template_id of this ListAlarmTemplatesRequest.
        :rtype: str
        """
        return self._alarm_template_id

    @alarm_template_id.setter
    def alarm_template_id(self, alarm_template_id):
        """Sets the alarm_template_id of this ListAlarmTemplatesRequest.

        :param alarm_template_id: The alarm_template_id of this ListAlarmTemplatesRequest.
        :type alarm_template_id: str
        """
        self._alarm_template_id = alarm_template_id

    @property
    def namespace(self):
        """Gets the namespace of this ListAlarmTemplatesRequest.

        :return: The namespace of this ListAlarmTemplatesRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this ListAlarmTemplatesRequest.

        :param namespace: The namespace of this ListAlarmTemplatesRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def dname(self):
        """Gets the dname of this ListAlarmTemplatesRequest.

        :return: The dname of this ListAlarmTemplatesRequest.
        :rtype: str
        """
        return self._dname

    @dname.setter
    def dname(self, dname):
        """Sets the dname of this ListAlarmTemplatesRequest.

        :param dname: The dname of this ListAlarmTemplatesRequest.
        :type dname: str
        """
        self._dname = dname

    @property
    def start(self):
        """Gets the start of this ListAlarmTemplatesRequest.

        :return: The start of this ListAlarmTemplatesRequest.
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this ListAlarmTemplatesRequest.

        :param start: The start of this ListAlarmTemplatesRequest.
        :type start: str
        """
        self._start = start

    @property
    def limit(self):
        """Gets the limit of this ListAlarmTemplatesRequest.

        :return: The limit of this ListAlarmTemplatesRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAlarmTemplatesRequest.

        :param limit: The limit of this ListAlarmTemplatesRequest.
        :type limit: str
        """
        self._limit = limit

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
        if not isinstance(other, ListAlarmTemplatesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
