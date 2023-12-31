"""
config.py
"""
import collections


class Config:
    """
    Class Config

    Later, transfer the collections to a class named DataType; remember inheritance.
    """

    # The values of Settings, Metadata, Source, & Attributes are defined in descriptors/images.yml
    Settings = collections.namedtuple(
        typename='Settings',
        field_names=['sample', 'replace', 'class_sample_size', 'epochs', 'random_state',
                     'minimum_class_instances', 'batch_size', 'train_size_initial', 'train_size_evaluation',
                     'early_stopping_patience', 'model_checkpoints_directory', 'error_matrix_variables'])

    Metadata = collections.namedtuple(
        typename='Metadata', field_names=['url', 'key', 'fields', 'path', 'labels'])

    Source = collections.namedtuple(
        typename='Source', field_names=['url', 'index_from', 'index_to', 'index_zero_filling', 'ext', 'directory'])

    Attributes = collections.namedtuple(
        typename='Attributes', field_names=['ext', 'rows', 'columns', 'channels', 'rotations'])

    # These are the metadata data frames of a prospective set of training, validating, & testing data
    Partitions = collections.namedtuple(
        typename='Partitions', field_names=['training', 'validating', 'testing'])

    def __init__(self):
        """
        Constructor
        """

    def exc(self):
        """

        :return:
        """
