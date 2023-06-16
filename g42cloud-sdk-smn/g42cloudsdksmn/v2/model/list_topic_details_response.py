# coding: utf-8

import six

from g42cloudsdkcore.sdk_response import SdkResponse
from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTopicDetailsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'update_time': 'str',
        'push_policy': 'int',
        'create_time': 'str',
        'name': 'str',
        'topic_urn': 'str',
        'display_name': 'str',
        'request_id': 'str',
        'enterprise_project_id': 'str',
        'topic_id': 'str'
    }

    attribute_map = {
        'update_time': 'update_time',
        'push_policy': 'push_policy',
        'create_time': 'create_time',
        'name': 'name',
        'topic_urn': 'topic_urn',
        'display_name': 'display_name',
        'request_id': 'request_id',
        'enterprise_project_id': 'enterprise_project_id',
        'topic_id': 'topic_id'
    }

    def __init__(self, update_time=None, push_policy=None, create_time=None, name=None, topic_urn=None, display_name=None, request_id=None, enterprise_project_id=None, topic_id=None):
        """ListTopicDetailsResponse

        The model defined in g42cloud sdk

        :param update_time: The param of the ListTopicDetailsResponse
        :type update_time: str
        :param push_policy: The param of the ListTopicDetailsResponse
        :type push_policy: int
        :param create_time: The param of the ListTopicDetailsResponse
        :type create_time: str
        :param name: The param of the ListTopicDetailsResponse
        :type name: str
        :param topic_urn: The param of the ListTopicDetailsResponse
        :type topic_urn: str
        :param display_name: The param of the ListTopicDetailsResponse
        :type display_name: str
        :param request_id: The param of the ListTopicDetailsResponse
        :type request_id: str
        :param enterprise_project_id: The param of the ListTopicDetailsResponse
        :type enterprise_project_id: str
        :param topic_id: The param of the ListTopicDetailsResponse
        :type topic_id: str
        """
        
        super(ListTopicDetailsResponse, self).__init__()

        self._update_time = None
        self._push_policy = None
        self._create_time = None
        self._name = None
        self._topic_urn = None
        self._display_name = None
        self._request_id = None
        self._enterprise_project_id = None
        self._topic_id = None
        self.discriminator = None

        if update_time is not None:
            self.update_time = update_time
        if push_policy is not None:
            self.push_policy = push_policy
        if create_time is not None:
            self.create_time = create_time
        if name is not None:
            self.name = name
        if topic_urn is not None:
            self.topic_urn = topic_urn
        if display_name is not None:
            self.display_name = display_name
        if request_id is not None:
            self.request_id = request_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if topic_id is not None:
            self.topic_id = topic_id

    @property
    def update_time(self):
        """Gets the update_time of this ListTopicDetailsResponse.

        :return: The update_time of this ListTopicDetailsResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ListTopicDetailsResponse.

        :param update_time: The update_time of this ListTopicDetailsResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def push_policy(self):
        """Gets the push_policy of this ListTopicDetailsResponse.

        :return: The push_policy of this ListTopicDetailsResponse.
        :rtype: int
        """
        return self._push_policy

    @push_policy.setter
    def push_policy(self, push_policy):
        """Sets the push_policy of this ListTopicDetailsResponse.

        :param push_policy: The push_policy of this ListTopicDetailsResponse.
        :type push_policy: int
        """
        self._push_policy = push_policy

    @property
    def create_time(self):
        """Gets the create_time of this ListTopicDetailsResponse.

        :return: The create_time of this ListTopicDetailsResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ListTopicDetailsResponse.

        :param create_time: The create_time of this ListTopicDetailsResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def name(self):
        """Gets the name of this ListTopicDetailsResponse.

        :return: The name of this ListTopicDetailsResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListTopicDetailsResponse.

        :param name: The name of this ListTopicDetailsResponse.
        :type name: str
        """
        self._name = name

    @property
    def topic_urn(self):
        """Gets the topic_urn of this ListTopicDetailsResponse.

        :return: The topic_urn of this ListTopicDetailsResponse.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        """Sets the topic_urn of this ListTopicDetailsResponse.

        :param topic_urn: The topic_urn of this ListTopicDetailsResponse.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

    @property
    def display_name(self):
        """Gets the display_name of this ListTopicDetailsResponse.

        :return: The display_name of this ListTopicDetailsResponse.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ListTopicDetailsResponse.

        :param display_name: The display_name of this ListTopicDetailsResponse.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def request_id(self):
        """Gets the request_id of this ListTopicDetailsResponse.

        :return: The request_id of this ListTopicDetailsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListTopicDetailsResponse.

        :param request_id: The request_id of this ListTopicDetailsResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListTopicDetailsResponse.

        :return: The enterprise_project_id of this ListTopicDetailsResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListTopicDetailsResponse.

        :param enterprise_project_id: The enterprise_project_id of this ListTopicDetailsResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def topic_id(self):
        """Gets the topic_id of this ListTopicDetailsResponse.

        :return: The topic_id of this ListTopicDetailsResponse.
        :rtype: str
        """
        return self._topic_id

    @topic_id.setter
    def topic_id(self, topic_id):
        """Sets the topic_id of this ListTopicDetailsResponse.

        :param topic_id: The topic_id of this ListTopicDetailsResponse.
        :type topic_id: str
        """
        self._topic_id = topic_id

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
        if not isinstance(other, ListTopicDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
