# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class CertificateInfo:

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
        'id': 'str',
        'name': 'str',
        'private_key': 'str',
        'type': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'expire_time': 'str',
        'project_id': 'str',
        'enc_certificate': 'str',
        'enc_private_key': 'str'
    }

    attribute_map = {
        'admin_state_up': 'admin_state_up',
        'certificate': 'certificate',
        'description': 'description',
        'domain': 'domain',
        'id': 'id',
        'name': 'name',
        'private_key': 'private_key',
        'type': 'type',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'expire_time': 'expire_time',
        'project_id': 'project_id',
        'enc_certificate': 'enc_certificate',
        'enc_private_key': 'enc_private_key'
    }

    def __init__(self, admin_state_up=None, certificate=None, description=None, domain=None, id=None, name=None, private_key=None, type=None, created_at=None, updated_at=None, expire_time=None, project_id=None, enc_certificate=None, enc_private_key=None):
        """CertificateInfo

        The model defined in g42cloud sdk

        :param admin_state_up: The param of the CertificateInfo
        :type admin_state_up: bool
        :param certificate: The param of the CertificateInfo
        :type certificate: str
        :param description: The param of the CertificateInfo
        :type description: str
        :param domain: The param of the CertificateInfo
        :type domain: str
        :param id: The param of the CertificateInfo
        :type id: str
        :param name: The param of the CertificateInfo
        :type name: str
        :param private_key: The param of the CertificateInfo
        :type private_key: str
        :param type: The param of the CertificateInfo
        :type type: str
        :param created_at: The param of the CertificateInfo
        :type created_at: str
        :param updated_at: The param of the CertificateInfo
        :type updated_at: str
        :param expire_time: The param of the CertificateInfo
        :type expire_time: str
        :param project_id: The param of the CertificateInfo
        :type project_id: str
        :param enc_certificate: The param of the CertificateInfo
        :type enc_certificate: str
        :param enc_private_key: The param of the CertificateInfo
        :type enc_private_key: str
        """
        
        

        self._admin_state_up = None
        self._certificate = None
        self._description = None
        self._domain = None
        self._id = None
        self._name = None
        self._private_key = None
        self._type = None
        self._created_at = None
        self._updated_at = None
        self._expire_time = None
        self._project_id = None
        self._enc_certificate = None
        self._enc_private_key = None
        self.discriminator = None

        self.admin_state_up = admin_state_up
        self.certificate = certificate
        self.description = description
        self.domain = domain
        self.id = id
        self.name = name
        self.private_key = private_key
        self.type = type
        self.created_at = created_at
        self.updated_at = updated_at
        self.expire_time = expire_time
        self.project_id = project_id
        if enc_certificate is not None:
            self.enc_certificate = enc_certificate
        if enc_private_key is not None:
            self.enc_private_key = enc_private_key

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this CertificateInfo.

        :return: The admin_state_up of this CertificateInfo.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this CertificateInfo.

        :param admin_state_up: The admin_state_up of this CertificateInfo.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def certificate(self):
        """Gets the certificate of this CertificateInfo.

        :return: The certificate of this CertificateInfo.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this CertificateInfo.

        :param certificate: The certificate of this CertificateInfo.
        :type certificate: str
        """
        self._certificate = certificate

    @property
    def description(self):
        """Gets the description of this CertificateInfo.

        :return: The description of this CertificateInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CertificateInfo.

        :param description: The description of this CertificateInfo.
        :type description: str
        """
        self._description = description

    @property
    def domain(self):
        """Gets the domain of this CertificateInfo.

        :return: The domain of this CertificateInfo.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this CertificateInfo.

        :param domain: The domain of this CertificateInfo.
        :type domain: str
        """
        self._domain = domain

    @property
    def id(self):
        """Gets the id of this CertificateInfo.

        :return: The id of this CertificateInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CertificateInfo.

        :param id: The id of this CertificateInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this CertificateInfo.

        :return: The name of this CertificateInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CertificateInfo.

        :param name: The name of this CertificateInfo.
        :type name: str
        """
        self._name = name

    @property
    def private_key(self):
        """Gets the private_key of this CertificateInfo.

        :return: The private_key of this CertificateInfo.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this CertificateInfo.

        :param private_key: The private_key of this CertificateInfo.
        :type private_key: str
        """
        self._private_key = private_key

    @property
    def type(self):
        """Gets the type of this CertificateInfo.

        :return: The type of this CertificateInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CertificateInfo.

        :param type: The type of this CertificateInfo.
        :type type: str
        """
        self._type = type

    @property
    def created_at(self):
        """Gets the created_at of this CertificateInfo.

        :return: The created_at of this CertificateInfo.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CertificateInfo.

        :param created_at: The created_at of this CertificateInfo.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this CertificateInfo.

        :return: The updated_at of this CertificateInfo.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this CertificateInfo.

        :param updated_at: The updated_at of this CertificateInfo.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def expire_time(self):
        """Gets the expire_time of this CertificateInfo.

        :return: The expire_time of this CertificateInfo.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this CertificateInfo.

        :param expire_time: The expire_time of this CertificateInfo.
        :type expire_time: str
        """
        self._expire_time = expire_time

    @property
    def project_id(self):
        """Gets the project_id of this CertificateInfo.

        :return: The project_id of this CertificateInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CertificateInfo.

        :param project_id: The project_id of this CertificateInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def enc_certificate(self):
        """Gets the enc_certificate of this CertificateInfo.

        :return: The enc_certificate of this CertificateInfo.
        :rtype: str
        """
        return self._enc_certificate

    @enc_certificate.setter
    def enc_certificate(self, enc_certificate):
        """Sets the enc_certificate of this CertificateInfo.

        :param enc_certificate: The enc_certificate of this CertificateInfo.
        :type enc_certificate: str
        """
        self._enc_certificate = enc_certificate

    @property
    def enc_private_key(self):
        """Gets the enc_private_key of this CertificateInfo.

        :return: The enc_private_key of this CertificateInfo.
        :rtype: str
        """
        return self._enc_private_key

    @enc_private_key.setter
    def enc_private_key(self, enc_private_key):
        """Sets the enc_private_key of this CertificateInfo.

        :param enc_private_key: The enc_private_key of this CertificateInfo.
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
        if not isinstance(other, CertificateInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
