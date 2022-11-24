# coding: utf-8

from __future__ import absolute_import

import datetime
import re
import importlib

import six

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class EvsClient(Client):
    PRIMITIVE_TYPES = (float, bool, bytes, six.text_type) + six.integer_types
    NATIVE_TYPES_MAPPING = {
        'int': int,
        'long': int if six.PY3 else long,
        'float': float,
        'str': str,
        'bool': bool,
        'date': datetime.date,
        'datetime': datetime.datetime,
        'object': object,
    }

    def __init__(self):
        super(EvsClient, self).__init__()
        self.model_package = importlib.import_module("g42cloudsdkevs.v2.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "EvsClient":
            raise TypeError("client type error, support client type is EvsClient")

        return ClientBuilder(clazz)

    def batch_create_volume_tags(self, request):
        """
        :param request: Request instance for BatchCreateVolumeTags
        :type request: :class:`g42cloudsdkevs.v2.BatchCreateVolumeTagsRequest`
        :rtype: :class:`g42cloudsdkevs.v2.BatchCreateVolumeTagsResponse`
        """
        return self.batch_create_volume_tags_with_http_info(request)

    def batch_create_volume_tags_with_http_info(self, request):
        all_params = ['volume_id', 'batch_create_volume_tags_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'volume_id' in local_var_params:
            path_params['volume_id'] = local_var_params['volume_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/cloudvolumes/{volume_id}/tags/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchCreateVolumeTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_volume_tags(self, request):
        """
        :param request: Request instance for BatchDeleteVolumeTags
        :type request: :class:`g42cloudsdkevs.v2.BatchDeleteVolumeTagsRequest`
        :rtype: :class:`g42cloudsdkevs.v2.BatchDeleteVolumeTagsResponse`
        """
        return self.batch_delete_volume_tags_with_http_info(request)

    def batch_delete_volume_tags_with_http_info(self, request):
        all_params = ['volume_id', 'batch_delete_volume_tags_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'volume_id' in local_var_params:
            path_params['volume_id'] = local_var_params['volume_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/cloudvolumes/{volume_id}/tags/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteVolumeTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def cinder_accept_volume_transfer(self, request):
        """
        :param request: Request instance for CinderAcceptVolumeTransfer
        :type request: :class:`g42cloudsdkevs.v2.CinderAcceptVolumeTransferRequest`
        :rtype: :class:`g42cloudsdkevs.v2.CinderAcceptVolumeTransferResponse`
        """
        return self.cinder_accept_volume_transfer_with_http_info(request)

    def cinder_accept_volume_transfer_with_http_info(self, request):
        all_params = ['transfer_id', 'cinder_accept_volume_transfer_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'transfer_id' in local_var_params:
            path_params['transfer_id'] = local_var_params['transfer_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/os-volume-transfer/{transfer_id}/accept',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CinderAcceptVolumeTransferResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def cinder_create_volume_transfer(self, request):
        """
        :param request: Request instance for CinderCreateVolumeTransfer
        :type request: :class:`g42cloudsdkevs.v2.CinderCreateVolumeTransferRequest`
        :rtype: :class:`g42cloudsdkevs.v2.CinderCreateVolumeTransferResponse`
        """
        return self.cinder_create_volume_transfer_with_http_info(request)

    def cinder_create_volume_transfer_with_http_info(self, request):
        all_params = ['cinder_create_volume_transfer_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/os-volume-transfer',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CinderCreateVolumeTransferResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def cinder_delete_volume_transfer(self, request):
        """
        :param request: Request instance for CinderDeleteVolumeTransfer
        :type request: :class:`g42cloudsdkevs.v2.CinderDeleteVolumeTransferRequest`
        :rtype: :class:`g42cloudsdkevs.v2.CinderDeleteVolumeTransferResponse`
        """
        return self.cinder_delete_volume_transfer_with_http_info(request)

    def cinder_delete_volume_transfer_with_http_info(self, request):
        all_params = ['transfer_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'transfer_id' in local_var_params:
            path_params['transfer_id'] = local_var_params['transfer_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/os-volume-transfer/{transfer_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CinderDeleteVolumeTransferResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def cinder_list_availability_zones(self, request):
        """
        :param request: Request instance for CinderListAvailabilityZones
        :type request: :class:`g42cloudsdkevs.v2.CinderListAvailabilityZonesRequest`
        :rtype: :class:`g42cloudsdkevs.v2.CinderListAvailabilityZonesResponse`
        """
        return self.cinder_list_availability_zones_with_http_info(request)

    def cinder_list_availability_zones_with_http_info(self, request):
        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/os-availability-zone',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CinderListAvailabilityZonesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def cinder_list_quotas(self, request):
        """
        :param request: Request instance for CinderListQuotas
        :type request: :class:`g42cloudsdkevs.v2.CinderListQuotasRequest`
        :rtype: :class:`g42cloudsdkevs.v2.CinderListQuotasResponse`
        """
        return self.cinder_list_quotas_with_http_info(request)

    def cinder_list_quotas_with_http_info(self, request):
        all_params = ['target_project_id', 'usage']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'target_project_id' in local_var_params:
            path_params['target_project_id'] = local_var_params['target_project_id']

        query_params = []
        if 'usage' in local_var_params:
            query_params.append(('usage', local_var_params['usage']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/os-quota-sets/{target_project_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CinderListQuotasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def cinder_list_volume_transfers(self, request):
        """
        :param request: Request instance for CinderListVolumeTransfers
        :type request: :class:`g42cloudsdkevs.v2.CinderListVolumeTransfersRequest`
        :rtype: :class:`g42cloudsdkevs.v2.CinderListVolumeTransfersResponse`
        """
        return self.cinder_list_volume_transfers_with_http_info(request)

    def cinder_list_volume_transfers_with_http_info(self, request):
        all_params = ['limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/os-volume-transfer',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CinderListVolumeTransfersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def cinder_list_volume_types(self, request):
        """
        :param request: Request instance for CinderListVolumeTypes
        :type request: :class:`g42cloudsdkevs.v2.CinderListVolumeTypesRequest`
        :rtype: :class:`g42cloudsdkevs.v2.CinderListVolumeTypesResponse`
        """
        return self.cinder_list_volume_types_with_http_info(request)

    def cinder_list_volume_types_with_http_info(self, request):
        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/types',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CinderListVolumeTypesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def cinder_show_volume_transfer(self, request):
        """
        :param request: Request instance for CinderShowVolumeTransfer
        :type request: :class:`g42cloudsdkevs.v2.CinderShowVolumeTransferRequest`
        :rtype: :class:`g42cloudsdkevs.v2.CinderShowVolumeTransferResponse`
        """
        return self.cinder_show_volume_transfer_with_http_info(request)

    def cinder_show_volume_transfer_with_http_info(self, request):
        all_params = ['transfer_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'transfer_id' in local_var_params:
            path_params['transfer_id'] = local_var_params['transfer_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/os-volume-transfer/{transfer_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CinderShowVolumeTransferResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_snapshot(self, request):
        """
        :param request: Request instance for CreateSnapshot
        :type request: :class:`g42cloudsdkevs.v2.CreateSnapshotRequest`
        :rtype: :class:`g42cloudsdkevs.v2.CreateSnapshotResponse`
        """
        return self.create_snapshot_with_http_info(request)

    def create_snapshot_with_http_info(self, request):
        all_params = ['create_snapshot_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/cloudsnapshots',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateSnapshotResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_volume(self, request):
        """
        :param request: Request instance for CreateVolume
        :type request: :class:`g42cloudsdkevs.v2.CreateVolumeRequest`
        :rtype: :class:`g42cloudsdkevs.v2.CreateVolumeResponse`
        """
        return self.create_volume_with_http_info(request)

    def create_volume_with_http_info(self, request):
        all_params = ['create_volume_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.1/{project_id}/cloudvolumes',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateVolumeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_snapshot(self, request):
        """
        :param request: Request instance for DeleteSnapshot
        :type request: :class:`g42cloudsdkevs.v2.DeleteSnapshotRequest`
        :rtype: :class:`g42cloudsdkevs.v2.DeleteSnapshotResponse`
        """
        return self.delete_snapshot_with_http_info(request)

    def delete_snapshot_with_http_info(self, request):
        all_params = ['snapshot_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'snapshot_id' in local_var_params:
            path_params['snapshot_id'] = local_var_params['snapshot_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/cloudsnapshots/{snapshot_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteSnapshotResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_volume(self, request):
        """
        :param request: Request instance for DeleteVolume
        :type request: :class:`g42cloudsdkevs.v2.DeleteVolumeRequest`
        :rtype: :class:`g42cloudsdkevs.v2.DeleteVolumeResponse`
        """
        return self.delete_volume_with_http_info(request)

    def delete_volume_with_http_info(self, request):
        all_params = ['volume_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'volume_id' in local_var_params:
            path_params['volume_id'] = local_var_params['volume_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/cloudvolumes/{volume_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteVolumeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_snapshots(self, request):
        """
        :param request: Request instance for ListSnapshots
        :type request: :class:`g42cloudsdkevs.v2.ListSnapshotsRequest`
        :rtype: :class:`g42cloudsdkevs.v2.ListSnapshotsResponse`
        """
        return self.list_snapshots_with_http_info(request)

    def list_snapshots_with_http_info(self, request):
        all_params = ['offset', 'limit', 'name', 'status', 'volume_id', 'availability_zone', 'id', 'dedicated_storage_name', 'dedicated_storage_id', 'service_type', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'volume_id' in local_var_params:
            query_params.append(('volume_id', local_var_params['volume_id']))
        if 'availability_zone' in local_var_params:
            query_params.append(('availability_zone', local_var_params['availability_zone']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'dedicated_storage_name' in local_var_params:
            query_params.append(('dedicated_storage_name', local_var_params['dedicated_storage_name']))
        if 'dedicated_storage_id' in local_var_params:
            query_params.append(('dedicated_storage_id', local_var_params['dedicated_storage_id']))
        if 'service_type' in local_var_params:
            query_params.append(('service_type', local_var_params['service_type']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/cloudsnapshots/detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSnapshotsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_volume_tags(self, request):
        """
        :param request: Request instance for ListVolumeTags
        :type request: :class:`g42cloudsdkevs.v2.ListVolumeTagsRequest`
        :rtype: :class:`g42cloudsdkevs.v2.ListVolumeTagsResponse`
        """
        return self.list_volume_tags_with_http_info(request)

    def list_volume_tags_with_http_info(self, request):
        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/cloudvolumes/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListVolumeTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_volumes(self, request):
        """
        :param request: Request instance for ListVolumes
        :type request: :class:`g42cloudsdkevs.v2.ListVolumesRequest`
        :rtype: :class:`g42cloudsdkevs.v2.ListVolumesResponse`
        """
        return self.list_volumes_with_http_info(request)

    def list_volumes_with_http_info(self, request):
        all_params = ['marker', 'name', 'limit', 'sort_key', 'offset', 'sort_dir', 'status', 'metadata', 'availability_zone', 'multiattach', 'service_type', 'dedicated_storage_id', 'dedicated_storage_name', 'volume_type_id', 'id', 'ids', 'enterprise_project_id', 'server_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'metadata' in local_var_params:
            query_params.append(('metadata', local_var_params['metadata']))
        if 'availability_zone' in local_var_params:
            query_params.append(('availability_zone', local_var_params['availability_zone']))
        if 'multiattach' in local_var_params:
            query_params.append(('multiattach', local_var_params['multiattach']))
        if 'service_type' in local_var_params:
            query_params.append(('service_type', local_var_params['service_type']))
        if 'dedicated_storage_id' in local_var_params:
            query_params.append(('dedicated_storage_id', local_var_params['dedicated_storage_id']))
        if 'dedicated_storage_name' in local_var_params:
            query_params.append(('dedicated_storage_name', local_var_params['dedicated_storage_name']))
        if 'volume_type_id' in local_var_params:
            query_params.append(('volume_type_id', local_var_params['volume_type_id']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'ids' in local_var_params:
            query_params.append(('ids', local_var_params['ids']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'server_id' in local_var_params:
            query_params.append(('server_id', local_var_params['server_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/cloudvolumes/detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListVolumesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_volumes_by_tags(self, request):
        """
        :param request: Request instance for ListVolumesByTags
        :type request: :class:`g42cloudsdkevs.v2.ListVolumesByTagsRequest`
        :rtype: :class:`g42cloudsdkevs.v2.ListVolumesByTagsResponse`
        """
        return self.list_volumes_by_tags_with_http_info(request)

    def list_volumes_by_tags_with_http_info(self, request):
        all_params = ['list_volumes_by_tags_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/cloudvolumes/resource_instances/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListVolumesByTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def resize_volume(self, request):
        """
        :param request: Request instance for ResizeVolume
        :type request: :class:`g42cloudsdkevs.v2.ResizeVolumeRequest`
        :rtype: :class:`g42cloudsdkevs.v2.ResizeVolumeResponse`
        """
        return self.resize_volume_with_http_info(request)

    def resize_volume_with_http_info(self, request):
        all_params = ['volume_id', 'resize_volume_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'volume_id' in local_var_params:
            path_params['volume_id'] = local_var_params['volume_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.1/{project_id}/cloudvolumes/{volume_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ResizeVolumeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def rollback_snapshot(self, request):
        """
        :param request: Request instance for RollbackSnapshot
        :type request: :class:`g42cloudsdkevs.v2.RollbackSnapshotRequest`
        :rtype: :class:`g42cloudsdkevs.v2.RollbackSnapshotResponse`
        """
        return self.rollback_snapshot_with_http_info(request)

    def rollback_snapshot_with_http_info(self, request):
        all_params = ['snapshot_id', 'rollback_snapshot_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'snapshot_id' in local_var_params:
            path_params['snapshot_id'] = local_var_params['snapshot_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/cloudsnapshots/{snapshot_id}/rollback',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RollbackSnapshotResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_job(self, request):
        """
        :param request: Request instance for ShowJob
        :type request: :class:`g42cloudsdkevs.v2.ShowJobRequest`
        :rtype: :class:`g42cloudsdkevs.v2.ShowJobResponse`
        """
        return self.show_job_with_http_info(request)

    def show_job_with_http_info(self, request):
        all_params = ['job_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/jobs/{job_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_snapshot(self, request):
        """
        :param request: Request instance for ShowSnapshot
        :type request: :class:`g42cloudsdkevs.v2.ShowSnapshotRequest`
        :rtype: :class:`g42cloudsdkevs.v2.ShowSnapshotResponse`
        """
        return self.show_snapshot_with_http_info(request)

    def show_snapshot_with_http_info(self, request):
        all_params = ['snapshot_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'snapshot_id' in local_var_params:
            path_params['snapshot_id'] = local_var_params['snapshot_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/cloudsnapshots/{snapshot_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowSnapshotResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_volume(self, request):
        """
        :param request: Request instance for ShowVolume
        :type request: :class:`g42cloudsdkevs.v2.ShowVolumeRequest`
        :rtype: :class:`g42cloudsdkevs.v2.ShowVolumeResponse`
        """
        return self.show_volume_with_http_info(request)

    def show_volume_with_http_info(self, request):
        all_params = ['volume_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'volume_id' in local_var_params:
            path_params['volume_id'] = local_var_params['volume_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/cloudvolumes/{volume_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowVolumeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_volume_tags(self, request):
        """
        :param request: Request instance for ShowVolumeTags
        :type request: :class:`g42cloudsdkevs.v2.ShowVolumeTagsRequest`
        :rtype: :class:`g42cloudsdkevs.v2.ShowVolumeTagsResponse`
        """
        return self.show_volume_tags_with_http_info(request)

    def show_volume_tags_with_http_info(self, request):
        all_params = ['volume_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'volume_id' in local_var_params:
            path_params['volume_id'] = local_var_params['volume_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/cloudvolumes/{volume_id}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowVolumeTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_snapshot(self, request):
        """
        :param request: Request instance for UpdateSnapshot
        :type request: :class:`g42cloudsdkevs.v2.UpdateSnapshotRequest`
        :rtype: :class:`g42cloudsdkevs.v2.UpdateSnapshotResponse`
        """
        return self.update_snapshot_with_http_info(request)

    def update_snapshot_with_http_info(self, request):
        all_params = ['snapshot_id', 'update_snapshot_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'snapshot_id' in local_var_params:
            path_params['snapshot_id'] = local_var_params['snapshot_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/cloudsnapshots/{snapshot_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateSnapshotResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_volume(self, request):
        """
        :param request: Request instance for UpdateVolume
        :type request: :class:`g42cloudsdkevs.v2.UpdateVolumeRequest`
        :rtype: :class:`g42cloudsdkevs.v2.UpdateVolumeResponse`
        """
        return self.update_volume_with_http_info(request)

    def update_volume_with_http_info(self, request):
        all_params = ['volume_id', 'update_volume_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'volume_id' in local_var_params:
            path_params['volume_id'] = local_var_params['volume_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/cloudvolumes/{volume_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateVolumeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_versions(self, request):
        """
        :param request: Request instance for ListVersions
        :type request: :class:`g42cloudsdkevs.v2.ListVersionsRequest`
        :rtype: :class:`g42cloudsdkevs.v2.ListVersionsResponse`
        """
        return self.list_versions_with_http_info(request)

    def list_versions_with_http_info(self, request):
        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListVersionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_version(self, request):
        """
        :param request: Request instance for ShowVersion
        :type request: :class:`g42cloudsdkevs.v2.ShowVersionRequest`
        :rtype: :class:`g42cloudsdkevs.v2.ShowVersionResponse`
        """
        return self.show_version_with_http_info(request)

    def show_version_with_http_info(self, request):
        all_params = ['version']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'version' in local_var_params:
            path_params['version'] = local_var_params['version']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/{version}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowVersionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def call_api(self, resource_path, method, path_params=None, query_params=None, header_params=None, body=None,
                 post_params=None, cname=None, response_type=None, response_headers=None, auth_settings=None,
                 collection_formats=None, request_type=None):
        """Makes the HTTP request and returns deserialized data.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be placed in the request header.
        :param body: Request body.
        :param post_params: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param cname: Used for obs endpoint.
        :param auth_settings: Auth Settings names for the request.
        :param response_type: Response data type.
        :param response_headers: Header should be added to response data.
        :param collection_formats: dict of collection formats for path, query,
            header, and post parameters.
        :param request_type: Request data type.
        :return:
            Return the response directly.
        """
        return self.do_http_request(
            method=method,
            resource_path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body,
            post_params=post_params,
            cname=cname,
            response_type=response_type,
            response_headers=response_headers,
            collection_formats=collection_formats,
            request_type=request_type)
