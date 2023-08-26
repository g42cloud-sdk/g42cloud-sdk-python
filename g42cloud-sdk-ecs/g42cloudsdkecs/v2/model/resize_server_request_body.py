# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResizeServerRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resize': 'ResizePrePaidServerOption',
        'dry_run': 'bool'
    }

    attribute_map = {
        'resize': 'resize',
        'dry_run': 'dry_run'
    }

    def __init__(self, resize=None, dry_run=None):
        """ResizeServerRequestBody

        The model defined in g42cloud sdk

        :param resize: The param of the ResizeServerRequestBody
        :type resize: :class:`g42cloudsdkecs.v2.ResizePrePaidServerOption`
        :param dry_run: The param of the ResizeServerRequestBody
        :type dry_run: bool
        """
        
        

        self._resize = None
        self._dry_run = None
        self.discriminator = None

        self.resize = resize
        if dry_run is not None:
            self.dry_run = dry_run

    @property
    def resize(self):
        """Gets the resize of this ResizeServerRequestBody.

        :return: The resize of this ResizeServerRequestBody.
        :rtype: :class:`g42cloudsdkecs.v2.ResizePrePaidServerOption`
        """
        return self._resize

    @resize.setter
    def resize(self, resize):
        """Sets the resize of this ResizeServerRequestBody.

        :param resize: The resize of this ResizeServerRequestBody.
        :type resize: :class:`g42cloudsdkecs.v2.ResizePrePaidServerOption`
        """
        self._resize = resize

    @property
    def dry_run(self):
        """Gets the dry_run of this ResizeServerRequestBody.

        :return: The dry_run of this ResizeServerRequestBody.
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        """Sets the dry_run of this ResizeServerRequestBody.

        :param dry_run: The dry_run of this ResizeServerRequestBody.
        :type dry_run: bool
        """
        self._dry_run = dry_run

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
        if not isinstance(other, ResizeServerRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
