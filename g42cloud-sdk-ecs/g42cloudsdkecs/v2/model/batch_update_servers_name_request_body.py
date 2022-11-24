# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdateServersNameRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'dry_run': 'bool',
        'servers': 'list[ServerId]'
    }

    attribute_map = {
        'name': 'name',
        'dry_run': 'dry_run',
        'servers': 'servers'
    }

    def __init__(self, name=None, dry_run=None, servers=None):
        """BatchUpdateServersNameRequestBody

        The model defined in g42cloud sdk

        :param name: The param of the BatchUpdateServersNameRequestBody
        :type name: str
        :param dry_run: The param of the BatchUpdateServersNameRequestBody
        :type dry_run: bool
        :param servers: The param of the BatchUpdateServersNameRequestBody
        :type servers: list[:class:`g42cloudsdkecs.v2.ServerId`]
        """
        
        

        self._name = None
        self._dry_run = None
        self._servers = None
        self.discriminator = None

        self.name = name
        if dry_run is not None:
            self.dry_run = dry_run
        self.servers = servers

    @property
    def name(self):
        """Gets the name of this BatchUpdateServersNameRequestBody.

        :return: The name of this BatchUpdateServersNameRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BatchUpdateServersNameRequestBody.

        :param name: The name of this BatchUpdateServersNameRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def dry_run(self):
        """Gets the dry_run of this BatchUpdateServersNameRequestBody.

        :return: The dry_run of this BatchUpdateServersNameRequestBody.
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        """Sets the dry_run of this BatchUpdateServersNameRequestBody.

        :param dry_run: The dry_run of this BatchUpdateServersNameRequestBody.
        :type dry_run: bool
        """
        self._dry_run = dry_run

    @property
    def servers(self):
        """Gets the servers of this BatchUpdateServersNameRequestBody.

        :return: The servers of this BatchUpdateServersNameRequestBody.
        :rtype: list[:class:`g42cloudsdkecs.v2.ServerId`]
        """
        return self._servers

    @servers.setter
    def servers(self, servers):
        """Sets the servers of this BatchUpdateServersNameRequestBody.

        :param servers: The servers of this BatchUpdateServersNameRequestBody.
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
        if not isinstance(other, BatchUpdateServersNameRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
