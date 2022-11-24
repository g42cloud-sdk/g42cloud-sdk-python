# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVolumesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'marker': 'str',
        'name': 'str',
        'limit': 'int',
        'sort_key': 'str',
        'offset': 'int',
        'sort_dir': 'str',
        'status': 'str',
        'metadata': 'str',
        'availability_zone': 'str',
        'multiattach': 'bool',
        'service_type': 'str',
        'dedicated_storage_id': 'str',
        'dedicated_storage_name': 'str',
        'volume_type_id': 'str',
        'id': 'str',
        'ids': 'str',
        'enterprise_project_id': 'str',
        'server_id': 'str'
    }

    attribute_map = {
        'marker': 'marker',
        'name': 'name',
        'limit': 'limit',
        'sort_key': 'sort_key',
        'offset': 'offset',
        'sort_dir': 'sort_dir',
        'status': 'status',
        'metadata': 'metadata',
        'availability_zone': 'availability_zone',
        'multiattach': 'multiattach',
        'service_type': 'service_type',
        'dedicated_storage_id': 'dedicated_storage_id',
        'dedicated_storage_name': 'dedicated_storage_name',
        'volume_type_id': 'volume_type_id',
        'id': 'id',
        'ids': 'ids',
        'enterprise_project_id': 'enterprise_project_id',
        'server_id': 'server_id'
    }

    def __init__(self, marker=None, name=None, limit=None, sort_key=None, offset=None, sort_dir=None, status=None, metadata=None, availability_zone=None, multiattach=None, service_type=None, dedicated_storage_id=None, dedicated_storage_name=None, volume_type_id=None, id=None, ids=None, enterprise_project_id=None, server_id=None):
        """ListVolumesRequest

        The model defined in g42cloud sdk

        :param marker: The param of the ListVolumesRequest
        :type marker: str
        :param name: The param of the ListVolumesRequest
        :type name: str
        :param limit: The param of the ListVolumesRequest
        :type limit: int
        :param sort_key: The param of the ListVolumesRequest
        :type sort_key: str
        :param offset: The param of the ListVolumesRequest
        :type offset: int
        :param sort_dir: The param of the ListVolumesRequest
        :type sort_dir: str
        :param status: The param of the ListVolumesRequest
        :type status: str
        :param metadata: The param of the ListVolumesRequest
        :type metadata: str
        :param availability_zone: The param of the ListVolumesRequest
        :type availability_zone: str
        :param multiattach: The param of the ListVolumesRequest
        :type multiattach: bool
        :param service_type: The param of the ListVolumesRequest
        :type service_type: str
        :param dedicated_storage_id: The param of the ListVolumesRequest
        :type dedicated_storage_id: str
        :param dedicated_storage_name: The param of the ListVolumesRequest
        :type dedicated_storage_name: str
        :param volume_type_id: The param of the ListVolumesRequest
        :type volume_type_id: str
        :param id: The param of the ListVolumesRequest
        :type id: str
        :param ids: The param of the ListVolumesRequest
        :type ids: str
        :param enterprise_project_id: The param of the ListVolumesRequest
        :type enterprise_project_id: str
        :param server_id: The param of the ListVolumesRequest
        :type server_id: str
        """
        
        

        self._marker = None
        self._name = None
        self._limit = None
        self._sort_key = None
        self._offset = None
        self._sort_dir = None
        self._status = None
        self._metadata = None
        self._availability_zone = None
        self._multiattach = None
        self._service_type = None
        self._dedicated_storage_id = None
        self._dedicated_storage_name = None
        self._volume_type_id = None
        self._id = None
        self._ids = None
        self._enterprise_project_id = None
        self._server_id = None
        self.discriminator = None

        if marker is not None:
            self.marker = marker
        if name is not None:
            self.name = name
        if limit is not None:
            self.limit = limit
        if sort_key is not None:
            self.sort_key = sort_key
        if offset is not None:
            self.offset = offset
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if status is not None:
            self.status = status
        if metadata is not None:
            self.metadata = metadata
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if multiattach is not None:
            self.multiattach = multiattach
        if service_type is not None:
            self.service_type = service_type
        if dedicated_storage_id is not None:
            self.dedicated_storage_id = dedicated_storage_id
        if dedicated_storage_name is not None:
            self.dedicated_storage_name = dedicated_storage_name
        if volume_type_id is not None:
            self.volume_type_id = volume_type_id
        if id is not None:
            self.id = id
        if ids is not None:
            self.ids = ids
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if server_id is not None:
            self.server_id = server_id

    @property
    def marker(self):
        """Gets the marker of this ListVolumesRequest.

        :return: The marker of this ListVolumesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListVolumesRequest.

        :param marker: The marker of this ListVolumesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def name(self):
        """Gets the name of this ListVolumesRequest.

        :return: The name of this ListVolumesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListVolumesRequest.

        :param name: The name of this ListVolumesRequest.
        :type name: str
        """
        self._name = name

    @property
    def limit(self):
        """Gets the limit of this ListVolumesRequest.

        :return: The limit of this ListVolumesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListVolumesRequest.

        :param limit: The limit of this ListVolumesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort_key(self):
        """Gets the sort_key of this ListVolumesRequest.

        :return: The sort_key of this ListVolumesRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListVolumesRequest.

        :param sort_key: The sort_key of this ListVolumesRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def offset(self):
        """Gets the offset of this ListVolumesRequest.

        :return: The offset of this ListVolumesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListVolumesRequest.

        :param offset: The offset of this ListVolumesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListVolumesRequest.

        :return: The sort_dir of this ListVolumesRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListVolumesRequest.

        :param sort_dir: The sort_dir of this ListVolumesRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def status(self):
        """Gets the status of this ListVolumesRequest.

        :return: The status of this ListVolumesRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListVolumesRequest.

        :param status: The status of this ListVolumesRequest.
        :type status: str
        """
        self._status = status

    @property
    def metadata(self):
        """Gets the metadata of this ListVolumesRequest.

        :return: The metadata of this ListVolumesRequest.
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ListVolumesRequest.

        :param metadata: The metadata of this ListVolumesRequest.
        :type metadata: str
        """
        self._metadata = metadata

    @property
    def availability_zone(self):
        """Gets the availability_zone of this ListVolumesRequest.

        :return: The availability_zone of this ListVolumesRequest.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this ListVolumesRequest.

        :param availability_zone: The availability_zone of this ListVolumesRequest.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def multiattach(self):
        """Gets the multiattach of this ListVolumesRequest.

        :return: The multiattach of this ListVolumesRequest.
        :rtype: bool
        """
        return self._multiattach

    @multiattach.setter
    def multiattach(self, multiattach):
        """Sets the multiattach of this ListVolumesRequest.

        :param multiattach: The multiattach of this ListVolumesRequest.
        :type multiattach: bool
        """
        self._multiattach = multiattach

    @property
    def service_type(self):
        """Gets the service_type of this ListVolumesRequest.

        :return: The service_type of this ListVolumesRequest.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this ListVolumesRequest.

        :param service_type: The service_type of this ListVolumesRequest.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def dedicated_storage_id(self):
        """Gets the dedicated_storage_id of this ListVolumesRequest.

        :return: The dedicated_storage_id of this ListVolumesRequest.
        :rtype: str
        """
        return self._dedicated_storage_id

    @dedicated_storage_id.setter
    def dedicated_storage_id(self, dedicated_storage_id):
        """Sets the dedicated_storage_id of this ListVolumesRequest.

        :param dedicated_storage_id: The dedicated_storage_id of this ListVolumesRequest.
        :type dedicated_storage_id: str
        """
        self._dedicated_storage_id = dedicated_storage_id

    @property
    def dedicated_storage_name(self):
        """Gets the dedicated_storage_name of this ListVolumesRequest.

        :return: The dedicated_storage_name of this ListVolumesRequest.
        :rtype: str
        """
        return self._dedicated_storage_name

    @dedicated_storage_name.setter
    def dedicated_storage_name(self, dedicated_storage_name):
        """Sets the dedicated_storage_name of this ListVolumesRequest.

        :param dedicated_storage_name: The dedicated_storage_name of this ListVolumesRequest.
        :type dedicated_storage_name: str
        """
        self._dedicated_storage_name = dedicated_storage_name

    @property
    def volume_type_id(self):
        """Gets the volume_type_id of this ListVolumesRequest.

        :return: The volume_type_id of this ListVolumesRequest.
        :rtype: str
        """
        return self._volume_type_id

    @volume_type_id.setter
    def volume_type_id(self, volume_type_id):
        """Sets the volume_type_id of this ListVolumesRequest.

        :param volume_type_id: The volume_type_id of this ListVolumesRequest.
        :type volume_type_id: str
        """
        self._volume_type_id = volume_type_id

    @property
    def id(self):
        """Gets the id of this ListVolumesRequest.

        :return: The id of this ListVolumesRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListVolumesRequest.

        :param id: The id of this ListVolumesRequest.
        :type id: str
        """
        self._id = id

    @property
    def ids(self):
        """Gets the ids of this ListVolumesRequest.

        :return: The ids of this ListVolumesRequest.
        :rtype: str
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this ListVolumesRequest.

        :param ids: The ids of this ListVolumesRequest.
        :type ids: str
        """
        self._ids = ids

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListVolumesRequest.

        :return: The enterprise_project_id of this ListVolumesRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListVolumesRequest.

        :param enterprise_project_id: The enterprise_project_id of this ListVolumesRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def server_id(self):
        """Gets the server_id of this ListVolumesRequest.

        :return: The server_id of this ListVolumesRequest.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this ListVolumesRequest.

        :param server_id: The server_id of this ListVolumesRequest.
        :type server_id: str
        """
        self._server_id = server_id

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
        if not isinstance(other, ListVolumesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
