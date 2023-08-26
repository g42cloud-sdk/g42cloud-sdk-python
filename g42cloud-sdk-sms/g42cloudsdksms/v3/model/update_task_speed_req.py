# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTaskSpeedReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'subtask_name': 'str',
        'progress': 'int',
        'replicatesize': 'int',
        'totalsize': 'int',
        'process_trace': 'str',
        'migrate_speed': 'float',
        'compress_rate': 'float',
        'remain_time': 'int'
    }

    attribute_map = {
        'subtask_name': 'subtask_name',
        'progress': 'progress',
        'replicatesize': 'replicatesize',
        'totalsize': 'totalsize',
        'process_trace': 'process_trace',
        'migrate_speed': 'migrate_speed',
        'compress_rate': 'compress_rate',
        'remain_time': 'remain_time'
    }

    def __init__(self, subtask_name=None, progress=None, replicatesize=None, totalsize=None, process_trace=None, migrate_speed=None, compress_rate=None, remain_time=None):
        """UpdateTaskSpeedReq

        The model defined in g42cloud sdk

        :param subtask_name: The param of the UpdateTaskSpeedReq
        :type subtask_name: str
        :param progress: The param of the UpdateTaskSpeedReq
        :type progress: int
        :param replicatesize: The param of the UpdateTaskSpeedReq
        :type replicatesize: int
        :param totalsize: The param of the UpdateTaskSpeedReq
        :type totalsize: int
        :param process_trace: The param of the UpdateTaskSpeedReq
        :type process_trace: str
        :param migrate_speed: The param of the UpdateTaskSpeedReq
        :type migrate_speed: float
        :param compress_rate: The param of the UpdateTaskSpeedReq
        :type compress_rate: float
        :param remain_time: The param of the UpdateTaskSpeedReq
        :type remain_time: int
        """
        
        

        self._subtask_name = None
        self._progress = None
        self._replicatesize = None
        self._totalsize = None
        self._process_trace = None
        self._migrate_speed = None
        self._compress_rate = None
        self._remain_time = None
        self.discriminator = None

        self.subtask_name = subtask_name
        self.progress = progress
        self.replicatesize = replicatesize
        self.totalsize = totalsize
        self.process_trace = process_trace
        if migrate_speed is not None:
            self.migrate_speed = migrate_speed
        if compress_rate is not None:
            self.compress_rate = compress_rate
        if remain_time is not None:
            self.remain_time = remain_time

    @property
    def subtask_name(self):
        """Gets the subtask_name of this UpdateTaskSpeedReq.

        :return: The subtask_name of this UpdateTaskSpeedReq.
        :rtype: str
        """
        return self._subtask_name

    @subtask_name.setter
    def subtask_name(self, subtask_name):
        """Sets the subtask_name of this UpdateTaskSpeedReq.

        :param subtask_name: The subtask_name of this UpdateTaskSpeedReq.
        :type subtask_name: str
        """
        self._subtask_name = subtask_name

    @property
    def progress(self):
        """Gets the progress of this UpdateTaskSpeedReq.

        :return: The progress of this UpdateTaskSpeedReq.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this UpdateTaskSpeedReq.

        :param progress: The progress of this UpdateTaskSpeedReq.
        :type progress: int
        """
        self._progress = progress

    @property
    def replicatesize(self):
        """Gets the replicatesize of this UpdateTaskSpeedReq.

        :return: The replicatesize of this UpdateTaskSpeedReq.
        :rtype: int
        """
        return self._replicatesize

    @replicatesize.setter
    def replicatesize(self, replicatesize):
        """Sets the replicatesize of this UpdateTaskSpeedReq.

        :param replicatesize: The replicatesize of this UpdateTaskSpeedReq.
        :type replicatesize: int
        """
        self._replicatesize = replicatesize

    @property
    def totalsize(self):
        """Gets the totalsize of this UpdateTaskSpeedReq.

        :return: The totalsize of this UpdateTaskSpeedReq.
        :rtype: int
        """
        return self._totalsize

    @totalsize.setter
    def totalsize(self, totalsize):
        """Sets the totalsize of this UpdateTaskSpeedReq.

        :param totalsize: The totalsize of this UpdateTaskSpeedReq.
        :type totalsize: int
        """
        self._totalsize = totalsize

    @property
    def process_trace(self):
        """Gets the process_trace of this UpdateTaskSpeedReq.

        :return: The process_trace of this UpdateTaskSpeedReq.
        :rtype: str
        """
        return self._process_trace

    @process_trace.setter
    def process_trace(self, process_trace):
        """Sets the process_trace of this UpdateTaskSpeedReq.

        :param process_trace: The process_trace of this UpdateTaskSpeedReq.
        :type process_trace: str
        """
        self._process_trace = process_trace

    @property
    def migrate_speed(self):
        """Gets the migrate_speed of this UpdateTaskSpeedReq.

        :return: The migrate_speed of this UpdateTaskSpeedReq.
        :rtype: float
        """
        return self._migrate_speed

    @migrate_speed.setter
    def migrate_speed(self, migrate_speed):
        """Sets the migrate_speed of this UpdateTaskSpeedReq.

        :param migrate_speed: The migrate_speed of this UpdateTaskSpeedReq.
        :type migrate_speed: float
        """
        self._migrate_speed = migrate_speed

    @property
    def compress_rate(self):
        """Gets the compress_rate of this UpdateTaskSpeedReq.

        :return: The compress_rate of this UpdateTaskSpeedReq.
        :rtype: float
        """
        return self._compress_rate

    @compress_rate.setter
    def compress_rate(self, compress_rate):
        """Sets the compress_rate of this UpdateTaskSpeedReq.

        :param compress_rate: The compress_rate of this UpdateTaskSpeedReq.
        :type compress_rate: float
        """
        self._compress_rate = compress_rate

    @property
    def remain_time(self):
        """Gets the remain_time of this UpdateTaskSpeedReq.

        :return: The remain_time of this UpdateTaskSpeedReq.
        :rtype: int
        """
        return self._remain_time

    @remain_time.setter
    def remain_time(self, remain_time):
        """Sets the remain_time of this UpdateTaskSpeedReq.

        :param remain_time: The remain_time of this UpdateTaskSpeedReq.
        :type remain_time: int
        """
        self._remain_time = remain_time

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
        if not isinstance(other, UpdateTaskSpeedReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
