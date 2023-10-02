"""
For determining
    (a) predictions vis-a-vis training, validation, and testing data
    (b) error matrix frequencies vis-a-vis testing data
"""
import logging
import os

import numpy as np
import pandas as pd
import tensorflow as tf

import src.elements.generators
import src.elements.metadata
import src.elements.partitions
import src.elements.settings
import src.evaluation.frequencies
import src.evaluation.predictions
import src.functions.streams


class Predicting:
    """
    Class Predicting
    """

    def __init__(self, metadata: src.elements.metadata.Metadata, settings: src.elements.settings.Settings,
                 model: tf.keras.Sequential, pathway: str) -> None:
        """

        :param metadata:
        :param settings:
        :param model:
        :param pathway:
        :return:        
        """

        self.__metadata = metadata
        self.__settings = settings
        self.__model = model
        self.__pathway = pathway

        # Predictions
        self.__predictions = src.evaluation.predictions.Predictions(
            pathway=self.__pathway, metadata=self.__metadata, settings=self.__settings)

        # The thresholds
        self.__thresholds = np.arange(
            start=self.__settings.threshold_min, stop=self.__settings.threshold_max, step=self.__settings.threshold_step)

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def __plausibilites(self, partition_: pd.DataFrame, generator_: tf.data.Dataset, name: str) -> np.ndarray:
        """
        
        :param partition_:
        :param generator_:
        :return:
        """

        return self.__predictions.exc(model=self.__model, partition_=partition_, generator_=generator_, name=name)

    def __frequencies(self, partition_: pd.DataFrame, plausibilities: np.ndarray) -> str:
        """
        
        :param partition_:
        :param plausibilities:
        :return:
        """

        
        # Truth
        truth = partition_[self.__metadata.labels].values

        # Error matrix frequencies
        data = src.evaluation.frequencies.Frequencies(
            thresholds=self.__thresholds, plausibilities=plausibilities, truth=truth, classes=self.__metadata.labels)

        return src.functions.streams.Streams().write(
            blob=data, path=os.path.join(self.__pathway, 'frequencies.csv'))

    def exc(self, generators: src.elements.generators.Generators,
                 partitions: src.elements.partitions.Partitions):
        """
        
        :param model:
        :param pathway:
        :return:
        """

        assert np.setdiff1d(
            generators._fields, partitions._fields).shape[0] == 0, 'There might be a set-up error w.r.t. modelling data'

        for field in partitions._fields:

            partition_: pd.DataFrame = getattr(partitions, field)
            generator_: tf.data.Dataset = getattr(generators, field)

            plausibilities: np.ndarray = self.__plausibilites(partition_=partition_, generator_=generator_, name=field)

            if field == 'testing':
                message = self.__frequencies(partition_=partition_, plausibilities=plausibilities)
                self.__logger.info(message)
