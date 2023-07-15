"""
config.py
"""
import collections


class Config:
    """
    Class Config
    """

    Modelling = collections.namedtuple(
        typename='Modelling',
        field_names=['sample', 'replace', 'class_sample_size', 'epochs', 'features', 'random_state',
                     'minimum_class_instances', 'batch_size', 'train_size_initial', 'train_size_evaluation',
                     'early_stopping_patience', 'model_checkpoints_directory', 'error_matrix_variables'])

    Metadata = collections.namedtuple(
        typename='Metadata',
        field_names=['url', 'key', 'fields', 'labels'])

    def __init__(self):
        """
        Constructor
        """

    def exc(self):
        """

        :return:
        """
