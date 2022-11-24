# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetJobInfoResponseBodyJob:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'status': 'str',
        'created': 'str',
        'ended': 'str',
        'process': 'str',
        'instance': 'GetTaskDetailListRspJobsInstance',
        'entities': 'object',
        'fail_reason': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'created': 'created',
        'ended': 'ended',
        'process': 'process',
        'instance': 'instance',
        'entities': 'entities',
        'fail_reason': 'fail_reason'
    }

    def __init__(self, id=None, name=None, status=None, created=None, ended=None, process=None, instance=None, entities=None, fail_reason=None):
        """GetJobInfoResponseBodyJob

        The model defined in g42cloud sdk

        :param id: The param of the GetJobInfoResponseBodyJob
        :type id: str
        :param name: The param of the GetJobInfoResponseBodyJob
        :type name: str
        :param status: The param of the GetJobInfoResponseBodyJob
        :type status: str
        :param created: The param of the GetJobInfoResponseBodyJob
        :type created: str
        :param ended: The param of the GetJobInfoResponseBodyJob
        :type ended: str
        :param process: The param of the GetJobInfoResponseBodyJob
        :type process: str
        :param instance: The param of the GetJobInfoResponseBodyJob
        :type instance: :class:`g42cloudsdkrds.v3.GetTaskDetailListRspJobsInstance`
        :param entities: The param of the GetJobInfoResponseBodyJob
        :type entities: object
        :param fail_reason: The param of the GetJobInfoResponseBodyJob
        :type fail_reason: str
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._created = None
        self._ended = None
        self._process = None
        self._instance = None
        self._entities = None
        self._fail_reason = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.status = status
        self.created = created
        if ended is not None:
            self.ended = ended
        if process is not None:
            self.process = process
        self.instance = instance
        if entities is not None:
            self.entities = entities
        if fail_reason is not None:
            self.fail_reason = fail_reason

    @property
    def id(self):
        """Gets the id of this GetJobInfoResponseBodyJob.

        :return: The id of this GetJobInfoResponseBodyJob.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetJobInfoResponseBodyJob.

        :param id: The id of this GetJobInfoResponseBodyJob.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this GetJobInfoResponseBodyJob.

        :return: The name of this GetJobInfoResponseBodyJob.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetJobInfoResponseBodyJob.

        :param name: The name of this GetJobInfoResponseBodyJob.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this GetJobInfoResponseBodyJob.

        :return: The status of this GetJobInfoResponseBodyJob.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GetJobInfoResponseBodyJob.

        :param status: The status of this GetJobInfoResponseBodyJob.
        :type status: str
        """
        self._status = status

    @property
    def created(self):
        """Gets the created of this GetJobInfoResponseBodyJob.

        :return: The created of this GetJobInfoResponseBodyJob.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this GetJobInfoResponseBodyJob.

        :param created: The created of this GetJobInfoResponseBodyJob.
        :type created: str
        """
        self._created = created

    @property
    def ended(self):
        """Gets the ended of this GetJobInfoResponseBodyJob.

        :return: The ended of this GetJobInfoResponseBodyJob.
        :rtype: str
        """
        return self._ended

    @ended.setter
    def ended(self, ended):
        """Sets the ended of this GetJobInfoResponseBodyJob.

        :param ended: The ended of this GetJobInfoResponseBodyJob.
        :type ended: str
        """
        self._ended = ended

    @property
    def process(self):
        """Gets the process of this GetJobInfoResponseBodyJob.

        :return: The process of this GetJobInfoResponseBodyJob.
        :rtype: str
        """
        return self._process

    @process.setter
    def process(self, process):
        """Sets the process of this GetJobInfoResponseBodyJob.

        :param process: The process of this GetJobInfoResponseBodyJob.
        :type process: str
        """
        self._process = process

    @property
    def instance(self):
        """Gets the instance of this GetJobInfoResponseBodyJob.

        :return: The instance of this GetJobInfoResponseBodyJob.
        :rtype: :class:`g42cloudsdkrds.v3.GetTaskDetailListRspJobsInstance`
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """Sets the instance of this GetJobInfoResponseBodyJob.

        :param instance: The instance of this GetJobInfoResponseBodyJob.
        :type instance: :class:`g42cloudsdkrds.v3.GetTaskDetailListRspJobsInstance`
        """
        self._instance = instance

    @property
    def entities(self):
        """Gets the entities of this GetJobInfoResponseBodyJob.

        :return: The entities of this GetJobInfoResponseBodyJob.
        :rtype: object
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """Sets the entities of this GetJobInfoResponseBodyJob.

        :param entities: The entities of this GetJobInfoResponseBodyJob.
        :type entities: object
        """
        self._entities = entities

    @property
    def fail_reason(self):
        """Gets the fail_reason of this GetJobInfoResponseBodyJob.

        :return: The fail_reason of this GetJobInfoResponseBodyJob.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        """Sets the fail_reason of this GetJobInfoResponseBodyJob.

        :param fail_reason: The fail_reason of this GetJobInfoResponseBodyJob.
        :type fail_reason: str
        """
        self._fail_reason = fail_reason

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
        if not isinstance(other, GetJobInfoResponseBodyJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
