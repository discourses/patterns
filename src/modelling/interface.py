"""
interface.py
"""
import logging
import os

import config
import src.functions.descriptors
import src.functions.streams
import src.modelling.splits
import src.register.sample


class Interface:
    """
    Class Interface

    This class executes the series of modelling, evaluation, etc., steps.
    """

    Settings = config.Config().Settings
    Metadata = config.Config().Metadata
    Source = config.Config().Source
    Attributes = config.Config().Attributes

    def __init__(self):
        """
        Constructor
        """

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

        # Descriptors
        self.__settings, self.__metadata, self.__source, self.__attributes = self.__descriptors()

    def __descriptors(self):
        """

        :return:
        """

        descriptors = src.functions.descriptors.Descriptors(
            path=os.path.join(os.getcwd(), 'descriptors', 'images.yml'))

        settings = self.Settings(**descriptors.exc(node=['settings']))
        metadata = self.Metadata(**descriptors.exc(node=['metadata']))
        source = self.Source(**descriptors.exc(node=['data', 'source']))
        attributes = self.Attributes(**descriptors.exc(node=['data', 'attributes']))

        return settings, metadata, source, attributes

    def exc(self):
        """

        :return:
        """

        sample = src.register.sample.Sample(
            settings=self.__settings, metadata=self.__metadata, source=self.__source).exc()
        self.__logger.info(sample)

        partitions = src.modelling.splits.Splits(settings=self.__settings, metadata=self.__metadata).exc(sample=sample)
        self.__logger.info(partitions.training)
        self.__logger.info(partitions.validating)
        self.__logger.info(partitions.testing)
