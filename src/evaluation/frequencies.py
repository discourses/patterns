"""
Error matrix frequencies
"""
import dask
import numpy as np
import pandas as pd


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

        self.thresholds = thresholds
        self.plausibilities = plausibilities
        self.truth = truth
        self.classes = classes

    def constraints(self, threshold: float) -> np.ndarray:
        """

        :param threshold:
        :return:
        """

        plausible: np.ndarray = np.where(self.plausibilities > threshold, self.plausibilities, 0)

        if plausible.ndim > 1:
            structure = plausible == np.max(plausible, axis=1, keepdims=True, initial=0)
        else:
            structure = plausible > threshold

        return (structure & (plausible > 0)).astype(int)

    def elements(self, threshold: float, instances: np.ndarray, segment: str):
        """
        
        :param threshold:
        :param instances:
        :param segment:
        :return:
        """

        if instances.ndim == 1:
            instances = instances[:, None]

        npc = instances.sum(axis=0, keepdims=True).squeeze(axis=0).tolist()

        return tuple(j for i in (threshold, tuple(npc), segment)
                     for j in (i if isinstance(i, tuple) else (i,)))

    @dask.delayed
    def true_positive(self, threshold: float) -> tuple:
        """

        :param threshold:
        :return:
        """

        prediction = self.constraints(threshold)
        instances = ((self.truth == prediction) & (self.truth == 1)).astype(int)

        return self.elements(threshold=threshold, instances=instances,  segment='tp')

    @dask.delayed
    def true_negative(self, threshold: float) -> tuple:
        """

        :param threshold:
        :return:
        """

        prediction = self.constraints(threshold)
        instances = ((self.truth == prediction) & (self.truth == 0)).astype(int)

        return self.elements(threshold=threshold, instances=instances,  segment='tn')

    @dask.delayed
    def false_positive(self, threshold: float) -> tuple:
        """

        :param threshold:
        :return:
        """

        prediction = self.constraints(threshold)
        instances = ((prediction == 1) & (self.truth == 0)).astype(int)

        return self.elements(threshold=threshold, instances=instances,  segment='fp')

    @dask.delayed
    def false_negative(self, threshold: float) -> tuple:
        """

        :param threshold:
        :return:
        """

        prediction = self.constraints(threshold)
        instances = ((prediction == 0) & (self.truth == 1)).astype(int)

        return self.elements(threshold=threshold, instances=instances,  segment='fn')

    @dask.delayed
    def frame(self, elements: tuple) -> pd.DataFrame:
        """

        :param elements:
        :return:
        """

        return pd.DataFrame(elements, columns=['threshold'] + self.classes + ['segment'])

    def exc(self) -> pd.DataFrame:
        """

        :return:
        """

        computations = []
        for threshold in self.thresholds:

            tp = self.true_positive(threshold=threshold)
            tn = self.true_negative(threshold=threshold)
            fp = self.false_positive(threshold=threshold)
            fn = self.false_negative(threshold=threshold)
            frame = self.frame(elements=(tp, tn, fp, fn))
            computations.append(frame)

        dask.visualize(computations, filename='error', format='pdf')
        calculations = dask.compute(computations, scheduler='processes')[0]
        data = pd.concat(calculations, axis=0, ignore_index=True)

        return data
