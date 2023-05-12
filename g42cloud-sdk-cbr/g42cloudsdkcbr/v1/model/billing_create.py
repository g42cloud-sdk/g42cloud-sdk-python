# coding: utf-8

import six

from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class BillingCreate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cloud_type': 'str',
        'consistent_level': 'str',
        'object_type': 'str',
        'protect_type': 'str',
        'size': 'int',
        'charging_mode': 'str',
        'period_type': 'str',
        'period_num': 'int',
        'is_auto_renew': 'bool',
        'is_auto_pay': 'bool',
        'console_url': 'str',
        'is_multi_az': 'bool',
        'promotion_info': 'str',
        'purchase_mode': 'str',
        'order_id': 'str',
        'extra_info': 'BillbingCreateExtraInfo'
    }

    attribute_map = {
        'cloud_type': 'cloud_type',
        'consistent_level': 'consistent_level',
        'object_type': 'object_type',
        'protect_type': 'protect_type',
        'size': 'size',
        'charging_mode': 'charging_mode',
        'period_type': 'period_type',
        'period_num': 'period_num',
        'is_auto_renew': 'is_auto_renew',
        'is_auto_pay': 'is_auto_pay',
        'console_url': 'console_url',
        'is_multi_az': 'is_multi_az',
        'promotion_info': 'promotion_info',
        'purchase_mode': 'purchase_mode',
        'order_id': 'order_id',
        'extra_info': 'extra_info'
    }

    def __init__(self, cloud_type=None, consistent_level=None, object_type=None, protect_type=None, size=None, charging_mode=None, period_type=None, period_num=None, is_auto_renew=None, is_auto_pay=None, console_url=None, is_multi_az=None, promotion_info=None, purchase_mode=None, order_id=None, extra_info=None):
        """BillingCreate

        The model defined in g42cloud sdk

        :param cloud_type: The param of the BillingCreate
        :type cloud_type: str
        :param consistent_level: The param of the BillingCreate
        :type consistent_level: str
        :param object_type: The param of the BillingCreate
        :type object_type: str
        :param protect_type: The param of the BillingCreate
        :type protect_type: str
        :param size: The param of the BillingCreate
        :type size: int
        :param charging_mode: The param of the BillingCreate
        :type charging_mode: str
        :param period_type: The param of the BillingCreate
        :type period_type: str
        :param period_num: The param of the BillingCreate
        :type period_num: int
        :param is_auto_renew: The param of the BillingCreate
        :type is_auto_renew: bool
        :param is_auto_pay: The param of the BillingCreate
        :type is_auto_pay: bool
        :param console_url: The param of the BillingCreate
        :type console_url: str
        :param is_multi_az: The param of the BillingCreate
        :type is_multi_az: bool
        :param promotion_info: The param of the BillingCreate
        :type promotion_info: str
        :param purchase_mode: The param of the BillingCreate
        :type purchase_mode: str
        :param order_id: The param of the BillingCreate
        :type order_id: str
        :param extra_info: The param of the BillingCreate
        :type extra_info: :class:`g42cloudsdkcbr.v1.BillbingCreateExtraInfo`
        """
        
        

        self._cloud_type = None
        self._consistent_level = None
        self._object_type = None
        self._protect_type = None
        self._size = None
        self._charging_mode = None
        self._period_type = None
        self._period_num = None
        self._is_auto_renew = None
        self._is_auto_pay = None
        self._console_url = None
        self._is_multi_az = None
        self._promotion_info = None
        self._purchase_mode = None
        self._order_id = None
        self._extra_info = None
        self.discriminator = None

        if cloud_type is not None:
            self.cloud_type = cloud_type
        self.consistent_level = consistent_level
        self.object_type = object_type
        self.protect_type = protect_type
        self.size = size
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if period_type is not None:
            self.period_type = period_type
        if period_num is not None:
            self.period_num = period_num
        if is_auto_renew is not None:
            self.is_auto_renew = is_auto_renew
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay
        if console_url is not None:
            self.console_url = console_url
        if is_multi_az is not None:
            self.is_multi_az = is_multi_az
        if promotion_info is not None:
            self.promotion_info = promotion_info
        if purchase_mode is not None:
            self.purchase_mode = purchase_mode
        if order_id is not None:
            self.order_id = order_id
        if extra_info is not None:
            self.extra_info = extra_info

    @property
    def cloud_type(self):
        """Gets the cloud_type of this BillingCreate.

        :return: The cloud_type of this BillingCreate.
        :rtype: str
        """
        return self._cloud_type

    @cloud_type.setter
    def cloud_type(self, cloud_type):
        """Sets the cloud_type of this BillingCreate.

        :param cloud_type: The cloud_type of this BillingCreate.
        :type cloud_type: str
        """
        self._cloud_type = cloud_type

    @property
    def consistent_level(self):
        """Gets the consistent_level of this BillingCreate.

        :return: The consistent_level of this BillingCreate.
        :rtype: str
        """
        return self._consistent_level

    @consistent_level.setter
    def consistent_level(self, consistent_level):
        """Sets the consistent_level of this BillingCreate.

        :param consistent_level: The consistent_level of this BillingCreate.
        :type consistent_level: str
        """
        self._consistent_level = consistent_level

    @property
    def object_type(self):
        """Gets the object_type of this BillingCreate.

        :return: The object_type of this BillingCreate.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this BillingCreate.

        :param object_type: The object_type of this BillingCreate.
        :type object_type: str
        """
        self._object_type = object_type

    @property
    def protect_type(self):
        """Gets the protect_type of this BillingCreate.

        :return: The protect_type of this BillingCreate.
        :rtype: str
        """
        return self._protect_type

    @protect_type.setter
    def protect_type(self, protect_type):
        """Sets the protect_type of this BillingCreate.

        :param protect_type: The protect_type of this BillingCreate.
        :type protect_type: str
        """
        self._protect_type = protect_type

    @property
    def size(self):
        """Gets the size of this BillingCreate.

        :return: The size of this BillingCreate.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this BillingCreate.

        :param size: The size of this BillingCreate.
        :type size: int
        """
        self._size = size

    @property
    def charging_mode(self):
        """Gets the charging_mode of this BillingCreate.

        :return: The charging_mode of this BillingCreate.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        """Sets the charging_mode of this BillingCreate.

        :param charging_mode: The charging_mode of this BillingCreate.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def period_type(self):
        """Gets the period_type of this BillingCreate.

        :return: The period_type of this BillingCreate.
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        """Sets the period_type of this BillingCreate.

        :param period_type: The period_type of this BillingCreate.
        :type period_type: str
        """
        self._period_type = period_type

    @property
    def period_num(self):
        """Gets the period_num of this BillingCreate.

        :return: The period_num of this BillingCreate.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        """Sets the period_num of this BillingCreate.

        :param period_num: The period_num of this BillingCreate.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def is_auto_renew(self):
        """Gets the is_auto_renew of this BillingCreate.

        :return: The is_auto_renew of this BillingCreate.
        :rtype: bool
        """
        return self._is_auto_renew

    @is_auto_renew.setter
    def is_auto_renew(self, is_auto_renew):
        """Sets the is_auto_renew of this BillingCreate.

        :param is_auto_renew: The is_auto_renew of this BillingCreate.
        :type is_auto_renew: bool
        """
        self._is_auto_renew = is_auto_renew

    @property
    def is_auto_pay(self):
        """Gets the is_auto_pay of this BillingCreate.

        :return: The is_auto_pay of this BillingCreate.
        :rtype: bool
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        """Sets the is_auto_pay of this BillingCreate.

        :param is_auto_pay: The is_auto_pay of this BillingCreate.
        :type is_auto_pay: bool
        """
        self._is_auto_pay = is_auto_pay

    @property
    def console_url(self):
        """Gets the console_url of this BillingCreate.

        :return: The console_url of this BillingCreate.
        :rtype: str
        """
        return self._console_url

    @console_url.setter
    def console_url(self, console_url):
        """Sets the console_url of this BillingCreate.

        :param console_url: The console_url of this BillingCreate.
        :type console_url: str
        """
        self._console_url = console_url

    @property
    def is_multi_az(self):
        """Gets the is_multi_az of this BillingCreate.

        :return: The is_multi_az of this BillingCreate.
        :rtype: bool
        """
        return self._is_multi_az

    @is_multi_az.setter
    def is_multi_az(self, is_multi_az):
        """Sets the is_multi_az of this BillingCreate.

        :param is_multi_az: The is_multi_az of this BillingCreate.
        :type is_multi_az: bool
        """
        self._is_multi_az = is_multi_az

    @property
    def promotion_info(self):
        """Gets the promotion_info of this BillingCreate.

        :return: The promotion_info of this BillingCreate.
        :rtype: str
        """
        return self._promotion_info

    @promotion_info.setter
    def promotion_info(self, promotion_info):
        """Sets the promotion_info of this BillingCreate.

        :param promotion_info: The promotion_info of this BillingCreate.
        :type promotion_info: str
        """
        self._promotion_info = promotion_info

    @property
    def purchase_mode(self):
        """Gets the purchase_mode of this BillingCreate.

        :return: The purchase_mode of this BillingCreate.
        :rtype: str
        """
        return self._purchase_mode

    @purchase_mode.setter
    def purchase_mode(self, purchase_mode):
        """Sets the purchase_mode of this BillingCreate.

        :param purchase_mode: The purchase_mode of this BillingCreate.
        :type purchase_mode: str
        """
        self._purchase_mode = purchase_mode

    @property
    def order_id(self):
        """Gets the order_id of this BillingCreate.

        :return: The order_id of this BillingCreate.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this BillingCreate.

        :param order_id: The order_id of this BillingCreate.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def extra_info(self):
        """Gets the extra_info of this BillingCreate.

        :return: The extra_info of this BillingCreate.
        :rtype: :class:`g42cloudsdkcbr.v1.BillbingCreateExtraInfo`
        """
        return self._extra_info

    @extra_info.setter
    def extra_info(self, extra_info):
        """Sets the extra_info of this BillingCreate.

        :param extra_info: The extra_info of this BillingCreate.
        :type extra_info: :class:`g42cloudsdkcbr.v1.BillbingCreateExtraInfo`
        """
        self._extra_info = extra_info

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
        if not isinstance(other, BillingCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
