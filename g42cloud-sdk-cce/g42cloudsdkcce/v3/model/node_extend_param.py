# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeExtendParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ecsperformancetype': 'str',
        'order_id': 'str',
        'product_id': 'str',
        'max_pods': 'int',
        'period_type': 'str',
        'period_num': 'int',
        'is_auto_renew': 'str',
        'is_auto_pay': 'str',
        'docker_lvm_config_override': 'str',
        'docker_base_size': 'int',
        'public_key': 'str',
        'alpha_cce_pre_install': 'str',
        'alpha_cce_post_install': 'str',
        'alpha_cce_node_image_id': 'str',
        'nic_multiqueue': 'str',
        'nic_threshold': 'str',
        'enterprise_project_id': 'str',
        'charging_mode': 'int'
    }

    attribute_map = {
        'ecsperformancetype': 'ecs:performancetype',
        'order_id': 'orderID',
        'product_id': 'productID',
        'max_pods': 'maxPods',
        'period_type': 'periodType',
        'period_num': 'periodNum',
        'is_auto_renew': 'isAutoRenew',
        'is_auto_pay': 'isAutoPay',
        'docker_lvm_config_override': 'DockerLVMConfigOverride',
        'docker_base_size': 'dockerBaseSize',
        'public_key': 'publicKey',
        'alpha_cce_pre_install': 'alpha.cce/preInstall',
        'alpha_cce_post_install': 'alpha.cce/postInstall',
        'alpha_cce_node_image_id': 'alpha.cce/NodeImageID',
        'nic_multiqueue': 'nicMultiqueue',
        'nic_threshold': 'nicThreshold',
        'enterprise_project_id': 'enterprise_project_id',
        'charging_mode': 'chargingMode'
    }

    def __init__(self, ecsperformancetype=None, order_id=None, product_id=None, max_pods=None, period_type=None, period_num=None, is_auto_renew=None, is_auto_pay=None, docker_lvm_config_override=None, docker_base_size=None, public_key=None, alpha_cce_pre_install=None, alpha_cce_post_install=None, alpha_cce_node_image_id=None, nic_multiqueue=None, nic_threshold=None, enterprise_project_id=None, charging_mode=None):
        """NodeExtendParam

        The model defined in g42cloud sdk

        :param ecsperformancetype: The param of the NodeExtendParam
        :type ecsperformancetype: str
        :param order_id: The param of the NodeExtendParam
        :type order_id: str
        :param product_id: The param of the NodeExtendParam
        :type product_id: str
        :param max_pods: The param of the NodeExtendParam
        :type max_pods: int
        :param period_type: The param of the NodeExtendParam
        :type period_type: str
        :param period_num: The param of the NodeExtendParam
        :type period_num: int
        :param is_auto_renew: The param of the NodeExtendParam
        :type is_auto_renew: str
        :param is_auto_pay: The param of the NodeExtendParam
        :type is_auto_pay: str
        :param docker_lvm_config_override: The param of the NodeExtendParam
        :type docker_lvm_config_override: str
        :param docker_base_size: The param of the NodeExtendParam
        :type docker_base_size: int
        :param public_key: The param of the NodeExtendParam
        :type public_key: str
        :param alpha_cce_pre_install: The param of the NodeExtendParam
        :type alpha_cce_pre_install: str
        :param alpha_cce_post_install: The param of the NodeExtendParam
        :type alpha_cce_post_install: str
        :param alpha_cce_node_image_id: The param of the NodeExtendParam
        :type alpha_cce_node_image_id: str
        :param nic_multiqueue: The param of the NodeExtendParam
        :type nic_multiqueue: str
        :param nic_threshold: The param of the NodeExtendParam
        :type nic_threshold: str
        :param enterprise_project_id: The param of the NodeExtendParam
        :type enterprise_project_id: str
        :param charging_mode: The param of the NodeExtendParam
        :type charging_mode: int
        """
        
        

        self._ecsperformancetype = None
        self._order_id = None
        self._product_id = None
        self._max_pods = None
        self._period_type = None
        self._period_num = None
        self._is_auto_renew = None
        self._is_auto_pay = None
        self._docker_lvm_config_override = None
        self._docker_base_size = None
        self._public_key = None
        self._alpha_cce_pre_install = None
        self._alpha_cce_post_install = None
        self._alpha_cce_node_image_id = None
        self._nic_multiqueue = None
        self._nic_threshold = None
        self._enterprise_project_id = None
        self._charging_mode = None
        self.discriminator = None

        if ecsperformancetype is not None:
            self.ecsperformancetype = ecsperformancetype
        if order_id is not None:
            self.order_id = order_id
        if product_id is not None:
            self.product_id = product_id
        if max_pods is not None:
            self.max_pods = max_pods
        if period_type is not None:
            self.period_type = period_type
        if period_num is not None:
            self.period_num = period_num
        if is_auto_renew is not None:
            self.is_auto_renew = is_auto_renew
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay
        if docker_lvm_config_override is not None:
            self.docker_lvm_config_override = docker_lvm_config_override
        if docker_base_size is not None:
            self.docker_base_size = docker_base_size
        if public_key is not None:
            self.public_key = public_key
        if alpha_cce_pre_install is not None:
            self.alpha_cce_pre_install = alpha_cce_pre_install
        if alpha_cce_post_install is not None:
            self.alpha_cce_post_install = alpha_cce_post_install
        if alpha_cce_node_image_id is not None:
            self.alpha_cce_node_image_id = alpha_cce_node_image_id
        if nic_multiqueue is not None:
            self.nic_multiqueue = nic_multiqueue
        if nic_threshold is not None:
            self.nic_threshold = nic_threshold
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if charging_mode is not None:
            self.charging_mode = charging_mode

    @property
    def ecsperformancetype(self):
        """Gets the ecsperformancetype of this NodeExtendParam.

        :return: The ecsperformancetype of this NodeExtendParam.
        :rtype: str
        """
        return self._ecsperformancetype

    @ecsperformancetype.setter
    def ecsperformancetype(self, ecsperformancetype):
        """Sets the ecsperformancetype of this NodeExtendParam.

        :param ecsperformancetype: The ecsperformancetype of this NodeExtendParam.
        :type ecsperformancetype: str
        """
        self._ecsperformancetype = ecsperformancetype

    @property
    def order_id(self):
        """Gets the order_id of this NodeExtendParam.

        :return: The order_id of this NodeExtendParam.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this NodeExtendParam.

        :param order_id: The order_id of this NodeExtendParam.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def product_id(self):
        """Gets the product_id of this NodeExtendParam.

        :return: The product_id of this NodeExtendParam.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this NodeExtendParam.

        :param product_id: The product_id of this NodeExtendParam.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def max_pods(self):
        """Gets the max_pods of this NodeExtendParam.

        :return: The max_pods of this NodeExtendParam.
        :rtype: int
        """
        return self._max_pods

    @max_pods.setter
    def max_pods(self, max_pods):
        """Sets the max_pods of this NodeExtendParam.

        :param max_pods: The max_pods of this NodeExtendParam.
        :type max_pods: int
        """
        self._max_pods = max_pods

    @property
    def period_type(self):
        """Gets the period_type of this NodeExtendParam.

        :return: The period_type of this NodeExtendParam.
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        """Sets the period_type of this NodeExtendParam.

        :param period_type: The period_type of this NodeExtendParam.
        :type period_type: str
        """
        self._period_type = period_type

    @property
    def period_num(self):
        """Gets the period_num of this NodeExtendParam.

        :return: The period_num of this NodeExtendParam.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        """Sets the period_num of this NodeExtendParam.

        :param period_num: The period_num of this NodeExtendParam.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def is_auto_renew(self):
        """Gets the is_auto_renew of this NodeExtendParam.

        :return: The is_auto_renew of this NodeExtendParam.
        :rtype: str
        """
        return self._is_auto_renew

    @is_auto_renew.setter
    def is_auto_renew(self, is_auto_renew):
        """Sets the is_auto_renew of this NodeExtendParam.

        :param is_auto_renew: The is_auto_renew of this NodeExtendParam.
        :type is_auto_renew: str
        """
        self._is_auto_renew = is_auto_renew

    @property
    def is_auto_pay(self):
        """Gets the is_auto_pay of this NodeExtendParam.

        :return: The is_auto_pay of this NodeExtendParam.
        :rtype: str
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        """Sets the is_auto_pay of this NodeExtendParam.

        :param is_auto_pay: The is_auto_pay of this NodeExtendParam.
        :type is_auto_pay: str
        """
        self._is_auto_pay = is_auto_pay

    @property
    def docker_lvm_config_override(self):
        """Gets the docker_lvm_config_override of this NodeExtendParam.

        :return: The docker_lvm_config_override of this NodeExtendParam.
        :rtype: str
        """
        return self._docker_lvm_config_override

    @docker_lvm_config_override.setter
    def docker_lvm_config_override(self, docker_lvm_config_override):
        """Sets the docker_lvm_config_override of this NodeExtendParam.

        :param docker_lvm_config_override: The docker_lvm_config_override of this NodeExtendParam.
        :type docker_lvm_config_override: str
        """
        self._docker_lvm_config_override = docker_lvm_config_override

    @property
    def docker_base_size(self):
        """Gets the docker_base_size of this NodeExtendParam.

        :return: The docker_base_size of this NodeExtendParam.
        :rtype: int
        """
        return self._docker_base_size

    @docker_base_size.setter
    def docker_base_size(self, docker_base_size):
        """Sets the docker_base_size of this NodeExtendParam.

        :param docker_base_size: The docker_base_size of this NodeExtendParam.
        :type docker_base_size: int
        """
        self._docker_base_size = docker_base_size

    @property
    def public_key(self):
        """Gets the public_key of this NodeExtendParam.

        :return: The public_key of this NodeExtendParam.
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this NodeExtendParam.

        :param public_key: The public_key of this NodeExtendParam.
        :type public_key: str
        """
        self._public_key = public_key

    @property
    def alpha_cce_pre_install(self):
        """Gets the alpha_cce_pre_install of this NodeExtendParam.

        :return: The alpha_cce_pre_install of this NodeExtendParam.
        :rtype: str
        """
        return self._alpha_cce_pre_install

    @alpha_cce_pre_install.setter
    def alpha_cce_pre_install(self, alpha_cce_pre_install):
        """Sets the alpha_cce_pre_install of this NodeExtendParam.

        :param alpha_cce_pre_install: The alpha_cce_pre_install of this NodeExtendParam.
        :type alpha_cce_pre_install: str
        """
        self._alpha_cce_pre_install = alpha_cce_pre_install

    @property
    def alpha_cce_post_install(self):
        """Gets the alpha_cce_post_install of this NodeExtendParam.

        :return: The alpha_cce_post_install of this NodeExtendParam.
        :rtype: str
        """
        return self._alpha_cce_post_install

    @alpha_cce_post_install.setter
    def alpha_cce_post_install(self, alpha_cce_post_install):
        """Sets the alpha_cce_post_install of this NodeExtendParam.

        :param alpha_cce_post_install: The alpha_cce_post_install of this NodeExtendParam.
        :type alpha_cce_post_install: str
        """
        self._alpha_cce_post_install = alpha_cce_post_install

    @property
    def alpha_cce_node_image_id(self):
        """Gets the alpha_cce_node_image_id of this NodeExtendParam.

        :return: The alpha_cce_node_image_id of this NodeExtendParam.
        :rtype: str
        """
        return self._alpha_cce_node_image_id

    @alpha_cce_node_image_id.setter
    def alpha_cce_node_image_id(self, alpha_cce_node_image_id):
        """Sets the alpha_cce_node_image_id of this NodeExtendParam.

        :param alpha_cce_node_image_id: The alpha_cce_node_image_id of this NodeExtendParam.
        :type alpha_cce_node_image_id: str
        """
        self._alpha_cce_node_image_id = alpha_cce_node_image_id

    @property
    def nic_multiqueue(self):
        """Gets the nic_multiqueue of this NodeExtendParam.

        :return: The nic_multiqueue of this NodeExtendParam.
        :rtype: str
        """
        return self._nic_multiqueue

    @nic_multiqueue.setter
    def nic_multiqueue(self, nic_multiqueue):
        """Sets the nic_multiqueue of this NodeExtendParam.

        :param nic_multiqueue: The nic_multiqueue of this NodeExtendParam.
        :type nic_multiqueue: str
        """
        self._nic_multiqueue = nic_multiqueue

    @property
    def nic_threshold(self):
        """Gets the nic_threshold of this NodeExtendParam.

        :return: The nic_threshold of this NodeExtendParam.
        :rtype: str
        """
        return self._nic_threshold

    @nic_threshold.setter
    def nic_threshold(self, nic_threshold):
        """Sets the nic_threshold of this NodeExtendParam.

        :param nic_threshold: The nic_threshold of this NodeExtendParam.
        :type nic_threshold: str
        """
        self._nic_threshold = nic_threshold

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this NodeExtendParam.

        :return: The enterprise_project_id of this NodeExtendParam.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this NodeExtendParam.

        :param enterprise_project_id: The enterprise_project_id of this NodeExtendParam.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def charging_mode(self):
        """Gets the charging_mode of this NodeExtendParam.

        :return: The charging_mode of this NodeExtendParam.
        :rtype: int
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        """Sets the charging_mode of this NodeExtendParam.

        :param charging_mode: The charging_mode of this NodeExtendParam.
        :type charging_mode: int
        """
        self._charging_mode = charging_mode

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
        if not isinstance(other, NodeExtendParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
