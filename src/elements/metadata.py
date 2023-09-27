"""
This is data type Metadata
"""
import os
import typing

import src.algorithms.descriptors


class Metadata(typing.NamedTuple):
    """
    The metadata class.
    """

    dictionary = src.algorithms.descriptors.Descriptors(
        path=os.path.join(os.getcwd(), 'data', 'images.yml')).exc(node=['metadata'])

    url: str = dictionary['url']
    key: str = dictionary['key']
    features: list = dictionary['features']
    path: str = dictionary['path']
    labels: list = dictionary['labels']
