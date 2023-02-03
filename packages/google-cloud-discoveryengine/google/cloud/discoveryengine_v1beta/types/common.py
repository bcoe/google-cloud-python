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
from typing import MutableMapping, MutableSequence

import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.discoveryengine.v1beta",
    manifest={
        "CustomAttribute",
        "UserInfo",
    },
)


class CustomAttribute(proto.Message):
    r"""A custom attribute that is not explicitly modeled in a resource,
    e.g. [UserEvent][google.cloud.discoveryengine.v1beta.UserEvent].

    Attributes:
        text (MutableSequence[str]):
            The textual values of this custom attribute. For example,
            ``["yellow", "green"]`` when the key is "color".

            Empty string is not allowed. Otherwise, an INVALID_ARGUMENT
            error is returned.

            Exactly one of
            [text][google.cloud.discoveryengine.v1beta.CustomAttribute.text]
            or
            [numbers][google.cloud.discoveryengine.v1beta.CustomAttribute.numbers]
            should be set. Otherwise, an INVALID_ARGUMENT error is
            returned.
        numbers (MutableSequence[float]):
            The numerical values of this custom attribute. For example,
            ``[2.3, 15.4]`` when the key is "lengths_cm".

            Exactly one of
            [text][google.cloud.discoveryengine.v1beta.CustomAttribute.text]
            or
            [numbers][google.cloud.discoveryengine.v1beta.CustomAttribute.numbers]
            should be set. Otherwise, an INVALID_ARGUMENT error is
            returned.
    """

    text: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    numbers: MutableSequence[float] = proto.RepeatedField(
        proto.DOUBLE,
        number=2,
    )


class UserInfo(proto.Message):
    r"""Information of an end user.

    Attributes:
        user_id (str):
            Highly recommended for logged-in users. Unique identifier
            for logged-in user, such as a user name. Don't set for
            anonymous users.

            Always use a hashed value for this ID.

            Don't set the field to the same fixed ID for different
            users. This mixes the event history of those users together,
            which results in degraded model quality.

            The field must be a UTF-8 encoded string with a length limit
            of 128 characters. Otherwise, an INVALID_ARGUMENT error is
            returned.
        user_agent (str):
            User agent as included in the HTTP header. Required for
            getting [SearchResponse.sponsored_results][].

            The field must be a UTF-8 encoded string with a length limit
            of 1,000 characters. Otherwise, an INVALID_ARGUMENT error is
            returned.

            This should not be set when using the client side event
            reporting with GTM or JavaScript tag in
            [UserEventService.CollectUserEvent][google.cloud.discoveryengine.v1beta.UserEventService.CollectUserEvent]
            or if [direct_user_request][] is set.
    """

    user_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    user_agent: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
