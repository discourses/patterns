"""
sample.py
"""
import glob
import os

import pandas as pd

import src.algorithms.descriptors
import src.functions.streams
import src.sampling.sample

import src.types.settings
import src.types.metadata
import src.types.source


class Interface:
    """
    Class Sample
    """

    

    def __init__(self, settings: src.types.settings.Settings,
                 metadata: src.types.metadata.Metadata,
                 source: src.types.source.Source):
        """

        :param settings:
        :param metadata:
        :param source:
        """

        # Descriptors
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

        return src.sampling.sample.Sample(
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
