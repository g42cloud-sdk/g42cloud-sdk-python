# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'begin_time': 'str',
        'code': 'str',
        'end_time': 'str',
        'entities': 'JobEntities',
        'error_code': 'str',
        'fail_reason': 'str',
        'job_id': 'str',
        'job_type': 'str',
        'message': 'str',
        'status': 'str'
    }

    attribute_map = {
        'begin_time': 'begin_time',
        'code': 'code',
        'end_time': 'end_time',
        'entities': 'entities',
        'error_code': 'error_code',
        'fail_reason': 'fail_reason',
        'job_id': 'job_id',
        'job_type': 'job_type',
        'message': 'message',
        'status': 'status'
    }

    def __init__(self, begin_time=None, code=None, end_time=None, entities=None, error_code=None, fail_reason=None, job_id=None, job_type=None, message=None, status=None):
        """ShowJobResponse

        The model defined in g42cloud sdk

        :param begin_time: The param of the ShowJobResponse
        :type begin_time: str
        :param code: The param of the ShowJobResponse
        :type code: str
        :param end_time: The param of the ShowJobResponse
        :type end_time: str
        :param entities: The param of the ShowJobResponse
        :type entities: :class:`g42cloudsdkecs.v2.JobEntities`
        :param error_code: The param of the ShowJobResponse
        :type error_code: str
        :param fail_reason: The param of the ShowJobResponse
        :type fail_reason: str
        :param job_id: The param of the ShowJobResponse
        :type job_id: str
        :param job_type: The param of the ShowJobResponse
        :type job_type: str
        :param message: The param of the ShowJobResponse
        :type message: str
        :param status: The param of the ShowJobResponse
        :type status: str
        """
        
        super(ShowJobResponse, self).__init__()

        self._begin_time = None
        self._code = None
        self._end_time = None
        self._entities = None
        self._error_code = None
        self._fail_reason = None
        self._job_id = None
        self._job_type = None
        self._message = None
        self._status = None
        self.discriminator = None

        if begin_time is not None:
            self.begin_time = begin_time
        if code is not None:
            self.code = code
        if end_time is not None:
            self.end_time = end_time
        if entities is not None:
            self.entities = entities
        if error_code is not None:
            self.error_code = error_code
        if fail_reason is not None:
            self.fail_reason = fail_reason
        if job_id is not None:
            self.job_id = job_id
        if job_type is not None:
            self.job_type = job_type
        if message is not None:
            self.message = message
        if status is not None:
            self.status = status

    @property
    def begin_time(self):
        """Gets the begin_time of this ShowJobResponse.

        :return: The begin_time of this ShowJobResponse.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this ShowJobResponse.

        :param begin_time: The begin_time of this ShowJobResponse.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def code(self):
        """Gets the code of this ShowJobResponse.

        :return: The code of this ShowJobResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ShowJobResponse.

        :param code: The code of this ShowJobResponse.
        :type code: str
        """
        self._code = code

    @property
    def end_time(self):
        """Gets the end_time of this ShowJobResponse.

        :return: The end_time of this ShowJobResponse.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowJobResponse.

        :param end_time: The end_time of this ShowJobResponse.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def entities(self):
        """Gets the entities of this ShowJobResponse.

        :return: The entities of this ShowJobResponse.
        :rtype: :class:`g42cloudsdkecs.v2.JobEntities`
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """Sets the entities of this ShowJobResponse.

        :param entities: The entities of this ShowJobResponse.
        :type entities: :class:`g42cloudsdkecs.v2.JobEntities`
        """
        self._entities = entities

    @property
    def error_code(self):
        """Gets the error_code of this ShowJobResponse.

        :return: The error_code of this ShowJobResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this ShowJobResponse.

        :param error_code: The error_code of this ShowJobResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def fail_reason(self):
        """Gets the fail_reason of this ShowJobResponse.

        :return: The fail_reason of this ShowJobResponse.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        """Sets the fail_reason of this ShowJobResponse.

        :param fail_reason: The fail_reason of this ShowJobResponse.
        :type fail_reason: str
        """
        self._fail_reason = fail_reason

    @property
    def job_id(self):
        """Gets the job_id of this ShowJobResponse.

        :return: The job_id of this ShowJobResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ShowJobResponse.

        :param job_id: The job_id of this ShowJobResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_type(self):
        """Gets the job_type of this ShowJobResponse.

        :return: The job_type of this ShowJobResponse.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this ShowJobResponse.

        :param job_type: The job_type of this ShowJobResponse.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def message(self):
        """Gets the message of this ShowJobResponse.

        :return: The message of this ShowJobResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ShowJobResponse.

        :param message: The message of this ShowJobResponse.
        :type message: str
        """
        self._message = message

    @property
    def status(self):
        """Gets the status of this ShowJobResponse.

        :return: The status of this ShowJobResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowJobResponse.

        :param status: The status of this ShowJobResponse.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ShowJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
