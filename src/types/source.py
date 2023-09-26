"""
This is data type Source
"""
import os
import typing

import src.algorithms.descriptors


class Source(typing.NamedTuple):
    """
    The source class.
    """

    dictionary = src.algorithms.descriptors.Descriptors(
        path=os.path.join(os.getcwd(), 'data', 'images.yml')).exc(node=['data', 'source'])

    url: str = dictionary['url']
    index_from: int = dictionary['index_from']
    index_to: int = dictionary['index_to']
    index_zero_filling: int = dictionary['index_zero_filling']
    ext: str = dictionary['ext']
