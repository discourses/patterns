"""
For evaluating various aspects of a model
"""
import ast
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


class Evaluating:
    """
    Class Evaluating
    """

    def __init__(self, metadata: src.elements.metadata.Metadata,
                 settings: src.elements.settings.Settings,
                 generators: src.elements.generators.Generators,
                 partitions: src.elements.partitions.Partitions) -> None:
        """

        :param metadata:
        :param settings:
        :param generators:
        :param partitions:
        :return:        
        """

        self.__metadata = metadata
        self.__settings = settings
        self.__generators = generators
        self.__partitions = partitions

    def __predictions(self, model: tf.keras.Sequential, pathway: str):
        """
        
        :param model:
        :param pathway:
        :return:
        """

        # The thresholds
        thresholds = np.arange(
            start=self.__settings.threshold_min, stop=self.__settings.threshold_max, step=self.__settings.threshold_step)

        # Predictions
        predictions = src.evaluation.predictions.Predictions(
            pathway=pathway, metadata=self.__metadata, settings=self.__settings)

        streams = src.functions.streams.Streams()
        for field in self.__partitions._fields:

            # Predictions
            partition_: pd.DataFrame = ast.literal_eval(f'self.__partitions.{field}')
            generator_: tf.data.Dataset = ast.literal_eval(f'self.__generators.{field}')
            plausibilities = predictions.exc(model=model, partition_=partition_, generator_=generator_, name=field)

            # Truth
            truth = partition_[self.__metadata.labels].values

            # Error matrix frequencies
            data = src.evaluation.frequencies.Frequencies(
                thresholds=thresholds, plausibilities=plausibilities, truth=truth, classes=self.__metadata.labels)

            streams.write(blob=data, path=os.path.join(pathway, f'frequencies_{field}.csv'))

    def exc(self, model: tf.keras.Sequential, pathway: str):
        """
        
        :param model:
        :param pathway:
        :return:
        """

        assert np.setdiff1d(self.__generators._fields,
                            self.__partitions._fields).shape[0] == 0, 'There might be a set-up error w.r.t. modelling data'

        self.__predictions(model=model, pathway=pathway)
