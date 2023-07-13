import logging
import os
import sys

import dask
import numpy as np


def main():
    """

    :return:
    """

    endpoint = 'https://github.com/greyhypotheses/dermatology/raw/master/augmentations/images/{name}.zip'
    strings = [endpoint.format(name=str(number).zfill(3)) for number in np.arange(0, 196)]
    logger.info(strings)

    images = [dask.delayed(dearchive.exc)(url=string) for string in strings]
    dask.compute(images, scheduler='threads')


if __name__ == '__main__':

    # Paths
    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'src'))

    # Threads
    os.environ['NUMEXPR_MAX_THREADS'] = '12'

    # Logging
    logging.basicConfig(level=logging.INFO,
                        format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                        datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(__name__)

    # Classes
    import src.functions.dearchive

    # Instances
    dearchive = src.functions.dearchive.Dearchive(path=os.path.join(os.getcwd(), 'images'))

    main()
