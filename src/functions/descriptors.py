"""
descriptors.py
"""
import yaml


class Descriptors:
    """
    Class Descriptors

    Reads-in a YAML of maximum depth two
    """

    def __init__(self, path: str):

        # The expected location of the YAML
        self.__path = path

        # Get the stream of descriptors upon class instantiation
        self.__stream = self.__get_stream()

    def __get_stream(self) -> dict:
        """
        Reads a YAML file of descriptors.

        :return:
        """

        with open(file=self.__path, mode='r', encoding='UTF-8') as stream:
            try:
                return yaml.load(stream=stream, Loader=yaml.CLoader)
            except yaml.YAMLError as err:
                raise ValueError(err) from err

    def __excerpt(self, node: list) -> dict:
        """

        :param node: A node of interest.
        :return:
        """

        # The dictionary of keys in focus
        if len(node) == 1:
            dictionary: dict = self.__stream[node[0]]
        else:
            dictionary: dict = self.__stream[node[0]][node[1]]

        return dictionary

    def exc(self, node: list) -> dict:
        """

        :param node: A node of interest vis-à-vis descriptors
        :return:
        """

        return self.__excerpt(node=node)
