#!/usr/bin/python3
"""Dfines the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Rresent a state.

    Attributes:
        name (str): The name of the state.
    """

    name = ""
