# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flavor': 'str',
        'az': 'str',
        'os': 'str',
        'login': 'Login',
        'root_volume': 'Volume',
        'data_volumes': 'list[Volume]',
        'storage': 'Storage',
        'public_ip': 'NodePublicIP',
        'node_nic_spec': 'NodeNicSpec',
        'count': 'int',
        'billing_mode': 'int',
        'taints': 'list[Taint]',
        'k8s_tags': 'dict(str, str)',
        'ecs_group_id': 'str',
        'dedicated_host_id': 'str',
        'user_tags': 'list[UserTag]',
        'runtime': 'Runtime',
        'extend_param': 'NodeExtendParam'
    }

    attribute_map = {
        'flavor': 'flavor',
        'az': 'az',
        'os': 'os',
        'login': 'login',
        'root_volume': 'rootVolume',
        'data_volumes': 'dataVolumes',
        'storage': 'storage',
        'public_ip': 'publicIP',
        'node_nic_spec': 'nodeNicSpec',
        'count': 'count',
        'billing_mode': 'billingMode',
        'taints': 'taints',
        'k8s_tags': 'k8sTags',
        'ecs_group_id': 'ecsGroupId',
        'dedicated_host_id': 'dedicatedHostId',
        'user_tags': 'userTags',
        'runtime': 'runtime',
        'extend_param': 'extendParam'
    }

    def __init__(self, flavor=None, az=None, os=None, login=None, root_volume=None, data_volumes=None, storage=None, public_ip=None, node_nic_spec=None, count=None, billing_mode=None, taints=None, k8s_tags=None, ecs_group_id=None, dedicated_host_id=None, user_tags=None, runtime=None, extend_param=None):
        """NodeSpec

        The model defined in g42cloud sdk

        :param flavor: The param of the NodeSpec
        :type flavor: str
        :param az: The param of the NodeSpec
        :type az: str
        :param os: The param of the NodeSpec
        :type os: str
        :param login: The param of the NodeSpec
        :type login: :class:`g42cloudsdkcce.v3.Login`
        :param root_volume: The param of the NodeSpec
        :type root_volume: :class:`g42cloudsdkcce.v3.Volume`
        :param data_volumes: The param of the NodeSpec
        :type data_volumes: list[:class:`g42cloudsdkcce.v3.Volume`]
        :param storage: The param of the NodeSpec
        :type storage: :class:`g42cloudsdkcce.v3.Storage`
        :param public_ip: The param of the NodeSpec
        :type public_ip: :class:`g42cloudsdkcce.v3.NodePublicIP`
        :param node_nic_spec: The param of the NodeSpec
        :type node_nic_spec: :class:`g42cloudsdkcce.v3.NodeNicSpec`
        :param count: The param of the NodeSpec
        :type count: int
        :param billing_mode: The param of the NodeSpec
        :type billing_mode: int
        :param taints: The param of the NodeSpec
        :type taints: list[:class:`g42cloudsdkcce.v3.Taint`]
        :param k8s_tags: The param of the NodeSpec
        :type k8s_tags: dict(str, str)
        :param ecs_group_id: The param of the NodeSpec
        :type ecs_group_id: str
        :param dedicated_host_id: The param of the NodeSpec
        :type dedicated_host_id: str
        :param user_tags: The param of the NodeSpec
        :type user_tags: list[:class:`g42cloudsdkcce.v3.UserTag`]
        :param runtime: The param of the NodeSpec
        :type runtime: :class:`g42cloudsdkcce.v3.Runtime`
        :param extend_param: The param of the NodeSpec
        :type extend_param: :class:`g42cloudsdkcce.v3.NodeExtendParam`
        """
        
        

        self._flavor = None
        self._az = None
        self._os = None
        self._login = None
        self._root_volume = None
        self._data_volumes = None
        self._storage = None
        self._public_ip = None
        self._node_nic_spec = None
        self._count = None
        self._billing_mode = None
        self._taints = None
        self._k8s_tags = None
        self._ecs_group_id = None
        self._dedicated_host_id = None
        self._user_tags = None
        self._runtime = None
        self._extend_param = None
        self.discriminator = None

        self.flavor = flavor
        self.az = az
        if os is not None:
            self.os = os
        self.login = login
        self.root_volume = root_volume
        self.data_volumes = data_volumes
        if storage is not None:
            self.storage = storage
        if public_ip is not None:
            self.public_ip = public_ip
        if node_nic_spec is not None:
            self.node_nic_spec = node_nic_spec
        if count is not None:
            self.count = count
        if billing_mode is not None:
            self.billing_mode = billing_mode
        if taints is not None:
            self.taints = taints
        if k8s_tags is not None:
            self.k8s_tags = k8s_tags
        if ecs_group_id is not None:
            self.ecs_group_id = ecs_group_id
        if dedicated_host_id is not None:
            self.dedicated_host_id = dedicated_host_id
        if user_tags is not None:
            self.user_tags = user_tags
        if runtime is not None:
            self.runtime = runtime
        if extend_param is not None:
            self.extend_param = extend_param

    @property
    def flavor(self):
        """Gets the flavor of this NodeSpec.

        :return: The flavor of this NodeSpec.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this NodeSpec.

        :param flavor: The flavor of this NodeSpec.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def az(self):
        """Gets the az of this NodeSpec.

        :return: The az of this NodeSpec.
        :rtype: str
        """
        return self._az

    @az.setter
    def az(self, az):
        """Sets the az of this NodeSpec.

        :param az: The az of this NodeSpec.
        :type az: str
        """
        self._az = az

    @property
    def os(self):
        """Gets the os of this NodeSpec.

        :return: The os of this NodeSpec.
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this NodeSpec.

        :param os: The os of this NodeSpec.
        :type os: str
        """
        self._os = os

    @property
    def login(self):
        """Gets the login of this NodeSpec.

        :return: The login of this NodeSpec.
        :rtype: :class:`g42cloudsdkcce.v3.Login`
        """
        return self._login

    @login.setter
    def login(self, login):
        """Sets the login of this NodeSpec.

        :param login: The login of this NodeSpec.
        :type login: :class:`g42cloudsdkcce.v3.Login`
        """
        self._login = login

    @property
    def root_volume(self):
        """Gets the root_volume of this NodeSpec.

        :return: The root_volume of this NodeSpec.
        :rtype: :class:`g42cloudsdkcce.v3.Volume`
        """
        return self._root_volume

    @root_volume.setter
    def root_volume(self, root_volume):
        """Sets the root_volume of this NodeSpec.

        :param root_volume: The root_volume of this NodeSpec.
        :type root_volume: :class:`g42cloudsdkcce.v3.Volume`
        """
        self._root_volume = root_volume

    @property
    def data_volumes(self):
        """Gets the data_volumes of this NodeSpec.

        :return: The data_volumes of this NodeSpec.
        :rtype: list[:class:`g42cloudsdkcce.v3.Volume`]
        """
        return self._data_volumes

    @data_volumes.setter
    def data_volumes(self, data_volumes):
        """Sets the data_volumes of this NodeSpec.

        :param data_volumes: The data_volumes of this NodeSpec.
        :type data_volumes: list[:class:`g42cloudsdkcce.v3.Volume`]
        """
        self._data_volumes = data_volumes

    @property
    def storage(self):
        """Gets the storage of this NodeSpec.

        :return: The storage of this NodeSpec.
        :rtype: :class:`g42cloudsdkcce.v3.Storage`
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """Sets the storage of this NodeSpec.

        :param storage: The storage of this NodeSpec.
        :type storage: :class:`g42cloudsdkcce.v3.Storage`
        """
        self._storage = storage

    @property
    def public_ip(self):
        """Gets the public_ip of this NodeSpec.

        :return: The public_ip of this NodeSpec.
        :rtype: :class:`g42cloudsdkcce.v3.NodePublicIP`
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this NodeSpec.

        :param public_ip: The public_ip of this NodeSpec.
        :type public_ip: :class:`g42cloudsdkcce.v3.NodePublicIP`
        """
        self._public_ip = public_ip

    @property
    def node_nic_spec(self):
        """Gets the node_nic_spec of this NodeSpec.

        :return: The node_nic_spec of this NodeSpec.
        :rtype: :class:`g42cloudsdkcce.v3.NodeNicSpec`
        """
        return self._node_nic_spec

    @node_nic_spec.setter
    def node_nic_spec(self, node_nic_spec):
        """Sets the node_nic_spec of this NodeSpec.

        :param node_nic_spec: The node_nic_spec of this NodeSpec.
        :type node_nic_spec: :class:`g42cloudsdkcce.v3.NodeNicSpec`
        """
        self._node_nic_spec = node_nic_spec

    @property
    def count(self):
        """Gets the count of this NodeSpec.

        :return: The count of this NodeSpec.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this NodeSpec.

        :param count: The count of this NodeSpec.
        :type count: int
        """
        self._count = count

    @property
    def billing_mode(self):
        """Gets the billing_mode of this NodeSpec.

        :return: The billing_mode of this NodeSpec.
        :rtype: int
        """
        return self._billing_mode

    @billing_mode.setter
    def billing_mode(self, billing_mode):
        """Sets the billing_mode of this NodeSpec.

        :param billing_mode: The billing_mode of this NodeSpec.
        :type billing_mode: int
        """
        self._billing_mode = billing_mode

    @property
    def taints(self):
        """Gets the taints of this NodeSpec.

        :return: The taints of this NodeSpec.
        :rtype: list[:class:`g42cloudsdkcce.v3.Taint`]
        """
        return self._taints

    @taints.setter
    def taints(self, taints):
        """Sets the taints of this NodeSpec.

        :param taints: The taints of this NodeSpec.
        :type taints: list[:class:`g42cloudsdkcce.v3.Taint`]
        """
        self._taints = taints

    @property
    def k8s_tags(self):
        """Gets the k8s_tags of this NodeSpec.

        :return: The k8s_tags of this NodeSpec.
        :rtype: dict(str, str)
        """
        return self._k8s_tags

    @k8s_tags.setter
    def k8s_tags(self, k8s_tags):
        """Sets the k8s_tags of this NodeSpec.

        :param k8s_tags: The k8s_tags of this NodeSpec.
        :type k8s_tags: dict(str, str)
        """
        self._k8s_tags = k8s_tags

    @property
    def ecs_group_id(self):
        """Gets the ecs_group_id of this NodeSpec.

        :return: The ecs_group_id of this NodeSpec.
        :rtype: str
        """
        return self._ecs_group_id

    @ecs_group_id.setter
    def ecs_group_id(self, ecs_group_id):
        """Sets the ecs_group_id of this NodeSpec.

        :param ecs_group_id: The ecs_group_id of this NodeSpec.
        :type ecs_group_id: str
        """
        self._ecs_group_id = ecs_group_id

    @property
    def dedicated_host_id(self):
        """Gets the dedicated_host_id of this NodeSpec.

        :return: The dedicated_host_id of this NodeSpec.
        :rtype: str
        """
        return self._dedicated_host_id

    @dedicated_host_id.setter
    def dedicated_host_id(self, dedicated_host_id):
        """Sets the dedicated_host_id of this NodeSpec.

        :param dedicated_host_id: The dedicated_host_id of this NodeSpec.
        :type dedicated_host_id: str
        """
        self._dedicated_host_id = dedicated_host_id

    @property
    def user_tags(self):
        """Gets the user_tags of this NodeSpec.

        :return: The user_tags of this NodeSpec.
        :rtype: list[:class:`g42cloudsdkcce.v3.UserTag`]
        """
        return self._user_tags

    @user_tags.setter
    def user_tags(self, user_tags):
        """Sets the user_tags of this NodeSpec.

        :param user_tags: The user_tags of this NodeSpec.
        :type user_tags: list[:class:`g42cloudsdkcce.v3.UserTag`]
        """
        self._user_tags = user_tags

    @property
    def runtime(self):
        """Gets the runtime of this NodeSpec.

        :return: The runtime of this NodeSpec.
        :rtype: :class:`g42cloudsdkcce.v3.Runtime`
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        """Sets the runtime of this NodeSpec.

        :param runtime: The runtime of this NodeSpec.
        :type runtime: :class:`g42cloudsdkcce.v3.Runtime`
        """
        self._runtime = runtime

    @property
    def extend_param(self):
        """Gets the extend_param of this NodeSpec.

        :return: The extend_param of this NodeSpec.
        :rtype: :class:`g42cloudsdkcce.v3.NodeExtendParam`
        """
        return self._extend_param

    @extend_param.setter
    def extend_param(self, extend_param):
        """Sets the extend_param of this NodeSpec.

        :param extend_param: The extend_param of this NodeSpec.
        :type extend_param: :class:`g42cloudsdkcce.v3.NodeExtendParam`
        """
        self._extend_param = extend_param

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
        if not isinstance(other, NodeSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
