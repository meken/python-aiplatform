# -*- coding: utf-8 -*-
# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from google.auth.transport.requests import AuthorizedSession  # type: ignore
import json  # type: ignore
import grpc  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import retry as retries
from google.api_core import rest_helpers
from google.api_core import rest_streaming
from google.api_core import path_template
from google.api_core import gapic_v1

from google.protobuf import json_format
from google.api_core import operations_v1
from google.iam.v1 import iam_policy_pb2  # type: ignore
from google.iam.v1 import policy_pb2  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from requests import __version__ as requests_version
import dataclasses
import re
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union
import warnings

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object, None]  # type: ignore


from google.cloud.aiplatform_v1beta1.types import artifact
from google.cloud.aiplatform_v1beta1.types import artifact as gca_artifact
from google.cloud.aiplatform_v1beta1.types import context
from google.cloud.aiplatform_v1beta1.types import context as gca_context
from google.cloud.aiplatform_v1beta1.types import execution
from google.cloud.aiplatform_v1beta1.types import execution as gca_execution
from google.cloud.aiplatform_v1beta1.types import lineage_subgraph
from google.cloud.aiplatform_v1beta1.types import metadata_schema
from google.cloud.aiplatform_v1beta1.types import metadata_schema as gca_metadata_schema
from google.cloud.aiplatform_v1beta1.types import metadata_service
from google.cloud.aiplatform_v1beta1.types import metadata_store
from google.longrunning import operations_pb2  # type: ignore

from .base import (
    MetadataServiceTransport,
    DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO,
)


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=BASE_DEFAULT_CLIENT_INFO.gapic_version,
    grpc_version=None,
    rest_version=requests_version,
)


class MetadataServiceRestInterceptor:
    """Interceptor for MetadataService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the MetadataServiceRestTransport.

    .. code-block:: python
        class MyCustomMetadataServiceInterceptor(MetadataServiceRestInterceptor):
            def pre_add_context_artifacts_and_executions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_add_context_artifacts_and_executions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_add_context_children(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_add_context_children(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_add_execution_events(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_add_execution_events(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_artifact(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_artifact(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_context(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_context(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_execution(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_execution(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_metadata_schema(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_metadata_schema(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_metadata_store(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_metadata_store(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_artifact(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_artifact(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_context(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_context(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_execution(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_execution(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_metadata_store(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_metadata_store(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_artifact(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_artifact(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_context(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_context(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_execution(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_execution(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_metadata_schema(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_metadata_schema(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_metadata_store(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_metadata_store(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_artifacts(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_artifacts(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_contexts(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_contexts(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_executions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_executions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_metadata_schemas(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_metadata_schemas(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_metadata_stores(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_metadata_stores(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_purge_artifacts(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_purge_artifacts(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_purge_contexts(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_purge_contexts(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_purge_executions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_purge_executions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_query_artifact_lineage_subgraph(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_query_artifact_lineage_subgraph(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_query_context_lineage_subgraph(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_query_context_lineage_subgraph(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_query_execution_inputs_and_outputs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_query_execution_inputs_and_outputs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_remove_context_children(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_remove_context_children(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_artifact(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_artifact(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_context(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_context(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_execution(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_execution(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = MetadataServiceRestTransport(interceptor=MyCustomMetadataServiceInterceptor())
        client = MetadataServiceClient(transport=transport)


    """

    def pre_add_context_artifacts_and_executions(
        self,
        request: metadata_service.AddContextArtifactsAndExecutionsRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[
        metadata_service.AddContextArtifactsAndExecutionsRequest,
        Sequence[Tuple[str, str]],
    ]:
        """Pre-rpc interceptor for add_context_artifacts_and_executions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MetadataService server.
        """
        return request, metadata

    def post_add_context_artifacts_and_executions(
        self, response: metadata_service.AddContextArtifactsAndExecutionsResponse
    ) -> metadata_service.AddContextArtifactsAndExecutionsResponse:
        """Post-rpc interceptor for add_context_artifacts_and_executions

        Override in a subclass to manipulate the response
        after it is returned by the MetadataService server but before
        it is returned to user code.
        """
        return response

    def pre_add_context_children(
        self,
        request: metadata_service.AddContextChildrenRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[metadata_service.AddContextChildrenRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for add_context_children

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MetadataService server.
        """
        return request, metadata

    def post_add_context_children(
        self, response: metadata_service.AddContextChildrenResponse
    ) -> metadata_service.AddContextChildrenResponse:
        """Post-rpc interceptor for add_context_children

        Override in a subclass to manipulate the response
        after it is returned by the MetadataService server but before
        it is returned to user code.
        """
        return response

    def pre_add_execution_events(
        self,
        request: metadata_service.AddExecutionEventsRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[metadata_service.AddExecutionEventsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for add_execution_events

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MetadataService server.
        """
        return request, metadata

    def post_add_execution_events(
        self, response: metadata_service.AddExecutionEventsResponse
    ) -> metadata_service.AddExecutionEventsResponse:
        """Post-rpc interceptor for add_execution_events

        Override in a subclass to manipulate the response
        after it is returned by the MetadataService server but before
        it is returned to user code.
        """
        return response

    def pre_create_artifact(
        self,
        request: metadata_service.CreateArtifactRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[metadata_service.CreateArtifactRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for create_artifact

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MetadataService server.
        """
        return request, metadata

    def post_create_artifact(
        self, response: gca_artifact.Artifact
    ) -> gca_artifact.Artifact:
        """Post-rpc interceptor for create_artifact

        Override in a subclass to manipulate the response
        after it is returned by the MetadataService server but before
        it is returned to user code.
        """
        return response

    def pre_create_context(
        self,
        request: metadata_service.CreateContextRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[metadata_service.CreateContextRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for create_context

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MetadataService server.
        """
        return request, metadata

    def post_create_context(self, response: gca_context.Context) -> gca_context.Context:
        """Post-rpc interceptor for create_context

        Override in a subclass to manipulate the response
        after it is returned by the MetadataService server but before
        it is returned to user code.
        """
        return response

    def pre_create_execution(
        self,
        request: metadata_service.CreateExecutionRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[metadata_service.CreateExecutionRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for create_execution

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MetadataService server.
        """
        return request, metadata

    def post_create_execution(
        self, response: gca_execution.Execution
    ) -> gca_execution.Execution:
        """Post-rpc interceptor for create_execution

        Override in a subclass to manipulate the response
        after it is returned by the MetadataService server but before
        it is returned to user code.
        """
        return response

    def pre_create_metadata_schema(
        self,
        request: metadata_service.CreateMetadataSchemaRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[metadata_service.CreateMetadataSchemaRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for create_metadata_schema

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MetadataService server.
        """
        return request, metadata

    def post_create_metadata_schema(
        self, response: gca_metadata_schema.MetadataSchema
    ) -> gca_metadata_schema.MetadataSchema:
        """Post-rpc interceptor for create_metadata_schema

        Override in a subclass to manipulate the response
        after it is returned by the MetadataService server but before
        it is returned to user code.
        """
        return response

    def pre_create_metadata_store(
        self,
        request: metadata_service.CreateMetadataStoreRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[metadata_service.CreateMetadataStoreRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for create_metadata_store

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MetadataService server.
        """
        return request, metadata

    def post_create_metadata_store(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_metadata_store

        Override in a subclass to manipulate the response
        after it is returned by the MetadataService server but before
        it is returned to user code.
        """
        return response

    def pre_delete_artifact(
        self,
        request: metadata_service.DeleteArtifactRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[metadata_service.DeleteArtifactRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for delete_artifact

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MetadataService server.
        """
        return request, metadata

    def post_delete_artifact(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_artifact

        Override in a subclass to manipulate the response
        after it is returned by the MetadataService server but before
        it is returned to user code.
        """
        return response

    def pre_delete_context(
        self,
        request: metadata_service.DeleteContextRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[metadata_service.DeleteContextRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for delete_context

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MetadataService server.
        """
        return request, metadata

    def post_delete_context(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_context

        Override in a subclass to manipulate the response
        after it is returned by the MetadataService server but before
        it is returned to user code.
        """
        return response

    def pre_delete_execution(
        self,
        request: metadata_service.DeleteExecutionRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[metadata_service.DeleteExecutionRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for delete_execution

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MetadataService server.
        """
        return request, metadata

    def post_delete_execution(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_execution

        Override in a subclass to manipulate the response
        after it is returned by the MetadataService server but before
        it is returned to user code.
        """
        return response

    def pre_delete_metadata_store(
        self,
        request: metadata_service.DeleteMetadataStoreRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[metadata_service.DeleteMetadataStoreRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for delete_metadata_store

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MetadataService server.
        """
        return request, metadata

    def post_delete_metadata_store(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_metadata_store

        Override in a subclass to manipulate the response
        after it is returned by the MetadataService server but before
        it is returned to user code.
        """
        return response

    def pre_get_artifact(
        self,
        request: metadata_service.GetArtifactRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[metadata_service.GetArtifactRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_artifact

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MetadataService server.
        """
        return request, metadata

    def post_get_artifact(self, response: artifact.Artifact) -> artifact.Artifact:
        """Post-rpc interceptor for get_artifact

        Override in a subclass to manipulate the response
        after it is returned by the MetadataService server but before
        it is returned to user code.
        """
        return response

    def pre_get_context(
        self,
        request: metadata_service.GetContextRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[metadata_service.GetContextRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_context

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MetadataService server.
        """
        return request, metadata

    def post_get_context(self, response: context.Context) -> context.Context:
        """Post-rpc interceptor for get_context

        Override in a subclass to manipulate the response
        after it is returned by the MetadataService server but before
        it is returned to user code.
        """
        return response

    def pre_get_execution(
        self,
        request: metadata_service.GetExecutionRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[metadata_service.GetExecutionRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_execution

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MetadataService server.
        """
        return request, metadata

    def post_get_execution(self, response: execution.Execution) -> execution.Execution:
        """Post-rpc interceptor for get_execution

        Override in a subclass to manipulate the response
        after it is returned by the MetadataService server but before
        it is returned to user code.
        """
        return response

    def pre_get_metadata_schema(
        self,
        request: metadata_service.GetMetadataSchemaRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[metadata_service.GetMetadataSchemaRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_metadata_schema

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MetadataService server.
        """
        return request, metadata

    def post_get_metadata_schema(
        self, response: metadata_schema.MetadataSchema
    ) -> metadata_schema.MetadataSchema:
        """Post-rpc interceptor for get_metadata_schema

        Override in a subclass to manipulate the response
        after it is returned by the MetadataService server but before
        it is returned to user code.
        """
        return response

    def pre_get_metadata_store(
        self,
        request: metadata_service.GetMetadataStoreRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[metadata_service.GetMetadataStoreRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_metadata_store

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MetadataService server.
        """
        return request, metadata

    def post_get_metadata_store(
        self, response: metadata_store.MetadataStore
    ) -> metadata_store.MetadataStore:
        """Post-rpc interceptor for get_metadata_store

        Override in a subclass to manipulate the response
        after it is returned by the MetadataService server but before
        it is returned to user code.
        """
        return response

    def pre_list_artifacts(
        self,
        request: metadata_service.ListArtifactsRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[metadata_service.ListArtifactsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_artifacts

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MetadataService server.
        """
        return request, metadata

    def post_list_artifacts(
        self, response: metadata_service.ListArtifactsResponse
    ) -> metadata_service.ListArtifactsResponse:
        """Post-rpc interceptor for list_artifacts

        Override in a subclass to manipulate the response
        after it is returned by the MetadataService server but before
        it is returned to user code.
        """
        return response

    def pre_list_contexts(
        self,
        request: metadata_service.ListContextsRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[metadata_service.ListContextsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_contexts

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MetadataService server.
        """
        return request, metadata

    def post_list_contexts(
        self, response: metadata_service.ListContextsResponse
    ) -> metadata_service.ListContextsResponse:
        """Post-rpc interceptor for list_contexts

        Override in a subclass to manipulate the response
        after it is returned by the MetadataService server but before
        it is returned to user code.
        """
        return response

    def pre_list_executions(
        self,
        request: metadata_service.ListExecutionsRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[metadata_service.ListExecutionsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_executions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MetadataService server.
        """
        return request, metadata

    def post_list_executions(
        self, response: metadata_service.ListExecutionsResponse
    ) -> metadata_service.ListExecutionsResponse:
        """Post-rpc interceptor for list_executions

        Override in a subclass to manipulate the response
        after it is returned by the MetadataService server but before
        it is returned to user code.
        """
        return response

    def pre_list_metadata_schemas(
        self,
        request: metadata_service.ListMetadataSchemasRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[metadata_service.ListMetadataSchemasRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_metadata_schemas

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MetadataService server.
        """
        return request, metadata

    def post_list_metadata_schemas(
        self, response: metadata_service.ListMetadataSchemasResponse
    ) -> metadata_service.ListMetadataSchemasResponse:
        """Post-rpc interceptor for list_metadata_schemas

        Override in a subclass to manipulate the response
        after it is returned by the MetadataService server but before
        it is returned to user code.
        """
        return response

    def pre_list_metadata_stores(
        self,
        request: metadata_service.ListMetadataStoresRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[metadata_service.ListMetadataStoresRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_metadata_stores

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MetadataService server.
        """
        return request, metadata

    def post_list_metadata_stores(
        self, response: metadata_service.ListMetadataStoresResponse
    ) -> metadata_service.ListMetadataStoresResponse:
        """Post-rpc interceptor for list_metadata_stores

        Override in a subclass to manipulate the response
        after it is returned by the MetadataService server but before
        it is returned to user code.
        """
        return response

    def pre_purge_artifacts(
        self,
        request: metadata_service.PurgeArtifactsRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[metadata_service.PurgeArtifactsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for purge_artifacts

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MetadataService server.
        """
        return request, metadata

    def post_purge_artifacts(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for purge_artifacts

        Override in a subclass to manipulate the response
        after it is returned by the MetadataService server but before
        it is returned to user code.
        """
        return response

    def pre_purge_contexts(
        self,
        request: metadata_service.PurgeContextsRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[metadata_service.PurgeContextsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for purge_contexts

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MetadataService server.
        """
        return request, metadata

    def post_purge_contexts(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for purge_contexts

        Override in a subclass to manipulate the response
        after it is returned by the MetadataService server but before
        it is returned to user code.
        """
        return response

    def pre_purge_executions(
        self,
        request: metadata_service.PurgeExecutionsRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[metadata_service.PurgeExecutionsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for purge_executions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MetadataService server.
        """
        return request, metadata

    def post_purge_executions(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for purge_executions

        Override in a subclass to manipulate the response
        after it is returned by the MetadataService server but before
        it is returned to user code.
        """
        return response

    def pre_query_artifact_lineage_subgraph(
        self,
        request: metadata_service.QueryArtifactLineageSubgraphRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[
        metadata_service.QueryArtifactLineageSubgraphRequest, Sequence[Tuple[str, str]]
    ]:
        """Pre-rpc interceptor for query_artifact_lineage_subgraph

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MetadataService server.
        """
        return request, metadata

    def post_query_artifact_lineage_subgraph(
        self, response: lineage_subgraph.LineageSubgraph
    ) -> lineage_subgraph.LineageSubgraph:
        """Post-rpc interceptor for query_artifact_lineage_subgraph

        Override in a subclass to manipulate the response
        after it is returned by the MetadataService server but before
        it is returned to user code.
        """
        return response

    def pre_query_context_lineage_subgraph(
        self,
        request: metadata_service.QueryContextLineageSubgraphRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[
        metadata_service.QueryContextLineageSubgraphRequest, Sequence[Tuple[str, str]]
    ]:
        """Pre-rpc interceptor for query_context_lineage_subgraph

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MetadataService server.
        """
        return request, metadata

    def post_query_context_lineage_subgraph(
        self, response: lineage_subgraph.LineageSubgraph
    ) -> lineage_subgraph.LineageSubgraph:
        """Post-rpc interceptor for query_context_lineage_subgraph

        Override in a subclass to manipulate the response
        after it is returned by the MetadataService server but before
        it is returned to user code.
        """
        return response

    def pre_query_execution_inputs_and_outputs(
        self,
        request: metadata_service.QueryExecutionInputsAndOutputsRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[
        metadata_service.QueryExecutionInputsAndOutputsRequest,
        Sequence[Tuple[str, str]],
    ]:
        """Pre-rpc interceptor for query_execution_inputs_and_outputs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MetadataService server.
        """
        return request, metadata

    def post_query_execution_inputs_and_outputs(
        self, response: lineage_subgraph.LineageSubgraph
    ) -> lineage_subgraph.LineageSubgraph:
        """Post-rpc interceptor for query_execution_inputs_and_outputs

        Override in a subclass to manipulate the response
        after it is returned by the MetadataService server but before
        it is returned to user code.
        """
        return response

    def pre_remove_context_children(
        self,
        request: metadata_service.RemoveContextChildrenRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[
        metadata_service.RemoveContextChildrenRequest, Sequence[Tuple[str, str]]
    ]:
        """Pre-rpc interceptor for remove_context_children

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MetadataService server.
        """
        return request, metadata

    def post_remove_context_children(
        self, response: metadata_service.RemoveContextChildrenResponse
    ) -> metadata_service.RemoveContextChildrenResponse:
        """Post-rpc interceptor for remove_context_children

        Override in a subclass to manipulate the response
        after it is returned by the MetadataService server but before
        it is returned to user code.
        """
        return response

    def pre_update_artifact(
        self,
        request: metadata_service.UpdateArtifactRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[metadata_service.UpdateArtifactRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for update_artifact

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MetadataService server.
        """
        return request, metadata

    def post_update_artifact(
        self, response: gca_artifact.Artifact
    ) -> gca_artifact.Artifact:
        """Post-rpc interceptor for update_artifact

        Override in a subclass to manipulate the response
        after it is returned by the MetadataService server but before
        it is returned to user code.
        """
        return response

    def pre_update_context(
        self,
        request: metadata_service.UpdateContextRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[metadata_service.UpdateContextRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for update_context

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MetadataService server.
        """
        return request, metadata

    def post_update_context(self, response: gca_context.Context) -> gca_context.Context:
        """Post-rpc interceptor for update_context

        Override in a subclass to manipulate the response
        after it is returned by the MetadataService server but before
        it is returned to user code.
        """
        return response

    def pre_update_execution(
        self,
        request: metadata_service.UpdateExecutionRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[metadata_service.UpdateExecutionRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for update_execution

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MetadataService server.
        """
        return request, metadata

    def post_update_execution(
        self, response: gca_execution.Execution
    ) -> gca_execution.Execution:
        """Post-rpc interceptor for update_execution

        Override in a subclass to manipulate the response
        after it is returned by the MetadataService server but before
        it is returned to user code.
        """
        return response

    def pre_get_location(
        self,
        request: locations_pb2.GetLocationRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[locations_pb2.GetLocationRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_location

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MetadataService server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the MetadataService server but before
        it is returned to user code.
        """
        return response

    def pre_list_locations(
        self,
        request: locations_pb2.ListLocationsRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[locations_pb2.ListLocationsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_locations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MetadataService server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the MetadataService server but before
        it is returned to user code.
        """
        return response

    def pre_get_iam_policy(
        self,
        request: iam_policy_pb2.GetIamPolicyRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[iam_policy_pb2.GetIamPolicyRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MetadataService server.
        """
        return request, metadata

    def post_get_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the MetadataService server but before
        it is returned to user code.
        """
        return response

    def pre_set_iam_policy(
        self,
        request: iam_policy_pb2.SetIamPolicyRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[iam_policy_pb2.SetIamPolicyRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MetadataService server.
        """
        return request, metadata

    def post_set_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the MetadataService server but before
        it is returned to user code.
        """
        return response

    def pre_test_iam_permissions(
        self,
        request: iam_policy_pb2.TestIamPermissionsRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[iam_policy_pb2.TestIamPermissionsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MetadataService server.
        """
        return request, metadata

    def post_test_iam_permissions(
        self, response: iam_policy_pb2.TestIamPermissionsResponse
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        """Post-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the response
        after it is returned by the MetadataService server but before
        it is returned to user code.
        """
        return response

    def pre_cancel_operation(
        self,
        request: operations_pb2.CancelOperationRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[operations_pb2.CancelOperationRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MetadataService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the MetadataService server but before
        it is returned to user code.
        """
        return response

    def pre_delete_operation(
        self,
        request: operations_pb2.DeleteOperationRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[operations_pb2.DeleteOperationRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for delete_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MetadataService server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the MetadataService server but before
        it is returned to user code.
        """
        return response

    def pre_get_operation(
        self,
        request: operations_pb2.GetOperationRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[operations_pb2.GetOperationRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MetadataService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the MetadataService server but before
        it is returned to user code.
        """
        return response

    def pre_list_operations(
        self,
        request: operations_pb2.ListOperationsRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[operations_pb2.ListOperationsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_operations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MetadataService server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the MetadataService server but before
        it is returned to user code.
        """
        return response

    def pre_wait_operation(
        self,
        request: operations_pb2.WaitOperationRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[operations_pb2.WaitOperationRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for wait_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MetadataService server.
        """
        return request, metadata

    def post_wait_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for wait_operation

        Override in a subclass to manipulate the response
        after it is returned by the MetadataService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class MetadataServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: MetadataServiceRestInterceptor


class MetadataServiceRestTransport(MetadataServiceTransport):
    """REST backend transport for MetadataService.

    Service for reading and writing metadata entries.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1

    NOTE: This REST transport functionality is currently in a beta
    state (preview). We welcome your feedback via an issue in this
    library's source repository. Thank you!
    """

    def __init__(
        self,
        *,
        host: str = "aiplatform.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[MetadataServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        NOTE: This REST transport functionality is currently in a beta
        state (preview). We welcome your feedback via a GitHub issue in
        this library's repository. Thank you!

         Args:
             host (Optional[str]):
                  The hostname to connect to (default: 'aiplatform.googleapis.com').
             credentials (Optional[google.auth.credentials.Credentials]): The
                 authorization credentials to attach to requests. These
                 credentials identify the application to the service; if none
                 are specified, the client will attempt to ascertain the
                 credentials from the environment.

             credentials_file (Optional[str]): A file with credentials that can
                 be loaded with :func:`google.auth.load_credentials_from_file`.
                 This argument is ignored if ``channel`` is provided.
             scopes (Optional(Sequence[str])): A list of scopes. This argument is
                 ignored if ``channel`` is provided.
             client_cert_source_for_mtls (Callable[[], Tuple[bytes, bytes]]): Client
                 certificate to configure mutual TLS HTTP channel. It is ignored
                 if ``channel`` is provided.
             quota_project_id (Optional[str]): An optional project to use for billing
                 and quota.
             client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                 The client info used to send a user-agent string along with
                 API requests. If ``None``, then default info will be used.
                 Generally, you only need to set this if you are developing
                 your own client library.
             always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                 be used for service account credentials.
             url_scheme: the protocol scheme for the API endpoint.  Normally
                 "https", but for testing or local servers,
                 "http" can be specified.
        """
        # Run the base constructor
        # TODO(yon-mg): resolve other ctor params i.e. scopes, quota, etc.
        # TODO: When custom host (api_endpoint) is set, `scopes` must *also* be set on the
        # credentials object
        maybe_url_match = re.match("^(?P<scheme>http(?:s)?://)?(?P<host>.*)$", host)
        if maybe_url_match is None:
            raise ValueError(
                f"Unexpected hostname structure: {host}"
            )  # pragma: NO COVER

        url_match_items = maybe_url_match.groupdict()

        host = f"{url_scheme}://{host}" if not url_match_items["scheme"] else host

        super().__init__(
            host=host,
            credentials=credentials,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            api_audience=api_audience,
        )
        self._session = AuthorizedSession(
            self._credentials, default_host=self.DEFAULT_HOST
        )
        self._operations_client: Optional[operations_v1.AbstractOperationsClient] = None
        if client_cert_source_for_mtls:
            self._session.configure_mtls_channel(client_cert_source_for_mtls)
        self._interceptor = interceptor or MetadataServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    @property
    def operations_client(self) -> operations_v1.AbstractOperationsClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Only create a new client if we do not already have one.
        if self._operations_client is None:
            http_options: Dict[str, List[Dict[str, str]]] = {
                "google.longrunning.Operations.CancelOperation": [
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/dataItems/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/savedQueries/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/annotationSpecs/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/dataItems/*/annotations/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/deploymentResourcePools/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/edgeDevices/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/endpoints/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/extensionControllers/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/extensions/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/featurestores/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/featurestores/*/entityTypes/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/featurestores/*/entityTypes/*/features/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/customJobs/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/dataLabelingJobs/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/hyperparameterTuningJobs/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/tuningJobs/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/indexes/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/indexEndpoints/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/artifacts/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/contexts/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/executions/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/modelMonitors/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/migratableResources/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/models/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/models/*/evaluations/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/persistentResources/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/studies/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/studies/*/trials/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/trainingPipelines/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/pipelineJobs/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/schedules/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/specialistPools/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/timeSeries/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/dataItems/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/savedQueries/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/annotationSpecs/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/dataItems/*/annotations/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/deploymentResourcePools/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/edgeDevices/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/endpoints/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/exampleStores/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/extensionControllers/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/extensions/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/entityTypes/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/entityTypes/*/features/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/customJobs/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/dataLabelingJobs/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/hyperparameterTuningJobs/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/indexes/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/indexEndpoints/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/artifacts/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/contexts/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/executions/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/modelMonitors/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/migratableResources/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/models/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/models/*/evaluations/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/persistentResources/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/ragCorpora/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/ragCorpora/*/ragFiles/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/studies/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/studies/*/trials/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/trainingPipelines/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/pipelineJobs/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/reasoningEngines/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/schedules/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/specialistPools/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/timeSeries/*/operations/*}:cancel",
                    },
                ],
                "google.longrunning.Operations.DeleteOperation": [
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/dataItems/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/savedQueries/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/annotationSpecs/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/dataItems/*/annotations/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/deploymentResourcePools/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/edgeDevices/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/endpoints/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/extensionControllers/*}/operations",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/extensions/*}/operations",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/featurestores/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/featurestores/*/entityTypes/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/featurestores/*/entityTypes/*/features/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/customJobs/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/dataLabelingJobs/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/hyperparameterTuningJobs/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/indexes/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/indexEndpoints/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/artifacts/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/contexts/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/executions/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/modelMonitors/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/migratableResources/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/models/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/models/*/evaluations/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/persistentResources/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/studies/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/studies/*/trials/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/trainingPipelines/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/pipelineJobs/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/schedules/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/specialistPools/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/timeSeries/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/featureOnlineStores/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/featureGroups/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/featureGroups/*/features/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/featureOnlineStores/*/featureViews/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/dataItems/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/savedQueries/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/annotationSpecs/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/dataItems/*/annotations/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/deploymentResourcePools/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/edgeDevices/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/endpoints/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/entityTypes/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/entityTypes/*/features/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/customJobs/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/dataLabelingJobs/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/evaluationTasks/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/exampleStores/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/extensionControllers/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/extensions/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/hyperparameterTuningJobs/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/indexes/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/indexEndpoints/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/artifacts/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/contexts/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/executions/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/modelMonitors/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/migratableResources/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/models/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/models/*/evaluations/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/persistentResources/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/ragCorpora/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/ragCorpora/*/ragFiles/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/reasoningEngines/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/solvers/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/studies/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/studies/*/trials/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/trainingPipelines/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/pipelineJobs/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/schedules/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/specialistPools/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/timeSeries/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featureOnlineStores/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featureGroups/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featureGroups/*/features/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featureOnlineStores/*/featureViews/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.GetOperation": [
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/dataItems/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/savedQueries/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/annotationSpecs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/dataItems/*/annotations/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/deploymentResourcePools/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/edgeDeploymentJobs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/edgeDevices/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/endpoints/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/extensionControllers/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/extensions/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/featurestores/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/featurestores/*/entityTypes/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/featurestores/*/entityTypes/*/features/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/customJobs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/dataLabelingJobs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/hyperparameterTuningJobs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/tuningJobs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/indexes/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/indexEndpoints/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/artifacts/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/contexts/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/executions/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/modelMonitors/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/migratableResources/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/models/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/models/*/evaluations/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/persistentResources/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/studies/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/studies/*/trials/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/trainingPipelines/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/pipelineJobs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/schedules/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/specialistPools/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/timeSeries/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/featureOnlineStores/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/featureOnlineStores/*/featureViews/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/featureGroups/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/featureGroups/*/features/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/dataItems/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/savedQueries/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/annotationSpecs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/dataItems/*/annotations/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/deploymentResourcePools/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/edgeDevices/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/endpoints/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/evaluationTasks/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/exampleStores/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/extensionControllers/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/extensions/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/entityTypes/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/entityTypes/*/features/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/customJobs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/dataLabelingJobs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/hyperparameterTuningJobs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/indexes/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/indexEndpoints/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/artifacts/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/contexts/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/executions/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/modelMonitors/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/migratableResources/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/models/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/models/*/evaluations/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/persistentResources/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/ragCorpora/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/ragCorpora/*/ragFiles/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/reasoningEngines/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/solvers/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/studies/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/studies/*/trials/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/trainingPipelines/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/pipelineJobs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/schedules/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/specialistPools/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/timeSeries/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featureOnlineStores/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featureOnlineStores/*/featureViews/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featureGroups/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featureGroups/*/features/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.ListOperations": [
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/dataItems/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/savedQueries/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/annotationSpecs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/dataItems/*/annotations/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/deploymentResourcePools/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/edgeDevices/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/endpoints/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/extensionControllers/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/extensions/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/featurestores/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/featurestores/*/entityTypes/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/featurestores/*/entityTypes/*/features/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/customJobs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/dataLabelingJobs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/hyperparameterTuningJobs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/tuningJobs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/indexes/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/indexEndpoints/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/artifacts/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/contexts/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/executions/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/modelMonitors/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/migratableResources/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/models/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/models/*/evaluations/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/studies/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/studies/*/trials/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/trainingPipelines/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/persistentResources/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/pipelineJobs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/schedules/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/specialistPools/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/timeSeries/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/featureOnlineStores/*/operations/*}:wait",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/featureOnlineStores/*/featureViews/*/operations/*}:wait",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/featureGroups/*/operations/*}:wait",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/featureGroups/*/features/*/operations/*}:wait",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/dataItems/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/savedQueries/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/annotationSpecs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/dataItems/*/annotations/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/deploymentResourcePools/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/edgeDevices/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/endpoints/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/evaluationTasks/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/exampleStores/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/extensionControllers/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/extensions/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/entityTypes/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/entityTypes/*/features/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/customJobs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/dataLabelingJobs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/hyperparameterTuningJobs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/indexes/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/indexEndpoints/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/artifacts/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/contexts/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/executions/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/modelMonitors/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/migratableResources/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/models/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/models/*/evaluations/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/persistentResources/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/ragCorpora/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/ragCorpora/*/ragFiles/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/reasoningEngines/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/solvers/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/studies/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/studies/*/trials/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/trainingPipelines/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/pipelineJobs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/schedules/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/specialistPools/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/timeSeries/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featureOnlineStores/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featureOnlineStores/*/featureViews/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featureGroups/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featureGroups/*/features/*}/operations",
                    },
                ],
                "google.longrunning.Operations.WaitOperation": [
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/dataItems/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/savedQueries/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/annotationSpecs/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/dataItems/*/annotations/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/deploymentResourcePools/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/edgeDevices/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/endpoints/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/extensionControllers/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/extensions/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/featurestores/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/featurestores/*/entityTypes/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/featurestores/*/entityTypes/*/features/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/customJobs/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/dataLabelingJobs/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/hyperparameterTuningJobs/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/tuningJobs/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/indexes/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/indexEndpoints/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/artifacts/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/contexts/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/executions/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/modelMonitors/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/migratableResources/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/models/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/models/*/evaluations/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/studies/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/studies/*/trials/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/trainingPipelines/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/persistentResources/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/pipelineJobs/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/schedules/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/specialistPools/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/timeSeries/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/featureOnlineStores/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/featureOnlineStores/*/featureViews/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/featureGroups/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/featureGroups/*/features/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/dataItems/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/savedQueries/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/annotationSpecs/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/dataItems/*/annotations/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/deploymentResourcePools/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/edgeDevices/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/endpoints/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/evaluationTasks/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/exampleStores/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/extensionControllers/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/extensions/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/entityTypes/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/entityTypes/*/features/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/customJobs/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/dataLabelingJobs/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/hyperparameterTuningJobs/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/indexes/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/indexEndpoints/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/artifacts/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/contexts/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/executions/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/modelMonitors/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/migratableResources/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/models/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/models/*/evaluations/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/persistentResources/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/ragCorpora/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/ragCorpora/*/ragFiles/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/reasoningEngines/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/studies/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/studies/*/trials/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/trainingPipelines/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/pipelineJobs/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/schedules/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/specialistPools/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/timeSeries/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featureOnlineStores/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featureOnlineStores/*/featureViews/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featureGroups/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featureGroups/*/features/*/operations/*}:wait",
                    },
                ],
            }

            rest_transport = operations_v1.OperationsRestTransport(
                host=self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                scopes=self._scopes,
                http_options=http_options,
                path_prefix="v1beta1",
            )

            self._operations_client = operations_v1.AbstractOperationsClient(
                transport=rest_transport
            )

        # Return the client from cache.
        return self._operations_client

    class _AddContextArtifactsAndExecutions(MetadataServiceRestStub):
        def __hash__(self):
            return hash("AddContextArtifactsAndExecutions")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: metadata_service.AddContextArtifactsAndExecutionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> metadata_service.AddContextArtifactsAndExecutionsResponse:
            r"""Call the add context artifacts and
            executions method over HTTP.

                Args:
                    request (~.metadata_service.AddContextArtifactsAndExecutionsRequest):
                        The request object. Request message for
                    [MetadataService.AddContextArtifactsAndExecutions][google.cloud.aiplatform.v1beta1.MetadataService.AddContextArtifactsAndExecutions].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, str]]): Strings which should be
                        sent along with the request as metadata.

                Returns:
                    ~.metadata_service.AddContextArtifactsAndExecutionsResponse:
                        Response message for
                    [MetadataService.AddContextArtifactsAndExecutions][google.cloud.aiplatform.v1beta1.MetadataService.AddContextArtifactsAndExecutions].

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1beta1/{context=projects/*/locations/*/metadataStores/*/contexts/*}:addContextArtifactsAndExecutions",
                    "body": "*",
                },
            ]
            (
                request,
                metadata,
            ) = self._interceptor.pre_add_context_artifacts_and_executions(
                request, metadata
            )
            pb_request = metadata_service.AddContextArtifactsAndExecutionsRequest.pb(
                request
            )
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request["body"], use_integers_for_enums=False
            )
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    use_integers_for_enums=False,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = metadata_service.AddContextArtifactsAndExecutionsResponse()
            pb_resp = metadata_service.AddContextArtifactsAndExecutionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_add_context_artifacts_and_executions(resp)
            return resp

    class _AddContextChildren(MetadataServiceRestStub):
        def __hash__(self):
            return hash("AddContextChildren")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: metadata_service.AddContextChildrenRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> metadata_service.AddContextChildrenResponse:
            r"""Call the add context children method over HTTP.

            Args:
                request (~.metadata_service.AddContextChildrenRequest):
                    The request object. Request message for
                [MetadataService.AddContextChildren][google.cloud.aiplatform.v1beta1.MetadataService.AddContextChildren].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.metadata_service.AddContextChildrenResponse:
                    Response message for
                [MetadataService.AddContextChildren][google.cloud.aiplatform.v1beta1.MetadataService.AddContextChildren].

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1beta1/{context=projects/*/locations/*/metadataStores/*/contexts/*}:addContextChildren",
                    "body": "*",
                },
            ]
            request, metadata = self._interceptor.pre_add_context_children(
                request, metadata
            )
            pb_request = metadata_service.AddContextChildrenRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request["body"], use_integers_for_enums=False
            )
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    use_integers_for_enums=False,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = metadata_service.AddContextChildrenResponse()
            pb_resp = metadata_service.AddContextChildrenResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_add_context_children(resp)
            return resp

    class _AddExecutionEvents(MetadataServiceRestStub):
        def __hash__(self):
            return hash("AddExecutionEvents")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: metadata_service.AddExecutionEventsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> metadata_service.AddExecutionEventsResponse:
            r"""Call the add execution events method over HTTP.

            Args:
                request (~.metadata_service.AddExecutionEventsRequest):
                    The request object. Request message for
                [MetadataService.AddExecutionEvents][google.cloud.aiplatform.v1beta1.MetadataService.AddExecutionEvents].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.metadata_service.AddExecutionEventsResponse:
                    Response message for
                [MetadataService.AddExecutionEvents][google.cloud.aiplatform.v1beta1.MetadataService.AddExecutionEvents].

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1beta1/{execution=projects/*/locations/*/metadataStores/*/executions/*}:addExecutionEvents",
                    "body": "*",
                },
            ]
            request, metadata = self._interceptor.pre_add_execution_events(
                request, metadata
            )
            pb_request = metadata_service.AddExecutionEventsRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request["body"], use_integers_for_enums=False
            )
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    use_integers_for_enums=False,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = metadata_service.AddExecutionEventsResponse()
            pb_resp = metadata_service.AddExecutionEventsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_add_execution_events(resp)
            return resp

    class _CreateArtifact(MetadataServiceRestStub):
        def __hash__(self):
            return hash("CreateArtifact")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: metadata_service.CreateArtifactRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> gca_artifact.Artifact:
            r"""Call the create artifact method over HTTP.

            Args:
                request (~.metadata_service.CreateArtifactRequest):
                    The request object. Request message for
                [MetadataService.CreateArtifact][google.cloud.aiplatform.v1beta1.MetadataService.CreateArtifact].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.gca_artifact.Artifact:
                    Instance of a general artifact.
            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1beta1/{parent=projects/*/locations/*/metadataStores/*}/artifacts",
                    "body": "artifact",
                },
            ]
            request, metadata = self._interceptor.pre_create_artifact(request, metadata)
            pb_request = metadata_service.CreateArtifactRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request["body"], use_integers_for_enums=False
            )
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    use_integers_for_enums=False,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = gca_artifact.Artifact()
            pb_resp = gca_artifact.Artifact.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_create_artifact(resp)
            return resp

    class _CreateContext(MetadataServiceRestStub):
        def __hash__(self):
            return hash("CreateContext")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: metadata_service.CreateContextRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> gca_context.Context:
            r"""Call the create context method over HTTP.

            Args:
                request (~.metadata_service.CreateContextRequest):
                    The request object. Request message for
                [MetadataService.CreateContext][google.cloud.aiplatform.v1beta1.MetadataService.CreateContext].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.gca_context.Context:
                    Instance of a general context.
            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1beta1/{parent=projects/*/locations/*/metadataStores/*}/contexts",
                    "body": "context",
                },
            ]
            request, metadata = self._interceptor.pre_create_context(request, metadata)
            pb_request = metadata_service.CreateContextRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request["body"], use_integers_for_enums=False
            )
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    use_integers_for_enums=False,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = gca_context.Context()
            pb_resp = gca_context.Context.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_create_context(resp)
            return resp

    class _CreateExecution(MetadataServiceRestStub):
        def __hash__(self):
            return hash("CreateExecution")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: metadata_service.CreateExecutionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> gca_execution.Execution:
            r"""Call the create execution method over HTTP.

            Args:
                request (~.metadata_service.CreateExecutionRequest):
                    The request object. Request message for
                [MetadataService.CreateExecution][google.cloud.aiplatform.v1beta1.MetadataService.CreateExecution].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.gca_execution.Execution:
                    Instance of a general execution.
            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1beta1/{parent=projects/*/locations/*/metadataStores/*}/executions",
                    "body": "execution",
                },
            ]
            request, metadata = self._interceptor.pre_create_execution(
                request, metadata
            )
            pb_request = metadata_service.CreateExecutionRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request["body"], use_integers_for_enums=False
            )
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    use_integers_for_enums=False,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = gca_execution.Execution()
            pb_resp = gca_execution.Execution.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_create_execution(resp)
            return resp

    class _CreateMetadataSchema(MetadataServiceRestStub):
        def __hash__(self):
            return hash("CreateMetadataSchema")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: metadata_service.CreateMetadataSchemaRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> gca_metadata_schema.MetadataSchema:
            r"""Call the create metadata schema method over HTTP.

            Args:
                request (~.metadata_service.CreateMetadataSchemaRequest):
                    The request object. Request message for
                [MetadataService.CreateMetadataSchema][google.cloud.aiplatform.v1beta1.MetadataService.CreateMetadataSchema].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.gca_metadata_schema.MetadataSchema:
                    Instance of a general MetadataSchema.
            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1beta1/{parent=projects/*/locations/*/metadataStores/*}/metadataSchemas",
                    "body": "metadata_schema",
                },
            ]
            request, metadata = self._interceptor.pre_create_metadata_schema(
                request, metadata
            )
            pb_request = metadata_service.CreateMetadataSchemaRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request["body"], use_integers_for_enums=False
            )
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    use_integers_for_enums=False,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = gca_metadata_schema.MetadataSchema()
            pb_resp = gca_metadata_schema.MetadataSchema.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_create_metadata_schema(resp)
            return resp

    class _CreateMetadataStore(MetadataServiceRestStub):
        def __hash__(self):
            return hash("CreateMetadataStore")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: metadata_service.CreateMetadataStoreRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create metadata store method over HTTP.

            Args:
                request (~.metadata_service.CreateMetadataStoreRequest):
                    The request object. Request message for
                [MetadataService.CreateMetadataStore][google.cloud.aiplatform.v1beta1.MetadataService.CreateMetadataStore].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1beta1/{parent=projects/*/locations/*}/metadataStores",
                    "body": "metadata_store",
                },
            ]
            request, metadata = self._interceptor.pre_create_metadata_store(
                request, metadata
            )
            pb_request = metadata_service.CreateMetadataStoreRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request["body"], use_integers_for_enums=False
            )
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    use_integers_for_enums=False,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_create_metadata_store(resp)
            return resp

    class _DeleteArtifact(MetadataServiceRestStub):
        def __hash__(self):
            return hash("DeleteArtifact")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: metadata_service.DeleteArtifactRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete artifact method over HTTP.

            Args:
                request (~.metadata_service.DeleteArtifactRequest):
                    The request object. Request message for
                [MetadataService.DeleteArtifact][google.cloud.aiplatform.v1beta1.MetadataService.DeleteArtifact].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/artifacts/*}",
                },
            ]
            request, metadata = self._interceptor.pre_delete_artifact(request, metadata)
            pb_request = metadata_service.DeleteArtifactRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    use_integers_for_enums=False,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_delete_artifact(resp)
            return resp

    class _DeleteContext(MetadataServiceRestStub):
        def __hash__(self):
            return hash("DeleteContext")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: metadata_service.DeleteContextRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete context method over HTTP.

            Args:
                request (~.metadata_service.DeleteContextRequest):
                    The request object. Request message for
                [MetadataService.DeleteContext][google.cloud.aiplatform.v1beta1.MetadataService.DeleteContext].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/contexts/*}",
                },
            ]
            request, metadata = self._interceptor.pre_delete_context(request, metadata)
            pb_request = metadata_service.DeleteContextRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    use_integers_for_enums=False,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_delete_context(resp)
            return resp

    class _DeleteExecution(MetadataServiceRestStub):
        def __hash__(self):
            return hash("DeleteExecution")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: metadata_service.DeleteExecutionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete execution method over HTTP.

            Args:
                request (~.metadata_service.DeleteExecutionRequest):
                    The request object. Request message for
                [MetadataService.DeleteExecution][google.cloud.aiplatform.v1beta1.MetadataService.DeleteExecution].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/executions/*}",
                },
            ]
            request, metadata = self._interceptor.pre_delete_execution(
                request, metadata
            )
            pb_request = metadata_service.DeleteExecutionRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    use_integers_for_enums=False,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_delete_execution(resp)
            return resp

    class _DeleteMetadataStore(MetadataServiceRestStub):
        def __hash__(self):
            return hash("DeleteMetadataStore")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: metadata_service.DeleteMetadataStoreRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete metadata store method over HTTP.

            Args:
                request (~.metadata_service.DeleteMetadataStoreRequest):
                    The request object. Request message for
                [MetadataService.DeleteMetadataStore][google.cloud.aiplatform.v1beta1.MetadataService.DeleteMetadataStore].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*}",
                },
            ]
            request, metadata = self._interceptor.pre_delete_metadata_store(
                request, metadata
            )
            pb_request = metadata_service.DeleteMetadataStoreRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    use_integers_for_enums=False,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_delete_metadata_store(resp)
            return resp

    class _GetArtifact(MetadataServiceRestStub):
        def __hash__(self):
            return hash("GetArtifact")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: metadata_service.GetArtifactRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> artifact.Artifact:
            r"""Call the get artifact method over HTTP.

            Args:
                request (~.metadata_service.GetArtifactRequest):
                    The request object. Request message for
                [MetadataService.GetArtifact][google.cloud.aiplatform.v1beta1.MetadataService.GetArtifact].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.artifact.Artifact:
                    Instance of a general artifact.
            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/artifacts/*}",
                },
            ]
            request, metadata = self._interceptor.pre_get_artifact(request, metadata)
            pb_request = metadata_service.GetArtifactRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    use_integers_for_enums=False,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = artifact.Artifact()
            pb_resp = artifact.Artifact.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_get_artifact(resp)
            return resp

    class _GetContext(MetadataServiceRestStub):
        def __hash__(self):
            return hash("GetContext")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: metadata_service.GetContextRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> context.Context:
            r"""Call the get context method over HTTP.

            Args:
                request (~.metadata_service.GetContextRequest):
                    The request object. Request message for
                [MetadataService.GetContext][google.cloud.aiplatform.v1beta1.MetadataService.GetContext].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.context.Context:
                    Instance of a general context.
            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/contexts/*}",
                },
            ]
            request, metadata = self._interceptor.pre_get_context(request, metadata)
            pb_request = metadata_service.GetContextRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    use_integers_for_enums=False,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = context.Context()
            pb_resp = context.Context.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_get_context(resp)
            return resp

    class _GetExecution(MetadataServiceRestStub):
        def __hash__(self):
            return hash("GetExecution")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: metadata_service.GetExecutionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> execution.Execution:
            r"""Call the get execution method over HTTP.

            Args:
                request (~.metadata_service.GetExecutionRequest):
                    The request object. Request message for
                [MetadataService.GetExecution][google.cloud.aiplatform.v1beta1.MetadataService.GetExecution].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.execution.Execution:
                    Instance of a general execution.
            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/executions/*}",
                },
            ]
            request, metadata = self._interceptor.pre_get_execution(request, metadata)
            pb_request = metadata_service.GetExecutionRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    use_integers_for_enums=False,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = execution.Execution()
            pb_resp = execution.Execution.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_get_execution(resp)
            return resp

    class _GetMetadataSchema(MetadataServiceRestStub):
        def __hash__(self):
            return hash("GetMetadataSchema")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: metadata_service.GetMetadataSchemaRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> metadata_schema.MetadataSchema:
            r"""Call the get metadata schema method over HTTP.

            Args:
                request (~.metadata_service.GetMetadataSchemaRequest):
                    The request object. Request message for
                [MetadataService.GetMetadataSchema][google.cloud.aiplatform.v1beta1.MetadataService.GetMetadataSchema].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.metadata_schema.MetadataSchema:
                    Instance of a general MetadataSchema.
            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/metadataSchemas/*}",
                },
            ]
            request, metadata = self._interceptor.pre_get_metadata_schema(
                request, metadata
            )
            pb_request = metadata_service.GetMetadataSchemaRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    use_integers_for_enums=False,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = metadata_schema.MetadataSchema()
            pb_resp = metadata_schema.MetadataSchema.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_get_metadata_schema(resp)
            return resp

    class _GetMetadataStore(MetadataServiceRestStub):
        def __hash__(self):
            return hash("GetMetadataStore")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: metadata_service.GetMetadataStoreRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> metadata_store.MetadataStore:
            r"""Call the get metadata store method over HTTP.

            Args:
                request (~.metadata_service.GetMetadataStoreRequest):
                    The request object. Request message for
                [MetadataService.GetMetadataStore][google.cloud.aiplatform.v1beta1.MetadataService.GetMetadataStore].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.metadata_store.MetadataStore:
                    Instance of a metadata store.
                Contains a set of metadata that can be
                queried.

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*}",
                },
            ]
            request, metadata = self._interceptor.pre_get_metadata_store(
                request, metadata
            )
            pb_request = metadata_service.GetMetadataStoreRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    use_integers_for_enums=False,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = metadata_store.MetadataStore()
            pb_resp = metadata_store.MetadataStore.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_get_metadata_store(resp)
            return resp

    class _ListArtifacts(MetadataServiceRestStub):
        def __hash__(self):
            return hash("ListArtifacts")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: metadata_service.ListArtifactsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> metadata_service.ListArtifactsResponse:
            r"""Call the list artifacts method over HTTP.

            Args:
                request (~.metadata_service.ListArtifactsRequest):
                    The request object. Request message for
                [MetadataService.ListArtifacts][google.cloud.aiplatform.v1beta1.MetadataService.ListArtifacts].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.metadata_service.ListArtifactsResponse:
                    Response message for
                [MetadataService.ListArtifacts][google.cloud.aiplatform.v1beta1.MetadataService.ListArtifacts].

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1beta1/{parent=projects/*/locations/*/metadataStores/*}/artifacts",
                },
            ]
            request, metadata = self._interceptor.pre_list_artifacts(request, metadata)
            pb_request = metadata_service.ListArtifactsRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    use_integers_for_enums=False,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = metadata_service.ListArtifactsResponse()
            pb_resp = metadata_service.ListArtifactsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_list_artifacts(resp)
            return resp

    class _ListContexts(MetadataServiceRestStub):
        def __hash__(self):
            return hash("ListContexts")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: metadata_service.ListContextsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> metadata_service.ListContextsResponse:
            r"""Call the list contexts method over HTTP.

            Args:
                request (~.metadata_service.ListContextsRequest):
                    The request object. Request message for
                [MetadataService.ListContexts][google.cloud.aiplatform.v1beta1.MetadataService.ListContexts]
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.metadata_service.ListContextsResponse:
                    Response message for
                [MetadataService.ListContexts][google.cloud.aiplatform.v1beta1.MetadataService.ListContexts].

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1beta1/{parent=projects/*/locations/*/metadataStores/*}/contexts",
                },
            ]
            request, metadata = self._interceptor.pre_list_contexts(request, metadata)
            pb_request = metadata_service.ListContextsRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    use_integers_for_enums=False,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = metadata_service.ListContextsResponse()
            pb_resp = metadata_service.ListContextsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_list_contexts(resp)
            return resp

    class _ListExecutions(MetadataServiceRestStub):
        def __hash__(self):
            return hash("ListExecutions")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: metadata_service.ListExecutionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> metadata_service.ListExecutionsResponse:
            r"""Call the list executions method over HTTP.

            Args:
                request (~.metadata_service.ListExecutionsRequest):
                    The request object. Request message for
                [MetadataService.ListExecutions][google.cloud.aiplatform.v1beta1.MetadataService.ListExecutions].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.metadata_service.ListExecutionsResponse:
                    Response message for
                [MetadataService.ListExecutions][google.cloud.aiplatform.v1beta1.MetadataService.ListExecutions].

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1beta1/{parent=projects/*/locations/*/metadataStores/*}/executions",
                },
            ]
            request, metadata = self._interceptor.pre_list_executions(request, metadata)
            pb_request = metadata_service.ListExecutionsRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    use_integers_for_enums=False,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = metadata_service.ListExecutionsResponse()
            pb_resp = metadata_service.ListExecutionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_list_executions(resp)
            return resp

    class _ListMetadataSchemas(MetadataServiceRestStub):
        def __hash__(self):
            return hash("ListMetadataSchemas")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: metadata_service.ListMetadataSchemasRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> metadata_service.ListMetadataSchemasResponse:
            r"""Call the list metadata schemas method over HTTP.

            Args:
                request (~.metadata_service.ListMetadataSchemasRequest):
                    The request object. Request message for
                [MetadataService.ListMetadataSchemas][google.cloud.aiplatform.v1beta1.MetadataService.ListMetadataSchemas].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.metadata_service.ListMetadataSchemasResponse:
                    Response message for
                [MetadataService.ListMetadataSchemas][google.cloud.aiplatform.v1beta1.MetadataService.ListMetadataSchemas].

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1beta1/{parent=projects/*/locations/*/metadataStores/*}/metadataSchemas",
                },
            ]
            request, metadata = self._interceptor.pre_list_metadata_schemas(
                request, metadata
            )
            pb_request = metadata_service.ListMetadataSchemasRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    use_integers_for_enums=False,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = metadata_service.ListMetadataSchemasResponse()
            pb_resp = metadata_service.ListMetadataSchemasResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_list_metadata_schemas(resp)
            return resp

    class _ListMetadataStores(MetadataServiceRestStub):
        def __hash__(self):
            return hash("ListMetadataStores")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: metadata_service.ListMetadataStoresRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> metadata_service.ListMetadataStoresResponse:
            r"""Call the list metadata stores method over HTTP.

            Args:
                request (~.metadata_service.ListMetadataStoresRequest):
                    The request object. Request message for
                [MetadataService.ListMetadataStores][google.cloud.aiplatform.v1beta1.MetadataService.ListMetadataStores].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.metadata_service.ListMetadataStoresResponse:
                    Response message for
                [MetadataService.ListMetadataStores][google.cloud.aiplatform.v1beta1.MetadataService.ListMetadataStores].

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1beta1/{parent=projects/*/locations/*}/metadataStores",
                },
            ]
            request, metadata = self._interceptor.pre_list_metadata_stores(
                request, metadata
            )
            pb_request = metadata_service.ListMetadataStoresRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    use_integers_for_enums=False,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = metadata_service.ListMetadataStoresResponse()
            pb_resp = metadata_service.ListMetadataStoresResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_list_metadata_stores(resp)
            return resp

    class _PurgeArtifacts(MetadataServiceRestStub):
        def __hash__(self):
            return hash("PurgeArtifacts")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: metadata_service.PurgeArtifactsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the purge artifacts method over HTTP.

            Args:
                request (~.metadata_service.PurgeArtifactsRequest):
                    The request object. Request message for
                [MetadataService.PurgeArtifacts][google.cloud.aiplatform.v1beta1.MetadataService.PurgeArtifacts].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1beta1/{parent=projects/*/locations/*/metadataStores/*}/artifacts:purge",
                    "body": "*",
                },
            ]
            request, metadata = self._interceptor.pre_purge_artifacts(request, metadata)
            pb_request = metadata_service.PurgeArtifactsRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request["body"], use_integers_for_enums=False
            )
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    use_integers_for_enums=False,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_purge_artifacts(resp)
            return resp

    class _PurgeContexts(MetadataServiceRestStub):
        def __hash__(self):
            return hash("PurgeContexts")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: metadata_service.PurgeContextsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the purge contexts method over HTTP.

            Args:
                request (~.metadata_service.PurgeContextsRequest):
                    The request object. Request message for
                [MetadataService.PurgeContexts][google.cloud.aiplatform.v1beta1.MetadataService.PurgeContexts].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1beta1/{parent=projects/*/locations/*/metadataStores/*}/contexts:purge",
                    "body": "*",
                },
            ]
            request, metadata = self._interceptor.pre_purge_contexts(request, metadata)
            pb_request = metadata_service.PurgeContextsRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request["body"], use_integers_for_enums=False
            )
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    use_integers_for_enums=False,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_purge_contexts(resp)
            return resp

    class _PurgeExecutions(MetadataServiceRestStub):
        def __hash__(self):
            return hash("PurgeExecutions")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: metadata_service.PurgeExecutionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the purge executions method over HTTP.

            Args:
                request (~.metadata_service.PurgeExecutionsRequest):
                    The request object. Request message for
                [MetadataService.PurgeExecutions][google.cloud.aiplatform.v1beta1.MetadataService.PurgeExecutions].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1beta1/{parent=projects/*/locations/*/metadataStores/*}/executions:purge",
                    "body": "*",
                },
            ]
            request, metadata = self._interceptor.pre_purge_executions(
                request, metadata
            )
            pb_request = metadata_service.PurgeExecutionsRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request["body"], use_integers_for_enums=False
            )
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    use_integers_for_enums=False,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_purge_executions(resp)
            return resp

    class _QueryArtifactLineageSubgraph(MetadataServiceRestStub):
        def __hash__(self):
            return hash("QueryArtifactLineageSubgraph")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: metadata_service.QueryArtifactLineageSubgraphRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> lineage_subgraph.LineageSubgraph:
            r"""Call the query artifact lineage
            subgraph method over HTTP.

                Args:
                    request (~.metadata_service.QueryArtifactLineageSubgraphRequest):
                        The request object. Request message for
                    [MetadataService.QueryArtifactLineageSubgraph][google.cloud.aiplatform.v1beta1.MetadataService.QueryArtifactLineageSubgraph].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, str]]): Strings which should be
                        sent along with the request as metadata.

                Returns:
                    ~.lineage_subgraph.LineageSubgraph:
                        A subgraph of the overall lineage
                    graph. Event edges connect Artifact and
                    Execution nodes.

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1beta1/{artifact=projects/*/locations/*/metadataStores/*/artifacts/*}:queryArtifactLineageSubgraph",
                },
            ]
            request, metadata = self._interceptor.pre_query_artifact_lineage_subgraph(
                request, metadata
            )
            pb_request = metadata_service.QueryArtifactLineageSubgraphRequest.pb(
                request
            )
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    use_integers_for_enums=False,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = lineage_subgraph.LineageSubgraph()
            pb_resp = lineage_subgraph.LineageSubgraph.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_query_artifact_lineage_subgraph(resp)
            return resp

    class _QueryContextLineageSubgraph(MetadataServiceRestStub):
        def __hash__(self):
            return hash("QueryContextLineageSubgraph")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: metadata_service.QueryContextLineageSubgraphRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> lineage_subgraph.LineageSubgraph:
            r"""Call the query context lineage
            subgraph method over HTTP.

                Args:
                    request (~.metadata_service.QueryContextLineageSubgraphRequest):
                        The request object. Request message for
                    [MetadataService.QueryContextLineageSubgraph][google.cloud.aiplatform.v1beta1.MetadataService.QueryContextLineageSubgraph].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, str]]): Strings which should be
                        sent along with the request as metadata.

                Returns:
                    ~.lineage_subgraph.LineageSubgraph:
                        A subgraph of the overall lineage
                    graph. Event edges connect Artifact and
                    Execution nodes.

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1beta1/{context=projects/*/locations/*/metadataStores/*/contexts/*}:queryContextLineageSubgraph",
                },
            ]
            request, metadata = self._interceptor.pre_query_context_lineage_subgraph(
                request, metadata
            )
            pb_request = metadata_service.QueryContextLineageSubgraphRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    use_integers_for_enums=False,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = lineage_subgraph.LineageSubgraph()
            pb_resp = lineage_subgraph.LineageSubgraph.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_query_context_lineage_subgraph(resp)
            return resp

    class _QueryExecutionInputsAndOutputs(MetadataServiceRestStub):
        def __hash__(self):
            return hash("QueryExecutionInputsAndOutputs")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: metadata_service.QueryExecutionInputsAndOutputsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> lineage_subgraph.LineageSubgraph:
            r"""Call the query execution inputs
            and outputs method over HTTP.

                Args:
                    request (~.metadata_service.QueryExecutionInputsAndOutputsRequest):
                        The request object. Request message for
                    [MetadataService.QueryExecutionInputsAndOutputs][google.cloud.aiplatform.v1beta1.MetadataService.QueryExecutionInputsAndOutputs].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, str]]): Strings which should be
                        sent along with the request as metadata.

                Returns:
                    ~.lineage_subgraph.LineageSubgraph:
                        A subgraph of the overall lineage
                    graph. Event edges connect Artifact and
                    Execution nodes.

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1beta1/{execution=projects/*/locations/*/metadataStores/*/executions/*}:queryExecutionInputsAndOutputs",
                },
            ]
            (
                request,
                metadata,
            ) = self._interceptor.pre_query_execution_inputs_and_outputs(
                request, metadata
            )
            pb_request = metadata_service.QueryExecutionInputsAndOutputsRequest.pb(
                request
            )
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    use_integers_for_enums=False,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = lineage_subgraph.LineageSubgraph()
            pb_resp = lineage_subgraph.LineageSubgraph.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_query_execution_inputs_and_outputs(resp)
            return resp

    class _RemoveContextChildren(MetadataServiceRestStub):
        def __hash__(self):
            return hash("RemoveContextChildren")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: metadata_service.RemoveContextChildrenRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> metadata_service.RemoveContextChildrenResponse:
            r"""Call the remove context children method over HTTP.

            Args:
                request (~.metadata_service.RemoveContextChildrenRequest):
                    The request object. Request message for
                [MetadataService.DeleteContextChildrenRequest][].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.metadata_service.RemoveContextChildrenResponse:
                    Response message for
                [MetadataService.RemoveContextChildren][google.cloud.aiplatform.v1beta1.MetadataService.RemoveContextChildren].

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1beta1/{context=projects/*/locations/*/metadataStores/*/contexts/*}:removeContextChildren",
                    "body": "*",
                },
            ]
            request, metadata = self._interceptor.pre_remove_context_children(
                request, metadata
            )
            pb_request = metadata_service.RemoveContextChildrenRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request["body"], use_integers_for_enums=False
            )
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    use_integers_for_enums=False,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = metadata_service.RemoveContextChildrenResponse()
            pb_resp = metadata_service.RemoveContextChildrenResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_remove_context_children(resp)
            return resp

    class _UpdateArtifact(MetadataServiceRestStub):
        def __hash__(self):
            return hash("UpdateArtifact")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: metadata_service.UpdateArtifactRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> gca_artifact.Artifact:
            r"""Call the update artifact method over HTTP.

            Args:
                request (~.metadata_service.UpdateArtifactRequest):
                    The request object. Request message for
                [MetadataService.UpdateArtifact][google.cloud.aiplatform.v1beta1.MetadataService.UpdateArtifact].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.gca_artifact.Artifact:
                    Instance of a general artifact.
            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "patch",
                    "uri": "/v1beta1/{artifact.name=projects/*/locations/*/metadataStores/*/artifacts/*}",
                    "body": "artifact",
                },
            ]
            request, metadata = self._interceptor.pre_update_artifact(request, metadata)
            pb_request = metadata_service.UpdateArtifactRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request["body"], use_integers_for_enums=False
            )
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    use_integers_for_enums=False,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = gca_artifact.Artifact()
            pb_resp = gca_artifact.Artifact.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_update_artifact(resp)
            return resp

    class _UpdateContext(MetadataServiceRestStub):
        def __hash__(self):
            return hash("UpdateContext")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: metadata_service.UpdateContextRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> gca_context.Context:
            r"""Call the update context method over HTTP.

            Args:
                request (~.metadata_service.UpdateContextRequest):
                    The request object. Request message for
                [MetadataService.UpdateContext][google.cloud.aiplatform.v1beta1.MetadataService.UpdateContext].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.gca_context.Context:
                    Instance of a general context.
            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "patch",
                    "uri": "/v1beta1/{context.name=projects/*/locations/*/metadataStores/*/contexts/*}",
                    "body": "context",
                },
            ]
            request, metadata = self._interceptor.pre_update_context(request, metadata)
            pb_request = metadata_service.UpdateContextRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request["body"], use_integers_for_enums=False
            )
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    use_integers_for_enums=False,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = gca_context.Context()
            pb_resp = gca_context.Context.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_update_context(resp)
            return resp

    class _UpdateExecution(MetadataServiceRestStub):
        def __hash__(self):
            return hash("UpdateExecution")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: metadata_service.UpdateExecutionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> gca_execution.Execution:
            r"""Call the update execution method over HTTP.

            Args:
                request (~.metadata_service.UpdateExecutionRequest):
                    The request object. Request message for
                [MetadataService.UpdateExecution][google.cloud.aiplatform.v1beta1.MetadataService.UpdateExecution].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.gca_execution.Execution:
                    Instance of a general execution.
            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "patch",
                    "uri": "/v1beta1/{execution.name=projects/*/locations/*/metadataStores/*/executions/*}",
                    "body": "execution",
                },
            ]
            request, metadata = self._interceptor.pre_update_execution(
                request, metadata
            )
            pb_request = metadata_service.UpdateExecutionRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request["body"], use_integers_for_enums=False
            )
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    use_integers_for_enums=False,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = gca_execution.Execution()
            pb_resp = gca_execution.Execution.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_update_execution(resp)
            return resp

    @property
    def add_context_artifacts_and_executions(
        self,
    ) -> Callable[
        [metadata_service.AddContextArtifactsAndExecutionsRequest],
        metadata_service.AddContextArtifactsAndExecutionsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._AddContextArtifactsAndExecutions(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def add_context_children(
        self,
    ) -> Callable[
        [metadata_service.AddContextChildrenRequest],
        metadata_service.AddContextChildrenResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._AddContextChildren(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def add_execution_events(
        self,
    ) -> Callable[
        [metadata_service.AddExecutionEventsRequest],
        metadata_service.AddExecutionEventsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._AddExecutionEvents(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_artifact(
        self,
    ) -> Callable[[metadata_service.CreateArtifactRequest], gca_artifact.Artifact]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateArtifact(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_context(
        self,
    ) -> Callable[[metadata_service.CreateContextRequest], gca_context.Context]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateContext(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_execution(
        self,
    ) -> Callable[[metadata_service.CreateExecutionRequest], gca_execution.Execution]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateExecution(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_metadata_schema(
        self,
    ) -> Callable[
        [metadata_service.CreateMetadataSchemaRequest],
        gca_metadata_schema.MetadataSchema,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateMetadataSchema(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_metadata_store(
        self,
    ) -> Callable[
        [metadata_service.CreateMetadataStoreRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateMetadataStore(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_artifact(
        self,
    ) -> Callable[[metadata_service.DeleteArtifactRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteArtifact(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_context(
        self,
    ) -> Callable[[metadata_service.DeleteContextRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteContext(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_execution(
        self,
    ) -> Callable[[metadata_service.DeleteExecutionRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteExecution(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_metadata_store(
        self,
    ) -> Callable[
        [metadata_service.DeleteMetadataStoreRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteMetadataStore(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_artifact(
        self,
    ) -> Callable[[metadata_service.GetArtifactRequest], artifact.Artifact]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetArtifact(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_context(
        self,
    ) -> Callable[[metadata_service.GetContextRequest], context.Context]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetContext(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_execution(
        self,
    ) -> Callable[[metadata_service.GetExecutionRequest], execution.Execution]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetExecution(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_metadata_schema(
        self,
    ) -> Callable[
        [metadata_service.GetMetadataSchemaRequest], metadata_schema.MetadataSchema
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetMetadataSchema(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_metadata_store(
        self,
    ) -> Callable[
        [metadata_service.GetMetadataStoreRequest], metadata_store.MetadataStore
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetMetadataStore(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_artifacts(
        self,
    ) -> Callable[
        [metadata_service.ListArtifactsRequest], metadata_service.ListArtifactsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListArtifacts(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_contexts(
        self,
    ) -> Callable[
        [metadata_service.ListContextsRequest], metadata_service.ListContextsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListContexts(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_executions(
        self,
    ) -> Callable[
        [metadata_service.ListExecutionsRequest],
        metadata_service.ListExecutionsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListExecutions(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_metadata_schemas(
        self,
    ) -> Callable[
        [metadata_service.ListMetadataSchemasRequest],
        metadata_service.ListMetadataSchemasResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListMetadataSchemas(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_metadata_stores(
        self,
    ) -> Callable[
        [metadata_service.ListMetadataStoresRequest],
        metadata_service.ListMetadataStoresResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListMetadataStores(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def purge_artifacts(
        self,
    ) -> Callable[[metadata_service.PurgeArtifactsRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._PurgeArtifacts(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def purge_contexts(
        self,
    ) -> Callable[[metadata_service.PurgeContextsRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._PurgeContexts(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def purge_executions(
        self,
    ) -> Callable[[metadata_service.PurgeExecutionsRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._PurgeExecutions(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def query_artifact_lineage_subgraph(
        self,
    ) -> Callable[
        [metadata_service.QueryArtifactLineageSubgraphRequest],
        lineage_subgraph.LineageSubgraph,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._QueryArtifactLineageSubgraph(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def query_context_lineage_subgraph(
        self,
    ) -> Callable[
        [metadata_service.QueryContextLineageSubgraphRequest],
        lineage_subgraph.LineageSubgraph,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._QueryContextLineageSubgraph(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def query_execution_inputs_and_outputs(
        self,
    ) -> Callable[
        [metadata_service.QueryExecutionInputsAndOutputsRequest],
        lineage_subgraph.LineageSubgraph,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._QueryExecutionInputsAndOutputs(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def remove_context_children(
        self,
    ) -> Callable[
        [metadata_service.RemoveContextChildrenRequest],
        metadata_service.RemoveContextChildrenResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RemoveContextChildren(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_artifact(
        self,
    ) -> Callable[[metadata_service.UpdateArtifactRequest], gca_artifact.Artifact]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateArtifact(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_context(
        self,
    ) -> Callable[[metadata_service.UpdateContextRequest], gca_context.Context]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateContext(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_execution(
        self,
    ) -> Callable[[metadata_service.UpdateExecutionRequest], gca_execution.Execution]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateExecution(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(MetadataServiceRestStub):
        def __call__(
            self,
            request: locations_pb2.GetLocationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> locations_pb2.Location:

            r"""Call the get location method over HTTP.

            Args:
                request (locations_pb2.GetLocationRequest):
                    The request object for GetLocation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                locations_pb2.Location: Response from GetLocation method.
            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*}",
                },
            ]

            request, metadata = self._interceptor.pre_get_location(request, metadata)
            request_kwargs = json_format.MessageToDict(request)
            transcoded_request = path_template.transcode(http_options, **request_kwargs)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(json.dumps(transcoded_request["query_params"]))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"

            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            resp = locations_pb2.Location()
            resp = json_format.Parse(response.content.decode("utf-8"), resp)
            resp = self._interceptor.post_get_location(resp)
            return resp

    @property
    def list_locations(self):
        return self._ListLocations(self._session, self._host, self._interceptor)  # type: ignore

    class _ListLocations(MetadataServiceRestStub):
        def __call__(
            self,
            request: locations_pb2.ListLocationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> locations_pb2.ListLocationsResponse:

            r"""Call the list locations method over HTTP.

            Args:
                request (locations_pb2.ListLocationsRequest):
                    The request object for ListLocations method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                locations_pb2.ListLocationsResponse: Response from ListLocations method.
            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*}/locations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*}/locations",
                },
            ]

            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            request_kwargs = json_format.MessageToDict(request)
            transcoded_request = path_template.transcode(http_options, **request_kwargs)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(json.dumps(transcoded_request["query_params"]))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"

            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            resp = locations_pb2.ListLocationsResponse()
            resp = json_format.Parse(response.content.decode("utf-8"), resp)
            resp = self._interceptor.post_list_locations(resp)
            return resp

    @property
    def get_iam_policy(self):
        return self._GetIamPolicy(self._session, self._host, self._interceptor)  # type: ignore

    class _GetIamPolicy(MetadataServiceRestStub):
        def __call__(
            self,
            request: iam_policy_pb2.GetIamPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> policy_pb2.Policy:

            r"""Call the get iam policy method over HTTP.

            Args:
                request (iam_policy_pb2.GetIamPolicyRequest):
                    The request object for GetIamPolicy method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                policy_pb2.Policy: Response from GetIamPolicy method.
            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1beta1/{resource=projects/*/locations/*/featurestores/*}:getIamPolicy",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{resource=projects/*/locations/*/featurestores/*/entityTypes/*}:getIamPolicy",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{resource=projects/*/locations/*/models/*}:getIamPolicy",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{resource=projects/*/locations/*/endpoints/*}:getIamPolicy",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{resource=projects/*/locations/*/notebookRuntimeTemplates/*}:getIamPolicy",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{resource=projects/*/locations/*/publishers/*/models/*}:getIamPolicy",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{resource=projects/*/locations/*/featureOnlineStores/*}:getIamPolicy",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{resource=projects/*/locations/*/featureOnlineStores/*/featureViews/*}:getIamPolicy",
                },
                {
                    "method": "post",
                    "uri": "/ui/{resource=projects/*/locations/*/featurestores/*}:getIamPolicy",
                },
                {
                    "method": "post",
                    "uri": "/ui/{resource=projects/*/locations/*/featurestores/*/entityTypes/*}:getIamPolicy",
                },
                {
                    "method": "post",
                    "uri": "/ui/{resource=projects/*/locations/*/models/*}:getIamPolicy",
                },
                {
                    "method": "post",
                    "uri": "/ui/{resource=projects/*/locations/*/endpoints/*}:getIamPolicy",
                },
                {
                    "method": "post",
                    "uri": "/ui/{resource=projects/*/locations/*/notebookRuntimeTemplates/*}:getIamPolicy",
                },
                {
                    "method": "post",
                    "uri": "/ui/{resource=projects/*/locations/*/publishers/*/models/*}:getIamPolicy",
                },
                {
                    "method": "post",
                    "uri": "/ui/{resource=projects/*/locations/*/featureOnlineStores/*}:getIamPolicy",
                },
                {
                    "method": "post",
                    "uri": "/ui/{resource=projects/*/locations/*/featureOnlineStores/*/featureViews/*}:getIamPolicy",
                },
            ]

            request, metadata = self._interceptor.pre_get_iam_policy(request, metadata)
            request_kwargs = json_format.MessageToDict(request)
            transcoded_request = path_template.transcode(http_options, **request_kwargs)

            body = json.dumps(transcoded_request["body"])
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(json.dumps(transcoded_request["query_params"]))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"

            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params),
                data=body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            resp = policy_pb2.Policy()
            resp = json_format.Parse(response.content.decode("utf-8"), resp)
            resp = self._interceptor.post_get_iam_policy(resp)
            return resp

    @property
    def set_iam_policy(self):
        return self._SetIamPolicy(self._session, self._host, self._interceptor)  # type: ignore

    class _SetIamPolicy(MetadataServiceRestStub):
        def __call__(
            self,
            request: iam_policy_pb2.SetIamPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> policy_pb2.Policy:

            r"""Call the set iam policy method over HTTP.

            Args:
                request (iam_policy_pb2.SetIamPolicyRequest):
                    The request object for SetIamPolicy method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                policy_pb2.Policy: Response from SetIamPolicy method.
            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1beta1/{resource=projects/*/locations/*/featurestores/*}:setIamPolicy",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{resource=projects/*/locations/*/featurestores/*/entityTypes/*}:setIamPolicy",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{resource=projects/*/locations/*/models/*}:setIamPolicy",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{resource=projects/*/locations/*/endpoints/*}:setIamPolicy",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{resource=projects/*/locations/*/notebookRuntimeTemplates/*}:setIamPolicy",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{resource=projects/*/locations/*/featureOnlineStores/*}:setIamPolicy",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{resource=projects/*/locations/*/featureOnlineStores/*/featureViews/*}:setIamPolicy",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/ui/{resource=projects/*/locations/*/featurestores/*}:setIamPolicy",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/ui/{resource=projects/*/locations/*/featurestores/*/entityTypes/*}:setIamPolicy",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/ui/{resource=projects/*/locations/*/models/*}:setIamPolicy",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/ui/{resource=projects/*/locations/*/endpoints/*}:setIamPolicy",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/ui/{resource=projects/*/locations/*/notebookRuntimeTemplates/*}:setIamPolicy",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/ui/{resource=projects/*/locations/*/featureOnlineStores/*}:setIamPolicy",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/ui/{resource=projects/*/locations/*/featureOnlineStores/*/featureViews/*}:setIamPolicy",
                    "body": "*",
                },
            ]

            request, metadata = self._interceptor.pre_set_iam_policy(request, metadata)
            request_kwargs = json_format.MessageToDict(request)
            transcoded_request = path_template.transcode(http_options, **request_kwargs)

            body = json.dumps(transcoded_request["body"])
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(json.dumps(transcoded_request["query_params"]))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"

            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params),
                data=body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            resp = policy_pb2.Policy()
            resp = json_format.Parse(response.content.decode("utf-8"), resp)
            resp = self._interceptor.post_set_iam_policy(resp)
            return resp

    @property
    def test_iam_permissions(self):
        return self._TestIamPermissions(self._session, self._host, self._interceptor)  # type: ignore

    class _TestIamPermissions(MetadataServiceRestStub):
        def __call__(
            self,
            request: iam_policy_pb2.TestIamPermissionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> iam_policy_pb2.TestIamPermissionsResponse:

            r"""Call the test iam permissions method over HTTP.

            Args:
                request (iam_policy_pb2.TestIamPermissionsRequest):
                    The request object for TestIamPermissions method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                iam_policy_pb2.TestIamPermissionsResponse: Response from TestIamPermissions method.
            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1beta1/{resource=projects/*/locations/*/featurestores/*}:testIamPermissions",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{resource=projects/*/locations/*/featurestores/*/entityTypes/*}:testIamPermissions",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{resource=projects/*/locations/*/models/*}:testIamPermissions",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{resource=projects/*/locations/*/endpoints/*}:testIamPermissions",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{resource=projects/*/locations/*/notebookRuntimeTemplates/*}:testIamPermissions",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{resource=projects/*/locations/*/featureOnlineStores/*}:testIamPermissions",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{resource=projects/*/locations/*/featureOnlineStores/*/featureViews/*}:testIamPermissions",
                },
                {
                    "method": "post",
                    "uri": "/ui/{resource=projects/*/locations/*/featurestores/*}:testIamPermissions",
                },
                {
                    "method": "post",
                    "uri": "/ui/{resource=projects/*/locations/*/featurestores/*/entityTypes/*}:testIamPermissions",
                },
                {
                    "method": "post",
                    "uri": "/ui/{resource=projects/*/locations/*/models/*}:testIamPermissions",
                },
                {
                    "method": "post",
                    "uri": "/ui/{resource=projects/*/locations/*/endpoints/*}:testIamPermissions",
                },
                {
                    "method": "post",
                    "uri": "/ui/{resource=projects/*/locations/*/notebookRuntimeTemplates/*}:testIamPermissions",
                },
                {
                    "method": "post",
                    "uri": "/ui/{resource=projects/*/locations/*/featureOnlineStores/*}:testIamPermissions",
                },
                {
                    "method": "post",
                    "uri": "/ui/{resource=projects/*/locations/*/featureOnlineStores/*/featureViews/*}:testIamPermissions",
                },
            ]

            request, metadata = self._interceptor.pre_test_iam_permissions(
                request, metadata
            )
            request_kwargs = json_format.MessageToDict(request)
            transcoded_request = path_template.transcode(http_options, **request_kwargs)

            body = json.dumps(transcoded_request["body"])
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(json.dumps(transcoded_request["query_params"]))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"

            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params),
                data=body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            resp = iam_policy_pb2.TestIamPermissionsResponse()
            resp = json_format.Parse(response.content.decode("utf-8"), resp)
            resp = self._interceptor.post_test_iam_permissions(resp)
            return resp

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(MetadataServiceRestStub):
        def __call__(
            self,
            request: operations_pb2.CancelOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> None:

            r"""Call the cancel operation method over HTTP.

            Args:
                request (operations_pb2.CancelOperationRequest):
                    The request object for CancelOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.
            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/datasets/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/datasets/*/dataItems/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/datasets/*/savedQueries/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/datasets/*/annotationSpecs/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/datasets/*/dataItems/*/annotations/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/deploymentResourcePools/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/edgeDevices/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/endpoints/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/extensionControllers/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/extensions/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/featurestores/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/featurestores/*/entityTypes/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/featurestores/*/entityTypes/*/features/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/customJobs/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/dataLabelingJobs/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/hyperparameterTuningJobs/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/tuningJobs/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/indexes/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/indexEndpoints/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/artifacts/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/contexts/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/executions/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/modelMonitors/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/migratableResources/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/models/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/models/*/evaluations/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/persistentResources/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/studies/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/studies/*/trials/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/trainingPipelines/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/pipelineJobs/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/schedules/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/specialistPools/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/timeSeries/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/dataItems/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/savedQueries/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/annotationSpecs/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/dataItems/*/annotations/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/deploymentResourcePools/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/edgeDevices/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/endpoints/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/exampleStores/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/extensionControllers/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/extensions/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/entityTypes/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/entityTypes/*/features/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/customJobs/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/dataLabelingJobs/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/hyperparameterTuningJobs/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/indexes/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/indexEndpoints/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/artifacts/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/contexts/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/executions/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/modelMonitors/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/migratableResources/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/models/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/models/*/evaluations/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/persistentResources/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/ragCorpora/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/ragCorpora/*/ragFiles/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/studies/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/studies/*/trials/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/trainingPipelines/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/pipelineJobs/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/reasoningEngines/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/schedules/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/specialistPools/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/timeSeries/*/operations/*}:cancel",
                },
            ]

            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            request_kwargs = json_format.MessageToDict(request)
            transcoded_request = path_template.transcode(http_options, **request_kwargs)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(json.dumps(transcoded_request["query_params"]))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"

            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            return self._interceptor.post_cancel_operation(None)

    @property
    def delete_operation(self):
        return self._DeleteOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _DeleteOperation(MetadataServiceRestStub):
        def __call__(
            self,
            request: operations_pb2.DeleteOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> None:

            r"""Call the delete operation method over HTTP.

            Args:
                request (operations_pb2.DeleteOperationRequest):
                    The request object for DeleteOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.
            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/datasets/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/datasets/*/dataItems/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/datasets/*/savedQueries/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/datasets/*/annotationSpecs/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/datasets/*/dataItems/*/annotations/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/deploymentResourcePools/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/edgeDevices/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/endpoints/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/extensionControllers/*}/operations",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/extensions/*}/operations",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/featurestores/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/featurestores/*/entityTypes/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/featurestores/*/entityTypes/*/features/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/customJobs/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/dataLabelingJobs/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/hyperparameterTuningJobs/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/indexes/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/indexEndpoints/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/artifacts/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/contexts/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/executions/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/modelMonitors/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/migratableResources/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/models/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/models/*/evaluations/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/persistentResources/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/studies/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/studies/*/trials/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/trainingPipelines/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/pipelineJobs/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/schedules/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/specialistPools/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/timeSeries/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/featureOnlineStores/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/featureGroups/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/featureGroups/*/features/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/featureOnlineStores/*/featureViews/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/dataItems/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/savedQueries/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/annotationSpecs/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/dataItems/*/annotations/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/deploymentResourcePools/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/edgeDevices/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/endpoints/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/entityTypes/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/entityTypes/*/features/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/customJobs/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/dataLabelingJobs/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/evaluationTasks/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/exampleStores/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/extensionControllers/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/extensions/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/hyperparameterTuningJobs/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/indexes/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/indexEndpoints/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/artifacts/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/contexts/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/executions/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/modelMonitors/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/migratableResources/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/models/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/models/*/evaluations/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/persistentResources/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/ragCorpora/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/ragCorpora/*/ragFiles/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/reasoningEngines/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/solvers/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/studies/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/studies/*/trials/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/trainingPipelines/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/pipelineJobs/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/schedules/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/specialistPools/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/timeSeries/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featureOnlineStores/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featureGroups/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featureGroups/*/features/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featureOnlineStores/*/featureViews/*/operations/*}",
                },
            ]

            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            request_kwargs = json_format.MessageToDict(request)
            transcoded_request = path_template.transcode(http_options, **request_kwargs)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(json.dumps(transcoded_request["query_params"]))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"

            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            return self._interceptor.post_delete_operation(None)

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(MetadataServiceRestStub):
        def __call__(
            self,
            request: operations_pb2.GetOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> operations_pb2.Operation:

            r"""Call the get operation method over HTTP.

            Args:
                request (operations_pb2.GetOperationRequest):
                    The request object for GetOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                operations_pb2.Operation: Response from GetOperation method.
            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/datasets/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/datasets/*/dataItems/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/datasets/*/savedQueries/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/datasets/*/annotationSpecs/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/datasets/*/dataItems/*/annotations/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/deploymentResourcePools/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/edgeDeploymentJobs/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/edgeDevices/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/endpoints/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/extensionControllers/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/extensions/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/featurestores/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/featurestores/*/entityTypes/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/featurestores/*/entityTypes/*/features/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/customJobs/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/dataLabelingJobs/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/hyperparameterTuningJobs/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/tuningJobs/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/indexes/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/indexEndpoints/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/artifacts/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/contexts/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/executions/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/modelMonitors/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/migratableResources/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/models/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/models/*/evaluations/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/persistentResources/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/studies/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/studies/*/trials/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/trainingPipelines/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/pipelineJobs/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/schedules/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/specialistPools/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/timeSeries/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/featureOnlineStores/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/featureOnlineStores/*/featureViews/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/featureGroups/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/featureGroups/*/features/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/dataItems/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/savedQueries/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/annotationSpecs/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/dataItems/*/annotations/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/deploymentResourcePools/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/edgeDevices/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/endpoints/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/evaluationTasks/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/exampleStores/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/extensionControllers/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/extensions/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/entityTypes/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/entityTypes/*/features/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/customJobs/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/dataLabelingJobs/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/hyperparameterTuningJobs/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/indexes/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/indexEndpoints/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/artifacts/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/contexts/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/executions/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/modelMonitors/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/migratableResources/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/models/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/models/*/evaluations/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/persistentResources/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/ragCorpora/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/ragCorpora/*/ragFiles/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/reasoningEngines/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/solvers/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/studies/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/studies/*/trials/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/trainingPipelines/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/pipelineJobs/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/schedules/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/specialistPools/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/timeSeries/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featureOnlineStores/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featureOnlineStores/*/featureViews/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featureGroups/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featureGroups/*/features/*/operations/*}",
                },
            ]

            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            request_kwargs = json_format.MessageToDict(request)
            transcoded_request = path_template.transcode(http_options, **request_kwargs)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(json.dumps(transcoded_request["query_params"]))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"

            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            resp = operations_pb2.Operation()
            resp = json_format.Parse(response.content.decode("utf-8"), resp)
            resp = self._interceptor.post_get_operation(resp)
            return resp

    @property
    def list_operations(self):
        return self._ListOperations(self._session, self._host, self._interceptor)  # type: ignore

    class _ListOperations(MetadataServiceRestStub):
        def __call__(
            self,
            request: operations_pb2.ListOperationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> operations_pb2.ListOperationsResponse:

            r"""Call the list operations method over HTTP.

            Args:
                request (operations_pb2.ListOperationsRequest):
                    The request object for ListOperations method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                operations_pb2.ListOperationsResponse: Response from ListOperations method.
            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/datasets/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/datasets/*/dataItems/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/datasets/*/savedQueries/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/datasets/*/annotationSpecs/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/datasets/*/dataItems/*/annotations/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/deploymentResourcePools/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/edgeDevices/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/endpoints/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/extensionControllers/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/extensions/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/featurestores/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/featurestores/*/entityTypes/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/featurestores/*/entityTypes/*/features/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/customJobs/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/dataLabelingJobs/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/hyperparameterTuningJobs/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/tuningJobs/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/indexes/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/indexEndpoints/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/metadataStores/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/artifacts/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/contexts/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/executions/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/modelMonitors/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/migratableResources/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/models/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/models/*/evaluations/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/studies/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/studies/*/trials/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/trainingPipelines/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/persistentResources/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/pipelineJobs/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/schedules/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/specialistPools/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/tensorboards/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/timeSeries/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/featureOnlineStores/*/operations/*}:wait",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/featureOnlineStores/*/featureViews/*/operations/*}:wait",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/featureGroups/*/operations/*}:wait",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/featureGroups/*/features/*/operations/*}:wait",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/dataItems/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/savedQueries/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/annotationSpecs/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/dataItems/*/annotations/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/deploymentResourcePools/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/edgeDevices/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/endpoints/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/evaluationTasks/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/exampleStores/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/extensionControllers/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/extensions/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/entityTypes/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/entityTypes/*/features/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/customJobs/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/dataLabelingJobs/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/hyperparameterTuningJobs/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/indexes/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/indexEndpoints/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/artifacts/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/contexts/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/executions/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/modelMonitors/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/migratableResources/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/models/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/models/*/evaluations/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/persistentResources/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/ragCorpora/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/ragCorpora/*/ragFiles/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/reasoningEngines/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/solvers/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/studies/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/studies/*/trials/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/trainingPipelines/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/pipelineJobs/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/schedules/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/specialistPools/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/timeSeries/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featureOnlineStores/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featureOnlineStores/*/featureViews/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featureGroups/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featureGroups/*/features/*}/operations",
                },
            ]

            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            request_kwargs = json_format.MessageToDict(request)
            transcoded_request = path_template.transcode(http_options, **request_kwargs)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(json.dumps(transcoded_request["query_params"]))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"

            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            resp = operations_pb2.ListOperationsResponse()
            resp = json_format.Parse(response.content.decode("utf-8"), resp)
            resp = self._interceptor.post_list_operations(resp)
            return resp

    @property
    def wait_operation(self):
        return self._WaitOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _WaitOperation(MetadataServiceRestStub):
        def __call__(
            self,
            request: operations_pb2.WaitOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> operations_pb2.Operation:

            r"""Call the wait operation method over HTTP.

            Args:
                request (operations_pb2.WaitOperationRequest):
                    The request object for WaitOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                operations_pb2.Operation: Response from WaitOperation method.
            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/datasets/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/datasets/*/dataItems/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/datasets/*/savedQueries/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/datasets/*/annotationSpecs/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/datasets/*/dataItems/*/annotations/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/deploymentResourcePools/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/edgeDevices/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/endpoints/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/extensionControllers/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/extensions/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/featurestores/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/featurestores/*/entityTypes/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/featurestores/*/entityTypes/*/features/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/customJobs/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/dataLabelingJobs/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/hyperparameterTuningJobs/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/tuningJobs/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/indexes/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/indexEndpoints/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/artifacts/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/contexts/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/executions/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/modelMonitors/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/migratableResources/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/models/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/models/*/evaluations/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/studies/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/studies/*/trials/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/trainingPipelines/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/persistentResources/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/pipelineJobs/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/schedules/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/specialistPools/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/timeSeries/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/featureOnlineStores/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/featureOnlineStores/*/featureViews/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/featureGroups/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/featureGroups/*/features/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/dataItems/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/savedQueries/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/annotationSpecs/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/dataItems/*/annotations/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/deploymentResourcePools/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/edgeDevices/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/endpoints/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/evaluationTasks/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/exampleStores/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/extensionControllers/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/extensions/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/entityTypes/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/entityTypes/*/features/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/customJobs/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/dataLabelingJobs/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/hyperparameterTuningJobs/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/indexes/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/indexEndpoints/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/artifacts/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/contexts/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/executions/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/modelMonitors/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/migratableResources/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/models/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/models/*/evaluations/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/persistentResources/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/ragCorpora/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/ragCorpora/*/ragFiles/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/reasoningEngines/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/studies/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/studies/*/trials/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/trainingPipelines/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/pipelineJobs/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/schedules/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/specialistPools/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/timeSeries/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featureOnlineStores/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featureOnlineStores/*/featureViews/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featureGroups/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featureGroups/*/features/*/operations/*}:wait",
                },
            ]

            request, metadata = self._interceptor.pre_wait_operation(request, metadata)
            request_kwargs = json_format.MessageToDict(request)
            transcoded_request = path_template.transcode(http_options, **request_kwargs)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(json.dumps(transcoded_request["query_params"]))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"

            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            resp = operations_pb2.Operation()
            resp = json_format.Parse(response.content.decode("utf-8"), resp)
            resp = self._interceptor.post_wait_operation(resp)
            return resp

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("MetadataServiceRestTransport",)
