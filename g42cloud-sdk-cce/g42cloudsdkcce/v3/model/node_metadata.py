# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeMetadata:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'uid': 'str',
        'labels': 'dict(str, str)',
        'annotations': 'dict(str, str)',
        'creation_timestamp': 'str',
        'update_timestamp': 'str'
    }

    attribute_map = {
        'name': 'name',
        'uid': 'uid',
        'labels': 'labels',
        'annotations': 'annotations',
        'creation_timestamp': 'creationTimestamp',
        'update_timestamp': 'updateTimestamp'
    }

    def __init__(self, name=None, uid=None, labels=None, annotations=None, creation_timestamp=None, update_timestamp=None):
        """NodeMetadata

        The model defined in g42cloud sdk

        :param name: The param of the NodeMetadata
        :type name: str
        :param uid: The param of the NodeMetadata
        :type uid: str
        :param labels: The param of the NodeMetadata
        :type labels: dict(str, str)
        :param annotations: The param of the NodeMetadata
        :type annotations: dict(str, str)
        :param creation_timestamp: The param of the NodeMetadata
        :type creation_timestamp: str
        :param update_timestamp: The param of the NodeMetadata
        :type update_timestamp: str
        """
        
        

        self._name = None
        self._uid = None
        self._labels = None
        self._annotations = None
        self._creation_timestamp = None
        self._update_timestamp = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if uid is not None:
            self.uid = uid
        if labels is not None:
            self.labels = labels
        if annotations is not None:
            self.annotations = annotations
        if creation_timestamp is not None:
            self.creation_timestamp = creation_timestamp
        if update_timestamp is not None:
            self.update_timestamp = update_timestamp

    @property
    def name(self):
        """Gets the name of this NodeMetadata.

        :return: The name of this NodeMetadata.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NodeMetadata.

        :param name: The name of this NodeMetadata.
        :type name: str
        """
        self._name = name

    @property
    def uid(self):
        """Gets the uid of this NodeMetadata.

        :return: The uid of this NodeMetadata.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this NodeMetadata.

        :param uid: The uid of this NodeMetadata.
        :type uid: str
        """
        self._uid = uid

    @property
    def labels(self):
        """Gets the labels of this NodeMetadata.

        :return: The labels of this NodeMetadata.
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this NodeMetadata.

        :param labels: The labels of this NodeMetadata.
        :type labels: dict(str, str)
        """
        self._labels = labels

    @property
    def annotations(self):
        """Gets the annotations of this NodeMetadata.

        :return: The annotations of this NodeMetadata.
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this NodeMetadata.

        :param annotations: The annotations of this NodeMetadata.
        :type annotations: dict(str, str)
        """
        self._annotations = annotations

    @property
    def creation_timestamp(self):
        """Gets the creation_timestamp of this NodeMetadata.

        :return: The creation_timestamp of this NodeMetadata.
        :rtype: str
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp):
        """Sets the creation_timestamp of this NodeMetadata.

        :param creation_timestamp: The creation_timestamp of this NodeMetadata.
        :type creation_timestamp: str
        """
        self._creation_timestamp = creation_timestamp

    @property
    def update_timestamp(self):
        """Gets the update_timestamp of this NodeMetadata.

        :return: The update_timestamp of this NodeMetadata.
        :rtype: str
        """
        return self._update_timestamp

    @update_timestamp.setter
    def update_timestamp(self, update_timestamp):
        """Sets the update_timestamp of this NodeMetadata.

        :param update_timestamp: The update_timestamp of this NodeMetadata.
        :type update_timestamp: str
        """
        self._update_timestamp = update_timestamp

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
        if not isinstance(other, NodeMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
