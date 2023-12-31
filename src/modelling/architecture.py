"""
The architecture of the deep learning model
"""

import logging

import tensorflow as tf

import src.elements.attributes
import src.elements.hpc


class Architecture:
    """
    The class Architecture
    """

    def __init__(self, attributes: src.elements.attributes.Attributes) -> None:
        """
        
        :param attributes: A set of image attributes
        """

        # Data Classes
        self.__attributes = attributes

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def __baseline(self):
        """
        Sets-up the baseline architecture

        :return:
        """

        # Base Model
        base = tf.keras.applications.VGG19(
            include_top=False,
            input_shape=(self.__attributes.columns, self.__attributes.rows, self.__attributes.channels),
            weights='imagenet')
        base.trainable = False

        return base

    def exc(self, hpc: src.elements.hpc.HPC, labels: list, metrics: list = None) -> tf.keras.Sequential:
        """
        
        :param hpc: A hyperparameters case
        :param labels: The classification labels
        :param metrics: The modelling metrics of interest
        :return:
        """

        # The base#
        base = self.__baseline()

        # Flattening Object
        flatten = tf.keras.layers.Flatten()

        # The fully connected layers
        alpha_units = tf.keras.layers.Dense(hpc.alpha_units, activation='relu', name='Alpha')
        alpha_dropout = tf.keras.layers.Dropout(rate=hpc.alpha_dropout, name='AlphaDropout')
        beta_units = tf.keras.layers.Dense(hpc.beta_units, activation='relu', name='Beta')
        beta_dropout = tf.keras.layers.Dropout(hpc.beta_dropout, name='BetaDropout')

        # The classification layer
        classifier = tf.keras.layers.Dense(len(labels), activation=tf.nn.softmax)

        # Build
        model = tf.keras.models.Sequential([base, flatten, alpha_units, alpha_dropout,
                                            beta_units, beta_dropout, classifier])

        # Labels. Case
        #       one-hot-code: categorical_crossentropy
        #       integers: sparse_categorical_crossentropy
        if metrics is None:
            model.compile(optimizer=hpc.opt,
                          loss=tf.keras.losses.categorical_crossentropy)
        else:
            model.compile(optimizer=hpc.opt,
                          metrics=metrics,
                          loss=tf.keras.losses.categorical_crossentropy)

        self.__logger.info(base.summary())
        self.__logger.info(model.summary())
        self.__logger.info(type(model))

        return model
