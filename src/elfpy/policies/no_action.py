"""Base policy class

Policies inherit from Users (thus each policy is assigned to a user)
subclasses of BasicPolicy will implement trade actions
"""
from __future__ import annotations  # types will be strings by default in 3.11

from elfpy.markets import Market
from elfpy.agent import Agent
from elfpy.types import MarketAction


class NoAction(Agent):
    """
    Most basic policy setup, which implements a noop agent that performs no action
    """

    def action(self, market: Market) -> list[MarketAction]:
        """Returns an empty list, indicating now action"""
        # pylint disable=unused-argument
        action_list = []
        return action_list
