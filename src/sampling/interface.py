"""
sample.py
"""
import glob
import os

import pandas as pd

import src.algorithms.descriptors
import src.elements.metadata
import src.elements.settings
import src.elements.source
import src.functions.streams
import src.sampling.sample


class Interface:
    """
    Class Sample
    """

    def __init__(self, settings: src.elements.settings.Settings,
                 metadata: src.elements.metadata.Metadata,
                 source: src.elements.source.Source):
        """

        :param settings:
        :param metadata:
        :param source:
        """

        # Descriptors
        self.__settings = settings
        self.__metadata = metadata
        self.__source = source

    def __registry(self) -> pd.DataFrame:
        """
        Reads-in the registry of skin cancer images

        :return:
        """

        dtype = {label: bool for label in self.__metadata.labels}

        return src.functions.streams.Streams().api(
            uri=self.__metadata.url, header=0, dtype=dtype)

    def __sample(self, registry: pd.DataFrame) -> pd.DataFrame:
        """
        Retrieves a sample image names from the registry.  The number of images retrieved depends on
        the -sample size per class- setting.
        (ref. (a) images.yml, class_sample_size, (b) src.elements.settings)

        :param registry:
        :return:
        """

        return src.sampling.sample.Sample(
            settings=self.__settings, metadata=self.__metadata).exc(registry=registry)

    def __append_paths(self, sample: pd.DataFrame) -> pd.DataFrame:
        """
        Per record, this method records the local location of an image, alongside the image name 
        and other characteristics.

        :param registry:
        :return:
        """

        paths = glob.glob(pathname=os.path.join(*self.__source.directory, '*.png'))
        frame = pd.DataFrame(data=paths, columns=[self.__metadata.path])
        frame.loc[:, 'name'] = frame.copy()[self.__metadata.path].apply(lambda x: os.path.split(x)[1])

        frame = frame.copy().merge(sample, how='inner', on='name')

        return frame

    def exc(self) -> pd.DataFrame:
        """

        :return:
        """

        registry = self.__registry()
        sample = self.__sample(registry=registry.copy())
        sample = self.__append_paths(sample=sample.copy())

        return sample
