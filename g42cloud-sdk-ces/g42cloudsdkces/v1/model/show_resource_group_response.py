# coding: utf-8

import six

from g42cloudsdkcore.sdk_response import SdkResponse
from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowResourceGroupResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_name': 'str',
        'group_id': 'str',
        'resources': 'list[ResourceGroup]',
        'status': 'str',
        'create_time': 'int',
        'meta_data': 'MetaData',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'group_name': 'group_name',
        'group_id': 'group_id',
        'resources': 'resources',
        'status': 'status',
        'create_time': 'create_time',
        'meta_data': 'meta_data',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, group_name=None, group_id=None, resources=None, status=None, create_time=None, meta_data=None, enterprise_project_id=None):
        """ShowResourceGroupResponse

        The model defined in g42cloud sdk

        :param group_name: The param of the ShowResourceGroupResponse
        :type group_name: str
        :param group_id: The param of the ShowResourceGroupResponse
        :type group_id: str
        :param resources: The param of the ShowResourceGroupResponse
        :type resources: list[:class:`g42cloudsdkces.v1.ResourceGroup`]
        :param status: The param of the ShowResourceGroupResponse
        :type status: str
        :param create_time: The param of the ShowResourceGroupResponse
        :type create_time: int
        :param meta_data: The param of the ShowResourceGroupResponse
        :type meta_data: :class:`g42cloudsdkces.v1.MetaData`
        :param enterprise_project_id: The param of the ShowResourceGroupResponse
        :type enterprise_project_id: str
        """
        
        super(ShowResourceGroupResponse, self).__init__()

        self._group_name = None
        self._group_id = None
        self._resources = None
        self._status = None
        self._create_time = None
        self._meta_data = None
        self._enterprise_project_id = None
        self.discriminator = None

        if group_name is not None:
            self.group_name = group_name
        if group_id is not None:
            self.group_id = group_id
        if resources is not None:
            self.resources = resources
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time
        if meta_data is not None:
            self.meta_data = meta_data
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def group_name(self):
        """Gets the group_name of this ShowResourceGroupResponse.

        :return: The group_name of this ShowResourceGroupResponse.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this ShowResourceGroupResponse.

        :param group_name: The group_name of this ShowResourceGroupResponse.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def group_id(self):
        """Gets the group_id of this ShowResourceGroupResponse.

        :return: The group_id of this ShowResourceGroupResponse.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ShowResourceGroupResponse.

        :param group_id: The group_id of this ShowResourceGroupResponse.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def resources(self):
        """Gets the resources of this ShowResourceGroupResponse.

        :return: The resources of this ShowResourceGroupResponse.
        :rtype: list[:class:`g42cloudsdkces.v1.ResourceGroup`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this ShowResourceGroupResponse.

        :param resources: The resources of this ShowResourceGroupResponse.
        :type resources: list[:class:`g42cloudsdkces.v1.ResourceGroup`]
        """
        self._resources = resources

    @property
    def status(self):
        """Gets the status of this ShowResourceGroupResponse.

        :return: The status of this ShowResourceGroupResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowResourceGroupResponse.

        :param status: The status of this ShowResourceGroupResponse.
        :type status: str
        """
        self._status = status

    @property
    def create_time(self):
        """Gets the create_time of this ShowResourceGroupResponse.

        :return: The create_time of this ShowResourceGroupResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowResourceGroupResponse.

        :param create_time: The create_time of this ShowResourceGroupResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def meta_data(self):
        """Gets the meta_data of this ShowResourceGroupResponse.

        :return: The meta_data of this ShowResourceGroupResponse.
        :rtype: :class:`g42cloudsdkces.v1.MetaData`
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        """Sets the meta_data of this ShowResourceGroupResponse.

        :param meta_data: The meta_data of this ShowResourceGroupResponse.
        :type meta_data: :class:`g42cloudsdkces.v1.MetaData`
        """
        self._meta_data = meta_data

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ShowResourceGroupResponse.

        :return: The enterprise_project_id of this ShowResourceGroupResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ShowResourceGroupResponse.

        :param enterprise_project_id: The enterprise_project_id of this ShowResourceGroupResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ShowResourceGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
