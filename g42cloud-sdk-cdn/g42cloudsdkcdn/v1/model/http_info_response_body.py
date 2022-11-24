# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HttpInfoResponseBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'https_status': 'int',
        'cert_name': 'str',
        'certificate': 'str',
        'private_key': 'str',
        'certificate_type': 'int',
        'force_redirect_https': 'int',
        'force_redirect_config': 'ForceRedirect',
        'http2': 'int',
        'expiration_time': 'int'
    }

    attribute_map = {
        'https_status': 'https_status',
        'cert_name': 'cert_name',
        'certificate': 'certificate',
        'private_key': 'private_key',
        'certificate_type': 'certificate_type',
        'force_redirect_https': 'force_redirect_https',
        'force_redirect_config': 'force_redirect_config',
        'http2': 'http2',
        'expiration_time': 'expiration_time'
    }

    def __init__(self, https_status=None, cert_name=None, certificate=None, private_key=None, certificate_type=None, force_redirect_https=None, force_redirect_config=None, http2=None, expiration_time=None):
        """HttpInfoResponseBody

        The model defined in g42cloud sdk

        :param https_status: The param of the HttpInfoResponseBody
        :type https_status: int
        :param cert_name: The param of the HttpInfoResponseBody
        :type cert_name: str
        :param certificate: The param of the HttpInfoResponseBody
        :type certificate: str
        :param private_key: The param of the HttpInfoResponseBody
        :type private_key: str
        :param certificate_type: The param of the HttpInfoResponseBody
        :type certificate_type: int
        :param force_redirect_https: The param of the HttpInfoResponseBody
        :type force_redirect_https: int
        :param force_redirect_config: The param of the HttpInfoResponseBody
        :type force_redirect_config: :class:`g42cloudsdkcdn.v1.ForceRedirect`
        :param http2: The param of the HttpInfoResponseBody
        :type http2: int
        :param expiration_time: The param of the HttpInfoResponseBody
        :type expiration_time: int
        """
        
        

        self._https_status = None
        self._cert_name = None
        self._certificate = None
        self._private_key = None
        self._certificate_type = None
        self._force_redirect_https = None
        self._force_redirect_config = None
        self._http2 = None
        self._expiration_time = None
        self.discriminator = None

        if https_status is not None:
            self.https_status = https_status
        if cert_name is not None:
            self.cert_name = cert_name
        if certificate is not None:
            self.certificate = certificate
        if private_key is not None:
            self.private_key = private_key
        if certificate_type is not None:
            self.certificate_type = certificate_type
        if force_redirect_https is not None:
            self.force_redirect_https = force_redirect_https
        if force_redirect_config is not None:
            self.force_redirect_config = force_redirect_config
        if http2 is not None:
            self.http2 = http2
        if expiration_time is not None:
            self.expiration_time = expiration_time

    @property
    def https_status(self):
        """Gets the https_status of this HttpInfoResponseBody.

        :return: The https_status of this HttpInfoResponseBody.
        :rtype: int
        """
        return self._https_status

    @https_status.setter
    def https_status(self, https_status):
        """Sets the https_status of this HttpInfoResponseBody.

        :param https_status: The https_status of this HttpInfoResponseBody.
        :type https_status: int
        """
        self._https_status = https_status

    @property
    def cert_name(self):
        """Gets the cert_name of this HttpInfoResponseBody.

        :return: The cert_name of this HttpInfoResponseBody.
        :rtype: str
        """
        return self._cert_name

    @cert_name.setter
    def cert_name(self, cert_name):
        """Sets the cert_name of this HttpInfoResponseBody.

        :param cert_name: The cert_name of this HttpInfoResponseBody.
        :type cert_name: str
        """
        self._cert_name = cert_name

    @property
    def certificate(self):
        """Gets the certificate of this HttpInfoResponseBody.

        :return: The certificate of this HttpInfoResponseBody.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this HttpInfoResponseBody.

        :param certificate: The certificate of this HttpInfoResponseBody.
        :type certificate: str
        """
        self._certificate = certificate

    @property
    def private_key(self):
        """Gets the private_key of this HttpInfoResponseBody.

        :return: The private_key of this HttpInfoResponseBody.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this HttpInfoResponseBody.

        :param private_key: The private_key of this HttpInfoResponseBody.
        :type private_key: str
        """
        self._private_key = private_key

    @property
    def certificate_type(self):
        """Gets the certificate_type of this HttpInfoResponseBody.

        :return: The certificate_type of this HttpInfoResponseBody.
        :rtype: int
        """
        return self._certificate_type

    @certificate_type.setter
    def certificate_type(self, certificate_type):
        """Sets the certificate_type of this HttpInfoResponseBody.

        :param certificate_type: The certificate_type of this HttpInfoResponseBody.
        :type certificate_type: int
        """
        self._certificate_type = certificate_type

    @property
    def force_redirect_https(self):
        """Gets the force_redirect_https of this HttpInfoResponseBody.

        :return: The force_redirect_https of this HttpInfoResponseBody.
        :rtype: int
        """
        return self._force_redirect_https

    @force_redirect_https.setter
    def force_redirect_https(self, force_redirect_https):
        """Sets the force_redirect_https of this HttpInfoResponseBody.

        :param force_redirect_https: The force_redirect_https of this HttpInfoResponseBody.
        :type force_redirect_https: int
        """
        self._force_redirect_https = force_redirect_https

    @property
    def force_redirect_config(self):
        """Gets the force_redirect_config of this HttpInfoResponseBody.

        :return: The force_redirect_config of this HttpInfoResponseBody.
        :rtype: :class:`g42cloudsdkcdn.v1.ForceRedirect`
        """
        return self._force_redirect_config

    @force_redirect_config.setter
    def force_redirect_config(self, force_redirect_config):
        """Sets the force_redirect_config of this HttpInfoResponseBody.

        :param force_redirect_config: The force_redirect_config of this HttpInfoResponseBody.
        :type force_redirect_config: :class:`g42cloudsdkcdn.v1.ForceRedirect`
        """
        self._force_redirect_config = force_redirect_config

    @property
    def http2(self):
        """Gets the http2 of this HttpInfoResponseBody.

        :return: The http2 of this HttpInfoResponseBody.
        :rtype: int
        """
        return self._http2

    @http2.setter
    def http2(self, http2):
        """Sets the http2 of this HttpInfoResponseBody.

        :param http2: The http2 of this HttpInfoResponseBody.
        :type http2: int
        """
        self._http2 = http2

    @property
    def expiration_time(self):
        """Gets the expiration_time of this HttpInfoResponseBody.

        :return: The expiration_time of this HttpInfoResponseBody.
        :rtype: int
        """
        return self._expiration_time

    @expiration_time.setter
    def expiration_time(self, expiration_time):
        """Sets the expiration_time of this HttpInfoResponseBody.

        :param expiration_time: The expiration_time of this HttpInfoResponseBody.
        :type expiration_time: int
        """
        self._expiration_time = expiration_time

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
        if not isinstance(other, HttpInfoResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
