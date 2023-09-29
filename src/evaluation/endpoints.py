"""
Model points
"""

import os

import tensorflow as tf

import src.elements.settings


class Endpoints:
    """
    Class Endpoints
    """

    def __init__(self, settings: src.elements.settings.Settings) -> None:
        """
        
        :param settings:
        """

        self.__settings = settings

    def early_stopping(self):
        """
        
        :return:
        """

        return tf.keras.callbacks.EarlyStopping(
            monitor='val_loss', verbose=1, patience=self.__settings.early_stopping_patience,
            mode='min', restore_best_weights=True)

    @staticmethod
    def model_checkpoint(network_checkpoints_path: str):
        """
        
        :param network_checkpoints_path:
        :return:
        """

        return tf.keras.callbacks.ModelCheckpoint(
            filepath=os.path.join(network_checkpoints_path, 'model_{epoch}.h5'),
            monitor='val_loss', verbose=1, save_best_only=False, save_weights_only=False,
            mode='auto', save_freq='epoch')
