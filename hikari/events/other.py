#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © Nekoka.tt 2019-2020
#
# This file is part of Hikari.
#
# Hikari is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Hikari is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Hikari. If not, see <https://www.gnu.org/licenses/>.
"""Application and entities that are used to describe Discord gateway other events."""

from __future__ import annotations

__all__ = [
    "ExceptionEvent",
    "ConnectedEvent",
    "DisconnectedEvent",
    "StartingEvent",
    "StartedEvent",
    "StoppingEvent",
    "StoppedEvent",
    "ReadyEvent",
    "ResumedEvent",
    "MyUserUpdateEvent",
]

import typing

import attr

from hikari.models import bases as base_models
from hikari.models import guilds
from hikari.models import users
from . import base as base_events

if typing.TYPE_CHECKING:
    from ..net import gateway as gateway_client


# Synthetic event, is not deserialized, and is produced by the dispatcher.
@base_events.no_catch()
@attr.s(auto_attribs=True, eq=False, hash=False, kw_only=True, slots=True)
class ExceptionEvent(base_events.HikariEvent):
    """Descriptor for an exception thrown while processing an event."""

    exception: Exception
    """The exception that was raised."""

    event: base_events.HikariEvent
    """The event that was being invoked when the exception occurred."""

    callback: typing.Callable[[base_events.HikariEvent], typing.Awaitable[None]]
    """The event that was being invoked when the exception occurred."""


# Synthetic event, is not deserialized
@attr.s(auto_attribs=True, eq=False, hash=False, kw_only=True, slots=True)
class StartingEvent(base_events.HikariEvent):
    """Event that is fired before the gateway client starts all shards."""


# Synthetic event, is not deserialized
@attr.s(auto_attribs=True, eq=False, hash=False, kw_only=True, slots=True)
class StartedEvent(base_events.HikariEvent):
    """Event that is fired when the gateway client starts all shards."""


# Synthetic event, is not deserialized
@attr.s(auto_attribs=True, eq=False, hash=False, kw_only=True, slots=True)
class StoppingEvent(base_events.HikariEvent):
    """Event that is fired when the gateway client is instructed to disconnect all shards."""


# Synthetic event, is not deserialized
@attr.s(auto_attribs=True, eq=False, hash=False, kw_only=True, slots=True)
class StoppedEvent(base_events.HikariEvent):
    """Event that is fired when the gateway client has finished disconnecting all shards."""


@attr.s(auto_attribs=True, eq=False, hash=False, kw_only=True, slots=True)
class ConnectedEvent(base_events.HikariEvent):
    """Event invoked each time a shard connects."""

    shard: gateway_client.Gateway
    """The shard that connected."""


@attr.s(auto_attribs=True, eq=False, hash=False, kw_only=True, slots=True)
class DisconnectedEvent(base_events.HikariEvent):
    """Event invoked each time a shard disconnects."""

    shard: gateway_client.Gateway
    """The shard that disconnected."""


@attr.s(auto_attribs=True, eq=False, hash=False, kw_only=True, slots=True)
class ResumedEvent(base_events.HikariEvent):
    """Represents a gateway Resume event."""

    shard: gateway_client.Gateway
    """The shard that reconnected."""


@attr.s(eq=False, hash=False, kw_only=True, slots=True)
class ReadyEvent(base_events.HikariEvent):
    """Represents the gateway Ready event.

    This is received only when IDENTIFYing with the gateway.
    """

    gateway_version: int = attr.ib(repr=True)
    """The gateway version this is currently connected to."""

    my_user: users.MyUser = attr.ib(repr=True)
    """The object of the current bot account this connection is for."""

    unavailable_guilds: typing.Mapping[base_models.Snowflake, guilds.UnavailableGuild] = attr.ib()
    """A mapping of the guilds this bot is currently in.

    All guilds will start off "unavailable".
    """

    session_id: str = attr.ib(repr=True)
    """The id of the current gateway session, used for reconnecting."""

    _shard_information: typing.Optional[typing.Tuple[int, int]] = attr.ib()
    """Information about the current shard, only provided when IDENTIFYing."""

    @property
    def shard_id(self) -> typing.Optional[int]:
        """Zero-indexed ID of the current shard.

        This is only available if this ready event was received while IDENTIFYing.
        """
        return self._shard_information[0] if self._shard_information else None

    @property
    def shard_count(self) -> typing.Optional[int]:
        """Total shard count for this bot.

        This is only available if this ready event was received while IDENTIFYing.
        """
        return self._shard_information[1] if self._shard_information else None


@attr.s(eq=False, hash=False, kw_only=True, slots=True)
class MyUserUpdateEvent(base_events.HikariEvent, users.MyUser):
    """Used to represent User Update gateway events.

    Sent when the current user is updated.
    """
