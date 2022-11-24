# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HttpInfoRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cert_name': 'str',
        'https_status': 'int',
        'certificate': 'str',
        'private_key': 'str',
        'http2': 'int',
        'certificate_type': 'int',
        'force_redirect_https': 'int',
        'force_redirect_config': 'ForceRedirect'
    }

    attribute_map = {
        'cert_name': 'cert_name',
        'https_status': 'https_status',
        'certificate': 'certificate',
        'private_key': 'private_key',
        'http2': 'http2',
        'certificate_type': 'certificate_type',
        'force_redirect_https': 'force_redirect_https',
        'force_redirect_config': 'force_redirect_config'
    }

    def __init__(self, cert_name=None, https_status=None, certificate=None, private_key=None, http2=None, certificate_type=None, force_redirect_https=None, force_redirect_config=None):
        """HttpInfoRequestBody

        The model defined in g42cloud sdk

        :param cert_name: The param of the HttpInfoRequestBody
        :type cert_name: str
        :param https_status: The param of the HttpInfoRequestBody
        :type https_status: int
        :param certificate: The param of the HttpInfoRequestBody
        :type certificate: str
        :param private_key: The param of the HttpInfoRequestBody
        :type private_key: str
        :param http2: The param of the HttpInfoRequestBody
        :type http2: int
        :param certificate_type: The param of the HttpInfoRequestBody
        :type certificate_type: int
        :param force_redirect_https: The param of the HttpInfoRequestBody
        :type force_redirect_https: int
        :param force_redirect_config: The param of the HttpInfoRequestBody
        :type force_redirect_config: :class:`g42cloudsdkcdn.v1.ForceRedirect`
        """
        
        

        self._cert_name = None
        self._https_status = None
        self._certificate = None
        self._private_key = None
        self._http2 = None
        self._certificate_type = None
        self._force_redirect_https = None
        self._force_redirect_config = None
        self.discriminator = None

        self.cert_name = cert_name
        self.https_status = https_status
        if certificate is not None:
            self.certificate = certificate
        if private_key is not None:
            self.private_key = private_key
        if http2 is not None:
            self.http2 = http2
        if certificate_type is not None:
            self.certificate_type = certificate_type
        if force_redirect_https is not None:
            self.force_redirect_https = force_redirect_https
        if force_redirect_config is not None:
            self.force_redirect_config = force_redirect_config

    @property
    def cert_name(self):
        """Gets the cert_name of this HttpInfoRequestBody.

        :return: The cert_name of this HttpInfoRequestBody.
        :rtype: str
        """
        return self._cert_name

    @cert_name.setter
    def cert_name(self, cert_name):
        """Sets the cert_name of this HttpInfoRequestBody.

        :param cert_name: The cert_name of this HttpInfoRequestBody.
        :type cert_name: str
        """
        self._cert_name = cert_name

    @property
    def https_status(self):
        """Gets the https_status of this HttpInfoRequestBody.

        :return: The https_status of this HttpInfoRequestBody.
        :rtype: int
        """
        return self._https_status

    @https_status.setter
    def https_status(self, https_status):
        """Sets the https_status of this HttpInfoRequestBody.

        :param https_status: The https_status of this HttpInfoRequestBody.
        :type https_status: int
        """
        self._https_status = https_status

    @property
    def certificate(self):
        """Gets the certificate of this HttpInfoRequestBody.

        :return: The certificate of this HttpInfoRequestBody.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this HttpInfoRequestBody.

        :param certificate: The certificate of this HttpInfoRequestBody.
        :type certificate: str
        """
        self._certificate = certificate

    @property
    def private_key(self):
        """Gets the private_key of this HttpInfoRequestBody.

        :return: The private_key of this HttpInfoRequestBody.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this HttpInfoRequestBody.

        :param private_key: The private_key of this HttpInfoRequestBody.
        :type private_key: str
        """
        self._private_key = private_key

    @property
    def http2(self):
        """Gets the http2 of this HttpInfoRequestBody.

        :return: The http2 of this HttpInfoRequestBody.
        :rtype: int
        """
        return self._http2

    @http2.setter
    def http2(self, http2):
        """Sets the http2 of this HttpInfoRequestBody.

        :param http2: The http2 of this HttpInfoRequestBody.
        :type http2: int
        """
        self._http2 = http2

    @property
    def certificate_type(self):
        """Gets the certificate_type of this HttpInfoRequestBody.

        :return: The certificate_type of this HttpInfoRequestBody.
        :rtype: int
        """
        return self._certificate_type

    @certificate_type.setter
    def certificate_type(self, certificate_type):
        """Sets the certificate_type of this HttpInfoRequestBody.

        :param certificate_type: The certificate_type of this HttpInfoRequestBody.
        :type certificate_type: int
        """
        self._certificate_type = certificate_type

    @property
    def force_redirect_https(self):
        """Gets the force_redirect_https of this HttpInfoRequestBody.

        :return: The force_redirect_https of this HttpInfoRequestBody.
        :rtype: int
        """
        return self._force_redirect_https

    @force_redirect_https.setter
    def force_redirect_https(self, force_redirect_https):
        """Sets the force_redirect_https of this HttpInfoRequestBody.

        :param force_redirect_https: The force_redirect_https of this HttpInfoRequestBody.
        :type force_redirect_https: int
        """
        self._force_redirect_https = force_redirect_https

    @property
    def force_redirect_config(self):
        """Gets the force_redirect_config of this HttpInfoRequestBody.

        :return: The force_redirect_config of this HttpInfoRequestBody.
        :rtype: :class:`g42cloudsdkcdn.v1.ForceRedirect`
        """
        return self._force_redirect_config

    @force_redirect_config.setter
    def force_redirect_config(self, force_redirect_config):
        """Sets the force_redirect_config of this HttpInfoRequestBody.

        :param force_redirect_config: The force_redirect_config of this HttpInfoRequestBody.
        :type force_redirect_config: :class:`g42cloudsdkcdn.v1.ForceRedirect`
        """
        self._force_redirect_config = force_redirect_config

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
        if not isinstance(other, HttpInfoRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
