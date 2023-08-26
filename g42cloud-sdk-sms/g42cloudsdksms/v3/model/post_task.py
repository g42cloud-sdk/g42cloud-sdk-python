# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostTask:

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
        'type': 'str',
        'start_target_server': 'bool',
        'os_type': 'str',
        'source_server': 'SourceServerByTask',
        'target_server': 'TargetServerByTask',
        'migration_ip': 'str',
        'region_name': 'str',
        'region_id': 'str',
        'project_name': 'str',
        'project_id': 'str',
        'vm_template_id': 'str',
        'use_public_ip': 'bool',
        'syncing': 'bool',
        'exist_server': 'bool',
        'start_network_check': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'start_target_server': 'start_target_server',
        'os_type': 'os_type',
        'source_server': 'source_server',
        'target_server': 'target_server',
        'migration_ip': 'migration_ip',
        'region_name': 'region_name',
        'region_id': 'region_id',
        'project_name': 'project_name',
        'project_id': 'project_id',
        'vm_template_id': 'vm_template_id',
        'use_public_ip': 'use_public_ip',
        'syncing': 'syncing',
        'exist_server': 'exist_server',
        'start_network_check': 'start_network_check'
    }

    def __init__(self, name=None, type=None, start_target_server=None, os_type=None, source_server=None, target_server=None, migration_ip=None, region_name=None, region_id=None, project_name=None, project_id=None, vm_template_id=None, use_public_ip=None, syncing=None, exist_server=None, start_network_check=None):
        """PostTask

        The model defined in g42cloud sdk

        :param name: The param of the PostTask
        :type name: str
        :param type: The param of the PostTask
        :type type: str
        :param start_target_server: The param of the PostTask
        :type start_target_server: bool
        :param os_type: The param of the PostTask
        :type os_type: str
        :param source_server: The param of the PostTask
        :type source_server: :class:`g42cloudsdksms.v3.SourceServerByTask`
        :param target_server: The param of the PostTask
        :type target_server: :class:`g42cloudsdksms.v3.TargetServerByTask`
        :param migration_ip: The param of the PostTask
        :type migration_ip: str
        :param region_name: The param of the PostTask
        :type region_name: str
        :param region_id: The param of the PostTask
        :type region_id: str
        :param project_name: The param of the PostTask
        :type project_name: str
        :param project_id: The param of the PostTask
        :type project_id: str
        :param vm_template_id: The param of the PostTask
        :type vm_template_id: str
        :param use_public_ip: The param of the PostTask
        :type use_public_ip: bool
        :param syncing: The param of the PostTask
        :type syncing: bool
        :param exist_server: The param of the PostTask
        :type exist_server: bool
        :param start_network_check: The param of the PostTask
        :type start_network_check: bool
        """
        
        

        self._name = None
        self._type = None
        self._start_target_server = None
        self._os_type = None
        self._source_server = None
        self._target_server = None
        self._migration_ip = None
        self._region_name = None
        self._region_id = None
        self._project_name = None
        self._project_id = None
        self._vm_template_id = None
        self._use_public_ip = None
        self._syncing = None
        self._exist_server = None
        self._start_network_check = None
        self.discriminator = None

        self.name = name
        self.type = type
        if start_target_server is not None:
            self.start_target_server = start_target_server
        self.os_type = os_type
        self.source_server = source_server
        self.target_server = target_server
        if migration_ip is not None:
            self.migration_ip = migration_ip
        self.region_name = region_name
        self.region_id = region_id
        self.project_name = project_name
        self.project_id = project_id
        if vm_template_id is not None:
            self.vm_template_id = vm_template_id
        if use_public_ip is not None:
            self.use_public_ip = use_public_ip
        if syncing is not None:
            self.syncing = syncing
        if exist_server is not None:
            self.exist_server = exist_server
        if start_network_check is not None:
            self.start_network_check = start_network_check

    @property
    def name(self):
        """Gets the name of this PostTask.

        :return: The name of this PostTask.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PostTask.

        :param name: The name of this PostTask.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this PostTask.

        :return: The type of this PostTask.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PostTask.

        :param type: The type of this PostTask.
        :type type: str
        """
        self._type = type

    @property
    def start_target_server(self):
        """Gets the start_target_server of this PostTask.

        :return: The start_target_server of this PostTask.
        :rtype: bool
        """
        return self._start_target_server

    @start_target_server.setter
    def start_target_server(self, start_target_server):
        """Sets the start_target_server of this PostTask.

        :param start_target_server: The start_target_server of this PostTask.
        :type start_target_server: bool
        """
        self._start_target_server = start_target_server

    @property
    def os_type(self):
        """Gets the os_type of this PostTask.

        :return: The os_type of this PostTask.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this PostTask.

        :param os_type: The os_type of this PostTask.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def source_server(self):
        """Gets the source_server of this PostTask.

        :return: The source_server of this PostTask.
        :rtype: :class:`g42cloudsdksms.v3.SourceServerByTask`
        """
        return self._source_server

    @source_server.setter
    def source_server(self, source_server):
        """Sets the source_server of this PostTask.

        :param source_server: The source_server of this PostTask.
        :type source_server: :class:`g42cloudsdksms.v3.SourceServerByTask`
        """
        self._source_server = source_server

    @property
    def target_server(self):
        """Gets the target_server of this PostTask.

        :return: The target_server of this PostTask.
        :rtype: :class:`g42cloudsdksms.v3.TargetServerByTask`
        """
        return self._target_server

    @target_server.setter
    def target_server(self, target_server):
        """Sets the target_server of this PostTask.

        :param target_server: The target_server of this PostTask.
        :type target_server: :class:`g42cloudsdksms.v3.TargetServerByTask`
        """
        self._target_server = target_server

    @property
    def migration_ip(self):
        """Gets the migration_ip of this PostTask.

        :return: The migration_ip of this PostTask.
        :rtype: str
        """
        return self._migration_ip

    @migration_ip.setter
    def migration_ip(self, migration_ip):
        """Sets the migration_ip of this PostTask.

        :param migration_ip: The migration_ip of this PostTask.
        :type migration_ip: str
        """
        self._migration_ip = migration_ip

    @property
    def region_name(self):
        """Gets the region_name of this PostTask.

        :return: The region_name of this PostTask.
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        """Sets the region_name of this PostTask.

        :param region_name: The region_name of this PostTask.
        :type region_name: str
        """
        self._region_name = region_name

    @property
    def region_id(self):
        """Gets the region_id of this PostTask.

        :return: The region_id of this PostTask.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this PostTask.

        :param region_id: The region_id of this PostTask.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def project_name(self):
        """Gets the project_name of this PostTask.

        :return: The project_name of this PostTask.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this PostTask.

        :param project_name: The project_name of this PostTask.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def project_id(self):
        """Gets the project_id of this PostTask.

        :return: The project_id of this PostTask.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this PostTask.

        :param project_id: The project_id of this PostTask.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def vm_template_id(self):
        """Gets the vm_template_id of this PostTask.

        :return: The vm_template_id of this PostTask.
        :rtype: str
        """
        return self._vm_template_id

    @vm_template_id.setter
    def vm_template_id(self, vm_template_id):
        """Sets the vm_template_id of this PostTask.

        :param vm_template_id: The vm_template_id of this PostTask.
        :type vm_template_id: str
        """
        self._vm_template_id = vm_template_id

    @property
    def use_public_ip(self):
        """Gets the use_public_ip of this PostTask.

        :return: The use_public_ip of this PostTask.
        :rtype: bool
        """
        return self._use_public_ip

    @use_public_ip.setter
    def use_public_ip(self, use_public_ip):
        """Sets the use_public_ip of this PostTask.

        :param use_public_ip: The use_public_ip of this PostTask.
        :type use_public_ip: bool
        """
        self._use_public_ip = use_public_ip

    @property
    def syncing(self):
        """Gets the syncing of this PostTask.

        :return: The syncing of this PostTask.
        :rtype: bool
        """
        return self._syncing

    @syncing.setter
    def syncing(self, syncing):
        """Sets the syncing of this PostTask.

        :param syncing: The syncing of this PostTask.
        :type syncing: bool
        """
        self._syncing = syncing

    @property
    def exist_server(self):
        """Gets the exist_server of this PostTask.

        :return: The exist_server of this PostTask.
        :rtype: bool
        """
        return self._exist_server

    @exist_server.setter
    def exist_server(self, exist_server):
        """Sets the exist_server of this PostTask.

        :param exist_server: The exist_server of this PostTask.
        :type exist_server: bool
        """
        self._exist_server = exist_server

    @property
    def start_network_check(self):
        """Gets the start_network_check of this PostTask.

        :return: The start_network_check of this PostTask.
        :rtype: bool
        """
        return self._start_network_check

    @start_network_check.setter
    def start_network_check(self, start_network_check):
        """Sets the start_network_check of this PostTask.

        :param start_network_check: The start_network_check of this PostTask.
        :type start_network_check: bool
        """
        self._start_network_check = start_network_check

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
        if not isinstance(other, PostTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
