#!/usr/bin/python3
"""creates a class city class."""
from models.base_model import BaseModel


class City(BaseModel):
    """intializes a class city with the following attributes:

        state_id (str): The state id.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""
