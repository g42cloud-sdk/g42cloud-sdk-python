# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class Statement:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sid': 'str',
        'effect': 'str',
        'principal': 'str',
        'not_principal': 'str',
        'action': 'str',
        'not_action': 'str',
        'resource': 'str',
        'not_resource': 'str'
    }

    attribute_map = {
        'sid': 'Sid',
        'effect': 'Effect',
        'principal': 'Principal',
        'not_principal': 'NotPrincipal',
        'action': 'Action',
        'not_action': 'NotAction',
        'resource': 'Resource',
        'not_resource': 'NotResource'
    }

    def __init__(self, sid=None, effect=None, principal=None, not_principal=None, action=None, not_action=None, resource=None, not_resource=None):
        """Statement

        The model defined in g42cloud sdk

        :param sid: The param of the Statement
        :type sid: str
        :param effect: The param of the Statement
        :type effect: str
        :param principal: The param of the Statement
        :type principal: str
        :param not_principal: The param of the Statement
        :type not_principal: str
        :param action: The param of the Statement
        :type action: str
        :param not_action: The param of the Statement
        :type not_action: str
        :param resource: The param of the Statement
        :type resource: str
        :param not_resource: The param of the Statement
        :type not_resource: str
        """
        
        

        self._sid = None
        self._effect = None
        self._principal = None
        self._not_principal = None
        self._action = None
        self._not_action = None
        self._resource = None
        self._not_resource = None
        self.discriminator = None

        self.sid = sid
        self.effect = effect
        if principal is not None:
            self.principal = principal
        if not_principal is not None:
            self.not_principal = not_principal
        if action is not None:
            self.action = action
        if not_action is not None:
            self.not_action = not_action
        if resource is not None:
            self.resource = resource
        if not_resource is not None:
            self.not_resource = not_resource

    @property
    def sid(self):
        """Gets the sid of this Statement.

        :return: The sid of this Statement.
        :rtype: str
        """
        return self._sid

    @sid.setter
    def sid(self, sid):
        """Sets the sid of this Statement.

        :param sid: The sid of this Statement.
        :type sid: str
        """
        self._sid = sid

    @property
    def effect(self):
        """Gets the effect of this Statement.

        :return: The effect of this Statement.
        :rtype: str
        """
        return self._effect

    @effect.setter
    def effect(self, effect):
        """Sets the effect of this Statement.

        :param effect: The effect of this Statement.
        :type effect: str
        """
        self._effect = effect

    @property
    def principal(self):
        """Gets the principal of this Statement.

        :return: The principal of this Statement.
        :rtype: str
        """
        return self._principal

    @principal.setter
    def principal(self, principal):
        """Sets the principal of this Statement.

        :param principal: The principal of this Statement.
        :type principal: str
        """
        self._principal = principal

    @property
    def not_principal(self):
        """Gets the not_principal of this Statement.

        :return: The not_principal of this Statement.
        :rtype: str
        """
        return self._not_principal

    @not_principal.setter
    def not_principal(self, not_principal):
        """Sets the not_principal of this Statement.

        :param not_principal: The not_principal of this Statement.
        :type not_principal: str
        """
        self._not_principal = not_principal

    @property
    def action(self):
        """Gets the action of this Statement.

        :return: The action of this Statement.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this Statement.

        :param action: The action of this Statement.
        :type action: str
        """
        self._action = action

    @property
    def not_action(self):
        """Gets the not_action of this Statement.

        :return: The not_action of this Statement.
        :rtype: str
        """
        return self._not_action

    @not_action.setter
    def not_action(self, not_action):
        """Sets the not_action of this Statement.

        :param not_action: The not_action of this Statement.
        :type not_action: str
        """
        self._not_action = not_action

    @property
    def resource(self):
        """Gets the resource of this Statement.

        :return: The resource of this Statement.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this Statement.

        :param resource: The resource of this Statement.
        :type resource: str
        """
        self._resource = resource

    @property
    def not_resource(self):
        """Gets the not_resource of this Statement.

        :return: The not_resource of this Statement.
        :rtype: str
        """
        return self._not_resource

    @not_resource.setter
    def not_resource(self, not_resource):
        """Sets the not_resource of this Statement.

        :param not_resource: The not_resource of this Statement.
        :type not_resource: str
        """
        self._not_resource = not_resource

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
        if not isinstance(other, Statement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
