"""
This is data type Attributes
"""
import os
import typing

import src.algorithms.descriptors


class Attributes(typing.NamedTuple):
    """
    The attributes class.
    """

    dictionary = src.algorithms.descriptors.Descriptors(
        path=os.path.join(os.getcwd(), 'data', 'images.yml')).exc(node=['data', 'attributes'])

    ext: str = dictionary['ext']
    rows: int = dictionary['rows']
    columns: int = dictionary['columns']
    channels: int = dictionary['channels']
    rotations: list[int] = dictionary['rotations']
