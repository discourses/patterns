"""
sample.py
"""
import logging

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

    def __init__(self):
        """
        Constructor
        """

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(type(self).__name__)

    def __sample(self, settings: Settings, metadata: Metadata) -> pd.DataFrame:
        """

        :param settings:
        :param metadata:
        :return:
        """

        register = src.functions.streams.Streams().api(
            uri=metadata.url, header=0)
        self.__logger.info(register)

        return src.register.sampling.Sampling(
            settings=settings, metadata=metadata).exc(register=register)

    def exc(self, descriptors: src.functions.descriptors.Descriptors) -> pd.DataFrame:
        """

        :param descriptors:
        :return:
        """

        settings = self.Settings(**descriptors.exc(node=['settings']))
        metadata = self.Metadata(**descriptors.exc(node=['metadata']))

        return self.__sample(settings=settings, metadata=metadata)
