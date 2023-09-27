"""
splits.py
"""
import pandas as pd

import src.functions.splitting

import src.types.settings
import src.types.metadata
import src.types.partitions


class Splits:
    """
    Class Splits

    Delivers the learning, validation, and testing splits
    """

    def __init__(self, settings: src.types.settings.Settings,
                 metadata: src.types.metadata.Metadata):
        """

        :param settings:
        :param metadata:
        """

        # Data Classes
        self.__settings = settings
        self.__metadata = metadata

        # And
        self.__fields = metadata.features + [metadata.path]

        # Instances
        self.__splitting = src.functions.splitting.Splitting(random_state=self.__settings.random_state)

    def __splits(self, data: pd.DataFrame, train_size: float) -> (pd.DataFrame, pd.DataFrame):
        """

        :param data:
        :param train_size:
        :return:
        """

        return self.__splitting.exc(
            independent=data[self.__fields], dependent=data[self.__metadata.labels],
            train_size=train_size, stratify=data[self.__metadata.labels])

    def exc(self, sample: pd.DataFrame) -> src.types.partitions.Partitions:
        """

        :param sample:  The metadata data frame that will be split into training/validating/testing
        :return:
        """

        training, evaluating = self.__splits(
            data=sample, train_size=self.__settings.train_size_initial)

        validating, testing = self.__splits(
            data=evaluating, train_size=self.__settings.train_size_evaluation)

        return src.types.partitions.Partitions(
            training=training, validating=validating, testing=testing)
