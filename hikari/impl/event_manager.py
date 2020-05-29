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
"""Event handling logic."""

from __future__ import annotations

__all__ = ["EventManagerImpl"]

from hikari.impl import event_manager_core
from hikari.net import gateway
from hikari.utilities import binding


class EventManagerImpl(event_manager_core.EventManagerCore):
    """Provides event handling logic for Discord events."""

    async def _on_message_create(self, shard: gateway.Gateway, payload: binding.JSONObject) -> None:
        print(shard, payload)
