# coding: utf-8

import six

from g42cloudsdkcore.sdk_response import SdkResponse
from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBackupsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'backups': 'list[BackupResp]',
        'count': 'int',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'backups': 'backups',
        'count': 'count',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, backups=None, count=None, offset=None, limit=None):
        """ListBackupsResponse

        The model defined in g42cloud sdk

        :param backups: The param of the ListBackupsResponse
        :type backups: list[:class:`g42cloudsdkcbr.v1.BackupResp`]
        :param count: The param of the ListBackupsResponse
        :type count: int
        :param offset: The param of the ListBackupsResponse
        :type offset: int
        :param limit: The param of the ListBackupsResponse
        :type limit: int
        """
        
        super(ListBackupsResponse, self).__init__()

        self._backups = None
        self._count = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if backups is not None:
            self.backups = backups
        if count is not None:
            self.count = count
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def backups(self):
        """Gets the backups of this ListBackupsResponse.

        :return: The backups of this ListBackupsResponse.
        :rtype: list[:class:`g42cloudsdkcbr.v1.BackupResp`]
        """
        return self._backups

    @backups.setter
    def backups(self, backups):
        """Sets the backups of this ListBackupsResponse.

        :param backups: The backups of this ListBackupsResponse.
        :type backups: list[:class:`g42cloudsdkcbr.v1.BackupResp`]
        """
        self._backups = backups

    @property
    def count(self):
        """Gets the count of this ListBackupsResponse.

        :return: The count of this ListBackupsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListBackupsResponse.

        :param count: The count of this ListBackupsResponse.
        :type count: int
        """
        self._count = count

    @property
    def offset(self):
        """Gets the offset of this ListBackupsResponse.

        :return: The offset of this ListBackupsResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListBackupsResponse.

        :param offset: The offset of this ListBackupsResponse.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListBackupsResponse.

        :return: The limit of this ListBackupsResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListBackupsResponse.

        :param limit: The limit of this ListBackupsResponse.
        :type limit: int
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
        if not isinstance(other, ListBackupsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
