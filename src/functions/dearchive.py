import requests
import zipfile
import io
import os
import sys


class Archives:

    def __init__(self):
        """

        """

    def __directories(self):
        """

        :return:
        """

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

        objects = zipfile.ZipFile(io.BytesIO(request.content))
        objects.extractall(path=path)
