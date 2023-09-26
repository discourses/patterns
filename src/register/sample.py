"""
sample.py
"""
import logging

import pandas as pd

import config


class Sample:
    """
    Class Sample

    Extracts a sample from the register of images; it ensures an appropriate sample size per class
    by comparing the -number of records per label- & -sample size requested-
    """

    Settings = config.Config().Settings
    Metadata = config.Config().Metadata

    def __init__(self, settings: Settings, metadata: Metadata):
        """
        Constructor

        :param settings:
        :param metadata:
        """

        self.__settings = settings
        self.__metadata = metadata

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def __sample_size(self, n_per_label: pd.Series) -> int:
        """
        If sampling without replacement is required, but one or more classes have fewer records than
        the requested sample size, the sample size is assigned as outlined below

        :param n_per_label: The number of records per distinct class/label
        :return:
        """

        if (not self.__settings.replace) & (n_per_label.min() < self.__settings.class_sample_size):
            class_sample_size = n_per_label.min()
            self.__logger.info(f'Case: Sampling with replacement.\n\nNote, the sample size per '
                               f'class will be {class_sample_size}, i.e., the '
                               f'sample size of the smallest class because it has fewer '
                               f'images than the requested sample '
                               f'size per class; {self.__settings.class_sample_size}.  Altogether, '
                               f'this ensures a balanced data set.')
        else:
            class_sample_size = self.__settings.class_sample_size

        return class_sample_size

    def __excerpt(self, register: pd.DataFrame, class_sample_size: int) -> pd.DataFrame:
        """

        :param register:
        :param class_sample_size:
        :return:
        """

        # Hence
        excerpt = register.groupby(self.__metadata.labels)[self.__metadata.fields + self.__metadata.labels] \
            .apply(lambda x: x.sample(n=class_sample_size, replace=self.__settings.replace,
                                      random_state=self.__settings.random_state))
        excerpt.reset_index(drop=True, inplace=True)

        return excerpt

    def exc(self, register: pd.DataFrame) -> pd.DataFrame:
        """

        :param register: The images register
        :return:
            A sample of the register
        """

        # __sample_size()
        n_per_label: pd.Series = register[self.__metadata.labels].sum(axis=0)
        class_sample_size: int = self.__sample_size(n_per_label)

        # The sample
        excerpt = self.__excerpt(register=register, class_sample_size=class_sample_size)

        return excerpt
