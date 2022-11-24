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


class CceClient(Client):
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
        super(CceClient, self).__init__()
        self.model_package = importlib.import_module("g42cloudsdkcce.v3.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "CceClient":
            raise TypeError("client type error, support client type is CceClient")

        return ClientBuilder(clazz)

    def awake_cluster(self, request):
        """
        :param request: Request instance for AwakeCluster
        :type request: :class:`g42cloudsdkcce.v3.AwakeClusterRequest`
        :rtype: :class:`g42cloudsdkcce.v3.AwakeClusterResponse`
        """
        return self.awake_cluster_with_http_info(request)

    def awake_cluster_with_http_info(self, request):
        all_params = ['cluster_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/api/v3/projects/{project_id}/clusters/{cluster_id}/operation/awake',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AwakeClusterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_addon_instance(self, request):
        """
        :param request: Request instance for CreateAddonInstance
        :type request: :class:`g42cloudsdkcce.v3.CreateAddonInstanceRequest`
        :rtype: :class:`g42cloudsdkcce.v3.CreateAddonInstanceResponse`
        """
        return self.create_addon_instance_with_http_info(request)

    def create_addon_instance_with_http_info(self, request):
        all_params = ['create_addon_instance_request_body']
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
            resource_path='/api/v3/addons',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateAddonInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_cloud_persistent_volume_claims(self, request):
        """
        :param request: Request instance for CreateCloudPersistentVolumeClaims
        :type request: :class:`g42cloudsdkcce.v3.CreateCloudPersistentVolumeClaimsRequest`
        :rtype: :class:`g42cloudsdkcce.v3.CreateCloudPersistentVolumeClaimsResponse`
        """
        return self.create_cloud_persistent_volume_claims_with_http_info(request)

    def create_cloud_persistent_volume_claims_with_http_info(self, request):
        all_params = ['namespace', 'create_cloud_persistent_volume_claims_request_body', 'x_cluster_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']

        query_params = []

        header_params = {}
        if 'x_cluster_id' in local_var_params:
            header_params['X-Cluster-ID'] = local_var_params['x_cluster_id']

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
            resource_path='/api/v1/namespaces/{namespace}/cloudpersistentvolumeclaims',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateCloudPersistentVolumeClaimsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_cluster(self, request):
        """
        :param request: Request instance for CreateCluster
        :type request: :class:`g42cloudsdkcce.v3.CreateClusterRequest`
        :rtype: :class:`g42cloudsdkcce.v3.CreateClusterResponse`
        """
        return self.create_cluster_with_http_info(request)

    def create_cluster_with_http_info(self, request):
        all_params = ['create_cluster_request_body']
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
            resource_path='/api/v3/projects/{project_id}/clusters',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateClusterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_kubernetes_cluster_cert(self, request):
        """
        :param request: Request instance for CreateKubernetesClusterCert
        :type request: :class:`g42cloudsdkcce.v3.CreateKubernetesClusterCertRequest`
        :rtype: :class:`g42cloudsdkcce.v3.CreateKubernetesClusterCertResponse`
        """
        return self.create_kubernetes_cluster_cert_with_http_info(request)

    def create_kubernetes_cluster_cert_with_http_info(self, request):
        all_params = ['cluster_id', 'create_kubernetes_cluster_cert_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["Port-ID", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/api/v3/projects/{project_id}/clusters/{cluster_id}/clustercert',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateKubernetesClusterCertResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_node(self, request):
        """
        :param request: Request instance for CreateNode
        :type request: :class:`g42cloudsdkcce.v3.CreateNodeRequest`
        :rtype: :class:`g42cloudsdkcce.v3.CreateNodeResponse`
        """
        return self.create_node_with_http_info(request)

    def create_node_with_http_info(self, request):
        all_params = ['cluster_id', 'create_node_request_body', 'nodepool_scale_up']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []
        if 'nodepool_scale_up' in local_var_params:
            query_params.append(('nodepoolScaleUp', local_var_params['nodepool_scale_up']))

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
            resource_path='/api/v3/projects/{project_id}/clusters/{cluster_id}/nodes',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateNodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_node_pool(self, request):
        """
        :param request: Request instance for CreateNodePool
        :type request: :class:`g42cloudsdkcce.v3.CreateNodePoolRequest`
        :rtype: :class:`g42cloudsdkcce.v3.CreateNodePoolResponse`
        """
        return self.create_node_pool_with_http_info(request)

    def create_node_pool_with_http_info(self, request):
        all_params = ['cluster_id', 'create_node_pool_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/api/v3/projects/{project_id}/clusters/{cluster_id}/nodepools',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateNodePoolResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_addon_instance(self, request):
        """
        :param request: Request instance for DeleteAddonInstance
        :type request: :class:`g42cloudsdkcce.v3.DeleteAddonInstanceRequest`
        :rtype: :class:`g42cloudsdkcce.v3.DeleteAddonInstanceResponse`
        """
        return self.delete_addon_instance_with_http_info(request)

    def delete_addon_instance_with_http_info(self, request):
        all_params = ['id', 'cluster_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []
        if 'cluster_id' in local_var_params:
            query_params.append(('cluster_id', local_var_params['cluster_id']))

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
            resource_path='/api/v3/addons/{id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteAddonInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_cloud_persistent_volume_claims(self, request):
        """
        :param request: Request instance for DeleteCloudPersistentVolumeClaims
        :type request: :class:`g42cloudsdkcce.v3.DeleteCloudPersistentVolumeClaimsRequest`
        :rtype: :class:`g42cloudsdkcce.v3.DeleteCloudPersistentVolumeClaimsResponse`
        """
        return self.delete_cloud_persistent_volume_claims_with_http_info(request)

    def delete_cloud_persistent_volume_claims_with_http_info(self, request):
        all_params = ['name', 'namespace', 'delete_volume', 'storage_type', 'x_cluster_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']

        query_params = []
        if 'delete_volume' in local_var_params:
            query_params.append(('deleteVolume', local_var_params['delete_volume']))
        if 'storage_type' in local_var_params:
            query_params.append(('storageType', local_var_params['storage_type']))

        header_params = {}
        if 'x_cluster_id' in local_var_params:
            header_params['X-Cluster-ID'] = local_var_params['x_cluster_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/api/v1/namespaces/{namespace}/cloudpersistentvolumeclaims/{name}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteCloudPersistentVolumeClaimsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_cluster(self, request):
        """
        :param request: Request instance for DeleteCluster
        :type request: :class:`g42cloudsdkcce.v3.DeleteClusterRequest`
        :rtype: :class:`g42cloudsdkcce.v3.DeleteClusterResponse`
        """
        return self.delete_cluster_with_http_info(request)

    def delete_cluster_with_http_info(self, request):
        all_params = ['cluster_id', 'delete_efs', 'delete_eni', 'delete_evs', 'delete_net', 'delete_obs', 'delete_sfs', 'tobedeleted']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []
        if 'delete_efs' in local_var_params:
            query_params.append(('delete_efs', local_var_params['delete_efs']))
        if 'delete_eni' in local_var_params:
            query_params.append(('delete_eni', local_var_params['delete_eni']))
        if 'delete_evs' in local_var_params:
            query_params.append(('delete_evs', local_var_params['delete_evs']))
        if 'delete_net' in local_var_params:
            query_params.append(('delete_net', local_var_params['delete_net']))
        if 'delete_obs' in local_var_params:
            query_params.append(('delete_obs', local_var_params['delete_obs']))
        if 'delete_sfs' in local_var_params:
            query_params.append(('delete_sfs', local_var_params['delete_sfs']))
        if 'tobedeleted' in local_var_params:
            query_params.append(('tobedeleted', local_var_params['tobedeleted']))

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
            resource_path='/api/v3/projects/{project_id}/clusters/{cluster_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteClusterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_node(self, request):
        """
        :param request: Request instance for DeleteNode
        :type request: :class:`g42cloudsdkcce.v3.DeleteNodeRequest`
        :rtype: :class:`g42cloudsdkcce.v3.DeleteNodeResponse`
        """
        return self.delete_node_with_http_info(request)

    def delete_node_with_http_info(self, request):
        all_params = ['cluster_id', 'node_id', 'nodepool_scale_down']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'node_id' in local_var_params:
            path_params['node_id'] = local_var_params['node_id']

        query_params = []
        if 'nodepool_scale_down' in local_var_params:
            query_params.append(('nodepoolScaleDown', local_var_params['nodepool_scale_down']))

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
            resource_path='/api/v3/projects/{project_id}/clusters/{cluster_id}/nodes/{node_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteNodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_node_pool(self, request):
        """
        :param request: Request instance for DeleteNodePool
        :type request: :class:`g42cloudsdkcce.v3.DeleteNodePoolRequest`
        :rtype: :class:`g42cloudsdkcce.v3.DeleteNodePoolResponse`
        """
        return self.delete_node_pool_with_http_info(request)

    def delete_node_pool_with_http_info(self, request):
        all_params = ['cluster_id', 'nodepool_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'nodepool_id' in local_var_params:
            path_params['nodepool_id'] = local_var_params['nodepool_id']

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
            resource_path='/api/v3/projects/{project_id}/clusters/{cluster_id}/nodepools/{nodepool_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteNodePoolResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def hibernate_cluster(self, request):
        """
        :param request: Request instance for HibernateCluster
        :type request: :class:`g42cloudsdkcce.v3.HibernateClusterRequest`
        :rtype: :class:`g42cloudsdkcce.v3.HibernateClusterResponse`
        """
        return self.hibernate_cluster_with_http_info(request)

    def hibernate_cluster_with_http_info(self, request):
        all_params = ['cluster_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/api/v3/projects/{project_id}/clusters/{cluster_id}/operation/hibernate',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='HibernateClusterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_addon_instances(self, request):
        """
        :param request: Request instance for ListAddonInstances
        :type request: :class:`g42cloudsdkcce.v3.ListAddonInstancesRequest`
        :rtype: :class:`g42cloudsdkcce.v3.ListAddonInstancesResponse`
        """
        return self.list_addon_instances_with_http_info(request)

    def list_addon_instances_with_http_info(self, request):
        all_params = ['cluster_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cluster_id' in local_var_params:
            query_params.append(('cluster_id', local_var_params['cluster_id']))

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
            resource_path='/api/v3/addons',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAddonInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_addon_templates(self, request):
        """
        :param request: Request instance for ListAddonTemplates
        :type request: :class:`g42cloudsdkcce.v3.ListAddonTemplatesRequest`
        :rtype: :class:`g42cloudsdkcce.v3.ListAddonTemplatesResponse`
        """
        return self.list_addon_templates_with_http_info(request)

    def list_addon_templates_with_http_info(self, request):
        all_params = ['addon_template_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'addon_template_name' in local_var_params:
            query_params.append(('addon_template_name', local_var_params['addon_template_name']))

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
            resource_path='/api/v3/addontemplates',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAddonTemplatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_clusters(self, request):
        """
        :param request: Request instance for ListClusters
        :type request: :class:`g42cloudsdkcce.v3.ListClustersRequest`
        :rtype: :class:`g42cloudsdkcce.v3.ListClustersResponse`
        """
        return self.list_clusters_with_http_info(request)

    def list_clusters_with_http_info(self, request):
        all_params = ['detail', 'status', 'type', 'version']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'detail' in local_var_params:
            query_params.append(('detail', local_var_params['detail']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'version' in local_var_params:
            query_params.append(('version', local_var_params['version']))

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
            resource_path='/api/v3/projects/{project_id}/clusters',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListClustersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_node_pools(self, request):
        """
        :param request: Request instance for ListNodePools
        :type request: :class:`g42cloudsdkcce.v3.ListNodePoolsRequest`
        :rtype: :class:`g42cloudsdkcce.v3.ListNodePoolsResponse`
        """
        return self.list_node_pools_with_http_info(request)

    def list_node_pools_with_http_info(self, request):
        all_params = ['cluster_id', 'show_default_node_pool']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []
        if 'show_default_node_pool' in local_var_params:
            query_params.append(('showDefaultNodePool', local_var_params['show_default_node_pool']))

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
            resource_path='/api/v3/projects/{project_id}/clusters/{cluster_id}/nodepools',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListNodePoolsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_nodes(self, request):
        """
        :param request: Request instance for ListNodes
        :type request: :class:`g42cloudsdkcce.v3.ListNodesRequest`
        :rtype: :class:`g42cloudsdkcce.v3.ListNodesResponse`
        """
        return self.list_nodes_with_http_info(request)

    def list_nodes_with_http_info(self, request):
        all_params = ['cluster_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/api/v3/projects/{project_id}/clusters/{cluster_id}/nodes',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListNodesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def migrate_node(self, request):
        """
        :param request: Request instance for MigrateNode
        :type request: :class:`g42cloudsdkcce.v3.MigrateNodeRequest`
        :rtype: :class:`g42cloudsdkcce.v3.MigrateNodeResponse`
        """
        return self.migrate_node_with_http_info(request)

    def migrate_node_with_http_info(self, request):
        all_params = ['cluster_id', 'target_cluster_id', 'migrate_nodes_task']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'target_cluster_id' in local_var_params:
            path_params['target_cluster_id'] = local_var_params['target_cluster_id']

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
            resource_path='/api/v3/projects/{project_id}/clusters/{cluster_id}/nodes/operation/migrateto/{target_cluster_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='MigrateNodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def remove_node(self, request):
        """
        :param request: Request instance for RemoveNode
        :type request: :class:`g42cloudsdkcce.v3.RemoveNodeRequest`
        :rtype: :class:`g42cloudsdkcce.v3.RemoveNodeResponse`
        """
        return self.remove_node_with_http_info(request)

    def remove_node_with_http_info(self, request):
        all_params = ['cluster_id', 'remove_nodes_task']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/api/v3/projects/{project_id}/clusters/{cluster_id}/nodes/operation/remove',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RemoveNodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_addon_instance(self, request):
        """
        :param request: Request instance for ShowAddonInstance
        :type request: :class:`g42cloudsdkcce.v3.ShowAddonInstanceRequest`
        :rtype: :class:`g42cloudsdkcce.v3.ShowAddonInstanceResponse`
        """
        return self.show_addon_instance_with_http_info(request)

    def show_addon_instance_with_http_info(self, request):
        all_params = ['id', 'cluster_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []
        if 'cluster_id' in local_var_params:
            query_params.append(('cluster_id', local_var_params['cluster_id']))

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
            resource_path='/api/v3/addons/{id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAddonInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_cluster(self, request):
        """
        :param request: Request instance for ShowCluster
        :type request: :class:`g42cloudsdkcce.v3.ShowClusterRequest`
        :rtype: :class:`g42cloudsdkcce.v3.ShowClusterResponse`
        """
        return self.show_cluster_with_http_info(request)

    def show_cluster_with_http_info(self, request):
        all_params = ['cluster_id', 'detail']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []
        if 'detail' in local_var_params:
            query_params.append(('detail', local_var_params['detail']))

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
            resource_path='/api/v3/projects/{project_id}/clusters/{cluster_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowClusterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_job(self, request):
        """
        :param request: Request instance for ShowJob
        :type request: :class:`g42cloudsdkcce.v3.ShowJobRequest`
        :rtype: :class:`g42cloudsdkcce.v3.ShowJobResponse`
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
            resource_path='/api/v3/projects/{project_id}/jobs/{job_id}',
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

    def show_node(self, request):
        """
        :param request: Request instance for ShowNode
        :type request: :class:`g42cloudsdkcce.v3.ShowNodeRequest`
        :rtype: :class:`g42cloudsdkcce.v3.ShowNodeResponse`
        """
        return self.show_node_with_http_info(request)

    def show_node_with_http_info(self, request):
        all_params = ['cluster_id', 'node_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'node_id' in local_var_params:
            path_params['node_id'] = local_var_params['node_id']

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
            resource_path='/api/v3/projects/{project_id}/clusters/{cluster_id}/nodes/{node_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowNodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_node_pool(self, request):
        """
        :param request: Request instance for ShowNodePool
        :type request: :class:`g42cloudsdkcce.v3.ShowNodePoolRequest`
        :rtype: :class:`g42cloudsdkcce.v3.ShowNodePoolResponse`
        """
        return self.show_node_pool_with_http_info(request)

    def show_node_pool_with_http_info(self, request):
        all_params = ['cluster_id', 'nodepool_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'nodepool_id' in local_var_params:
            path_params['nodepool_id'] = local_var_params['nodepool_id']

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
            resource_path='/api/v3/projects/{project_id}/clusters/{cluster_id}/nodepools/{nodepool_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowNodePoolResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_addon_instance(self, request):
        """
        :param request: Request instance for UpdateAddonInstance
        :type request: :class:`g42cloudsdkcce.v3.UpdateAddonInstanceRequest`
        :rtype: :class:`g42cloudsdkcce.v3.UpdateAddonInstanceResponse`
        """
        return self.update_addon_instance_with_http_info(request)

    def update_addon_instance_with_http_info(self, request):
        all_params = ['id', 'update_addon_instance_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            resource_path='/api/v3/addons/{id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateAddonInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_cluster(self, request):
        """
        :param request: Request instance for UpdateCluster
        :type request: :class:`g42cloudsdkcce.v3.UpdateClusterRequest`
        :rtype: :class:`g42cloudsdkcce.v3.UpdateClusterResponse`
        """
        return self.update_cluster_with_http_info(request)

    def update_cluster_with_http_info(self, request):
        all_params = ['cluster_id', 'update_cluster_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/api/v3/projects/{project_id}/clusters/{cluster_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateClusterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_node(self, request):
        """
        :param request: Request instance for UpdateNode
        :type request: :class:`g42cloudsdkcce.v3.UpdateNodeRequest`
        :rtype: :class:`g42cloudsdkcce.v3.UpdateNodeResponse`
        """
        return self.update_node_with_http_info(request)

    def update_node_with_http_info(self, request):
        all_params = ['cluster_id', 'node_id', 'update_node_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'node_id' in local_var_params:
            path_params['node_id'] = local_var_params['node_id']

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
            resource_path='/api/v3/projects/{project_id}/clusters/{cluster_id}/nodes/{node_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateNodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_node_pool(self, request):
        """
        :param request: Request instance for UpdateNodePool
        :type request: :class:`g42cloudsdkcce.v3.UpdateNodePoolRequest`
        :rtype: :class:`g42cloudsdkcce.v3.UpdateNodePoolResponse`
        """
        return self.update_node_pool_with_http_info(request)

    def update_node_pool_with_http_info(self, request):
        all_params = ['cluster_id', 'nodepool_id', 'update_node_pool_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'nodepool_id' in local_var_params:
            path_params['nodepool_id'] = local_var_params['nodepool_id']

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
            resource_path='/api/v3/projects/{project_id}/clusters/{cluster_id}/nodepools/{nodepool_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateNodePoolResponse',
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
