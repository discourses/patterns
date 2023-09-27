"""
pipeline.py
"""

import pandas as pd
import tensorflow as tf

import src.elements.attributes
import src.elements.metadata
import src.elements.settings


class Pipeline:
    """
    Class Pipeline

    Decodes the images that will be fed to a model, and instantiates the image delivery pipeline.  There are 2 options:
    Tensorflow's DataSets and Keras' ImageDataGenerator.  Google's performance exercise suggests that the former is
    much more efficient.
    """

    def __init__(self, attributes: src.elements.attributes.Attributes, metadata: src.elements.metadata.Metadata, 
                 settings: src.elements.settings.Settings):
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
    def __doublet(self, filename: str, observation: str):
        """
        Create image & label pairs

        :param filename:
        :param observation:
        :return:
        """
        img = tf.io.read_file(filename)
        img = self.__decoding(img)

        return img, observation

    @tf.autograph.experimental.do_not_convert
    def __single(self, filename: str):
        """

        :param filename:
        :return:
        """

        img = tf.io.read_file(filename)
        img = self.__decoding(img)

        return img

    def exc(self, data: pd.DataFrame, testing: bool):
        """
        Create image delivery pipeline

        :param data: The metadata table of the images
        :param testing: Testing?
        :return:
        """

        # The names, local uniform resource identifiers, of the image files
        filenames = data[self.__metadata.path].values

        # Whilst testing, serving, the input tensor will not, should not, include ground truth data
        if testing:
            matrices = filenames
        else:
            observations = data[self.__metadata.labels].values
            matrices = (filenames, observations)

        # Hence
        # 'cache/.../log'
        dataset = tf.data.Dataset.from_tensor_slices(matrices)
        if testing:
            dataset = dataset.map(self.__single, num_parallel_calls=tf.data.AUTOTUNE)
        else:
            dataset = dataset.map(self.__doublet, num_parallel_calls=tf.data.AUTOTUNE)
        dataset = dataset.cache()
        dataset = dataset.batch(batch_size=self.__settings.batch_size, drop_remainder=False)
        if not testing:
            dataset = dataset.repeat()
        dataset = dataset.prefetch(buffer_size=tf.data.experimental.AUTOTUNE)

        return dataset
