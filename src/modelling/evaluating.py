"""
For evaluating various aspects of a model
"""
import ast

import pandas as pd
import tensorflow as tf

import src.elements.generators
import src.elements.metadata
import src.elements.partitions
import src.elements.settings
import src.evaluation.predictions


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

    def exc(self, model: tf.keras.Sequential, identifier: str):
        """
        
        :return:
        """

        print(self.__settings._fields)
        print(self.__generators._fields)
        print(self.__partitions._fields)

        predictions = src.evaluation.predictions.Predictions(
            identifier=identifier, metadata=self.__metadata, settings=self.__settings)

        for field in self.__partitions._fields:

            partition_: pd.DataFrame = ast.literal_eval(f'self.__partitions.{field}')
            generator_: tf.data.Dataset = ast.literal_eval(f'self.__generators.{field}')
            predictions.exc(model=model, partition_=partition_, generator_=generator_, name=field)
