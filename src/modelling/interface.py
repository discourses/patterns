"""
interface.py
"""
import logging
import os

import src.functions.descriptors
import src.functions.streams
import src.register.sample


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

    def exc(self):
        """

        :return:
        """

        descriptors = src.functions.descriptors.Descriptors(
            path=os.path.join(os.getcwd(), 'descriptors', 'images.yml'))

        sample = src.register.sample.Sample(descriptors=descriptors).exc()
        self.__logger.info(sample)
