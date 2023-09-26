"""
This is data type Partitions
"""
import typing

import pandas as pd



class Partitions(typing.NamedTuple):
    """
    The partitions class.
    """

    training: pd.DataFrame = None
    validating: pd.DataFrame = None
    testing: pd.DataFrame = None
