"""
This is data type Metadata
"""
import typing


class Metadata(typing.NamedTuple):
    """
    Constructor
    """

    url: str = None
    key: str
    fields: list
    path: str
    labels: list
