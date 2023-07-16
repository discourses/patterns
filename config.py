"""
config.py
"""
import collections


class Config:
    """
    Class Config
    """

    Settings = collections.namedtuple(
        typename='Settings',
        field_names=['sample', 'replace', 'class_sample_size', 'epochs', 'independent', 'random_state',
                     'minimum_class_instances', 'batch_size', 'train_size_initial', 'train_size_evaluation',
                     'early_stopping_patience', 'model_checkpoints_directory', 'error_matrix_variables'])

    Metadata = collections.namedtuple(
        typename='Metadata',
        field_names=['url', 'key', 'fields', 'labels'])

    Source = collections.namedtuple(
        typename='Source',
        field_names=['url', 'index_from', 'index_to', 'index_zero_filling', 'ext', 'directory'])

    def __init__(self):
        """
        Constructor
        """

    def exc(self):
        """

        :return:
        """
