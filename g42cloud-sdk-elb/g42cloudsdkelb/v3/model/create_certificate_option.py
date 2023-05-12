# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCertificateOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'admin_state_up': 'bool',
        'certificate': 'str',
        'description': 'str',
        'domain': 'str',
        'name': 'str',
        'private_key': 'str',
        'project_id': 'str',
        'type': 'str',
        'enterprise_project_id': 'str',
        'enc_certificate': 'str',
        'enc_private_key': 'str'
    }

    attribute_map = {
        'admin_state_up': 'admin_state_up',
        'certificate': 'certificate',
        'description': 'description',
        'domain': 'domain',
        'name': 'name',
        'private_key': 'private_key',
        'project_id': 'project_id',
        'type': 'type',
        'enterprise_project_id': 'enterprise_project_id',
        'enc_certificate': 'enc_certificate',
        'enc_private_key': 'enc_private_key'
    }

    def __init__(self, admin_state_up=None, certificate=None, description=None, domain=None, name=None, private_key=None, project_id=None, type=None, enterprise_project_id=None, enc_certificate=None, enc_private_key=None):
        """CreateCertificateOption

        The model defined in g42cloud sdk

        :param admin_state_up: The param of the CreateCertificateOption
        :type admin_state_up: bool
        :param certificate: The param of the CreateCertificateOption
        :type certificate: str
        :param description: The param of the CreateCertificateOption
        :type description: str
        :param domain: The param of the CreateCertificateOption
        :type domain: str
        :param name: The param of the CreateCertificateOption
        :type name: str
        :param private_key: The param of the CreateCertificateOption
        :type private_key: str
        :param project_id: The param of the CreateCertificateOption
        :type project_id: str
        :param type: The param of the CreateCertificateOption
        :type type: str
        :param enterprise_project_id: The param of the CreateCertificateOption
        :type enterprise_project_id: str
        :param enc_certificate: The param of the CreateCertificateOption
        :type enc_certificate: str
        :param enc_private_key: The param of the CreateCertificateOption
        :type enc_private_key: str
        """
        
        

        self._admin_state_up = None
        self._certificate = None
        self._description = None
        self._domain = None
        self._name = None
        self._private_key = None
        self._project_id = None
        self._type = None
        self._enterprise_project_id = None
        self._enc_certificate = None
        self._enc_private_key = None
        self.discriminator = None

        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        self.certificate = certificate
        if description is not None:
            self.description = description
        if domain is not None:
            self.domain = domain
        if name is not None:
            self.name = name
        if private_key is not None:
            self.private_key = private_key
        if project_id is not None:
            self.project_id = project_id
        if type is not None:
            self.type = type
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if enc_certificate is not None:
            self.enc_certificate = enc_certificate
        if enc_private_key is not None:
            self.enc_private_key = enc_private_key

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this CreateCertificateOption.

        :return: The admin_state_up of this CreateCertificateOption.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this CreateCertificateOption.

        :param admin_state_up: The admin_state_up of this CreateCertificateOption.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def certificate(self):
        """Gets the certificate of this CreateCertificateOption.

        :return: The certificate of this CreateCertificateOption.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this CreateCertificateOption.

        :param certificate: The certificate of this CreateCertificateOption.
        :type certificate: str
        """
        self._certificate = certificate

    @property
    def description(self):
        """Gets the description of this CreateCertificateOption.

        :return: The description of this CreateCertificateOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateCertificateOption.

        :param description: The description of this CreateCertificateOption.
        :type description: str
        """
        self._description = description

    @property
    def domain(self):
        """Gets the domain of this CreateCertificateOption.

        :return: The domain of this CreateCertificateOption.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this CreateCertificateOption.

        :param domain: The domain of this CreateCertificateOption.
        :type domain: str
        """
        self._domain = domain

    @property
    def name(self):
        """Gets the name of this CreateCertificateOption.

        :return: The name of this CreateCertificateOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateCertificateOption.

        :param name: The name of this CreateCertificateOption.
        :type name: str
        """
        self._name = name

    @property
    def private_key(self):
        """Gets the private_key of this CreateCertificateOption.

        :return: The private_key of this CreateCertificateOption.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this CreateCertificateOption.

        :param private_key: The private_key of this CreateCertificateOption.
        :type private_key: str
        """
        self._private_key = private_key

    @property
    def project_id(self):
        """Gets the project_id of this CreateCertificateOption.

        :return: The project_id of this CreateCertificateOption.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreateCertificateOption.

        :param project_id: The project_id of this CreateCertificateOption.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def type(self):
        """Gets the type of this CreateCertificateOption.

        :return: The type of this CreateCertificateOption.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateCertificateOption.

        :param type: The type of this CreateCertificateOption.
        :type type: str
        """
        self._type = type

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateCertificateOption.

        :return: The enterprise_project_id of this CreateCertificateOption.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateCertificateOption.

        :param enterprise_project_id: The enterprise_project_id of this CreateCertificateOption.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def enc_certificate(self):
        """Gets the enc_certificate of this CreateCertificateOption.

        :return: The enc_certificate of this CreateCertificateOption.
        :rtype: str
        """
        return self._enc_certificate

    @enc_certificate.setter
    def enc_certificate(self, enc_certificate):
        """Sets the enc_certificate of this CreateCertificateOption.

        :param enc_certificate: The enc_certificate of this CreateCertificateOption.
        :type enc_certificate: str
        """
        self._enc_certificate = enc_certificate

    @property
    def enc_private_key(self):
        """Gets the enc_private_key of this CreateCertificateOption.

        :return: The enc_private_key of this CreateCertificateOption.
        :rtype: str
        """
        return self._enc_private_key

    @enc_private_key.setter
    def enc_private_key(self, enc_private_key):
        """Sets the enc_private_key of this CreateCertificateOption.

        :param enc_private_key: The enc_private_key of this CreateCertificateOption.
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
        if not isinstance(other, CreateCertificateOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
