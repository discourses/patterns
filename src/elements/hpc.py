"""
This is data type HPC (hyperparameter case)
"""

import typing


class HPC(typing.NamedTuple):
    """
    The HPC class.
    """

    alpha_units: int = 512
    alpha_dropout: float = 0.1
    beta_units: int = 512
    beta_dropout: float = 0.1
    opt: str = 'adam'
