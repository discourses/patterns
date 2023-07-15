"""
interface.py
"""
import logging

import config
import src.algorithms.descriptors


class Interface:
    """
    Class Interface

    This class executes the series of modelling, evaluation, etc., steps.
    """
    Modelling = config.Config().Modelling

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

        objects = src.algorithms.descriptors.Descriptors().exc(node=['modelling'])
        attributes = self.Modelling(**objects)
        self.__logger.info(attributes._fields)
