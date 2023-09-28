"""
Determines hyperparameter combinations
"""
import os
import tensorboard.plugins.hparams.api as hp

import src.algorithms.descriptors

import src.elements.hpc


class Hyperparameters:
    """
    Class Hyperparameters

    For the case wherein
        alpha_dropout = hp.HParam('dropout', hp.RealInterval(0.1, 0.3))
    we set/request values via
        for i in [alpha_drop_rate.domain.sample_uniform() for _ in range(n)]
    whereby n is the number of values that should be sampled from the range.
    """

    def __init__(self) -> None:
        """
        
        """

        dictionary = src.algorithms.descriptors.Descriptors(
            path=os.path.join(os.getcwd(), 'data', 'images.yml')).exc(node=['hyperparameters'])

        self.__alpha_units: list[int] = dictionary['alpha_units']
        self.__alpha_dropout: list[float] = dictionary['alpha_dropout']
        self.__beta_units: list[int] = dictionary['beta_units']
        self.__beta_dropout: list[float] = dictionary['beta_dropout']
        self.__opt: list[str] = dictionary['opt']

    def __priors(self) -> (hp.HParam, hp.HParam, hp.HParam, hp.HParam, hp.HParam):
        """
        Initialises the set of values per hyperparameter type
        :return:
        """

        alpha_units: hp.HParam = hp.HParam('num_units', hp.Discrete(self.__alpha_units))
        alpha_dropout = hp.HParam('dropout', hp.Discrete(self.__alpha_dropout))

        beta_units = hp.HParam('num_units', hp.Discrete(self.__beta_units))
        beta_dropout = hp.HParam('dropout', hp.Discrete(self.__beta_dropout))

        opt = hp.HParam('optimizer', hp.Discrete(self.__opt))

        return alpha_units, alpha_dropout, beta_units, beta_dropout, opt

    def exc(self) -> list:
        """
        Creates unique combinations of hyperparameters
        :return:
            combinations: A list of dictionaries, wherein each dictionary is a unique combination
            of hyperparameters.  Each combination estimates a distinct/single model.
        """

        alpha_units, alpha_dropout, beta_units, beta_dropout, opt = self.__priors()

        combinations = [src.elements.hpc.HPC(
            alpha_dropout=i, alpha_units=j, beta_dropout=x, beta_units=y, opt=opt)

            for i in alpha_dropout.domain.values
            for j in alpha_units.domain.values
            for x in beta_dropout.domain.values
            for y in beta_units.domain.values
            for opt in opt.domain.values]
