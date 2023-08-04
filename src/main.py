"""
main.py
"""
import logging
import os
import sys
import tensorflow as tf


def main():
    """
    Entry point

    :return:
    """

    logger.info('Patterns')

    # If True, download the online images ...
    if DOWNLOAD:
        src.images.interface.Interface().exc()

    # Proceed
    src.modelling.interface.Interface().exc()


if __name__ == '__main__':

    # Paths
    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'src'))

    # Threads
    os.environ['NUMEXPR_MAX_THREADS'] = '13'

    # Logging
    logging.basicConfig(level=logging.INFO,
                        format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                        datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(__name__)

    # Classes
    import src.images.interface
    import src.modelling.interface

    # Later, the arguments
    DOWNLOAD = False

    main()
