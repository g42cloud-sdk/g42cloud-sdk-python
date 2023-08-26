# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class Quota:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'loadbalancer': 'int',
        'certificate': 'int',
        'listener': 'int',
        'l7policy': 'int',
        'pool': 'int',
        'healthmonitor': 'int',
        'member': 'int',
        'members_per_pool': 'int',
        'ipgroup': 'int',
        'security_policy': 'int'
    }

    attribute_map = {
        'project_id': 'project_id',
        'loadbalancer': 'loadbalancer',
        'certificate': 'certificate',
        'listener': 'listener',
        'l7policy': 'l7policy',
        'pool': 'pool',
        'healthmonitor': 'healthmonitor',
        'member': 'member',
        'members_per_pool': 'members_per_pool',
        'ipgroup': 'ipgroup',
        'security_policy': 'security_policy'
    }

    def __init__(self, project_id=None, loadbalancer=None, certificate=None, listener=None, l7policy=None, pool=None, healthmonitor=None, member=None, members_per_pool=None, ipgroup=None, security_policy=None):
        """Quota

        The model defined in g42cloud sdk

        :param project_id: The param of the Quota
        :type project_id: str
        :param loadbalancer: The param of the Quota
        :type loadbalancer: int
        :param certificate: The param of the Quota
        :type certificate: int
        :param listener: The param of the Quota
        :type listener: int
        :param l7policy: The param of the Quota
        :type l7policy: int
        :param pool: The param of the Quota
        :type pool: int
        :param healthmonitor: The param of the Quota
        :type healthmonitor: int
        :param member: The param of the Quota
        :type member: int
        :param members_per_pool: The param of the Quota
        :type members_per_pool: int
        :param ipgroup: The param of the Quota
        :type ipgroup: int
        :param security_policy: The param of the Quota
        :type security_policy: int
        """
        
        

        self._project_id = None
        self._loadbalancer = None
        self._certificate = None
        self._listener = None
        self._l7policy = None
        self._pool = None
        self._healthmonitor = None
        self._member = None
        self._members_per_pool = None
        self._ipgroup = None
        self._security_policy = None
        self.discriminator = None

        self.project_id = project_id
        self.loadbalancer = loadbalancer
        self.certificate = certificate
        self.listener = listener
        self.l7policy = l7policy
        self.pool = pool
        self.healthmonitor = healthmonitor
        self.member = member
        self.members_per_pool = members_per_pool
        self.ipgroup = ipgroup
        self.security_policy = security_policy

    @property
    def project_id(self):
        """Gets the project_id of this Quota.

        :return: The project_id of this Quota.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Quota.

        :param project_id: The project_id of this Quota.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def loadbalancer(self):
        """Gets the loadbalancer of this Quota.

        :return: The loadbalancer of this Quota.
        :rtype: int
        """
        return self._loadbalancer

    @loadbalancer.setter
    def loadbalancer(self, loadbalancer):
        """Sets the loadbalancer of this Quota.

        :param loadbalancer: The loadbalancer of this Quota.
        :type loadbalancer: int
        """
        self._loadbalancer = loadbalancer

    @property
    def certificate(self):
        """Gets the certificate of this Quota.

        :return: The certificate of this Quota.
        :rtype: int
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this Quota.

        :param certificate: The certificate of this Quota.
        :type certificate: int
        """
        self._certificate = certificate

    @property
    def listener(self):
        """Gets the listener of this Quota.

        :return: The listener of this Quota.
        :rtype: int
        """
        return self._listener

    @listener.setter
    def listener(self, listener):
        """Sets the listener of this Quota.

        :param listener: The listener of this Quota.
        :type listener: int
        """
        self._listener = listener

    @property
    def l7policy(self):
        """Gets the l7policy of this Quota.

        :return: The l7policy of this Quota.
        :rtype: int
        """
        return self._l7policy

    @l7policy.setter
    def l7policy(self, l7policy):
        """Sets the l7policy of this Quota.

        :param l7policy: The l7policy of this Quota.
        :type l7policy: int
        """
        self._l7policy = l7policy

    @property
    def pool(self):
        """Gets the pool of this Quota.

        :return: The pool of this Quota.
        :rtype: int
        """
        return self._pool

    @pool.setter
    def pool(self, pool):
        """Sets the pool of this Quota.

        :param pool: The pool of this Quota.
        :type pool: int
        """
        self._pool = pool

    @property
    def healthmonitor(self):
        """Gets the healthmonitor of this Quota.

        :return: The healthmonitor of this Quota.
        :rtype: int
        """
        return self._healthmonitor

    @healthmonitor.setter
    def healthmonitor(self, healthmonitor):
        """Sets the healthmonitor of this Quota.

        :param healthmonitor: The healthmonitor of this Quota.
        :type healthmonitor: int
        """
        self._healthmonitor = healthmonitor

    @property
    def member(self):
        """Gets the member of this Quota.

        :return: The member of this Quota.
        :rtype: int
        """
        return self._member

    @member.setter
    def member(self, member):
        """Sets the member of this Quota.

        :param member: The member of this Quota.
        :type member: int
        """
        self._member = member

    @property
    def members_per_pool(self):
        """Gets the members_per_pool of this Quota.

        :return: The members_per_pool of this Quota.
        :rtype: int
        """
        return self._members_per_pool

    @members_per_pool.setter
    def members_per_pool(self, members_per_pool):
        """Sets the members_per_pool of this Quota.

        :param members_per_pool: The members_per_pool of this Quota.
        :type members_per_pool: int
        """
        self._members_per_pool = members_per_pool

    @property
    def ipgroup(self):
        """Gets the ipgroup of this Quota.

        :return: The ipgroup of this Quota.
        :rtype: int
        """
        return self._ipgroup

    @ipgroup.setter
    def ipgroup(self, ipgroup):
        """Sets the ipgroup of this Quota.

        :param ipgroup: The ipgroup of this Quota.
        :type ipgroup: int
        """
        self._ipgroup = ipgroup

    @property
    def security_policy(self):
        """Gets the security_policy of this Quota.

        :return: The security_policy of this Quota.
        :rtype: int
        """
        return self._security_policy

    @security_policy.setter
    def security_policy(self, security_policy):
        """Sets the security_policy of this Quota.

        :param security_policy: The security_policy of this Quota.
        :type security_policy: int
        """
        self._security_policy = security_policy

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
        if not isinstance(other, Quota):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
