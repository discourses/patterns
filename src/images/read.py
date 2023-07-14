"""
read.py
"""
import os

import dask

import src.functions.dearchive


class Read:
    """
    Class Read
    """

    def __init__(self):
        """
        Constructor
        """

        self.__dearchive = src.functions.dearchive.Dearchive(path=os.path.join(os.getcwd(), 'images'))

    @dask.delayed
    def __executing(self, url) -> str:
        """

        :param url:
        :return:
        """

        return self.__dearchive.external(url=url)

    def exc(self, strings: list[str]) -> list:
        """

        :param strings:
        :return:
        """

        # Get Images
        computations = []
        for string in strings[:12]:
            message = self.__executing(url=string)
            computations.append(message)
        messages = dask.compute(computations, scheduler='threads')[0]

        return messages
