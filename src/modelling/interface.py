"""
interface.py
"""
import logging

import src.algorithms.descriptors
import src.elements.attributes
import src.elements.metadata
import src.elements.settings
import src.elements.source
import src.functions.streams
import src.modelling.pipeline
import src.modelling.splits
import src.sampling.interface


class Interface:
    """
    Class Interface

    This class executes the series of modelling, evaluation, etc., steps.
    """

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
        self.__attributes = src.elements.attributes.Attributes()
        self.__metadata = src.elements.metadata.Metadata()
        self.__settings = src.elements.settings.Settings()
        self.__source = src.elements.source.Source()

        # Pipeline Objects
        self.__pipeline = src.modelling.pipeline.Pipeline(
            attributes=self.__attributes, metadata=self.__metadata, settings=self.__settings)

    def exc(self):
        """

        :return:
        """

        sample = src.sampling.interface.Interface(
            settings=self.__settings, metadata=self.__metadata, source=self.__source).exc()
        self.__logger.info(sample)

        partitions = src.modelling.splits.Splits(
            settings=self.__settings, metadata=self.__metadata).exc(sample=sample)
        self.__logger.info('Training %s, Validating %s, Testing %s',
                           partitions.training.shape, partitions.validating.shape, partitions.testing.shape)

        training = self.__pipeline.exc(data=partitions.training, testing=False)
        validating = self.__pipeline.exc(data=partitions.validating, testing=False)
        testing = self.__pipeline.exc(data=partitions.testing, testing=True)
        self.__logger.info(training.element_spec)
        self.__logger.info(validating.element_spec)
        self.__logger.info(testing.element_spec)
