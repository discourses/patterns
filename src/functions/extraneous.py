"""
extraneous.py
"""
import logging
import pathlib
import shutil


class Extraneous:

    def __init__(self) -> None:
        """
        
        """
        
        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def exc(self):
        """
        Deletes all __pycache__ directories
        """

        for path in pathlib.Path.cwd().rglob('__pycache__'):
            if path.is_dir():
                try:
                    shutil.rmtree(path=path, ignore_errors=True)
                except PermissionError:
                    raise Exception(f'Delete Permission Denied: {path}')
                else:
                    self.__logger.info(f'Deleted: {path}')
