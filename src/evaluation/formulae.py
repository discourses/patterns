"""
The Frequencies class formulae 
"""
import numpy as np


class Formulae:
    """
    Class Formulae
    """

    def __init__(self, plausibilities: np.ndarray) -> None:
        """
        
        :param plausibilities: Each instance, row, of this matrix records the plausibility that an 
                               image belongs to a class.  Each column represents a distinct class.
        :return:
        """

        self.__plausibilities = plausibilities

    def constraints(self, threshold: float) -> np.ndarray:
        """

        :param threshold: A classification threshold
        :return:
        """

        plausible: np.ndarray = np.where(self.__plausibilities > threshold, self.__plausibilities, 0)

        if plausible.ndim > 1:
            structure = plausible == np.max(plausible, axis=1, keepdims=True, initial=0)
        else:
            structure = plausible > threshold

        return (structure & (plausible > 0)).astype(int)

    def elements(self, threshold: float, instances: np.ndarray, segment: str) -> tuple:
        """
        
        :param threshold: A classification threshold
        :param instances: The instances w.r.t. (with respect to) an error matrix frequency calculation
        :param segment: Either tp (true positive), tn (true negative), fp (false postive), or fn (false negative)
        :return:
        """

        if instances.ndim == 1:
            instances = instances[:, None]

        npc = instances.sum(axis=0, keepdims=True).squeeze(axis=0).tolist()

        return tuple(j for i in (threshold, tuple(npc), segment)
                     for j in (i if isinstance(i, tuple) else (i,)))
