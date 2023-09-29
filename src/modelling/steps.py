"""
The modelling steps for interface.py
"""
import src.modelling.hyperparameters
import src.modelling.architecture
import src.elements.attributes
import src.elements.metadata

class Steps:
    """
    Class Steps
    """

    def __init__(self, attributes: src.elements.attributes.Attributes, metadata: src.elements.metadata.Metadata) -> None:
        """
        Constructor
        """

        self.__hyperparameters = src.modelling.hyperparameters.Hyperparameters().exc()
        self.__architecture = src.modelling.architecture.Architecture(attributes=attributes)
        self.__metadata = metadata

    def exc(self):
        """
        
        :return:
        """

        index: int = 0

        for hpc in self.__hyperparameters:

            index = index + 1
            str(index).zfill(4)

            model = self.__architecture.exc(hpc=hpc, labels=self.__metadata.labels)
            print(type(model))
