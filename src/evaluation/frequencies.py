"""
Error matrix frequencies
"""
import dask
import numpy as np
import pandas as pd

import src.evaluation.formulae


class Frequencies:
    """The frequencies class"""

    def __init__(self, thresholds: np.ndarray, plausibilities: np.ndarray, truth: np.ndarray, classes: list):
        """

        :param thresholds:
        :param plausibilities:
        :param truth:
        :param classes: If a multi-class problem, then plausibilities & truth will be matrices, rather
                        than vectors, and each column will represent a class/label/category.  The 'classes' list
                        is the name of each column w.r.t. the encoded order in plausibilities & truth.

        """

        self.__thresholds = thresholds
        self.__truth = truth
        self.__classes = classes

        self.__formulae = src.evaluation.formulae.Formulae(plausibilities=plausibilities)

    @dask.delayed
    def true_positive(self, threshold: float) -> tuple:
        """

        :param threshold:
        :return:
        """

        prediction = self.__formulae.constraints(threshold)
        instances = ((self.__truth == prediction) & (self.__truth == 1)).astype(int)

        return self.__formulae.elements(threshold=threshold, instances=instances,  segment='tp')

    @dask.delayed
    def true_negative(self, threshold: float) -> tuple:
        """

        :param threshold:
        :return:
        """

        prediction = self.__formulae.constraints(threshold)
        instances = ((self.__truth == prediction) & (self.__truth == 0)).astype(int)

        return self.__formulae.elements(threshold=threshold, instances=instances,  segment='tn')

    @dask.delayed
    def false_positive(self, threshold: float) -> tuple:
        """

        :param threshold:
        :return:
        """

        prediction = self.__formulae.constraints(threshold)
        instances = ((prediction == 1) & (self.__truth == 0)).astype(int)

        return self.__formulae.elements(threshold=threshold, instances=instances,  segment='fp')

    @dask.delayed
    def false_negative(self, threshold: float) -> tuple:
        """

        :param threshold:
        :return:
        """

        prediction = self.__formulae.constraints(threshold)
        instances = ((prediction == 0) & (self.__truth == 1)).astype(int)

        return self.__formulae.elements(threshold=threshold, instances=instances,  segment='fn')

    @dask.delayed
    def frame(self, elements: tuple) -> pd.DataFrame:
        """

        :param elements:
        :return:
        """

        return pd.DataFrame(elements, columns=['threshold'] + self.__classes + ['segment'])

    def exc(self) -> pd.DataFrame:
        """

        :return:
        """

        computations = []
        for threshold in self.__thresholds:

            tpv = self.true_positive(threshold=threshold)
            tnv = self.true_negative(threshold=threshold)
            fpv = self.false_positive(threshold=threshold)
            fnv = self.false_negative(threshold=threshold)
            frame = self.frame(elements=(tpv, tnv, fpv, fnv))
            computations.append(frame)

        dask.visualize(computations, filename='error', format='pdf')
        calculations = dask.compute(computations, scheduler='processes')[0]
        data = pd.concat(calculations, axis=0, ignore_index=True)

        return data
