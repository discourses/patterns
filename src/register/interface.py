"""
sample.py
"""
import glob
import os

import pandas as pd

import config
import src.algorithms.descriptors
import src.functions.streams
import src.register.sampling


class Sample:
    """
    Class Sample
    """

    Settings = config.Config().Settings
    Metadata = config.Config().Metadata
    Source = config.Config().Source

    def __init__(self, settings: Settings, metadata: Metadata, source: Source):
        """

        :param settings:
        :param metadata:
        :param source:
        """

        self.__settings = settings
        self.__metadata = metadata
        self.__source = source

    def __register(self) -> pd.DataFrame:
        """

        :return:
        """

        return src.functions.streams.Streams().api(
            uri=self.__metadata.url, header=0)

    def __sample(self, register: pd.DataFrame) -> pd.DataFrame:
        """

        :param register:
        :return:
        """

        return src.register.sampling.Sampling(
            settings=self.__settings, metadata=self.__metadata).exc(register=register)

    def __append_paths(self, register: pd.DataFrame) -> pd.DataFrame:
        """

        :param register:
        :return:
        """

        paths = glob.glob(pathname=os.path.join(os.getcwd(), *self.__source.directory, '*.png'))
        frame = pd.DataFrame(data=paths, columns=[self.__metadata.path])
        frame.loc[:, 'name'] = frame.copy()[self.__metadata.path].apply(lambda x: os.path.split(x)[1])

        frame = frame.copy().merge(register, how='inner', on='name')

        return frame

    def exc(self) -> pd.DataFrame:
        """

        :return:
        """

        register = self.__register()
        register = self.__sample(register=register.copy())
        register = self.__append_paths(register=register.copy())

        return register
