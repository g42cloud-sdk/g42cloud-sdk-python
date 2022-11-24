# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category': 'str',
        'type': 'str',
        'flavor': 'str',
        'version': 'str',
        'platform_version': 'str',
        'description': 'str',
        'custom_san': 'list[str]',
        'ipv6enable': 'bool',
        'host_network': 'HostNetwork',
        'container_network': 'ContainerNetwork',
        'eni_network': 'EniNetwork',
        'authentication': 'Authentication',
        'billing_mode': 'int',
        'masters': 'list[MasterSpec]',
        'kubernetes_svc_ip_range': 'str',
        'cluster_tags': 'list[ResourceTag]',
        'kube_proxy_mode': 'str',
        'az': 'str',
        'extend_param': 'ClusterExtendParam',
        'support_istio': 'bool'
    }

    attribute_map = {
        'category': 'category',
        'type': 'type',
        'flavor': 'flavor',
        'version': 'version',
        'platform_version': 'platformVersion',
        'description': 'description',
        'custom_san': 'customSan',
        'ipv6enable': 'ipv6enable',
        'host_network': 'hostNetwork',
        'container_network': 'containerNetwork',
        'eni_network': 'eniNetwork',
        'authentication': 'authentication',
        'billing_mode': 'billingMode',
        'masters': 'masters',
        'kubernetes_svc_ip_range': 'kubernetesSvcIpRange',
        'cluster_tags': 'clusterTags',
        'kube_proxy_mode': 'kubeProxyMode',
        'az': 'az',
        'extend_param': 'extendParam',
        'support_istio': 'supportIstio'
    }

    def __init__(self, category=None, type=None, flavor=None, version=None, platform_version=None, description=None, custom_san=None, ipv6enable=None, host_network=None, container_network=None, eni_network=None, authentication=None, billing_mode=None, masters=None, kubernetes_svc_ip_range=None, cluster_tags=None, kube_proxy_mode=None, az=None, extend_param=None, support_istio=None):
        """ClusterSpec

        The model defined in g42cloud sdk

        :param category: The param of the ClusterSpec
        :type category: str
        :param type: The param of the ClusterSpec
        :type type: str
        :param flavor: The param of the ClusterSpec
        :type flavor: str
        :param version: The param of the ClusterSpec
        :type version: str
        :param platform_version: The param of the ClusterSpec
        :type platform_version: str
        :param description: The param of the ClusterSpec
        :type description: str
        :param custom_san: The param of the ClusterSpec
        :type custom_san: list[str]
        :param ipv6enable: The param of the ClusterSpec
        :type ipv6enable: bool
        :param host_network: The param of the ClusterSpec
        :type host_network: :class:`g42cloudsdkcce.v3.HostNetwork`
        :param container_network: The param of the ClusterSpec
        :type container_network: :class:`g42cloudsdkcce.v3.ContainerNetwork`
        :param eni_network: The param of the ClusterSpec
        :type eni_network: :class:`g42cloudsdkcce.v3.EniNetwork`
        :param authentication: The param of the ClusterSpec
        :type authentication: :class:`g42cloudsdkcce.v3.Authentication`
        :param billing_mode: The param of the ClusterSpec
        :type billing_mode: int
        :param masters: The param of the ClusterSpec
        :type masters: list[:class:`g42cloudsdkcce.v3.MasterSpec`]
        :param kubernetes_svc_ip_range: The param of the ClusterSpec
        :type kubernetes_svc_ip_range: str
        :param cluster_tags: The param of the ClusterSpec
        :type cluster_tags: list[:class:`g42cloudsdkcce.v3.ResourceTag`]
        :param kube_proxy_mode: The param of the ClusterSpec
        :type kube_proxy_mode: str
        :param az: The param of the ClusterSpec
        :type az: str
        :param extend_param: The param of the ClusterSpec
        :type extend_param: :class:`g42cloudsdkcce.v3.ClusterExtendParam`
        :param support_istio: The param of the ClusterSpec
        :type support_istio: bool
        """
        
        

        self._category = None
        self._type = None
        self._flavor = None
        self._version = None
        self._platform_version = None
        self._description = None
        self._custom_san = None
        self._ipv6enable = None
        self._host_network = None
        self._container_network = None
        self._eni_network = None
        self._authentication = None
        self._billing_mode = None
        self._masters = None
        self._kubernetes_svc_ip_range = None
        self._cluster_tags = None
        self._kube_proxy_mode = None
        self._az = None
        self._extend_param = None
        self._support_istio = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if type is not None:
            self.type = type
        self.flavor = flavor
        if version is not None:
            self.version = version
        if platform_version is not None:
            self.platform_version = platform_version
        if description is not None:
            self.description = description
        if custom_san is not None:
            self.custom_san = custom_san
        if ipv6enable is not None:
            self.ipv6enable = ipv6enable
        self.host_network = host_network
        self.container_network = container_network
        if eni_network is not None:
            self.eni_network = eni_network
        if authentication is not None:
            self.authentication = authentication
        if billing_mode is not None:
            self.billing_mode = billing_mode
        if masters is not None:
            self.masters = masters
        if kubernetes_svc_ip_range is not None:
            self.kubernetes_svc_ip_range = kubernetes_svc_ip_range
        if cluster_tags is not None:
            self.cluster_tags = cluster_tags
        if kube_proxy_mode is not None:
            self.kube_proxy_mode = kube_proxy_mode
        if az is not None:
            self.az = az
        if extend_param is not None:
            self.extend_param = extend_param
        if support_istio is not None:
            self.support_istio = support_istio

    @property
    def category(self):
        """Gets the category of this ClusterSpec.

        :return: The category of this ClusterSpec.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ClusterSpec.

        :param category: The category of this ClusterSpec.
        :type category: str
        """
        self._category = category

    @property
    def type(self):
        """Gets the type of this ClusterSpec.

        :return: The type of this ClusterSpec.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ClusterSpec.

        :param type: The type of this ClusterSpec.
        :type type: str
        """
        self._type = type

    @property
    def flavor(self):
        """Gets the flavor of this ClusterSpec.

        :return: The flavor of this ClusterSpec.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this ClusterSpec.

        :param flavor: The flavor of this ClusterSpec.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def version(self):
        """Gets the version of this ClusterSpec.

        :return: The version of this ClusterSpec.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ClusterSpec.

        :param version: The version of this ClusterSpec.
        :type version: str
        """
        self._version = version

    @property
    def platform_version(self):
        """Gets the platform_version of this ClusterSpec.

        :return: The platform_version of this ClusterSpec.
        :rtype: str
        """
        return self._platform_version

    @platform_version.setter
    def platform_version(self, platform_version):
        """Sets the platform_version of this ClusterSpec.

        :param platform_version: The platform_version of this ClusterSpec.
        :type platform_version: str
        """
        self._platform_version = platform_version

    @property
    def description(self):
        """Gets the description of this ClusterSpec.

        :return: The description of this ClusterSpec.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ClusterSpec.

        :param description: The description of this ClusterSpec.
        :type description: str
        """
        self._description = description

    @property
    def custom_san(self):
        """Gets the custom_san of this ClusterSpec.

        :return: The custom_san of this ClusterSpec.
        :rtype: list[str]
        """
        return self._custom_san

    @custom_san.setter
    def custom_san(self, custom_san):
        """Sets the custom_san of this ClusterSpec.

        :param custom_san: The custom_san of this ClusterSpec.
        :type custom_san: list[str]
        """
        self._custom_san = custom_san

    @property
    def ipv6enable(self):
        """Gets the ipv6enable of this ClusterSpec.

        :return: The ipv6enable of this ClusterSpec.
        :rtype: bool
        """
        return self._ipv6enable

    @ipv6enable.setter
    def ipv6enable(self, ipv6enable):
        """Sets the ipv6enable of this ClusterSpec.

        :param ipv6enable: The ipv6enable of this ClusterSpec.
        :type ipv6enable: bool
        """
        self._ipv6enable = ipv6enable

    @property
    def host_network(self):
        """Gets the host_network of this ClusterSpec.

        :return: The host_network of this ClusterSpec.
        :rtype: :class:`g42cloudsdkcce.v3.HostNetwork`
        """
        return self._host_network

    @host_network.setter
    def host_network(self, host_network):
        """Sets the host_network of this ClusterSpec.

        :param host_network: The host_network of this ClusterSpec.
        :type host_network: :class:`g42cloudsdkcce.v3.HostNetwork`
        """
        self._host_network = host_network

    @property
    def container_network(self):
        """Gets the container_network of this ClusterSpec.

        :return: The container_network of this ClusterSpec.
        :rtype: :class:`g42cloudsdkcce.v3.ContainerNetwork`
        """
        return self._container_network

    @container_network.setter
    def container_network(self, container_network):
        """Sets the container_network of this ClusterSpec.

        :param container_network: The container_network of this ClusterSpec.
        :type container_network: :class:`g42cloudsdkcce.v3.ContainerNetwork`
        """
        self._container_network = container_network

    @property
    def eni_network(self):
        """Gets the eni_network of this ClusterSpec.

        :return: The eni_network of this ClusterSpec.
        :rtype: :class:`g42cloudsdkcce.v3.EniNetwork`
        """
        return self._eni_network

    @eni_network.setter
    def eni_network(self, eni_network):
        """Sets the eni_network of this ClusterSpec.

        :param eni_network: The eni_network of this ClusterSpec.
        :type eni_network: :class:`g42cloudsdkcce.v3.EniNetwork`
        """
        self._eni_network = eni_network

    @property
    def authentication(self):
        """Gets the authentication of this ClusterSpec.

        :return: The authentication of this ClusterSpec.
        :rtype: :class:`g42cloudsdkcce.v3.Authentication`
        """
        return self._authentication

    @authentication.setter
    def authentication(self, authentication):
        """Sets the authentication of this ClusterSpec.

        :param authentication: The authentication of this ClusterSpec.
        :type authentication: :class:`g42cloudsdkcce.v3.Authentication`
        """
        self._authentication = authentication

    @property
    def billing_mode(self):
        """Gets the billing_mode of this ClusterSpec.

        :return: The billing_mode of this ClusterSpec.
        :rtype: int
        """
        return self._billing_mode

    @billing_mode.setter
    def billing_mode(self, billing_mode):
        """Sets the billing_mode of this ClusterSpec.

        :param billing_mode: The billing_mode of this ClusterSpec.
        :type billing_mode: int
        """
        self._billing_mode = billing_mode

    @property
    def masters(self):
        """Gets the masters of this ClusterSpec.

        :return: The masters of this ClusterSpec.
        :rtype: list[:class:`g42cloudsdkcce.v3.MasterSpec`]
        """
        return self._masters

    @masters.setter
    def masters(self, masters):
        """Sets the masters of this ClusterSpec.

        :param masters: The masters of this ClusterSpec.
        :type masters: list[:class:`g42cloudsdkcce.v3.MasterSpec`]
        """
        self._masters = masters

    @property
    def kubernetes_svc_ip_range(self):
        """Gets the kubernetes_svc_ip_range of this ClusterSpec.

        :return: The kubernetes_svc_ip_range of this ClusterSpec.
        :rtype: str
        """
        return self._kubernetes_svc_ip_range

    @kubernetes_svc_ip_range.setter
    def kubernetes_svc_ip_range(self, kubernetes_svc_ip_range):
        """Sets the kubernetes_svc_ip_range of this ClusterSpec.

        :param kubernetes_svc_ip_range: The kubernetes_svc_ip_range of this ClusterSpec.
        :type kubernetes_svc_ip_range: str
        """
        self._kubernetes_svc_ip_range = kubernetes_svc_ip_range

    @property
    def cluster_tags(self):
        """Gets the cluster_tags of this ClusterSpec.

        :return: The cluster_tags of this ClusterSpec.
        :rtype: list[:class:`g42cloudsdkcce.v3.ResourceTag`]
        """
        return self._cluster_tags

    @cluster_tags.setter
    def cluster_tags(self, cluster_tags):
        """Sets the cluster_tags of this ClusterSpec.

        :param cluster_tags: The cluster_tags of this ClusterSpec.
        :type cluster_tags: list[:class:`g42cloudsdkcce.v3.ResourceTag`]
        """
        self._cluster_tags = cluster_tags

    @property
    def kube_proxy_mode(self):
        """Gets the kube_proxy_mode of this ClusterSpec.

        :return: The kube_proxy_mode of this ClusterSpec.
        :rtype: str
        """
        return self._kube_proxy_mode

    @kube_proxy_mode.setter
    def kube_proxy_mode(self, kube_proxy_mode):
        """Sets the kube_proxy_mode of this ClusterSpec.

        :param kube_proxy_mode: The kube_proxy_mode of this ClusterSpec.
        :type kube_proxy_mode: str
        """
        self._kube_proxy_mode = kube_proxy_mode

    @property
    def az(self):
        """Gets the az of this ClusterSpec.

        :return: The az of this ClusterSpec.
        :rtype: str
        """
        return self._az

    @az.setter
    def az(self, az):
        """Sets the az of this ClusterSpec.

        :param az: The az of this ClusterSpec.
        :type az: str
        """
        self._az = az

    @property
    def extend_param(self):
        """Gets the extend_param of this ClusterSpec.

        :return: The extend_param of this ClusterSpec.
        :rtype: :class:`g42cloudsdkcce.v3.ClusterExtendParam`
        """
        return self._extend_param

    @extend_param.setter
    def extend_param(self, extend_param):
        """Sets the extend_param of this ClusterSpec.

        :param extend_param: The extend_param of this ClusterSpec.
        :type extend_param: :class:`g42cloudsdkcce.v3.ClusterExtendParam`
        """
        self._extend_param = extend_param

    @property
    def support_istio(self):
        """Gets the support_istio of this ClusterSpec.

        :return: The support_istio of this ClusterSpec.
        :rtype: bool
        """
        return self._support_istio

    @support_istio.setter
    def support_istio(self, support_istio):
        """Sets the support_istio of this ClusterSpec.

        :param support_istio: The support_istio of this ClusterSpec.
        :type support_istio: bool
        """
        self._support_istio = support_istio

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
        if not isinstance(other, ClusterSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
