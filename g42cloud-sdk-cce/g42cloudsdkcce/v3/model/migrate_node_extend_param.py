# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MigrateNodeExtendParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'max_pods': 'int',
        'docker_lvm_config_override': 'str',
        'alpha_cce_pre_install': 'str',
        'alpha_cce_post_install': 'str',
        'alpha_cce_node_image_id': 'str'
    }

    attribute_map = {
        'max_pods': 'maxPods',
        'docker_lvm_config_override': 'DockerLVMConfigOverride',
        'alpha_cce_pre_install': 'alpha.cce/preInstall',
        'alpha_cce_post_install': 'alpha.cce/postInstall',
        'alpha_cce_node_image_id': 'alpha.cce/NodeImageID'
    }

    def __init__(self, max_pods=None, docker_lvm_config_override=None, alpha_cce_pre_install=None, alpha_cce_post_install=None, alpha_cce_node_image_id=None):
        """MigrateNodeExtendParam

        The model defined in g42cloud sdk

        :param max_pods: The param of the MigrateNodeExtendParam
        :type max_pods: int
        :param docker_lvm_config_override: The param of the MigrateNodeExtendParam
        :type docker_lvm_config_override: str
        :param alpha_cce_pre_install: The param of the MigrateNodeExtendParam
        :type alpha_cce_pre_install: str
        :param alpha_cce_post_install: The param of the MigrateNodeExtendParam
        :type alpha_cce_post_install: str
        :param alpha_cce_node_image_id: The param of the MigrateNodeExtendParam
        :type alpha_cce_node_image_id: str
        """
        
        

        self._max_pods = None
        self._docker_lvm_config_override = None
        self._alpha_cce_pre_install = None
        self._alpha_cce_post_install = None
        self._alpha_cce_node_image_id = None
        self.discriminator = None

        if max_pods is not None:
            self.max_pods = max_pods
        if docker_lvm_config_override is not None:
            self.docker_lvm_config_override = docker_lvm_config_override
        if alpha_cce_pre_install is not None:
            self.alpha_cce_pre_install = alpha_cce_pre_install
        if alpha_cce_post_install is not None:
            self.alpha_cce_post_install = alpha_cce_post_install
        if alpha_cce_node_image_id is not None:
            self.alpha_cce_node_image_id = alpha_cce_node_image_id

    @property
    def max_pods(self):
        """Gets the max_pods of this MigrateNodeExtendParam.

        :return: The max_pods of this MigrateNodeExtendParam.
        :rtype: int
        """
        return self._max_pods

    @max_pods.setter
    def max_pods(self, max_pods):
        """Sets the max_pods of this MigrateNodeExtendParam.

        :param max_pods: The max_pods of this MigrateNodeExtendParam.
        :type max_pods: int
        """
        self._max_pods = max_pods

    @property
    def docker_lvm_config_override(self):
        """Gets the docker_lvm_config_override of this MigrateNodeExtendParam.

        :return: The docker_lvm_config_override of this MigrateNodeExtendParam.
        :rtype: str
        """
        return self._docker_lvm_config_override

    @docker_lvm_config_override.setter
    def docker_lvm_config_override(self, docker_lvm_config_override):
        """Sets the docker_lvm_config_override of this MigrateNodeExtendParam.

        :param docker_lvm_config_override: The docker_lvm_config_override of this MigrateNodeExtendParam.
        :type docker_lvm_config_override: str
        """
        self._docker_lvm_config_override = docker_lvm_config_override

    @property
    def alpha_cce_pre_install(self):
        """Gets the alpha_cce_pre_install of this MigrateNodeExtendParam.

        :return: The alpha_cce_pre_install of this MigrateNodeExtendParam.
        :rtype: str
        """
        return self._alpha_cce_pre_install

    @alpha_cce_pre_install.setter
    def alpha_cce_pre_install(self, alpha_cce_pre_install):
        """Sets the alpha_cce_pre_install of this MigrateNodeExtendParam.

        :param alpha_cce_pre_install: The alpha_cce_pre_install of this MigrateNodeExtendParam.
        :type alpha_cce_pre_install: str
        """
        self._alpha_cce_pre_install = alpha_cce_pre_install

    @property
    def alpha_cce_post_install(self):
        """Gets the alpha_cce_post_install of this MigrateNodeExtendParam.

        :return: The alpha_cce_post_install of this MigrateNodeExtendParam.
        :rtype: str
        """
        return self._alpha_cce_post_install

    @alpha_cce_post_install.setter
    def alpha_cce_post_install(self, alpha_cce_post_install):
        """Sets the alpha_cce_post_install of this MigrateNodeExtendParam.

        :param alpha_cce_post_install: The alpha_cce_post_install of this MigrateNodeExtendParam.
        :type alpha_cce_post_install: str
        """
        self._alpha_cce_post_install = alpha_cce_post_install

    @property
    def alpha_cce_node_image_id(self):
        """Gets the alpha_cce_node_image_id of this MigrateNodeExtendParam.

        :return: The alpha_cce_node_image_id of this MigrateNodeExtendParam.
        :rtype: str
        """
        return self._alpha_cce_node_image_id

    @alpha_cce_node_image_id.setter
    def alpha_cce_node_image_id(self, alpha_cce_node_image_id):
        """Sets the alpha_cce_node_image_id of this MigrateNodeExtendParam.

        :param alpha_cce_node_image_id: The alpha_cce_node_image_id of this MigrateNodeExtendParam.
        :type alpha_cce_node_image_id: str
        """
        self._alpha_cce_node_image_id = alpha_cce_node_image_id

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
        if not isinstance(other, MigrateNodeExtendParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
