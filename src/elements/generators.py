"""
This is data type Generators
"""
import typing

import tensorflow as tf


class Generators(typing.NamedTuple):
    """
    The generators class
    """

    training: tf.data.Dataset
    validating: tf.data.Dataset
    testing: tf.data.Dataset
