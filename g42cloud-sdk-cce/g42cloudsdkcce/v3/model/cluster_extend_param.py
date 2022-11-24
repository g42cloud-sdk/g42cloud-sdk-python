# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterExtendParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_az': 'str',
        'dss_master_volumes': 'str',
        'enterprise_project_id': 'str',
        'kube_proxy_mode': 'str',
        'cluster_external_ip': 'str',
        'alpha_cce_fix_pool_mask': 'str',
        'dec_master_flavor': 'str',
        'docker_umask_mode': 'str',
        'kubernetes_io_cpu_manager_policy': 'str',
        'order_id': 'str',
        'period_type': 'str',
        'period_num': 'int',
        'is_auto_renew': 'str',
        'is_auto_pay': 'str',
        'upgradefrom': 'str'
    }

    attribute_map = {
        'cluster_az': 'clusterAZ',
        'dss_master_volumes': 'dssMasterVolumes',
        'enterprise_project_id': 'enterpriseProjectId',
        'kube_proxy_mode': 'kubeProxyMode',
        'cluster_external_ip': 'clusterExternalIP',
        'alpha_cce_fix_pool_mask': 'alpha.cce/fixPoolMask',
        'dec_master_flavor': 'decMasterFlavor',
        'docker_umask_mode': 'dockerUmaskMode',
        'kubernetes_io_cpu_manager_policy': 'kubernetes.io/cpuManagerPolicy',
        'order_id': 'orderID',
        'period_type': 'periodType',
        'period_num': 'periodNum',
        'is_auto_renew': 'isAutoRenew',
        'is_auto_pay': 'isAutoPay',
        'upgradefrom': 'upgradefrom'
    }

    def __init__(self, cluster_az=None, dss_master_volumes=None, enterprise_project_id=None, kube_proxy_mode=None, cluster_external_ip=None, alpha_cce_fix_pool_mask=None, dec_master_flavor=None, docker_umask_mode=None, kubernetes_io_cpu_manager_policy=None, order_id=None, period_type=None, period_num=None, is_auto_renew=None, is_auto_pay=None, upgradefrom=None):
        """ClusterExtendParam

        The model defined in g42cloud sdk

        :param cluster_az: The param of the ClusterExtendParam
        :type cluster_az: str
        :param dss_master_volumes: The param of the ClusterExtendParam
        :type dss_master_volumes: str
        :param enterprise_project_id: The param of the ClusterExtendParam
        :type enterprise_project_id: str
        :param kube_proxy_mode: The param of the ClusterExtendParam
        :type kube_proxy_mode: str
        :param cluster_external_ip: The param of the ClusterExtendParam
        :type cluster_external_ip: str
        :param alpha_cce_fix_pool_mask: The param of the ClusterExtendParam
        :type alpha_cce_fix_pool_mask: str
        :param dec_master_flavor: The param of the ClusterExtendParam
        :type dec_master_flavor: str
        :param docker_umask_mode: The param of the ClusterExtendParam
        :type docker_umask_mode: str
        :param kubernetes_io_cpu_manager_policy: The param of the ClusterExtendParam
        :type kubernetes_io_cpu_manager_policy: str
        :param order_id: The param of the ClusterExtendParam
        :type order_id: str
        :param period_type: The param of the ClusterExtendParam
        :type period_type: str
        :param period_num: The param of the ClusterExtendParam
        :type period_num: int
        :param is_auto_renew: The param of the ClusterExtendParam
        :type is_auto_renew: str
        :param is_auto_pay: The param of the ClusterExtendParam
        :type is_auto_pay: str
        :param upgradefrom: The param of the ClusterExtendParam
        :type upgradefrom: str
        """
        
        

        self._cluster_az = None
        self._dss_master_volumes = None
        self._enterprise_project_id = None
        self._kube_proxy_mode = None
        self._cluster_external_ip = None
        self._alpha_cce_fix_pool_mask = None
        self._dec_master_flavor = None
        self._docker_umask_mode = None
        self._kubernetes_io_cpu_manager_policy = None
        self._order_id = None
        self._period_type = None
        self._period_num = None
        self._is_auto_renew = None
        self._is_auto_pay = None
        self._upgradefrom = None
        self.discriminator = None

        if cluster_az is not None:
            self.cluster_az = cluster_az
        if dss_master_volumes is not None:
            self.dss_master_volumes = dss_master_volumes
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if kube_proxy_mode is not None:
            self.kube_proxy_mode = kube_proxy_mode
        if cluster_external_ip is not None:
            self.cluster_external_ip = cluster_external_ip
        if alpha_cce_fix_pool_mask is not None:
            self.alpha_cce_fix_pool_mask = alpha_cce_fix_pool_mask
        if dec_master_flavor is not None:
            self.dec_master_flavor = dec_master_flavor
        if docker_umask_mode is not None:
            self.docker_umask_mode = docker_umask_mode
        if kubernetes_io_cpu_manager_policy is not None:
            self.kubernetes_io_cpu_manager_policy = kubernetes_io_cpu_manager_policy
        if order_id is not None:
            self.order_id = order_id
        if period_type is not None:
            self.period_type = period_type
        if period_num is not None:
            self.period_num = period_num
        if is_auto_renew is not None:
            self.is_auto_renew = is_auto_renew
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay
        if upgradefrom is not None:
            self.upgradefrom = upgradefrom

    @property
    def cluster_az(self):
        """Gets the cluster_az of this ClusterExtendParam.

        :return: The cluster_az of this ClusterExtendParam.
        :rtype: str
        """
        return self._cluster_az

    @cluster_az.setter
    def cluster_az(self, cluster_az):
        """Sets the cluster_az of this ClusterExtendParam.

        :param cluster_az: The cluster_az of this ClusterExtendParam.
        :type cluster_az: str
        """
        self._cluster_az = cluster_az

    @property
    def dss_master_volumes(self):
        """Gets the dss_master_volumes of this ClusterExtendParam.

        :return: The dss_master_volumes of this ClusterExtendParam.
        :rtype: str
        """
        return self._dss_master_volumes

    @dss_master_volumes.setter
    def dss_master_volumes(self, dss_master_volumes):
        """Sets the dss_master_volumes of this ClusterExtendParam.

        :param dss_master_volumes: The dss_master_volumes of this ClusterExtendParam.
        :type dss_master_volumes: str
        """
        self._dss_master_volumes = dss_master_volumes

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ClusterExtendParam.

        :return: The enterprise_project_id of this ClusterExtendParam.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ClusterExtendParam.

        :param enterprise_project_id: The enterprise_project_id of this ClusterExtendParam.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def kube_proxy_mode(self):
        """Gets the kube_proxy_mode of this ClusterExtendParam.

        :return: The kube_proxy_mode of this ClusterExtendParam.
        :rtype: str
        """
        return self._kube_proxy_mode

    @kube_proxy_mode.setter
    def kube_proxy_mode(self, kube_proxy_mode):
        """Sets the kube_proxy_mode of this ClusterExtendParam.

        :param kube_proxy_mode: The kube_proxy_mode of this ClusterExtendParam.
        :type kube_proxy_mode: str
        """
        self._kube_proxy_mode = kube_proxy_mode

    @property
    def cluster_external_ip(self):
        """Gets the cluster_external_ip of this ClusterExtendParam.

        :return: The cluster_external_ip of this ClusterExtendParam.
        :rtype: str
        """
        return self._cluster_external_ip

    @cluster_external_ip.setter
    def cluster_external_ip(self, cluster_external_ip):
        """Sets the cluster_external_ip of this ClusterExtendParam.

        :param cluster_external_ip: The cluster_external_ip of this ClusterExtendParam.
        :type cluster_external_ip: str
        """
        self._cluster_external_ip = cluster_external_ip

    @property
    def alpha_cce_fix_pool_mask(self):
        """Gets the alpha_cce_fix_pool_mask of this ClusterExtendParam.

        :return: The alpha_cce_fix_pool_mask of this ClusterExtendParam.
        :rtype: str
        """
        return self._alpha_cce_fix_pool_mask

    @alpha_cce_fix_pool_mask.setter
    def alpha_cce_fix_pool_mask(self, alpha_cce_fix_pool_mask):
        """Sets the alpha_cce_fix_pool_mask of this ClusterExtendParam.

        :param alpha_cce_fix_pool_mask: The alpha_cce_fix_pool_mask of this ClusterExtendParam.
        :type alpha_cce_fix_pool_mask: str
        """
        self._alpha_cce_fix_pool_mask = alpha_cce_fix_pool_mask

    @property
    def dec_master_flavor(self):
        """Gets the dec_master_flavor of this ClusterExtendParam.

        :return: The dec_master_flavor of this ClusterExtendParam.
        :rtype: str
        """
        return self._dec_master_flavor

    @dec_master_flavor.setter
    def dec_master_flavor(self, dec_master_flavor):
        """Sets the dec_master_flavor of this ClusterExtendParam.

        :param dec_master_flavor: The dec_master_flavor of this ClusterExtendParam.
        :type dec_master_flavor: str
        """
        self._dec_master_flavor = dec_master_flavor

    @property
    def docker_umask_mode(self):
        """Gets the docker_umask_mode of this ClusterExtendParam.

        :return: The docker_umask_mode of this ClusterExtendParam.
        :rtype: str
        """
        return self._docker_umask_mode

    @docker_umask_mode.setter
    def docker_umask_mode(self, docker_umask_mode):
        """Sets the docker_umask_mode of this ClusterExtendParam.

        :param docker_umask_mode: The docker_umask_mode of this ClusterExtendParam.
        :type docker_umask_mode: str
        """
        self._docker_umask_mode = docker_umask_mode

    @property
    def kubernetes_io_cpu_manager_policy(self):
        """Gets the kubernetes_io_cpu_manager_policy of this ClusterExtendParam.

        :return: The kubernetes_io_cpu_manager_policy of this ClusterExtendParam.
        :rtype: str
        """
        return self._kubernetes_io_cpu_manager_policy

    @kubernetes_io_cpu_manager_policy.setter
    def kubernetes_io_cpu_manager_policy(self, kubernetes_io_cpu_manager_policy):
        """Sets the kubernetes_io_cpu_manager_policy of this ClusterExtendParam.

        :param kubernetes_io_cpu_manager_policy: The kubernetes_io_cpu_manager_policy of this ClusterExtendParam.
        :type kubernetes_io_cpu_manager_policy: str
        """
        self._kubernetes_io_cpu_manager_policy = kubernetes_io_cpu_manager_policy

    @property
    def order_id(self):
        """Gets the order_id of this ClusterExtendParam.

        :return: The order_id of this ClusterExtendParam.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this ClusterExtendParam.

        :param order_id: The order_id of this ClusterExtendParam.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def period_type(self):
        """Gets the period_type of this ClusterExtendParam.

        :return: The period_type of this ClusterExtendParam.
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        """Sets the period_type of this ClusterExtendParam.

        :param period_type: The period_type of this ClusterExtendParam.
        :type period_type: str
        """
        self._period_type = period_type

    @property
    def period_num(self):
        """Gets the period_num of this ClusterExtendParam.

        :return: The period_num of this ClusterExtendParam.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        """Sets the period_num of this ClusterExtendParam.

        :param period_num: The period_num of this ClusterExtendParam.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def is_auto_renew(self):
        """Gets the is_auto_renew of this ClusterExtendParam.

        :return: The is_auto_renew of this ClusterExtendParam.
        :rtype: str
        """
        return self._is_auto_renew

    @is_auto_renew.setter
    def is_auto_renew(self, is_auto_renew):
        """Sets the is_auto_renew of this ClusterExtendParam.

        :param is_auto_renew: The is_auto_renew of this ClusterExtendParam.
        :type is_auto_renew: str
        """
        self._is_auto_renew = is_auto_renew

    @property
    def is_auto_pay(self):
        """Gets the is_auto_pay of this ClusterExtendParam.

        :return: The is_auto_pay of this ClusterExtendParam.
        :rtype: str
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        """Sets the is_auto_pay of this ClusterExtendParam.

        :param is_auto_pay: The is_auto_pay of this ClusterExtendParam.
        :type is_auto_pay: str
        """
        self._is_auto_pay = is_auto_pay

    @property
    def upgradefrom(self):
        """Gets the upgradefrom of this ClusterExtendParam.

        :return: The upgradefrom of this ClusterExtendParam.
        :rtype: str
        """
        return self._upgradefrom

    @upgradefrom.setter
    def upgradefrom(self, upgradefrom):
        """Sets the upgradefrom of this ClusterExtendParam.

        :param upgradefrom: The upgradefrom of this ClusterExtendParam.
        :type upgradefrom: str
        """
        self._upgradefrom = upgradefrom

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
        if not isinstance(other, ClusterExtendParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
