"""
Estimating a model's parameters
"""
import logging

import math

import tensorflow as tf

import src.elements.generators
import src.elements.partitions
import src.elements.settings
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

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)


    def __endpoints(self, pathway: str):
        """
        
        :return:
        """

        endpoints = src.evaluation.endpoints.Endpoints(settings=self.__settings)

        # Stopping
        early_stopping = endpoints.early_stopping()

        # Persisting Checkpoints
        model_checkpoint = endpoints.model_checkpoint(
            network_checkpoints_path=pathway)

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

    def exc(self, model: tf.keras.Sequential, pathway: str):
        """
        
        :param model: A tf.keras.Sequential model
        :param pathway: The directory wherein the model's check points will be saved
        :return:
        """

        early_stopping, model_checkpoint = self.__endpoints(pathway=pathway)

        history = self.__estimate(model=model, early_stopping=early_stopping, model_checkpoint=model_checkpoint)
        self.__logger.info(history)

        return history
