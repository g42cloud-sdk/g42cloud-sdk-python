# coding: utf-8

import six

from g42cloudsdkcore.sdk_response import SdkResponse
from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMigprojectResponse(SdkResponse):

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
        'description': 'str',
        'isdefault': 'bool',
        'template': 'TemplateResponseBody',
        'region': 'str',
        'start_target_server': 'bool',
        'speed_limit': 'int',
        'use_public_ip': 'bool',
        'exist_server': 'bool',
        'type': 'str',
        'enterprise_project': 'str',
        'syncing': 'bool',
        'start_network_check': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'isdefault': 'isdefault',
        'template': 'template',
        'region': 'region',
        'start_target_server': 'start_target_server',
        'speed_limit': 'speed_limit',
        'use_public_ip': 'use_public_ip',
        'exist_server': 'exist_server',
        'type': 'type',
        'enterprise_project': 'enterprise_project',
        'syncing': 'syncing',
        'start_network_check': 'start_network_check'
    }

    def __init__(self, id=None, name=None, description=None, isdefault=None, template=None, region=None, start_target_server=None, speed_limit=None, use_public_ip=None, exist_server=None, type=None, enterprise_project=None, syncing=None, start_network_check=None):
        """ShowMigprojectResponse

        The model defined in g42cloud sdk

        :param id: The param of the ShowMigprojectResponse
        :type id: str
        :param name: The param of the ShowMigprojectResponse
        :type name: str
        :param description: The param of the ShowMigprojectResponse
        :type description: str
        :param isdefault: The param of the ShowMigprojectResponse
        :type isdefault: bool
        :param template: The param of the ShowMigprojectResponse
        :type template: :class:`g42cloudsdksms.v3.TemplateResponseBody`
        :param region: The param of the ShowMigprojectResponse
        :type region: str
        :param start_target_server: The param of the ShowMigprojectResponse
        :type start_target_server: bool
        :param speed_limit: The param of the ShowMigprojectResponse
        :type speed_limit: int
        :param use_public_ip: The param of the ShowMigprojectResponse
        :type use_public_ip: bool
        :param exist_server: The param of the ShowMigprojectResponse
        :type exist_server: bool
        :param type: The param of the ShowMigprojectResponse
        :type type: str
        :param enterprise_project: The param of the ShowMigprojectResponse
        :type enterprise_project: str
        :param syncing: The param of the ShowMigprojectResponse
        :type syncing: bool
        :param start_network_check: The param of the ShowMigprojectResponse
        :type start_network_check: bool
        """
        
        super(ShowMigprojectResponse, self).__init__()

        self._id = None
        self._name = None
        self._description = None
        self._isdefault = None
        self._template = None
        self._region = None
        self._start_target_server = None
        self._speed_limit = None
        self._use_public_ip = None
        self._exist_server = None
        self._type = None
        self._enterprise_project = None
        self._syncing = None
        self._start_network_check = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if isdefault is not None:
            self.isdefault = isdefault
        if template is not None:
            self.template = template
        if region is not None:
            self.region = region
        if start_target_server is not None:
            self.start_target_server = start_target_server
        if speed_limit is not None:
            self.speed_limit = speed_limit
        if use_public_ip is not None:
            self.use_public_ip = use_public_ip
        if exist_server is not None:
            self.exist_server = exist_server
        if type is not None:
            self.type = type
        if enterprise_project is not None:
            self.enterprise_project = enterprise_project
        if syncing is not None:
            self.syncing = syncing
        if start_network_check is not None:
            self.start_network_check = start_network_check

    @property
    def id(self):
        """Gets the id of this ShowMigprojectResponse.

        :return: The id of this ShowMigprojectResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowMigprojectResponse.

        :param id: The id of this ShowMigprojectResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ShowMigprojectResponse.

        :return: The name of this ShowMigprojectResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowMigprojectResponse.

        :param name: The name of this ShowMigprojectResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ShowMigprojectResponse.

        :return: The description of this ShowMigprojectResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowMigprojectResponse.

        :param description: The description of this ShowMigprojectResponse.
        :type description: str
        """
        self._description = description

    @property
    def isdefault(self):
        """Gets the isdefault of this ShowMigprojectResponse.

        :return: The isdefault of this ShowMigprojectResponse.
        :rtype: bool
        """
        return self._isdefault

    @isdefault.setter
    def isdefault(self, isdefault):
        """Sets the isdefault of this ShowMigprojectResponse.

        :param isdefault: The isdefault of this ShowMigprojectResponse.
        :type isdefault: bool
        """
        self._isdefault = isdefault

    @property
    def template(self):
        """Gets the template of this ShowMigprojectResponse.

        :return: The template of this ShowMigprojectResponse.
        :rtype: :class:`g42cloudsdksms.v3.TemplateResponseBody`
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this ShowMigprojectResponse.

        :param template: The template of this ShowMigprojectResponse.
        :type template: :class:`g42cloudsdksms.v3.TemplateResponseBody`
        """
        self._template = template

    @property
    def region(self):
        """Gets the region of this ShowMigprojectResponse.

        :return: The region of this ShowMigprojectResponse.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ShowMigprojectResponse.

        :param region: The region of this ShowMigprojectResponse.
        :type region: str
        """
        self._region = region

    @property
    def start_target_server(self):
        """Gets the start_target_server of this ShowMigprojectResponse.

        :return: The start_target_server of this ShowMigprojectResponse.
        :rtype: bool
        """
        return self._start_target_server

    @start_target_server.setter
    def start_target_server(self, start_target_server):
        """Sets the start_target_server of this ShowMigprojectResponse.

        :param start_target_server: The start_target_server of this ShowMigprojectResponse.
        :type start_target_server: bool
        """
        self._start_target_server = start_target_server

    @property
    def speed_limit(self):
        """Gets the speed_limit of this ShowMigprojectResponse.

        :return: The speed_limit of this ShowMigprojectResponse.
        :rtype: int
        """
        return self._speed_limit

    @speed_limit.setter
    def speed_limit(self, speed_limit):
        """Sets the speed_limit of this ShowMigprojectResponse.

        :param speed_limit: The speed_limit of this ShowMigprojectResponse.
        :type speed_limit: int
        """
        self._speed_limit = speed_limit

    @property
    def use_public_ip(self):
        """Gets the use_public_ip of this ShowMigprojectResponse.

        :return: The use_public_ip of this ShowMigprojectResponse.
        :rtype: bool
        """
        return self._use_public_ip

    @use_public_ip.setter
    def use_public_ip(self, use_public_ip):
        """Sets the use_public_ip of this ShowMigprojectResponse.

        :param use_public_ip: The use_public_ip of this ShowMigprojectResponse.
        :type use_public_ip: bool
        """
        self._use_public_ip = use_public_ip

    @property
    def exist_server(self):
        """Gets the exist_server of this ShowMigprojectResponse.

        :return: The exist_server of this ShowMigprojectResponse.
        :rtype: bool
        """
        return self._exist_server

    @exist_server.setter
    def exist_server(self, exist_server):
        """Sets the exist_server of this ShowMigprojectResponse.

        :param exist_server: The exist_server of this ShowMigprojectResponse.
        :type exist_server: bool
        """
        self._exist_server = exist_server

    @property
    def type(self):
        """Gets the type of this ShowMigprojectResponse.

        :return: The type of this ShowMigprojectResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowMigprojectResponse.

        :param type: The type of this ShowMigprojectResponse.
        :type type: str
        """
        self._type = type

    @property
    def enterprise_project(self):
        """Gets the enterprise_project of this ShowMigprojectResponse.

        :return: The enterprise_project of this ShowMigprojectResponse.
        :rtype: str
        """
        return self._enterprise_project

    @enterprise_project.setter
    def enterprise_project(self, enterprise_project):
        """Sets the enterprise_project of this ShowMigprojectResponse.

        :param enterprise_project: The enterprise_project of this ShowMigprojectResponse.
        :type enterprise_project: str
        """
        self._enterprise_project = enterprise_project

    @property
    def syncing(self):
        """Gets the syncing of this ShowMigprojectResponse.

        :return: The syncing of this ShowMigprojectResponse.
        :rtype: bool
        """
        return self._syncing

    @syncing.setter
    def syncing(self, syncing):
        """Sets the syncing of this ShowMigprojectResponse.

        :param syncing: The syncing of this ShowMigprojectResponse.
        :type syncing: bool
        """
        self._syncing = syncing

    @property
    def start_network_check(self):
        """Gets the start_network_check of this ShowMigprojectResponse.

        :return: The start_network_check of this ShowMigprojectResponse.
        :rtype: bool
        """
        return self._start_network_check

    @start_network_check.setter
    def start_network_check(self, start_network_check):
        """Sets the start_network_check of this ShowMigprojectResponse.

        :param start_network_check: The start_network_check of this ShowMigprojectResponse.
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
        if not isinstance(other, ShowMigprojectResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
