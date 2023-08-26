# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobProgressEntities:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_id': 'str',
        'current_task': 'str',
        'image_name': 'str',
        'process_percent': 'float',
        'sub_job_id': 'str'
    }

    attribute_map = {
        'image_id': 'image_id',
        'current_task': 'current_task',
        'image_name': 'image_name',
        'process_percent': 'process_percent',
        'sub_job_id': 'subJobId'
    }

    def __init__(self, image_id=None, current_task=None, image_name=None, process_percent=None, sub_job_id=None):
        """JobProgressEntities

        The model defined in g42cloud sdk

        :param image_id: The param of the JobProgressEntities
        :type image_id: str
        :param current_task: The param of the JobProgressEntities
        :type current_task: str
        :param image_name: The param of the JobProgressEntities
        :type image_name: str
        :param process_percent: The param of the JobProgressEntities
        :type process_percent: float
        :param sub_job_id: The param of the JobProgressEntities
        :type sub_job_id: str
        """
        
        

        self._image_id = None
        self._current_task = None
        self._image_name = None
        self._process_percent = None
        self._sub_job_id = None
        self.discriminator = None

        if image_id is not None:
            self.image_id = image_id
        if current_task is not None:
            self.current_task = current_task
        if image_name is not None:
            self.image_name = image_name
        if process_percent is not None:
            self.process_percent = process_percent
        if sub_job_id is not None:
            self.sub_job_id = sub_job_id

    @property
    def image_id(self):
        """Gets the image_id of this JobProgressEntities.

        :return: The image_id of this JobProgressEntities.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this JobProgressEntities.

        :param image_id: The image_id of this JobProgressEntities.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def current_task(self):
        """Gets the current_task of this JobProgressEntities.

        :return: The current_task of this JobProgressEntities.
        :rtype: str
        """
        return self._current_task

    @current_task.setter
    def current_task(self, current_task):
        """Sets the current_task of this JobProgressEntities.

        :param current_task: The current_task of this JobProgressEntities.
        :type current_task: str
        """
        self._current_task = current_task

    @property
    def image_name(self):
        """Gets the image_name of this JobProgressEntities.

        :return: The image_name of this JobProgressEntities.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        """Sets the image_name of this JobProgressEntities.

        :param image_name: The image_name of this JobProgressEntities.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def process_percent(self):
        """Gets the process_percent of this JobProgressEntities.

        :return: The process_percent of this JobProgressEntities.
        :rtype: float
        """
        return self._process_percent

    @process_percent.setter
    def process_percent(self, process_percent):
        """Sets the process_percent of this JobProgressEntities.

        :param process_percent: The process_percent of this JobProgressEntities.
        :type process_percent: float
        """
        self._process_percent = process_percent

    @property
    def sub_job_id(self):
        """Gets the sub_job_id of this JobProgressEntities.

        :return: The sub_job_id of this JobProgressEntities.
        :rtype: str
        """
        return self._sub_job_id

    @sub_job_id.setter
    def sub_job_id(self, sub_job_id):
        """Sets the sub_job_id of this JobProgressEntities.

        :param sub_job_id: The sub_job_id of this JobProgressEntities.
        :type sub_job_id: str
        """
        self._sub_job_id = sub_job_id

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
        if not isinstance(other, JobProgressEntities):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
