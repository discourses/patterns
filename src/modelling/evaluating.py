"""
For evaluating various aspects of a model
"""
import src.elements.generators
import src.elements.partitions
import src.elements.settings


class Evaluating:
    """
    Class Evaluating
    """

    def __init__(self, settings: src.elements.settings.Settings,
                 generators: src.elements.generators.Generators,
                 partitions: src.elements.partitions.Partitions) -> None:
        """

        :param settings:
        :param generators:
        :param partitions:
        :return:        
        """

        self.__settings = settings
        self.__generators = generators
        self.__partitions = partitions

    def exc(self):
        """
        
        :return:
        """

        print(self.__settings._fields)
        print(self.__generators._fields)
        print(self.__partitions._fields)
