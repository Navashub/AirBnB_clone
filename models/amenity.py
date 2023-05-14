#!/usr/bin/python3
"""creates an Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """initializes  an amenity with the following attributes:

        name (str): The name of the amenity.
    """

    name = ""
