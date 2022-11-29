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


class CesClient(Client):
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
        super(CesClient, self).__init__()
        self.model_package = importlib.import_module("g42cloudsdkces.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "CesClient":
            raise TypeError("client type error, support client type is CesClient")

        return ClientBuilder(clazz)

    def batch_list_metric_data(self, request):
        """
        :param request: Request instance for BatchListMetricData
        :type request: :class:`g42cloudsdkces.v1.BatchListMetricDataRequest`
        :rtype: :class:`g42cloudsdkces.v1.BatchListMetricDataResponse`
        """
        return self.batch_list_metric_data_with_http_info(request)

    def batch_list_metric_data_with_http_info(self, request):
        all_params = ['batch_list_metric_data_request_body']
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/V1.0/{project_id}/batch-query-metric-data',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchListMetricDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_alarm(self, request):
        """
        :param request: Request instance for CreateAlarm
        :type request: :class:`g42cloudsdkces.v1.CreateAlarmRequest`
        :rtype: :class:`g42cloudsdkces.v1.CreateAlarmResponse`
        """
        return self.create_alarm_with_http_info(request)

    def create_alarm_with_http_info(self, request):
        all_params = ['create_alarm_request_body']
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/V1.0/{project_id}/alarms',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateAlarmResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_alarm_template(self, request):
        """
        :param request: Request instance for CreateAlarmTemplate
        :type request: :class:`g42cloudsdkces.v1.CreateAlarmTemplateRequest`
        :rtype: :class:`g42cloudsdkces.v1.CreateAlarmTemplateResponse`
        """
        return self.create_alarm_template_with_http_info(request)

    def create_alarm_template_with_http_info(self, request):
        all_params = ['create_alarm_template_request_body']
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/V1.0/{project_id}/alarm-template',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateAlarmTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_events(self, request):
        """
        :param request: Request instance for CreateEvents
        :type request: :class:`g42cloudsdkces.v1.CreateEventsRequest`
        :rtype: :class:`g42cloudsdkces.v1.CreateEventsResponse`
        """
        return self.create_events_with_http_info(request)

    def create_events_with_http_info(self, request):
        all_params = ['event_items']
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/V1.0/{project_id}/events',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateEventsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_metric_data(self, request):
        """
        :param request: Request instance for CreateMetricData
        :type request: :class:`g42cloudsdkces.v1.CreateMetricDataRequest`
        :rtype: :class:`g42cloudsdkces.v1.CreateMetricDataResponse`
        """
        return self.create_metric_data_with_http_info(request)

    def create_metric_data_with_http_info(self, request):
        all_params = ['metric_data_item']
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/V1.0/{project_id}/metric-data',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateMetricDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_resource_group(self, request):
        """
        :param request: Request instance for CreateResourceGroup
        :type request: :class:`g42cloudsdkces.v1.CreateResourceGroupRequest`
        :rtype: :class:`g42cloudsdkces.v1.CreateResourceGroupResponse`
        """
        return self.create_resource_group_with_http_info(request)

    def create_resource_group_with_http_info(self, request):
        all_params = ['create_resource_group_request_body']
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/V1.0/{project_id}/resource-groups',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateResourceGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_alarm(self, request):
        """
        :param request: Request instance for DeleteAlarm
        :type request: :class:`g42cloudsdkces.v1.DeleteAlarmRequest`
        :rtype: :class:`g42cloudsdkces.v1.DeleteAlarmResponse`
        """
        return self.delete_alarm_with_http_info(request)

    def delete_alarm_with_http_info(self, request):
        all_params = ['alarm_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'alarm_id' in local_var_params:
            path_params['alarm_id'] = local_var_params['alarm_id']

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
            resource_path='/V1.0/{project_id}/alarms/{alarm_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteAlarmResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_alarm_template(self, request):
        """
        :param request: Request instance for DeleteAlarmTemplate
        :type request: :class:`g42cloudsdkces.v1.DeleteAlarmTemplateRequest`
        :rtype: :class:`g42cloudsdkces.v1.DeleteAlarmTemplateResponse`
        """
        return self.delete_alarm_template_with_http_info(request)

    def delete_alarm_template_with_http_info(self, request):
        all_params = ['template_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

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
            resource_path='/V1.0/{project_id}/alarm-template/{template_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteAlarmTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_resource_group(self, request):
        """
        :param request: Request instance for DeleteResourceGroup
        :type request: :class:`g42cloudsdkces.v1.DeleteResourceGroupRequest`
        :rtype: :class:`g42cloudsdkces.v1.DeleteResourceGroupResponse`
        """
        return self.delete_resource_group_with_http_info(request)

    def delete_resource_group_with_http_info(self, request):
        all_params = ['group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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
            resource_path='/V1.0/{project_id}/resource-groups/{group_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteResourceGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_alarm_histories(self, request):
        """
        :param request: Request instance for ListAlarmHistories
        :type request: :class:`g42cloudsdkces.v1.ListAlarmHistoriesRequest`
        :rtype: :class:`g42cloudsdkces.v1.ListAlarmHistoriesResponse`
        """
        return self.list_alarm_histories_with_http_info(request)

    def list_alarm_histories_with_http_info(self, request):
        all_params = ['group_id', 'alarm_id', 'alarm_name', 'alarm_status', 'alarm_level', 'namespace', '_from', 'to', 'start', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'alarm_id' in local_var_params:
            query_params.append(('alarm_id', local_var_params['alarm_id']))
        if 'alarm_name' in local_var_params:
            query_params.append(('alarm_name', local_var_params['alarm_name']))
        if 'alarm_status' in local_var_params:
            query_params.append(('alarm_status', local_var_params['alarm_status']))
        if 'alarm_level' in local_var_params:
            query_params.append(('alarm_level', local_var_params['alarm_level']))
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))
        if '_from' in local_var_params:
            query_params.append(('from', local_var_params['_from']))
        if 'to' in local_var_params:
            query_params.append(('to', local_var_params['to']))
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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
            resource_path='/V1.0/{project_id}/alarm-histories',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAlarmHistoriesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_alarm_templates(self, request):
        """
        :param request: Request instance for ListAlarmTemplates
        :type request: :class:`g42cloudsdkces.v1.ListAlarmTemplatesRequest`
        :rtype: :class:`g42cloudsdkces.v1.ListAlarmTemplatesResponse`
        """
        return self.list_alarm_templates_with_http_info(request)

    def list_alarm_templates_with_http_info(self, request):
        all_params = ['alarm_template_id', 'namespace', 'dname', 'start', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'alarm_template_id' in local_var_params:
            query_params.append(('alarmTemplateId', local_var_params['alarm_template_id']))
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))
        if 'dname' in local_var_params:
            query_params.append(('dname', local_var_params['dname']))
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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
            resource_path='/V1.0/{project_id}/alarm-template',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAlarmTemplatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_alarms(self, request):
        """
        :param request: Request instance for ListAlarms
        :type request: :class:`g42cloudsdkces.v1.ListAlarmsRequest`
        :rtype: :class:`g42cloudsdkces.v1.ListAlarmsResponse`
        """
        return self.list_alarms_with_http_info(request)

    def list_alarms_with_http_info(self, request):
        all_params = ['limit', 'order', 'start']
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
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))

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
            resource_path='/V1.0/{project_id}/alarms',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAlarmsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_event_detail(self, request):
        """
        :param request: Request instance for ListEventDetail
        :type request: :class:`g42cloudsdkces.v1.ListEventDetailRequest`
        :rtype: :class:`g42cloudsdkces.v1.ListEventDetailResponse`
        """
        return self.list_event_detail_with_http_info(request)

    def list_event_detail_with_http_info(self, request):
        all_params = ['event_name', 'event_type', 'event_source', 'event_level', 'event_user', 'event_state', '_from', 'to', 'start', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'event_name' in local_var_params:
            path_params['event_name'] = local_var_params['event_name']

        query_params = []
        if 'event_type' in local_var_params:
            query_params.append(('event_type', local_var_params['event_type']))
        if 'event_source' in local_var_params:
            query_params.append(('event_source', local_var_params['event_source']))
        if 'event_level' in local_var_params:
            query_params.append(('event_level', local_var_params['event_level']))
        if 'event_user' in local_var_params:
            query_params.append(('event_user', local_var_params['event_user']))
        if 'event_state' in local_var_params:
            query_params.append(('event_state', local_var_params['event_state']))
        if '_from' in local_var_params:
            query_params.append(('from', local_var_params['_from']))
        if 'to' in local_var_params:
            query_params.append(('to', local_var_params['to']))
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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
            resource_path='/V1.0/{project_id}/event/{event_name}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEventDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_events(self, request):
        """
        :param request: Request instance for ListEvents
        :type request: :class:`g42cloudsdkces.v1.ListEventsRequest`
        :rtype: :class:`g42cloudsdkces.v1.ListEventsResponse`
        """
        return self.list_events_with_http_info(request)

    def list_events_with_http_info(self, request):
        all_params = ['event_type', 'event_name', '_from', 'to', 'start', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'event_type' in local_var_params:
            query_params.append(('event_type', local_var_params['event_type']))
        if 'event_name' in local_var_params:
            query_params.append(('event_name', local_var_params['event_name']))
        if '_from' in local_var_params:
            query_params.append(('from', local_var_params['_from']))
        if 'to' in local_var_params:
            query_params.append(('to', local_var_params['to']))
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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
            resource_path='/V1.0/{project_id}/events',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEventsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_metrics(self, request):
        """
        :param request: Request instance for ListMetrics
        :type request: :class:`g42cloudsdkces.v1.ListMetricsRequest`
        :rtype: :class:`g42cloudsdkces.v1.ListMetricsResponse`
        """
        return self.list_metrics_with_http_info(request)

    def list_metrics_with_http_info(self, request):
        all_params = ['dim_0', 'dim_1', 'dim_2', 'limit', 'metric_name', 'namespace', 'order', 'start']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'dim_0' in local_var_params:
            query_params.append(('dim.0', local_var_params['dim_0']))
        if 'dim_1' in local_var_params:
            query_params.append(('dim.1', local_var_params['dim_1']))
        if 'dim_2' in local_var_params:
            query_params.append(('dim.2', local_var_params['dim_2']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'metric_name' in local_var_params:
            query_params.append(('metric_name', local_var_params['metric_name']))
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))

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
            resource_path='/V1.0/{project_id}/metrics',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListMetricsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_resource_group(self, request):
        """
        :param request: Request instance for ListResourceGroup
        :type request: :class:`g42cloudsdkces.v1.ListResourceGroupRequest`
        :rtype: :class:`g42cloudsdkces.v1.ListResourceGroupResponse`
        """
        return self.list_resource_group_with_http_info(request)

    def list_resource_group_with_http_info(self, request):
        all_params = ['group_name', 'group_id', 'status', 'start', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'group_name' in local_var_params:
            query_params.append(('group_name', local_var_params['group_name']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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
            resource_path='/V1.0/{project_id}/resource-groups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListResourceGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_alarm(self, request):
        """
        :param request: Request instance for ShowAlarm
        :type request: :class:`g42cloudsdkces.v1.ShowAlarmRequest`
        :rtype: :class:`g42cloudsdkces.v1.ShowAlarmResponse`
        """
        return self.show_alarm_with_http_info(request)

    def show_alarm_with_http_info(self, request):
        all_params = ['alarm_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'alarm_id' in local_var_params:
            path_params['alarm_id'] = local_var_params['alarm_id']

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
            resource_path='/V1.0/{project_id}/alarms/{alarm_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAlarmResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_event_data(self, request):
        """
        :param request: Request instance for ShowEventData
        :type request: :class:`g42cloudsdkces.v1.ShowEventDataRequest`
        :rtype: :class:`g42cloudsdkces.v1.ShowEventDataResponse`
        """
        return self.show_event_data_with_http_info(request)

    def show_event_data_with_http_info(self, request):
        all_params = ['namespace', 'dim_0', 'type', '_from', 'to', 'dim_1', 'dim_2', 'dim_3']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))
        if 'dim_0' in local_var_params:
            query_params.append(('dim.0', local_var_params['dim_0']))
        if 'dim_1' in local_var_params:
            query_params.append(('dim.1', local_var_params['dim_1']))
        if 'dim_2' in local_var_params:
            query_params.append(('dim.2', local_var_params['dim_2']))
        if 'dim_3' in local_var_params:
            query_params.append(('dim.3', local_var_params['dim_3']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if '_from' in local_var_params:
            query_params.append(('from', local_var_params['_from']))
        if 'to' in local_var_params:
            query_params.append(('to', local_var_params['to']))

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
            resource_path='/V1.0/{project_id}/event-data',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowEventDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_metric_data(self, request):
        """
        :param request: Request instance for ShowMetricData
        :type request: :class:`g42cloudsdkces.v1.ShowMetricDataRequest`
        :rtype: :class:`g42cloudsdkces.v1.ShowMetricDataResponse`
        """
        return self.show_metric_data_with_http_info(request)

    def show_metric_data_with_http_info(self, request):
        all_params = ['namespace', 'metric_name', 'dim_0', 'filter', 'period', '_from', 'to', 'dim_1', 'dim_2', 'dim_3']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))
        if 'metric_name' in local_var_params:
            query_params.append(('metric_name', local_var_params['metric_name']))
        if 'dim_0' in local_var_params:
            query_params.append(('dim.0', local_var_params['dim_0']))
        if 'dim_1' in local_var_params:
            query_params.append(('dim.1', local_var_params['dim_1']))
        if 'dim_2' in local_var_params:
            query_params.append(('dim.2', local_var_params['dim_2']))
        if 'dim_3' in local_var_params:
            query_params.append(('dim.3', local_var_params['dim_3']))
        if 'filter' in local_var_params:
            query_params.append(('filter', local_var_params['filter']))
        if 'period' in local_var_params:
            query_params.append(('period', local_var_params['period']))
        if '_from' in local_var_params:
            query_params.append(('from', local_var_params['_from']))
        if 'to' in local_var_params:
            query_params.append(('to', local_var_params['to']))

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
            resource_path='/V1.0/{project_id}/metric-data',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowMetricDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_quotas(self, request):
        """
        :param request: Request instance for ShowQuotas
        :type request: :class:`g42cloudsdkces.v1.ShowQuotasRequest`
        :rtype: :class:`g42cloudsdkces.v1.ShowQuotasResponse`
        """
        return self.show_quotas_with_http_info(request)

    def show_quotas_with_http_info(self, request):
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
            resource_path='/V1.0/{project_id}/quotas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowQuotasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_resource_group(self, request):
        """
        :param request: Request instance for ShowResourceGroup
        :type request: :class:`g42cloudsdkces.v1.ShowResourceGroupRequest`
        :rtype: :class:`g42cloudsdkces.v1.ShowResourceGroupResponse`
        """
        return self.show_resource_group_with_http_info(request)

    def show_resource_group_with_http_info(self, request):
        all_params = ['group_id', 'status', 'namespace', 'dname', 'start', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))
        if 'dname' in local_var_params:
            query_params.append(('dname', local_var_params['dname']))
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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
            resource_path='/V1.0/{project_id}/resource-groups/{group_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowResourceGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_alarm(self, request):
        """
        :param request: Request instance for UpdateAlarm
        :type request: :class:`g42cloudsdkces.v1.UpdateAlarmRequest`
        :rtype: :class:`g42cloudsdkces.v1.UpdateAlarmResponse`
        """
        return self.update_alarm_with_http_info(request)

    def update_alarm_with_http_info(self, request):
        all_params = ['alarm_id', 'update_alarm_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'alarm_id' in local_var_params:
            path_params['alarm_id'] = local_var_params['alarm_id']

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
            resource_path='/V1.0/{project_id}/alarms/{alarm_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateAlarmResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_alarm_action(self, request):
        """
        :param request: Request instance for UpdateAlarmAction
        :type request: :class:`g42cloudsdkces.v1.UpdateAlarmActionRequest`
        :rtype: :class:`g42cloudsdkces.v1.UpdateAlarmActionResponse`
        """
        return self.update_alarm_action_with_http_info(request)

    def update_alarm_action_with_http_info(self, request):
        all_params = ['alarm_id', 'modify_alarm_action_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'alarm_id' in local_var_params:
            path_params['alarm_id'] = local_var_params['alarm_id']

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
            resource_path='/V1.0/{project_id}/alarms/{alarm_id}/action',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateAlarmActionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_alarm_template(self, request):
        """
        :param request: Request instance for UpdateAlarmTemplate
        :type request: :class:`g42cloudsdkces.v1.UpdateAlarmTemplateRequest`
        :rtype: :class:`g42cloudsdkces.v1.UpdateAlarmTemplateResponse`
        """
        return self.update_alarm_template_with_http_info(request)

    def update_alarm_template_with_http_info(self, request):
        all_params = ['template_id', 'update_alarm_template_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

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
            resource_path='/V1.0/{project_id}/alarm-template/{template_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateAlarmTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_resource_group(self, request):
        """
        :param request: Request instance for UpdateResourceGroup
        :type request: :class:`g42cloudsdkces.v1.UpdateResourceGroupRequest`
        :rtype: :class:`g42cloudsdkces.v1.UpdateResourceGroupResponse`
        """
        return self.update_resource_group_with_http_info(request)

    def update_resource_group_with_http_info(self, request):
        all_params = ['group_id', 'update_resource_group_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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
            resource_path='/V1.0/{project_id}/resource-groups/{group_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateResourceGroupResponse',
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
