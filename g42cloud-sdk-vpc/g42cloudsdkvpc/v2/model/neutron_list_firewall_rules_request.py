# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NeutronListFirewallRulesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'marker': 'str',
        'limit': 'int',
        'id': 'list[str]',
        'name': 'list[str]',
        'description': 'list[str]',
        'action': 'str',
        'tenant_id': 'str'
    }

    attribute_map = {
        'marker': 'marker',
        'limit': 'limit',
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'action': 'action',
        'tenant_id': 'tenant_id'
    }

    def __init__(self, marker=None, limit=None, id=None, name=None, description=None, action=None, tenant_id=None):
        """NeutronListFirewallRulesRequest

        The model defined in g42cloud sdk

        :param marker: The param of the NeutronListFirewallRulesRequest
        :type marker: str
        :param limit: The param of the NeutronListFirewallRulesRequest
        :type limit: int
        :param id: The param of the NeutronListFirewallRulesRequest
        :type id: list[str]
        :param name: The param of the NeutronListFirewallRulesRequest
        :type name: list[str]
        :param description: The param of the NeutronListFirewallRulesRequest
        :type description: list[str]
        :param action: The param of the NeutronListFirewallRulesRequest
        :type action: str
        :param tenant_id: The param of the NeutronListFirewallRulesRequest
        :type tenant_id: str
        """
        
        

        self._marker = None
        self._limit = None
        self._id = None
        self._name = None
        self._description = None
        self._action = None
        self._tenant_id = None
        self.discriminator = None

        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if action is not None:
            self.action = action
        if tenant_id is not None:
            self.tenant_id = tenant_id

    @property
    def marker(self):
        """Gets the marker of this NeutronListFirewallRulesRequest.

        :return: The marker of this NeutronListFirewallRulesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this NeutronListFirewallRulesRequest.

        :param marker: The marker of this NeutronListFirewallRulesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        """Gets the limit of this NeutronListFirewallRulesRequest.

        :return: The limit of this NeutronListFirewallRulesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this NeutronListFirewallRulesRequest.

        :param limit: The limit of this NeutronListFirewallRulesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def id(self):
        """Gets the id of this NeutronListFirewallRulesRequest.

        :return: The id of this NeutronListFirewallRulesRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NeutronListFirewallRulesRequest.

        :param id: The id of this NeutronListFirewallRulesRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this NeutronListFirewallRulesRequest.

        :return: The name of this NeutronListFirewallRulesRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NeutronListFirewallRulesRequest.

        :param name: The name of this NeutronListFirewallRulesRequest.
        :type name: list[str]
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this NeutronListFirewallRulesRequest.

        :return: The description of this NeutronListFirewallRulesRequest.
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NeutronListFirewallRulesRequest.

        :param description: The description of this NeutronListFirewallRulesRequest.
        :type description: list[str]
        """
        self._description = description

    @property
    def action(self):
        """Gets the action of this NeutronListFirewallRulesRequest.

        :return: The action of this NeutronListFirewallRulesRequest.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this NeutronListFirewallRulesRequest.

        :param action: The action of this NeutronListFirewallRulesRequest.
        :type action: str
        """
        self._action = action

    @property
    def tenant_id(self):
        """Gets the tenant_id of this NeutronListFirewallRulesRequest.

        :return: The tenant_id of this NeutronListFirewallRulesRequest.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this NeutronListFirewallRulesRequest.

        :param tenant_id: The tenant_id of this NeutronListFirewallRulesRequest.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

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
        if not isinstance(other, NeutronListFirewallRulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
