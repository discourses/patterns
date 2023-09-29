"""
The modelling steps for interface.py
"""
import src.modelling.hyperparameters
import src.modelling.architecture
import src.elements.attributes
import src.elements.generators
import src.elements.metadata
import src.elements.partitions

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

    def exc(self, generators: src.elements.generators.Generators, partitions: src.elements.partitions.Partitions):
        """
        
        :return:
        """

        index: int = 0

        for hpc in self.__hyperparameters:

            index = index + 1
            str(index).zfill(4)

            model = self.__architecture.exc(hpc=hpc, labels=self.__metadata.labels)
            print(type(model))
            print(generators._fields)
            print(partitions._fields)
