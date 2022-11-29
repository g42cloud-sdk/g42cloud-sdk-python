# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckpointReplicateRespBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'backups': 'list[CheckpointReplicateRespbackups]',
        'destination_project_id': 'str',
        'destination_region': 'str',
        'destination_vault_id': 'str',
        'project_id': 'str',
        'provider_id': 'str',
        'source_region': 'str',
        'vault_id': 'str'
    }

    attribute_map = {
        'backups': 'backups',
        'destination_project_id': 'destination_project_id',
        'destination_region': 'destination_region',
        'destination_vault_id': 'destination_vault_id',
        'project_id': 'project_id',
        'provider_id': 'provider_id',
        'source_region': 'source_region',
        'vault_id': 'vault_id'
    }

    def __init__(self, backups=None, destination_project_id=None, destination_region=None, destination_vault_id=None, project_id=None, provider_id=None, source_region=None, vault_id=None):
        """CheckpointReplicateRespBody

        The model defined in g42cloud sdk

        :param backups: The param of the CheckpointReplicateRespBody
        :type backups: list[:class:`g42cloudsdkcbr.v1.CheckpointReplicateRespbackups`]
        :param destination_project_id: The param of the CheckpointReplicateRespBody
        :type destination_project_id: str
        :param destination_region: The param of the CheckpointReplicateRespBody
        :type destination_region: str
        :param destination_vault_id: The param of the CheckpointReplicateRespBody
        :type destination_vault_id: str
        :param project_id: The param of the CheckpointReplicateRespBody
        :type project_id: str
        :param provider_id: The param of the CheckpointReplicateRespBody
        :type provider_id: str
        :param source_region: The param of the CheckpointReplicateRespBody
        :type source_region: str
        :param vault_id: The param of the CheckpointReplicateRespBody
        :type vault_id: str
        """
        
        

        self._backups = None
        self._destination_project_id = None
        self._destination_region = None
        self._destination_vault_id = None
        self._project_id = None
        self._provider_id = None
        self._source_region = None
        self._vault_id = None
        self.discriminator = None

        self.backups = backups
        self.destination_project_id = destination_project_id
        self.destination_region = destination_region
        self.destination_vault_id = destination_vault_id
        self.project_id = project_id
        self.provider_id = provider_id
        self.source_region = source_region
        self.vault_id = vault_id

    @property
    def backups(self):
        """Gets the backups of this CheckpointReplicateRespBody.

        :return: The backups of this CheckpointReplicateRespBody.
        :rtype: list[:class:`g42cloudsdkcbr.v1.CheckpointReplicateRespbackups`]
        """
        return self._backups

    @backups.setter
    def backups(self, backups):
        """Sets the backups of this CheckpointReplicateRespBody.

        :param backups: The backups of this CheckpointReplicateRespBody.
        :type backups: list[:class:`g42cloudsdkcbr.v1.CheckpointReplicateRespbackups`]
        """
        self._backups = backups

    @property
    def destination_project_id(self):
        """Gets the destination_project_id of this CheckpointReplicateRespBody.

        :return: The destination_project_id of this CheckpointReplicateRespBody.
        :rtype: str
        """
        return self._destination_project_id

    @destination_project_id.setter
    def destination_project_id(self, destination_project_id):
        """Sets the destination_project_id of this CheckpointReplicateRespBody.

        :param destination_project_id: The destination_project_id of this CheckpointReplicateRespBody.
        :type destination_project_id: str
        """
        self._destination_project_id = destination_project_id

    @property
    def destination_region(self):
        """Gets the destination_region of this CheckpointReplicateRespBody.

        :return: The destination_region of this CheckpointReplicateRespBody.
        :rtype: str
        """
        return self._destination_region

    @destination_region.setter
    def destination_region(self, destination_region):
        """Sets the destination_region of this CheckpointReplicateRespBody.

        :param destination_region: The destination_region of this CheckpointReplicateRespBody.
        :type destination_region: str
        """
        self._destination_region = destination_region

    @property
    def destination_vault_id(self):
        """Gets the destination_vault_id of this CheckpointReplicateRespBody.

        :return: The destination_vault_id of this CheckpointReplicateRespBody.
        :rtype: str
        """
        return self._destination_vault_id

    @destination_vault_id.setter
    def destination_vault_id(self, destination_vault_id):
        """Sets the destination_vault_id of this CheckpointReplicateRespBody.

        :param destination_vault_id: The destination_vault_id of this CheckpointReplicateRespBody.
        :type destination_vault_id: str
        """
        self._destination_vault_id = destination_vault_id

    @property
    def project_id(self):
        """Gets the project_id of this CheckpointReplicateRespBody.

        :return: The project_id of this CheckpointReplicateRespBody.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CheckpointReplicateRespBody.

        :param project_id: The project_id of this CheckpointReplicateRespBody.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def provider_id(self):
        """Gets the provider_id of this CheckpointReplicateRespBody.

        :return: The provider_id of this CheckpointReplicateRespBody.
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        """Sets the provider_id of this CheckpointReplicateRespBody.

        :param provider_id: The provider_id of this CheckpointReplicateRespBody.
        :type provider_id: str
        """
        self._provider_id = provider_id

    @property
    def source_region(self):
        """Gets the source_region of this CheckpointReplicateRespBody.

        :return: The source_region of this CheckpointReplicateRespBody.
        :rtype: str
        """
        return self._source_region

    @source_region.setter
    def source_region(self, source_region):
        """Sets the source_region of this CheckpointReplicateRespBody.

        :param source_region: The source_region of this CheckpointReplicateRespBody.
        :type source_region: str
        """
        self._source_region = source_region

    @property
    def vault_id(self):
        """Gets the vault_id of this CheckpointReplicateRespBody.

        :return: The vault_id of this CheckpointReplicateRespBody.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        """Sets the vault_id of this CheckpointReplicateRespBody.

        :param vault_id: The vault_id of this CheckpointReplicateRespBody.
        :type vault_id: str
        """
        self._vault_id = vault_id

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
        if not isinstance(other, CheckpointReplicateRespBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
