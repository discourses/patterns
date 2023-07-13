import requests
import zipfile
import io
import os
import sys

import src.functions.directories


class Dearchive:

    def __init__(self):
        """

        """

        self.__directories = src.functions.directories.Directories()

    def __setup(self, path: str):
        """

        :return:
        """

        self.__directories.cleanup(path=path)
        self.__directories.create(path=path)

    def exc(self, url: str, path: str):
        """

        :param url:
        :param path:
        :return:
        """

        try:
            request = requests.get(url=url)
        except requests.HTTPError as err:
            raise Exception(err)

        self.__setup(path=path)
        objects = zipfile.ZipFile(io.BytesIO(request.content))
        objects.extractall(path=path)
