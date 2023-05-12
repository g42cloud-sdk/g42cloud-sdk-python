# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCertificateOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'certificate': 'str',
        'description': 'str',
        'name': 'str',
        'private_key': 'str',
        'domain': 'str',
        'enc_certificate': 'str',
        'enc_private_key': 'str'
    }

    attribute_map = {
        'certificate': 'certificate',
        'description': 'description',
        'name': 'name',
        'private_key': 'private_key',
        'domain': 'domain',
        'enc_certificate': 'enc_certificate',
        'enc_private_key': 'enc_private_key'
    }

    def __init__(self, certificate=None, description=None, name=None, private_key=None, domain=None, enc_certificate=None, enc_private_key=None):
        """UpdateCertificateOption

        The model defined in g42cloud sdk

        :param certificate: The param of the UpdateCertificateOption
        :type certificate: str
        :param description: The param of the UpdateCertificateOption
        :type description: str
        :param name: The param of the UpdateCertificateOption
        :type name: str
        :param private_key: The param of the UpdateCertificateOption
        :type private_key: str
        :param domain: The param of the UpdateCertificateOption
        :type domain: str
        :param enc_certificate: The param of the UpdateCertificateOption
        :type enc_certificate: str
        :param enc_private_key: The param of the UpdateCertificateOption
        :type enc_private_key: str
        """
        
        

        self._certificate = None
        self._description = None
        self._name = None
        self._private_key = None
        self._domain = None
        self._enc_certificate = None
        self._enc_private_key = None
        self.discriminator = None

        if certificate is not None:
            self.certificate = certificate
        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if private_key is not None:
            self.private_key = private_key
        if domain is not None:
            self.domain = domain
        if enc_certificate is not None:
            self.enc_certificate = enc_certificate
        if enc_private_key is not None:
            self.enc_private_key = enc_private_key

    @property
    def certificate(self):
        """Gets the certificate of this UpdateCertificateOption.

        :return: The certificate of this UpdateCertificateOption.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this UpdateCertificateOption.

        :param certificate: The certificate of this UpdateCertificateOption.
        :type certificate: str
        """
        self._certificate = certificate

    @property
    def description(self):
        """Gets the description of this UpdateCertificateOption.

        :return: The description of this UpdateCertificateOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateCertificateOption.

        :param description: The description of this UpdateCertificateOption.
        :type description: str
        """
        self._description = description

    @property
    def name(self):
        """Gets the name of this UpdateCertificateOption.

        :return: The name of this UpdateCertificateOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateCertificateOption.

        :param name: The name of this UpdateCertificateOption.
        :type name: str
        """
        self._name = name

    @property
    def private_key(self):
        """Gets the private_key of this UpdateCertificateOption.

        :return: The private_key of this UpdateCertificateOption.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this UpdateCertificateOption.

        :param private_key: The private_key of this UpdateCertificateOption.
        :type private_key: str
        """
        self._private_key = private_key

    @property
    def domain(self):
        """Gets the domain of this UpdateCertificateOption.

        :return: The domain of this UpdateCertificateOption.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this UpdateCertificateOption.

        :param domain: The domain of this UpdateCertificateOption.
        :type domain: str
        """
        self._domain = domain

    @property
    def enc_certificate(self):
        """Gets the enc_certificate of this UpdateCertificateOption.

        :return: The enc_certificate of this UpdateCertificateOption.
        :rtype: str
        """
        return self._enc_certificate

    @enc_certificate.setter
    def enc_certificate(self, enc_certificate):
        """Sets the enc_certificate of this UpdateCertificateOption.

        :param enc_certificate: The enc_certificate of this UpdateCertificateOption.
        :type enc_certificate: str
        """
        self._enc_certificate = enc_certificate

    @property
    def enc_private_key(self):
        """Gets the enc_private_key of this UpdateCertificateOption.

        :return: The enc_private_key of this UpdateCertificateOption.
        :rtype: str
        """
        return self._enc_private_key

    @enc_private_key.setter
    def enc_private_key(self, enc_private_key):
        """Sets the enc_private_key of this UpdateCertificateOption.

        :param enc_private_key: The enc_private_key of this UpdateCertificateOption.
        :type enc_private_key: str
        """
        self._enc_private_key = enc_private_key

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
        if not isinstance(other, UpdateCertificateOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
