"""
Estimating a model's parameters
"""

import os
import math

import tensorflow as tf

import src.elements.settings
import src.elements.generators
import src.elements.partitions
import src.evaluation.endpoints


class Estimating:
    """
    Class Estimating
    """

    def __init__(self, settings: src.elements.settings.Settings,
                 generators: src.elements.generators.Generators,
                 partitions: src.elements.partitions.Partitions) -> None:
        """
        
        :param settings:
        """

        self.__settings = settings
        self.__generators = generators
        self.__partitions = partitions


    def __endpoints(self, identifier: str):
        """
        
        :return:
        """

        endpoints = src.evaluation.endpoints.Endpoints(settings=self.__settings)

        # Stopping
        early_stopping = endpoints.early_stopping()

        # Persisting Checkpoints
        model_checkpoint = endpoints.model_checkpoint(
            network_checkpoints_path=os.path.join(self.__settings.model_checkpoints_directory, identifier))

        return early_stopping, model_checkpoint

    def __estimate(self, model: tf.keras.Sequential, early_stopping: tf.keras.callbacks.EarlyStopping, 
                   model_checkpoint: tf.keras.callbacks.ModelCheckpoint):
        """
        
        :param model:
        :return:
        """

        # Steps per epoch
        steps_per_epoch = math.ceil(self.__partitions.training.shape[0] / self.__settings.batch_size)

        # Validation steps
        validation_steps = math.ceil(self.__partitions.validating.shape[0] / self.__settings.batch_size)

        history = model.fit_generator(
            generator=self.__generators.training, steps_per_epoch=steps_per_epoch, epochs=self.__settings.epochs,
            verbose=1, callbacks=[early_stopping, model_checkpoint], validation_data=self.__generators.validating,
            validation_steps=validation_steps, validation_freq=1)

        return history

    def exc(self, model: tf.keras.Sequential, identifier: str):
        """
        
        :param model:
        :param identifier:
        :return:
        """

        early_stopping, model_checkpoint = self.__endpoints(identifier=identifier)

        history = self.__estimate(model=model, early_stopping=early_stopping, model_checkpoint=model_checkpoint)

        return history
