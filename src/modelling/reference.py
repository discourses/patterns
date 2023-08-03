"""
reference.py
"""
import numpy as np
import pandas as pd
import tensorflow as tf

import config


class Reference:
    """
    
    """

    Attributes = config.Config().Attributes
    Metadata = config.Config().Metadata
    Settings = config.Config().Settings
    Partitions = config.Config().Partitions

    def __init__(self, attributes: Attributes, metadata: Metadata, settings: Settings):
        """

        :param attributes:
        :param metadata:
        :param settings:
        """

        self.__attributes = attributes
        self.__metadata = metadata
        self.__settings = settings

    def __decoding(self, img) -> tf.Tensor:
        """
        Image decoder

        :param img:
        :return:
        """

        # Convert the compressed image to a 3D uint8 tensor
        img = tf.image.decode_png(contents=img, channels=self.__attributes.channels)

        # This step converts the image tensor values to floats in the [0, 1] range.
        img = tf.image.convert_image_dtype(img, tf.float32)

        # Hence
        return img
    
    @tf.autograph.experimental.do_not_convert
    def __single(self, filename: str):
        """

        :param filename:
        :return:
        """

        img = tf.io.read_file(filename)
        img = self.__decoding(img)

        return img

    def exc(self, data: pd.DataFrame):
        
        # The names, local uniform resource identifiers, of the image files
        filenames = data[self.__metadata.path].array

        dataset = tf.data.Dataset.from_tensor_slices(filenames)
        dataset = dataset.map(self.__single, num_parallel_calls=tf.data.AUTOTUNE)
        dataset = dataset.cache()
        dataset = dataset.batch(batch_size=self.__settings.batch_size, drop_remainder=False)
        dataset = dataset.prefetch(buffer_size=tf.data.experimental.AUTOTUNE)

        return dataset
