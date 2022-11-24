# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Proxy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pool_id': 'str',
        'status': 'str',
        'address': 'str',
        'elb_vip': 'str',
        'eip': 'str',
        'port': 'int',
        'pool_status': 'str',
        'delay_threshold_in_kilobytes': 'int',
        'cpu': 'str',
        'mem': 'str',
        'node_num': 'int',
        'nodes': 'list[ProxyNode]',
        'mode': 'str'
    }

    attribute_map = {
        'pool_id': 'pool_id',
        'status': 'status',
        'address': 'address',
        'elb_vip': 'elb_vip',
        'eip': 'eip',
        'port': 'port',
        'pool_status': 'pool_status',
        'delay_threshold_in_kilobytes': 'delay_threshold_in_kilobytes',
        'cpu': 'cpu',
        'mem': 'mem',
        'node_num': 'node_num',
        'nodes': 'nodes',
        'mode': 'mode'
    }

    def __init__(self, pool_id=None, status=None, address=None, elb_vip=None, eip=None, port=None, pool_status=None, delay_threshold_in_kilobytes=None, cpu=None, mem=None, node_num=None, nodes=None, mode=None):
        """Proxy

        The model defined in g42cloud sdk

        :param pool_id: The param of the Proxy
        :type pool_id: str
        :param status: The param of the Proxy
        :type status: str
        :param address: The param of the Proxy
        :type address: str
        :param elb_vip: The param of the Proxy
        :type elb_vip: str
        :param eip: The param of the Proxy
        :type eip: str
        :param port: The param of the Proxy
        :type port: int
        :param pool_status: The param of the Proxy
        :type pool_status: str
        :param delay_threshold_in_kilobytes: The param of the Proxy
        :type delay_threshold_in_kilobytes: int
        :param cpu: The param of the Proxy
        :type cpu: str
        :param mem: The param of the Proxy
        :type mem: str
        :param node_num: The param of the Proxy
        :type node_num: int
        :param nodes: The param of the Proxy
        :type nodes: list[:class:`g42cloudsdkrds.v3.ProxyNode`]
        :param mode: The param of the Proxy
        :type mode: str
        """
        
        

        self._pool_id = None
        self._status = None
        self._address = None
        self._elb_vip = None
        self._eip = None
        self._port = None
        self._pool_status = None
        self._delay_threshold_in_kilobytes = None
        self._cpu = None
        self._mem = None
        self._node_num = None
        self._nodes = None
        self._mode = None
        self.discriminator = None

        self.pool_id = pool_id
        self.status = status
        self.address = address
        self.elb_vip = elb_vip
        self.eip = eip
        self.port = port
        self.pool_status = pool_status
        self.delay_threshold_in_kilobytes = delay_threshold_in_kilobytes
        self.cpu = cpu
        self.mem = mem
        self.node_num = node_num
        self.nodes = nodes
        self.mode = mode

    @property
    def pool_id(self):
        """Gets the pool_id of this Proxy.

        :return: The pool_id of this Proxy.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        """Sets the pool_id of this Proxy.

        :param pool_id: The pool_id of this Proxy.
        :type pool_id: str
        """
        self._pool_id = pool_id

    @property
    def status(self):
        """Gets the status of this Proxy.

        :return: The status of this Proxy.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Proxy.

        :param status: The status of this Proxy.
        :type status: str
        """
        self._status = status

    @property
    def address(self):
        """Gets the address of this Proxy.

        :return: The address of this Proxy.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Proxy.

        :param address: The address of this Proxy.
        :type address: str
        """
        self._address = address

    @property
    def elb_vip(self):
        """Gets the elb_vip of this Proxy.

        :return: The elb_vip of this Proxy.
        :rtype: str
        """
        return self._elb_vip

    @elb_vip.setter
    def elb_vip(self, elb_vip):
        """Sets the elb_vip of this Proxy.

        :param elb_vip: The elb_vip of this Proxy.
        :type elb_vip: str
        """
        self._elb_vip = elb_vip

    @property
    def eip(self):
        """Gets the eip of this Proxy.

        :return: The eip of this Proxy.
        :rtype: str
        """
        return self._eip

    @eip.setter
    def eip(self, eip):
        """Sets the eip of this Proxy.

        :param eip: The eip of this Proxy.
        :type eip: str
        """
        self._eip = eip

    @property
    def port(self):
        """Gets the port of this Proxy.

        :return: The port of this Proxy.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this Proxy.

        :param port: The port of this Proxy.
        :type port: int
        """
        self._port = port

    @property
    def pool_status(self):
        """Gets the pool_status of this Proxy.

        :return: The pool_status of this Proxy.
        :rtype: str
        """
        return self._pool_status

    @pool_status.setter
    def pool_status(self, pool_status):
        """Sets the pool_status of this Proxy.

        :param pool_status: The pool_status of this Proxy.
        :type pool_status: str
        """
        self._pool_status = pool_status

    @property
    def delay_threshold_in_kilobytes(self):
        """Gets the delay_threshold_in_kilobytes of this Proxy.

        :return: The delay_threshold_in_kilobytes of this Proxy.
        :rtype: int
        """
        return self._delay_threshold_in_kilobytes

    @delay_threshold_in_kilobytes.setter
    def delay_threshold_in_kilobytes(self, delay_threshold_in_kilobytes):
        """Sets the delay_threshold_in_kilobytes of this Proxy.

        :param delay_threshold_in_kilobytes: The delay_threshold_in_kilobytes of this Proxy.
        :type delay_threshold_in_kilobytes: int
        """
        self._delay_threshold_in_kilobytes = delay_threshold_in_kilobytes

    @property
    def cpu(self):
        """Gets the cpu of this Proxy.

        :return: The cpu of this Proxy.
        :rtype: str
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this Proxy.

        :param cpu: The cpu of this Proxy.
        :type cpu: str
        """
        self._cpu = cpu

    @property
    def mem(self):
        """Gets the mem of this Proxy.

        :return: The mem of this Proxy.
        :rtype: str
        """
        return self._mem

    @mem.setter
    def mem(self, mem):
        """Sets the mem of this Proxy.

        :param mem: The mem of this Proxy.
        :type mem: str
        """
        self._mem = mem

    @property
    def node_num(self):
        """Gets the node_num of this Proxy.

        :return: The node_num of this Proxy.
        :rtype: int
        """
        return self._node_num

    @node_num.setter
    def node_num(self, node_num):
        """Sets the node_num of this Proxy.

        :param node_num: The node_num of this Proxy.
        :type node_num: int
        """
        self._node_num = node_num

    @property
    def nodes(self):
        """Gets the nodes of this Proxy.

        :return: The nodes of this Proxy.
        :rtype: list[:class:`g42cloudsdkrds.v3.ProxyNode`]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this Proxy.

        :param nodes: The nodes of this Proxy.
        :type nodes: list[:class:`g42cloudsdkrds.v3.ProxyNode`]
        """
        self._nodes = nodes

    @property
    def mode(self):
        """Gets the mode of this Proxy.

        :return: The mode of this Proxy.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this Proxy.

        :param mode: The mode of this Proxy.
        :type mode: str
        """
        self._mode = mode

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
        if not isinstance(other, Proxy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
