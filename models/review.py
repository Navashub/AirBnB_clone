#!/usr/bin/python3
"""creates the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """initializes a review by a guest with the following attributes:

    
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
