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


class EcsClient(Client):
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
        super(EcsClient, self).__init__()
        self.model_package = importlib.import_module("g42cloudsdkecs.v2.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "EcsClient":
            raise TypeError("client type error, support client type is EcsClient")

        return ClientBuilder(clazz)

    def add_server_group_member(self, request):
        """
        :param request: Request instance for AddServerGroupMember
        :type request: :class:`g42cloudsdkecs.v2.AddServerGroupMemberRequest`
        :rtype: :class:`g42cloudsdkecs.v2.AddServerGroupMemberResponse`
        """
        return self.add_server_group_member_with_http_info(request)

    def add_server_group_member_with_http_info(self, request):
        all_params = ['server_group_id', 'add_server_group_member_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_group_id' in local_var_params:
            path_params['server_group_id'] = local_var_params['server_group_id']

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
            resource_path='/v1/{project_id}/cloudservers/os-server-groups/{server_group_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddServerGroupMemberResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def associate_server_virtual_ip(self, request):
        """
        :param request: Request instance for AssociateServerVirtualIp
        :type request: :class:`g42cloudsdkecs.v2.AssociateServerVirtualIpRequest`
        :rtype: :class:`g42cloudsdkecs.v2.AssociateServerVirtualIpResponse`
        """
        return self.associate_server_virtual_ip_with_http_info(request)

    def associate_server_virtual_ip_with_http_info(self, request):
        all_params = ['nic_id', 'associate_server_virtual_ip_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'nic_id' in local_var_params:
            path_params['nic_id'] = local_var_params['nic_id']

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
            resource_path='/v1/{project_id}/cloudservers/nics/{nic_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AssociateServerVirtualIpResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def attach_server_volume(self, request):
        """
        :param request: Request instance for AttachServerVolume
        :type request: :class:`g42cloudsdkecs.v2.AttachServerVolumeRequest`
        :rtype: :class:`g42cloudsdkecs.v2.AttachServerVolumeResponse`
        """
        return self.attach_server_volume_with_http_info(request)

    def attach_server_volume_with_http_info(self, request):
        all_params = ['server_id', 'attach_server_volume_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1/{project_id}/cloudservers/{server_id}/attachvolume',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AttachServerVolumeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_add_server_nics(self, request):
        """
        :param request: Request instance for BatchAddServerNics
        :type request: :class:`g42cloudsdkecs.v2.BatchAddServerNicsRequest`
        :rtype: :class:`g42cloudsdkecs.v2.BatchAddServerNicsResponse`
        """
        return self.batch_add_server_nics_with_http_info(request)

    def batch_add_server_nics_with_http_info(self, request):
        all_params = ['server_id', 'batch_add_server_nics_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1/{project_id}/cloudservers/{server_id}/nics',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchAddServerNicsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_attach_sharable_volumes(self, request):
        """
        :param request: Request instance for BatchAttachSharableVolumes
        :type request: :class:`g42cloudsdkecs.v2.BatchAttachSharableVolumesRequest`
        :rtype: :class:`g42cloudsdkecs.v2.BatchAttachSharableVolumesResponse`
        """
        return self.batch_attach_sharable_volumes_with_http_info(request)

    def batch_attach_sharable_volumes_with_http_info(self, request):
        all_params = ['volume_id', 'batch_attach_sharable_volumes_request_body']
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
            resource_path='/v1/{project_id}/batchaction/attachvolumes/{volume_id}',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchAttachSharableVolumesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_create_server_tags(self, request):
        """
        :param request: Request instance for BatchCreateServerTags
        :type request: :class:`g42cloudsdkecs.v2.BatchCreateServerTagsRequest`
        :rtype: :class:`g42cloudsdkecs.v2.BatchCreateServerTagsResponse`
        """
        return self.batch_create_server_tags_with_http_info(request)

    def batch_create_server_tags_with_http_info(self, request):
        all_params = ['server_id', 'batch_create_server_tags_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1/{project_id}/cloudservers/{server_id}/tags/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchCreateServerTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_server_nics(self, request):
        """
        :param request: Request instance for BatchDeleteServerNics
        :type request: :class:`g42cloudsdkecs.v2.BatchDeleteServerNicsRequest`
        :rtype: :class:`g42cloudsdkecs.v2.BatchDeleteServerNicsResponse`
        """
        return self.batch_delete_server_nics_with_http_info(request)

    def batch_delete_server_nics_with_http_info(self, request):
        all_params = ['server_id', 'batch_delete_server_nics_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1/{project_id}/cloudservers/{server_id}/nics/delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteServerNicsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_server_tags(self, request):
        """
        :param request: Request instance for BatchDeleteServerTags
        :type request: :class:`g42cloudsdkecs.v2.BatchDeleteServerTagsRequest`
        :rtype: :class:`g42cloudsdkecs.v2.BatchDeleteServerTagsResponse`
        """
        return self.batch_delete_server_tags_with_http_info(request)

    def batch_delete_server_tags_with_http_info(self, request):
        all_params = ['server_id', 'batch_delete_server_tags_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1/{project_id}/cloudservers/{server_id}/tags/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteServerTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_reboot_servers(self, request):
        """
        :param request: Request instance for BatchRebootServers
        :type request: :class:`g42cloudsdkecs.v2.BatchRebootServersRequest`
        :rtype: :class:`g42cloudsdkecs.v2.BatchRebootServersResponse`
        """
        return self.batch_reboot_servers_with_http_info(request)

    def batch_reboot_servers_with_http_info(self, request):
        all_params = ['batch_reboot_servers_request_body']
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
            resource_path='/v1/{project_id}/cloudservers/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchRebootServersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_reset_servers_password(self, request):
        """
        :param request: Request instance for BatchResetServersPassword
        :type request: :class:`g42cloudsdkecs.v2.BatchResetServersPasswordRequest`
        :rtype: :class:`g42cloudsdkecs.v2.BatchResetServersPasswordResponse`
        """
        return self.batch_reset_servers_password_with_http_info(request)

    def batch_reset_servers_password_with_http_info(self, request):
        all_params = ['batch_reset_servers_password_request_body']
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
            resource_path='/v1/{project_id}/cloudservers/os-reset-passwords',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchResetServersPasswordResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_start_servers(self, request):
        """
        :param request: Request instance for BatchStartServers
        :type request: :class:`g42cloudsdkecs.v2.BatchStartServersRequest`
        :rtype: :class:`g42cloudsdkecs.v2.BatchStartServersResponse`
        """
        return self.batch_start_servers_with_http_info(request)

    def batch_start_servers_with_http_info(self, request):
        all_params = ['batch_start_servers_request_body']
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
            resource_path='/v1/{project_id}/cloudservers/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchStartServersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_stop_servers(self, request):
        """
        :param request: Request instance for BatchStopServers
        :type request: :class:`g42cloudsdkecs.v2.BatchStopServersRequest`
        :rtype: :class:`g42cloudsdkecs.v2.BatchStopServersResponse`
        """
        return self.batch_stop_servers_with_http_info(request)

    def batch_stop_servers_with_http_info(self, request):
        all_params = ['batch_stop_servers_request_body']
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
            resource_path='/v1/{project_id}/cloudservers/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchStopServersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_update_servers_name(self, request):
        """
        :param request: Request instance for BatchUpdateServersName
        :type request: :class:`g42cloudsdkecs.v2.BatchUpdateServersNameRequest`
        :rtype: :class:`g42cloudsdkecs.v2.BatchUpdateServersNameResponse`
        """
        return self.batch_update_servers_name_with_http_info(request)

    def batch_update_servers_name_with_http_info(self, request):
        all_params = ['batch_update_servers_name_request_body']
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
            resource_path='/v1/{project_id}/cloudservers/server-name',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchUpdateServersNameResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_server_os_with_cloud_init(self, request):
        """
        :param request: Request instance for ChangeServerOsWithCloudInit
        :type request: :class:`g42cloudsdkecs.v2.ChangeServerOsWithCloudInitRequest`
        :rtype: :class:`g42cloudsdkecs.v2.ChangeServerOsWithCloudInitResponse`
        """
        return self.change_server_os_with_cloud_init_with_http_info(request)

    def change_server_os_with_cloud_init_with_http_info(self, request):
        all_params = ['server_id', 'change_server_os_with_cloud_init_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v2/{project_id}/cloudservers/{server_id}/changeos',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangeServerOsWithCloudInitResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_server_os_without_cloud_init(self, request):
        """
        :param request: Request instance for ChangeServerOsWithoutCloudInit
        :type request: :class:`g42cloudsdkecs.v2.ChangeServerOsWithoutCloudInitRequest`
        :rtype: :class:`g42cloudsdkecs.v2.ChangeServerOsWithoutCloudInitResponse`
        """
        return self.change_server_os_without_cloud_init_with_http_info(request)

    def change_server_os_without_cloud_init_with_http_info(self, request):
        all_params = ['server_id', 'change_server_os_without_cloud_init_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1/{project_id}/cloudservers/{server_id}/changeos',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangeServerOsWithoutCloudInitResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_post_paid_servers(self, request):
        """
        :param request: Request instance for CreatePostPaidServers
        :type request: :class:`g42cloudsdkecs.v2.CreatePostPaidServersRequest`
        :rtype: :class:`g42cloudsdkecs.v2.CreatePostPaidServersResponse`
        """
        return self.create_post_paid_servers_with_http_info(request)

    def create_post_paid_servers_with_http_info(self, request):
        all_params = ['create_post_paid_servers_request_body']
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
            resource_path='/v1/{project_id}/cloudservers',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreatePostPaidServersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_server_group(self, request):
        """
        :param request: Request instance for CreateServerGroup
        :type request: :class:`g42cloudsdkecs.v2.CreateServerGroupRequest`
        :rtype: :class:`g42cloudsdkecs.v2.CreateServerGroupResponse`
        """
        return self.create_server_group_with_http_info(request)

    def create_server_group_with_http_info(self, request):
        all_params = ['create_server_group_request_body']
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
            resource_path='/v1/{project_id}/cloudservers/os-server-groups',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateServerGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_servers(self, request):
        """
        :param request: Request instance for CreateServers
        :type request: :class:`g42cloudsdkecs.v2.CreateServersRequest`
        :rtype: :class:`g42cloudsdkecs.v2.CreateServersResponse`
        """
        return self.create_servers_with_http_info(request)

    def create_servers_with_http_info(self, request):
        all_params = ['create_servers_request_body']
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
            resource_path='/v1.1/{project_id}/cloudservers',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateServersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_server_group(self, request):
        """
        :param request: Request instance for DeleteServerGroup
        :type request: :class:`g42cloudsdkecs.v2.DeleteServerGroupRequest`
        :rtype: :class:`g42cloudsdkecs.v2.DeleteServerGroupResponse`
        """
        return self.delete_server_group_with_http_info(request)

    def delete_server_group_with_http_info(self, request):
        all_params = ['server_group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_group_id' in local_var_params:
            path_params['server_group_id'] = local_var_params['server_group_id']

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
            resource_path='/v1/{project_id}/cloudservers/os-server-groups/{server_group_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteServerGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_server_group_member(self, request):
        """
        :param request: Request instance for DeleteServerGroupMember
        :type request: :class:`g42cloudsdkecs.v2.DeleteServerGroupMemberRequest`
        :rtype: :class:`g42cloudsdkecs.v2.DeleteServerGroupMemberResponse`
        """
        return self.delete_server_group_member_with_http_info(request)

    def delete_server_group_member_with_http_info(self, request):
        all_params = ['server_group_id', 'delete_server_group_member_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_group_id' in local_var_params:
            path_params['server_group_id'] = local_var_params['server_group_id']

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
            resource_path='/v1/{project_id}/cloudservers/os-server-groups/{server_group_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteServerGroupMemberResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_server_metadata(self, request):
        """
        :param request: Request instance for DeleteServerMetadata
        :type request: :class:`g42cloudsdkecs.v2.DeleteServerMetadataRequest`
        :rtype: :class:`g42cloudsdkecs.v2.DeleteServerMetadataResponse`
        """
        return self.delete_server_metadata_with_http_info(request)

    def delete_server_metadata_with_http_info(self, request):
        all_params = ['key', 'server_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'key' in local_var_params:
            path_params['key'] = local_var_params['key']
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1/{project_id}/cloudservers/{server_id}/metadata/{key}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteServerMetadataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_server_password(self, request):
        """
        :param request: Request instance for DeleteServerPassword
        :type request: :class:`g42cloudsdkecs.v2.DeleteServerPasswordRequest`
        :rtype: :class:`g42cloudsdkecs.v2.DeleteServerPasswordResponse`
        """
        return self.delete_server_password_with_http_info(request)

    def delete_server_password_with_http_info(self, request):
        all_params = ['server_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1/{project_id}/cloudservers/{server_id}/os-server-password',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteServerPasswordResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_servers(self, request):
        """
        :param request: Request instance for DeleteServers
        :type request: :class:`g42cloudsdkecs.v2.DeleteServersRequest`
        :rtype: :class:`g42cloudsdkecs.v2.DeleteServersResponse`
        """
        return self.delete_servers_with_http_info(request)

    def delete_servers_with_http_info(self, request):
        all_params = ['delete_servers_request_body']
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
            resource_path='/v1/{project_id}/cloudservers/delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteServersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def detach_server_volume(self, request):
        """
        :param request: Request instance for DetachServerVolume
        :type request: :class:`g42cloudsdkecs.v2.DetachServerVolumeRequest`
        :rtype: :class:`g42cloudsdkecs.v2.DetachServerVolumeResponse`
        """
        return self.detach_server_volume_with_http_info(request)

    def detach_server_volume_with_http_info(self, request):
        all_params = ['server_id', 'volume_id', 'delete_flag']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']
        if 'volume_id' in local_var_params:
            path_params['volume_id'] = local_var_params['volume_id']

        query_params = []
        if 'delete_flag' in local_var_params:
            query_params.append(('delete_flag', local_var_params['delete_flag']))

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
            resource_path='/v1/{project_id}/cloudservers/{server_id}/detachvolume/{volume_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DetachServerVolumeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def disassociate_server_virtual_ip(self, request):
        """
        :param request: Request instance for DisassociateServerVirtualIp
        :type request: :class:`g42cloudsdkecs.v2.DisassociateServerVirtualIpRequest`
        :rtype: :class:`g42cloudsdkecs.v2.DisassociateServerVirtualIpResponse`
        """
        return self.disassociate_server_virtual_ip_with_http_info(request)

    def disassociate_server_virtual_ip_with_http_info(self, request):
        all_params = ['nic_id', 'disassociate_server_virtual_ip_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'nic_id' in local_var_params:
            path_params['nic_id'] = local_var_params['nic_id']

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
            resource_path='/v1/{project_id}/cloudservers/nics/{nic_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DisassociateServerVirtualIpResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_flavors(self, request):
        """
        :param request: Request instance for ListFlavors
        :type request: :class:`g42cloudsdkecs.v2.ListFlavorsRequest`
        :rtype: :class:`g42cloudsdkecs.v2.ListFlavorsResponse`
        """
        return self.list_flavors_with_http_info(request)

    def list_flavors_with_http_info(self, request):
        all_params = ['availability_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'availability_zone' in local_var_params:
            query_params.append(('availability_zone', local_var_params['availability_zone']))

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
            resource_path='/v1/{project_id}/cloudservers/flavors',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListFlavorsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_resize_flavors(self, request):
        """
        :param request: Request instance for ListResizeFlavors
        :type request: :class:`g42cloudsdkecs.v2.ListResizeFlavorsRequest`
        :rtype: :class:`g42cloudsdkecs.v2.ListResizeFlavorsResponse`
        """
        return self.list_resize_flavors_with_http_info(request)

    def list_resize_flavors_with_http_info(self, request):
        all_params = ['instance_uuid', 'limit', 'marker', 'sort_dir', 'sort_key', 'source_flavor_id', 'source_flavor_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instance_uuid' in local_var_params:
            query_params.append(('instance_uuid', local_var_params['instance_uuid']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'source_flavor_id' in local_var_params:
            query_params.append(('source_flavor_id', local_var_params['source_flavor_id']))
        if 'source_flavor_name' in local_var_params:
            query_params.append(('source_flavor_name', local_var_params['source_flavor_name']))

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
            resource_path='/v1/{project_id}/cloudservers/resize_flavors',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListResizeFlavorsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_server_block_devices(self, request):
        """
        :param request: Request instance for ListServerBlockDevices
        :type request: :class:`g42cloudsdkecs.v2.ListServerBlockDevicesRequest`
        :rtype: :class:`g42cloudsdkecs.v2.ListServerBlockDevicesResponse`
        """
        return self.list_server_block_devices_with_http_info(request)

    def list_server_block_devices_with_http_info(self, request):
        all_params = ['server_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1/{project_id}/cloudservers/{server_id}/block_device',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListServerBlockDevicesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_server_groups(self, request):
        """
        :param request: Request instance for ListServerGroups
        :type request: :class:`g42cloudsdkecs.v2.ListServerGroupsRequest`
        :rtype: :class:`g42cloudsdkecs.v2.ListServerGroupsResponse`
        """
        return self.list_server_groups_with_http_info(request)

    def list_server_groups_with_http_info(self, request):
        all_params = ['limit', 'marker']
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
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

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
            resource_path='/v1/{project_id}/cloudservers/os-server-groups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListServerGroupsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_server_interfaces(self, request):
        """
        :param request: Request instance for ListServerInterfaces
        :type request: :class:`g42cloudsdkecs.v2.ListServerInterfacesRequest`
        :rtype: :class:`g42cloudsdkecs.v2.ListServerInterfacesResponse`
        """
        return self.list_server_interfaces_with_http_info(request)

    def list_server_interfaces_with_http_info(self, request):
        all_params = ['server_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1/{project_id}/cloudservers/{server_id}/os-interface',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListServerInterfacesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_server_tags(self, request):
        """
        :param request: Request instance for ListServerTags
        :type request: :class:`g42cloudsdkecs.v2.ListServerTagsRequest`
        :rtype: :class:`g42cloudsdkecs.v2.ListServerTagsResponse`
        """
        return self.list_server_tags_with_http_info(request)

    def list_server_tags_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/cloudservers/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListServerTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_servers_details(self, request):
        """
        :param request: Request instance for ListServersDetails
        :type request: :class:`g42cloudsdkecs.v2.ListServersDetailsRequest`
        :rtype: :class:`g42cloudsdkecs.v2.ListServersDetailsResponse`
        """
        return self.list_servers_details_with_http_info(request)

    def list_servers_details_with_http_info(self, request):
        all_params = ['enterprise_project_id', 'flavor', 'ip', 'limit', 'name', 'not_tags', 'offset', 'reservation_id', 'status', 'tags', 'ip_eq']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'flavor' in local_var_params:
            query_params.append(('flavor', local_var_params['flavor']))
        if 'ip' in local_var_params:
            query_params.append(('ip', local_var_params['ip']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'not_tags' in local_var_params:
            query_params.append(('not-tags', local_var_params['not_tags']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'reservation_id' in local_var_params:
            query_params.append(('reservation_id', local_var_params['reservation_id']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
        if 'ip_eq' in local_var_params:
            query_params.append(('ip_eq', local_var_params['ip_eq']))

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
            resource_path='/v1/{project_id}/cloudservers/detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListServersDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def migrate_server(self, request):
        """
        :param request: Request instance for MigrateServer
        :type request: :class:`g42cloudsdkecs.v2.MigrateServerRequest`
        :rtype: :class:`g42cloudsdkecs.v2.MigrateServerResponse`
        """
        return self.migrate_server_with_http_info(request)

    def migrate_server_with_http_info(self, request):
        all_params = ['server_id', 'migrate_server_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1/{project_id}/cloudservers/{server_id}/migrate',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='MigrateServerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def nova_associate_security_group(self, request):
        """
        :param request: Request instance for NovaAssociateSecurityGroup
        :type request: :class:`g42cloudsdkecs.v2.NovaAssociateSecurityGroupRequest`
        :rtype: :class:`g42cloudsdkecs.v2.NovaAssociateSecurityGroupResponse`
        """
        return self.nova_associate_security_group_with_http_info(request)

    def nova_associate_security_group_with_http_info(self, request):
        all_params = ['server_id', 'nova_associate_security_group_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v2.1/{project_id}/servers/{server_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='NovaAssociateSecurityGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def nova_create_keypair(self, request):
        """
        :param request: Request instance for NovaCreateKeypair
        :type request: :class:`g42cloudsdkecs.v2.NovaCreateKeypairRequest`
        :rtype: :class:`g42cloudsdkecs.v2.NovaCreateKeypairResponse`
        """
        return self.nova_create_keypair_with_http_info(request)

    def nova_create_keypair_with_http_info(self, request):
        all_params = ['nova_create_keypair_request_body', 'open_stack_api_version']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'open_stack_api_version' in local_var_params:
            header_params['OpenStack-API-Version'] = local_var_params['open_stack_api_version']

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
            resource_path='/v2.1/{project_id}/os-keypairs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='NovaCreateKeypairResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def nova_create_servers(self, request):
        """
        :param request: Request instance for NovaCreateServers
        :type request: :class:`g42cloudsdkecs.v2.NovaCreateServersRequest`
        :rtype: :class:`g42cloudsdkecs.v2.NovaCreateServersResponse`
        """
        return self.nova_create_servers_with_http_info(request)

    def nova_create_servers_with_http_info(self, request):
        all_params = ['nova_create_servers_request_body', 'open_stack_api_version']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'open_stack_api_version' in local_var_params:
            header_params['OpenStack-API-Version'] = local_var_params['open_stack_api_version']

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
            resource_path='/v2.1/{project_id}/servers',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='NovaCreateServersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def nova_delete_keypair(self, request):
        """
        :param request: Request instance for NovaDeleteKeypair
        :type request: :class:`g42cloudsdkecs.v2.NovaDeleteKeypairRequest`
        :rtype: :class:`g42cloudsdkecs.v2.NovaDeleteKeypairResponse`
        """
        return self.nova_delete_keypair_with_http_info(request)

    def nova_delete_keypair_with_http_info(self, request):
        all_params = ['keypair_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'keypair_name' in local_var_params:
            path_params['keypair_name'] = local_var_params['keypair_name']

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
            resource_path='/v2.1/{project_id}/os-keypairs/{keypair_name}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='NovaDeleteKeypairResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def nova_delete_server(self, request):
        """
        :param request: Request instance for NovaDeleteServer
        :type request: :class:`g42cloudsdkecs.v2.NovaDeleteServerRequest`
        :rtype: :class:`g42cloudsdkecs.v2.NovaDeleteServerResponse`
        """
        return self.nova_delete_server_with_http_info(request)

    def nova_delete_server_with_http_info(self, request):
        all_params = ['server_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v2.1/{project_id}/servers/{server_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='NovaDeleteServerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def nova_disassociate_security_group(self, request):
        """
        :param request: Request instance for NovaDisassociateSecurityGroup
        :type request: :class:`g42cloudsdkecs.v2.NovaDisassociateSecurityGroupRequest`
        :rtype: :class:`g42cloudsdkecs.v2.NovaDisassociateSecurityGroupResponse`
        """
        return self.nova_disassociate_security_group_with_http_info(request)

    def nova_disassociate_security_group_with_http_info(self, request):
        all_params = ['server_id', 'nova_disassociate_security_group_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v2.1/{project_id}/servers/{server_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='NovaDisassociateSecurityGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def nova_list_availability_zones(self, request):
        """
        :param request: Request instance for NovaListAvailabilityZones
        :type request: :class:`g42cloudsdkecs.v2.NovaListAvailabilityZonesRequest`
        :rtype: :class:`g42cloudsdkecs.v2.NovaListAvailabilityZonesResponse`
        """
        return self.nova_list_availability_zones_with_http_info(request)

    def nova_list_availability_zones_with_http_info(self, request):
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
            resource_path='/v2.1/{project_id}/os-availability-zone',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='NovaListAvailabilityZonesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def nova_list_keypairs(self, request):
        """
        :param request: Request instance for NovaListKeypairs
        :type request: :class:`g42cloudsdkecs.v2.NovaListKeypairsRequest`
        :rtype: :class:`g42cloudsdkecs.v2.NovaListKeypairsResponse`
        """
        return self.nova_list_keypairs_with_http_info(request)

    def nova_list_keypairs_with_http_info(self, request):
        all_params = ['limit', 'marker', 'open_stack_api_version']
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
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

        header_params = {}
        if 'open_stack_api_version' in local_var_params:
            header_params['OpenStack-API-Version'] = local_var_params['open_stack_api_version']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.1/{project_id}/os-keypairs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='NovaListKeypairsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def nova_list_server_security_groups(self, request):
        """
        :param request: Request instance for NovaListServerSecurityGroups
        :type request: :class:`g42cloudsdkecs.v2.NovaListServerSecurityGroupsRequest`
        :rtype: :class:`g42cloudsdkecs.v2.NovaListServerSecurityGroupsResponse`
        """
        return self.nova_list_server_security_groups_with_http_info(request)

    def nova_list_server_security_groups_with_http_info(self, request):
        all_params = ['server_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v2.1/{project_id}/servers/{server_id}/os-security-groups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='NovaListServerSecurityGroupsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def nova_list_servers_details(self, request):
        """
        :param request: Request instance for NovaListServersDetails
        :type request: :class:`g42cloudsdkecs.v2.NovaListServersDetailsRequest`
        :rtype: :class:`g42cloudsdkecs.v2.NovaListServersDetailsResponse`
        """
        return self.nova_list_servers_details_with_http_info(request)

    def nova_list_servers_details_with_http_info(self, request):
        all_params = ['changes_since', 'flavor', 'image', 'ip', 'limit', 'marker', 'name', 'not_tags', 'reservation_id', 'sort_key', 'status', 'tags', 'open_stack_api_version']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'changes_since' in local_var_params:
            query_params.append(('changes-since', local_var_params['changes_since']))
        if 'flavor' in local_var_params:
            query_params.append(('flavor', local_var_params['flavor']))
        if 'image' in local_var_params:
            query_params.append(('image', local_var_params['image']))
        if 'ip' in local_var_params:
            query_params.append(('ip', local_var_params['ip']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'not_tags' in local_var_params:
            query_params.append(('not-tags', local_var_params['not_tags']))
        if 'reservation_id' in local_var_params:
            query_params.append(('reservation_id', local_var_params['reservation_id']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))

        header_params = {}
        if 'open_stack_api_version' in local_var_params:
            header_params['OpenStack-API-Version'] = local_var_params['open_stack_api_version']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.1/{project_id}/servers/detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='NovaListServersDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def nova_show_keypair(self, request):
        """
        :param request: Request instance for NovaShowKeypair
        :type request: :class:`g42cloudsdkecs.v2.NovaShowKeypairRequest`
        :rtype: :class:`g42cloudsdkecs.v2.NovaShowKeypairResponse`
        """
        return self.nova_show_keypair_with_http_info(request)

    def nova_show_keypair_with_http_info(self, request):
        all_params = ['keypair_name', 'open_stack_api_version']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'keypair_name' in local_var_params:
            path_params['keypair_name'] = local_var_params['keypair_name']

        query_params = []

        header_params = {}
        if 'open_stack_api_version' in local_var_params:
            header_params['OpenStack-API-Version'] = local_var_params['open_stack_api_version']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.1/{project_id}/os-keypairs/{keypair_name}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='NovaShowKeypairResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def nova_show_server(self, request):
        """
        :param request: Request instance for NovaShowServer
        :type request: :class:`g42cloudsdkecs.v2.NovaShowServerRequest`
        :rtype: :class:`g42cloudsdkecs.v2.NovaShowServerResponse`
        """
        return self.nova_show_server_with_http_info(request)

    def nova_show_server_with_http_info(self, request):
        all_params = ['server_id', 'open_stack_api_version']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

        query_params = []

        header_params = {}
        if 'open_stack_api_version' in local_var_params:
            header_params['OpenStack-API-Version'] = local_var_params['open_stack_api_version']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.1/{project_id}/servers/{server_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='NovaShowServerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def register_server_auto_recovery(self, request):
        """
        :param request: Request instance for RegisterServerAutoRecovery
        :type request: :class:`g42cloudsdkecs.v2.RegisterServerAutoRecoveryRequest`
        :rtype: :class:`g42cloudsdkecs.v2.RegisterServerAutoRecoveryResponse`
        """
        return self.register_server_auto_recovery_with_http_info(request)

    def register_server_auto_recovery_with_http_info(self, request):
        all_params = ['server_id', 'register_server_auto_recovery_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1/{project_id}/cloudservers/{server_id}/autorecovery',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RegisterServerAutoRecoveryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def register_server_monitor(self, request):
        """
        :param request: Request instance for RegisterServerMonitor
        :type request: :class:`g42cloudsdkecs.v2.RegisterServerMonitorRequest`
        :rtype: :class:`g42cloudsdkecs.v2.RegisterServerMonitorResponse`
        """
        return self.register_server_monitor_with_http_info(request)

    def register_server_monitor_with_http_info(self, request):
        all_params = ['server_id', 'register_server_monitor_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1.0/servers/{server_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RegisterServerMonitorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def reinstall_server_with_cloud_init(self, request):
        """
        :param request: Request instance for ReinstallServerWithCloudInit
        :type request: :class:`g42cloudsdkecs.v2.ReinstallServerWithCloudInitRequest`
        :rtype: :class:`g42cloudsdkecs.v2.ReinstallServerWithCloudInitResponse`
        """
        return self.reinstall_server_with_cloud_init_with_http_info(request)

    def reinstall_server_with_cloud_init_with_http_info(self, request):
        all_params = ['server_id', 'reinstall_server_with_cloud_init_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v2/{project_id}/cloudservers/{server_id}/reinstallos',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ReinstallServerWithCloudInitResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def reinstall_server_without_cloud_init(self, request):
        """
        :param request: Request instance for ReinstallServerWithoutCloudInit
        :type request: :class:`g42cloudsdkecs.v2.ReinstallServerWithoutCloudInitRequest`
        :rtype: :class:`g42cloudsdkecs.v2.ReinstallServerWithoutCloudInitResponse`
        """
        return self.reinstall_server_without_cloud_init_with_http_info(request)

    def reinstall_server_without_cloud_init_with_http_info(self, request):
        all_params = ['server_id', 'reinstall_server_without_cloud_init_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1/{project_id}/cloudservers/{server_id}/reinstallos',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ReinstallServerWithoutCloudInitResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def reset_server_password(self, request):
        """
        :param request: Request instance for ResetServerPassword
        :type request: :class:`g42cloudsdkecs.v2.ResetServerPasswordRequest`
        :rtype: :class:`g42cloudsdkecs.v2.ResetServerPasswordResponse`
        """
        return self.reset_server_password_with_http_info(request)

    def reset_server_password_with_http_info(self, request):
        all_params = ['server_id', 'reset_server_password_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1/{project_id}/cloudservers/{server_id}/os-reset-password',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ResetServerPasswordResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def resize_post_paid_server(self, request):
        """
        :param request: Request instance for ResizePostPaidServer
        :type request: :class:`g42cloudsdkecs.v2.ResizePostPaidServerRequest`
        :rtype: :class:`g42cloudsdkecs.v2.ResizePostPaidServerResponse`
        """
        return self.resize_post_paid_server_with_http_info(request)

    def resize_post_paid_server_with_http_info(self, request):
        all_params = ['server_id', 'resize_post_paid_server_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1/{project_id}/cloudservers/{server_id}/resize',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ResizePostPaidServerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def resize_server(self, request):
        """
        :param request: Request instance for ResizeServer
        :type request: :class:`g42cloudsdkecs.v2.ResizeServerRequest`
        :rtype: :class:`g42cloudsdkecs.v2.ResizeServerResponse`
        """
        return self.resize_server_with_http_info(request)

    def resize_server_with_http_info(self, request):
        all_params = ['server_id', 'resize_server_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1.1/{project_id}/cloudservers/{server_id}/resize',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ResizeServerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_reset_password_flag(self, request):
        """
        :param request: Request instance for ShowResetPasswordFlag
        :type request: :class:`g42cloudsdkecs.v2.ShowResetPasswordFlagRequest`
        :rtype: :class:`g42cloudsdkecs.v2.ShowResetPasswordFlagResponse`
        """
        return self.show_reset_password_flag_with_http_info(request)

    def show_reset_password_flag_with_http_info(self, request):
        all_params = ['server_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1/{project_id}/cloudservers/{server_id}/os-resetpwd-flag',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowResetPasswordFlagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_server(self, request):
        """
        :param request: Request instance for ShowServer
        :type request: :class:`g42cloudsdkecs.v2.ShowServerRequest`
        :rtype: :class:`g42cloudsdkecs.v2.ShowServerResponse`
        """
        return self.show_server_with_http_info(request)

    def show_server_with_http_info(self, request):
        all_params = ['server_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1/{project_id}/cloudservers/{server_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowServerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_server_auto_recovery(self, request):
        """
        :param request: Request instance for ShowServerAutoRecovery
        :type request: :class:`g42cloudsdkecs.v2.ShowServerAutoRecoveryRequest`
        :rtype: :class:`g42cloudsdkecs.v2.ShowServerAutoRecoveryResponse`
        """
        return self.show_server_auto_recovery_with_http_info(request)

    def show_server_auto_recovery_with_http_info(self, request):
        all_params = ['server_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1/{project_id}/cloudservers/{server_id}/autorecovery',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowServerAutoRecoveryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_server_block_device(self, request):
        """
        :param request: Request instance for ShowServerBlockDevice
        :type request: :class:`g42cloudsdkecs.v2.ShowServerBlockDeviceRequest`
        :rtype: :class:`g42cloudsdkecs.v2.ShowServerBlockDeviceResponse`
        """
        return self.show_server_block_device_with_http_info(request)

    def show_server_block_device_with_http_info(self, request):
        all_params = ['server_id', 'volume_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']
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
            resource_path='/v1/{project_id}/cloudservers/{server_id}/block_device/{volume_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowServerBlockDeviceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_server_group(self, request):
        """
        :param request: Request instance for ShowServerGroup
        :type request: :class:`g42cloudsdkecs.v2.ShowServerGroupRequest`
        :rtype: :class:`g42cloudsdkecs.v2.ShowServerGroupResponse`
        """
        return self.show_server_group_with_http_info(request)

    def show_server_group_with_http_info(self, request):
        all_params = ['server_group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_group_id' in local_var_params:
            path_params['server_group_id'] = local_var_params['server_group_id']

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
            resource_path='/v1/{project_id}/cloudservers/os-server-groups/{server_group_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowServerGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_server_limits(self, request):
        """
        :param request: Request instance for ShowServerLimits
        :type request: :class:`g42cloudsdkecs.v2.ShowServerLimitsRequest`
        :rtype: :class:`g42cloudsdkecs.v2.ShowServerLimitsResponse`
        """
        return self.show_server_limits_with_http_info(request)

    def show_server_limits_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/cloudservers/limits',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowServerLimitsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_server_password(self, request):
        """
        :param request: Request instance for ShowServerPassword
        :type request: :class:`g42cloudsdkecs.v2.ShowServerPasswordRequest`
        :rtype: :class:`g42cloudsdkecs.v2.ShowServerPasswordResponse`
        """
        return self.show_server_password_with_http_info(request)

    def show_server_password_with_http_info(self, request):
        all_params = ['server_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1/{project_id}/cloudservers/{server_id}/os-server-password',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowServerPasswordResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_server_remote_console(self, request):
        """
        :param request: Request instance for ShowServerRemoteConsole
        :type request: :class:`g42cloudsdkecs.v2.ShowServerRemoteConsoleRequest`
        :rtype: :class:`g42cloudsdkecs.v2.ShowServerRemoteConsoleResponse`
        """
        return self.show_server_remote_console_with_http_info(request)

    def show_server_remote_console_with_http_info(self, request):
        all_params = ['server_id', 'show_server_remote_console_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1/{project_id}/cloudservers/{server_id}/remote_console',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowServerRemoteConsoleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_server_tags(self, request):
        """
        :param request: Request instance for ShowServerTags
        :type request: :class:`g42cloudsdkecs.v2.ShowServerTagsRequest`
        :rtype: :class:`g42cloudsdkecs.v2.ShowServerTagsResponse`
        """
        return self.show_server_tags_with_http_info(request)

    def show_server_tags_with_http_info(self, request):
        all_params = ['server_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1/{project_id}/cloudservers/{server_id}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowServerTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_server(self, request):
        """
        :param request: Request instance for UpdateServer
        :type request: :class:`g42cloudsdkecs.v2.UpdateServerRequest`
        :rtype: :class:`g42cloudsdkecs.v2.UpdateServerResponse`
        """
        return self.update_server_with_http_info(request)

    def update_server_with_http_info(self, request):
        all_params = ['server_id', 'update_server_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1/{project_id}/cloudservers/{server_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateServerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_server_auto_terminate_time(self, request):
        """
        :param request: Request instance for UpdateServerAutoTerminateTime
        :type request: :class:`g42cloudsdkecs.v2.UpdateServerAutoTerminateTimeRequest`
        :rtype: :class:`g42cloudsdkecs.v2.UpdateServerAutoTerminateTimeResponse`
        """
        return self.update_server_auto_terminate_time_with_http_info(request)

    def update_server_auto_terminate_time_with_http_info(self, request):
        all_params = ['server_id', 'update_server_auto_terminate_time_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1/{project_id}/cloudservers/{server_id}/actions/update-auto-terminate-time',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateServerAutoTerminateTimeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_server_metadata(self, request):
        """
        :param request: Request instance for UpdateServerMetadata
        :type request: :class:`g42cloudsdkecs.v2.UpdateServerMetadataRequest`
        :rtype: :class:`g42cloudsdkecs.v2.UpdateServerMetadataResponse`
        """
        return self.update_server_metadata_with_http_info(request)

    def update_server_metadata_with_http_info(self, request):
        all_params = ['server_id', 'update_server_metadata_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1/{project_id}/cloudservers/{server_id}/metadata',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateServerMetadataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_job(self, request):
        """
        :param request: Request instance for ShowJob
        :type request: :class:`g42cloudsdkecs.v2.ShowJobRequest`
        :rtype: :class:`g42cloudsdkecs.v2.ShowJobResponse`
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
