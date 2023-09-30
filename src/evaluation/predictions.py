
"""
Predicting with respect to a model
"""
import math
import os

import numpy as np
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

    def __init__(self, pathway: str, metadata: src.elements.metadata.Metadata,
                 settings: src.elements.settings.Settings) -> None:
        """
        
        :param pathway:
        :param metadata:
        :param settings:
        """

        self.__pathway = pathway
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
            path=os.path.join(self.__pathway, f'{name}_predictions.csv'))

    def exc(self, model: tf.keras.Sequential, partition_: pd.DataFrame, generator_: tf.data.Dataset,
            name: str) -> np.ndarray:
        """
        
        :param model:
        """

        steps = math.ceil(partition_.shape[0] / self.__settings.batch_size)

        plausibilities: np.ndarray = model.predict(generator_, steps=steps)

        # Save
        frame = pd.DataFrame(data=plausibilities, columns=self.__metadata.labels)
        frame = partition_.join(frame.copy())
        self.__write(blob=frame, name=name)

        return plausibilities
