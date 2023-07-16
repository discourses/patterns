"""
interface.py
"""
import logging
import os

import config
import src.functions.descriptors
import src.functions.splitting
import src.functions.streams
import src.register.sample


class Interface:
    """
    Class Interface

    This class executes the series of modelling, evaluation, etc., steps.
    """

    Settings = config.Config().Settings
    Metadata = config.Config().Metadata
    Source = config.Config().Source

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
        self.__settings, self.__metadata, self.__source = self.__descriptors()

        # Instances
        self.__splitting = src.functions.splitting.Splitting(random_state=self.__settings.random_state)

    def __descriptors(self):
        """

        :return:
        """

        descriptors = src.functions.descriptors.Descriptors(
            path=os.path.join(os.getcwd(), 'descriptors', 'images.yml'))

        settings = self.Settings(**descriptors.exc(node=['settings']))
        metadata = self.Metadata(**descriptors.exc(node=['metadata']))
        source = self.Source(**descriptors.exc(node=['data', 'source']))

        return settings, metadata, source

    def exc(self):
        """

        :return:
        """

        sample = src.register.sample.Sample(
            settings=self.__settings, metadata=self.__metadata, source=self.__source).exc()
        self.__logger.info(sample)

        training, evaluating = self.__splitting.exc(
            independent=sample['path'], dependent=sample[self.__metadata.labels],
            train_size=self.__settings.train_size_initial, stratify=sample[self.__metadata.labels])

        validating, testing = self.__splitting.exc(
            independent=evaluating['path'], dependent=evaluating[self.__metadata.labels],
            train_size=self.__settings.train_size_evaluation, stratify=evaluating[self.__metadata.labels])

        self.__logger.info(f'{training.shape}')
        self.__logger.info(f'{validating.shape}')
        self.__logger.info(f'{testing.shape}')

        self.__logger.info(training.head())
        self.__logger.info(validating.head())
        self.__logger.info(testing.head())
