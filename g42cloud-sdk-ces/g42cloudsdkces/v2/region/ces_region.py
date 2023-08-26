# coding: utf-8

import types
import six

from g42cloudsdkcore.region.region import Region
from g42cloudsdkcore.region.provider import RegionProviderChain

class CesRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("CES")

    AE_AD_1 = Region("ae-ad-1",
                        "https://ces.ae-ad-1.g42cloud.com")

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


