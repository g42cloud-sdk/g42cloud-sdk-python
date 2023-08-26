# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class ObsInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bucket_name': 'str',
        'file_prefix_name': 'str',
        'is_obs_created': 'bool',
        'is_authorized_bucket': 'bool',
        'bucket_lifecycle': 'int'
    }

    attribute_map = {
        'bucket_name': 'bucket_name',
        'file_prefix_name': 'file_prefix_name',
        'is_obs_created': 'is_obs_created',
        'is_authorized_bucket': 'is_authorized_bucket',
        'bucket_lifecycle': 'bucket_lifecycle'
    }

    def __init__(self, bucket_name=None, file_prefix_name=None, is_obs_created=None, is_authorized_bucket=None, bucket_lifecycle=None):
        """ObsInfo

        The model defined in g42cloud sdk

        :param bucket_name: The param of the ObsInfo
        :type bucket_name: str
        :param file_prefix_name: The param of the ObsInfo
        :type file_prefix_name: str
        :param is_obs_created: The param of the ObsInfo
        :type is_obs_created: bool
        :param is_authorized_bucket: The param of the ObsInfo
        :type is_authorized_bucket: bool
        :param bucket_lifecycle: The param of the ObsInfo
        :type bucket_lifecycle: int
        """
        
        

        self._bucket_name = None
        self._file_prefix_name = None
        self._is_obs_created = None
        self._is_authorized_bucket = None
        self._bucket_lifecycle = None
        self.discriminator = None

        if bucket_name is not None:
            self.bucket_name = bucket_name
        if file_prefix_name is not None:
            self.file_prefix_name = file_prefix_name
        if is_obs_created is not None:
            self.is_obs_created = is_obs_created
        if is_authorized_bucket is not None:
            self.is_authorized_bucket = is_authorized_bucket
        if bucket_lifecycle is not None:
            self.bucket_lifecycle = bucket_lifecycle

    @property
    def bucket_name(self):
        """Gets the bucket_name of this ObsInfo.

        :return: The bucket_name of this ObsInfo.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """Sets the bucket_name of this ObsInfo.

        :param bucket_name: The bucket_name of this ObsInfo.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def file_prefix_name(self):
        """Gets the file_prefix_name of this ObsInfo.

        :return: The file_prefix_name of this ObsInfo.
        :rtype: str
        """
        return self._file_prefix_name

    @file_prefix_name.setter
    def file_prefix_name(self, file_prefix_name):
        """Sets the file_prefix_name of this ObsInfo.

        :param file_prefix_name: The file_prefix_name of this ObsInfo.
        :type file_prefix_name: str
        """
        self._file_prefix_name = file_prefix_name

    @property
    def is_obs_created(self):
        """Gets the is_obs_created of this ObsInfo.

        :return: The is_obs_created of this ObsInfo.
        :rtype: bool
        """
        return self._is_obs_created

    @is_obs_created.setter
    def is_obs_created(self, is_obs_created):
        """Sets the is_obs_created of this ObsInfo.

        :param is_obs_created: The is_obs_created of this ObsInfo.
        :type is_obs_created: bool
        """
        self._is_obs_created = is_obs_created

    @property
    def is_authorized_bucket(self):
        """Gets the is_authorized_bucket of this ObsInfo.

        :return: The is_authorized_bucket of this ObsInfo.
        :rtype: bool
        """
        return self._is_authorized_bucket

    @is_authorized_bucket.setter
    def is_authorized_bucket(self, is_authorized_bucket):
        """Sets the is_authorized_bucket of this ObsInfo.

        :param is_authorized_bucket: The is_authorized_bucket of this ObsInfo.
        :type is_authorized_bucket: bool
        """
        self._is_authorized_bucket = is_authorized_bucket

    @property
    def bucket_lifecycle(self):
        """Gets the bucket_lifecycle of this ObsInfo.

        :return: The bucket_lifecycle of this ObsInfo.
        :rtype: int
        """
        return self._bucket_lifecycle

    @bucket_lifecycle.setter
    def bucket_lifecycle(self, bucket_lifecycle):
        """Sets the bucket_lifecycle of this ObsInfo.

        :param bucket_lifecycle: The bucket_lifecycle of this ObsInfo.
        :type bucket_lifecycle: int
        """
        self._bucket_lifecycle = bucket_lifecycle

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
        if not isinstance(other, ObsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
