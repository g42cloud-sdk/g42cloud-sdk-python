# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchResetServersPasswordRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'new_password': 'str',
        'dry_run': 'bool',
        'servers': 'list[ServerId]'
    }

    attribute_map = {
        'new_password': 'new_password',
        'dry_run': 'dry_run',
        'servers': 'servers'
    }

    def __init__(self, new_password=None, dry_run=None, servers=None):
        """BatchResetServersPasswordRequestBody

        The model defined in g42cloud sdk

        :param new_password: The param of the BatchResetServersPasswordRequestBody
        :type new_password: str
        :param dry_run: The param of the BatchResetServersPasswordRequestBody
        :type dry_run: bool
        :param servers: The param of the BatchResetServersPasswordRequestBody
        :type servers: list[:class:`g42cloudsdkecs.v2.ServerId`]
        """
        
        

        self._new_password = None
        self._dry_run = None
        self._servers = None
        self.discriminator = None

        self.new_password = new_password
        if dry_run is not None:
            self.dry_run = dry_run
        self.servers = servers

    @property
    def new_password(self):
        """Gets the new_password of this BatchResetServersPasswordRequestBody.

        :return: The new_password of this BatchResetServersPasswordRequestBody.
        :rtype: str
        """
        return self._new_password

    @new_password.setter
    def new_password(self, new_password):
        """Sets the new_password of this BatchResetServersPasswordRequestBody.

        :param new_password: The new_password of this BatchResetServersPasswordRequestBody.
        :type new_password: str
        """
        self._new_password = new_password

    @property
    def dry_run(self):
        """Gets the dry_run of this BatchResetServersPasswordRequestBody.

        :return: The dry_run of this BatchResetServersPasswordRequestBody.
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        """Sets the dry_run of this BatchResetServersPasswordRequestBody.

        :param dry_run: The dry_run of this BatchResetServersPasswordRequestBody.
        :type dry_run: bool
        """
        self._dry_run = dry_run

    @property
    def servers(self):
        """Gets the servers of this BatchResetServersPasswordRequestBody.

        :return: The servers of this BatchResetServersPasswordRequestBody.
        :rtype: list[:class:`g42cloudsdkecs.v2.ServerId`]
        """
        return self._servers

    @servers.setter
    def servers(self, servers):
        """Sets the servers of this BatchResetServersPasswordRequestBody.

        :param servers: The servers of this BatchResetServersPasswordRequestBody.
        :type servers: list[:class:`g42cloudsdkecs.v2.ServerId`]
        """
        self._servers = servers

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
        if not isinstance(other, BatchResetServersPasswordRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
