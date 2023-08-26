# coding: utf-8

import six

from g42cloudsdkcore.sdk_response import SdkResponse
from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListStatSummaryResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'summary': 'list[StatSummary]',
        'total': 'float',
        'stat_type': 'str'
    }

    attribute_map = {
        'summary': 'summary',
        'total': 'total',
        'stat_type': 'stat_type'
    }

    def __init__(self, summary=None, total=None, stat_type=None):
        """ListStatSummaryResponse

        The model defined in g42cloud sdk

        :param summary: The param of the ListStatSummaryResponse
        :type summary: list[:class:`g42cloudsdkmpc.v1.StatSummary`]
        :param total: The param of the ListStatSummaryResponse
        :type total: float
        :param stat_type: The param of the ListStatSummaryResponse
        :type stat_type: str
        """
        
        super(ListStatSummaryResponse, self).__init__()

        self._summary = None
        self._total = None
        self._stat_type = None
        self.discriminator = None

        if summary is not None:
            self.summary = summary
        if total is not None:
            self.total = total
        if stat_type is not None:
            self.stat_type = stat_type

    @property
    def summary(self):
        """Gets the summary of this ListStatSummaryResponse.

        :return: The summary of this ListStatSummaryResponse.
        :rtype: list[:class:`g42cloudsdkmpc.v1.StatSummary`]
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this ListStatSummaryResponse.

        :param summary: The summary of this ListStatSummaryResponse.
        :type summary: list[:class:`g42cloudsdkmpc.v1.StatSummary`]
        """
        self._summary = summary

    @property
    def total(self):
        """Gets the total of this ListStatSummaryResponse.

        :return: The total of this ListStatSummaryResponse.
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListStatSummaryResponse.

        :param total: The total of this ListStatSummaryResponse.
        :type total: float
        """
        self._total = total

    @property
    def stat_type(self):
        """Gets the stat_type of this ListStatSummaryResponse.

        :return: The stat_type of this ListStatSummaryResponse.
        :rtype: str
        """
        return self._stat_type

    @stat_type.setter
    def stat_type(self, stat_type):
        """Sets the stat_type of this ListStatSummaryResponse.

        :param stat_type: The stat_type of this ListStatSummaryResponse.
        :type stat_type: str
        """
        self._stat_type = stat_type

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
        if not isinstance(other, ListStatSummaryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
