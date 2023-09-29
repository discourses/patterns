"""
Estimating a model's parameters
"""

import src.elements.settings


class Estimating:
    """
    Class Estimating
    """

    def __init__(self, settings: src.elements.settings.Settings) -> None:
        """
        
        :param settings:
        """

        self.__batch_size = settings.batch_size
        self.__early_stopping_patience = settings.early_stopping_patience

    def network(self):
        """
        
        :return:
        """

        print(self.__batch_size)
        print(self.__early_stopping_patience)
