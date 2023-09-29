"""
losses.py structures and saves a models loss calculations 
"""
import os

import numpy as np
import pandas as pd


class Losses:
    """
    The losses class
    """

    def __init__(self) -> None:
        pass

    def exc(self, history, path):
        """
        
        :param history:
        :param path:
        :return:
        """

        numbers = np.array([history.epoch, history.history['loss'], history.history['val_loss']]).T

        frame = pd.DataFrame(data=numbers, columns=['epoch', 'training_loss', 'validation_loss'])
        frame.loc[:, 'epoch'] = frame['epoch'].astype(dtype=int)
        frame.to_csv(path_or_buf=os.path.join(path, 'history.csv'), header=True, index=False, encoding='utf-8')
