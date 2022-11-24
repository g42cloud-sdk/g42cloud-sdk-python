# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeServerOsWithCloudInitOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'adminpass': 'str',
        'keyname': 'str',
        'userid': 'str',
        'imageid': 'str',
        'metadata': 'ChangeSeversOsMetadata',
        'mode': 'str'
    }

    attribute_map = {
        'adminpass': 'adminpass',
        'keyname': 'keyname',
        'userid': 'userid',
        'imageid': 'imageid',
        'metadata': 'metadata',
        'mode': 'mode'
    }

    def __init__(self, adminpass=None, keyname=None, userid=None, imageid=None, metadata=None, mode=None):
        """ChangeServerOsWithCloudInitOption

        The model defined in g42cloud sdk

        :param adminpass: The param of the ChangeServerOsWithCloudInitOption
        :type adminpass: str
        :param keyname: The param of the ChangeServerOsWithCloudInitOption
        :type keyname: str
        :param userid: The param of the ChangeServerOsWithCloudInitOption
        :type userid: str
        :param imageid: The param of the ChangeServerOsWithCloudInitOption
        :type imageid: str
        :param metadata: The param of the ChangeServerOsWithCloudInitOption
        :type metadata: :class:`g42cloudsdkecs.v2.ChangeSeversOsMetadata`
        :param mode: The param of the ChangeServerOsWithCloudInitOption
        :type mode: str
        """
        
        

        self._adminpass = None
        self._keyname = None
        self._userid = None
        self._imageid = None
        self._metadata = None
        self._mode = None
        self.discriminator = None

        if adminpass is not None:
            self.adminpass = adminpass
        if keyname is not None:
            self.keyname = keyname
        if userid is not None:
            self.userid = userid
        self.imageid = imageid
        if metadata is not None:
            self.metadata = metadata
        if mode is not None:
            self.mode = mode

    @property
    def adminpass(self):
        """Gets the adminpass of this ChangeServerOsWithCloudInitOption.

        :return: The adminpass of this ChangeServerOsWithCloudInitOption.
        :rtype: str
        """
        return self._adminpass

    @adminpass.setter
    def adminpass(self, adminpass):
        """Sets the adminpass of this ChangeServerOsWithCloudInitOption.

        :param adminpass: The adminpass of this ChangeServerOsWithCloudInitOption.
        :type adminpass: str
        """
        self._adminpass = adminpass

    @property
    def keyname(self):
        """Gets the keyname of this ChangeServerOsWithCloudInitOption.

        :return: The keyname of this ChangeServerOsWithCloudInitOption.
        :rtype: str
        """
        return self._keyname

    @keyname.setter
    def keyname(self, keyname):
        """Sets the keyname of this ChangeServerOsWithCloudInitOption.

        :param keyname: The keyname of this ChangeServerOsWithCloudInitOption.
        :type keyname: str
        """
        self._keyname = keyname

    @property
    def userid(self):
        """Gets the userid of this ChangeServerOsWithCloudInitOption.

        :return: The userid of this ChangeServerOsWithCloudInitOption.
        :rtype: str
        """
        return self._userid

    @userid.setter
    def userid(self, userid):
        """Sets the userid of this ChangeServerOsWithCloudInitOption.

        :param userid: The userid of this ChangeServerOsWithCloudInitOption.
        :type userid: str
        """
        self._userid = userid

    @property
    def imageid(self):
        """Gets the imageid of this ChangeServerOsWithCloudInitOption.

        :return: The imageid of this ChangeServerOsWithCloudInitOption.
        :rtype: str
        """
        return self._imageid

    @imageid.setter
    def imageid(self, imageid):
        """Sets the imageid of this ChangeServerOsWithCloudInitOption.

        :param imageid: The imageid of this ChangeServerOsWithCloudInitOption.
        :type imageid: str
        """
        self._imageid = imageid

    @property
    def metadata(self):
        """Gets the metadata of this ChangeServerOsWithCloudInitOption.

        :return: The metadata of this ChangeServerOsWithCloudInitOption.
        :rtype: :class:`g42cloudsdkecs.v2.ChangeSeversOsMetadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ChangeServerOsWithCloudInitOption.

        :param metadata: The metadata of this ChangeServerOsWithCloudInitOption.
        :type metadata: :class:`g42cloudsdkecs.v2.ChangeSeversOsMetadata`
        """
        self._metadata = metadata

    @property
    def mode(self):
        """Gets the mode of this ChangeServerOsWithCloudInitOption.

        :return: The mode of this ChangeServerOsWithCloudInitOption.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this ChangeServerOsWithCloudInitOption.

        :param mode: The mode of this ChangeServerOsWithCloudInitOption.
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
        if not isinstance(other, ChangeServerOsWithCloudInitOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
