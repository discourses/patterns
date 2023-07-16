"""
pipeline.py
"""
import pandas as pd
import tensorflow as tf

import config


class Pipeline:
    """
    Class Pipeline

    Decodes the images that will be fed to a model, and instantiates the image delivery pipeline.  There are 2 options:
    Tensorflow's DataSets and Keras' ImageDataGenerator.  Google's performance exercise suggests that the former is
    much more efficient.
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

    def __decoding(self, img):
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

    def __pairing(self, filename: str, observation: str = None):
        """
        Create image & label pairs

        :param filename:
        :param observation:
        :return:
        """
        img = tf.io.read_file(filename)
        img = self.__decoding(img)

        if observation is None:
            return img
        else:
            return img, observation

    def exc(self, data: pd.DataFrame, predicting: bool):
        """
        Create image delivery pipeline

        :param data: The metadata table of the images
        :param predicting: Predicting?
        :return:
        """

        # The names, local uniform resource identifiers, of the image files
        filenames = data[self.__metadata.path].values

        # During prediction exercises the input data frame will not, should not, include ground truth data
        if predicting:
            matrices = filenames
        else:
            observations = data[self.__metadata.labels].values
            matrices = (filenames, observations)

        # Hence
        # 'cache/.../log'
        dataset = tf.data.Dataset.from_tensor_slices(matrices)
        dataset = dataset.map(self.__pairing, num_parallel_calls=tf.data.experimental.AUTOTUNE)
        dataset = dataset.cache()
        dataset = dataset.batch(batch_size=self.__settings.batch_size, drop_remainder=False)
        dataset = dataset.repeat()
        dataset = dataset.prefetch(buffer_size=tf.data.experimental.AUTOTUNE)

        return dataset
