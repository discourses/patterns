
"""
Predicting with respect to a model
"""
import math
import os

import pandas as pd
import tensorflow as tf

import src.elements.generators
import src.elements.metadata
import src.elements.partitions
import src.elements.settings
import src.functions.streams


class Predictions:
    """
    Class Predictions
    """

    def __init__(self, identifier: str, metadata: src.elements.metadata.Metadata,
                 settings: src.elements.settings.Settings) -> None:
        """
        
        :param identifier:
        :param metadata:
        :param settings:
        """
        
        self.__identifier = identifier
        self.__metadata = metadata
        self.__settings = settings

    def __write(self, blob: pd.DataFrame, name: str):
        """
        
        :param blob:
        :param name:
        :return:
        """

        return src.functions.streams.Streams().write(
            blob=blob,
            path=os.path.join(self.__settings.model_checkpoints_directory, self.__identifier, f'{name}_predictions.csv'))

    def exc(self, model: tf.keras.Sequential, partition_: pd.DataFrame, generator_: tf.data.Dataset,
            name: str):
        """
        
        :param model:
        """

        steps = math.ceil(partition_.shape[0] / self.__settings.batch_size)

        plausibilities = model.predict(generator_, steps=steps)

        # Save
        frame = pd.DataFrame(data=plausibilities, columns=self.__metadata.labels)
        frame = partition_.join(frame.copy())
        self.__write(blob=frame, name=name)

        return plausibilities
