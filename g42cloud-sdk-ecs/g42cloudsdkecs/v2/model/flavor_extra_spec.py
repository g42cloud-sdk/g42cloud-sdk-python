# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlavorExtraSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ecsperformancetype': 'str',
        'hwnuma_nodes': 'str',
        'resource_type': 'str',
        'hpet_support': 'str',
        'instance_vnictype': 'str',
        'instance_vnicinstance_bandwidth': 'str',
        'instance_vnicmax_count': 'str',
        'quotalocal_disk': 'str',
        'quotanvme_ssd': 'str',
        'extra_speciopersistent_grant': 'str',
        'ecsgeneration': 'str',
        'ecsvirtualization_env_types': 'str',
        'pci_passthroughenable_gpu': 'str',
        'pci_passthroughgpu_specs': 'str',
        'pci_passthroughalias': 'str',
        'condoperationstatus': 'str',
        'condoperationaz': 'str',
        'quotamax_rate': 'str',
        'quotamin_rate': 'str',
        'quotamax_pps': 'str',
        'condoperationcharge': 'str',
        'condoperationchargestop': 'str',
        'condspotoperationaz': 'str',
        'condoperationroles': 'str',
        'condspotoperationstatus': 'str',
        'condnetwork': 'str',
        'condstorage': 'str',
        'condcomputelive_resizable': 'str',
        'condcompute': 'str',
        'infogpuname': 'str',
        'infocpuname': 'str',
        'quotagpu': 'str',
        'ecsinstance_architecture': 'str'
    }

    attribute_map = {
        'ecsperformancetype': 'ecs:performancetype',
        'hwnuma_nodes': 'hw:numa_nodes',
        'resource_type': 'resource_type',
        'hpet_support': 'hpet_support',
        'instance_vnictype': 'instance_vnic:type',
        'instance_vnicinstance_bandwidth': 'instance_vnic:instance_bandwidth',
        'instance_vnicmax_count': 'instance_vnic:max_count',
        'quotalocal_disk': 'quota:local_disk',
        'quotanvme_ssd': 'quota:nvme_ssd',
        'extra_speciopersistent_grant': 'extra_spec:io:persistent_grant',
        'ecsgeneration': 'ecs:generation',
        'ecsvirtualization_env_types': 'ecs:virtualization_env_types',
        'pci_passthroughenable_gpu': 'pci_passthrough:enable_gpu',
        'pci_passthroughgpu_specs': 'pci_passthrough:gpu_specs',
        'pci_passthroughalias': 'pci_passthrough:alias',
        'condoperationstatus': 'cond:operation:status',
        'condoperationaz': 'cond:operation:az',
        'quotamax_rate': 'quota:max_rate',
        'quotamin_rate': 'quota:min_rate',
        'quotamax_pps': 'quota:max_pps',
        'condoperationcharge': 'cond:operation:charge',
        'condoperationchargestop': 'cond:operation:charge:stop',
        'condspotoperationaz': 'cond:spot:operation:az',
        'condoperationroles': 'cond:operation:roles',
        'condspotoperationstatus': 'cond:spot:operation:status',
        'condnetwork': 'cond:network',
        'condstorage': 'cond:storage',
        'condcomputelive_resizable': 'cond:compute:live_resizable',
        'condcompute': 'cond:compute',
        'infogpuname': 'info:gpu:name',
        'infocpuname': 'info:cpu:name',
        'quotagpu': 'quota:gpu',
        'ecsinstance_architecture': 'ecs:instance_architecture'
    }

    def __init__(self, ecsperformancetype=None, hwnuma_nodes=None, resource_type=None, hpet_support=None, instance_vnictype=None, instance_vnicinstance_bandwidth=None, instance_vnicmax_count=None, quotalocal_disk=None, quotanvme_ssd=None, extra_speciopersistent_grant=None, ecsgeneration=None, ecsvirtualization_env_types=None, pci_passthroughenable_gpu=None, pci_passthroughgpu_specs=None, pci_passthroughalias=None, condoperationstatus=None, condoperationaz=None, quotamax_rate=None, quotamin_rate=None, quotamax_pps=None, condoperationcharge=None, condoperationchargestop=None, condspotoperationaz=None, condoperationroles=None, condspotoperationstatus=None, condnetwork=None, condstorage=None, condcomputelive_resizable=None, condcompute=None, infogpuname=None, infocpuname=None, quotagpu=None, ecsinstance_architecture=None):
        """FlavorExtraSpec

        The model defined in g42cloud sdk

        :param ecsperformancetype: The param of the FlavorExtraSpec
        :type ecsperformancetype: str
        :param hwnuma_nodes: The param of the FlavorExtraSpec
        :type hwnuma_nodes: str
        :param resource_type: The param of the FlavorExtraSpec
        :type resource_type: str
        :param hpet_support: The param of the FlavorExtraSpec
        :type hpet_support: str
        :param instance_vnictype: The param of the FlavorExtraSpec
        :type instance_vnictype: str
        :param instance_vnicinstance_bandwidth: The param of the FlavorExtraSpec
        :type instance_vnicinstance_bandwidth: str
        :param instance_vnicmax_count: The param of the FlavorExtraSpec
        :type instance_vnicmax_count: str
        :param quotalocal_disk: The param of the FlavorExtraSpec
        :type quotalocal_disk: str
        :param quotanvme_ssd: The param of the FlavorExtraSpec
        :type quotanvme_ssd: str
        :param extra_speciopersistent_grant: The param of the FlavorExtraSpec
        :type extra_speciopersistent_grant: str
        :param ecsgeneration: The param of the FlavorExtraSpec
        :type ecsgeneration: str
        :param ecsvirtualization_env_types: The param of the FlavorExtraSpec
        :type ecsvirtualization_env_types: str
        :param pci_passthroughenable_gpu: The param of the FlavorExtraSpec
        :type pci_passthroughenable_gpu: str
        :param pci_passthroughgpu_specs: The param of the FlavorExtraSpec
        :type pci_passthroughgpu_specs: str
        :param pci_passthroughalias: The param of the FlavorExtraSpec
        :type pci_passthroughalias: str
        :param condoperationstatus: The param of the FlavorExtraSpec
        :type condoperationstatus: str
        :param condoperationaz: The param of the FlavorExtraSpec
        :type condoperationaz: str
        :param quotamax_rate: The param of the FlavorExtraSpec
        :type quotamax_rate: str
        :param quotamin_rate: The param of the FlavorExtraSpec
        :type quotamin_rate: str
        :param quotamax_pps: The param of the FlavorExtraSpec
        :type quotamax_pps: str
        :param condoperationcharge: The param of the FlavorExtraSpec
        :type condoperationcharge: str
        :param condoperationchargestop: The param of the FlavorExtraSpec
        :type condoperationchargestop: str
        :param condspotoperationaz: The param of the FlavorExtraSpec
        :type condspotoperationaz: str
        :param condoperationroles: The param of the FlavorExtraSpec
        :type condoperationroles: str
        :param condspotoperationstatus: The param of the FlavorExtraSpec
        :type condspotoperationstatus: str
        :param condnetwork: The param of the FlavorExtraSpec
        :type condnetwork: str
        :param condstorage: The param of the FlavorExtraSpec
        :type condstorage: str
        :param condcomputelive_resizable: The param of the FlavorExtraSpec
        :type condcomputelive_resizable: str
        :param condcompute: The param of the FlavorExtraSpec
        :type condcompute: str
        :param infogpuname: The param of the FlavorExtraSpec
        :type infogpuname: str
        :param infocpuname: The param of the FlavorExtraSpec
        :type infocpuname: str
        :param quotagpu: The param of the FlavorExtraSpec
        :type quotagpu: str
        :param ecsinstance_architecture: The param of the FlavorExtraSpec
        :type ecsinstance_architecture: str
        """
        
        

        self._ecsperformancetype = None
        self._hwnuma_nodes = None
        self._resource_type = None
        self._hpet_support = None
        self._instance_vnictype = None
        self._instance_vnicinstance_bandwidth = None
        self._instance_vnicmax_count = None
        self._quotalocal_disk = None
        self._quotanvme_ssd = None
        self._extra_speciopersistent_grant = None
        self._ecsgeneration = None
        self._ecsvirtualization_env_types = None
        self._pci_passthroughenable_gpu = None
        self._pci_passthroughgpu_specs = None
        self._pci_passthroughalias = None
        self._condoperationstatus = None
        self._condoperationaz = None
        self._quotamax_rate = None
        self._quotamin_rate = None
        self._quotamax_pps = None
        self._condoperationcharge = None
        self._condoperationchargestop = None
        self._condspotoperationaz = None
        self._condoperationroles = None
        self._condspotoperationstatus = None
        self._condnetwork = None
        self._condstorage = None
        self._condcomputelive_resizable = None
        self._condcompute = None
        self._infogpuname = None
        self._infocpuname = None
        self._quotagpu = None
        self._ecsinstance_architecture = None
        self.discriminator = None

        if ecsperformancetype is not None:
            self.ecsperformancetype = ecsperformancetype
        if hwnuma_nodes is not None:
            self.hwnuma_nodes = hwnuma_nodes
        if resource_type is not None:
            self.resource_type = resource_type
        if hpet_support is not None:
            self.hpet_support = hpet_support
        if instance_vnictype is not None:
            self.instance_vnictype = instance_vnictype
        if instance_vnicinstance_bandwidth is not None:
            self.instance_vnicinstance_bandwidth = instance_vnicinstance_bandwidth
        if instance_vnicmax_count is not None:
            self.instance_vnicmax_count = instance_vnicmax_count
        if quotalocal_disk is not None:
            self.quotalocal_disk = quotalocal_disk
        if quotanvme_ssd is not None:
            self.quotanvme_ssd = quotanvme_ssd
        if extra_speciopersistent_grant is not None:
            self.extra_speciopersistent_grant = extra_speciopersistent_grant
        if ecsgeneration is not None:
            self.ecsgeneration = ecsgeneration
        if ecsvirtualization_env_types is not None:
            self.ecsvirtualization_env_types = ecsvirtualization_env_types
        if pci_passthroughenable_gpu is not None:
            self.pci_passthroughenable_gpu = pci_passthroughenable_gpu
        if pci_passthroughgpu_specs is not None:
            self.pci_passthroughgpu_specs = pci_passthroughgpu_specs
        if pci_passthroughalias is not None:
            self.pci_passthroughalias = pci_passthroughalias
        if condoperationstatus is not None:
            self.condoperationstatus = condoperationstatus
        if condoperationaz is not None:
            self.condoperationaz = condoperationaz
        if quotamax_rate is not None:
            self.quotamax_rate = quotamax_rate
        if quotamin_rate is not None:
            self.quotamin_rate = quotamin_rate
        if quotamax_pps is not None:
            self.quotamax_pps = quotamax_pps
        if condoperationcharge is not None:
            self.condoperationcharge = condoperationcharge
        if condoperationchargestop is not None:
            self.condoperationchargestop = condoperationchargestop
        if condspotoperationaz is not None:
            self.condspotoperationaz = condspotoperationaz
        if condoperationroles is not None:
            self.condoperationroles = condoperationroles
        if condspotoperationstatus is not None:
            self.condspotoperationstatus = condspotoperationstatus
        if condnetwork is not None:
            self.condnetwork = condnetwork
        if condstorage is not None:
            self.condstorage = condstorage
        if condcomputelive_resizable is not None:
            self.condcomputelive_resizable = condcomputelive_resizable
        if condcompute is not None:
            self.condcompute = condcompute
        if infogpuname is not None:
            self.infogpuname = infogpuname
        if infocpuname is not None:
            self.infocpuname = infocpuname
        if quotagpu is not None:
            self.quotagpu = quotagpu
        if ecsinstance_architecture is not None:
            self.ecsinstance_architecture = ecsinstance_architecture

    @property
    def ecsperformancetype(self):
        """Gets the ecsperformancetype of this FlavorExtraSpec.

        :return: The ecsperformancetype of this FlavorExtraSpec.
        :rtype: str
        """
        return self._ecsperformancetype

    @ecsperformancetype.setter
    def ecsperformancetype(self, ecsperformancetype):
        """Sets the ecsperformancetype of this FlavorExtraSpec.

        :param ecsperformancetype: The ecsperformancetype of this FlavorExtraSpec.
        :type ecsperformancetype: str
        """
        self._ecsperformancetype = ecsperformancetype

    @property
    def hwnuma_nodes(self):
        """Gets the hwnuma_nodes of this FlavorExtraSpec.

        :return: The hwnuma_nodes of this FlavorExtraSpec.
        :rtype: str
        """
        return self._hwnuma_nodes

    @hwnuma_nodes.setter
    def hwnuma_nodes(self, hwnuma_nodes):
        """Sets the hwnuma_nodes of this FlavorExtraSpec.

        :param hwnuma_nodes: The hwnuma_nodes of this FlavorExtraSpec.
        :type hwnuma_nodes: str
        """
        self._hwnuma_nodes = hwnuma_nodes

    @property
    def resource_type(self):
        """Gets the resource_type of this FlavorExtraSpec.

        :return: The resource_type of this FlavorExtraSpec.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this FlavorExtraSpec.

        :param resource_type: The resource_type of this FlavorExtraSpec.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def hpet_support(self):
        """Gets the hpet_support of this FlavorExtraSpec.

        :return: The hpet_support of this FlavorExtraSpec.
        :rtype: str
        """
        return self._hpet_support

    @hpet_support.setter
    def hpet_support(self, hpet_support):
        """Sets the hpet_support of this FlavorExtraSpec.

        :param hpet_support: The hpet_support of this FlavorExtraSpec.
        :type hpet_support: str
        """
        self._hpet_support = hpet_support

    @property
    def instance_vnictype(self):
        """Gets the instance_vnictype of this FlavorExtraSpec.

        :return: The instance_vnictype of this FlavorExtraSpec.
        :rtype: str
        """
        return self._instance_vnictype

    @instance_vnictype.setter
    def instance_vnictype(self, instance_vnictype):
        """Sets the instance_vnictype of this FlavorExtraSpec.

        :param instance_vnictype: The instance_vnictype of this FlavorExtraSpec.
        :type instance_vnictype: str
        """
        self._instance_vnictype = instance_vnictype

    @property
    def instance_vnicinstance_bandwidth(self):
        """Gets the instance_vnicinstance_bandwidth of this FlavorExtraSpec.

        :return: The instance_vnicinstance_bandwidth of this FlavorExtraSpec.
        :rtype: str
        """
        return self._instance_vnicinstance_bandwidth

    @instance_vnicinstance_bandwidth.setter
    def instance_vnicinstance_bandwidth(self, instance_vnicinstance_bandwidth):
        """Sets the instance_vnicinstance_bandwidth of this FlavorExtraSpec.

        :param instance_vnicinstance_bandwidth: The instance_vnicinstance_bandwidth of this FlavorExtraSpec.
        :type instance_vnicinstance_bandwidth: str
        """
        self._instance_vnicinstance_bandwidth = instance_vnicinstance_bandwidth

    @property
    def instance_vnicmax_count(self):
        """Gets the instance_vnicmax_count of this FlavorExtraSpec.

        :return: The instance_vnicmax_count of this FlavorExtraSpec.
        :rtype: str
        """
        return self._instance_vnicmax_count

    @instance_vnicmax_count.setter
    def instance_vnicmax_count(self, instance_vnicmax_count):
        """Sets the instance_vnicmax_count of this FlavorExtraSpec.

        :param instance_vnicmax_count: The instance_vnicmax_count of this FlavorExtraSpec.
        :type instance_vnicmax_count: str
        """
        self._instance_vnicmax_count = instance_vnicmax_count

    @property
    def quotalocal_disk(self):
        """Gets the quotalocal_disk of this FlavorExtraSpec.

        :return: The quotalocal_disk of this FlavorExtraSpec.
        :rtype: str
        """
        return self._quotalocal_disk

    @quotalocal_disk.setter
    def quotalocal_disk(self, quotalocal_disk):
        """Sets the quotalocal_disk of this FlavorExtraSpec.

        :param quotalocal_disk: The quotalocal_disk of this FlavorExtraSpec.
        :type quotalocal_disk: str
        """
        self._quotalocal_disk = quotalocal_disk

    @property
    def quotanvme_ssd(self):
        """Gets the quotanvme_ssd of this FlavorExtraSpec.

        :return: The quotanvme_ssd of this FlavorExtraSpec.
        :rtype: str
        """
        return self._quotanvme_ssd

    @quotanvme_ssd.setter
    def quotanvme_ssd(self, quotanvme_ssd):
        """Sets the quotanvme_ssd of this FlavorExtraSpec.

        :param quotanvme_ssd: The quotanvme_ssd of this FlavorExtraSpec.
        :type quotanvme_ssd: str
        """
        self._quotanvme_ssd = quotanvme_ssd

    @property
    def extra_speciopersistent_grant(self):
        """Gets the extra_speciopersistent_grant of this FlavorExtraSpec.

        :return: The extra_speciopersistent_grant of this FlavorExtraSpec.
        :rtype: str
        """
        return self._extra_speciopersistent_grant

    @extra_speciopersistent_grant.setter
    def extra_speciopersistent_grant(self, extra_speciopersistent_grant):
        """Sets the extra_speciopersistent_grant of this FlavorExtraSpec.

        :param extra_speciopersistent_grant: The extra_speciopersistent_grant of this FlavorExtraSpec.
        :type extra_speciopersistent_grant: str
        """
        self._extra_speciopersistent_grant = extra_speciopersistent_grant

    @property
    def ecsgeneration(self):
        """Gets the ecsgeneration of this FlavorExtraSpec.

        :return: The ecsgeneration of this FlavorExtraSpec.
        :rtype: str
        """
        return self._ecsgeneration

    @ecsgeneration.setter
    def ecsgeneration(self, ecsgeneration):
        """Sets the ecsgeneration of this FlavorExtraSpec.

        :param ecsgeneration: The ecsgeneration of this FlavorExtraSpec.
        :type ecsgeneration: str
        """
        self._ecsgeneration = ecsgeneration

    @property
    def ecsvirtualization_env_types(self):
        """Gets the ecsvirtualization_env_types of this FlavorExtraSpec.

        :return: The ecsvirtualization_env_types of this FlavorExtraSpec.
        :rtype: str
        """
        return self._ecsvirtualization_env_types

    @ecsvirtualization_env_types.setter
    def ecsvirtualization_env_types(self, ecsvirtualization_env_types):
        """Sets the ecsvirtualization_env_types of this FlavorExtraSpec.

        :param ecsvirtualization_env_types: The ecsvirtualization_env_types of this FlavorExtraSpec.
        :type ecsvirtualization_env_types: str
        """
        self._ecsvirtualization_env_types = ecsvirtualization_env_types

    @property
    def pci_passthroughenable_gpu(self):
        """Gets the pci_passthroughenable_gpu of this FlavorExtraSpec.

        :return: The pci_passthroughenable_gpu of this FlavorExtraSpec.
        :rtype: str
        """
        return self._pci_passthroughenable_gpu

    @pci_passthroughenable_gpu.setter
    def pci_passthroughenable_gpu(self, pci_passthroughenable_gpu):
        """Sets the pci_passthroughenable_gpu of this FlavorExtraSpec.

        :param pci_passthroughenable_gpu: The pci_passthroughenable_gpu of this FlavorExtraSpec.
        :type pci_passthroughenable_gpu: str
        """
        self._pci_passthroughenable_gpu = pci_passthroughenable_gpu

    @property
    def pci_passthroughgpu_specs(self):
        """Gets the pci_passthroughgpu_specs of this FlavorExtraSpec.

        :return: The pci_passthroughgpu_specs of this FlavorExtraSpec.
        :rtype: str
        """
        return self._pci_passthroughgpu_specs

    @pci_passthroughgpu_specs.setter
    def pci_passthroughgpu_specs(self, pci_passthroughgpu_specs):
        """Sets the pci_passthroughgpu_specs of this FlavorExtraSpec.

        :param pci_passthroughgpu_specs: The pci_passthroughgpu_specs of this FlavorExtraSpec.
        :type pci_passthroughgpu_specs: str
        """
        self._pci_passthroughgpu_specs = pci_passthroughgpu_specs

    @property
    def pci_passthroughalias(self):
        """Gets the pci_passthroughalias of this FlavorExtraSpec.

        :return: The pci_passthroughalias of this FlavorExtraSpec.
        :rtype: str
        """
        return self._pci_passthroughalias

    @pci_passthroughalias.setter
    def pci_passthroughalias(self, pci_passthroughalias):
        """Sets the pci_passthroughalias of this FlavorExtraSpec.

        :param pci_passthroughalias: The pci_passthroughalias of this FlavorExtraSpec.
        :type pci_passthroughalias: str
        """
        self._pci_passthroughalias = pci_passthroughalias

    @property
    def condoperationstatus(self):
        """Gets the condoperationstatus of this FlavorExtraSpec.

        :return: The condoperationstatus of this FlavorExtraSpec.
        :rtype: str
        """
        return self._condoperationstatus

    @condoperationstatus.setter
    def condoperationstatus(self, condoperationstatus):
        """Sets the condoperationstatus of this FlavorExtraSpec.

        :param condoperationstatus: The condoperationstatus of this FlavorExtraSpec.
        :type condoperationstatus: str
        """
        self._condoperationstatus = condoperationstatus

    @property
    def condoperationaz(self):
        """Gets the condoperationaz of this FlavorExtraSpec.

        :return: The condoperationaz of this FlavorExtraSpec.
        :rtype: str
        """
        return self._condoperationaz

    @condoperationaz.setter
    def condoperationaz(self, condoperationaz):
        """Sets the condoperationaz of this FlavorExtraSpec.

        :param condoperationaz: The condoperationaz of this FlavorExtraSpec.
        :type condoperationaz: str
        """
        self._condoperationaz = condoperationaz

    @property
    def quotamax_rate(self):
        """Gets the quotamax_rate of this FlavorExtraSpec.

        :return: The quotamax_rate of this FlavorExtraSpec.
        :rtype: str
        """
        return self._quotamax_rate

    @quotamax_rate.setter
    def quotamax_rate(self, quotamax_rate):
        """Sets the quotamax_rate of this FlavorExtraSpec.

        :param quotamax_rate: The quotamax_rate of this FlavorExtraSpec.
        :type quotamax_rate: str
        """
        self._quotamax_rate = quotamax_rate

    @property
    def quotamin_rate(self):
        """Gets the quotamin_rate of this FlavorExtraSpec.

        :return: The quotamin_rate of this FlavorExtraSpec.
        :rtype: str
        """
        return self._quotamin_rate

    @quotamin_rate.setter
    def quotamin_rate(self, quotamin_rate):
        """Sets the quotamin_rate of this FlavorExtraSpec.

        :param quotamin_rate: The quotamin_rate of this FlavorExtraSpec.
        :type quotamin_rate: str
        """
        self._quotamin_rate = quotamin_rate

    @property
    def quotamax_pps(self):
        """Gets the quotamax_pps of this FlavorExtraSpec.

        :return: The quotamax_pps of this FlavorExtraSpec.
        :rtype: str
        """
        return self._quotamax_pps

    @quotamax_pps.setter
    def quotamax_pps(self, quotamax_pps):
        """Sets the quotamax_pps of this FlavorExtraSpec.

        :param quotamax_pps: The quotamax_pps of this FlavorExtraSpec.
        :type quotamax_pps: str
        """
        self._quotamax_pps = quotamax_pps

    @property
    def condoperationcharge(self):
        """Gets the condoperationcharge of this FlavorExtraSpec.

        :return: The condoperationcharge of this FlavorExtraSpec.
        :rtype: str
        """
        return self._condoperationcharge

    @condoperationcharge.setter
    def condoperationcharge(self, condoperationcharge):
        """Sets the condoperationcharge of this FlavorExtraSpec.

        :param condoperationcharge: The condoperationcharge of this FlavorExtraSpec.
        :type condoperationcharge: str
        """
        self._condoperationcharge = condoperationcharge

    @property
    def condoperationchargestop(self):
        """Gets the condoperationchargestop of this FlavorExtraSpec.

        :return: The condoperationchargestop of this FlavorExtraSpec.
        :rtype: str
        """
        return self._condoperationchargestop

    @condoperationchargestop.setter
    def condoperationchargestop(self, condoperationchargestop):
        """Sets the condoperationchargestop of this FlavorExtraSpec.

        :param condoperationchargestop: The condoperationchargestop of this FlavorExtraSpec.
        :type condoperationchargestop: str
        """
        self._condoperationchargestop = condoperationchargestop

    @property
    def condspotoperationaz(self):
        """Gets the condspotoperationaz of this FlavorExtraSpec.

        :return: The condspotoperationaz of this FlavorExtraSpec.
        :rtype: str
        """
        return self._condspotoperationaz

    @condspotoperationaz.setter
    def condspotoperationaz(self, condspotoperationaz):
        """Sets the condspotoperationaz of this FlavorExtraSpec.

        :param condspotoperationaz: The condspotoperationaz of this FlavorExtraSpec.
        :type condspotoperationaz: str
        """
        self._condspotoperationaz = condspotoperationaz

    @property
    def condoperationroles(self):
        """Gets the condoperationroles of this FlavorExtraSpec.

        :return: The condoperationroles of this FlavorExtraSpec.
        :rtype: str
        """
        return self._condoperationroles

    @condoperationroles.setter
    def condoperationroles(self, condoperationroles):
        """Sets the condoperationroles of this FlavorExtraSpec.

        :param condoperationroles: The condoperationroles of this FlavorExtraSpec.
        :type condoperationroles: str
        """
        self._condoperationroles = condoperationroles

    @property
    def condspotoperationstatus(self):
        """Gets the condspotoperationstatus of this FlavorExtraSpec.

        :return: The condspotoperationstatus of this FlavorExtraSpec.
        :rtype: str
        """
        return self._condspotoperationstatus

    @condspotoperationstatus.setter
    def condspotoperationstatus(self, condspotoperationstatus):
        """Sets the condspotoperationstatus of this FlavorExtraSpec.

        :param condspotoperationstatus: The condspotoperationstatus of this FlavorExtraSpec.
        :type condspotoperationstatus: str
        """
        self._condspotoperationstatus = condspotoperationstatus

    @property
    def condnetwork(self):
        """Gets the condnetwork of this FlavorExtraSpec.

        :return: The condnetwork of this FlavorExtraSpec.
        :rtype: str
        """
        return self._condnetwork

    @condnetwork.setter
    def condnetwork(self, condnetwork):
        """Sets the condnetwork of this FlavorExtraSpec.

        :param condnetwork: The condnetwork of this FlavorExtraSpec.
        :type condnetwork: str
        """
        self._condnetwork = condnetwork

    @property
    def condstorage(self):
        """Gets the condstorage of this FlavorExtraSpec.

        :return: The condstorage of this FlavorExtraSpec.
        :rtype: str
        """
        return self._condstorage

    @condstorage.setter
    def condstorage(self, condstorage):
        """Sets the condstorage of this FlavorExtraSpec.

        :param condstorage: The condstorage of this FlavorExtraSpec.
        :type condstorage: str
        """
        self._condstorage = condstorage

    @property
    def condcomputelive_resizable(self):
        """Gets the condcomputelive_resizable of this FlavorExtraSpec.

        :return: The condcomputelive_resizable of this FlavorExtraSpec.
        :rtype: str
        """
        return self._condcomputelive_resizable

    @condcomputelive_resizable.setter
    def condcomputelive_resizable(self, condcomputelive_resizable):
        """Sets the condcomputelive_resizable of this FlavorExtraSpec.

        :param condcomputelive_resizable: The condcomputelive_resizable of this FlavorExtraSpec.
        :type condcomputelive_resizable: str
        """
        self._condcomputelive_resizable = condcomputelive_resizable

    @property
    def condcompute(self):
        """Gets the condcompute of this FlavorExtraSpec.

        :return: The condcompute of this FlavorExtraSpec.
        :rtype: str
        """
        return self._condcompute

    @condcompute.setter
    def condcompute(self, condcompute):
        """Sets the condcompute of this FlavorExtraSpec.

        :param condcompute: The condcompute of this FlavorExtraSpec.
        :type condcompute: str
        """
        self._condcompute = condcompute

    @property
    def infogpuname(self):
        """Gets the infogpuname of this FlavorExtraSpec.

        :return: The infogpuname of this FlavorExtraSpec.
        :rtype: str
        """
        return self._infogpuname

    @infogpuname.setter
    def infogpuname(self, infogpuname):
        """Sets the infogpuname of this FlavorExtraSpec.

        :param infogpuname: The infogpuname of this FlavorExtraSpec.
        :type infogpuname: str
        """
        self._infogpuname = infogpuname

    @property
    def infocpuname(self):
        """Gets the infocpuname of this FlavorExtraSpec.

        :return: The infocpuname of this FlavorExtraSpec.
        :rtype: str
        """
        return self._infocpuname

    @infocpuname.setter
    def infocpuname(self, infocpuname):
        """Sets the infocpuname of this FlavorExtraSpec.

        :param infocpuname: The infocpuname of this FlavorExtraSpec.
        :type infocpuname: str
        """
        self._infocpuname = infocpuname

    @property
    def quotagpu(self):
        """Gets the quotagpu of this FlavorExtraSpec.

        :return: The quotagpu of this FlavorExtraSpec.
        :rtype: str
        """
        return self._quotagpu

    @quotagpu.setter
    def quotagpu(self, quotagpu):
        """Sets the quotagpu of this FlavorExtraSpec.

        :param quotagpu: The quotagpu of this FlavorExtraSpec.
        :type quotagpu: str
        """
        self._quotagpu = quotagpu

    @property
    def ecsinstance_architecture(self):
        """Gets the ecsinstance_architecture of this FlavorExtraSpec.

        :return: The ecsinstance_architecture of this FlavorExtraSpec.
        :rtype: str
        """
        return self._ecsinstance_architecture

    @ecsinstance_architecture.setter
    def ecsinstance_architecture(self, ecsinstance_architecture):
        """Sets the ecsinstance_architecture of this FlavorExtraSpec.

        :param ecsinstance_architecture: The ecsinstance_architecture of this FlavorExtraSpec.
        :type ecsinstance_architecture: str
        """
        self._ecsinstance_architecture = ecsinstance_architecture

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
        if not isinstance(other, FlavorExtraSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
