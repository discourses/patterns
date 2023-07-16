"""
splits.py
"""
import pandas as pd

import src.functions.splitting

import config


class Splits:
    """
    Class Splits

    Delivers the learning, validation, and testing splits
    """

    Settings = config.Config().Settings
    Metadata = config.Config().Metadata

    def __init__(self, settings: Settings, metadata: Metadata):
        """

        :param settings:
        :param metadata:
        """

        # Data Classes
        self.__settings = settings
        self.__metadata = metadata

        # Instances
        self.__splitting = src.functions.splitting.Splitting(random_state=self.__settings.random_state)
        
    def __splits(self, data: pd.DataFrame, train_size: float):

        return self.__splitting.exc(
            independent=data['path'], dependent=data[self.__metadata.labels],
            train_size=train_size, stratify=data[self.__metadata.labels])

    def exc(self, sample: pd.DataFrame):
        """

        :return:
        """

        training: pd.DataFrame
        evaluating: pd.DataFrame
        training, evaluating = self.__splits(
            data=sample, train_size=self.__settings.train_size_initial)

        validating: pd.DataFrame
        testing: pd.DataFrame
        validating, testing = self.__splits(
            data=evaluating, train_size=self.__settings.train_size_evaluation)
