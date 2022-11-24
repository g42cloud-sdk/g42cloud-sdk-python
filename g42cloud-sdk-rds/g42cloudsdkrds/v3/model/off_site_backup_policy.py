# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OffSiteBackupPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'backup_type': 'str',
        'keep_days': 'int',
        'destination_region': 'str',
        'destination_project_id': 'str'
    }

    attribute_map = {
        'backup_type': 'backup_type',
        'keep_days': 'keep_days',
        'destination_region': 'destination_region',
        'destination_project_id': 'destination_project_id'
    }

    def __init__(self, backup_type=None, keep_days=None, destination_region=None, destination_project_id=None):
        """OffSiteBackupPolicy

        The model defined in g42cloud sdk

        :param backup_type: The param of the OffSiteBackupPolicy
        :type backup_type: str
        :param keep_days: The param of the OffSiteBackupPolicy
        :type keep_days: int
        :param destination_region: The param of the OffSiteBackupPolicy
        :type destination_region: str
        :param destination_project_id: The param of the OffSiteBackupPolicy
        :type destination_project_id: str
        """
        
        

        self._backup_type = None
        self._keep_days = None
        self._destination_region = None
        self._destination_project_id = None
        self.discriminator = None

        self.backup_type = backup_type
        self.keep_days = keep_days
        self.destination_region = destination_region
        self.destination_project_id = destination_project_id

    @property
    def backup_type(self):
        """Gets the backup_type of this OffSiteBackupPolicy.

        :return: The backup_type of this OffSiteBackupPolicy.
        :rtype: str
        """
        return self._backup_type

    @backup_type.setter
    def backup_type(self, backup_type):
        """Sets the backup_type of this OffSiteBackupPolicy.

        :param backup_type: The backup_type of this OffSiteBackupPolicy.
        :type backup_type: str
        """
        self._backup_type = backup_type

    @property
    def keep_days(self):
        """Gets the keep_days of this OffSiteBackupPolicy.

        :return: The keep_days of this OffSiteBackupPolicy.
        :rtype: int
        """
        return self._keep_days

    @keep_days.setter
    def keep_days(self, keep_days):
        """Sets the keep_days of this OffSiteBackupPolicy.

        :param keep_days: The keep_days of this OffSiteBackupPolicy.
        :type keep_days: int
        """
        self._keep_days = keep_days

    @property
    def destination_region(self):
        """Gets the destination_region of this OffSiteBackupPolicy.

        :return: The destination_region of this OffSiteBackupPolicy.
        :rtype: str
        """
        return self._destination_region

    @destination_region.setter
    def destination_region(self, destination_region):
        """Sets the destination_region of this OffSiteBackupPolicy.

        :param destination_region: The destination_region of this OffSiteBackupPolicy.
        :type destination_region: str
        """
        self._destination_region = destination_region

    @property
    def destination_project_id(self):
        """Gets the destination_project_id of this OffSiteBackupPolicy.

        :return: The destination_project_id of this OffSiteBackupPolicy.
        :rtype: str
        """
        return self._destination_project_id

    @destination_project_id.setter
    def destination_project_id(self, destination_project_id):
        """Sets the destination_project_id of this OffSiteBackupPolicy.

        :param destination_project_id: The destination_project_id of this OffSiteBackupPolicy.
        :type destination_project_id: str
        """
        self._destination_project_id = destination_project_id

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
        if not isinstance(other, OffSiteBackupPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
