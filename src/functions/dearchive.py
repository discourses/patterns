import io
import zipfile

import requests

import src.functions.directories


class Dearchive:

    def __init__(self):
        """

        """

        self.__directories = src.functions.directories.Directories()

    def __setup(self, path: str):
        """

        :param path: A local directory path
        :return:
        """

        self.__directories.cleanup(path=path)
        self.__directories.create(path=path)

    def exc(self, url: str, path: str):
        """

        :param url: The URL (uniform resource locator) of an online archive of images
        :param path: A local directory path for the unzipped set of files
        :return:
        """

        try:
            request = requests.get(url=url)
        except requests.HTTPError as err:
            raise Exception(err)

        self.__setup(path=path)
        objects = zipfile.ZipFile(io.BytesIO(request.content))
        objects.extractall(path=path)
