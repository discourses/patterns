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

    # Devices; the machine has two GPU (graphics processing units) devices
    tf.debugging.set_log_device_placement(True)
    devices = tf.config.list_physical_devices('GPU')
    try:
        tf.config.set_visible_devices(devices[0], 'GPU')
    except RuntimeError as err:
        raise ValueError(err) from err

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
