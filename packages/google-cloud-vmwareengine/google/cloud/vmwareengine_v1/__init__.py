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
from google.cloud.vmwareengine_v1 import gapic_version as package_version

__version__ = package_version.__version__


from .services.vmware_engine import VmwareEngineAsyncClient, VmwareEngineClient
from .types.vmwareengine import (
    CreateClusterRequest,
    CreateHcxActivationKeyRequest,
    CreateNetworkPolicyRequest,
    CreatePrivateCloudRequest,
    CreateVmwareEngineNetworkRequest,
    DeleteClusterRequest,
    DeleteNetworkPolicyRequest,
    DeletePrivateCloudRequest,
    DeleteVmwareEngineNetworkRequest,
    GetClusterRequest,
    GetHcxActivationKeyRequest,
    GetNetworkPolicyRequest,
    GetNodeTypeRequest,
    GetPrivateCloudRequest,
    GetVmwareEngineNetworkRequest,
    ListClustersRequest,
    ListClustersResponse,
    ListHcxActivationKeysRequest,
    ListHcxActivationKeysResponse,
    ListNetworkPoliciesRequest,
    ListNetworkPoliciesResponse,
    ListNodeTypesRequest,
    ListNodeTypesResponse,
    ListPrivateCloudsRequest,
    ListPrivateCloudsResponse,
    ListSubnetsRequest,
    ListSubnetsResponse,
    ListVmwareEngineNetworksRequest,
    ListVmwareEngineNetworksResponse,
    OperationMetadata,
    ResetNsxCredentialsRequest,
    ResetVcenterCredentialsRequest,
    ShowNsxCredentialsRequest,
    ShowVcenterCredentialsRequest,
    UndeletePrivateCloudRequest,
    UpdateClusterRequest,
    UpdateNetworkPolicyRequest,
    UpdatePrivateCloudRequest,
    UpdateVmwareEngineNetworkRequest,
)
from .types.vmwareengine_resources import (
    Cluster,
    Credentials,
    Hcx,
    HcxActivationKey,
    NetworkConfig,
    NetworkPolicy,
    NodeType,
    NodeTypeConfig,
    Nsx,
    PrivateCloud,
    Subnet,
    Vcenter,
    VmwareEngineNetwork,
)

__all__ = (
    "VmwareEngineAsyncClient",
    "Cluster",
    "CreateClusterRequest",
    "CreateHcxActivationKeyRequest",
    "CreateNetworkPolicyRequest",
    "CreatePrivateCloudRequest",
    "CreateVmwareEngineNetworkRequest",
    "Credentials",
    "DeleteClusterRequest",
    "DeleteNetworkPolicyRequest",
    "DeletePrivateCloudRequest",
    "DeleteVmwareEngineNetworkRequest",
    "GetClusterRequest",
    "GetHcxActivationKeyRequest",
    "GetNetworkPolicyRequest",
    "GetNodeTypeRequest",
    "GetPrivateCloudRequest",
    "GetVmwareEngineNetworkRequest",
    "Hcx",
    "HcxActivationKey",
    "ListClustersRequest",
    "ListClustersResponse",
    "ListHcxActivationKeysRequest",
    "ListHcxActivationKeysResponse",
    "ListNetworkPoliciesRequest",
    "ListNetworkPoliciesResponse",
    "ListNodeTypesRequest",
    "ListNodeTypesResponse",
    "ListPrivateCloudsRequest",
    "ListPrivateCloudsResponse",
    "ListSubnetsRequest",
    "ListSubnetsResponse",
    "ListVmwareEngineNetworksRequest",
    "ListVmwareEngineNetworksResponse",
    "NetworkConfig",
    "NetworkPolicy",
    "NodeType",
    "NodeTypeConfig",
    "Nsx",
    "OperationMetadata",
    "PrivateCloud",
    "ResetNsxCredentialsRequest",
    "ResetVcenterCredentialsRequest",
    "ShowNsxCredentialsRequest",
    "ShowVcenterCredentialsRequest",
    "Subnet",
    "UndeletePrivateCloudRequest",
    "UpdateClusterRequest",
    "UpdateNetworkPolicyRequest",
    "UpdatePrivateCloudRequest",
    "UpdateVmwareEngineNetworkRequest",
    "Vcenter",
    "VmwareEngineClient",
    "VmwareEngineNetwork",
)
