# coding: utf-8

import six

from g42cloudsdkcore.sdk_response import SdkResponse
from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVpcPeeringsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'peerings': 'list[VpcPeering]',
        'peerings_links': 'list[NeutronPageLink]'
    }

    attribute_map = {
        'peerings': 'peerings',
        'peerings_links': 'peerings_links'
    }

    def __init__(self, peerings=None, peerings_links=None):
        """ListVpcPeeringsResponse

        The model defined in g42cloud sdk

        :param peerings: The param of the ListVpcPeeringsResponse
        :type peerings: list[:class:`g42cloudsdkvpc.v2.VpcPeering`]
        :param peerings_links: The param of the ListVpcPeeringsResponse
        :type peerings_links: list[:class:`g42cloudsdkvpc.v2.NeutronPageLink`]
        """
        
        super(ListVpcPeeringsResponse, self).__init__()

        self._peerings = None
        self._peerings_links = None
        self.discriminator = None

        if peerings is not None:
            self.peerings = peerings
        if peerings_links is not None:
            self.peerings_links = peerings_links

    @property
    def peerings(self):
        """Gets the peerings of this ListVpcPeeringsResponse.

        :return: The peerings of this ListVpcPeeringsResponse.
        :rtype: list[:class:`g42cloudsdkvpc.v2.VpcPeering`]
        """
        return self._peerings

    @peerings.setter
    def peerings(self, peerings):
        """Sets the peerings of this ListVpcPeeringsResponse.

        :param peerings: The peerings of this ListVpcPeeringsResponse.
        :type peerings: list[:class:`g42cloudsdkvpc.v2.VpcPeering`]
        """
        self._peerings = peerings

    @property
    def peerings_links(self):
        """Gets the peerings_links of this ListVpcPeeringsResponse.

        :return: The peerings_links of this ListVpcPeeringsResponse.
        :rtype: list[:class:`g42cloudsdkvpc.v2.NeutronPageLink`]
        """
        return self._peerings_links

    @peerings_links.setter
    def peerings_links(self, peerings_links):
        """Sets the peerings_links of this ListVpcPeeringsResponse.

        :param peerings_links: The peerings_links of this ListVpcPeeringsResponse.
        :type peerings_links: list[:class:`g42cloudsdkvpc.v2.NeutronPageLink`]
        """
        self._peerings_links = peerings_links

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
        if not isinstance(other, ListVpcPeeringsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
