"""
dearchive.py
"""
import io
import os.path
import zipfile

import requests

import src.functions.directories


class Dearchive:
    """
    Class Dearchive
    """

    def __init__(self, path: str):
        """

        :param path: A local directory path for the unzipped set of files
        """

        self.__path = path
        self.__setup(path=self.__path)

    @staticmethod
    def __setup(path: str):
        """

        :param path: A local directory path
        :return:
        """

        directories = src.functions.directories.Directories()
        directories.cleanup(path=path)
        directories.create(path=path)

    def external(self, url: str) -> str:
        """

        :param url: The URL (uniform resource locator) of an online archive of images
        :return:
        """

        try:
            request = requests.get(url=url)
        except requests.HTTPError as err:
            raise Exception(err)

        objects = zipfile.ZipFile(io.BytesIO(request.content))
        objects.extractall(path=self.__path)

        return f'{os.path.basename(url)}'
