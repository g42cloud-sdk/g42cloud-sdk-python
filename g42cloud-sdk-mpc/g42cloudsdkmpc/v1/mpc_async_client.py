# coding: utf-8

from __future__ import absolute_import

import importlib

from g42cloudsdkcore.client import Client, ClientBuilder
from g42cloudsdkcore.utils import http_utils
from g42cloudsdkcore.sdk_stream_request import SdkStreamRequest


class MpcAsyncClient(Client):
    def __init__(self):
        super(MpcAsyncClient, self).__init__()
        self.model_package = importlib.import_module("g42cloudsdkmpc.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "MpcClient":
            raise TypeError("client type error, support client type is MpcClient")

        return ClientBuilder(clazz)

    def create_animated_graphics_task_async(self, request):
        """

        :param request: Request instance for CreateAnimatedGraphicsTask
        :type request: :class:`g42cloudsdkmpc.v1.CreateAnimatedGraphicsTaskRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.CreateAnimatedGraphicsTaskResponse`
        """
        return self._create_animated_graphics_task_with_http_info(request)

    def _create_animated_graphics_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/animated-graphics',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateAnimatedGraphicsTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_animated_graphics_task_async(self, request):
        """

        :param request: Request instance for DeleteAnimatedGraphicsTask
        :type request: :class:`g42cloudsdkmpc.v1.DeleteAnimatedGraphicsTaskRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.DeleteAnimatedGraphicsTaskResponse`
        """
        return self._delete_animated_graphics_task_with_http_info(request)

    def _delete_animated_graphics_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
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
            resource_path='/v1/{project_id}/animated-graphics',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteAnimatedGraphicsTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_animated_graphics_task_async(self, request):
        """

        :param request: Request instance for ListAnimatedGraphicsTask
        :type request: :class:`g42cloudsdkmpc.v1.ListAnimatedGraphicsTaskRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.ListAnimatedGraphicsTaskResponse`
        """
        return self._list_animated_graphics_task_with_http_info(request)

    def _list_animated_graphics_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
            collection_formats['task_id'] = 'multi'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']
        if 'x_language' in local_var_params:
            header_params['x-language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/animated-graphics',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAnimatedGraphicsTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_agencies_task_async(self, request):
        """

        :param request: Request instance for CreateAgenciesTask
        :type request: :class:`g42cloudsdkmpc.v1.CreateAgenciesTaskRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.CreateAgenciesTaskResponse`
        """
        return self._create_agencies_task_with_http_info(request)

    def _create_agencies_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/agencies',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateAgenciesTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_all_buckets_async(self, request):
        """

        :param request: Request instance for ListAllBuckets
        :type request: :class:`g42cloudsdkmpc.v1.ListAllBucketsRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.ListAllBucketsResponse`
        """
        return self._list_all_buckets_with_http_info(request)

    def _list_all_buckets_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
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
            resource_path='/v1/{project_id}/buckets',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAllBucketsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_all_obs_obj_list_async(self, request):
        """

        :param request: Request instance for ListAllObsObjList
        :type request: :class:`g42cloudsdkmpc.v1.ListAllObsObjListRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.ListAllObsObjListResponse`
        """
        return self._list_all_obs_obj_list_with_http_info(request)

    def _list_all_obs_obj_list_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'bucket' in local_var_params:
            query_params.append(('bucket', local_var_params['bucket']))
        if 'prefix' in local_var_params:
            query_params.append(('prefix', local_var_params['prefix']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
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
            resource_path='/v1.0-ext/{project_id}/objects',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAllObsObjListResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_notify_event_async(self, request):
        """

        :param request: Request instance for ListNotifyEvent
        :type request: :class:`g42cloudsdkmpc.v1.ListNotifyEventRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.ListNotifyEventResponse`
        """
        return self._list_notify_event_with_http_info(request)

    def _list_notify_event_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
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
            resource_path='/v1/{project_id}/notification/event',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListNotifyEventResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_notify_smn_topic_config_async(self, request):
        """

        :param request: Request instance for ListNotifySmnTopicConfig
        :type request: :class:`g42cloudsdkmpc.v1.ListNotifySmnTopicConfigRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.ListNotifySmnTopicConfigResponse`
        """
        return self._list_notify_smn_topic_config_with_http_info(request)

    def _list_notify_smn_topic_config_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
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
            resource_path='/v1/{project_id}/notification',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListNotifySmnTopicConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def notify_smn_topic_config_async(self, request):
        """

        :param request: Request instance for NotifySmnTopicConfig
        :type request: :class:`g42cloudsdkmpc.v1.NotifySmnTopicConfigRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.NotifySmnTopicConfigResponse`
        """
        return self._notify_smn_topic_config_with_http_info(request)

    def _notify_smn_topic_config_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/notification',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='NotifySmnTopicConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_agencies_task_async(self, request):
        """

        :param request: Request instance for ShowAgenciesTask
        :type request: :class:`g42cloudsdkmpc.v1.ShowAgenciesTaskRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.ShowAgenciesTaskResponse`
        """
        return self._show_agencies_task_with_http_info(request)

    def _show_agencies_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
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
            resource_path='/v1/{project_id}/agencies',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAgenciesTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_bucket_authorized_async(self, request):
        """

        :param request: Request instance for UpdateBucketAuthorized
        :type request: :class:`g42cloudsdkmpc.v1.UpdateBucketAuthorizedRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.UpdateBucketAuthorizedResponse`
        """
        return self._update_bucket_authorized_with_http_info(request)

    def _update_bucket_authorized_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/authority',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateBucketAuthorizedResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_editing_job_async(self, request):
        """

        :param request: Request instance for CreateEditingJob
        :type request: :class:`g42cloudsdkmpc.v1.CreateEditingJobRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.CreateEditingJobResponse`
        """
        return self._create_editing_job_with_http_info(request)

    def _create_editing_job_with_http_info(self, request):
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/editing/jobs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateEditingJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_editing_job_async(self, request):
        """

        :param request: Request instance for DeleteEditingJob
        :type request: :class:`g42cloudsdkmpc.v1.DeleteEditingJobRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.DeleteEditingJobResponse`
        """
        return self._delete_editing_job_with_http_info(request)

    def _delete_editing_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'job_id' in local_var_params:
            query_params.append(('job_id', local_var_params['job_id']))

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
            resource_path='/v1/{project_id}/editing/jobs',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteEditingJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_editing_job_async(self, request):
        """

        :param request: Request instance for ListEditingJob
        :type request: :class:`g42cloudsdkmpc.v1.ListEditingJobRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.ListEditingJobResponse`
        """
        return self._list_editing_job_with_http_info(request)

    def _list_editing_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'job_id' in local_var_params:
            query_params.append(('job_id', local_var_params['job_id']))
            collection_formats['job_id'] = 'multi'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['x-language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/editing/jobs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEditingJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_encrypt_task_async(self, request):
        """

        :param request: Request instance for CreateEncryptTask
        :type request: :class:`g42cloudsdkmpc.v1.CreateEncryptTaskRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.CreateEncryptTaskResponse`
        """
        return self._create_encrypt_task_with_http_info(request)

    def _create_encrypt_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/encryptions',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateEncryptTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_encrypt_task_async(self, request):
        """

        :param request: Request instance for DeleteEncryptTask
        :type request: :class:`g42cloudsdkmpc.v1.DeleteEncryptTaskRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.DeleteEncryptTaskResponse`
        """
        return self._delete_encrypt_task_with_http_info(request)

    def _delete_encrypt_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
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
            resource_path='/v1/{project_id}/encryptions',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteEncryptTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_encrypt_task_async(self, request):
        """

        :param request: Request instance for ListEncryptTask
        :type request: :class:`g42cloudsdkmpc.v1.ListEncryptTaskRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.ListEncryptTaskResponse`
        """
        return self._list_encrypt_task_with_http_info(request)

    def _list_encrypt_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
            collection_formats['task_id'] = 'multi'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
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
            resource_path='/v1/{project_id}/encryptions',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEncryptTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_extract_task_async(self, request):
        """

        :param request: Request instance for CreateExtractTask
        :type request: :class:`g42cloudsdkmpc.v1.CreateExtractTaskRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.CreateExtractTaskResponse`
        """
        return self._create_extract_task_with_http_info(request)

    def _create_extract_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/extract-metadata',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateExtractTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_extract_task_async(self, request):
        """

        :param request: Request instance for DeleteExtractTask
        :type request: :class:`g42cloudsdkmpc.v1.DeleteExtractTaskRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.DeleteExtractTaskResponse`
        """
        return self._delete_extract_task_with_http_info(request)

    def _delete_extract_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
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
            resource_path='/v1/{project_id}/extract-metadata',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteExtractTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_extract_task_async(self, request):
        """

        :param request: Request instance for ListExtractTask
        :type request: :class:`g42cloudsdkmpc.v1.ListExtractTaskRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.ListExtractTaskResponse`
        """
        return self._list_extract_task_with_http_info(request)

    def _list_extract_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
            collection_formats['task_id'] = 'multi'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']
        if 'x_language' in local_var_params:
            header_params['x-language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/extract-metadata',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListExtractTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_mb_tasks_report_async(self, request):
        """

        :param request: Request instance for CreateMbTasksReport
        :type request: :class:`g42cloudsdkmpc.v1.CreateMbTasksReportRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.CreateMbTasksReportResponse`
        """
        return self._create_mb_tasks_report_with_http_info(request)

    def _create_mb_tasks_report_with_http_info(self, request):
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/mediabox/tasks/report',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateMbTasksReportResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_merge_channels_task_async(self, request):
        """

        :param request: Request instance for CreateMergeChannelsTask
        :type request: :class:`g42cloudsdkmpc.v1.CreateMergeChannelsTaskRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.CreateMergeChannelsTaskResponse`
        """
        return self._create_merge_channels_task_with_http_info(request)

    def _create_merge_channels_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/audio/services/merge_channels/task',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateMergeChannelsTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_reset_tracks_task_async(self, request):
        """

        :param request: Request instance for CreateResetTracksTask
        :type request: :class:`g42cloudsdkmpc.v1.CreateResetTracksTaskRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.CreateResetTracksTaskResponse`
        """
        return self._create_reset_tracks_task_with_http_info(request)

    def _create_reset_tracks_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/audio/services/reset_tracks/task',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateResetTracksTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_merge_channels_task_async(self, request):
        """

        :param request: Request instance for DeleteMergeChannelsTask
        :type request: :class:`g42cloudsdkmpc.v1.DeleteMergeChannelsTaskRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.DeleteMergeChannelsTaskResponse`
        """
        return self._delete_merge_channels_task_with_http_info(request)

    def _delete_merge_channels_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
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
            resource_path='/v1/{project_id}/audio/services/merge_channels/task',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteMergeChannelsTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_reset_tracks_task_async(self, request):
        """

        :param request: Request instance for DeleteResetTracksTask
        :type request: :class:`g42cloudsdkmpc.v1.DeleteResetTracksTaskRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.DeleteResetTracksTaskResponse`
        """
        return self._delete_reset_tracks_task_with_http_info(request)

    def _delete_reset_tracks_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
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
            resource_path='/v1/{project_id}/audio/services/reset_tracks/task',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteResetTracksTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_merge_channels_task_async(self, request):
        """

        :param request: Request instance for ListMergeChannelsTask
        :type request: :class:`g42cloudsdkmpc.v1.ListMergeChannelsTaskRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.ListMergeChannelsTaskResponse`
        """
        return self._list_merge_channels_task_with_http_info(request)

    def _list_merge_channels_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
            collection_formats['task_id'] = 'multi'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
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
            resource_path='/v1/{project_id}/audio/services/merge_channels/task',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListMergeChannelsTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_reset_tracks_task_async(self, request):
        """

        :param request: Request instance for ListResetTracksTask
        :type request: :class:`g42cloudsdkmpc.v1.ListResetTracksTaskRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.ListResetTracksTaskResponse`
        """
        return self._list_reset_tracks_task_with_http_info(request)

    def _list_reset_tracks_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
            collection_formats['task_id'] = 'multi'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
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
            resource_path='/v1/{project_id}/audio/services/reset_tracks/task',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListResetTracksTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_media_process_task_async(self, request):
        """

        :param request: Request instance for CreateMediaProcessTask
        :type request: :class:`g42cloudsdkmpc.v1.CreateMediaProcessTaskRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.CreateMediaProcessTaskResponse`
        """
        return self._create_media_process_task_with_http_info(request)

    def _create_media_process_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/enhancements',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateMediaProcessTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_media_process_task_async(self, request):
        """

        :param request: Request instance for DeleteMediaProcessTask
        :type request: :class:`g42cloudsdkmpc.v1.DeleteMediaProcessTaskRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.DeleteMediaProcessTaskResponse`
        """
        return self._delete_media_process_task_with_http_info(request)

    def _delete_media_process_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
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
            resource_path='/v1/{project_id}/enhancements',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteMediaProcessTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_media_process_task_async(self, request):
        """

        :param request: Request instance for ListMediaProcessTask
        :type request: :class:`g42cloudsdkmpc.v1.ListMediaProcessTaskRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.ListMediaProcessTaskResponse`
        """
        return self._list_media_process_task_with_http_info(request)

    def _list_media_process_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
            collection_formats['task_id'] = 'multi'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
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
            resource_path='/v1/{project_id}/enhancements',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListMediaProcessTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_mpe_call_back_async(self, request):
        """

        :param request: Request instance for CreateMpeCallBack
        :type request: :class:`g42cloudsdkmpc.v1.CreateMpeCallBackRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.CreateMpeCallBackResponse`
        """
        return self._create_mpe_call_back_with_http_info(request)

    def _create_mpe_call_back_with_http_info(self, request):
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/mpe/notification',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateMpeCallBackResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_quality_enhance_template_async(self, request):
        """

        :param request: Request instance for CreateQualityEnhanceTemplate
        :type request: :class:`g42cloudsdkmpc.v1.CreateQualityEnhanceTemplateRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.CreateQualityEnhanceTemplateResponse`
        """
        return self._create_quality_enhance_template_with_http_info(request)

    def _create_quality_enhance_template_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/template/qualityenhance',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateQualityEnhanceTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_quality_enhance_template_async(self, request):
        """

        :param request: Request instance for DeleteQualityEnhanceTemplate
        :type request: :class:`g42cloudsdkmpc.v1.DeleteQualityEnhanceTemplateRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.DeleteQualityEnhanceTemplateResponse`
        """
        return self._delete_quality_enhance_template_with_http_info(request)

    def _delete_quality_enhance_template_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'template_id' in local_var_params:
            query_params.append(('template_id', local_var_params['template_id']))

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
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
            resource_path='/v1/{project_id}/template/qualityenhance',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteQualityEnhanceTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_quality_enhance_default_template_async(self, request):
        """

        :param request: Request instance for ListQualityEnhanceDefaultTemplate
        :type request: :class:`g42cloudsdkmpc.v1.ListQualityEnhanceDefaultTemplateRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.ListQualityEnhanceDefaultTemplateResponse`
        """
        return self._list_quality_enhance_default_template_with_http_info(request)

    def _list_quality_enhance_default_template_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
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
            resource_path='/v1/{project_id}/template/qualityenhance/default',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListQualityEnhanceDefaultTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_quality_enhance_template_async(self, request):
        """

        :param request: Request instance for UpdateQualityEnhanceTemplate
        :type request: :class:`g42cloudsdkmpc.v1.UpdateQualityEnhanceTemplateRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.UpdateQualityEnhanceTemplateResponse`
        """
        return self._update_quality_enhance_template_with_http_info(request)

    def _update_quality_enhance_template_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/template/qualityenhance',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateQualityEnhanceTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_transcode_detail_async(self, request):
        """

        :param request: Request instance for ListTranscodeDetail
        :type request: :class:`g42cloudsdkmpc.v1.ListTranscodeDetailRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.ListTranscodeDetailResponse`
        """
        return self._list_transcode_detail_with_http_info(request)

    def _list_transcode_detail_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
            collection_formats['task_id'] = 'multi'

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']
        if 'x_vod_project_id' in local_var_params:
            header_params['x-vod-projectId'] = local_var_params['x_vod_project_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/transcodings/detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListTranscodeDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def cancel_remux_task_async(self, request):
        """

        :param request: Request instance for CancelRemuxTask
        :type request: :class:`g42cloudsdkmpc.v1.CancelRemuxTaskRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.CancelRemuxTaskResponse`
        """
        return self._cancel_remux_task_with_http_info(request)

    def _cancel_remux_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
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
            resource_path='/v1/{project_id}/remux',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CancelRemuxTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_remux_task_async(self, request):
        """

        :param request: Request instance for CreateRemuxTask
        :type request: :class:`g42cloudsdkmpc.v1.CreateRemuxTaskRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.CreateRemuxTaskResponse`
        """
        return self._create_remux_task_with_http_info(request)

    def _create_remux_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/remux',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateRemuxTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_retry_remux_task_async(self, request):
        """

        :param request: Request instance for CreateRetryRemuxTask
        :type request: :class:`g42cloudsdkmpc.v1.CreateRetryRemuxTaskRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.CreateRetryRemuxTaskResponse`
        """
        return self._create_retry_remux_task_with_http_info(request)

    def _create_retry_remux_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/remux',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateRetryRemuxTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_remux_task_async(self, request):
        """

        :param request: Request instance for DeleteRemuxTask
        :type request: :class:`g42cloudsdkmpc.v1.DeleteRemuxTaskRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.DeleteRemuxTaskResponse`
        """
        return self._delete_remux_task_with_http_info(request)

    def _delete_remux_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
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
            resource_path='/v1/{project_id}/remux/task',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteRemuxTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_remux_task_async(self, request):
        """

        :param request: Request instance for ListRemuxTask
        :type request: :class:`g42cloudsdkmpc.v1.ListRemuxTaskRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.ListRemuxTaskResponse`
        """
        return self._list_remux_task_with_http_info(request)

    def _list_remux_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
            collection_formats['task_id'] = 'multi'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'input_bucket' in local_var_params:
            query_params.append(('input_bucket', local_var_params['input_bucket']))
        if 'input_object' in local_var_params:
            query_params.append(('input_object', local_var_params['input_object']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
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
            resource_path='/v1/{project_id}/remux',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRemuxTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_template_group_async(self, request):
        """

        :param request: Request instance for CreateTemplateGroup
        :type request: :class:`g42cloudsdkmpc.v1.CreateTemplateGroupRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.CreateTemplateGroupResponse`
        """
        return self._create_template_group_with_http_info(request)

    def _create_template_group_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/template_group/transcodings',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateTemplateGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_template_group_async(self, request):
        """

        :param request: Request instance for DeleteTemplateGroup
        :type request: :class:`g42cloudsdkmpc.v1.DeleteTemplateGroupRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.DeleteTemplateGroupResponse`
        """
        return self._delete_template_group_with_http_info(request)

    def _delete_template_group_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
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
            resource_path='/v1/{project_id}/template_group/transcodings',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteTemplateGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_template_group_async(self, request):
        """

        :param request: Request instance for ListTemplateGroup
        :type request: :class:`g42cloudsdkmpc.v1.ListTemplateGroupRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.ListTemplateGroupResponse`
        """
        return self._list_template_group_with_http_info(request)

    def _list_template_group_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
            collection_formats['group_id'] = 'multi'
        if 'group_name' in local_var_params:
            query_params.append(('group_name', local_var_params['group_name']))
            collection_formats['group_name'] = 'multi'
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
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
            resource_path='/v1/{project_id}/template_group/transcodings',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListTemplateGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_template_group_async(self, request):
        """

        :param request: Request instance for UpdateTemplateGroup
        :type request: :class:`g42cloudsdkmpc.v1.UpdateTemplateGroupRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.UpdateTemplateGroupResponse`
        """
        return self._update_template_group_with_http_info(request)

    def _update_template_group_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/template_group/transcodings',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateTemplateGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_thumbnails_task_async(self, request):
        """

        :param request: Request instance for CreateThumbnailsTask
        :type request: :class:`g42cloudsdkmpc.v1.CreateThumbnailsTaskRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.CreateThumbnailsTaskResponse`
        """
        return self._create_thumbnails_task_with_http_info(request)

    def _create_thumbnails_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']
        if 'x_vod_project_id' in local_var_params:
            header_params['x-vod-projectId'] = local_var_params['x_vod_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/thumbnails',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateThumbnailsTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_thumbnails_task_async(self, request):
        """

        :param request: Request instance for DeleteThumbnailsTask
        :type request: :class:`g42cloudsdkmpc.v1.DeleteThumbnailsTaskRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.DeleteThumbnailsTaskResponse`
        """
        return self._delete_thumbnails_task_with_http_info(request)

    def _delete_thumbnails_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
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
            resource_path='/v1/{project_id}/thumbnails',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteThumbnailsTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_thumbnails_task_async(self, request):
        """

        :param request: Request instance for ListThumbnailsTask
        :type request: :class:`g42cloudsdkmpc.v1.ListThumbnailsTaskRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.ListThumbnailsTaskResponse`
        """
        return self._list_thumbnails_task_with_http_info(request)

    def _list_thumbnails_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
            collection_formats['task_id'] = 'multi'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']
        if 'x_language' in local_var_params:
            header_params['x-language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/thumbnails',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListThumbnailsTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_transcoding_task_async(self, request):
        """

        :param request: Request instance for CreateTranscodingTask
        :type request: :class:`g42cloudsdkmpc.v1.CreateTranscodingTaskRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.CreateTranscodingTaskResponse`
        """
        return self._create_transcoding_task_with_http_info(request)

    def _create_transcoding_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']
        if 'x_vod_project_id' in local_var_params:
            header_params['x-vod-projectId'] = local_var_params['x_vod_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/transcodings',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateTranscodingTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_transcoding_task_async(self, request):
        """

        :param request: Request instance for DeleteTranscodingTask
        :type request: :class:`g42cloudsdkmpc.v1.DeleteTranscodingTaskRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.DeleteTranscodingTaskResponse`
        """
        return self._delete_transcoding_task_with_http_info(request)

    def _delete_transcoding_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
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
            resource_path='/v1/{project_id}/transcodings',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteTranscodingTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_transcoding_task_by_console_async(self, request):
        """

        :param request: Request instance for DeleteTranscodingTaskByConsole
        :type request: :class:`g42cloudsdkmpc.v1.DeleteTranscodingTaskByConsoleRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.DeleteTranscodingTaskByConsoleResponse`
        """
        return self._delete_transcoding_task_by_console_with_http_info(request)

    def _delete_transcoding_task_by_console_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
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
            resource_path='/v1/{project_id}/transcodings/task',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteTranscodingTaskByConsoleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_stat_summary_async(self, request):
        """

        :param request: Request instance for ListStatSummary
        :type request: :class:`g42cloudsdkmpc.v1.ListStatSummaryRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.ListStatSummaryResponse`
        """
        return self._list_stat_summary_with_http_info(request)

    def _list_stat_summary_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'stat_type' in local_var_params:
            query_params.append(('stat_type', local_var_params['stat_type']))

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
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
            resource_path='/v1/{project_id}/transcodings/summaries',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListStatSummaryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_transcoding_task_async(self, request):
        """

        :param request: Request instance for ListTranscodingTask
        :type request: :class:`g42cloudsdkmpc.v1.ListTranscodingTaskRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.ListTranscodingTaskResponse`
        """
        return self._list_transcoding_task_with_http_info(request)

    def _list_transcoding_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
            collection_formats['task_id'] = 'multi'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['x-language'] = local_var_params['x_language']
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
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
            resource_path='/v1/{project_id}/transcodings',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListTranscodingTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_trans_template_async(self, request):
        """

        :param request: Request instance for CreateTransTemplate
        :type request: :class:`g42cloudsdkmpc.v1.CreateTransTemplateRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.CreateTransTemplateResponse`
        """
        return self._create_trans_template_with_http_info(request)

    def _create_trans_template_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']
        if 'x_vod_project_id' in local_var_params:
            header_params['x-vod-projectId'] = local_var_params['x_vod_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/template/transcodings',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateTransTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_template_async(self, request):
        """

        :param request: Request instance for DeleteTemplate
        :type request: :class:`g42cloudsdkmpc.v1.DeleteTemplateRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.DeleteTemplateResponse`
        """
        return self._delete_template_with_http_info(request)

    def _delete_template_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'template_id' in local_var_params:
            query_params.append(('template_id', local_var_params['template_id']))

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']
        if 'x_vod_project_id' in local_var_params:
            header_params['x-vod-projectId'] = local_var_params['x_vod_project_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/template/transcodings',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_template_async(self, request):
        """

        :param request: Request instance for ListTemplate
        :type request: :class:`g42cloudsdkmpc.v1.ListTemplateRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.ListTemplateResponse`
        """
        return self._list_template_with_http_info(request)

    def _list_template_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'template_id' in local_var_params:
            query_params.append(('template_id', local_var_params['template_id']))
            collection_formats['template_id'] = 'multi'
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']
        if 'x_vod_project_id' in local_var_params:
            header_params['x-vod-projectId'] = local_var_params['x_vod_project_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/template/transcodings',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_trans_template_async(self, request):
        """

        :param request: Request instance for UpdateTransTemplate
        :type request: :class:`g42cloudsdkmpc.v1.UpdateTransTemplateRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.UpdateTransTemplateResponse`
        """
        return self._update_trans_template_with_http_info(request)

    def _update_trans_template_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/template/transcodings',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateTransTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_watermark_template_async(self, request):
        """

        :param request: Request instance for CreateWatermarkTemplate
        :type request: :class:`g42cloudsdkmpc.v1.CreateWatermarkTemplateRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.CreateWatermarkTemplateResponse`
        """
        return self._create_watermark_template_with_http_info(request)

    def _create_watermark_template_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']
        if 'x_vod_project_id' in local_var_params:
            header_params['x-vod-projectId'] = local_var_params['x_vod_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/template/watermark',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateWatermarkTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_watermark_template_async(self, request):
        """

        :param request: Request instance for DeleteWatermarkTemplate
        :type request: :class:`g42cloudsdkmpc.v1.DeleteWatermarkTemplateRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.DeleteWatermarkTemplateResponse`
        """
        return self._delete_watermark_template_with_http_info(request)

    def _delete_watermark_template_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'template_id' in local_var_params:
            query_params.append(('template_id', local_var_params['template_id']))

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']
        if 'x_vod_project_id' in local_var_params:
            header_params['x-vod-projectId'] = local_var_params['x_vod_project_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/template/watermark',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteWatermarkTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_watermark_template_async(self, request):
        """

        :param request: Request instance for ListWatermarkTemplate
        :type request: :class:`g42cloudsdkmpc.v1.ListWatermarkTemplateRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.ListWatermarkTemplateResponse`
        """
        return self._list_watermark_template_with_http_info(request)

    def _list_watermark_template_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'template_id' in local_var_params:
            query_params.append(('template_id', local_var_params['template_id']))
            collection_formats['template_id'] = 'multi'
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
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
            resource_path='/v1/{project_id}/template/watermark',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListWatermarkTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_watermark_template_async(self, request):
        """

        :param request: Request instance for UpdateWatermarkTemplate
        :type request: :class:`g42cloudsdkmpc.v1.UpdateWatermarkTemplateRequest`
        :rtype: :class:`g42cloudsdkmpc.v1.UpdateWatermarkTemplateResponse`
        """
        return self._update_watermark_template_with_http_info(request)

    def _update_watermark_template_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']
        if 'x_project_id' in local_var_params:
            header_params['X-Project_Id'] = local_var_params['x_project_id']
        if 'x_sdk_date' in local_var_params:
            header_params['X-Sdk-Date'] = local_var_params['x_sdk_date']
        if 'x_vod_project_id' in local_var_params:
            header_params['x-vod-projectId'] = local_var_params['x_vod_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/template/watermark',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateWatermarkTemplateResponse',
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
