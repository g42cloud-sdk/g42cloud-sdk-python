# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class BucketAuthorizedReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bucket': 'str',
        'operation': 'str'
    }

    attribute_map = {
        'bucket': 'bucket',
        'operation': 'operation'
    }

    def __init__(self, bucket=None, operation=None):
        """BucketAuthorizedReq

        The model defined in g42cloud sdk

        :param bucket: The param of the BucketAuthorizedReq
        :type bucket: str
        :param operation: The param of the BucketAuthorizedReq
        :type operation: str
        """
        
        

        self._bucket = None
        self._operation = None
        self.discriminator = None

        self.bucket = bucket
        self.operation = operation

    @property
    def bucket(self):
        """Gets the bucket of this BucketAuthorizedReq.

        :return: The bucket of this BucketAuthorizedReq.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this BucketAuthorizedReq.

        :param bucket: The bucket of this BucketAuthorizedReq.
        :type bucket: str
        """
        self._bucket = bucket

    @property
    def operation(self):
        """Gets the operation of this BucketAuthorizedReq.

        :return: The operation of this BucketAuthorizedReq.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this BucketAuthorizedReq.

        :param operation: The operation of this BucketAuthorizedReq.
        :type operation: str
        """
        self._operation = operation

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
        if not isinstance(other, BucketAuthorizedReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other