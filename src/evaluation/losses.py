"""
losses.py structures and saves a models loss calculations 
"""

import logging
import os

import numpy as np
import pandas as pd

import src.functions.streams


class Losses:
    """
    The losses class
    """

    def __init__(self) -> None:
        """
        Constructor
        """

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def __write(self, blob: pd.DataFrame, path: str) -> str:
        """
        
        :param blob:
        :param path:
        :return:
            message
        """

        return src.functions.streams.Streams().write(
            blob=blob, path=os.path.join(path, 'history.csv'))

    def exc(self, history, path):
        """
        
        :param history: A model's history of loss calculations per epoch
        :param path: The directory wherein the history data will be saved
        :return:
        """

        # The epoch & loss values
        numbers = np.array([history.epoch, history.history['loss'], history.history['val_loss']]).T

        # In data frame form
        frame = pd.DataFrame(data=numbers, columns=['epoch', 'training_loss', 'validation_loss'])
        frame.loc[:, 'epoch'] = frame['epoch'].astype(dtype=int)

        # Persist
        message = self.__write(blob=frame, path=path)
        self.__logger.info(message)
