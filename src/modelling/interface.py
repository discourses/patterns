"""
interface.py
"""
import logging

import src.algorithms.descriptors
import src.elements.attributes
import src.elements.generators
import src.elements.metadata
import src.elements.partitions
import src.elements.settings
import src.elements.source
import src.functions.directories
import src.functions.streams
import src.modelling.pipeline
import src.modelling.splits
import src.modelling.steps
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

    def __directories(self):
        """
        
        :return:
        """

        src.functions.directories.Directories().cleanup(
            path=self.__settings.model_checkpoints_directory)


    def __generators(self, partitions: src.elements.partitions.Partitions) -> src.elements.generators.Generators:
        """
        
        :params partitions: The training, validation, and testing data partitions
        :return:
        """

        training = self.__pipeline.exc(data=partitions.training, testing=False)
        validating = self.__pipeline.exc(data=partitions.validating, testing=False)
        testing = self.__pipeline.exc(data=partitions.testing, testing=True)

        return src.elements.generators.Generators(
            training=training, validating=validating, testing=testing)

    def exc(self):
        """

        :return:
        """

        # Clear outputs directory
        self.__directories()

        # Get a sample of image names.  In general, there are more than 60,000 images, and
        # it is an imbalanced set of images.
        sample = src.sampling.interface.Interface(
            settings=self.__settings, metadata=self.__metadata, source=self.__source).exc()

        partitions = src.modelling.splits.Splits(
            settings=self.__settings, metadata=self.__metadata).exc(sample=sample)

        generators = self.__generators(partitions=partitions)

        # Preview
        self.__logger.info('training %s, validating %s, testing %s',
                           partitions.training.shape, partitions.validating.shape, partitions.testing.shape)

        self.__logger.info('training: %s\nvalidating: %s\ntesting: %s', generators.training.element_spec,
                           generators.validating.element_spec, generators.testing.element_spec)

        # Steps
        src.modelling.steps.Steps(
            attributes=self.__attributes, metadata=self.__metadata, settings=self.__settings).exc(
                generators=generators, partitions=partitions)
