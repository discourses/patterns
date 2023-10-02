"""
The modelling steps for interface.py
"""
import os

import src.elements.attributes
import src.elements.generators
import src.elements.metadata
import src.elements.partitions
import src.elements.settings
import src.evaluation.losses
import src.modelling.architecture
import src.modelling.estimating
import src.modelling.hyperparameters
import src.modelling.performance


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

        # Instances
        estimating = src.modelling.estimating.Estimating(
            settings=self.__settings, generators=generators, partitions=partitions)
        losses = src.evaluation.losses.Losses()

        # Modelling, etc.
        index: int = 0
        for hpc in self.__hyperparameters:

            # A directory name per hyperparameter set
            index = index + 1
            identifier = str(index).zfill(4)
            pathway = os.path.join(self.__settings.model_checkpoints_directory, identifier)

            # A model architecture vis-à-vis the hyperparameter set
            model = self.__architecture.exc(hpc=hpc, labels=self.__metadata.labels)

            # Model training, i.e., estimation of model parameters
            history = estimating.exc(model=model, pathway=pathway)

            # History of losses
            losses.exc(history=history, path=pathway)

            # Predictions and frequencies
            src.modelling.performance.Performance(
                metadata=self.__metadata, settings=self.__settings, model=model, pathway=pathway).exc(
                    generators=generators, partitions=partitions)
