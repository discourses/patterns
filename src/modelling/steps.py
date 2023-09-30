"""
The modelling steps for interface.py
"""

import src.modelling.estimating
import src.modelling.hyperparameters
import src.modelling.architecture

import src.elements.attributes
import src.elements.settings
import src.elements.generators
import src.elements.metadata
import src.elements.partitions

class Steps:
    """
    Class Steps
    """

    def __init__(self, attributes: src.elements.attributes.Attributes, metadata: src.elements.metadata.Metadata, 
                 settings: src.elements.settings.Settings) -> None:
        """
        Constructor
        """

        self.__metadata = metadata
        self.__settings = settings

        # The deep learning architecture of interest
        self.__architecture = src.modelling.architecture.Architecture(attributes=attributes)

        # A list of hyperparameter collections for training the deep learning model
        self.__hyperparameters = src.modelling.hyperparameters.Hyperparameters().exc()

    def exc(self, generators: src.elements.generators.Generators, partitions: src.elements.partitions.Partitions):
        """
        
        :return:
        """

        estimating = src.modelling.estimating.Estimating(
            settings=self.__settings, generators=generators, partitions=partitions)

        index: int = 0

        for hpc in self.__hyperparameters:

            index = index + 1
            identifier = str(index).zfill(4)

            model = self.__architecture.exc(hpc=hpc, labels=self.__metadata.labels)

            history = estimating.exc(model=model, identifier=identifier)

            print(history)
