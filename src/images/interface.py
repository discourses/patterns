"""
interface.py
"""
import logging

import numpy as np

import src.images.read


class Interface:
    """
    Class Interface
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

        # The URL strings of the images zip files
        self.__endpoint = 'https://github.com/greyhypotheses/dermatology/raw/master/augmentations/images/{name}.zip'

    def exc(self):
        """

        :return:
        """

        strings = [self.__endpoint.format(name=str(number).zfill(3)) for number in np.arange(0, 16)]
        self.__logger.info(strings)

        messages = src.images.read.Read().exc(strings=strings)
        self.__logger.info(messages)
