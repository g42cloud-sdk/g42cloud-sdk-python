# coding: utf-8

from __future__ import absolute_import

import importlib

from g42cloudsdkcore.client import Client, ClientBuilder
from g42cloudsdkcore.utils import http_utils
from g42cloudsdkcore.sdk_stream_request import SdkStreamRequest


class ImsAsyncClient(Client):
    def __init__(self):
        super(ImsAsyncClient, self).__init__()
        self.model_package = importlib.import_module("g42cloudsdkims.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "ImsClient":
            raise TypeError("client type error, support client type is ImsClient")

        return ClientBuilder(clazz)

    def add_image_tag_async(self, request):
        """

        :param request: Request instance for AddImageTag
        :type request: :class:`g42cloudsdkims.v2.AddImageTagRequest`
        :rtype: :class:`g42cloudsdkims.v2.AddImageTagResponse`
        """
        return self._add_image_tag_with_http_info(request)

    def _add_image_tag_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']

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
            resource_path='/v2/{project_id}/images/{image_id}/tags',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddImageTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_add_members_async(self, request):
        """

        :param request: Request instance for BatchAddMembers
        :type request: :class:`g42cloudsdkims.v2.BatchAddMembersRequest`
        :rtype: :class:`g42cloudsdkims.v2.BatchAddMembersResponse`
        """
        return self._batch_add_members_with_http_info(request)

    def _batch_add_members_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v1/cloudimages/members',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchAddMembersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_add_or_delete_tags_async(self, request):
        """

        :param request: Request instance for BatchAddOrDeleteTags
        :type request: :class:`g42cloudsdkims.v2.BatchAddOrDeleteTagsRequest`
        :rtype: :class:`g42cloudsdkims.v2.BatchAddOrDeleteTagsResponse`
        """
        return self._batch_add_or_delete_tags_with_http_info(request)

    def _batch_add_or_delete_tags_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']

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
            resource_path='/v2/{project_id}/images/{image_id}/tags/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchAddOrDeleteTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_members_async(self, request):
        """

        :param request: Request instance for BatchDeleteMembers
        :type request: :class:`g42cloudsdkims.v2.BatchDeleteMembersRequest`
        :rtype: :class:`g42cloudsdkims.v2.BatchDeleteMembersResponse`
        """
        return self._batch_delete_members_with_http_info(request)

    def _batch_delete_members_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v1/cloudimages/members',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteMembersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_update_members_async(self, request):
        """

        :param request: Request instance for BatchUpdateMembers
        :type request: :class:`g42cloudsdkims.v2.BatchUpdateMembersRequest`
        :rtype: :class:`g42cloudsdkims.v2.BatchUpdateMembersResponse`
        """
        return self._batch_update_members_with_http_info(request)

    def _batch_update_members_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v1/cloudimages/members',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchUpdateMembersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def copy_image_cross_region_async(self, request):
        """

        :param request: Request instance for CopyImageCrossRegion
        :type request: :class:`g42cloudsdkims.v2.CopyImageCrossRegionRequest`
        :rtype: :class:`g42cloudsdkims.v2.CopyImageCrossRegionResponse`
        """
        return self._copy_image_cross_region_with_http_info(request)

    def _copy_image_cross_region_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']

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
            resource_path='/v1/cloudimages/{image_id}/cross_region_copy',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CopyImageCrossRegionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def copy_image_in_region_async(self, request):
        """

        :param request: Request instance for CopyImageInRegion
        :type request: :class:`g42cloudsdkims.v2.CopyImageInRegionRequest`
        :rtype: :class:`g42cloudsdkims.v2.CopyImageInRegionResponse`
        """
        return self._copy_image_in_region_with_http_info(request)

    def _copy_image_in_region_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']

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
            resource_path='/v1/cloudimages/{image_id}/copy',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CopyImageInRegionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_data_image_async(self, request):
        """

        :param request: Request instance for CreateDataImage
        :type request: :class:`g42cloudsdkims.v2.CreateDataImageRequest`
        :rtype: :class:`g42cloudsdkims.v2.CreateDataImageResponse`
        """
        return self._create_data_image_with_http_info(request)

    def _create_data_image_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v1/cloudimages/dataimages/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateDataImageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_image_async(self, request):
        """

        :param request: Request instance for CreateImage
        :type request: :class:`g42cloudsdkims.v2.CreateImageRequest`
        :rtype: :class:`g42cloudsdkims.v2.CreateImageResponse`
        """
        return self._create_image_with_http_info(request)

    def _create_image_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v2/cloudimages/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateImageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_or_update_tags_async(self, request):
        """

        :param request: Request instance for CreateOrUpdateTags
        :type request: :class:`g42cloudsdkims.v2.CreateOrUpdateTagsRequest`
        :rtype: :class:`g42cloudsdkims.v2.CreateOrUpdateTagsResponse`
        """
        return self._create_or_update_tags_with_http_info(request)

    def _create_or_update_tags_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v1/cloudimages/tags',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateOrUpdateTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_whole_image_async(self, request):
        """

        :param request: Request instance for CreateWholeImage
        :type request: :class:`g42cloudsdkims.v2.CreateWholeImageRequest`
        :rtype: :class:`g42cloudsdkims.v2.CreateWholeImageResponse`
        """
        return self._create_whole_image_with_http_info(request)

    def _create_whole_image_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v1/cloudimages/wholeimages/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateWholeImageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_image_tag_async(self, request):
        """

        :param request: Request instance for DeleteImageTag
        :type request: :class:`g42cloudsdkims.v2.DeleteImageTagRequest`
        :rtype: :class:`g42cloudsdkims.v2.DeleteImageTagResponse`
        """
        return self._delete_image_tag_with_http_info(request)

    def _delete_image_tag_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']
        if 'key' in local_var_params:
            path_params['key'] = local_var_params['key']

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
            resource_path='/v2/{project_id}/images/{image_id}/tags/{key}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteImageTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def export_image_async(self, request):
        """

        :param request: Request instance for ExportImage
        :type request: :class:`g42cloudsdkims.v2.ExportImageRequest`
        :rtype: :class:`g42cloudsdkims.v2.ExportImageResponse`
        """
        return self._export_image_with_http_info(request)

    def _export_image_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']

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
            resource_path='/v1/cloudimages/{image_id}/file',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExportImageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def import_image_quick_async(self, request):
        """

        :param request: Request instance for ImportImageQuick
        :type request: :class:`g42cloudsdkims.v2.ImportImageQuickRequest`
        :rtype: :class:`g42cloudsdkims.v2.ImportImageQuickResponse`
        """
        return self._import_image_quick_with_http_info(request)

    def _import_image_quick_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v2/cloudimages/quickimport/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ImportImageQuickResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_image_by_tags_async(self, request):
        """

        :param request: Request instance for ListImageByTags
        :type request: :class:`g42cloudsdkims.v2.ListImageByTagsRequest`
        :rtype: :class:`g42cloudsdkims.v2.ListImageByTagsResponse`
        """
        return self._list_image_by_tags_with_http_info(request)

    def _list_image_by_tags_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v2/{project_id}/images/resource_instances/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListImageByTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_image_tags_async(self, request):
        """

        :param request: Request instance for ListImageTags
        :type request: :class:`g42cloudsdkims.v2.ListImageTagsRequest`
        :rtype: :class:`g42cloudsdkims.v2.ListImageTagsResponse`
        """
        return self._list_image_tags_with_http_info(request)

    def _list_image_tags_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']

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
            resource_path='/v2/{project_id}/images/{image_id}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListImageTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_images_async(self, request):
        """

        :param request: Request instance for ListImages
        :type request: :class:`g42cloudsdkims.v2.ListImagesRequest`
        :rtype: :class:`g42cloudsdkims.v2.ListImagesResponse`
        """
        return self._list_images_with_http_info(request)

    def _list_images_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'imagetype' in local_var_params:
            query_params.append(('__imagetype', local_var_params['imagetype']))
        if 'isregistered' in local_var_params:
            query_params.append(('__isregistered', local_var_params['isregistered']))
        if 'os_bit' in local_var_params:
            query_params.append(('__os_bit', local_var_params['os_bit']))
        if 'os_type' in local_var_params:
            query_params.append(('__os_type', local_var_params['os_type']))
        if 'platform' in local_var_params:
            query_params.append(('__platform', local_var_params['platform']))
        if 'support_diskintensive' in local_var_params:
            query_params.append(('__support_diskintensive', local_var_params['support_diskintensive']))
        if 'support_highperformance' in local_var_params:
            query_params.append(('__support_highperformance', local_var_params['support_highperformance']))
        if 'support_kvm' in local_var_params:
            query_params.append(('__support_kvm', local_var_params['support_kvm']))
        if 'support_kvm_gpu_type' in local_var_params:
            query_params.append(('__support_kvm_gpu_type', local_var_params['support_kvm_gpu_type']))
        if 'support_kvm_infiniband' in local_var_params:
            query_params.append(('__support_kvm_infiniband', local_var_params['support_kvm_infiniband']))
        if 'support_largememory' in local_var_params:
            query_params.append(('__support_largememory', local_var_params['support_largememory']))
        if 'support_xen' in local_var_params:
            query_params.append(('__support_xen', local_var_params['support_xen']))
        if 'support_xen_gpu_type' in local_var_params:
            query_params.append(('__support_xen_gpu_type', local_var_params['support_xen_gpu_type']))
        if 'support_xen_hana' in local_var_params:
            query_params.append(('__support_xen_hana', local_var_params['support_xen_hana']))
        if 'container_format' in local_var_params:
            query_params.append(('container_format', local_var_params['container_format']))
        if 'disk_format' in local_var_params:
            query_params.append(('disk_format', local_var_params['disk_format']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'member_status' in local_var_params:
            query_params.append(('member_status', local_var_params['member_status']))
        if 'min_disk' in local_var_params:
            query_params.append(('min_disk', local_var_params['min_disk']))
        if 'min_ram' in local_var_params:
            query_params.append(('min_ram', local_var_params['min_ram']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'owner' in local_var_params:
            query_params.append(('owner', local_var_params['owner']))
        if 'protected' in local_var_params:
            query_params.append(('protected', local_var_params['protected']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'tag' in local_var_params:
            query_params.append(('tag', local_var_params['tag']))
        if 'virtual_env_type' in local_var_params:
            query_params.append(('virtual_env_type', local_var_params['virtual_env_type']))
        if 'visibility' in local_var_params:
            query_params.append(('visibility', local_var_params['visibility']))
        if 'flavor_id' in local_var_params:
            query_params.append(('flavor_id', local_var_params['flavor_id']))
        if 'created_at' in local_var_params:
            query_params.append(('created_at', local_var_params['created_at']))
        if 'updated_at' in local_var_params:
            query_params.append(('updated_at', local_var_params['updated_at']))
        if 'architecture' in local_var_params:
            query_params.append(('architecture', local_var_params['architecture']))

        header_params = {}
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/cloudimages',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListImagesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_images_tags_async(self, request):
        """

        :param request: Request instance for ListImagesTags
        :type request: :class:`g42cloudsdkims.v2.ListImagesTagsRequest`
        :rtype: :class:`g42cloudsdkims.v2.ListImagesTagsResponse`
        """
        return self._list_images_tags_with_http_info(request)

    def _list_images_tags_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v2/{project_id}/images/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListImagesTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_os_versions_async(self, request):
        """

        :param request: Request instance for ListOsVersions
        :type request: :class:`g42cloudsdkims.v2.ListOsVersionsRequest`
        :rtype: :class:`g42cloudsdkims.v2.ListOsVersionsResponse`
        """
        return self._list_os_versions_with_http_info(request)

    def _list_os_versions_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'tag' in local_var_params:
            query_params.append(('tag', local_var_params['tag']))

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
            resource_path='/v1/cloudimages/os_version',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListOsVersionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_tags_async(self, request):
        """

        :param request: Request instance for ListTags
        :type request: :class:`g42cloudsdkims.v2.ListTagsRequest`
        :rtype: :class:`g42cloudsdkims.v2.ListTagsResponse`
        """
        return self._list_tags_with_http_info(request)

    def _list_tags_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'imagetype' in local_var_params:
            query_params.append(('__imagetype', local_var_params['imagetype']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'min_disk' in local_var_params:
            query_params.append(('min_disk', local_var_params['min_disk']))
        if 'platform' in local_var_params:
            query_params.append(('__platform', local_var_params['platform']))
        if 'os_type' in local_var_params:
            query_params.append(('__os_type', local_var_params['os_type']))
        if 'member_status' in local_var_params:
            query_params.append(('member_status', local_var_params['member_status']))
        if 'virtual_env_type' in local_var_params:
            query_params.append(('virtual_env_type', local_var_params['virtual_env_type']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'architecture' in local_var_params:
            query_params.append(('architecture', local_var_params['architecture']))
        if 'created_at' in local_var_params:
            query_params.append(('created_at', local_var_params['created_at']))
        if 'updated_at' in local_var_params:
            query_params.append(('updated_at', local_var_params['updated_at']))

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
            resource_path='/v1/cloudimages/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def register_image_async(self, request):
        """

        :param request: Request instance for RegisterImage
        :type request: :class:`g42cloudsdkims.v2.RegisterImageRequest`
        :rtype: :class:`g42cloudsdkims.v2.RegisterImageResponse`
        """
        return self._register_image_with_http_info(request)

    def _register_image_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']

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
            resource_path='/v1/cloudimages/{image_id}/upload',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RegisterImageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_image_quota_async(self, request):
        """

        :param request: Request instance for ShowImageQuota
        :type request: :class:`g42cloudsdkims.v2.ShowImageQuotaRequest`
        :rtype: :class:`g42cloudsdkims.v2.ShowImageQuotaResponse`
        """
        return self._show_image_quota_with_http_info(request)

    def _show_image_quota_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v1/cloudimages/quota',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowImageQuotaResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_job_async(self, request):
        """

        :param request: Request instance for ShowJob
        :type request: :class:`g42cloudsdkims.v2.ShowJobRequest`
        :rtype: :class:`g42cloudsdkims.v2.ShowJobResponse`
        """
        return self._show_job_with_http_info(request)

    def _show_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def show_job_progress_async(self, request):
        """

        :param request: Request instance for ShowJobProgress
        :type request: :class:`g42cloudsdkims.v2.ShowJobProgressRequest`
        :rtype: :class:`g42cloudsdkims.v2.ShowJobProgressResponse`
        """
        return self._show_job_progress_with_http_info(request)

    def _show_job_progress_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v1/cloudimages/job/{job_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowJobProgressResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_image_async(self, request):
        """

        :param request: Request instance for UpdateImage
        :type request: :class:`g42cloudsdkims.v2.UpdateImageRequest`
        :rtype: :class:`g42cloudsdkims.v2.UpdateImageResponse`
        """
        return self._update_image_with_http_info(request)

    def _update_image_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']

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
            resource_path='/v2/cloudimages/{image_id}',
            method='PATCH',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateImageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_versions_async(self, request):
        """

        :param request: Request instance for ListVersions
        :type request: :class:`g42cloudsdkims.v2.ListVersionsRequest`
        :rtype: :class:`g42cloudsdkims.v2.ListVersionsResponse`
        """
        return self._list_versions_with_http_info(request)

    def _list_versions_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def show_version_async(self, request):
        """

        :param request: Request instance for ShowVersion
        :type request: :class:`g42cloudsdkims.v2.ShowVersionRequest`
        :rtype: :class:`g42cloudsdkims.v2.ShowVersionResponse`
        """
        return self._show_version_with_http_info(request)

    def _show_version_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def glance_add_image_member_async(self, request):
        """

        :param request: Request instance for GlanceAddImageMember
        :type request: :class:`g42cloudsdkims.v2.GlanceAddImageMemberRequest`
        :rtype: :class:`g42cloudsdkims.v2.GlanceAddImageMemberResponse`
        """
        return self._glance_add_image_member_with_http_info(request)

    def _glance_add_image_member_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']

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
            resource_path='/v2/images/{image_id}/members',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='GlanceAddImageMemberResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def glance_create_image_metadata_async(self, request):
        """

        :param request: Request instance for GlanceCreateImageMetadata
        :type request: :class:`g42cloudsdkims.v2.GlanceCreateImageMetadataRequest`
        :rtype: :class:`g42cloudsdkims.v2.GlanceCreateImageMetadataResponse`
        """
        return self._glance_create_image_metadata_with_http_info(request)

    def _glance_create_image_metadata_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v2/images',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='GlanceCreateImageMetadataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def glance_create_tag_async(self, request):
        """

        :param request: Request instance for GlanceCreateTag
        :type request: :class:`g42cloudsdkims.v2.GlanceCreateTagRequest`
        :rtype: :class:`g42cloudsdkims.v2.GlanceCreateTagResponse`
        """
        return self._glance_create_tag_with_http_info(request)

    def _glance_create_tag_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']
        if 'tag' in local_var_params:
            path_params['tag'] = local_var_params['tag']

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
            resource_path='/v2/images/{image_id}/tags/{tag}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='GlanceCreateTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def glance_delete_image_async(self, request):
        """

        :param request: Request instance for GlanceDeleteImage
        :type request: :class:`g42cloudsdkims.v2.GlanceDeleteImageRequest`
        :rtype: :class:`g42cloudsdkims.v2.GlanceDeleteImageResponse`
        """
        return self._glance_delete_image_with_http_info(request)

    def _glance_delete_image_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']

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
            resource_path='/v2/images/{image_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='GlanceDeleteImageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def glance_delete_image_member_async(self, request):
        """

        :param request: Request instance for GlanceDeleteImageMember
        :type request: :class:`g42cloudsdkims.v2.GlanceDeleteImageMemberRequest`
        :rtype: :class:`g42cloudsdkims.v2.GlanceDeleteImageMemberResponse`
        """
        return self._glance_delete_image_member_with_http_info(request)

    def _glance_delete_image_member_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']
        if 'member_id' in local_var_params:
            path_params['member_id'] = local_var_params['member_id']

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
            resource_path='/v2/images/{image_id}/members/{member_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='GlanceDeleteImageMemberResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def glance_delete_tag_async(self, request):
        """

        :param request: Request instance for GlanceDeleteTag
        :type request: :class:`g42cloudsdkims.v2.GlanceDeleteTagRequest`
        :rtype: :class:`g42cloudsdkims.v2.GlanceDeleteTagResponse`
        """
        return self._glance_delete_tag_with_http_info(request)

    def _glance_delete_tag_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']
        if 'tag' in local_var_params:
            path_params['tag'] = local_var_params['tag']

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
            resource_path='/v2/images/{image_id}/tags/{tag}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='GlanceDeleteTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def glance_list_image_member_schemas_async(self, request):
        """

        :param request: Request instance for GlanceListImageMemberSchemas
        :type request: :class:`g42cloudsdkims.v2.GlanceListImageMemberSchemasRequest`
        :rtype: :class:`g42cloudsdkims.v2.GlanceListImageMemberSchemasResponse`
        """
        return self._glance_list_image_member_schemas_with_http_info(request)

    def _glance_list_image_member_schemas_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v2/schemas/members',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='GlanceListImageMemberSchemasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def glance_list_image_members_async(self, request):
        """

        :param request: Request instance for GlanceListImageMembers
        :type request: :class:`g42cloudsdkims.v2.GlanceListImageMembersRequest`
        :rtype: :class:`g42cloudsdkims.v2.GlanceListImageMembersResponse`
        """
        return self._glance_list_image_members_with_http_info(request)

    def _glance_list_image_members_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']

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
            resource_path='/v2/images/{image_id}/members',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='GlanceListImageMembersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def glance_list_image_schemas_async(self, request):
        """

        :param request: Request instance for GlanceListImageSchemas
        :type request: :class:`g42cloudsdkims.v2.GlanceListImageSchemasRequest`
        :rtype: :class:`g42cloudsdkims.v2.GlanceListImageSchemasResponse`
        """
        return self._glance_list_image_schemas_with_http_info(request)

    def _glance_list_image_schemas_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v2/schemas/images',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='GlanceListImageSchemasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def glance_list_images_async(self, request):
        """

        :param request: Request instance for GlanceListImages
        :type request: :class:`g42cloudsdkims.v2.GlanceListImagesRequest`
        :rtype: :class:`g42cloudsdkims.v2.GlanceListImagesResponse`
        """
        return self._glance_list_images_with_http_info(request)

    def _glance_list_images_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'imagetype' in local_var_params:
            query_params.append(('__imagetype', local_var_params['imagetype']))
        if 'isregistered' in local_var_params:
            query_params.append(('__isregistered', local_var_params['isregistered']))
        if 'os_bit' in local_var_params:
            query_params.append(('__os_bit', local_var_params['os_bit']))
        if 'os_type' in local_var_params:
            query_params.append(('__os_type', local_var_params['os_type']))
        if 'platform' in local_var_params:
            query_params.append(('__platform', local_var_params['platform']))
        if 'support_diskintensive' in local_var_params:
            query_params.append(('__support_diskintensive', local_var_params['support_diskintensive']))
        if 'support_highperformance' in local_var_params:
            query_params.append(('__support_highperformance', local_var_params['support_highperformance']))
        if 'support_kvm' in local_var_params:
            query_params.append(('__support_kvm', local_var_params['support_kvm']))
        if 'support_kvm_gpu_type' in local_var_params:
            query_params.append(('__support_kvm_gpu_type', local_var_params['support_kvm_gpu_type']))
        if 'support_kvm_infiniband' in local_var_params:
            query_params.append(('__support_kvm_infiniband', local_var_params['support_kvm_infiniband']))
        if 'support_largememory' in local_var_params:
            query_params.append(('__support_largememory', local_var_params['support_largememory']))
        if 'support_xen' in local_var_params:
            query_params.append(('__support_xen', local_var_params['support_xen']))
        if 'support_xen_gpu_type' in local_var_params:
            query_params.append(('__support_xen_gpu_type', local_var_params['support_xen_gpu_type']))
        if 'support_xen_hana' in local_var_params:
            query_params.append(('__support_xen_hana', local_var_params['support_xen_hana']))
        if 'container_format' in local_var_params:
            query_params.append(('container_format', local_var_params['container_format']))
        if 'disk_format' in local_var_params:
            query_params.append(('disk_format', local_var_params['disk_format']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'member_status' in local_var_params:
            query_params.append(('member_status', local_var_params['member_status']))
        if 'min_disk' in local_var_params:
            query_params.append(('min_disk', local_var_params['min_disk']))
        if 'min_ram' in local_var_params:
            query_params.append(('min_ram', local_var_params['min_ram']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'owner' in local_var_params:
            query_params.append(('owner', local_var_params['owner']))
        if 'protected' in local_var_params:
            query_params.append(('protected', local_var_params['protected']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'tag' in local_var_params:
            query_params.append(('tag', local_var_params['tag']))
        if 'visibility' in local_var_params:
            query_params.append(('visibility', local_var_params['visibility']))
        if 'created_at' in local_var_params:
            query_params.append(('created_at', local_var_params['created_at']))
        if 'updated_at' in local_var_params:
            query_params.append(('updated_at', local_var_params['updated_at']))

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
            resource_path='/v2/images',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='GlanceListImagesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def glance_show_image_async(self, request):
        """

        :param request: Request instance for GlanceShowImage
        :type request: :class:`g42cloudsdkims.v2.GlanceShowImageRequest`
        :rtype: :class:`g42cloudsdkims.v2.GlanceShowImageResponse`
        """
        return self._glance_show_image_with_http_info(request)

    def _glance_show_image_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']

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
            resource_path='/v2/images/{image_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='GlanceShowImageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def glance_show_image_member_async(self, request):
        """

        :param request: Request instance for GlanceShowImageMember
        :type request: :class:`g42cloudsdkims.v2.GlanceShowImageMemberRequest`
        :rtype: :class:`g42cloudsdkims.v2.GlanceShowImageMemberResponse`
        """
        return self._glance_show_image_member_with_http_info(request)

    def _glance_show_image_member_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']
        if 'member_id' in local_var_params:
            path_params['member_id'] = local_var_params['member_id']

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
            resource_path='/v2/images/{image_id}/members/{member_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='GlanceShowImageMemberResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def glance_show_image_member_schemas_async(self, request):
        """

        :param request: Request instance for GlanceShowImageMemberSchemas
        :type request: :class:`g42cloudsdkims.v2.GlanceShowImageMemberSchemasRequest`
        :rtype: :class:`g42cloudsdkims.v2.GlanceShowImageMemberSchemasResponse`
        """
        return self._glance_show_image_member_schemas_with_http_info(request)

    def _glance_show_image_member_schemas_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v2/schemas/member',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='GlanceShowImageMemberSchemasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def glance_show_image_schemas_async(self, request):
        """

        :param request: Request instance for GlanceShowImageSchemas
        :type request: :class:`g42cloudsdkims.v2.GlanceShowImageSchemasRequest`
        :rtype: :class:`g42cloudsdkims.v2.GlanceShowImageSchemasResponse`
        """
        return self._glance_show_image_schemas_with_http_info(request)

    def _glance_show_image_schemas_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v2/schemas/image',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='GlanceShowImageSchemasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def glance_update_image_async(self, request):
        """

        :param request: Request instance for GlanceUpdateImage
        :type request: :class:`g42cloudsdkims.v2.GlanceUpdateImageRequest`
        :rtype: :class:`g42cloudsdkims.v2.GlanceUpdateImageResponse`
        """
        return self._glance_update_image_with_http_info(request)

    def _glance_update_image_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']

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
            ['application/openstack-images-v2.1-json-patch'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/images/{image_id}',
            method='PATCH',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='GlanceUpdateImageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def glance_update_image_member_async(self, request):
        """

        :param request: Request instance for GlanceUpdateImageMember
        :type request: :class:`g42cloudsdkims.v2.GlanceUpdateImageMemberRequest`
        :rtype: :class:`g42cloudsdkims.v2.GlanceUpdateImageMemberResponse`
        """
        return self._glance_update_image_member_with_http_info(request)

    def _glance_update_image_member_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']
        if 'member_id' in local_var_params:
            path_params['member_id'] = local_var_params['member_id']

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
            resource_path='/v2/images/{image_id}/members/{member_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='GlanceUpdateImageMemberResponse',
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
        :param header_params: Header parameters to be
            placed in the request header.
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
            request_type=request_type,
	    async_request=True)
