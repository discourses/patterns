"""
sample.py
"""
import logging
import os
import glob

import pandas as pd

import config
import src.functions.descriptors
import src.functions.streams
import src.register.sampling


class Sample:
    """
    Class Sample
    """

    Settings = config.Config().Settings
    Metadata = config.Config().Metadata
    Source = config.Config().Source

    def __init__(self, descriptors: src.functions.descriptors.Descriptors):
        """

        :param descriptors:
        """

        self.__settings = self.Settings(**descriptors.exc(node=['settings']))
        self.__metadata = self.Metadata(**descriptors.exc(node=['metadata']))
        self.__source = self.Source(**descriptors.exc(node=['data', 'source']))

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(type(self).__name__)

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

    def __restructure(self, register: pd.DataFrame) -> pd.DataFrame:
        """

        :param register:
        :return:
        """

        paths = glob.glob(pathname=os.path.join(os.getcwd(), *self.__source.directory, '*.png'))
        frame = pd.DataFrame(data={'path': paths})
        frame.loc[:, 'name'] = frame.copy()['path'].apply(lambda x: os.path.split(x)[1])

        frame = frame.copy().merge(register, how='inner', on='name')

        return frame

    def exc(self) -> pd.DataFrame:
        """

        :return:
        """

        register = self.__register()
        register = self.__sample(register=register.copy())
        register = self.__restructure(register=register.copy())

        return register
