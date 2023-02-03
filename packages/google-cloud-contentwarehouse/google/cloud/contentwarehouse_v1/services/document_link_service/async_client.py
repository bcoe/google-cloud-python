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
from collections import OrderedDict
import functools
import re
from typing import (
    Dict,
    Mapping,
    MutableMapping,
    MutableSequence,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
)

from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.api_core.client_options import ClientOptions
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.contentwarehouse_v1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore

from google.longrunning import operations_pb2
from google.protobuf import timestamp_pb2  # type: ignore

from google.cloud.contentwarehouse_v1.services.document_link_service import pagers
from google.cloud.contentwarehouse_v1.types import document, document_link_service

from .client import DocumentLinkServiceClient
from .transports.base import DEFAULT_CLIENT_INFO, DocumentLinkServiceTransport
from .transports.grpc_asyncio import DocumentLinkServiceGrpcAsyncIOTransport


class DocumentLinkServiceAsyncClient:
    """This service lets you manage document-links.
    Document-Links are treated as sub-resources under source
    documents.
    """

    _client: DocumentLinkServiceClient

    DEFAULT_ENDPOINT = DocumentLinkServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = DocumentLinkServiceClient.DEFAULT_MTLS_ENDPOINT

    document_path = staticmethod(DocumentLinkServiceClient.document_path)
    parse_document_path = staticmethod(DocumentLinkServiceClient.parse_document_path)
    document_link_path = staticmethod(DocumentLinkServiceClient.document_link_path)
    parse_document_link_path = staticmethod(
        DocumentLinkServiceClient.parse_document_link_path
    )
    common_billing_account_path = staticmethod(
        DocumentLinkServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        DocumentLinkServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(DocumentLinkServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        DocumentLinkServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        DocumentLinkServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        DocumentLinkServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(DocumentLinkServiceClient.common_project_path)
    parse_common_project_path = staticmethod(
        DocumentLinkServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(DocumentLinkServiceClient.common_location_path)
    parse_common_location_path = staticmethod(
        DocumentLinkServiceClient.parse_common_location_path
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            DocumentLinkServiceAsyncClient: The constructed client.
        """
        return DocumentLinkServiceClient.from_service_account_info.__func__(DocumentLinkServiceAsyncClient, info, *args, **kwargs)  # type: ignore

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            DocumentLinkServiceAsyncClient: The constructed client.
        """
        return DocumentLinkServiceClient.from_service_account_file.__func__(DocumentLinkServiceAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[ClientOptions] = None
    ):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variable is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        return DocumentLinkServiceClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> DocumentLinkServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            DocumentLinkServiceTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(DocumentLinkServiceClient).get_transport_class,
        type(DocumentLinkServiceClient),
    )

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Union[str, DocumentLinkServiceTransport] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the document link service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.DocumentLinkServiceTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = DocumentLinkServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def list_linked_targets(
        self,
        request: Optional[
            Union[document_link_service.ListLinkedTargetsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> document_link_service.ListLinkedTargetsResponse:
        r"""Return all target document-links from the document.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contentwarehouse_v1

            async def sample_list_linked_targets():
                # Create a client
                client = contentwarehouse_v1.DocumentLinkServiceAsyncClient()

                # Initialize request argument(s)
                request = contentwarehouse_v1.ListLinkedTargetsRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.list_linked_targets(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.contentwarehouse_v1.types.ListLinkedTargetsRequest, dict]]):
                The request object. Request message for
                DocumentLinkService.ListLinkedTargets.
            parent (:class:`str`):
                Required. The name of the document, for which all target
                links are returned. Format:
                projects/{project_number}/locations/{location}/documents/{target_document_id}.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.contentwarehouse_v1.types.ListLinkedTargetsResponse:
                Response message for
                DocumentLinkService.ListLinkedTargets.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = document_link_service.ListLinkedTargetsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_linked_targets,
            default_timeout=180.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_linked_sources(
        self,
        request: Optional[
            Union[document_link_service.ListLinkedSourcesRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListLinkedSourcesAsyncPager:
        r"""Return all source document-links from the document.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contentwarehouse_v1

            async def sample_list_linked_sources():
                # Create a client
                client = contentwarehouse_v1.DocumentLinkServiceAsyncClient()

                # Initialize request argument(s)
                request = contentwarehouse_v1.ListLinkedSourcesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_linked_sources(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.contentwarehouse_v1.types.ListLinkedSourcesRequest, dict]]):
                The request object. Response message for
                DocumentLinkService.ListLinkedSources.
            parent (:class:`str`):
                Required. The name of the document, for which all source
                links are returned. Format:
                projects/{project_number}/locations/{location}/documents/{source_document_id}.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.contentwarehouse_v1.services.document_link_service.pagers.ListLinkedSourcesAsyncPager:
                Response message for
                DocumentLinkService.ListLinkedSources.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = document_link_service.ListLinkedSourcesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_linked_sources,
            default_timeout=180.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListLinkedSourcesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def create_document_link(
        self,
        request: Optional[
            Union[document_link_service.CreateDocumentLinkRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        document_link: Optional[document_link_service.DocumentLink] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> document_link_service.DocumentLink:
        r"""Create a link between a source document and a target
        document.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contentwarehouse_v1

            async def sample_create_document_link():
                # Create a client
                client = contentwarehouse_v1.DocumentLinkServiceAsyncClient()

                # Initialize request argument(s)
                request = contentwarehouse_v1.CreateDocumentLinkRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.create_document_link(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.contentwarehouse_v1.types.CreateDocumentLinkRequest, dict]]):
                The request object. Request message for
                DocumentLinkService.CreateDocumentLink.
            parent (:class:`str`):
                Required. Parent of the document-link to be created.
                parent of document-link should be a document. Format:
                projects/{project_number}/locations/{location}/documents/{source_document_id}.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            document_link (:class:`google.cloud.contentwarehouse_v1.types.DocumentLink`):
                Required. Document links associated with the source
                documents (source_document_id).

                This corresponds to the ``document_link`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.contentwarehouse_v1.types.DocumentLink:
                A document-link between source and
                target document.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, document_link])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = document_link_service.CreateDocumentLinkRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if document_link is not None:
            request.document_link = document_link

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_document_link,
            default_timeout=180.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_document_link(
        self,
        request: Optional[
            Union[document_link_service.DeleteDocumentLinkRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Remove the link between the source and target
        documents.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contentwarehouse_v1

            async def sample_delete_document_link():
                # Create a client
                client = contentwarehouse_v1.DocumentLinkServiceAsyncClient()

                # Initialize request argument(s)
                request = contentwarehouse_v1.DeleteDocumentLinkRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_document_link(request=request)

        Args:
            request (Optional[Union[google.cloud.contentwarehouse_v1.types.DeleteDocumentLinkRequest, dict]]):
                The request object. Request message for
                DocumentLinkService.DeleteDocumentLink.
            name (:class:`str`):
                Required. The name of the document-link to be deleted.
                Format:
                projects/{project_number}/locations/{location}/documents/{source_document_id}/documentLinks/{document_link_id}.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = document_link_service.DeleteDocumentLinkRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_document_link,
            default_timeout=180.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)


__all__ = ("DocumentLinkServiceAsyncClient",)
