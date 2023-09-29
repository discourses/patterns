"""
The modelling steps for interface.py
"""
import src.modelling.hyperparameters

class Steps:
    """
    Class Steps
    """

    def __init__(self) -> None:
        """
        Constructor
        """

        self.__hyperparameters = src.modelling.hyperparameters.Hyperparameters().exc()

    def exc(self):
        """
        
        :return:
        """

        index: int = 0

        for hpc in self.__hyperparameters:

            index = index + 1
            str(index).zfill(4)

            hpc
