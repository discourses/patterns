import os
import logging
import sys

import tensorflow as tf


def main():
    """

    :return:
    """

    logger.info('Patterns')

    # The machine has two GPU (graphics processing units) devices
    devices = tf.config.list_physical_devices('GPU')
    logger.info(devices)


if __name__ == '__main__':

    # Paths
    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'src'))

    # Logging
    logging.basicConfig(level=logging.INFO,
                        format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                        datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(__name__)

    main()