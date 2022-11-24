# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MasterInstance:

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
        'status': 'str',
        'name': 'str',
        'weight': 'int',
        'available_zones': 'list[AvailableZone]',
        'cpu_num': 'int'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'name': 'name',
        'weight': 'weight',
        'available_zones': 'available_zones',
        'cpu_num': 'cpu_num'
    }

    def __init__(self, id=None, status=None, name=None, weight=None, available_zones=None, cpu_num=None):
        """MasterInstance

        The model defined in g42cloud sdk

        :param id: The param of the MasterInstance
        :type id: str
        :param status: The param of the MasterInstance
        :type status: str
        :param name: The param of the MasterInstance
        :type name: str
        :param weight: The param of the MasterInstance
        :type weight: int
        :param available_zones: The param of the MasterInstance
        :type available_zones: list[:class:`g42cloudsdkrds.v3.AvailableZone`]
        :param cpu_num: The param of the MasterInstance
        :type cpu_num: int
        """
        
        

        self._id = None
        self._status = None
        self._name = None
        self._weight = None
        self._available_zones = None
        self._cpu_num = None
        self.discriminator = None

        self.id = id
        self.status = status
        self.name = name
        self.weight = weight
        self.available_zones = available_zones
        self.cpu_num = cpu_num

    @property
    def id(self):
        """Gets the id of this MasterInstance.

        :return: The id of this MasterInstance.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MasterInstance.

        :param id: The id of this MasterInstance.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this MasterInstance.

        :return: The status of this MasterInstance.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MasterInstance.

        :param status: The status of this MasterInstance.
        :type status: str
        """
        self._status = status

    @property
    def name(self):
        """Gets the name of this MasterInstance.

        :return: The name of this MasterInstance.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MasterInstance.

        :param name: The name of this MasterInstance.
        :type name: str
        """
        self._name = name

    @property
    def weight(self):
        """Gets the weight of this MasterInstance.

        :return: The weight of this MasterInstance.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this MasterInstance.

        :param weight: The weight of this MasterInstance.
        :type weight: int
        """
        self._weight = weight

    @property
    def available_zones(self):
        """Gets the available_zones of this MasterInstance.

        :return: The available_zones of this MasterInstance.
        :rtype: list[:class:`g42cloudsdkrds.v3.AvailableZone`]
        """
        return self._available_zones

    @available_zones.setter
    def available_zones(self, available_zones):
        """Sets the available_zones of this MasterInstance.

        :param available_zones: The available_zones of this MasterInstance.
        :type available_zones: list[:class:`g42cloudsdkrds.v3.AvailableZone`]
        """
        self._available_zones = available_zones

    @property
    def cpu_num(self):
        """Gets the cpu_num of this MasterInstance.

        :return: The cpu_num of this MasterInstance.
        :rtype: int
        """
        return self._cpu_num

    @cpu_num.setter
    def cpu_num(self, cpu_num):
        """Sets the cpu_num of this MasterInstance.

        :param cpu_num: The cpu_num of this MasterInstance.
        :type cpu_num: int
        """
        self._cpu_num = cpu_num

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
        if not isinstance(other, MasterInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
