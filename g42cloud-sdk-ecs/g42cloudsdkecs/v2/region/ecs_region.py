# coding: utf-8

import types
import six

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class EcsRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("ECS")


    AE_AD_1 = Region(id="ae-ad-1", endpoint="https://ecs.ae-ad-1.g42cloud.com")

    static_fields = {
        "ae-ad-1": AE_AD_1,
    }

    @classmethod
    def value_of(cls, region_id, static_fields=None):
        if not region_id:
            raise KeyError("Unexpected empty parameter: region_id.")

        fields = static_fields if static_fields else cls.static_fields

        region = cls._PROVIDER.get_region(region_id)
        if region:
            return region

        if region_id in fields:
            return fields.get(region_id)

        raise KeyError("Unexpected region_id: " + region_id)


