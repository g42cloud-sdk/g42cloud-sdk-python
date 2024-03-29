# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateLoadBalancerOption:

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
        'admin_state_up': 'bool',
        'description': 'str',
        'ipv6_vip_virsubnet_id': 'str',
        'vip_subnet_cidr_id': 'str',
        'vip_address': 'str',
        'l4_flavor_id': 'str',
        'l7_flavor_id': 'str',
        'ipv6_bandwidth': 'BandwidthRef',
        'ip_target_enable': 'bool',
        'elb_virsubnet_ids': 'list[str]',
        'deletion_protection_enable': 'bool',
        'prepaid_options': 'PrepaidUpdateOption',
        'autoscaling': 'UpdateLoadbalancerAutoscalingOption',
        'waf_failure_action': 'str'
    }

    attribute_map = {
        'name': 'name',
        'admin_state_up': 'admin_state_up',
        'description': 'description',
        'ipv6_vip_virsubnet_id': 'ipv6_vip_virsubnet_id',
        'vip_subnet_cidr_id': 'vip_subnet_cidr_id',
        'vip_address': 'vip_address',
        'l4_flavor_id': 'l4_flavor_id',
        'l7_flavor_id': 'l7_flavor_id',
        'ipv6_bandwidth': 'ipv6_bandwidth',
        'ip_target_enable': 'ip_target_enable',
        'elb_virsubnet_ids': 'elb_virsubnet_ids',
        'deletion_protection_enable': 'deletion_protection_enable',
        'prepaid_options': 'prepaid_options',
        'autoscaling': 'autoscaling',
        'waf_failure_action': 'waf_failure_action'
    }

    def __init__(self, name=None, admin_state_up=None, description=None, ipv6_vip_virsubnet_id=None, vip_subnet_cidr_id=None, vip_address=None, l4_flavor_id=None, l7_flavor_id=None, ipv6_bandwidth=None, ip_target_enable=None, elb_virsubnet_ids=None, deletion_protection_enable=None, prepaid_options=None, autoscaling=None, waf_failure_action=None):
        """UpdateLoadBalancerOption

        The model defined in g42cloud sdk

        :param name: The param of the UpdateLoadBalancerOption
        :type name: str
        :param admin_state_up: The param of the UpdateLoadBalancerOption
        :type admin_state_up: bool
        :param description: The param of the UpdateLoadBalancerOption
        :type description: str
        :param ipv6_vip_virsubnet_id: The param of the UpdateLoadBalancerOption
        :type ipv6_vip_virsubnet_id: str
        :param vip_subnet_cidr_id: The param of the UpdateLoadBalancerOption
        :type vip_subnet_cidr_id: str
        :param vip_address: The param of the UpdateLoadBalancerOption
        :type vip_address: str
        :param l4_flavor_id: The param of the UpdateLoadBalancerOption
        :type l4_flavor_id: str
        :param l7_flavor_id: The param of the UpdateLoadBalancerOption
        :type l7_flavor_id: str
        :param ipv6_bandwidth: The param of the UpdateLoadBalancerOption
        :type ipv6_bandwidth: :class:`g42cloudsdkelb.v3.BandwidthRef`
        :param ip_target_enable: The param of the UpdateLoadBalancerOption
        :type ip_target_enable: bool
        :param elb_virsubnet_ids: The param of the UpdateLoadBalancerOption
        :type elb_virsubnet_ids: list[str]
        :param deletion_protection_enable: The param of the UpdateLoadBalancerOption
        :type deletion_protection_enable: bool
        :param prepaid_options: The param of the UpdateLoadBalancerOption
        :type prepaid_options: :class:`g42cloudsdkelb.v3.PrepaidUpdateOption`
        :param autoscaling: The param of the UpdateLoadBalancerOption
        :type autoscaling: :class:`g42cloudsdkelb.v3.UpdateLoadbalancerAutoscalingOption`
        :param waf_failure_action: The param of the UpdateLoadBalancerOption
        :type waf_failure_action: str
        """
        
        

        self._name = None
        self._admin_state_up = None
        self._description = None
        self._ipv6_vip_virsubnet_id = None
        self._vip_subnet_cidr_id = None
        self._vip_address = None
        self._l4_flavor_id = None
        self._l7_flavor_id = None
        self._ipv6_bandwidth = None
        self._ip_target_enable = None
        self._elb_virsubnet_ids = None
        self._deletion_protection_enable = None
        self._prepaid_options = None
        self._autoscaling = None
        self._waf_failure_action = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if description is not None:
            self.description = description
        if ipv6_vip_virsubnet_id is not None:
            self.ipv6_vip_virsubnet_id = ipv6_vip_virsubnet_id
        if vip_subnet_cidr_id is not None:
            self.vip_subnet_cidr_id = vip_subnet_cidr_id
        if vip_address is not None:
            self.vip_address = vip_address
        if l4_flavor_id is not None:
            self.l4_flavor_id = l4_flavor_id
        if l7_flavor_id is not None:
            self.l7_flavor_id = l7_flavor_id
        if ipv6_bandwidth is not None:
            self.ipv6_bandwidth = ipv6_bandwidth
        if ip_target_enable is not None:
            self.ip_target_enable = ip_target_enable
        if elb_virsubnet_ids is not None:
            self.elb_virsubnet_ids = elb_virsubnet_ids
        if deletion_protection_enable is not None:
            self.deletion_protection_enable = deletion_protection_enable
        if prepaid_options is not None:
            self.prepaid_options = prepaid_options
        if autoscaling is not None:
            self.autoscaling = autoscaling
        if waf_failure_action is not None:
            self.waf_failure_action = waf_failure_action

    @property
    def name(self):
        """Gets the name of this UpdateLoadBalancerOption.

        :return: The name of this UpdateLoadBalancerOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateLoadBalancerOption.

        :param name: The name of this UpdateLoadBalancerOption.
        :type name: str
        """
        self._name = name

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this UpdateLoadBalancerOption.

        :return: The admin_state_up of this UpdateLoadBalancerOption.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this UpdateLoadBalancerOption.

        :param admin_state_up: The admin_state_up of this UpdateLoadBalancerOption.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def description(self):
        """Gets the description of this UpdateLoadBalancerOption.

        :return: The description of this UpdateLoadBalancerOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateLoadBalancerOption.

        :param description: The description of this UpdateLoadBalancerOption.
        :type description: str
        """
        self._description = description

    @property
    def ipv6_vip_virsubnet_id(self):
        """Gets the ipv6_vip_virsubnet_id of this UpdateLoadBalancerOption.

        :return: The ipv6_vip_virsubnet_id of this UpdateLoadBalancerOption.
        :rtype: str
        """
        return self._ipv6_vip_virsubnet_id

    @ipv6_vip_virsubnet_id.setter
    def ipv6_vip_virsubnet_id(self, ipv6_vip_virsubnet_id):
        """Sets the ipv6_vip_virsubnet_id of this UpdateLoadBalancerOption.

        :param ipv6_vip_virsubnet_id: The ipv6_vip_virsubnet_id of this UpdateLoadBalancerOption.
        :type ipv6_vip_virsubnet_id: str
        """
        self._ipv6_vip_virsubnet_id = ipv6_vip_virsubnet_id

    @property
    def vip_subnet_cidr_id(self):
        """Gets the vip_subnet_cidr_id of this UpdateLoadBalancerOption.

        :return: The vip_subnet_cidr_id of this UpdateLoadBalancerOption.
        :rtype: str
        """
        return self._vip_subnet_cidr_id

    @vip_subnet_cidr_id.setter
    def vip_subnet_cidr_id(self, vip_subnet_cidr_id):
        """Sets the vip_subnet_cidr_id of this UpdateLoadBalancerOption.

        :param vip_subnet_cidr_id: The vip_subnet_cidr_id of this UpdateLoadBalancerOption.
        :type vip_subnet_cidr_id: str
        """
        self._vip_subnet_cidr_id = vip_subnet_cidr_id

    @property
    def vip_address(self):
        """Gets the vip_address of this UpdateLoadBalancerOption.

        :return: The vip_address of this UpdateLoadBalancerOption.
        :rtype: str
        """
        return self._vip_address

    @vip_address.setter
    def vip_address(self, vip_address):
        """Sets the vip_address of this UpdateLoadBalancerOption.

        :param vip_address: The vip_address of this UpdateLoadBalancerOption.
        :type vip_address: str
        """
        self._vip_address = vip_address

    @property
    def l4_flavor_id(self):
        """Gets the l4_flavor_id of this UpdateLoadBalancerOption.

        :return: The l4_flavor_id of this UpdateLoadBalancerOption.
        :rtype: str
        """
        return self._l4_flavor_id

    @l4_flavor_id.setter
    def l4_flavor_id(self, l4_flavor_id):
        """Sets the l4_flavor_id of this UpdateLoadBalancerOption.

        :param l4_flavor_id: The l4_flavor_id of this UpdateLoadBalancerOption.
        :type l4_flavor_id: str
        """
        self._l4_flavor_id = l4_flavor_id

    @property
    def l7_flavor_id(self):
        """Gets the l7_flavor_id of this UpdateLoadBalancerOption.

        :return: The l7_flavor_id of this UpdateLoadBalancerOption.
        :rtype: str
        """
        return self._l7_flavor_id

    @l7_flavor_id.setter
    def l7_flavor_id(self, l7_flavor_id):
        """Sets the l7_flavor_id of this UpdateLoadBalancerOption.

        :param l7_flavor_id: The l7_flavor_id of this UpdateLoadBalancerOption.
        :type l7_flavor_id: str
        """
        self._l7_flavor_id = l7_flavor_id

    @property
    def ipv6_bandwidth(self):
        """Gets the ipv6_bandwidth of this UpdateLoadBalancerOption.

        :return: The ipv6_bandwidth of this UpdateLoadBalancerOption.
        :rtype: :class:`g42cloudsdkelb.v3.BandwidthRef`
        """
        return self._ipv6_bandwidth

    @ipv6_bandwidth.setter
    def ipv6_bandwidth(self, ipv6_bandwidth):
        """Sets the ipv6_bandwidth of this UpdateLoadBalancerOption.

        :param ipv6_bandwidth: The ipv6_bandwidth of this UpdateLoadBalancerOption.
        :type ipv6_bandwidth: :class:`g42cloudsdkelb.v3.BandwidthRef`
        """
        self._ipv6_bandwidth = ipv6_bandwidth

    @property
    def ip_target_enable(self):
        """Gets the ip_target_enable of this UpdateLoadBalancerOption.

        :return: The ip_target_enable of this UpdateLoadBalancerOption.
        :rtype: bool
        """
        return self._ip_target_enable

    @ip_target_enable.setter
    def ip_target_enable(self, ip_target_enable):
        """Sets the ip_target_enable of this UpdateLoadBalancerOption.

        :param ip_target_enable: The ip_target_enable of this UpdateLoadBalancerOption.
        :type ip_target_enable: bool
        """
        self._ip_target_enable = ip_target_enable

    @property
    def elb_virsubnet_ids(self):
        """Gets the elb_virsubnet_ids of this UpdateLoadBalancerOption.

        :return: The elb_virsubnet_ids of this UpdateLoadBalancerOption.
        :rtype: list[str]
        """
        return self._elb_virsubnet_ids

    @elb_virsubnet_ids.setter
    def elb_virsubnet_ids(self, elb_virsubnet_ids):
        """Sets the elb_virsubnet_ids of this UpdateLoadBalancerOption.

        :param elb_virsubnet_ids: The elb_virsubnet_ids of this UpdateLoadBalancerOption.
        :type elb_virsubnet_ids: list[str]
        """
        self._elb_virsubnet_ids = elb_virsubnet_ids

    @property
    def deletion_protection_enable(self):
        """Gets the deletion_protection_enable of this UpdateLoadBalancerOption.

        :return: The deletion_protection_enable of this UpdateLoadBalancerOption.
        :rtype: bool
        """
        return self._deletion_protection_enable

    @deletion_protection_enable.setter
    def deletion_protection_enable(self, deletion_protection_enable):
        """Sets the deletion_protection_enable of this UpdateLoadBalancerOption.

        :param deletion_protection_enable: The deletion_protection_enable of this UpdateLoadBalancerOption.
        :type deletion_protection_enable: bool
        """
        self._deletion_protection_enable = deletion_protection_enable

    @property
    def prepaid_options(self):
        """Gets the prepaid_options of this UpdateLoadBalancerOption.

        :return: The prepaid_options of this UpdateLoadBalancerOption.
        :rtype: :class:`g42cloudsdkelb.v3.PrepaidUpdateOption`
        """
        return self._prepaid_options

    @prepaid_options.setter
    def prepaid_options(self, prepaid_options):
        """Sets the prepaid_options of this UpdateLoadBalancerOption.

        :param prepaid_options: The prepaid_options of this UpdateLoadBalancerOption.
        :type prepaid_options: :class:`g42cloudsdkelb.v3.PrepaidUpdateOption`
        """
        self._prepaid_options = prepaid_options

    @property
    def autoscaling(self):
        """Gets the autoscaling of this UpdateLoadBalancerOption.

        :return: The autoscaling of this UpdateLoadBalancerOption.
        :rtype: :class:`g42cloudsdkelb.v3.UpdateLoadbalancerAutoscalingOption`
        """
        return self._autoscaling

    @autoscaling.setter
    def autoscaling(self, autoscaling):
        """Sets the autoscaling of this UpdateLoadBalancerOption.

        :param autoscaling: The autoscaling of this UpdateLoadBalancerOption.
        :type autoscaling: :class:`g42cloudsdkelb.v3.UpdateLoadbalancerAutoscalingOption`
        """
        self._autoscaling = autoscaling

    @property
    def waf_failure_action(self):
        """Gets the waf_failure_action of this UpdateLoadBalancerOption.

        :return: The waf_failure_action of this UpdateLoadBalancerOption.
        :rtype: str
        """
        return self._waf_failure_action

    @waf_failure_action.setter
    def waf_failure_action(self, waf_failure_action):
        """Sets the waf_failure_action of this UpdateLoadBalancerOption.

        :param waf_failure_action: The waf_failure_action of this UpdateLoadBalancerOption.
        :type waf_failure_action: str
        """
        self._waf_failure_action = waf_failure_action

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
        if not isinstance(other, UpdateLoadBalancerOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
