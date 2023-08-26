# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResizeFlavorsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_uuid': 'str',
        'limit': 'int',
        'marker': 'str',
        'sort_dir': 'str',
        'sort_key': 'str',
        'source_flavor_id': 'str',
        'source_flavor_name': 'str'
    }

    attribute_map = {
        'instance_uuid': 'instance_uuid',
        'limit': 'limit',
        'marker': 'marker',
        'sort_dir': 'sort_dir',
        'sort_key': 'sort_key',
        'source_flavor_id': 'source_flavor_id',
        'source_flavor_name': 'source_flavor_name'
    }

    def __init__(self, instance_uuid=None, limit=None, marker=None, sort_dir=None, sort_key=None, source_flavor_id=None, source_flavor_name=None):
        """ListResizeFlavorsRequest

        The model defined in g42cloud sdk

        :param instance_uuid: The param of the ListResizeFlavorsRequest
        :type instance_uuid: str
        :param limit: The param of the ListResizeFlavorsRequest
        :type limit: int
        :param marker: The param of the ListResizeFlavorsRequest
        :type marker: str
        :param sort_dir: The param of the ListResizeFlavorsRequest
        :type sort_dir: str
        :param sort_key: The param of the ListResizeFlavorsRequest
        :type sort_key: str
        :param source_flavor_id: The param of the ListResizeFlavorsRequest
        :type source_flavor_id: str
        :param source_flavor_name: The param of the ListResizeFlavorsRequest
        :type source_flavor_name: str
        """
        
        

        self._instance_uuid = None
        self._limit = None
        self._marker = None
        self._sort_dir = None
        self._sort_key = None
        self._source_flavor_id = None
        self._source_flavor_name = None
        self.discriminator = None

        if instance_uuid is not None:
            self.instance_uuid = instance_uuid
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if sort_key is not None:
            self.sort_key = sort_key
        if source_flavor_id is not None:
            self.source_flavor_id = source_flavor_id
        if source_flavor_name is not None:
            self.source_flavor_name = source_flavor_name

    @property
    def instance_uuid(self):
        """Gets the instance_uuid of this ListResizeFlavorsRequest.

        :return: The instance_uuid of this ListResizeFlavorsRequest.
        :rtype: str
        """
        return self._instance_uuid

    @instance_uuid.setter
    def instance_uuid(self, instance_uuid):
        """Sets the instance_uuid of this ListResizeFlavorsRequest.

        :param instance_uuid: The instance_uuid of this ListResizeFlavorsRequest.
        :type instance_uuid: str
        """
        self._instance_uuid = instance_uuid

    @property
    def limit(self):
        """Gets the limit of this ListResizeFlavorsRequest.

        :return: The limit of this ListResizeFlavorsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListResizeFlavorsRequest.

        :param limit: The limit of this ListResizeFlavorsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListResizeFlavorsRequest.

        :return: The marker of this ListResizeFlavorsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListResizeFlavorsRequest.

        :param marker: The marker of this ListResizeFlavorsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListResizeFlavorsRequest.

        :return: The sort_dir of this ListResizeFlavorsRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListResizeFlavorsRequest.

        :param sort_dir: The sort_dir of this ListResizeFlavorsRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def sort_key(self):
        """Gets the sort_key of this ListResizeFlavorsRequest.

        :return: The sort_key of this ListResizeFlavorsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListResizeFlavorsRequest.

        :param sort_key: The sort_key of this ListResizeFlavorsRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def source_flavor_id(self):
        """Gets the source_flavor_id of this ListResizeFlavorsRequest.

        :return: The source_flavor_id of this ListResizeFlavorsRequest.
        :rtype: str
        """
        return self._source_flavor_id

    @source_flavor_id.setter
    def source_flavor_id(self, source_flavor_id):
        """Sets the source_flavor_id of this ListResizeFlavorsRequest.

        :param source_flavor_id: The source_flavor_id of this ListResizeFlavorsRequest.
        :type source_flavor_id: str
        """
        self._source_flavor_id = source_flavor_id

    @property
    def source_flavor_name(self):
        """Gets the source_flavor_name of this ListResizeFlavorsRequest.

        :return: The source_flavor_name of this ListResizeFlavorsRequest.
        :rtype: str
        """
        return self._source_flavor_name

    @source_flavor_name.setter
    def source_flavor_name(self, source_flavor_name):
        """Sets the source_flavor_name of this ListResizeFlavorsRequest.

        :param source_flavor_name: The source_flavor_name of this ListResizeFlavorsRequest.
        :type source_flavor_name: str
        """
        self._source_flavor_name = source_flavor_name

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
        if not isinstance(other, ListResizeFlavorsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
