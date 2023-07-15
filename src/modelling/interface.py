"""
interface.py
"""
import logging

import config
import src.algorithms.descriptors
import src.functions.streams


class Interface:
    """
    Class Interface

    This class executes the series of modelling, evaluation, etc., steps.
    """
    Modelling = config.Config().Modelling
    Metadata = config.Config().Metadata

    def __init__(self):
        """
        Constructor
        """

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def exc(self):
        """

        :return:
        """
        
        descriptors = src.algorithms.descriptors.Descriptors()

        settings = self.Modelling(**descriptors.exc(node=['settings']))
        metadata = self.Metadata(**descriptors.exc(node=['metadata']))
        self.__logger.info(metadata)
        self.__logger.info(settings._fields)

        return src.functions.streams.Streams().api(
            uri=metadata.url, header=0)
