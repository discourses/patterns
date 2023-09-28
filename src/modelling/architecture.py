"""
The architecture of the deep learning model
"""
import tensorflow as tf

import src.elements.attributes


class Architecture:
    """
    The class Architecture
    """

    def __init__(self, attributes: src.elements.attributes.Attributes) -> None:
        """
        
        :param attributes:
        """

        # Data Classes
        self.__attributes = attributes

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

    def exc(self):
        """
        
        :return:
        """

        # The base#
        base = self.__baseline()

        print(base)
