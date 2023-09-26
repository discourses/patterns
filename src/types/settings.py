"""
This is data type Settings
"""
import os
import typing

import src.algorithms.descriptors


class Settings(typing.NamedTuple):
    """
    The settings class.
    """

    dictionary = src.algorithms.descriptors.Descriptors(
        path=os.path.join(os.getcwd(), 'data', 'images.yml')).exc(node=['settings'])

    sample: bool = dictionary['sample']
    replace: bool = dictionary['replace']
    class_sample_size: int = dictionary['class_sample_size']
    epochs: int = dictionary['epochs']
    random_state: int = dictionary['random_state']
    minimum_class_instances: int
    batch_size: int = dictionary['batch_size']
    train_size_initial: float = dictionary['train_size_initial']
    train_size_evaluation: float = dictionary['train_size_evaluation']
    early_stopping_patience: int = dictionary['early_stopping_patience']
    model_checkpoints_directory: list = dictionary['model_checkpoints_directory']
    error_matrix_variables: list = dictionary['error_matrix_variables']
