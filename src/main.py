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

    # The machine has two GPU (graphics processing units) devices
    devices = tf.config.list_physical_devices('GPU')
    logger.info(devices)

    # If True, download the online images ...
    if download:
        src.images.interface.Interface().exc()


if __name__ == '__main__':
    """
    Initially
    """

    # Paths
    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'src'))

    # Threads
    os.environ['NUMEXPR_MAX_THREADS'] = '8'

    # Logging
    logging.basicConfig(level=logging.INFO,
                        format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                        datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(__name__)

    # Classes
    import src.images.interface

    # Later, the arguments
    download = True

    main()
