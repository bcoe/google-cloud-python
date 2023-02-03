# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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
from typing import Awaitable, Callable, Dict, Optional, Sequence, Tuple, Union
import warnings

from google.api_core import gapic_v1, grpc_helpers_async, operations_v1
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.iam.v1 import iam_policy_pb2  # type: ignore
from google.iam.v1 import policy_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
import grpc  # type: ignore
from grpc.experimental import aio  # type: ignore

from google.cloud.vmwareengine_v1.types import vmwareengine, vmwareengine_resources

from .base import DEFAULT_CLIENT_INFO, VmwareEngineTransport
from .grpc import VmwareEngineGrpcTransport


class VmwareEngineGrpcAsyncIOTransport(VmwareEngineTransport):
    """gRPC AsyncIO backend transport for VmwareEngine.

    VMwareEngine manages VMware's private clusters in the Cloud.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """

    _grpc_channel: aio.Channel
    _stubs: Dict[str, Callable] = {}

    @classmethod
    def create_channel(
        cls,
        host: str = "vmwareengine.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        **kwargs,
    ) -> aio.Channel:
        """Create and return a gRPC AsyncIO channel object.
        Args:
            host (Optional[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            aio.Channel: A gRPC AsyncIO channel object.
        """

        return grpc_helpers_async.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            quota_project_id=quota_project_id,
            default_scopes=cls.AUTH_SCOPES,
            scopes=scopes,
            default_host=cls.DEFAULT_HOST,
            **kwargs,
        )

    def __init__(
        self,
        *,
        host: str = "vmwareengine.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        channel: Optional[aio.Channel] = None,
        api_mtls_endpoint: Optional[str] = None,
        client_cert_source: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        ssl_channel_credentials: Optional[grpc.ChannelCredentials] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if ``channel`` is provided.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            channel (Optional[aio.Channel]): A ``Channel`` instance through
                which to make calls.
            api_mtls_endpoint (Optional[str]): Deprecated. The mutual TLS endpoint.
                If provided, it overrides the ``host`` argument and tries to create
                a mutual TLS channel with client SSL credentials from
                ``client_cert_source`` or application default SSL credentials.
            client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]):
                Deprecated. A callback to provide client SSL certificate bytes and
                private key bytes, both in PEM format. It is ignored if
                ``api_mtls_endpoint`` is None.
            ssl_channel_credentials (grpc.ChannelCredentials): SSL credentials
                for the grpc channel. It is ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Optional[Callable[[], Tuple[bytes, bytes]]]):
                A callback to provide client certificate bytes and private key bytes,
                both in PEM format. It is used to configure a mutual TLS channel. It is
                ignored if ``channel`` or ``ssl_channel_credentials`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        self._grpc_channel = None
        self._ssl_channel_credentials = ssl_channel_credentials
        self._stubs: Dict[str, Callable] = {}
        self._operations_client: Optional[operations_v1.OperationsAsyncClient] = None

        if api_mtls_endpoint:
            warnings.warn("api_mtls_endpoint is deprecated", DeprecationWarning)
        if client_cert_source:
            warnings.warn("client_cert_source is deprecated", DeprecationWarning)

        if channel:
            # Ignore credentials if a channel was passed.
            credentials = False
            # If a channel was explicitly provided, set it.
            self._grpc_channel = channel
            self._ssl_channel_credentials = None
        else:
            if api_mtls_endpoint:
                host = api_mtls_endpoint

                # Create SSL credentials with client_cert_source or application
                # default SSL credentials.
                if client_cert_source:
                    cert, key = client_cert_source()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )
                else:
                    self._ssl_channel_credentials = SslCredentials().ssl_credentials

            else:
                if client_cert_source_for_mtls and not ssl_channel_credentials:
                    cert, key = client_cert_source_for_mtls()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )

        # The base transport sets the host, credentials and scopes
        super().__init__(
            host=host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes,
            quota_project_id=quota_project_id,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            api_audience=api_audience,
        )

        if not self._grpc_channel:
            self._grpc_channel = type(self).create_channel(
                self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                # Set ``credentials_file`` to ``None`` here as
                # the credentials that we saved earlier should be used.
                credentials_file=None,
                scopes=self._scopes,
                ssl_credentials=self._ssl_channel_credentials,
                quota_project_id=quota_project_id,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )

        # Wrap messages. This must be done after self._grpc_channel exists
        self._prep_wrapped_messages(client_info)

    @property
    def grpc_channel(self) -> aio.Channel:
        """Create the channel designed to connect to this service.

        This property caches on the instance; repeated calls return
        the same channel.
        """
        # Return the channel from cache.
        return self._grpc_channel

    @property
    def operations_client(self) -> operations_v1.OperationsAsyncClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Quick check: Only create a new client if we do not already have one.
        if self._operations_client is None:
            self._operations_client = operations_v1.OperationsAsyncClient(
                self.grpc_channel
            )

        # Return the client from cache.
        return self._operations_client

    @property
    def list_private_clouds(
        self,
    ) -> Callable[
        [vmwareengine.ListPrivateCloudsRequest],
        Awaitable[vmwareengine.ListPrivateCloudsResponse],
    ]:
        r"""Return a callable for the list private clouds method over gRPC.

        Lists ``PrivateCloud`` resources in a given project and
        location.

        Returns:
            Callable[[~.ListPrivateCloudsRequest],
                    Awaitable[~.ListPrivateCloudsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_private_clouds" not in self._stubs:
            self._stubs["list_private_clouds"] = self.grpc_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/ListPrivateClouds",
                request_serializer=vmwareengine.ListPrivateCloudsRequest.serialize,
                response_deserializer=vmwareengine.ListPrivateCloudsResponse.deserialize,
            )
        return self._stubs["list_private_clouds"]

    @property
    def get_private_cloud(
        self,
    ) -> Callable[
        [vmwareengine.GetPrivateCloudRequest],
        Awaitable[vmwareengine_resources.PrivateCloud],
    ]:
        r"""Return a callable for the get private cloud method over gRPC.

        Retrieves a ``PrivateCloud`` resource by its resource name.

        Returns:
            Callable[[~.GetPrivateCloudRequest],
                    Awaitable[~.PrivateCloud]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_private_cloud" not in self._stubs:
            self._stubs["get_private_cloud"] = self.grpc_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/GetPrivateCloud",
                request_serializer=vmwareengine.GetPrivateCloudRequest.serialize,
                response_deserializer=vmwareengine_resources.PrivateCloud.deserialize,
            )
        return self._stubs["get_private_cloud"]

    @property
    def create_private_cloud(
        self,
    ) -> Callable[
        [vmwareengine.CreatePrivateCloudRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the create private cloud method over gRPC.

        Creates a new ``PrivateCloud`` resource in a given project and
        location. Private clouds can only be created in zones, regional
        private clouds are not supported.

        Creating a private cloud also creates a `management
        cluster <https://cloud.google.com/vmware-engine/docs/concepts-vmware-components>`__
        for that private cloud.

        Returns:
            Callable[[~.CreatePrivateCloudRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_private_cloud" not in self._stubs:
            self._stubs["create_private_cloud"] = self.grpc_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/CreatePrivateCloud",
                request_serializer=vmwareengine.CreatePrivateCloudRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_private_cloud"]

    @property
    def update_private_cloud(
        self,
    ) -> Callable[
        [vmwareengine.UpdatePrivateCloudRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the update private cloud method over gRPC.

        Modifies a ``PrivateCloud`` resource. Only the following fields
        can be updated: ``description``. Only fields specified in
        ``updateMask`` are applied.

        During operation processing, the resource is temporarily in the
        ``ACTIVE`` state before the operation fully completes. For that
        period of time, you can't update the resource. Use the operation
        status to determine when the processing fully completes.

        Returns:
            Callable[[~.UpdatePrivateCloudRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_private_cloud" not in self._stubs:
            self._stubs["update_private_cloud"] = self.grpc_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/UpdatePrivateCloud",
                request_serializer=vmwareengine.UpdatePrivateCloudRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_private_cloud"]

    @property
    def delete_private_cloud(
        self,
    ) -> Callable[
        [vmwareengine.DeletePrivateCloudRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the delete private cloud method over gRPC.

        Schedules a ``PrivateCloud`` resource for deletion.

        A ``PrivateCloud`` resource scheduled for deletion has
        ``PrivateCloud.state`` set to ``DELETED`` and ``expireTime`` set
        to the time when deletion is final and can no longer be
        reversed. The delete operation is marked as done as soon as the
        ``PrivateCloud`` is successfully scheduled for deletion (this
        also applies when ``delayHours`` is set to zero), and the
        operation is not kept in pending state until ``PrivateCloud`` is
        purged. ``PrivateCloud`` can be restored using
        ``UndeletePrivateCloud`` method before the ``expireTime``
        elapses. When ``expireTime`` is reached, deletion is final and
        all private cloud resources are irreversibly removed and billing
        stops. During the final removal process, ``PrivateCloud.state``
        is set to ``PURGING``. ``PrivateCloud`` can be polled using
        standard ``GET`` method for the whole period of deletion and
        purging. It will not be returned only when it is completely
        purged.

        Returns:
            Callable[[~.DeletePrivateCloudRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_private_cloud" not in self._stubs:
            self._stubs["delete_private_cloud"] = self.grpc_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/DeletePrivateCloud",
                request_serializer=vmwareengine.DeletePrivateCloudRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_private_cloud"]

    @property
    def undelete_private_cloud(
        self,
    ) -> Callable[
        [vmwareengine.UndeletePrivateCloudRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the undelete private cloud method over gRPC.

        Restores a private cloud that was previously scheduled for
        deletion by ``DeletePrivateCloud``. A ``PrivateCloud`` resource
        scheduled for deletion has ``PrivateCloud.state`` set to
        ``DELETED`` and ``PrivateCloud.expireTime`` set to the time when
        deletion can no longer be reversed.

        Returns:
            Callable[[~.UndeletePrivateCloudRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "undelete_private_cloud" not in self._stubs:
            self._stubs["undelete_private_cloud"] = self.grpc_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/UndeletePrivateCloud",
                request_serializer=vmwareengine.UndeletePrivateCloudRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["undelete_private_cloud"]

    @property
    def list_clusters(
        self,
    ) -> Callable[
        [vmwareengine.ListClustersRequest], Awaitable[vmwareengine.ListClustersResponse]
    ]:
        r"""Return a callable for the list clusters method over gRPC.

        Lists ``Cluster`` resources in a given private cloud.

        Returns:
            Callable[[~.ListClustersRequest],
                    Awaitable[~.ListClustersResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_clusters" not in self._stubs:
            self._stubs["list_clusters"] = self.grpc_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/ListClusters",
                request_serializer=vmwareengine.ListClustersRequest.serialize,
                response_deserializer=vmwareengine.ListClustersResponse.deserialize,
            )
        return self._stubs["list_clusters"]

    @property
    def get_cluster(
        self,
    ) -> Callable[
        [vmwareengine.GetClusterRequest], Awaitable[vmwareengine_resources.Cluster]
    ]:
        r"""Return a callable for the get cluster method over gRPC.

        Retrieves a ``Cluster`` resource by its resource name.

        Returns:
            Callable[[~.GetClusterRequest],
                    Awaitable[~.Cluster]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_cluster" not in self._stubs:
            self._stubs["get_cluster"] = self.grpc_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/GetCluster",
                request_serializer=vmwareengine.GetClusterRequest.serialize,
                response_deserializer=vmwareengine_resources.Cluster.deserialize,
            )
        return self._stubs["get_cluster"]

    @property
    def create_cluster(
        self,
    ) -> Callable[
        [vmwareengine.CreateClusterRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the create cluster method over gRPC.

        Creates a new cluster in a given private cloud. Creating a new
        cluster provides additional nodes for use in the parent private
        cloud and requires sufficient `node
        quota <https://cloud.google.com/vmware-engine/quotas>`__.

        Returns:
            Callable[[~.CreateClusterRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_cluster" not in self._stubs:
            self._stubs["create_cluster"] = self.grpc_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/CreateCluster",
                request_serializer=vmwareengine.CreateClusterRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_cluster"]

    @property
    def update_cluster(
        self,
    ) -> Callable[
        [vmwareengine.UpdateClusterRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the update cluster method over gRPC.

        Modifies a ``Cluster`` resource. Only the following fields can
        be updated: ``node_type_configs.*.node_count``. Only fields
        specified in ``updateMask`` are applied.

        During operation processing, the resource is temporarily in the
        ``ACTIVE`` state before the operation fully completes. For that
        period of time, you can't update the resource. Use the operation
        status to determine when the processing fully completes.

        Returns:
            Callable[[~.UpdateClusterRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_cluster" not in self._stubs:
            self._stubs["update_cluster"] = self.grpc_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/UpdateCluster",
                request_serializer=vmwareengine.UpdateClusterRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_cluster"]

    @property
    def delete_cluster(
        self,
    ) -> Callable[
        [vmwareengine.DeleteClusterRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the delete cluster method over gRPC.

        Deletes a ``Cluster`` resource. To avoid unintended data loss,
        migrate or gracefully shut down any workloads running on the
        cluster before deletion. You cannot delete the management
        cluster of a private cloud using this method.

        Returns:
            Callable[[~.DeleteClusterRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_cluster" not in self._stubs:
            self._stubs["delete_cluster"] = self.grpc_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/DeleteCluster",
                request_serializer=vmwareengine.DeleteClusterRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_cluster"]

    @property
    def list_subnets(
        self,
    ) -> Callable[
        [vmwareengine.ListSubnetsRequest], Awaitable[vmwareengine.ListSubnetsResponse]
    ]:
        r"""Return a callable for the list subnets method over gRPC.

        Lists subnets in a given private cloud.

        Returns:
            Callable[[~.ListSubnetsRequest],
                    Awaitable[~.ListSubnetsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_subnets" not in self._stubs:
            self._stubs["list_subnets"] = self.grpc_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/ListSubnets",
                request_serializer=vmwareengine.ListSubnetsRequest.serialize,
                response_deserializer=vmwareengine.ListSubnetsResponse.deserialize,
            )
        return self._stubs["list_subnets"]

    @property
    def list_node_types(
        self,
    ) -> Callable[
        [vmwareengine.ListNodeTypesRequest],
        Awaitable[vmwareengine.ListNodeTypesResponse],
    ]:
        r"""Return a callable for the list node types method over gRPC.

        Lists node types

        Returns:
            Callable[[~.ListNodeTypesRequest],
                    Awaitable[~.ListNodeTypesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_node_types" not in self._stubs:
            self._stubs["list_node_types"] = self.grpc_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/ListNodeTypes",
                request_serializer=vmwareengine.ListNodeTypesRequest.serialize,
                response_deserializer=vmwareengine.ListNodeTypesResponse.deserialize,
            )
        return self._stubs["list_node_types"]

    @property
    def get_node_type(
        self,
    ) -> Callable[
        [vmwareengine.GetNodeTypeRequest], Awaitable[vmwareengine_resources.NodeType]
    ]:
        r"""Return a callable for the get node type method over gRPC.

        Gets details of a single ``NodeType``.

        Returns:
            Callable[[~.GetNodeTypeRequest],
                    Awaitable[~.NodeType]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_node_type" not in self._stubs:
            self._stubs["get_node_type"] = self.grpc_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/GetNodeType",
                request_serializer=vmwareengine.GetNodeTypeRequest.serialize,
                response_deserializer=vmwareengine_resources.NodeType.deserialize,
            )
        return self._stubs["get_node_type"]

    @property
    def show_nsx_credentials(
        self,
    ) -> Callable[
        [vmwareengine.ShowNsxCredentialsRequest],
        Awaitable[vmwareengine_resources.Credentials],
    ]:
        r"""Return a callable for the show nsx credentials method over gRPC.

        Gets details of credentials for NSX appliance.

        Returns:
            Callable[[~.ShowNsxCredentialsRequest],
                    Awaitable[~.Credentials]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "show_nsx_credentials" not in self._stubs:
            self._stubs["show_nsx_credentials"] = self.grpc_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/ShowNsxCredentials",
                request_serializer=vmwareengine.ShowNsxCredentialsRequest.serialize,
                response_deserializer=vmwareengine_resources.Credentials.deserialize,
            )
        return self._stubs["show_nsx_credentials"]

    @property
    def show_vcenter_credentials(
        self,
    ) -> Callable[
        [vmwareengine.ShowVcenterCredentialsRequest],
        Awaitable[vmwareengine_resources.Credentials],
    ]:
        r"""Return a callable for the show vcenter credentials method over gRPC.

        Gets details of credentials for Vcenter appliance.

        Returns:
            Callable[[~.ShowVcenterCredentialsRequest],
                    Awaitable[~.Credentials]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "show_vcenter_credentials" not in self._stubs:
            self._stubs["show_vcenter_credentials"] = self.grpc_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/ShowVcenterCredentials",
                request_serializer=vmwareengine.ShowVcenterCredentialsRequest.serialize,
                response_deserializer=vmwareengine_resources.Credentials.deserialize,
            )
        return self._stubs["show_vcenter_credentials"]

    @property
    def reset_nsx_credentials(
        self,
    ) -> Callable[
        [vmwareengine.ResetNsxCredentialsRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the reset nsx credentials method over gRPC.

        Resets credentials of the NSX appliance.

        Returns:
            Callable[[~.ResetNsxCredentialsRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "reset_nsx_credentials" not in self._stubs:
            self._stubs["reset_nsx_credentials"] = self.grpc_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/ResetNsxCredentials",
                request_serializer=vmwareengine.ResetNsxCredentialsRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["reset_nsx_credentials"]

    @property
    def reset_vcenter_credentials(
        self,
    ) -> Callable[
        [vmwareengine.ResetVcenterCredentialsRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the reset vcenter credentials method over gRPC.

        Resets credentials of the Vcenter appliance.

        Returns:
            Callable[[~.ResetVcenterCredentialsRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "reset_vcenter_credentials" not in self._stubs:
            self._stubs["reset_vcenter_credentials"] = self.grpc_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/ResetVcenterCredentials",
                request_serializer=vmwareengine.ResetVcenterCredentialsRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["reset_vcenter_credentials"]

    @property
    def create_hcx_activation_key(
        self,
    ) -> Callable[
        [vmwareengine.CreateHcxActivationKeyRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the create hcx activation key method over gRPC.

        Creates a new HCX activation key in a given private
        cloud.

        Returns:
            Callable[[~.CreateHcxActivationKeyRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_hcx_activation_key" not in self._stubs:
            self._stubs["create_hcx_activation_key"] = self.grpc_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/CreateHcxActivationKey",
                request_serializer=vmwareengine.CreateHcxActivationKeyRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_hcx_activation_key"]

    @property
    def list_hcx_activation_keys(
        self,
    ) -> Callable[
        [vmwareengine.ListHcxActivationKeysRequest],
        Awaitable[vmwareengine.ListHcxActivationKeysResponse],
    ]:
        r"""Return a callable for the list hcx activation keys method over gRPC.

        Lists ``HcxActivationKey`` resources in a given private cloud.

        Returns:
            Callable[[~.ListHcxActivationKeysRequest],
                    Awaitable[~.ListHcxActivationKeysResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_hcx_activation_keys" not in self._stubs:
            self._stubs["list_hcx_activation_keys"] = self.grpc_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/ListHcxActivationKeys",
                request_serializer=vmwareengine.ListHcxActivationKeysRequest.serialize,
                response_deserializer=vmwareengine.ListHcxActivationKeysResponse.deserialize,
            )
        return self._stubs["list_hcx_activation_keys"]

    @property
    def get_hcx_activation_key(
        self,
    ) -> Callable[
        [vmwareengine.GetHcxActivationKeyRequest],
        Awaitable[vmwareengine_resources.HcxActivationKey],
    ]:
        r"""Return a callable for the get hcx activation key method over gRPC.

        Retrieves a ``HcxActivationKey`` resource by its resource name.

        Returns:
            Callable[[~.GetHcxActivationKeyRequest],
                    Awaitable[~.HcxActivationKey]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_hcx_activation_key" not in self._stubs:
            self._stubs["get_hcx_activation_key"] = self.grpc_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/GetHcxActivationKey",
                request_serializer=vmwareengine.GetHcxActivationKeyRequest.serialize,
                response_deserializer=vmwareengine_resources.HcxActivationKey.deserialize,
            )
        return self._stubs["get_hcx_activation_key"]

    @property
    def get_network_policy(
        self,
    ) -> Callable[
        [vmwareengine.GetNetworkPolicyRequest],
        Awaitable[vmwareengine_resources.NetworkPolicy],
    ]:
        r"""Return a callable for the get network policy method over gRPC.

        Retrieves a ``NetworkPolicy`` resource by its resource name.

        Returns:
            Callable[[~.GetNetworkPolicyRequest],
                    Awaitable[~.NetworkPolicy]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_network_policy" not in self._stubs:
            self._stubs["get_network_policy"] = self.grpc_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/GetNetworkPolicy",
                request_serializer=vmwareengine.GetNetworkPolicyRequest.serialize,
                response_deserializer=vmwareengine_resources.NetworkPolicy.deserialize,
            )
        return self._stubs["get_network_policy"]

    @property
    def list_network_policies(
        self,
    ) -> Callable[
        [vmwareengine.ListNetworkPoliciesRequest],
        Awaitable[vmwareengine.ListNetworkPoliciesResponse],
    ]:
        r"""Return a callable for the list network policies method over gRPC.

        Lists ``NetworkPolicy`` resources in a specified project and
        location.

        Returns:
            Callable[[~.ListNetworkPoliciesRequest],
                    Awaitable[~.ListNetworkPoliciesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_network_policies" not in self._stubs:
            self._stubs["list_network_policies"] = self.grpc_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/ListNetworkPolicies",
                request_serializer=vmwareengine.ListNetworkPoliciesRequest.serialize,
                response_deserializer=vmwareengine.ListNetworkPoliciesResponse.deserialize,
            )
        return self._stubs["list_network_policies"]

    @property
    def create_network_policy(
        self,
    ) -> Callable[
        [vmwareengine.CreateNetworkPolicyRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the create network policy method over gRPC.

        Creates a new network policy in a given VMware Engine
        network of a project and location (region). A new
        network policy cannot be created if another network
        policy already exists in the same scope.

        Returns:
            Callable[[~.CreateNetworkPolicyRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_network_policy" not in self._stubs:
            self._stubs["create_network_policy"] = self.grpc_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/CreateNetworkPolicy",
                request_serializer=vmwareengine.CreateNetworkPolicyRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_network_policy"]

    @property
    def update_network_policy(
        self,
    ) -> Callable[
        [vmwareengine.UpdateNetworkPolicyRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the update network policy method over gRPC.

        Modifies a ``NetworkPolicy`` resource. Only the following fields
        can be updated: ``internet_access``, ``external_ip``,
        ``edge_services_cidr``. Only fields specified in ``updateMask``
        are applied. When updating a network policy, the external IP
        network service can only be disabled if there are no external IP
        addresses present in the scope of the policy. Also, a
        ``NetworkService`` cannot be updated when
        ``NetworkService.state`` is set to ``RECONCILING``.

        During operation processing, the resource is temporarily in the
        ``ACTIVE`` state before the operation fully completes. For that
        period of time, you can't update the resource. Use the operation
        status to determine when the processing fully completes.

        Returns:
            Callable[[~.UpdateNetworkPolicyRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_network_policy" not in self._stubs:
            self._stubs["update_network_policy"] = self.grpc_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/UpdateNetworkPolicy",
                request_serializer=vmwareengine.UpdateNetworkPolicyRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_network_policy"]

    @property
    def delete_network_policy(
        self,
    ) -> Callable[
        [vmwareengine.DeleteNetworkPolicyRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the delete network policy method over gRPC.

        Deletes a ``NetworkPolicy`` resource. A network policy cannot be
        deleted when ``NetworkService.state`` is set to ``RECONCILING``
        for either its external IP or internet access service.

        Returns:
            Callable[[~.DeleteNetworkPolicyRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_network_policy" not in self._stubs:
            self._stubs["delete_network_policy"] = self.grpc_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/DeleteNetworkPolicy",
                request_serializer=vmwareengine.DeleteNetworkPolicyRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_network_policy"]

    @property
    def create_vmware_engine_network(
        self,
    ) -> Callable[
        [vmwareengine.CreateVmwareEngineNetworkRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the create vmware engine network method over gRPC.

        Creates a new VMware Engine network that can be used
        by a private cloud.

        Returns:
            Callable[[~.CreateVmwareEngineNetworkRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_vmware_engine_network" not in self._stubs:
            self._stubs["create_vmware_engine_network"] = self.grpc_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/CreateVmwareEngineNetwork",
                request_serializer=vmwareengine.CreateVmwareEngineNetworkRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_vmware_engine_network"]

    @property
    def update_vmware_engine_network(
        self,
    ) -> Callable[
        [vmwareengine.UpdateVmwareEngineNetworkRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the update vmware engine network method over gRPC.

        Modifies a VMware Engine network resource. Only the following
        fields can be updated: ``description``. Only fields specified in
        ``updateMask`` are applied.

        Returns:
            Callable[[~.UpdateVmwareEngineNetworkRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_vmware_engine_network" not in self._stubs:
            self._stubs["update_vmware_engine_network"] = self.grpc_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/UpdateVmwareEngineNetwork",
                request_serializer=vmwareengine.UpdateVmwareEngineNetworkRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_vmware_engine_network"]

    @property
    def delete_vmware_engine_network(
        self,
    ) -> Callable[
        [vmwareengine.DeleteVmwareEngineNetworkRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the delete vmware engine network method over gRPC.

        Deletes a ``VmwareEngineNetwork`` resource. You can only delete
        a VMware Engine network after all resources that refer to it are
        deleted. For example, a private cloud, a network peering, and a
        network policy can all refer to the same VMware Engine network.

        Returns:
            Callable[[~.DeleteVmwareEngineNetworkRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_vmware_engine_network" not in self._stubs:
            self._stubs["delete_vmware_engine_network"] = self.grpc_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/DeleteVmwareEngineNetwork",
                request_serializer=vmwareengine.DeleteVmwareEngineNetworkRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_vmware_engine_network"]

    @property
    def get_vmware_engine_network(
        self,
    ) -> Callable[
        [vmwareengine.GetVmwareEngineNetworkRequest],
        Awaitable[vmwareengine_resources.VmwareEngineNetwork],
    ]:
        r"""Return a callable for the get vmware engine network method over gRPC.

        Retrieves a ``VmwareEngineNetwork`` resource by its resource
        name. The resource contains details of the VMware Engine
        network, such as its VMware Engine network type, peered networks
        in a service project, and state (for example, ``CREATING``,
        ``ACTIVE``, ``DELETING``).

        Returns:
            Callable[[~.GetVmwareEngineNetworkRequest],
                    Awaitable[~.VmwareEngineNetwork]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_vmware_engine_network" not in self._stubs:
            self._stubs["get_vmware_engine_network"] = self.grpc_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/GetVmwareEngineNetwork",
                request_serializer=vmwareengine.GetVmwareEngineNetworkRequest.serialize,
                response_deserializer=vmwareengine_resources.VmwareEngineNetwork.deserialize,
            )
        return self._stubs["get_vmware_engine_network"]

    @property
    def list_vmware_engine_networks(
        self,
    ) -> Callable[
        [vmwareengine.ListVmwareEngineNetworksRequest],
        Awaitable[vmwareengine.ListVmwareEngineNetworksResponse],
    ]:
        r"""Return a callable for the list vmware engine networks method over gRPC.

        Lists ``VmwareEngineNetwork`` resources in a given project and
        location.

        Returns:
            Callable[[~.ListVmwareEngineNetworksRequest],
                    Awaitable[~.ListVmwareEngineNetworksResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_vmware_engine_networks" not in self._stubs:
            self._stubs["list_vmware_engine_networks"] = self.grpc_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/ListVmwareEngineNetworks",
                request_serializer=vmwareengine.ListVmwareEngineNetworksRequest.serialize,
                response_deserializer=vmwareengine.ListVmwareEngineNetworksResponse.deserialize,
            )
        return self._stubs["list_vmware_engine_networks"]

    def close(self):
        return self.grpc_channel.close()

    @property
    def delete_operation(
        self,
    ) -> Callable[[operations_pb2.DeleteOperationRequest], None]:
        r"""Return a callable for the delete_operation method over gRPC."""
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_operation" not in self._stubs:
            self._stubs["delete_operation"] = self.grpc_channel.unary_unary(
                "/google.longrunning.Operations/DeleteOperation",
                request_serializer=operations_pb2.DeleteOperationRequest.SerializeToString,
                response_deserializer=None,
            )
        return self._stubs["delete_operation"]

    @property
    def get_operation(
        self,
    ) -> Callable[[operations_pb2.GetOperationRequest], operations_pb2.Operation]:
        r"""Return a callable for the get_operation method over gRPC."""
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_operation" not in self._stubs:
            self._stubs["get_operation"] = self.grpc_channel.unary_unary(
                "/google.longrunning.Operations/GetOperation",
                request_serializer=operations_pb2.GetOperationRequest.SerializeToString,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["get_operation"]

    @property
    def list_operations(
        self,
    ) -> Callable[
        [operations_pb2.ListOperationsRequest], operations_pb2.ListOperationsResponse
    ]:
        r"""Return a callable for the list_operations method over gRPC."""
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_operations" not in self._stubs:
            self._stubs["list_operations"] = self.grpc_channel.unary_unary(
                "/google.longrunning.Operations/ListOperations",
                request_serializer=operations_pb2.ListOperationsRequest.SerializeToString,
                response_deserializer=operations_pb2.ListOperationsResponse.FromString,
            )
        return self._stubs["list_operations"]

    @property
    def list_locations(
        self,
    ) -> Callable[
        [locations_pb2.ListLocationsRequest], locations_pb2.ListLocationsResponse
    ]:
        r"""Return a callable for the list locations method over gRPC."""
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_locations" not in self._stubs:
            self._stubs["list_locations"] = self.grpc_channel.unary_unary(
                "/google.cloud.location.Locations/ListLocations",
                request_serializer=locations_pb2.ListLocationsRequest.SerializeToString,
                response_deserializer=locations_pb2.ListLocationsResponse.FromString,
            )
        return self._stubs["list_locations"]

    @property
    def get_location(
        self,
    ) -> Callable[[locations_pb2.GetLocationRequest], locations_pb2.Location]:
        r"""Return a callable for the list locations method over gRPC."""
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_location" not in self._stubs:
            self._stubs["get_location"] = self.grpc_channel.unary_unary(
                "/google.cloud.location.Locations/GetLocation",
                request_serializer=locations_pb2.GetLocationRequest.SerializeToString,
                response_deserializer=locations_pb2.Location.FromString,
            )
        return self._stubs["get_location"]

    @property
    def set_iam_policy(
        self,
    ) -> Callable[[iam_policy_pb2.SetIamPolicyRequest], policy_pb2.Policy]:
        r"""Return a callable for the set iam policy method over gRPC.
        Sets the IAM access control policy on the specified
        function. Replaces any existing policy.
        Returns:
            Callable[[~.SetIamPolicyRequest],
                    ~.Policy]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "set_iam_policy" not in self._stubs:
            self._stubs["set_iam_policy"] = self.grpc_channel.unary_unary(
                "/google.iam.v1.IAMPolicy/SetIamPolicy",
                request_serializer=iam_policy_pb2.SetIamPolicyRequest.SerializeToString,
                response_deserializer=policy_pb2.Policy.FromString,
            )
        return self._stubs["set_iam_policy"]

    @property
    def get_iam_policy(
        self,
    ) -> Callable[[iam_policy_pb2.GetIamPolicyRequest], policy_pb2.Policy]:
        r"""Return a callable for the get iam policy method over gRPC.
        Gets the IAM access control policy for a function.
        Returns an empty policy if the function exists and does
        not have a policy set.
        Returns:
            Callable[[~.GetIamPolicyRequest],
                    ~.Policy]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_iam_policy" not in self._stubs:
            self._stubs["get_iam_policy"] = self.grpc_channel.unary_unary(
                "/google.iam.v1.IAMPolicy/GetIamPolicy",
                request_serializer=iam_policy_pb2.GetIamPolicyRequest.SerializeToString,
                response_deserializer=policy_pb2.Policy.FromString,
            )
        return self._stubs["get_iam_policy"]

    @property
    def test_iam_permissions(
        self,
    ) -> Callable[
        [iam_policy_pb2.TestIamPermissionsRequest],
        iam_policy_pb2.TestIamPermissionsResponse,
    ]:
        r"""Return a callable for the test iam permissions method over gRPC.
        Tests the specified permissions against the IAM access control
        policy for a function. If the function does not exist, this will
        return an empty set of permissions, not a NOT_FOUND error.
        Returns:
            Callable[[~.TestIamPermissionsRequest],
                    ~.TestIamPermissionsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "test_iam_permissions" not in self._stubs:
            self._stubs["test_iam_permissions"] = self.grpc_channel.unary_unary(
                "/google.iam.v1.IAMPolicy/TestIamPermissions",
                request_serializer=iam_policy_pb2.TestIamPermissionsRequest.SerializeToString,
                response_deserializer=iam_policy_pb2.TestIamPermissionsResponse.FromString,
            )
        return self._stubs["test_iam_permissions"]


__all__ = ("VmwareEngineGrpcAsyncIOTransport",)
