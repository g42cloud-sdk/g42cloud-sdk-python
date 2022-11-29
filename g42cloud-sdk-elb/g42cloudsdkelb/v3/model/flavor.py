# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Flavor:

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
        'info': 'FlavorInfo',
        'name': 'str',
        'shared': 'bool',
        'project_id': 'str',
        'type': 'str',
        'flavor_sold_out': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'info': 'info',
        'name': 'name',
        'shared': 'shared',
        'project_id': 'project_id',
        'type': 'type',
        'flavor_sold_out': 'flavor_sold_out'
    }

    def __init__(self, id=None, info=None, name=None, shared=None, project_id=None, type=None, flavor_sold_out=None):
        """Flavor

        The model defined in g42cloud sdk

        :param id: The param of the Flavor
        :type id: str
        :param info: The param of the Flavor
        :type info: :class:`g42cloudsdkelb.v3.FlavorInfo`
        :param name: The param of the Flavor
        :type name: str
        :param shared: The param of the Flavor
        :type shared: bool
        :param project_id: The param of the Flavor
        :type project_id: str
        :param type: The param of the Flavor
        :type type: str
        :param flavor_sold_out: The param of the Flavor
        :type flavor_sold_out: bool
        """
        
        

        self._id = None
        self._info = None
        self._name = None
        self._shared = None
        self._project_id = None
        self._type = None
        self._flavor_sold_out = None
        self.discriminator = None

        self.id = id
        self.info = info
        self.name = name
        self.shared = shared
        self.project_id = project_id
        self.type = type
        self.flavor_sold_out = flavor_sold_out

    @property
    def id(self):
        """Gets the id of this Flavor.

        :return: The id of this Flavor.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Flavor.

        :param id: The id of this Flavor.
        :type id: str
        """
        self._id = id

    @property
    def info(self):
        """Gets the info of this Flavor.

        :return: The info of this Flavor.
        :rtype: :class:`g42cloudsdkelb.v3.FlavorInfo`
        """
        return self._info

    @info.setter
    def info(self, info):
        """Sets the info of this Flavor.

        :param info: The info of this Flavor.
        :type info: :class:`g42cloudsdkelb.v3.FlavorInfo`
        """
        self._info = info

    @property
    def name(self):
        """Gets the name of this Flavor.

        :return: The name of this Flavor.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Flavor.

        :param name: The name of this Flavor.
        :type name: str
        """
        self._name = name

    @property
    def shared(self):
        """Gets the shared of this Flavor.

        :return: The shared of this Flavor.
        :rtype: bool
        """
        return self._shared

    @shared.setter
    def shared(self, shared):
        """Sets the shared of this Flavor.

        :param shared: The shared of this Flavor.
        :type shared: bool
        """
        self._shared = shared

    @property
    def project_id(self):
        """Gets the project_id of this Flavor.

        :return: The project_id of this Flavor.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Flavor.

        :param project_id: The project_id of this Flavor.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def type(self):
        """Gets the type of this Flavor.

        :return: The type of this Flavor.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Flavor.

        :param type: The type of this Flavor.
        :type type: str
        """
        self._type = type

    @property
    def flavor_sold_out(self):
        """Gets the flavor_sold_out of this Flavor.

        :return: The flavor_sold_out of this Flavor.
        :rtype: bool
        """
        return self._flavor_sold_out

    @flavor_sold_out.setter
    def flavor_sold_out(self, flavor_sold_out):
        """Sets the flavor_sold_out of this Flavor.

        :param flavor_sold_out: The flavor_sold_out of this Flavor.
        :type flavor_sold_out: bool
        """
        self._flavor_sold_out = flavor_sold_out

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
        if not isinstance(other, Flavor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
