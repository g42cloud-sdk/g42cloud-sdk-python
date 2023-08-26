# coding: utf-8

import six

from g42cloudsdkcore.sdk_response import SdkResponse
from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEngineJobResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'engine_id': 'str',
        'type': 'str',
        'description': 'str',
        'status': 'str',
        'scheduling': 'int',
        'create_user': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'context': 'str',
        'tasks': 'list[TaskSteps]'
    }

    attribute_map = {
        'id': 'id',
        'engine_id': 'engine_id',
        'type': 'type',
        'description': 'description',
        'status': 'status',
        'scheduling': 'scheduling',
        'create_user': 'create_user',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'context': 'context',
        'tasks': 'tasks'
    }

    def __init__(self, id=None, engine_id=None, type=None, description=None, status=None, scheduling=None, create_user=None, start_time=None, end_time=None, context=None, tasks=None):
        """ShowEngineJobResponse

        The model defined in g42cloud sdk

        :param id: The param of the ShowEngineJobResponse
        :type id: int
        :param engine_id: The param of the ShowEngineJobResponse
        :type engine_id: str
        :param type: The param of the ShowEngineJobResponse
        :type type: str
        :param description: The param of the ShowEngineJobResponse
        :type description: str
        :param status: The param of the ShowEngineJobResponse
        :type status: str
        :param scheduling: The param of the ShowEngineJobResponse
        :type scheduling: int
        :param create_user: The param of the ShowEngineJobResponse
        :type create_user: str
        :param start_time: The param of the ShowEngineJobResponse
        :type start_time: int
        :param end_time: The param of the ShowEngineJobResponse
        :type end_time: int
        :param context: The param of the ShowEngineJobResponse
        :type context: str
        :param tasks: The param of the ShowEngineJobResponse
        :type tasks: list[:class:`g42cloudsdkcse.v1.TaskSteps`]
        """
        
        super(ShowEngineJobResponse, self).__init__()

        self._id = None
        self._engine_id = None
        self._type = None
        self._description = None
        self._status = None
        self._scheduling = None
        self._create_user = None
        self._start_time = None
        self._end_time = None
        self._context = None
        self._tasks = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if engine_id is not None:
            self.engine_id = engine_id
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if scheduling is not None:
            self.scheduling = scheduling
        if create_user is not None:
            self.create_user = create_user
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if context is not None:
            self.context = context
        if tasks is not None:
            self.tasks = tasks

    @property
    def id(self):
        """Gets the id of this ShowEngineJobResponse.

        :return: The id of this ShowEngineJobResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowEngineJobResponse.

        :param id: The id of this ShowEngineJobResponse.
        :type id: int
        """
        self._id = id

    @property
    def engine_id(self):
        """Gets the engine_id of this ShowEngineJobResponse.

        :return: The engine_id of this ShowEngineJobResponse.
        :rtype: str
        """
        return self._engine_id

    @engine_id.setter
    def engine_id(self, engine_id):
        """Sets the engine_id of this ShowEngineJobResponse.

        :param engine_id: The engine_id of this ShowEngineJobResponse.
        :type engine_id: str
        """
        self._engine_id = engine_id

    @property
    def type(self):
        """Gets the type of this ShowEngineJobResponse.

        :return: The type of this ShowEngineJobResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowEngineJobResponse.

        :param type: The type of this ShowEngineJobResponse.
        :type type: str
        """
        self._type = type

    @property
    def description(self):
        """Gets the description of this ShowEngineJobResponse.

        :return: The description of this ShowEngineJobResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowEngineJobResponse.

        :param description: The description of this ShowEngineJobResponse.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        """Gets the status of this ShowEngineJobResponse.

        :return: The status of this ShowEngineJobResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowEngineJobResponse.

        :param status: The status of this ShowEngineJobResponse.
        :type status: str
        """
        self._status = status

    @property
    def scheduling(self):
        """Gets the scheduling of this ShowEngineJobResponse.

        :return: The scheduling of this ShowEngineJobResponse.
        :rtype: int
        """
        return self._scheduling

    @scheduling.setter
    def scheduling(self, scheduling):
        """Sets the scheduling of this ShowEngineJobResponse.

        :param scheduling: The scheduling of this ShowEngineJobResponse.
        :type scheduling: int
        """
        self._scheduling = scheduling

    @property
    def create_user(self):
        """Gets the create_user of this ShowEngineJobResponse.

        :return: The create_user of this ShowEngineJobResponse.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this ShowEngineJobResponse.

        :param create_user: The create_user of this ShowEngineJobResponse.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def start_time(self):
        """Gets the start_time of this ShowEngineJobResponse.

        :return: The start_time of this ShowEngineJobResponse.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowEngineJobResponse.

        :param start_time: The start_time of this ShowEngineJobResponse.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowEngineJobResponse.

        :return: The end_time of this ShowEngineJobResponse.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowEngineJobResponse.

        :param end_time: The end_time of this ShowEngineJobResponse.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def context(self):
        """Gets the context of this ShowEngineJobResponse.

        :return: The context of this ShowEngineJobResponse.
        :rtype: str
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this ShowEngineJobResponse.

        :param context: The context of this ShowEngineJobResponse.
        :type context: str
        """
        self._context = context

    @property
    def tasks(self):
        """Gets the tasks of this ShowEngineJobResponse.

        :return: The tasks of this ShowEngineJobResponse.
        :rtype: list[:class:`g42cloudsdkcse.v1.TaskSteps`]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """Sets the tasks of this ShowEngineJobResponse.

        :param tasks: The tasks of this ShowEngineJobResponse.
        :type tasks: list[:class:`g42cloudsdkcse.v1.TaskSteps`]
        """
        self._tasks = tasks

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
        if not isinstance(other, ShowEngineJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
