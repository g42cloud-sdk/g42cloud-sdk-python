# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateLoadBalancerOption:

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
        'project_id': 'str',
        'name': 'str',
        'description': 'str',
        'vip_address': 'str',
        'vip_subnet_cidr_id': 'str',
        'ipv6_vip_virsubnet_id': 'str',
        'provider': 'str',
        'l4_flavor_id': 'str',
        'l7_flavor_id': 'str',
        'guaranteed': 'bool',
        'vpc_id': 'str',
        'availability_zone_list': 'list[str]',
        'enterprise_project_id': 'str',
        'tags': 'list[Tag]',
        'admin_state_up': 'bool',
        'billing_info': 'str',
        'ipv6_bandwidth': 'BandwidthRef',
        'publicip_ids': 'list[str]',
        'publicip': 'CreateLoadBalancerPublicIpOption',
        'elb_virsubnet_ids': 'list[str]',
        'ip_target_enable': 'bool',
        'deletion_protection_enable': 'bool',
        'prepaid_options': 'PrepaidCreateOption',
        'autoscaling': 'CreateLoadbalancerAutoscalingOption',
        'waf_failure_action': 'str'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'name': 'name',
        'description': 'description',
        'vip_address': 'vip_address',
        'vip_subnet_cidr_id': 'vip_subnet_cidr_id',
        'ipv6_vip_virsubnet_id': 'ipv6_vip_virsubnet_id',
        'provider': 'provider',
        'l4_flavor_id': 'l4_flavor_id',
        'l7_flavor_id': 'l7_flavor_id',
        'guaranteed': 'guaranteed',
        'vpc_id': 'vpc_id',
        'availability_zone_list': 'availability_zone_list',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags',
        'admin_state_up': 'admin_state_up',
        'billing_info': 'billing_info',
        'ipv6_bandwidth': 'ipv6_bandwidth',
        'publicip_ids': 'publicip_ids',
        'publicip': 'publicip',
        'elb_virsubnet_ids': 'elb_virsubnet_ids',
        'ip_target_enable': 'ip_target_enable',
        'deletion_protection_enable': 'deletion_protection_enable',
        'prepaid_options': 'prepaid_options',
        'autoscaling': 'autoscaling',
        'waf_failure_action': 'waf_failure_action'
    }

    def __init__(self, id=None, project_id=None, name=None, description=None, vip_address=None, vip_subnet_cidr_id=None, ipv6_vip_virsubnet_id=None, provider=None, l4_flavor_id=None, l7_flavor_id=None, guaranteed=None, vpc_id=None, availability_zone_list=None, enterprise_project_id=None, tags=None, admin_state_up=None, billing_info=None, ipv6_bandwidth=None, publicip_ids=None, publicip=None, elb_virsubnet_ids=None, ip_target_enable=None, deletion_protection_enable=None, prepaid_options=None, autoscaling=None, waf_failure_action=None):
        """CreateLoadBalancerOption

        The model defined in g42cloud sdk

        :param id: The param of the CreateLoadBalancerOption
        :type id: str
        :param project_id: The param of the CreateLoadBalancerOption
        :type project_id: str
        :param name: The param of the CreateLoadBalancerOption
        :type name: str
        :param description: The param of the CreateLoadBalancerOption
        :type description: str
        :param vip_address: The param of the CreateLoadBalancerOption
        :type vip_address: str
        :param vip_subnet_cidr_id: The param of the CreateLoadBalancerOption
        :type vip_subnet_cidr_id: str
        :param ipv6_vip_virsubnet_id: The param of the CreateLoadBalancerOption
        :type ipv6_vip_virsubnet_id: str
        :param provider: The param of the CreateLoadBalancerOption
        :type provider: str
        :param l4_flavor_id: The param of the CreateLoadBalancerOption
        :type l4_flavor_id: str
        :param l7_flavor_id: The param of the CreateLoadBalancerOption
        :type l7_flavor_id: str
        :param guaranteed: The param of the CreateLoadBalancerOption
        :type guaranteed: bool
        :param vpc_id: The param of the CreateLoadBalancerOption
        :type vpc_id: str
        :param availability_zone_list: The param of the CreateLoadBalancerOption
        :type availability_zone_list: list[str]
        :param enterprise_project_id: The param of the CreateLoadBalancerOption
        :type enterprise_project_id: str
        :param tags: The param of the CreateLoadBalancerOption
        :type tags: list[:class:`g42cloudsdkelb.v3.Tag`]
        :param admin_state_up: The param of the CreateLoadBalancerOption
        :type admin_state_up: bool
        :param billing_info: The param of the CreateLoadBalancerOption
        :type billing_info: str
        :param ipv6_bandwidth: The param of the CreateLoadBalancerOption
        :type ipv6_bandwidth: :class:`g42cloudsdkelb.v3.BandwidthRef`
        :param publicip_ids: The param of the CreateLoadBalancerOption
        :type publicip_ids: list[str]
        :param publicip: The param of the CreateLoadBalancerOption
        :type publicip: :class:`g42cloudsdkelb.v3.CreateLoadBalancerPublicIpOption`
        :param elb_virsubnet_ids: The param of the CreateLoadBalancerOption
        :type elb_virsubnet_ids: list[str]
        :param ip_target_enable: The param of the CreateLoadBalancerOption
        :type ip_target_enable: bool
        :param deletion_protection_enable: The param of the CreateLoadBalancerOption
        :type deletion_protection_enable: bool
        :param prepaid_options: The param of the CreateLoadBalancerOption
        :type prepaid_options: :class:`g42cloudsdkelb.v3.PrepaidCreateOption`
        :param autoscaling: The param of the CreateLoadBalancerOption
        :type autoscaling: :class:`g42cloudsdkelb.v3.CreateLoadbalancerAutoscalingOption`
        :param waf_failure_action: The param of the CreateLoadBalancerOption
        :type waf_failure_action: str
        """
        
        

        self._id = None
        self._project_id = None
        self._name = None
        self._description = None
        self._vip_address = None
        self._vip_subnet_cidr_id = None
        self._ipv6_vip_virsubnet_id = None
        self._provider = None
        self._l4_flavor_id = None
        self._l7_flavor_id = None
        self._guaranteed = None
        self._vpc_id = None
        self._availability_zone_list = None
        self._enterprise_project_id = None
        self._tags = None
        self._admin_state_up = None
        self._billing_info = None
        self._ipv6_bandwidth = None
        self._publicip_ids = None
        self._publicip = None
        self._elb_virsubnet_ids = None
        self._ip_target_enable = None
        self._deletion_protection_enable = None
        self._prepaid_options = None
        self._autoscaling = None
        self._waf_failure_action = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if project_id is not None:
            self.project_id = project_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if vip_address is not None:
            self.vip_address = vip_address
        if vip_subnet_cidr_id is not None:
            self.vip_subnet_cidr_id = vip_subnet_cidr_id
        if ipv6_vip_virsubnet_id is not None:
            self.ipv6_vip_virsubnet_id = ipv6_vip_virsubnet_id
        if provider is not None:
            self.provider = provider
        if l4_flavor_id is not None:
            self.l4_flavor_id = l4_flavor_id
        if l7_flavor_id is not None:
            self.l7_flavor_id = l7_flavor_id
        if guaranteed is not None:
            self.guaranteed = guaranteed
        if vpc_id is not None:
            self.vpc_id = vpc_id
        self.availability_zone_list = availability_zone_list
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if billing_info is not None:
            self.billing_info = billing_info
        if ipv6_bandwidth is not None:
            self.ipv6_bandwidth = ipv6_bandwidth
        if publicip_ids is not None:
            self.publicip_ids = publicip_ids
        if publicip is not None:
            self.publicip = publicip
        if elb_virsubnet_ids is not None:
            self.elb_virsubnet_ids = elb_virsubnet_ids
        if ip_target_enable is not None:
            self.ip_target_enable = ip_target_enable
        if deletion_protection_enable is not None:
            self.deletion_protection_enable = deletion_protection_enable
        if prepaid_options is not None:
            self.prepaid_options = prepaid_options
        if autoscaling is not None:
            self.autoscaling = autoscaling
        if waf_failure_action is not None:
            self.waf_failure_action = waf_failure_action

    @property
    def id(self):
        """Gets the id of this CreateLoadBalancerOption.

        :return: The id of this CreateLoadBalancerOption.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateLoadBalancerOption.

        :param id: The id of this CreateLoadBalancerOption.
        :type id: str
        """
        self._id = id

    @property
    def project_id(self):
        """Gets the project_id of this CreateLoadBalancerOption.

        :return: The project_id of this CreateLoadBalancerOption.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreateLoadBalancerOption.

        :param project_id: The project_id of this CreateLoadBalancerOption.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def name(self):
        """Gets the name of this CreateLoadBalancerOption.

        :return: The name of this CreateLoadBalancerOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateLoadBalancerOption.

        :param name: The name of this CreateLoadBalancerOption.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateLoadBalancerOption.

        :return: The description of this CreateLoadBalancerOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateLoadBalancerOption.

        :param description: The description of this CreateLoadBalancerOption.
        :type description: str
        """
        self._description = description

    @property
    def vip_address(self):
        """Gets the vip_address of this CreateLoadBalancerOption.

        :return: The vip_address of this CreateLoadBalancerOption.
        :rtype: str
        """
        return self._vip_address

    @vip_address.setter
    def vip_address(self, vip_address):
        """Sets the vip_address of this CreateLoadBalancerOption.

        :param vip_address: The vip_address of this CreateLoadBalancerOption.
        :type vip_address: str
        """
        self._vip_address = vip_address

    @property
    def vip_subnet_cidr_id(self):
        """Gets the vip_subnet_cidr_id of this CreateLoadBalancerOption.

        :return: The vip_subnet_cidr_id of this CreateLoadBalancerOption.
        :rtype: str
        """
        return self._vip_subnet_cidr_id

    @vip_subnet_cidr_id.setter
    def vip_subnet_cidr_id(self, vip_subnet_cidr_id):
        """Sets the vip_subnet_cidr_id of this CreateLoadBalancerOption.

        :param vip_subnet_cidr_id: The vip_subnet_cidr_id of this CreateLoadBalancerOption.
        :type vip_subnet_cidr_id: str
        """
        self._vip_subnet_cidr_id = vip_subnet_cidr_id

    @property
    def ipv6_vip_virsubnet_id(self):
        """Gets the ipv6_vip_virsubnet_id of this CreateLoadBalancerOption.

        :return: The ipv6_vip_virsubnet_id of this CreateLoadBalancerOption.
        :rtype: str
        """
        return self._ipv6_vip_virsubnet_id

    @ipv6_vip_virsubnet_id.setter
    def ipv6_vip_virsubnet_id(self, ipv6_vip_virsubnet_id):
        """Sets the ipv6_vip_virsubnet_id of this CreateLoadBalancerOption.

        :param ipv6_vip_virsubnet_id: The ipv6_vip_virsubnet_id of this CreateLoadBalancerOption.
        :type ipv6_vip_virsubnet_id: str
        """
        self._ipv6_vip_virsubnet_id = ipv6_vip_virsubnet_id

    @property
    def provider(self):
        """Gets the provider of this CreateLoadBalancerOption.

        :return: The provider of this CreateLoadBalancerOption.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this CreateLoadBalancerOption.

        :param provider: The provider of this CreateLoadBalancerOption.
        :type provider: str
        """
        self._provider = provider

    @property
    def l4_flavor_id(self):
        """Gets the l4_flavor_id of this CreateLoadBalancerOption.

        :return: The l4_flavor_id of this CreateLoadBalancerOption.
        :rtype: str
        """
        return self._l4_flavor_id

    @l4_flavor_id.setter
    def l4_flavor_id(self, l4_flavor_id):
        """Sets the l4_flavor_id of this CreateLoadBalancerOption.

        :param l4_flavor_id: The l4_flavor_id of this CreateLoadBalancerOption.
        :type l4_flavor_id: str
        """
        self._l4_flavor_id = l4_flavor_id

    @property
    def l7_flavor_id(self):
        """Gets the l7_flavor_id of this CreateLoadBalancerOption.

        :return: The l7_flavor_id of this CreateLoadBalancerOption.
        :rtype: str
        """
        return self._l7_flavor_id

    @l7_flavor_id.setter
    def l7_flavor_id(self, l7_flavor_id):
        """Sets the l7_flavor_id of this CreateLoadBalancerOption.

        :param l7_flavor_id: The l7_flavor_id of this CreateLoadBalancerOption.
        :type l7_flavor_id: str
        """
        self._l7_flavor_id = l7_flavor_id

    @property
    def guaranteed(self):
        """Gets the guaranteed of this CreateLoadBalancerOption.

        :return: The guaranteed of this CreateLoadBalancerOption.
        :rtype: bool
        """
        return self._guaranteed

    @guaranteed.setter
    def guaranteed(self, guaranteed):
        """Sets the guaranteed of this CreateLoadBalancerOption.

        :param guaranteed: The guaranteed of this CreateLoadBalancerOption.
        :type guaranteed: bool
        """
        self._guaranteed = guaranteed

    @property
    def vpc_id(self):
        """Gets the vpc_id of this CreateLoadBalancerOption.

        :return: The vpc_id of this CreateLoadBalancerOption.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this CreateLoadBalancerOption.

        :param vpc_id: The vpc_id of this CreateLoadBalancerOption.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def availability_zone_list(self):
        """Gets the availability_zone_list of this CreateLoadBalancerOption.

        :return: The availability_zone_list of this CreateLoadBalancerOption.
        :rtype: list[str]
        """
        return self._availability_zone_list

    @availability_zone_list.setter
    def availability_zone_list(self, availability_zone_list):
        """Sets the availability_zone_list of this CreateLoadBalancerOption.

        :param availability_zone_list: The availability_zone_list of this CreateLoadBalancerOption.
        :type availability_zone_list: list[str]
        """
        self._availability_zone_list = availability_zone_list

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateLoadBalancerOption.

        :return: The enterprise_project_id of this CreateLoadBalancerOption.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateLoadBalancerOption.

        :param enterprise_project_id: The enterprise_project_id of this CreateLoadBalancerOption.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        """Gets the tags of this CreateLoadBalancerOption.

        :return: The tags of this CreateLoadBalancerOption.
        :rtype: list[:class:`g42cloudsdkelb.v3.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateLoadBalancerOption.

        :param tags: The tags of this CreateLoadBalancerOption.
        :type tags: list[:class:`g42cloudsdkelb.v3.Tag`]
        """
        self._tags = tags

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this CreateLoadBalancerOption.

        :return: The admin_state_up of this CreateLoadBalancerOption.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this CreateLoadBalancerOption.

        :param admin_state_up: The admin_state_up of this CreateLoadBalancerOption.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def billing_info(self):
        """Gets the billing_info of this CreateLoadBalancerOption.

        :return: The billing_info of this CreateLoadBalancerOption.
        :rtype: str
        """
        return self._billing_info

    @billing_info.setter
    def billing_info(self, billing_info):
        """Sets the billing_info of this CreateLoadBalancerOption.

        :param billing_info: The billing_info of this CreateLoadBalancerOption.
        :type billing_info: str
        """
        self._billing_info = billing_info

    @property
    def ipv6_bandwidth(self):
        """Gets the ipv6_bandwidth of this CreateLoadBalancerOption.

        :return: The ipv6_bandwidth of this CreateLoadBalancerOption.
        :rtype: :class:`g42cloudsdkelb.v3.BandwidthRef`
        """
        return self._ipv6_bandwidth

    @ipv6_bandwidth.setter
    def ipv6_bandwidth(self, ipv6_bandwidth):
        """Sets the ipv6_bandwidth of this CreateLoadBalancerOption.

        :param ipv6_bandwidth: The ipv6_bandwidth of this CreateLoadBalancerOption.
        :type ipv6_bandwidth: :class:`g42cloudsdkelb.v3.BandwidthRef`
        """
        self._ipv6_bandwidth = ipv6_bandwidth

    @property
    def publicip_ids(self):
        """Gets the publicip_ids of this CreateLoadBalancerOption.

        :return: The publicip_ids of this CreateLoadBalancerOption.
        :rtype: list[str]
        """
        return self._publicip_ids

    @publicip_ids.setter
    def publicip_ids(self, publicip_ids):
        """Sets the publicip_ids of this CreateLoadBalancerOption.

        :param publicip_ids: The publicip_ids of this CreateLoadBalancerOption.
        :type publicip_ids: list[str]
        """
        self._publicip_ids = publicip_ids

    @property
    def publicip(self):
        """Gets the publicip of this CreateLoadBalancerOption.

        :return: The publicip of this CreateLoadBalancerOption.
        :rtype: :class:`g42cloudsdkelb.v3.CreateLoadBalancerPublicIpOption`
        """
        return self._publicip

    @publicip.setter
    def publicip(self, publicip):
        """Sets the publicip of this CreateLoadBalancerOption.

        :param publicip: The publicip of this CreateLoadBalancerOption.
        :type publicip: :class:`g42cloudsdkelb.v3.CreateLoadBalancerPublicIpOption`
        """
        self._publicip = publicip

    @property
    def elb_virsubnet_ids(self):
        """Gets the elb_virsubnet_ids of this CreateLoadBalancerOption.

        :return: The elb_virsubnet_ids of this CreateLoadBalancerOption.
        :rtype: list[str]
        """
        return self._elb_virsubnet_ids

    @elb_virsubnet_ids.setter
    def elb_virsubnet_ids(self, elb_virsubnet_ids):
        """Sets the elb_virsubnet_ids of this CreateLoadBalancerOption.

        :param elb_virsubnet_ids: The elb_virsubnet_ids of this CreateLoadBalancerOption.
        :type elb_virsubnet_ids: list[str]
        """
        self._elb_virsubnet_ids = elb_virsubnet_ids

    @property
    def ip_target_enable(self):
        """Gets the ip_target_enable of this CreateLoadBalancerOption.

        :return: The ip_target_enable of this CreateLoadBalancerOption.
        :rtype: bool
        """
        return self._ip_target_enable

    @ip_target_enable.setter
    def ip_target_enable(self, ip_target_enable):
        """Sets the ip_target_enable of this CreateLoadBalancerOption.

        :param ip_target_enable: The ip_target_enable of this CreateLoadBalancerOption.
        :type ip_target_enable: bool
        """
        self._ip_target_enable = ip_target_enable

    @property
    def deletion_protection_enable(self):
        """Gets the deletion_protection_enable of this CreateLoadBalancerOption.

        :return: The deletion_protection_enable of this CreateLoadBalancerOption.
        :rtype: bool
        """
        return self._deletion_protection_enable

    @deletion_protection_enable.setter
    def deletion_protection_enable(self, deletion_protection_enable):
        """Sets the deletion_protection_enable of this CreateLoadBalancerOption.

        :param deletion_protection_enable: The deletion_protection_enable of this CreateLoadBalancerOption.
        :type deletion_protection_enable: bool
        """
        self._deletion_protection_enable = deletion_protection_enable

    @property
    def prepaid_options(self):
        """Gets the prepaid_options of this CreateLoadBalancerOption.

        :return: The prepaid_options of this CreateLoadBalancerOption.
        :rtype: :class:`g42cloudsdkelb.v3.PrepaidCreateOption`
        """
        return self._prepaid_options

    @prepaid_options.setter
    def prepaid_options(self, prepaid_options):
        """Sets the prepaid_options of this CreateLoadBalancerOption.

        :param prepaid_options: The prepaid_options of this CreateLoadBalancerOption.
        :type prepaid_options: :class:`g42cloudsdkelb.v3.PrepaidCreateOption`
        """
        self._prepaid_options = prepaid_options

    @property
    def autoscaling(self):
        """Gets the autoscaling of this CreateLoadBalancerOption.

        :return: The autoscaling of this CreateLoadBalancerOption.
        :rtype: :class:`g42cloudsdkelb.v3.CreateLoadbalancerAutoscalingOption`
        """
        return self._autoscaling

    @autoscaling.setter
    def autoscaling(self, autoscaling):
        """Sets the autoscaling of this CreateLoadBalancerOption.

        :param autoscaling: The autoscaling of this CreateLoadBalancerOption.
        :type autoscaling: :class:`g42cloudsdkelb.v3.CreateLoadbalancerAutoscalingOption`
        """
        self._autoscaling = autoscaling

    @property
    def waf_failure_action(self):
        """Gets the waf_failure_action of this CreateLoadBalancerOption.

        :return: The waf_failure_action of this CreateLoadBalancerOption.
        :rtype: str
        """
        return self._waf_failure_action

    @waf_failure_action.setter
    def waf_failure_action(self, waf_failure_action):
        """Sets the waf_failure_action of this CreateLoadBalancerOption.

        :param waf_failure_action: The waf_failure_action of this CreateLoadBalancerOption.
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
        if not isinstance(other, CreateLoadBalancerOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
